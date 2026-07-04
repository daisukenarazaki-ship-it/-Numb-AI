# 【CM企画】SHUWA Sparkling — 飲料・食品（炭酸水 / アニメ風）
生成日: 2026-07-04

## 仮定した項目
- 商品名: 未定 → 架空名「SHUWA（シュワ）」で作成（炭酸のオノマトペ由来・実在ブランドと非重複）
- スタイル: **アニメ風**（ユーザー指定）。このためプロンプト末尾を実写用の `photoreal, ultra realistic, 4k` から
  **`modern Japanese anime style, cel-shaded, vibrant saturated colors, clean crisp line art, detailed painterly sky, soft cinematic lighting, 4k`** に差し替えた
- ターゲット: 10代後半〜20代男女（アニメ風・炭酸のため既定の「20-40代」から若干若く寄せた）
- トーン: フレッシュ・開放感（カテゴリ既定）
- 尺: 30秒・5カット（既定）
- モデル: あり・アニメキャラ1名（既定の「AIモデル1名」をアニメキャラに読み替え）

## 企画サマリー
- コンセプト: 真夏の放課後、ひと口の炭酸で世界がキラめく——青春の一瞬を切り取る
- コピー案: ①「はじける、夏。」②「シュワっと、青春。」③「ひと口で、空が近い。」

## カット割り（30秒）
| Cut | 秒 | 内容 | 使う画像 |
|---|---|---|---|
| 1 | 0–5 | フック: 無数の気泡が光を受けて立ちのぼるマクロ（人物・商品なし） | 画像D |
| 2 | 5–11 | キャラ登場: 夏空の下、少女が振り向く | 画像A |
| 3 | 11–17 | 商品ヒーロー: ボトルが陽光の中で結露を帯びる | 画像B |
| 4 | 17–23 | 使用感: グラスに炭酸が注がれ気泡が弾ける | 画像E |
| 5 | 23–30 | 仕上がり: 少女がボトルを空へ掲げて笑う | 画像C |

## フェーズ1: DALL·E 3 プロンプト

### 画像A｜モデルシート（キャラ基準）
```
A cheerful teenage anime girl, big expressive sparkling eyes, short dark bob haircut with a single ahoge, light summer sailor-style school uniform, bright joyful smile, healthy fair skin, standing under a vivid blue summer sky with cumulus clouds, front facing, modern Japanese anime style, cel-shaded, vibrant saturated colors, clean crisp line art, detailed painterly sky, soft cinematic lighting, 4k
```

### 画像B｜商品シート（商品基準）
```
A slim tall clear glass sparkling water bottle, pale aqua-blue tint, minimalist rounded shape, matte white cap, a small embossed silver droplet emblem on the front (no readable text), fresh condensation droplets on the surface, placed against a bright summer sky background, modern Japanese anime style, cel-shaded, vibrant saturated colors, clean crisp line art, detailed painterly sky, soft cinematic lighting, 4k
```

### 画像C｜合成（キャラ＋商品）
```
A cheerful teenage anime girl, big expressive sparkling eyes, short dark bob haircut with a single ahoge, light summer sailor-style school uniform, bright joyful smile, healthy fair skin, holding up a slim tall clear glass sparkling water bottle with pale aqua-blue tint and matte white cap and a small embossed silver droplet emblem (no readable text) toward the sky, wind gently blowing her hair, vivid blue summer sky with cumulus clouds behind her, leave empty space top-left, modern Japanese anime style, cel-shaded, vibrant saturated colors, clean crisp line art, detailed painterly sky, soft cinematic lighting, 4k
```

### 画像D｜Cut1用（フック / 気泡マクロ）
```
Extreme macro of countless rising sparkling bubbles inside clear pale aqua-blue liquid, sunlight glinting through, delicate effervescence, dreamy sparkle highlights, modern Japanese anime style, cel-shaded, vibrant saturated colors, clean crisp line art, soft cinematic lighting, 4k
```

### 画像E｜Cut4用（使用感 / 注ぎ）
```
Sparkling water being poured into a clear glass, bubbles bursting and fizzing upward, tiny droplets splashing, bright summer light, refreshing anime atmosphere, modern Japanese anime style, cel-shaded, vibrant saturated colors, clean crisp line art, soft cinematic lighting, 4k
```

## フェーズ2: Kling プロンプト

### Cut 1｜立ちのぼる気泡（0–5s）
- 使う画像: 画像D（画像から動画）
```
countless tiny bubbles rise slowly through the clear liquid as sunlight glints through, smooth anime animation, slow motion, cinematic, no text
```

### Cut 2｜少女登場（5–11s）
- 使う画像: 画像A（画像から動画）
```
she turns toward the camera with a bright joyful smile as her hair sways in the breeze, smooth anime animation, slow motion, cinematic, no text
```

### Cut 3｜商品ヒーロー（11–17s）
- 使う画像: 画像B（画像から動画）
```
slow push-in on the bottle as condensation droplets slide down its surface glistening in the light, smooth anime animation, slow motion, cinematic, no text
```

### Cut 4｜弾ける炭酸（17–23s）
- 使う画像: 画像E（画像から動画）
```
sparkling water pours into the glass and bubbles burst upward energetically, smooth anime animation, slow motion, cinematic, no text
```

### Cut 5｜空へ掲げる（23–30s）
- 使う画像: 画像C（画像から動画）
```
she lifts the bottle toward the bright sky and laughs happily as light flares behind her, smooth anime animation, slow motion, cinematic, no text
```

## フェーズ3: 編集指示
1. Cut1→Cut5 を時系列に連結、カット間は 0.3〜0.5秒クロスディゾルブ（Cut1→Cut2 は気泡が弾けるタイミングでカット切替にすると爽快感が出る）
2. 音楽: 軽快なアコースティック＋炭酸の弾ける音（アニメ風のためポップな夏ソング系でも可）
3. カラーグレーディング: クリアで鮮やかなブルー／グリーン基調、空の青を強調
4. ラスト3秒にロゴ＋コピー「はじける、夏。」を編集で合成（動画に文字は生成しない）
5. 書き出し: 1080p / MP4 / H.264

## 制作チェックリスト
- [x] 画像AとCのキャラ記述が一字一句同じ
- [x] 画像BとCの商品記述が一字一句同じ
- [x] 全プロンプトに文字・実在ブランド・実在人物が入っていない
- [x] DALL·E末尾がアニメ用の締めで統一されている（実写指定はアニメ用に差し替え済み）
- [x] Kling末尾が smooth anime animation, slow motion, cinematic, no text
- [x] 各Klingプロンプトの動きが1つだけ
- [x] プレースホルダー（[ ]や{ }）が残っていない
- [x] ロゴ・コピーは編集で載せる前提になっている
