#!/usr/bin/env python3
"""
画像・動画ファイルを Cloudinary にアップロードして公開URLを返すスクリプト
Instagram Graph API は https:// の公開URLが必要なため使用する
"""

import os
import sys
import requests


CLOUDINARY_CLOUD_NAME = os.environ.get("CLOUDINARY_CLOUD_NAME", "")
CLOUDINARY_API_KEY    = os.environ.get("CLOUDINARY_API_KEY", "")
CLOUDINARY_API_SECRET = os.environ.get("CLOUDINARY_API_SECRET", "")


def upload_file(file_path: str, resource_type: str = "auto") -> str:
    """
    ファイルをCloudinaryにアップロードして公開URLを返す
    resource_type: "image" | "video" | "auto"
    """
    if not all([CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET]):
        raise EnvironmentError("Cloudinary環境変数が未設定です")

    upload_url = f"https://api.cloudinary.com/v1_1/{CLOUDINARY_CLOUD_NAME}/{resource_type}/upload"

    with open(file_path, "rb") as f:
        res = requests.post(upload_url, files={"file": f}, data={
            "api_key": CLOUDINARY_API_KEY,
            "upload_preset": "instagram_auto",
        })

    res.raise_for_status()
    public_url = res.json()["secure_url"]
    print(f"✅ アップロード完了: {public_url}")
    return public_url


if __name__ == "__main__":
    file_path = sys.argv[1]
    url = upload_file(file_path)
    print(url)
