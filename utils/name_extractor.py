"""
name_extractor.py - 名前抽出ユーティリティ

LINE メッセージから @メンション や「〇〇さん」形式の名前を抽出します。
"""

import re
import logging

logger = logging.getLogger(__name__)


def extract_name_from_mention(text: str) -> str:
    """
    @メンション形式から名前を抽出する。

    Args:
        text: 対象テキスト（例: "@田中 資料作成をお願いします"）

    Returns:
        抽出した名前（例: "田中"）、見つからない場合は空文字列
    """
    # @名前 パターン（スペースまたは文末で終わる）
    match = re.search(r"@([\w　-鿿！-｠]+)", text)
    if match:
        name = match.group(1).strip()
        logger.debug(f"@メンションから名前抽出: {name}")
        return name
    return ""


def extract_name_with_suffix(text: str) -> str:
    """
    「〇〇さん」「〇〇くん」「〇〇ちゃん」形式から名前を抽出する。

    Args:
        text: 対象テキスト（例: "田中さんに資料作成をお願い"）

    Returns:
        抽出した名前（例: "田中"）、見つからない場合は空文字列
    """
    # 「〇〇さん/くん/ちゃん/様」パターン
    suffixes = ["さん", "くん", "ちゃん", "様", "氏"]
    for suffix in suffixes:
        pattern = rf"([぀-ゟ゠-ヿ一-鿿ｦ-ﾟ]+){suffix}"
        match = re.search(pattern, text)
        if match:
            name = match.group(1).strip()
            logger.debug(f"敬称から名前抽出: {name}（{suffix}）")
            return name
    return ""


def normalize_name(name: str) -> str:
    """
    名前から不要な敬称・記号を除去して正規化する。

    Args:
        name: 正規化対象の名前

    Returns:
        正規化された名前
    """
    if not name:
        return ""
    # 敬称を除去
    for suffix in ["さん", "くん", "ちゃん", "様", "氏"]:
        name = name.replace(suffix, "")
    # @ 記号を除去
    name = name.replace("@", "").strip()
    return name


def extract_name(text: str) -> str:
    """
    テキストから名前を抽出するメイン関数。
    @メンション → 敬称の順で試みる。

    Args:
        text: 対象テキスト

    Returns:
        抽出した名前（正規化済み）
    """
    # @メンション形式を優先
    name = extract_name_from_mention(text)
    if name:
        return normalize_name(name)

    # 敬称形式を試みる
    name = extract_name_with_suffix(text)
    if name:
        return normalize_name(name)

    return ""
