"""
sheets_handler.py - Google Sheets 連携モジュール

タスクの読み書き・状態更新を Google Sheets API で行います。
認証はサービスアカウント JSON キーファイルを使用します。
"""

import logging
import os
from datetime import datetime
from typing import Optional

import pytz
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import config

logger = logging.getLogger(__name__)

JST = pytz.timezone("Asia/Tokyo")


class SheetsHandler:
    """Google Sheets API を操作するハンドラークラス"""

    def __init__(self):
        self.service = None
        self.spreadsheet_id = config.GOOGLE_SHEETS_ID
        self.sheet_name = config.SHEET_NAME
        self._initialize()

    def _initialize(self):
        """Google Sheets API クライアントを初期化する"""
        try:
            credentials = service_account.Credentials.from_service_account_file(
                config.GOOGLE_SERVICE_ACCOUNT_JSON,
                scopes=config.GOOGLE_SCOPES,
            )
            self.service = build("sheets", "v4", credentials=credentials)
            logger.info("Google Sheets API クライアント初期化完了")

            # シートの存在確認・初期化
            self._ensure_sheet_initialized()

        except FileNotFoundError:
            logger.error(
                f"サービスアカウント JSON ファイルが見つかりません: "
                f"{config.GOOGLE_SERVICE_ACCOUNT_JSON}"
            )
            logger.error("Google Cloud Console でサービスアカウントを作成し、"
                         "JSON キーをダウンロードしてください")
        except Exception as e:
            logger.error(f"Google Sheets API 初期化エラー: {e}", exc_info=True)

    def _ensure_sheet_initialized(self):
        """
        シートの存在を確認し、ヘッダー行がなければ追加する。
        初回実行時に自動でシートを準備します。
        """
        try:
            result = self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range=f"{self.sheet_name}!A1:F1",
            ).execute()

            values = result.get("values", [])
            if not values:
                # ヘッダー行を追加
                self._append_row(config.SHEET_HEADERS)
                logger.info("ヘッダー行を追加しました")
            else:
                logger.debug("シートのヘッダーを確認しました")

        except HttpError as e:
            if e.resp.status == 400:
                # シートが存在しない場合は作成
                logger.info(f"シート '{self.sheet_name}' が存在しないため作成します")
                self._create_sheet()
                self._append_row(config.SHEET_HEADERS)
            else:
                logger.error(f"シート確認エラー: {e}")
        except Exception as e:
            logger.error(f"シート初期化エラー: {e}", exc_info=True)

    def _create_sheet(self):
        """新しいシートを作成する"""
        try:
            body = {
                "requests": [{
                    "addSheet": {
                        "properties": {"title": self.sheet_name}
                    }
                }]
            }
            self.service.spreadsheets().batchUpdate(
                spreadsheetId=self.spreadsheet_id,
                body=body,
            ).execute()
            logger.info(f"シート '{self.sheet_name}' を作成しました")
        except Exception as e:
            logger.error(f"シート作成エラー: {e}", exc_info=True)

    def _append_row(self, row_data: list):
        """シートの末尾に行を追加する"""
        body = {"values": [row_data]}
        self.service.spreadsheets().values().append(
            spreadsheetId=self.spreadsheet_id,
            range=f"{self.sheet_name}!A:F",
            valueInputOption="USER_ENTERED",
            insertDataOption="INSERT_ROWS",
            body=body,
        ).execute()

    def add_task(self, 依頼者: str, 担当: str, 内容: str, 期限: str) -> bool:
        """
        新しいタスクを Google Sheets に追加する。

        Args:
            依頼者: タスクを依頼した人の名前
            担当: タスクを担当する人の名前
            内容: タスクの内容
            期限: 期限（YYYY/MM/DD 形式）

        Returns:
            成功時 True、失敗時 False
        """
        if not self.service:
            logger.error("Google Sheets サービスが初期化されていません")
            return False

        try:
            # 登録日時（JST）
            now = datetime.now(JST).strftime("%Y/%m/%d %H:%M:%S")

            row_data = [now, 依頼者, 担当, 内容, 期限, "未着手"]
            self._append_row(row_data)

            logger.info(f"タスク追加成功: 担当={担当}, 内容={内容}, 期限={期限}")
            return True

        except HttpError as e:
            logger.error(f"Google Sheets API エラー（タスク追加）: {e}")
            return False
        except Exception as e:
            logger.error(f"タスク追加エラー: {e}", exc_info=True)
            return False

    def get_all_tasks(self) -> list:
        """
        全タスクを取得する。

        Returns:
            タスクのリスト（辞書形式）
        """
        if not self.service:
            logger.error("Google Sheets サービスが初期化されていません")
            return []

        try:
            result = self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range=f"{self.sheet_name}!A:F",
            ).execute()

            values = result.get("values", [])
            if len(values) <= 1:
                return []  # ヘッダーのみ or 空

            tasks = []
            headers = values[0]
            for i, row in enumerate(values[1:], start=2):  # 2行目から（行番号は2始まり）
                # 列数が足りない場合は空文字で補完
                while len(row) < len(headers):
                    row.append("")
                task = {
                    "row_index": i,
                    "登録日時": row[0] if len(row) > 0 else "",
                    "依頼者": row[1] if len(row) > 1 else "",
                    "担当": row[2] if len(row) > 2 else "",
                    "内容": row[3] if len(row) > 3 else "",
                    "期限": row[4] if len(row) > 4 else "",
                    "状態": row[5] if len(row) > 5 else "未着手",
                }
                tasks.append(task)

            logger.debug(f"全タスク取得: {len(tasks)} 件")
            return tasks

        except Exception as e:
            logger.error(f"タスク取得エラー: {e}", exc_info=True)
            return []

    def get_pending_tasks(self) -> list:
        """
        未着手・進行中タスクを取得する（状態 = "未着手" or "進行中"）。

        Returns:
            未完了タスクのリスト
        """
        all_tasks = self.get_all_tasks()
        pending = [t for t in all_tasks if t.get("状態", "") in ("未着手", "進行中")]
        logger.debug(f"未完了タスク: {len(pending)} 件")
        return pending

    def complete_task(self, task_content: str) -> Optional[dict]:
        """
        タスクの状態を「完了」に更新する。
        内容フィールドで最も近い（部分一致）タスクを検索します。

        Args:
            task_content: 完了するタスクの内容（Gemini が抽出したテキスト）

        Returns:
            更新したタスクの辞書、見つからない場合は None
        """
        if not self.service:
            logger.error("Google Sheets サービスが初期化されていません")
            return None

        all_tasks = self.get_all_tasks()

        # 完全一致を優先、次に部分一致
        matched_task = None

        # 完全一致検索（状態が未着手・進行中のもの）
        for task in all_tasks:
            if (task["内容"] == task_content
                    and task["状態"] in ("未着手", "進行中")):
                matched_task = task
                break

        # 部分一致検索（完全一致が見つからない場合）
        if not matched_task:
            for task in all_tasks:
                if (task_content in task["内容"] or task["内容"] in task_content):
                    if task["状態"] in ("未着手", "進行中"):
                        matched_task = task
                        break

        if not matched_task:
            logger.warning(f"対象タスクが見つかりません: {task_content}")
            return None

        # 状態を「完了」に更新
        try:
            row_index = matched_task["row_index"]
            # F列（状態）を更新
            range_notation = f"{self.sheet_name}!F{row_index}"
            body = {"values": [["完了"]]}
            self.service.spreadsheets().values().update(
                spreadsheetId=self.spreadsheet_id,
                range=range_notation,
                valueInputOption="USER_ENTERED",
                body=body,
            ).execute()

            logger.info(f"タスク完了更新: {matched_task['内容']} (行 {row_index})")
            return matched_task

        except HttpError as e:
            logger.error(f"タスク完了更新エラー（API）: {e}")
            return None
        except Exception as e:
            logger.error(f"タスク完了更新エラー: {e}", exc_info=True)
            return None


# シングルトンインスタンス（アプリ起動時に一度だけ初期化）
_sheets_handler_instance = None


def get_sheets_handler() -> SheetsHandler:
    """SheetsHandler のシングルトンインスタンスを返す"""
    global _sheets_handler_instance
    if _sheets_handler_instance is None:
        _sheets_handler_instance = SheetsHandler()
    return _sheets_handler_instance
