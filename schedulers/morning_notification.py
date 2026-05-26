"""
morning_notification.py - 朝の通知スケジューラー

毎日朝 8:00 (Asia/Tokyo) に未完了タスク一覧を LINE グループに送信します。
APScheduler を使用してバックグラウンドで実行されます。
"""

import logging
from datetime import datetime

import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

import config
from handlers.sheets_handler import get_sheets_handler
from handlers.line_handler import push_message

logger = logging.getLogger(__name__)

JST = pytz.timezone("Asia/Tokyo")


def build_morning_message(tasks: list) -> str:
    """
    朝の通知メッセージを組み立てる。

    Args:
        tasks: 未完了タスクのリスト

    Returns:
        送信するメッセージテキスト
    """
    today = datetime.now(JST).strftime("%m月%d日")
    header = f"📋 {today} 本日のタスク"

    if not tasks:
        return f"{header}\n\n未完了のタスクはありません 🎉\n\n今日もよろしくお願いします！"

    task_lines = []
    # 数字絵文字マッピング（1〜10）
    number_emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣",
                     "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

    for i, task in enumerate(tasks):
        emoji = number_emojis[i] if i < len(number_emojis) else f"{i+1}."
        担当 = task.get("担当", "未定")
        内容 = task.get("内容", "")
        期限 = task.get("期限", "")

        line = f"{emoji} 【{担当}】{内容}"
        if 期限:
            line += f"（期限: {期限}）"
        task_lines.append(line)

    tasks_text = "\n".join(task_lines)
    return f"{header}\n\n{tasks_text}\n\n今日もよろしくお願いします！"


def send_morning_notification() -> None:
    """
    朝の通知を実行する関数。
    スケジューラーから定期的に呼び出されます。
    """
    logger.info("朝の通知処理を開始します")

    try:
        # Google Sheets から未完了タスクを取得
        sheets = get_sheets_handler()
        pending_tasks = sheets.get_pending_tasks()

        logger.info(f"未完了タスク数: {len(pending_tasks)}")

        # メッセージを組み立てて送信
        message = build_morning_message(pending_tasks)
        success = push_message(config.LINE_GROUP_ID, message)

        if success:
            logger.info("朝の通知送信完了")
        else:
            logger.error("朝の通知送信失敗")

    except Exception as e:
        logger.error(f"朝の通知処理エラー: {e}", exc_info=True)


def create_scheduler() -> BackgroundScheduler:
    """
    APScheduler のスケジューラーを作成・設定する。

    Returns:
        設定済みの BackgroundScheduler インスタンス
    """
    scheduler = BackgroundScheduler(
        timezone=JST,
        job_defaults={
            "coalesce": False,        # 同時実行しない
            "max_instances": 1,       # 最大1インスタンス
            "misfire_grace_time": 60, # 1分以内の遅延は許容
        }
    )

    # 毎日朝の通知ジョブを追加
    scheduler.add_job(
        func=send_morning_notification,
        trigger=CronTrigger(
            hour=config.MORNING_NOTIFICATION_HOUR,
            minute=config.MORNING_NOTIFICATION_MINUTE,
            timezone=JST,
        ),
        id="morning_notification",
        name="朝のタスク通知",
        replace_existing=True,
    )

    logger.info(
        f"スケジューラー設定完了: 毎日 "
        f"{config.MORNING_NOTIFICATION_HOUR:02d}:{config.MORNING_NOTIFICATION_MINUTE:02d} "
        f"(JST) に通知"
    )

    return scheduler


def start_scheduler() -> BackgroundScheduler:
    """
    スケジューラーを起動する。

    Returns:
        起動済みの BackgroundScheduler インスタンス
    """
    scheduler = create_scheduler()
    scheduler.start()
    logger.info("スケジューラー起動完了")
    return scheduler
