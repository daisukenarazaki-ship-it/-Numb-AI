# AIモデルCM 制作ガイド（化粧品・飲料）
DALL·E 3（画像）→ Kling（動画）→ 編集 までの一貫手順
※すべてのプロンプトは置き換え不要・そのままコピペでOK

---

## 0. 準備

- 画像生成：**DALL·E 3**（ChatGPT内）
- 動画生成：**Kling**（画像から動画 / Elements）
- 編集：CapCut / Premiere / DaVinci Resolve など

### 一貫性の黄金ルール
1. モデルは「1枚の顔画像」を全カットで使い回す
2. 商品は「1枚の商品画像」を全カットで使い回す
3. ラベルに文字は入れない（AIは文字を崩す）→ エンブレムにする
4. 各カットは5秒で個別生成 → 編集で連結
5. プロンプト末尾は常に：cinematic, ultra realistic, slow motion, no text

---
---

# 【CM①】化粧品：LUMIÈRE — Radiance Serum

## フェーズ1：DALL·E 3で画像を作る

### 画像A｜モデルシート（顔の基準）
```
A late-20s East Asian woman, luminous flawless dewy skin, natural minimalist makeup, soft glossy nude lips, sleek low bun, refined elegant features, calm confident gaze, ultra realistic skin texture with fine pores, studio beauty portrait, front facing, neutral soft cream background, soft window light, photoreal, 4k
```

### 画像B｜商品シート（商品の基準）
```
A luxury cosmetic serum bottle, frosted cream-white glass, slim cylindrical shape, polished gold dropper cap, a small embossed gold leaf emblem on the front (no readable text), minimalist design, soft studio lighting, neutral cream background, premium product photography, photoreal, ultra realistic, 4k
```

### 画像C｜Cut5用 合成（モデル＋商品）
```
A late-20s East Asian woman, luminous flawless dewy skin, natural minimalist makeup, soft glossy nude lips, sleek low bun, refined elegant features, gently holding a luxury cosmetic serum bottle with frosted cream-white glass and polished gold dropper cap and a small embossed gold leaf emblem (no readable text) near her cheek, soft golden window light, elegant beauty commercial, shallow depth of field, photoreal, ultra realistic, leave empty space top-left, 4k
```

### 画像D｜Cut1用 マクロ肌
```
Extreme macro close-up of luminous dewy skin catching soft morning light, tiny golden light reflections, fine pores, shallow depth of field, photoreal, ultra realistic, 4k
```

### 画像E｜Cut4用 テクスチャー
```
Macro of a glossy golden cosmetic serum droplet spreading on luminous dewy skin, silky texture, soft light reflections, extremely detailed, photoreal, ultra realistic, 4k
```

---

## フェーズ2：Klingで各カットを動画化（各5秒）

### Cut 1｜目覚める肌（0–5s）
- 使う画像：**画像D**（画像から動画）
```
slow cinematic push-in on dewy glowing skin, soft golden morning light, gentle subtle movement, slow motion, ultra realistic, no text
```

### Cut 2｜モデル登場（5–11s）
- 使う画像：**画像A**（画像から動画）
```
she slowly turns toward camera with a gentle confident smile, soft window light with warm golden rim light, glowing radiant skin, slow motion, cinematic, photoreal, no text
```

### Cut 3｜商品ヒーロー（11–17s）
- 使う画像：**画像B**（画像から動画）
```
slow cinematic push-in, a single golden droplet falls from the dropper in slow motion, delicate light refraction through the liquid, premium product shot, ultra realistic, no text
```

### Cut 4｜テクスチャー（17–23s）
- 使う画像：**画像E**（画像から動画）
```
the golden serum slowly spreads and absorbs into glowing skin, silky texture, soft light reflections, slow motion, cinematic, ultra realistic, no text
```

### Cut 5｜仕上がりの肌（23–30s）
- 使う画像：**画像C**（画像から動画）
```
she gently touches her glowing cheek, eyes closed then softly opening, warm golden light, serene elegant mood, slow motion, cinematic, photoreal, no text
```

📝 コピー：「光を、素肌から。」／ LUMIÈRE Radiance Serum

---
---

# 【CM②】飲料：AOI — Sparkling Botanical

## フェーズ1：DALL·E 3で画像を作る

