#!/usr/bin/env python3
"""
Liberty Cat Instagram Auto Poster
Instagram Graph API を使って自動投稿するスクリプト
"""

import os
import sys
import json
import time
import requests
from pathlib import Path


# ── 設定（環境変数から読み込む） ──────────────────────────
ACCESS_TOKEN   = os.environ.get("IG_ACCESS_TOKEN", "")
IG_USER_ID     = os.environ.get("IG_USER_ID", "")
IMAGE_HOST_URL = os.environ.get("IMAGE_HOST_URL", "")  # 画像を公開URLで渡す場合


def post_photo(image_url: str, caption: str) -> dict:
    """
    フィード写真投稿（1枚）
    image_url: 公開アクセス可能な画像URL（https必須）
    caption:   投稿文 + ハッシュタグ
    """
    # Step 1: メディアオブジェクト作成
    create_url = f"https://graph.facebook.com/v19.0/{IG_USER_ID}/media"
    create_payload = {
        "image_url": image_url,
        "caption": caption,
        "access_token": ACCESS_TOKEN,
    }
    res = requests.post(create_url, data=create_payload)
    res.raise_for_status()
    creation_id = res.json()["id"]
    print(f"✅ メディアオブジェクト作成: {creation_id}")

    # Step 2: 投稿を公開
    publish_url = f"https://graph.facebook.com/v19.0/{IG_USER_ID}/media_publish"
    publish_payload = {
        "creation_id": creation_id,
        "access_token": ACCESS_TOKEN,
    }
    res = requests.post(publish_url, data=publish_payload)
    res.raise_for_status()
    post_id = res.json()["id"]
    print(f"🎉 投稿完了！ post_id: {post_id}")
    return {"post_id": post_id, "creation_id": creation_id}


def post_reel(video_url: str, caption: str) -> dict:
    """
    リール動画投稿
    video_url: 公開アクセス可能な動画URL（https必須、mp4推奨）
    caption:   投稿文 + ハッシュタグ
    """
    # Step 1: メディアオブジェクト作成（リール）
    create_url = f"https://graph.facebook.com/v19.0/{IG_USER_ID}/media"
    create_payload = {
        "media_type": "REELS",
        "video_url": video_url,
        "caption": caption,
        "share_to_feed": "true",
        "access_token": ACCESS_TOKEN,
    }
    res = requests.post(create_url, data=create_payload)
    res.raise_for_status()
    creation_id = res.json()["id"]
    print(f"✅ リールオブジェクト作成: {creation_id}")

    # Step 2: アップロード完了を待つ（最大2分）
    print("⏳ 動画アップロード中...")
    for _ in range(24):
        time.sleep(5)
        status_url = f"https://graph.facebook.com/v19.0/{creation_id}"
        status_res = requests.get(status_url, params={
            "fields": "status_code",
            "access_token": ACCESS_TOKEN,
        })
        status = status_res.json().get("status_code", "")
        print(f"   ステータス: {status}")
        if status == "FINISHED":
            break
        if status == "ERROR":
            raise RuntimeError("動画アップロードに失敗しました")
    else:
        raise TimeoutError("動画アップロードがタイムアウトしました")

    # Step 3: 投稿を公開
    publish_url = f"https://graph.facebook.com/v19.0/{IG_USER_ID}/media_publish"
    publish_payload = {
        "creation_id": creation_id,
        "access_token": ACCESS_TOKEN,
    }
    res = requests.post(publish_url, data=publish_payload)
    res.raise_for_status()
    post_id = res.json()["id"]
    print(f"🎉 リール投稿完了！ post_id: {post_id}")
    return {"post_id": post_id, "creation_id": creation_id}


def get_account_info() -> dict:
    """アカウント情報を確認する（トークンのテスト用）"""
    url = f"https://graph.facebook.com/v19.0/{IG_USER_ID}"
    res = requests.get(url, params={
        "fields": "id,name,username,followers_count,media_count",
        "access_token": ACCESS_TOKEN,
    })
    res.raise_for_status()
    return res.json()


def get_media_insights(post_id: str) -> dict:
    """投稿のインサイト（いいね・リーチ・保存数）を取得"""
    url = f"https://graph.facebook.com/v19.0/{post_id}/insights"
    res = requests.get(url, params={
        "metric": "impressions,reach,saved,likes",
        "access_token": ACCESS_TOKEN,
    })
    res.raise_for_status()
    return res.json()


# ── CLI インターフェース ───────────────────────────────────
if __name__ == "__main__":
    if not ACCESS_TOKEN or not IG_USER_ID:
        print("❌ 環境変数が未設定です")
        print("   export IG_ACCESS_TOKEN='your_token'")
        print("   export IG_USER_ID='your_ig_user_id'")
        sys.exit(1)

    command = sys.argv[1] if len(sys.argv) > 1 else "info"

    if command == "info":
        info = get_account_info()
        print(json.dumps(info, ensure_ascii=False, indent=2))

    elif command == "photo":
        # 使用例: python poster.py photo "https://..." "キャプション文"
        image_url = sys.argv[2]
        caption   = sys.argv[3]
        result = post_photo(image_url, caption)
        print(json.dumps(result, ensure_ascii=False, indent=2))

    elif command == "reel":
        # 使用例: python poster.py reel "https://..." "キャプション文"
        video_url = sys.argv[2]
        caption   = sys.argv[3]
        result = post_reel(video_url, caption)
        print(json.dumps(result, ensure_ascii=False, indent=2))

    elif command == "insights":
        # 使用例: python poster.py insights "post_id"
        post_id = sys.argv[2]
        result = get_media_insights(post_id)
        print(json.dumps(result, ensure_ascii=False, indent=2))

    else:
        print(f"❌ 不明なコマンド: {command}")
        print("使い方: python poster.py [info|photo|reel|insights]")
