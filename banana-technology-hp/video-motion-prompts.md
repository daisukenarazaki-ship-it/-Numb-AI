# Banana Technology HP トップ背景動画 — 動画モーションプロンプト集

使用ツール推奨：Kling AI / Runway Gen-3
用途：HPトップページ背景動画（20秒ループ）

---

## シーン1 — AI映像生成のビジュアル（0〜5秒）

**対応画像：** シーン1プロンプトで生成した画像

**日本語解説：**
暗い背景の中、光の粒子がゆっくりと流れ出し、画面全体に広がっていきます。カメラは完全固定。静かで幻想的な雰囲気でスタートし、「AIが何かを生み出している」感覚を視覚的に表現します。

```
Light particles slowly emerge and drift across dark space,
soft glow expanding gradually across the frame,
no camera movement, static shot,
smooth and ethereal particle animation,
electric blue light trails flowing gently, no sudden changes
```

**設定目安**
- 尺：5秒
- 動きの強さ：弱め
- カメラ：固定

---

## シーン2 — マルチデバイス映像表示（5〜10秒）

**対応画像：** シーン2プロンプトで生成した画像

**日本語解説：**
複数のスクリーンが暗い空間に浮かび、それぞれの画面に映像が流れます。カメラがゆっくり前進することで「映像の世界に引き込まれていく」感覚を演出します。画面の光が周囲を照らして幻想的な雰囲気を作ります。

```
Camera slowly pushes forward toward the floating screens,
screens glow and flicker with dynamic video content,
light from screens softly illuminates surrounding dark space,
smooth dolly forward, no shake, cinematic and futuristic atmosphere
```

**設定目安**
- 尺：5秒
- 動きの強さ：弱め
- カメラ：ドリーフォワード（ゆっくり前進）

---

## シーン3 — ロゴ収束ビジュアル（10〜15秒）

**対応画像：** シーン3プロンプトで生成した画像

**日本語解説：**
画面の四方から光のラインが中央に向かって収束してきます。カメラは固定。光が集まるにつれて中央が明るくなり、クライマックス感が高まります。HPのロゴはこの光の焦点の上にHP側で別レイヤーとして重ねます。

```
Glowing light beams converge from all directions toward the center,
energy lines accelerate as they approach the focal point,
center becomes intensely bright, camera completely still,
dramatic buildup of light energy, no camera movement,
electric blue and yellow colors intensifying
```

**設定目安**
- 尺：5秒
- 動きの強さ：中〜強め
- カメラ：固定

---

## シーン4 — ループエンド（15〜20秒）

**対応画像：** シーン4プロンプトで生成した画像

**日本語解説：**
シーン3で集まった光が今度は静かに拡散・消散していきます。徐々に暗くなり、シーン1の冒頭とシームレスにつながるよう、最後は光の粒子がゆっくり漂う状態で終わります。ループ再生を意識した自然なフェードアウト。

```
Bright light gradually dissolves and disperses outward,
particles slowly drift apart and fade into dark space,
smooth and gradual dimming, no sudden changes,
ending with softly floating light particles matching the opening scene,
seamless loop transition, calm and minimal movement
```

**設定目安**
- 尺：5秒
- 動きの強さ：弱め（フェードアウト感）
- カメラ：固定

---

## ループ編集の注意点

シーン4の最終フレームとシーン1の最初のフレームの**明るさ・光の量を揃える**ことが重要です。
CapCutまたはDaVinci Resolveで以下を確認してください：

1. シーン4の最後 → 光の粒子が薄く漂っている状態
2. シーン1の最初 → 同じく光の粒子が薄く漂っている状態
3. 繋ぎ目に**クロスディゾルブ（0.5秒）**をかけると自然にループする

---

## HP実装時の重ねるテキスト

動画の上にHTMLで以下を重ねて表示します（動画には含めない）

```
AIで映像を、もっと自由に。

[事例を見る]　[無料相談する]
```

- テキスト色：ホワイト（#FFFFFF）
- フォント：太めのゴシック体
- 位置：画面中央やや上

---

*Rev.1.0 — 2026/06/28*
