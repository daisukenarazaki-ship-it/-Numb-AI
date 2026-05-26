"""
main.py - Numb タスク管理システム メインアプリケーション

Flask サーバーのエントリーポイント。
LINE Webhook を受け取り、AI 判定 → Google Sheets 操作 → LINE 返信を行います。
"""

import logging
import sys

from flask import Flask, request, abort

from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.webhooks import MessageEvent, TextMessageContent

import config
from config import setup_logging, validate_config
from handlers.line_handler import (
    get_webhook_handler,
    handle_message_event,
    verify_signature,
)
from schedulers.morning_notification import start_scheduler

# ログ設定を最初に初期化
setup_logging()
logger = logging.getLogger(__name__)

# Flask アプリを作成
app = Flask(__name__)
app.secret_key = config.FLASK_SECRET_KEY

# LINE Webhook ハンドラーを取得
handler = get_webhook_handler()


# ============================================================
# LINE Webhook エンドポイント
# ============================================================
@app.route("/callback", methods=["POST"])
def callback():
    """
    LINE Platform から Webhook イベントを受け取るエンドポイント。

    セキュリティ:
    - X-Line-Signature ヘッダーで HMAC-SHA256 署名を検証
    - 署名が無効な場合は 403 を返す
    """
    # 署名検証
    x_line_signature = request.headers.get("X-Line-Signature", "")
    body = request.get_data()

    if not x_line_signature:
        logger.warning("X-Line-Signature ヘッダーがありません")
        abort(400, "Missing X-Line-Signature header")

    # カスタム署名検証（念のため二重確認）
    if not verify_signature(body, x_line_signature):
        logger.warning("署名検証失敗 - 不正なリクエストを拒否しました")
        abort(403, "Invalid signature")

    # LINE SDK の署名検証 + イベント処理
    try:
        handler.handle(body.decode("utf-8"), x_line_signature)
    except InvalidSignatureError:
        logger.warning("LINE SDK 署名検証失敗")
        abort(403, "Invalid signature")
    except Exception as e:
        logger.error(f"Webhook 処理エラー: {e}", exc_info=True)
        # LINE サーバーには 200 を返して再送を防ぐ
        return "Internal Error", 200

    return "OK", 200


# ============================================================
# LINE SDK イベントハンドラー登録
# ============================================================
@handler.add(MessageEvent, message=TextMessageContent)
def on_message(event: MessageEvent):
    """テキストメッセージイベントのハンドラー"""
    try:
        handle_message_event(event)
    except Exception as e:
        logger.error(f"メッセージ処理エラー: {e}", exc_info=True)


# ============================================================
# ヘルスチェックエンドポイント
# ============================================================
@app.route("/health", methods=["GET"])
def health_check():
    """サーバーの稼働確認用エンドポイント"""
    return {"status": "ok", "service": "Numb Task System"}, 200


@app.route("/", methods=["GET"])
def index():
    """ルートエンドポイント"""
    return {"message": "Numb タスク管理システム稼働中"}, 200


# ============================================================
# アプリケーション起動
# ============================================================
def main():
    """メインエントリーポイント"""
    logger.info("=" * 60)
    logger.info("Numb タスク管理システム 起動中...")
    logger.info("=" * 60)

    # 設定バリデーション
    if not validate_config():
        logger.error("設定エラーのため起動を中止します")
        logger.error(".env ファイルを確認してください（.env.example を参照）")
        sys.exit(1)

    # 朝の通知スケジューラーを起動
    logger.info("スケジューラーを起動中...")
    scheduler = start_scheduler()

    logger.info(f"Flask サーバーを起動中... ポート: {config.FLASK_PORT}")
    logger.info(f"Webhook URL: http://localhost:{config.FLASK_PORT}/callback")
    logger.info("ngrok などで外部公開して LINE Webhook URL に設定してください")
    logger.info("=" * 60)

    try:
        app.run(
            host="0.0.0.0",
            port=config.FLASK_PORT,
            debug=config.FLASK_DEBUG,
            use_reloader=False,  # スケジューラーの二重起動を防ぐ
        )
    except KeyboardInterrupt:
        logger.info("シャットダウン中...")
    finally:
        scheduler.shutdown(wait=False)
        logger.info("Numb タスク管理システム 停止しました")


if __name__ == "__main__":
    main()
