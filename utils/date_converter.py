"""
date_converter.py - 日付変換ユーティリティ

「明日」「今週金曜」「5月10日」などの自然言語日付を
YYYY/MM/DD 形式に変換します。
"""

import re
import logging
from datetime import datetime, timedelta
import pytz

logger = logging.getLogger(__name__)

JST = pytz.timezone("Asia/Tokyo")

# 曜日の日本語→数値マッピング（月=0, 日=6）
WEEKDAY_MAP = {
    "月": 0, "火": 1, "水": 2, "木": 3, "金": 4, "土": 5, "日": 6,
    "月曜": 0, "火曜": 1, "水曜": 2, "木曜": 3, "金曜": 4, "土曜": 5, "日曜": 6,
    "月曜日": 0, "火曜日": 1, "水曜日": 2, "木曜日": 3, "金曜日": 4, "土曜日": 5, "日曜日": 6,
}


def get_today_jst() -> datetime:
    """日本時間の今日の日付を返す"""
    return datetime.now(JST).replace(hour=0, minute=0, second=0, microsecond=0)


def convert_date_expression(text: str) -> str:
    """
    日本語の日付表現を YYYY/MM/DD 形式に変換する。

    Args:
        text: 変換対象のテキスト（例: "明日", "5月10日", "今週金曜"）

    Returns:
        YYYY/MM/DD 形式の日付文字列、変換できない場合は空文字列
    """
    if not text:
        return ""

    text = text.strip()
    today = get_today_jst()

    # --- 相対日付表現 ---
    if text in ("今日", "本日"):
        return today.strftime("%Y/%m/%d")

    if text in ("明日", "あした", "あす"):
        return (today + timedelta(days=1)).strftime("%Y/%m/%d")

    if text in ("明後日", "あさって"):
        return (today + timedelta(days=2)).strftime("%Y/%m/%d")

    if text in ("今週末", "週末"):
        # 今週の土曜日
        days_to_saturday = (5 - today.weekday()) % 7
        if days_to_saturday == 0:
            days_to_saturday = 7
        return (today + timedelta(days=days_to_saturday)).strftime("%Y/%m/%d")

    # 「今週〇曜日」パターン
    match = re.match(r"今週(.+)", text)
    if match:
        weekday_str = match.group(1).rstrip("日")
        if weekday_str in WEEKDAY_MAP:
            target_weekday = WEEKDAY_MAP[weekday_str]
            days_ahead = (target_weekday - today.weekday()) % 7
            if days_ahead == 0:
                days_ahead = 7  # 同じ曜日なら来週
            result = today + timedelta(days=days_ahead)
            return result.strftime("%Y/%m/%d")

    # 「来週〇曜日」パターン
    match = re.match(r"来週(.+)", text)
    if match:
        weekday_str = match.group(1).rstrip("日")
        if weekday_str in WEEKDAY_MAP:
            target_weekday = WEEKDAY_MAP[weekday_str]
            days_ahead = (target_weekday - today.weekday()) % 7 + 7
            result = today + timedelta(days=days_ahead)
            return result.strftime("%Y/%m/%d")

    # 「〇曜日」「〇曜」パターン（今週の該当曜日、過ぎていたら来週）
    for weekday_str, weekday_num in WEEKDAY_MAP.items():
        if text == weekday_str or text == weekday_str + "日":
            days_ahead = (weekday_num - today.weekday()) % 7
            if days_ahead == 0:
                days_ahead = 7
            result = today + timedelta(days=days_ahead)
            return result.strftime("%Y/%m/%d")

    # 「〇月〇日」パターン
    match = re.match(r"(\d{1,2})月(\d{1,2})日?", text)
    if match:
        month = int(match.group(1))
        day = int(match.group(2))
        year = today.year
        # 過去の日付なら翌年と判断
        try:
            candidate = datetime(year, month, day, tzinfo=JST)
            if candidate < today:
                candidate = datetime(year + 1, month, day, tzinfo=JST)
            return candidate.strftime("%Y/%m/%d")
        except ValueError:
            logger.warning(f"無効な日付: {month}月{day}日")
            return ""

    # 「YYYY年〇月〇日」パターン
    match = re.match(r"(\d{4})年(\d{1,2})月(\d{1,2})日?", text)
    if match:
        year = int(match.group(1))
        month = int(match.group(2))
        day = int(match.group(3))
        try:
            return datetime(year, month, day).strftime("%Y/%m/%d")
        except ValueError:
            logger.warning(f"無効な日付: {year}年{month}月{day}日")
            return ""

    # 「YYYY/MM/DD」または「YYYY-MM-DD」パターン（すでに整形済み）
    match = re.match(r"(\d{4})[/\-](\d{1,2})[/\-](\d{1,2})", text)
    if match:
        try:
            y, m, d = int(match.group(1)), int(match.group(2)), int(match.group(3))
            return f"{y:04d}/{m:02d}/{d:02d}"
        except ValueError:
            return ""

    # 「MM/DD」パターン
    match = re.match(r"(\d{1,2})/(\d{1,2})$", text)
    if match:
        month = int(match.group(1))
        day = int(match.group(2))
        year = today.year
        try:
            candidate = datetime(year, month, day, tzinfo=JST)
            if candidate < today:
                candidate = datetime(year + 1, month, day, tzinfo=JST)
            return candidate.strftime("%Y/%m/%d")
        except ValueError:
            return ""

    logger.debug(f"日付変換できませんでした: '{text}'")
    return text  # 変換できなかった場合はそのまま返す


def extract_date_from_text(text: str) -> str:
    """
    テキスト中から日付表現を検索して YYYY/MM/DD に変換する。
    Gemini が日付を抽出済みの場合に使用する補助関数。
    """
    if not text:
        return ""

    # すでに YYYY/MM/DD 形式ならそのまま返す
    if re.match(r"^\d{4}/\d{2}/\d{2}$", text):
        return text

    return convert_date_expression(text)
