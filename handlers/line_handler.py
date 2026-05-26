"""
line_handler.py - LINE メッセージ処理モジュール

LINE Webhook から受け取ったイベントを処理し、
Gemini AI による判定 → Google Sheets 操作 → LINE 返信 の流れを管理します。
"""

import hashlib
import hmac
import logging
import base64
from typing import Optional

from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.messaging import (
    ApiClient,
    Configuration,
    MessagingApi,
    ReplyMessageRequest,
    PushMessageRequest,
    TextMessage,
)
from linebot.v3.webhooks import MessageEvent, TextMessageContent, GroupSource

import config
from handlers import gemini_handler
from handlers.sheets_handler import get_sheets_handler

logger = logging.getLogger(__name__)

# LINE SDK の設定
_line_configuration = Configuration(access_token=config.LINE_CHANNEL_ACCESS_TOKEN)
_webhook_handler = WebhookHandler(config.LINE_CHANNEL_SECRET)


def get_webhook_handler() -> WebhookHandler:
    """WebhookHandler インスタンスを返す"""
    return _webhook_handler


def verify_signature(body: bytes, x_line_signature: str) -> bool:
    """
    LINE の HMAC-SHA256 署名を検証する。
    セキュリティ上、必ずこの検証を通過させること。

    Args:
        body: リクエストのバイトボディ
        x_line_signature: X-Line-Signature ヘッダーの値

    Returns:
        署名が正しければ True
    """
    channel_secret = config.LINE_CHANNEL_SECRET.encode("utf-8")
    hash_digest = hmac.new(channel_secret, body, hashlib.sha256).digest()
    expected_signature = base64.b64encode(hash_digest).decode("utf-8")

    is_valid = hmac.compare_digest(expected_signature, x_line_signature)
    if not is_valid:
        logger.warning("LINE 署名検証失敗 - 不正なリクエストの可能性があります")
    return is_valid


def reply_message(reply_token: str, text: str) -> bool:
    """
    LINE リプライ API でメッセージを送信する。

    Args:
        reply_token: Webhook イベントのリプライトークン
        text: 送信するメッセージテキスト

    Returns:
        成功時 True
    """
    try:
        with ApiClient(_line_configuration) as api_client:
            line_bot_api = MessagingApi(api_client)
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=reply_token,
                    messages=[TextMessage(text=text)],
                )
            )
        logger.info(f"リプライ送信成功: {text[:50]}...")
        return True
    except Exception as e:
        logger.error(f"リプライ送信エラー: {e}", exc_info=True)
        return False


def push_message(group_id: str, text: str) -> bool:
    """
    LINE Push API でグループにメッセージを送信する。
    スケジューラーからの朝の通知などに使用します。

    Args:
        group_id: 送信先グループ ID
        text: 送信するメッセージテキスト

    Returns:
        成功時 True
    """
    try:
        with ApiClient(_line_configuration) as api_client:
            line_bot_api = MessagingApi(api_client)
            line_bot_api.push_message(
                PushMessageRequest(
                    to=group_id,
                    messages=[TextMessage(text=text)],
                )
            )
        logger.info(f"プッシュメッセージ送信成功: {text[:50]}...")
        return True
    except Exception as e:
        logger.error(f"プッシュメッセージ送信エラー: {e}", exc_info=True)
        return False


def handle_message_event(event: MessageEvent) -> None:
    """
    テキストメッセージイベントを処理するメイン関数。

    フロー:
    1. 送信者名を取得
    2. 未完了タスクを取得
    3. Gemini AI でメッセージを解析
    4. アクションに応じた処理を実行
    5. LINE リプライを送信

    Args:
        event: LINE Webhook のメッセージイベント
    """
    # テキストメッセージのみ処理
    if not isinstance(event.message, TextMessageContent):
        return

    message_text = event.message.text
    reply_token = event.reply_token

    # 送信者名を取得（プロフィール情報は別 API コールが必要なため暫定値）
    sender_name = _get_sender_name(event)

    logger.info(f"メッセージ受信 - 送信者: {sender_name}, 内容: {message_text[:80]}")

    # Google Sheets から未完了タスクを取得（Gemini の判定精度向上のため）
    sheets = get_sheets_handler()
    pending_tasks = sheets.get_pending_tasks()

    # Gemini AI でメッセージを解析
    analysis = gemini_handler.analyze_message(sender_name, message_text, pending_tasks)
    action = analysis.get("action", "none")

    logger.info(f"アクション実行: {action}")

    # アクションに応じた処理
    if action == "new_task":
        _handle_new_task(reply_token, analysis, sender_name, sheets)
    elif action == "complete":
        _handle_complete(reply_token, analysis, sheets)
    elif action == "ask":
        _handle_ask(reply_token, analysis)
    else:
        # none: 返信しない
        logger.debug("action=none: 返信しません")


