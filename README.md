# Numb タスク管理システム

LINE グループでタスクを報告 → Gemini AI が整形 → Google Sheets に自動保存 → 毎朝タスクを自動通知

## システム概要

```
LINEグループでメッセージ送信
        ↓
Gemini AI がアクションを判定 (new_task / complete / ask / none)
        ↓
Google Sheets に保存 or 状態更新
        ↓
LINE にリプライ
        ↓
毎日朝8:00 に未完了タスクをグループへ自動通知
```

## 機能

- **タスク登録**: 「田中さんに資料作成、5月10日まで」→ 自動で Google Sheets に登録
- **タスク完了**: 「会議完了」「会議終わった」→ 状態が「完了」に自動更新
- **朝の通知**: 毎日 8:00 に未完了タスク一覧を LINE グループへ Push
- **AI 判定**: Gemini AI による自然言語理解（話し言葉に対応）

## セットアップ

### 1. 必要なもの

- Python 3.11+
- LINE Bot アカウント（Messaging API チャネル）
- Google Cloud プロジェクト（Sheets API + サービスアカウント）
- Gemini API キー（Google AI Studio）

### 2. Python パッケージのインストール

```bash
pip install -r requirements.txt
```

### 3. 環境変数の設定

```bash
cp .env.example .env
# .env を編集して各 API キーを設定
```

`.env` に以下を設定してください:

```env
LINE_CHANNEL_ACCESS_TOKEN=your_token
LINE_CHANNEL_SECRET=your_secret
LINE_GROUP_ID=your_group_id
GEMINI_API_KEY=your_key
GOOGLE_SHEETS_ID=your_sheets_id
GOOGLE_SERVICE_ACCOUNT_JSON=service_account.json
```

### 4. Google Sheets サービスアカウントの設定

1. [Google Cloud Console](https://console.cloud.google.com/) でプロジェクトを作成
2. `Google Sheets API` と `Google Drive API` を有効化
3. IAM > サービスアカウント > キーを作成（JSON 形式）
4. ダウンロードした JSON ファイルを `service_account.json` としてプロジェクトルートに配置
5. Google Sheets を開いてサービスアカウントのメールアドレスに編集権限を付与

### 5. LINE Webhook URL の設定

```bash
# ngrok をインストール後
ngrok http 5000
```

ngrok の URL（例: `https://xxxx.ngrok.io`）を LINE Developers Console の Webhook URL に設定:
```
https://xxxx.ngrok.io/callback
```

### 6. サーバー起動

```bash
python main.py
```

### 7. LINE グループ ID の取得

1. LINE グループに Bot を招待
2. グループで任意のメッセージを送信
3. サーバーのログに Group ID が表示されるので `.env` の `LINE_GROUP_ID` に設定

## Google Sheets の構成

| 登録日時 | 依頼者 | 担当 | 内容 | 期限 | 状態 |
|---------|--------|------|------|------|------|
| 2026/05/10 09:00:00 | 山田 | 田中 | 資料作成 | 2026/05/21 | 未着手 |

- **状態**: 未着手 / 進行中 / 完了

## 使い方

### タスクを登録する

```
田中さんに資料作成をお願い、5月21日まで
@田中 会議の準備を明日までにやって
5月21日に会議があるんで、タスクに追加
```

### タスクを完了にする

```
会議完了
資料作成終わった
会議の準備できました
```

### 朝の通知例

```
📋 05月26日 本日のタスク

1️⃣ 【田中】資料作成（期限: 2026/05/21）
2️⃣ 【山田】会議準備（期限: 2026/05/26）

今日もよろしくお願いします！
```

## ファイル構成

```
numb-task-system/
├── main.py                        # メインアプリ・Flask サーバー
├── config.py                      # 設定・環境変数
├── handlers/
│   ├── line_handler.py            # LINE メッセージ処理
│   ├── gemini_handler.py          # Gemini AI 判定
│   └── sheets_handler.py          # Google Sheets 連携
├── schedulers/
│   └── morning_notification.py    # 朝 8:00 の通知
├── utils/
│   ├── date_converter.py          # 日付変換ユーティリティ
│   └── name_extractor.py          # 名前抽出ユーティリティ
├── .env.example                   # 環境変数テンプレート
├── requirements.txt               # 依存関係
└── README.md                      # このファイル
```

## 注意事項

- **`.env` ファイルは絶対に Git にコミットしないでください**
- **`service_account.json` も Git にコミットしないでください**
- Gemini API の無料枠は 1 日 250 回（このシステムでは十分）
- 本番環境では `FLASK_DEBUG=False` に設定してください
- LINE Webhook URL は HTTPS が必須（ngrok 推奨）

## トラブルシューティング

### 署名検証エラー

`LINE_CHANNEL_SECRET` が正しく設定されているか確認してください。

### Google Sheets 書き込みエラー

- サービスアカウントの JSON ファイルパスを確認
- スプレッドシートにサービスアカウントの編集権限が付与されているか確認

### Gemini API エラー

- `GEMINI_API_KEY` が有効か確認
- API の利用制限（1分あたりのリクエスト数）に達していないか確認