### 画像A｜モデルシート（顔の基準）
```
A late-20s East Asian woman, fresh dewy radiant skin, natural fresh makeup, healthy glowing complexion, soft wavy hair, bright lively eyes, light linen outfit, joyful elegant expression, natural lifestyle portrait, front facing, bright outdoor botanical garden with soft bokeh, daylight, ultra realistic, photoreal, 4k
```

### 画像B｜商品シート（商品の基準）
```
A premium sparkling beverage bottle, clear frosted glass, tall slim elegant shape, matte deep-blue cap, a single abstract green leaf emblem on the front (no readable text), fresh condensation droplets, bright studio lighting, clean neutral background, premium beverage product photography, photoreal, ultra realistic, 4k
```

### 画像C｜Cut3・Cut5用 合成（モデル＋商品）
```
A late-20s East Asian woman, fresh dewy radiant skin, natural fresh makeup, soft wavy hair, bright lively eyes, light linen outfit, joyful elegant expression, holding a premium sparkling beverage bottle with clear frosted glass and matte deep-blue cap and a single abstract green leaf emblem (no readable text), sunlit outdoor botanical garden with soft bokeh, gentle breeze in hair, fresh airy atmosphere, photoreal, ultra realistic, 4k
```

### 画像D｜Cut2用 スプラッシュ
```
High-speed macro of clear sparkling water splashing upward with fresh mint leaves and bubbles, crystal clear droplets frozen in air, bright daylight, vivid clean colors, photoreal, ultra realistic, 4k
```

### 画像E｜Cut4用 気泡マクロ
```
Extreme macro of rising sparkling bubbles inside clear liquid, delicate effervescence, soft sunlight passing through, blue-green tint, extremely detailed, photoreal, ultra realistic, 4k
```

---

## フェーズ2：Klingで各カットを動画化（各5秒）

### Cut 1｜結露するボトル（0–5s）
- 使う画像：**画像B**（画像から動画）
```
cold mist slowly rolls off the frosted bottle, condensation droplets glisten and slide down, blue-green reflections, bright natural light, slow motion, cinematic, ultra realistic, no text
```

### Cut 2｜スプラッシュ（5–11s）
- 使う画像：**画像D**（画像から動画）
```
clear sparkling water and mint leaves splash upward in high-speed slow motion, crystal droplets frozen in air, vivid clean colors, bright daylight, cinematic, ultra realistic, no text
```

### Cut 3｜モデルの解放感（11–18s）
- 使う画像：**画像C**（画像から動画）
```
she takes a refreshing sip from the bottle then smiles with eyes closed feeling refreshed, sunlit garden bokeh, gentle breeze in hair, slow motion, cinematic, photoreal, no text
```

### Cut 4｜気泡マクロ（18–24s）
- 使う画像：**画像E**（画像から動画）
```
countless tiny bubbles rise through the clear liquid, sunlight glinting through, blue-green tint, slow motion, ultra detailed, cinematic, no text
```

### Cut 5｜ヒーロー＆ライフスタイル（24–30s）
- 使う画像：**画像C**（画像から動画）
```
she laughs lightly and lifts the bottle toward the sunlight, lens flare, fresh airy atmosphere, the bottle clearly in frame, slow motion, cinematic, photoreal, no text
```

📝 コピー：「ひと口の、深呼吸。」／ AOI Sparkling Botanical

---
---

## フェーズ3：編集で1本にまとめる（共通）

1. 各カット（5秒×5）を時系列に並べる（Cut1→Cut5）
2. カット間は 0.3〜0.5秒のクロスディゾルブで繋ぐ
3. 音楽を乗せる
   - 化粧品：静かなピアノ＋ストリングス＋水滴のASMR
   - 飲料：軽快なアコースティック＋炭酸の弾ける音
4. カラーグレーディングで統一
   - 化粧品：温かいゴールド／クリーム寄り
   - 飲料：クリアで鮮やかなブルー／グリーン寄り
5. ラスト3秒にロゴ＋コピーを重ねる（動画には文字を入れず編集で）
6. 書き出し：1080p / MP4 / H.264

---

## Kling 操作のヒント
- Image to Video：開始画像をアップ → 動きをプロンプトで指示
- Elements（複数参照）：モデル画像＋商品画像を同時参照（合成カットに便利）
- 始点・終点フレーム：開始と終了の画像を指定すると動きを制御できる
- 1回で決まらない → 複数回生成して一番良いテイクを採用

---

## Webサイトへの掲載
完成した動画を YouTube に限定公開 → URL を共有すれば、実績（Works）に掲載します。
