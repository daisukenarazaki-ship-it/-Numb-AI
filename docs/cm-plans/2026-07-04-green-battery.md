# 【CM台本＋制作指示】株式会社Green Battery — 企業ブランドムービー
生成日: 2026-07-04 ／ クライアント案件（プロ制作・クオリティ重視）

## 0. この案件の前提（クライアント確認で変更可）
- **尺**: 30秒（コーポレートサイト・展示会・SNS全対応の汎用尺）
- **スタイル**: 実写風シネマティック（インフラ企業の信頼感・スケール感を優先）
- **語り**: 日本語ナレーション＋テロップ
- **訴求軸**: 「再エネを無駄にしない」を中核に、電力安定 → 脱炭素の未来へ展開
- 会社情報の出典: [事業紹介](https://greenbattery.co.jp/services/) / [会社概要](https://greenbattery.co.jp/en/about-en/)
  - 事業: 系統用蓄電池の開発・運用（用地取得〜建設〜運用までワンストップ）
  - ミッション: 再エネを無駄にしない／エネルギーの「もったいない」をなくす
  - 解決課題: 出力制御による再エネの廃棄、需給ミスマッチ、日本のエネルギー自給・脱炭素

> ⚠️ 制作上の重要注意（クライアント案件のため厳守）
> - ナレーションに**具体的な数値・実績（削減率・容量・顧客名など）を勝手に入れない**。事実として確認できるものだけをクライアントに埋めてもらう（台本では `【要確認：数値】` にする）
> - AI生成映像は**実在のGreen Battery施設ではない**。実在施設の写真だと誤認させる使い方はしない（イメージ映像として制作・提出）
> - ロゴ・社名・コピーは**AI生成に含めず、編集で合成**（AIは文字を崩す）
> - 完成後、納品前に必ずクライアントの確認を通す

---

## 1. コンセプト
**「捨てられていた電気が、未来を灯す。」**
太陽や風がつくった電気が、行き場を失って捨てられている——その"もったいない"を蓄電池が受け止め、夜の街や社会を支える力に変える。問題提起から希望への転換を、光の移動で描く30秒。

### タグライン3案（ロゴ横に編集で合成）
1. 「再エネを、無駄にしない。」
2. 「捨てない電気が、未来をつくる。」
3. 「エネルギーの"もったいない"を、なくす。」

---

## 2. 構成（30秒・6ブロック）
起承転結を「昼→夕→夜→朝」の時間経過に重ねる。

| # | 秒 | 役割 | 映像（画像） | ナレーション | テロップ |
|---|---|---|---|---|---|
| S1 | 0–5 | フック／問題提起 | 夕暮れ、稼働を止めるメガソーラー（画像A） | 「つくられた電気の、その先を考える。」 | — |
| S2 | 5–10 | 課題の可視化 | 送電線と、行き場を失う光の粒子（画像B） | 「再生可能エネルギーは、使いきれずに捨てられることがある。」 | 出力制御という"もったいない" |
| S3 | 10–16 | ソリューション登場 | 系統用蓄電池施設のワイド（画像C） | 「その電気を、無駄にしない。」 | 系統用蓄電池 |
| S4 | 16–22 | 価値①蓄える | 蓄電池に光が吸い込まれるイメージ（画像D） | 「あまった力を、蓄えて。」 | 貯めて、活かす |
| S5 | 22–27 | 価値②灯す | 夜、貯めた電気が街を灯す（画像E） | 「必要なときに、社会へ届ける。」 | 電力の安定と、脱炭素へ |
| S6 | 27–30 | ロゴ／CTA | 朝焼け＋施設のシルエット→ロゴ（画像F） | 「Green Battery。」 | ロゴ＋タグライン |

---

## 3. フェーズ1: DALL·E 3 プロンプト（実写風シネマティック・英語）

### 共通ルール（この案件版）
- **施設記述ブロックを1つ確定し、施設が映る全カット（C・D・E・F）で一字一句コピーする**（施設の見た目を全カットで統一するため）
- ラベル・看板に文字は入れない（`no readable text, no logos`）
- 全プロンプト末尾を固定: `cinematic, photoreal, ultra realistic, natural lighting, 4k`

**施設記述ブロック（確定・以下を全カットにコピー）:**
`a row of modern grid-scale battery storage units, clean white containers with green accent panels, arranged neatly beside a large solar panel field, distant transmission towers, green hills on the horizon`

### 画像A｜S1用（夕暮れのメガソーラー）
```
A vast solar panel field at golden dusk, endless rows of photovoltaic panels reflecting warm orange sky, gentle lens flare, calm quiet atmosphere, wide aerial establishing shot, cinematic, photoreal, ultra realistic, natural lighting, 4k
```

### 画像B｜S2用（送電線と失われる光）
```
High-voltage transmission towers and power lines stretching across a wide landscape at dusk, faint glowing light particles drifting away and fading into the darkening sky, sense of energy being lost, moody cinematic atmosphere, no readable text, no logos, cinematic, photoreal, ultra realistic, natural lighting, 4k
```

### 画像C｜S3用（蓄電池施設ワイド）
```
A row of modern grid-scale battery storage units, clean white containers with green accent panels, arranged neatly beside a large solar panel field, distant transmission towers, green hills on the horizon, wide cinematic establishing shot under soft daylight, no readable text, no logos, cinematic, photoreal, ultra realistic, natural lighting, 4k
```

### 画像D｜S4用（蓄える）
```
Close-up of a row of modern grid-scale battery storage units, clean white containers with green accent panels, arranged neatly beside a large solar panel field, distant transmission towers, green hills on the horizon, soft green light glowing gently along the seams of the containers as if energy is being absorbed, twilight, no readable text, no logos, cinematic, photoreal, ultra realistic, natural lighting, 4k
```

### 画像E｜S5用（夜、街を灯す）
```
A row of modern grid-scale battery storage units, clean white containers with green accent panels, arranged neatly beside a large solar panel field, distant transmission towers, green hills on the horizon, at night, warm city lights glowing brightly in the distant valley, subtle green energy light flowing from the facility toward the city, hopeful atmosphere, no readable text, no logos, cinematic, photoreal, ultra realistic, natural lighting, 4k
```

### 画像F｜S6用（朝焼け・ロゴ用余白）
```
A row of modern grid-scale battery storage units, clean white containers with green accent panels, arranged neatly beside a large solar panel field, distant transmission towers, green hills on the horizon, silhouetted against a beautiful sunrise, warm hopeful golden light, wide cinematic shot, leave large empty space in the upper center for a logo, no readable text, no logos, cinematic, photoreal, ultra realistic, natural lighting, 4k
```

---

## 4. フェーズ2: Kling プロンプト（各カット・英語）
動きは1カット1つ。末尾固定: `slow motion, cinematic, photoreal, no text`

### S1（0–5s）→ 画像A（画像から動画）
```
slow cinematic aerial push-in over the solar field as the golden sunset light shifts gently, slow motion, cinematic, photoreal, no text
```

### S2（5–10s）→ 画像B（画像から動画）
```
faint glowing light particles drift away from the power lines and slowly fade into the sky, slow motion, cinematic, photoreal, no text
```

### S3（10–16s）→ 画像C（画像から動画）
```
slow cinematic dolly push-in toward the battery storage facility, slow motion, cinematic, photoreal, no text
```

### S4（16–22s）→ 画像D（画像から動画）
```
soft green light gently flows along the seams of the storage containers as energy is absorbed, slow motion, cinematic, photoreal, no text
```

### S5（22–27s）→ 画像E（画像から動画）
```
green energy light flows from the facility toward the distant city as the city lights brighten, slow motion, cinematic, photoreal, no text
```

### S6（27–30s）→ 画像F（画像から動画）
```
slow gentle push-in on the facility silhouette as the sunrise light grows warmer, slow motion, cinematic, photoreal, no text
```

---

## 5. フェーズ3: 編集指示
1. S1→S6 を時系列連結。カット間は 0.4〜0.6秒のゆっくりしたクロスディゾルブ（時間経過＝昼→夜→朝を滑らかに見せる）
2. **音楽**: 静かに始まり後半で希望的に盛り上がるオーケストラ／アンビエント（環境音: 微風・低い電気のハム音をS4で薄く）
3. **カラーグレーディング**: 前半（S1-S2）は少し寂しげな寒色〜夕景、S3以降でGreen Batteryのグリーンを差し色に、S5-S6で暖色の希望トーンへ。**企業カラーのグリーンをアクセントに統一**
4. **ナレーション**: 落ち着いた信頼感のある声（男女どちらでも可）。上表の通り。BGMより前に出す
5. **テロップ**: 明朝 or 端正なゴシック、白＋グリーンの下線。上表の通り
6. ラスト3秒（S6）で**ロゴ＋タグライン**を編集で合成。ロゴは画像Fの上部余白へ
7. 書き出し: 1080p（可能なら4K納品）/ MP4 / H.264

---

## 6. 制作チェックリスト
- [ ] 施設記述ブロックが C・D・E・F で一字一句同じ
- [ ] 全プロンプトに文字・ロゴ・実在ブランド名が入っていない（no readable text, no logos）
- [ ] ナレーションに未確認の数値・実績・顧客名が入っていない（`【要確認】`のまま残っていないか）
- [ ] DALL·E末尾が cinematic, photoreal, ultra realistic, natural lighting, 4k
- [ ] Kling末尾が slow motion, cinematic, photoreal, no text
- [ ] 各Klingの動きが1つだけ
- [ ] ロゴ・社名・タグラインは編集で合成する前提になっている
- [ ] 「イメージ映像」であることをクライアントと共有済み
- [ ] 納品前にクライアント確認を通す

---

## 7. 制作前にクライアントへ確認したいこと（任意）
1. 尺は30秒でよいか（15/60秒の希望はないか）
2. ロゴデータ（透過PNG）とブランドカラーの正確な指定（グリーンのカラーコード）
3. ナレーション原稿の最終文言と、入れてよい数値・実績の有無
4. 実在施設の映像を一部使いたいか（あれば提供素材と差し替え）
5. 音楽の指定・支給の有無
