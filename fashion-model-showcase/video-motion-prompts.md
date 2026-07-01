# AIモデル生成サンプル動画 — 動画モーションプロンプト集

使用ツール：Kling AI（Image to Video）
設定：1080p・6秒・16:9

---

## S1 — 日本人女性モデル（0〜6秒）

**対応画像：** S1プロンプトで生成した画像

**日本語解説：**
20代日本人女性がホワイトスタジオをカメラに向かってゆっくり歩いてきます。カメラは固定で、モデルが近づくにつれて自然にフォーカスが引き締まります。歩き方は自信に満ちて、でも柔らかい雰囲気で。

```
Model walks slowly and confidently toward the camera,
natural elegant stride, white studio background remains completely static,
camera completely still, no camera movement,
model gradually gets closer and fills more of the frame,
soft studio lighting stays consistent, smooth and cinematic motion,
high-end fashion editorial style, no sudden movements
```

**設定目安**
- 尺：6秒
- 動きの強さ：弱め
- カメラ：固定

---

## S2 — 欧米系女性モデル（6〜12秒）

**対応画像：** S2プロンプトで生成した画像

**日本語解説：**
S1と全く同じカメラアングル・照明で、欧米系30代女性がカメラに向かって歩いてきます。S1との「切り替わり」を際立たせるため、動きのパターンもS1と同じになるよう指示します。

```
Model walks slowly and confidently toward the camera,
natural elegant stride, white studio background remains completely static,
camera completely still, no camera movement,
model gradually gets closer and fills more of the frame,
soft studio lighting stays consistent, smooth and cinematic motion,
high-end fashion editorial style, no sudden movements
```

**設定目安**
- 尺：6秒
- 動きの強さ：弱め
- カメラ：固定

---

## S3-A — アジア系女性モデル（12〜15秒）

**対応画像：** S3-Aプロンプトで生成した画像

**日本語解説：**
40代アジア系女性が同じスタジオを歩いてきます。S1・S2より少し短いクリップです。編集でテンポを上げるため3秒クリップを使用します。

```
Model walks slowly and confidently toward the camera,
natural elegant stride, white studio background remains completely static,
camera completely still, no camera movement,
soft studio lighting stays consistent, smooth and cinematic motion,
high-end fashion editorial style, no sudden movements
```

**設定目安**
- 尺：3秒（6秒生成後、前半3秒をCapCutでトリミング）
- 動きの強さ：弱め
- カメラ：固定

---

## S3-B — 男性モデル（15〜18秒）

**対応画像：** S3-Bプロンプトで生成した画像

**日本語解説：**
20代男性モデルが白いスーツでカメラに向かって歩いてきます。S3-Aに続いてテンポよく切り替わることで「何人でも生成できる」という印象を与えます。

```
Male model walks slowly and confidently toward the camera,
natural elegant stride, white studio background remains completely static,
camera completely still, no camera movement,
soft studio lighting stays consistent, smooth and cinematic motion,
high-end fashion commercial style, no sudden movements
```

**設定目安**
- 尺：3秒（6秒生成後、前半3秒をCapCutでトリミング）
- 動きの強さ：弱め
- カメラ：固定

---

## S4 — 生成ビジュアル（18〜24秒）

**対応画像：** S4プロンプトで生成した画像

**日本語解説：**
光の粒子が人のシルエットを形成していくビジュアルが静かに動きます。「AIが生成している」感覚を視覚的に表現するシーンです。カメラは固定、光だけがゆっくり動きます。

```
Light particles slowly drift and swirl in dark space,
glowing blue and white light trails move gently across the frame,
no camera movement, ethereal and futuristic atmosphere,
smooth particle animation, no sudden changes,
calm and minimal motion, AI generation visual concept
```

**設定目安**
- 尺：6秒
- 動きの強さ：弱め
- カメラ：固定

---

## 編集の順番と目安尺

| 順番 | シーン | クリップ尺 | 累計 |
|------|--------|-----------|------|
| 1 | S1（日本人女性） | 6秒 | 6秒 |
| 2 | S2（欧米系女性） | 6秒 | 12秒 |
| 3 | S3-A（アジア系女性） | 3秒 | 15秒 |
| 4 | S3-B（男性） | 3秒 | 18秒 |
| 5 | S4（生成ビジュアル） | 6秒 | 24秒 |
| 6 | エンドカード（CapCutで作成） | 6秒 | **30秒** |

---

## 編集のポイント（CapCut）

- **S1→S2の切り替え**：「ディゾルブ（0.3秒）」で繋ぐと、モデルだけが溶け替わるように見えて効果的
- **S2→S3-A→S3-B**：カット（0秒）で繋いでテンポを出す
- **S3-B→S4**：「暗転（0.5秒）」で種明かしシーンへの切り替えを明確にする
- BGMはS3からテンポアップするよう音楽素材を調整する

---

*Rev.1.0 — 2026/07/01*