def _get_sender_name(event: MessageEvent) -> str:
    """
    イベントから送信者名を取得する。
    グループトークではユーザー ID のみ取得できるため、
    実際の名前は LINE Profile API（別途コール）が必要。
    ここでは "ユーザー" をデフォルト値とします。

    Args:
        event: LINE Webhook イベント

    Returns:
        送信者名
    """
    try:
        if event.source and hasattr(event.source, "user_id"):
            user_id = event.source.user_id
            # ユーザープロフィールを取得（グループメンバー向け）
            if isinstance(event.source, GroupSource):
                group_id = event.source.group_id
                with ApiClient(_line_configuration) as api_client:
                    line_bot_api = MessagingApi(api_client)
                    profile = line_bot_api.get_group_member_profile(
                        group_id=group_id,
                        user_id=user_id,
                    )
                    return profile.display_name
            else:
                with ApiClient(_line_configuration) as api_client:
                    line_bot_api = MessagingApi(api_client)
                    profile = line_bot_api.get_profile(user_id=user_id)
                    return profile.display_name
    except Exception as e:
        logger.warning(f"送信者名取得エラー（デフォルト値を使用）: {e}")
    return "ユーザー"


def _handle_new_task(
    reply_token: str,
    analysis: dict,
    sender_name: str,
    sheets,
) -> None:
    """
    new_task アクション: Google Sheets にタスクを追加して返信する。

    Args:
        reply_token: LINE リプライトークン
        analysis: Gemini の解析結果
        sender_name: 発言者名
        sheets: SheetsHandler インスタンス
    """
    tasks = analysis.get("tasks", [])
    if not tasks:
        reply_message(reply_token, "⚠️ タスクの情報を取得できませんでした。もう少し詳しく教えてください。")
        return

    success_count = 0
    reply_lines = []

    for task in tasks:
        依頼者 = task.get("依頼者", sender_name) or sender_name
        担当 = task.get("担当", sender_name) or sender_name
        内容 = task.get("内容", "")
        期限 = task.get("期限", "")

        if not 内容:
            logger.warning("タスク内容が空のためスキップ")
            continue

        success = sheets.add_task(
            依頼者=依頼者,
            担当=担当,
            内容=内容,
            期限=期限,
        )

        if success:
            success_count += 1
            detail = f"【{担当}】{内容}"
            if 期限:
                detail += f"（期限: {期限}）"
            reply_lines.append(detail)

    if success_count > 0:
        tasks_summary = "\n".join(f"・{line}" for line in reply_lines)
        reply_text = f"✅ タスクを登録しました\n\n{tasks_summary}"
    else:
        reply_text = "⚠️ タスクの登録に失敗しました。しばらく後でもう一度お試しください。"

    reply_message(reply_token, reply_text)


def _handle_complete(reply_token: str, analysis: dict, sheets) -> None:
    """
    complete アクション: タスクを完了状態に更新して返信する。

    Args:
        reply_token: LINE リプライトークン
        analysis: Gemini の解析結果
        sheets: SheetsHandler インスタンス
    """
    target = analysis.get("対象", "")

    if not target:
        reply_message(reply_token, "⚠️ 完了するタスクを特定できませんでした。タスク名を具体的に教えてください。")
        return

    updated_task = sheets.complete_task(target)

    if updated_task:
        task_name = updated_task.get("内容", target)
        reply_text = f"✅『{task_name}』を完了にしました！"
    else:
        # 見つからない場合は現在のタスク一覧を提示
        pending = sheets.get_pending_tasks()
        if pending:
            task_list = "\n".join(
                [f"・{t['内容']}（担当: {t['担当']}）" for t in pending[:5]]
            )
            reply_text = f"⚠️ 対象のタスクが見つかりませんでした。\n\n現在の未完了タスク:\n{task_list}"
        else:
            reply_text = "⚠️ 対象のタスクが見つかりませんでした。現在未完了のタスクはありません。"

    reply_message(reply_token, reply_text)


def _handle_ask(reply_token: str, analysis: dict) -> None:
    """
    ask アクション: どのタスクか確認するメッセージを返信する。

    Args:
        reply_token: LINE リプライトークン
        analysis: Gemini の解析結果
    """
    candidates = analysis.get("候補", [])

    if candidates:
        candidate_list = "\n".join([f"・{c}" for c in candidates])
        reply_text = f"どのタスクの完了ですか？\n\n{candidate_list}"
    else:
        reply_text = "どのタスクの完了ですか？タスク名を教えてください。"

    reply_message(reply_token, reply_text)
