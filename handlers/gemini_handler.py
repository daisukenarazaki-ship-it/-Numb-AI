"""
gemini_handler.py - Gemini AI 判定モジュール

LINE メッセージをGemini AIで解析し、アクションと必要情報を抽出します。
action: "new_task" / "complete" / "ask" / "none"
"""

import json
import logging
import re

from google import genai
from google.genai import types

import config
from utils.date_converter import extract_date_from_text, get_today_jst

logger = logging.getLogger(__name__)

# Gemini クライアントを初期化
_client = None


def get_client() -> genai.Client:
    """Gemini クライアントのシングルトンインスタンスを返す"""
    global _client
    if _client is None:
        _client = genai.Client(api_key=config.GEMINI_API_KEY)
    return _client


def build_prompt(sender_name: str, message_text: str, pending_tasks: list) -> str:
    """
    Gemini に送るプロンプトを構築する。

    Args:
        sender_name: 発言者の名前
        message_text: メッセージ本文
        pending_tasks: 未完了タスク一覧（[{"内容": str, "担当": str}, ...]）

    Returns:
        Gemini に送るプロンプト文字列
    """
    today = get_today_jst()
    today_str = today.strftime("%Y年%m月%d日")
    tomorrow = today.replace(day=today.day + 1) if today.day < 28 else today

    # 未完了タスク一覧をテキスト化
    if pending_tasks:
        tasks_text = "\n".join(
            [f"- {t.get('内容', '')}（担当: {t.get('担当', '')}、期限: {t.get('期限', '')}）"
             for t in pending_tasks]
        )
    else:
        tasks_text = "（なし）"

    prompt = f"""あなたは飲食店「Numb」のタスク管理アシスタントです。
以下のLINEメッセージを解析して、適切なJSONを返してください。

## 入力情報
- 発言者: {sender_name}
- 今日の日付: {today_str}
- メッセージ: {message_text}

## 現在の未完了タスク一覧
{tasks_text}

## 判定ルール

### 1. new_task（タスク登録）
以下のキーワードやパターンが含まれる場合:
- 「タスク」「お願い」「依頼」「やって」「追加」「登録」「まで」「までに」
- 期限が含まれている場合
- 誰かに何かを依頼するニュアンスの場合
- 「〜があるんで」「〜を対応して」「〜を準備して」など

### 2. complete（タスク完了）
以下のキーワードが含まれる場合:
- 「完了」「終わった」「終了」「やった」「やっといた」「済み」「できました」
- 「完成」「片付いた」「対応済み」「済んだ」「終わりました」「done」

### 3. ask（確認が必要）
- 完了らしいが、どのタスクか特定できない場合
- 候補が複数ある場合

### 4. none（無視）
- 通常の会話
- 挨拶
- タスクに関係しない発言

## 出力フォーマット（JSONのみ、説明文不要、コードブロック不要）

new_task の場合:
{{"action": "new_task", "tasks": [{{"依頼者": "発言者名", "担当": "担当者名", "内容": "タスク内容", "期限": "YYYY/MM/DD"}}]}}

complete の場合:
{{"action": "complete", "対象": "完了したタスクの内容"}}

ask の場合:
{{"action": "ask", "候補": ["タスク内容1", "タスク内容2"]}}

none の場合:
{{"action": "none"}}

## 重要なルール
- 依頼者は発言者（{sender_name}）
- 担当は @メンションや「〇〇さん」「〇〇くん」から抽出。不明な場合は発言者名
- 期限は YYYY/MM/DD 形式に変換すること（今日={today_str}、明日={tomorrow.strftime("%Y/%m/%d")}）
- complete の場合は未完了タスク一覧から最も近いものを選ぶ
- JSONのみを返すこと（コードブロックや説明文は不要）
"""
    return prompt


def analyze_message(sender_name: str, message_text: str, pending_tasks: list) -> dict:
    """
    Gemini AI でメッセージを解析し、アクションと必要情報を返す。

    Args:
        sender_name: 発言者名
        message_text: メッセージ本文
        pending_tasks: 未完了タスク一覧

    Returns:
        解析結果の辞書（action フィールドを含む）
    """
    logger.info(f"Gemini 解析開始 - 発言者: {sender_name}, メッセージ: {message_text[:50]}...")

    try:
        client = get_client()
        prompt = build_prompt(sender_name, message_text, pending_tasks)

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.1,
                max_output_tokens=1024,
            ),
        )

        response_text = response.text.strip()
        logger.debug(f"Gemini レスポンス: {response_text}")

        # コードブロックが含まれる場合に JSON 部分を抽出
        json_text = extract_json(response_text)
        result = json.loads(json_text)
        action = result.get("action", "none")
        logger.info(f"Gemini 判定結果: action={action}")

        # new_task の場合、期限を正規化する
        if action == "new_task" and "tasks" in result:
            for task in result["tasks"]:
                if "期限" in task and task["期限"]:
                    task["期限"] = extract_date_from_text(task["期限"])

        return result

    except json.JSONDecodeError as e:
        logger.error(f"Gemini レスポンスの JSON パース失敗: {e}")
        return {"action": "none"}

    except Exception as e:
        logger.error(f"Gemini API エラー: {e}", exc_info=True)
        return {"action": "none"}


def extract_json(text: str) -> str:
    """
    テキストから JSON 部分を抽出する。
    コードブロック（```json ... ```）で囲まれている場合にも対応。
    """
    text = re.sub(r"```json\s*", "", text)
    text = re.sub(r"```\s*", "", text)
    text = text.strip()

    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return match.group(0)

    return text
