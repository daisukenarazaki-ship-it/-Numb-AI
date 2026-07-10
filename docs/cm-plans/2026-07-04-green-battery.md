# 【CM台本＋制作指示】株式会社Green Battery — 米国Netflix 15秒 ブランドムービー（日本発を前面に）
生成日: 2026-07-04 ／ クライアント案件（プロ制作・クオリティ重視）

## 0. この案件のブリーフ
- **尺**: 15秒（Netflix 標準広告枠）
- **掲載先**: Netflix（米国）CM枠 → **視聴者は米国の一般層。言語は英語（American English）**
- **目的**: ①米国での知名度・ブランド認知 ②投資家への訴求（スケール・成長性・信頼） ③同業（系統用蓄電池）買収を視野にしたポジショニング
- **クリエイティブの軸（今回の核）**: **「日本発の企業であること」を前面に。** 日本の歴史・風景・文化でまず心を掴み、日本語「**もったいない（Mottainai）**」の精神＝再エネを無駄にしない事業、へ橋渡しする
- **スタイル**: 実写風シネマティック（日本の荘厳な原風景 × 最新の蓄電インフラ）
- **語り**: 英語ナレーション（最小限）＋英語テロップ＋日本語キーワード演出＋ロゴ

### なぜこの軸が効くか（提案意図）
- 「もったいない」はGreen Batteryの公式ミッション（[出典](https://greenbattery.co.jp/services/)）そのもの。作り話ではなく**本物のブランドストーリー**
- 米国では "Mottainai" は環境思想の言葉として知られ、**日本らしさ＋事業内容が一語で両立**する
- 「日本のものづくり＝精密・高信頼・長期目線」は**投資家・買収文脈での信頼感**に直結

> ⚠️ 制作上の重要注意（厳守）
> - **投資リターン／利回りを約束・示唆する表現を入れない**（米国の証券・広告規制リスク。ブランド認知に徹する）
> - **数値・実績・顧客名・シェアを勝手に入れない**。事実確認済みのみクライアントが埋める（台本は `【要確認】`）
> - **旭日旗（radiating-rays military flag）を想起させるデザインは使わない。** 使うのは自然な「朝日／日の出」まで（一部アジア地域で政治的に敏感なため。プロンプトにも `natural rising sun, no flags` を明記）
> - 日本語テロップ「もったいない／勿体無い」やロゴ・社名・タグラインは**AI生成に含めず編集で合成**（AIは文字を崩す）。表記（かな/漢字/ローマ字）はクライアント確認
> - AI生成映像は**実在のGreen Battery施設ではないイメージ映像**。実写と誤認させない
> - **Netflix（米国）広告の技術要件**（尺きっかり15秒／16:9・1080p以上・ラウドネス規定・過度なフラッシュ禁止・字幕要否）に書き出しを合わせる。代理店指定が最優先

---

## 1. コンセプト
**"From the land of the rising sun — waste nothing."**
日出づる国・日本の朝日と原風景で始まり、「もったいない」の精神を提示 → その思想で再エネを蓄える最新インフラへ → 未来を灯す。**伝統の美 × 最先端技術**のギャップで、静かな感動と信頼を15秒に凝縮する。

### 英語タグライン3案（ロゴ横に編集で合成）
1. **"Mottainai. Waste nothing."**
2. **"From Japan. Powering what's next."**
3. **"Store the future."**

### エンドカードの出し分け（用途別・任意）
- Netflix一般枠: ロゴ＋タグラインのみ（クリーンに）
- 投資家・商談用の別バージョン: 末尾に小さく `Partner with us — {米国向けURL【要確認】}` を追加（Netflix入稿版には入れない）

---

## 2. 構成（15秒・4ブロック）
15秒はVOを詰め込まない。**英語ナレーションは合計で短く（約16語）**、日本の映像美とテロップで見せる。

| # | 秒 | 役割 | 映像（画像） | 英語VO | テロップ演出 |
|---|---|---|---|---|---|
| S1 | 0–4 | 心を掴む／日本の朝 | 富士山と桜、昇る朝日（画像A） | "In Japan, there is a word." | — |
| S2 | 4–8 | 思想の提示 | 桜舞う静謐な日本の風景（画像B） | "Mottainai. Waste nothing precious." | 勿体無い / MOTTAINAI（編集で合成） |
| S3 | 8–12 | 伝統×技術の橋渡し | 日本の風景に建つ蓄電池施設・富士遠景（画像C） | "So we store clean energy—" | GRID-SCALE ENERGY STORAGE |
| S4 | 12–15 | 未来／ロゴ | 朝日と施設シルエット→ロゴ（画像D） | "—to power what's next." | ロゴ＋タグライン |

> ナレーション総量 約16語。落ち着いた、品格ある米国ネイティブの声。間と余白を大切に。"Mottainai" は丁寧に発音（モッタイナイ）。

---

## 3. フェーズ1: DALL·E 3 プロンプト（実写風シネマティック・英語）

### 共通ルール（この案件版）
- **施設記述ブロックを1つ確定し、施設が映る全カット（C・D）で一字一句コピーする**
- 看板・ラベル・旗に文字/紋章を入れない（`no readable text, no logos, no flags`）
- 朝日は自然な太陽のみ（`natural rising sun`）。旭日旗デザインは禁止
- 全プロンプト末尾を固定: `cinematic, photoreal, ultra realistic, natural lighting, epic scale, 4k`

**施設記述ブロック（確定・C・Dにコピー）:**
`a row of modern grid-scale battery storage units, clean white containers with green accent panels, arranged neatly beside a solar panel field, set in a serene Japanese countryside with green mountains and a distant snow-capped Mt. Fuji`

### 画像A｜S1用（富士山・桜・朝日）
```
A breathtaking view of snow-capped Mt. Fuji at dawn, soft pink cherry blossom branches in the foreground, a gentle natural rising sun casting warm golden light, calm serene timeless Japanese landscape, delicate morning mist, epic cinematic wide shot, natural rising sun, no flags, cinematic, photoreal, ultra realistic, natural lighting, epic scale, 4k
```

### 画像B｜S2用（桜舞う静謐な風景）
```
Soft cherry blossom petals drifting gently through the air over a serene traditional Japanese landscape, quiet countryside with green hills and a calm river, warm soft morning light, peaceful contemplative mood, shallow depth of field, no readable text, no logos, no flags, cinematic, photoreal, ultra realistic, natural lighting, epic scale, 4k
```

### 画像C｜S3用（日本の風景に建つ蓄電池施設）
```
A row of modern grid-scale battery storage units, clean white containers with green accent panels, arranged neatly beside a solar panel field, set in a serene Japanese countryside with green mountains and a distant snow-capped Mt. Fuji, soft morning daylight, harmony of tradition and advanced technology, powerful cinematic wide shot, no readable text, no logos, no flags, cinematic, photoreal, ultra realistic, natural lighting, epic scale, 4k
```

### 画像D｜S4用（朝日・施設シルエット・ロゴ余白）
```
A row of modern grid-scale battery storage units, clean white containers with green accent panels, arranged neatly beside a solar panel field, set in a serene Japanese countryside with green mountains and a distant snow-capped Mt. Fuji, silhouetted against a beautiful natural rising sun, warm hopeful golden light, epic wide cinematic shot, leave large empty space in the upper center for a logo, natural rising sun, no readable text, no logos, no flags, cinematic, photoreal, ultra realistic, natural lighting, epic scale, 4k
```

---

## 4. フェーズ2: Kling プロンプト（各カット・英語）
動きは1カット1つ。末尾固定: `slow motion, cinematic, photoreal, no text`

### S1（0–4s）→ 画像A（画像から動画）
```
slow cinematic push-in toward Mt. Fuji as the rising sun light grows warmer and a few cherry blossom petals drift gently, slow motion, cinematic, photoreal, no text
```

### S2（4–8s）→ 画像B（画像から動画）
```
cherry blossom petals drift slowly through the air across the peaceful landscape, slow motion, cinematic, photoreal, no text
```

### S3（8–12s）→ 画像C（画像から動画）
```
slow cinematic dolly push-in toward the battery storage facility with Mt. Fuji in the distance, slow motion, cinematic, photoreal, no text
```

### S4（12–15s）→ 画像D（画像から動画）
```
slow gentle push-in on the facility silhouette as the rising sun light grows warmer and brighter, slow motion, cinematic, photoreal, no text
```

---

## 5. フェーズ3: 編集指示
1. S1→S4 を時系列連結。カット間は 0.3〜0.5秒のクロスディゾルブ（間を活かしつつダレさせない）
2. **音楽**: 和のエッセンス（尺八・琴・和太鼓の一打など）を静かに織り込みつつ、S3-S4で希望的に高揚するシネマティック／オーケストラ。米国プレミアム広告の格。ラウドネスはNetflix規定
3. **カラーグレーディング**: 全体は朝の暖色・自然光基調。**企業カラーのグリーンを施設で差し色に**。桜のピンク→朝日のゴールドの流れを美しく
4. **ナレーション**: 品格ある米国ネイティブ、落ち着いた声。上表の英語VO（"Mottainai" は丁寧に発音）
5. **テロップ**: 上品なサンセリフ（英語）＋日本語「勿体無い / もったいない」を明朝系で美しく。S2で `勿体無い（MOTTAINAI）`、S3で `GRID-SCALE ENERGY STORAGE`。**すべて編集で合成**
6. ラスト（S4）で**ロゴ＋英語タグライン**を朝日の余白へ合成。必要なら小さく `A Japanese company`（任意）
7. **書き出し**: Netflix入稿仕様に準拠（尺きっかり15.0秒／16:9／1080p以上・可能なら4K／H.264 or ProRes／ラウドネス規定・字幕要否）

---

## 6. 制作チェックリスト
- [ ] 施設記述ブロックが C・D で一字一句同じ
- [ ] 全プロンプトに文字・ロゴ・旗が入っていない（no readable text, no logos, no flags）
- [ ] 旭日旗を想起させる意匠がない（朝日は自然な太陽のみ）
- [ ] ナレーション・テロップに未確認の数値・実績・顧客名が入っていない
- [ ] **投資リターン／利回りを約束・示唆する表現がない**
- [ ] 英語は American English で統一
- [ ] 日本語テロップ「もったいない」の表記をクライアント確認済み
- [ ] DALL·E末尾が cinematic, photoreal, ultra realistic, natural lighting, epic scale, 4k
- [ ] Kling末尾が slow motion, cinematic, photoreal, no text
- [ ] 各Klingの動きが1つだけ
- [ ] ロゴ・社名・タグラインは編集で合成する前提
- [ ] 尺きっかり15秒／Netflix技術要件に準拠
- [ ] 「イメージ映像」であることをクライアントと共有済み
- [ ] 納品前にクライアント確認を通す

---

## 7. 制作前にクライアントへ確認したいこと
1. Netflix（米国）**広告入稿の技術仕様**（尺・解像度・コーデック・ラウドネス・字幕要否）。代理店経由なら代理店指定
2. **ロゴデータ（透過PNG）とブランドカラー**（グリーンのカラーコード）
3. 英語ナレーションの**最終文言**、日本語テロップ「もったいない」の**表記（かな/漢字/ローマ字）**
4. 「もったいない」を核にする**方向性の承認**（会社ミッションと一致するため相性は良いが最終判断はクライアント）
5. 米国向けに出す**URL/ドメイン**と "Green Battery" の**米国商標状況**
6. 投資家・商談用の**別エンドカード**（`Partner with us` 版）を作るか
7. 実在施設の映像を一部使いたいか（あれば提供素材と差し替え）
