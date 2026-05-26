"""
config.py - 設定・環境変数管理モジュール

.env ファイルから設定を読み込み、アプリ全体で使用する定数を定義します。
"""

import os
import logging
from dotenv import load_dotenv

# .env ファイルを読み込む
load_dotenv()

# ============================================================
# ログ設定
# ============================================================
def setup_logging():
    """アプリケーション全体のログ設定を初期化する"""
    log_format = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    logging.basicConfig(
        level=logging.DEBUG,
        format=log_format,
        handlers=[
            logging.StreamHandler(),  # コンソール出力
        ]
    )
    # 外部ライブラリのログを WARNING 以上に制限（ノイズ削減）
    logging.getLogger("googleapiclient").setLevel(logging.WARNING)
    logging.getLogger("google.auth").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("linebot").setLevel(logging.WARNING)
    logging.getLogger("apscheduler").setLevel(logging.INFO)


# ============================================================
# LINE API 設定
# ============================================================
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", "")
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET", "")
LINE_GROUP_ID = os.getenv("LINE_GROUP_ID", "")

# ============================================================
# Gemini API 設定
# ============================================================
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-1.5-flash"  # 高速・低コストモデル

# ============================================================
# Google Sheets 設定
# ============================================================
GOOGLE_SHEETS_ID = os.getenv("GOOGLE_SHEETS_ID", "")
GOOGLE_SERVICE_ACCOUNT_JSON = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON", "service_account.json")

# Google Sheets API のスコープ
GOOGLE_SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

# スプレッドシートのシート名と列定義
SHEET_NAME = "tasks"
SHEET_COLUMNS = {
    "登録日時": 0,
    "依頼者": 1,
    "担当": 2,
    "内容": 3,
    "期限": 4,
    "状態": 5,
}
# ヘッダー行（1行目）のデータ
SHEET_HEADERS = ["登録日時", "依頼者", "担当", "内容", "期限", "状態"]

# ============================================================
# Flask 設定
# ============================================================
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "numb-task-system-secret")
FLASK_DEBUG = os.getenv("FLASK_DEBUG", "False").lower() == "true"
FLASK_PORT = int(os.getenv("FLASK_PORT", "5000"))

# ============================================================
# タイムゾーン・スケジューラー設定
# ============================================================
TIMEZONE = os.getenv("TIMEZONE", "Asia/Tokyo")
MORNING_NOTIFICATION_HOUR = int(os.getenv("MORNING_NOTIFICATION_HOUR", "8"))
MORNING_NOTIFICATION_MINUTE = int(os.getenv("MORNING_NOTIFICATION_MINUTE", "0"))

# ============================================================
# 設定バリデーション
# ============================================================
def validate_config():
    """必須の環境変数が設定されているか確認する"""
    logger = logging.getLogger(__name__)
    missing = []

    required_vars = {
        "LINE_CHANNEL_ACCESS_TOKEN": LINE_CHANNEL_ACCESS_TOKEN,
        "LINE_CHANNEL_SECRET": LINE_CHANNEL_SECRET,
        "LINE_GROUP_ID": LINE_GROUP_ID,
        "GEMINI_API_KEY": GEMINI_API_KEY,
        "GOOGLE_SHEETS_ID": GOOGLE_SHEETS_ID,
    }

    for var_name, value in required_vars.items():
        if not value:
            missing.append(var_name)

    if missing:
        logger.error(f"必須の環境変数が未設定です: {', '.join(missing)}")
        logger.error(".env ファイルを確認してください（.env.example を参照）")
        return False

    logger.info("設定バリデーション: すべての必須環境変数が設定されています")
    return True
