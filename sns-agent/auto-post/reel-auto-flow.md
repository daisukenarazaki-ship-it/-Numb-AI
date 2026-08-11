# 📱 Liberty Cat｜Instagram自動投稿フロー設計書

> Google Docマニュアル「社員1人で月1,000万円を削減したAI自動化マニュアル」から
> Instagram自動投稿に関わる箇所を抽出・Liberty Cat向けに整理（2026年8月）

---

## 全体フロー（リール自動制作・投稿）

```
① テーマ・素材を入力
       ↓
② Claude がキャプション・台本・ハッシュタグを自動生成
       ↓
③ Cloudinary に画像/動画をアップロード（公開URL取得）
       ↓
④ poster.py でInstagram Graph API に投稿
       ↓
⑤ 投稿結果・インサイトを liberty-cat-schedule.md に記録
```

---

## 各ステップの詳細

### ① 入力（Claude Codeへの指示）
```
「内装の写真（photo_01.jpg）を今すぐ投稿して。
キャプションはスケジュールの8/8のものを使って」

「グラフィティの動画をリールで投稿して」

「チンチロのフライヤーを今夜20時に投稿予約して」
```

### ② Claude が生成するもの
- 投稿キャプション（絵文字・改行・CTA含む）
- ハッシュタグ（ビッグ3＋ミドル7＋ニッチ10）
- リール台本（動画の場合）

### ③ Cloudinary アップロード
```bash
python sns-agent/auto-post/uploader.py <ファイルパス>
# → 公開URLを返す（https://res.cloudinary.com/...）
```

### ④ Instagram 投稿
```bash
# 写真フィード投稿
python sns-agent/auto-post/poster.py photo "https://..." "キャプション文"

# リール投稿
python sns-agent/auto-post/poster.py reel "https://..." "キャプション文"

# アカウント確認
python sns-agent/auto-post/poster.py info
```

### ⑤ 結果記録
投稿完了後、`liberty-cat-schedule.md` の完了欄を ⬜ → ✅ に更新

---

## 必要な環境変数（セットアップ必須）

```bash
export IG_ACCESS_TOKEN="EAAxxxx..."      # Meta Developer App から取得
export IG_USER_ID="17841xxxxxxxx"        # Instagram Business アカウントID
export CLOUDINARY_CLOUD_NAME="xxxx"     # Cloudinary ダッシュボードから
export CLOUDINARY_API_KEY="xxxx"        # Cloudinary ダッシュボードから
export CLOUDINARY_API_SECRET="xxxx"    # Cloudinary ダッシュボードから
```

---

## セットアップ残タスク

| ステップ | 内容 | 状態 |
|---|---|---|
| Step 1 | Facebook＋Instagram 連携 | ✅ 完了 |
| Step 2 | Meta Developer App 作成 | 🔄 進行中（認証待ち） |
| Step 3 | アクセストークン取得（IG_ACCESS_TOKEN・IG_USER_ID） | ⬜ 未完了 |
| Step 4 | Cloudinary アカウント作成 | ⬜ 未完了 |
| Step 5 | 環境変数を設定 | ⬜ 未完了 |
| Step 6 | poster.py で動作テスト | ⬜ 未完了 |

---

## コスト試算（参考）

| 項目 | 従来 | AI自動化後 |
|---|---|---|
| 投稿文作成 | 30〜60分/本 | 2〜3分/本（Claude） |
| 動画制作（外注） | 15〜20万円/本 | Kling AI＋自動化で1万円以下/本 |
| 月10本の制作費 | 150〜200万円 | 10〜20万円 |

---

## 参考スクリプト

詳細は同フォルダ内の以下を参照：
- `poster.py` — Instagram Graph API 投稿スクリプト
- `uploader.py` — Cloudinary アップロードスクリプト
- `setup-guide.md` — 6ステップセットアップガイド
