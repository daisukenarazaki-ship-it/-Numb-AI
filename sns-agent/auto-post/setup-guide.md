# 🔧 Instagram自動投稿 セットアップガイド

## 全体の流れ

```
Step 1: FacebookページをInstagramに連携（5分）
Step 2: Metaデベロッパーアプリ作成（15分）
Step 3: アクセストークン取得（10分）
Step 4: Cloudinaryアカウント作成（5分）
Step 5: 環境変数を設定（2分）
Step 6: 動作テスト（2分）
```

---

## Step 1: FacebookページとInstagramを連携

1. https://www.facebook.com/pages/create にアクセス
2. 「ビジネスまたはブランド」→ ページ名「Liberty Cat」で作成
3. Instagramアプリ → プロフィール → ☰メニュー
4. 「設定とアクティビティ」→「アカウント」→「Metaアカウントセンター」
5. 「アカウントを追加」→ 作成したFacebookページと連携

---

## Step 2: Metaデベロッパーアプリ作成

1. https://developers.facebook.com にアクセス（Facebookログイン）
2. 右上「マイアプリ」→「アプリを作成」
3. 「その他」→「ビジネス」を選択
4. アプリ名「Liberty Cat Poster」で作成
5. 左メニュー「製品を追加」→「Instagram Graph API」を追加

---

## Step 3: アクセストークン取得

### 3-1. IG User IDを確認
```
https://graph.facebook.com/v19.0/me/accounts?access_token=一時トークン
```
→ InstagramページのIDをメモ

### 3-2. 長期トークンに変換（60日有効）
```
https://graph.facebook.com/v19.0/oauth/access_token?
  grant_type=fb_exchange_token&
  client_id=アプリID&
  client_secret=アプリシークレット&
  fb_exchange_token=一時トークン
```

### 3-3. 取得できた値をメモ
```
IG_ACCESS_TOKEN = "EAAxxxx..."
IG_USER_ID      = "17841xxxxxxxx"
```

---

## Step 4: Cloudinaryアカウント作成（画像ホスティング用）

1. https://cloudinary.com にアクセス → 無料登録
2. ダッシュボードで以下をメモ：
   - Cloud Name
   - API Key
   - API Secret
3. 「Settings」→「Upload」→「Add upload preset」
   - Preset name: `instagram_auto`
   - Signing Mode: `Unsigned`

---

## Step 5: 環境変数を設定

以下をClaudeのチャットで教えてください（安全に保存します）：

```
IG_ACCESS_TOKEN=EAAxxxx...
IG_USER_ID=17841xxxxxxxx
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

---

## Step 6: 動作テスト

設定完了後、Claudeに以下のように指示するだけで投稿できます：

```
【投稿指示の例】
「内装の写真（photo_01.jpg）を今すぐ投稿して。
キャプションはスケジュールの8/8のものを使って」

「グラフィティの動画をリールで投稿して」

「チンチロのフライヤーを今夜20時に投稿予約して」
```

---

## よくある質問

**Q: トークンが60日で切れたらどうする？**  
A: 切れる前にClaudeに「トークンを更新して」と言えば手順を案内します。

**Q: 写真はどこから渡せばいい？**  
A: スマホからCloudinaryに直接アップロードするか、このチャットに写真を送ればClaudeが処理します。

**Q: 予約投稿はできる？**  
A: Instagram Graph APIは予約投稿に対応しています。「〇月〇日〇時に投稿して」と指示してください。
