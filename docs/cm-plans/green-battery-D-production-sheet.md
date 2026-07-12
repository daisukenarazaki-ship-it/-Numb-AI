# 案D｜THIS IS JAPAN 制作進行シート（15秒・6カット）

Green Battery 米国Netflix CM ／ 制作用。上から順に進めればOK。
ツール：静止画＝DALL·E 3 / Firefly（無料）→ 動画＝**Kling**（有料）→ 声＝**HeyGen**（有料）→ 音楽＝Suno等 → 編集＝CapCut（無料）。

## 全体像
| Cut | 秒 | 映像 | カメラ | 英語VO | テロップ（編集で合成） |
|---|---|---|---|---|---|
| 1 | 0–2 | 富士山と満開の桜 | 空撮グライド | "This is Japan." | — |
| 2 | 2–5 | 歌舞伎の見得 | スナップズーム | （和楽器のキメ） | — |
| 3 | 5–8 | 京都・朱の鳥居のトンネル | 前進ドリー | （和楽器） | — |
| 4 | 8–10 | 川に架かる朱の太鼓橋と桜 | 横移動ドリー | （和楽器） | — |
| 5 | 10–13 | 日本の風景に佇む蓄電池施設・富士遠景 | ゆっくり寄る | "And this is how we power it." | GRID-SCALE ENERGY STORAGE（小さく） |
| 6 | 13–15 | 日の丸→ロゴ | 静止 | "Green Battery. From Japan." | A Japanese energy company ／ From Japan |

VOは合計約12語。声のトーン＝米国ネイティブ、静かで誇らしい、急がない。

---

## STEP 1：静止画を6枚つくる（DALL·E 3 / Firefly）
各プロンプトをそのまま貼る。末尾は実写・文字なしで統一。

1. 富士と桜：`snow-capped Mt. Fuji with full-bloom cherry blossoms in the foreground, bright celebratory morning light, iconic Japan, cinematic, photoreal, natural light, no text, no logos, no flags, 16:9`
2. 歌舞伎：`a dramatic kabuki actor striking a powerful mie pose, bold red and white kumadori face makeup, elaborate colorful kimono, dark theatrical background with a spotlight, cinematic, photoreal, natural light, no text, no logos, no flags, no crests, 16:9`
3. 鳥居：`walking POV through a tunnel of vivid vermilion torii gates at a Kyoto shrine, warm sunlight streaming through, lush green forest, receding perspective, cinematic, photoreal, natural light, no text, no logos, no flags, 16:9`
4. 太鼓橋：`a traditional Japanese vermilion arched bridge over a calm river, cherry blossom trees on the banks, petals drifting onto the water, soft spring light, cinematic, photoreal, natural light, no text, no logos, no flags, 16:9`
5. 施設：`modern battery storage containers with green accent panels quietly nestled in a serene Japanese landscape with a distant snow-capped Mt. Fuji, soft daylight, cinematic, photoreal, natural light, no text, no logos, no flags, 16:9`
6. ロゴ背景：`minimal warm off-white washi-textured background with a soft red sun circle, elegant and simple, empty space in the center for a logo, cinematic, photoreal, natural light, no text, no logos, 16:9`

> コツ：各カット2〜3枚生成して一番良い1枚を採用。歌舞伎・施設は「気に入った1枚に似せて」再生成でブレ防止。

## STEP 2：Klingで動画化（各カット、静止画→動画）
設定：高品質・1080p。STEP1の画像を「開始フレーム」に。花びら・光・水は「モーションブラシ」で動かす。ネガティブ：`text, watermark, logo, distortion, extra fingers`。各カット複数テイク→ベスト採用（生成5秒→編集で必要秒数に）。

1. 富士＋桜：`slow cinematic aerial glide toward Mt. Fuji as cherry blossom petals drift gently, cinematic, photoreal, no text`
2. 歌舞伎：`quick snap zoom onto the kabuki actor as he holds the powerful mie pose, sharp and dramatic, cinematic, photoreal, no text`
3. 鳥居：`forward dolly walking through the tunnel of vermilion torii gates toward the light, cinematic, photoreal, no text`
4. 太鼓橋：`slow side-tracking dolly across the red bridge as petals fall onto the river, cinematic, photoreal, no text`
5. 施設：`slow gentle push-in on the battery facility nestled in the landscape with Mt. Fuji behind, cinematic, photoreal, no text`
6. ロゴ：動画化不要（静止背景に編集でロゴ）。

## STEP 3：HeyGenで英語ナレーション
AI Voice（米国ネイティブ・男女どちらでも可）で下記を生成。声色：静かで誇らしい、落ち着いた低〜中音。
- Cut1（0–2s）：`This is Japan.`
- Cut5（10–13s）：`And this is how we power it.`
- Cut6（13–15s）：`Green Battery. From Japan.`
※ 日本語版が必要なら HeyGen の Video Translate で作成。
※ HeyGenのアバターはCM本編には使わない（映像はKling）。投資家用の別動画を作る場合のみ使う。

## STEP 4：音楽（Suno等・任意でEpidemic Sound）
Sunoプロンプト例：`epic cinematic Japanese traditional instrumental, taiko drums, shamisen, koto, celebratory and uplifting, building to a triumphant finish, no vocals, ~15 seconds`
- Cut2（歌舞伎の見得）で和太鼓の「ドン」を合わせるとキマる。
- ⚠️ 生成音楽の商用利用ライセンスを必ず確認（不安ならEpidemic等の権利クリア音源）。

## STEP 5：編集（CapCut）
1. Cut1→6 を順に配置。前半（1–4）は和楽器のビートに合わせ**歯切れよくカット**、Cut5でひと呼吸、Cut6で締め
2. カット尺：上の表の秒数に合わせトリム（合計15.0秒ぴったり）
3. VO（STEP3）を各カットに配置、BGMより前に
4. テロップ（編集で合成）：Cut5に `GRID-SCALE ENERGY STORAGE`（小さめ）、Cut6に `A Japanese energy company / From Japan`。日本語を入れる場合はローマ字＋英訳併記
5. Cut6：日の丸背景に**ロゴ＋タグライン**（例：This is Japan.／From Japan, with energy.）を合成。ロゴは透過PNGを使用
6. カラー：鮮やかで華やか、桜のピンクと朱の赤を効かせる
7. 書き出し：**1080p / MP4 / H.264**（Netflix入稿仕様は代理店・最新仕様を確認）。続けて 9:16・1:1・6秒版も同素材から書き出し

## 最終チェック（提出前）
- [ ] 尺きっかり15.0秒
- [ ] 映像に文字・ロゴ・旗が焼き込まれていない（ロゴ/テロップは編集合成）
- [ ] 旭日旗の意匠なし（日の丸＝赤い丸はOK）／歌舞伎・鳥居に実在の紋・社名なし
- [ ] 未確認の数値・実績・投資リターン表現なし
- [ ] テロップの英語表記が正しい（GRID-SCALE ENERGY STORAGE 等）
- [ ] "Green Battery" 米国商標の確認、音楽・声の商用ライセンス確認
- [ ] クライアント確認を経て納品
