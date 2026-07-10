# 【CM台本＋制作指示】株式会社Green Battery — 米国Netflix 15秒 ブランドムービー
生成日: 2026-07-04 ／ クライアント案件（プロ制作・クオリティ重視）

## 0. この案件のブリーフ
- **尺**: 15秒（Netflix 標準広告枠に合わせる）
- **掲載先**: Netflix（米国）CM枠 → **視聴者は米国の一般層。言語は英語（American English）**
- **目的**:
  1. 米国での**知名度・ブランド認知**の向上
  2. **投資家**への訴求（スケール感・成長性・信頼感を見せる）
  3. 同業（系統用蓄電池）**企業の買収**を視野に入れたポジショニング（「業界を牽引する存在」に見せる）
- **スタイル**: 実写風シネマティック（米国スケールの雄大なランドスケープ）
- **語り**: 英語ナレーション（最小限）＋英語テロップ＋ロゴ
- **訴求軸**: 「捨てられる再エネを蓄え、未来を動かす（Store energy. Power the future.）」

### 事業情報の出典
[事業紹介](https://greenbattery.co.jp/services/) / [会社概要](https://greenbattery.co.jp/en/about-en/)
系統用蓄電池の開発・運用（用地取得〜建設〜運用までワンストップ）／ミッション: 再エネを無駄にしない。

> ⚠️ 制作上の重要注意（米国・投資家向けのため特に厳守）
> - **投資リターンや利回りを約束・示唆する表現を入れない**（米国では証券・広告規制のリスク。ブランド認知に徹する）
> - **具体的な数値・実績（削減率・容量・顧客名・シェア）を勝手に入れない**。事実確認済みのものだけをクライアントに埋めてもらう（台本では `【要確認】`）
> - AI生成映像は**実在のGreen Battery施設ではないイメージ映像**。実写と誤認させない形で提出
> - ロゴ・社名・コピーは**AI生成に含めず編集で合成**（AIは文字を崩す）
> - **Netflix広告の技術要件**（尺きっかり15秒／16:9・1080p以上推奨・ラウドネス規定・過度なフラッシュ禁止 等）に最終書き出しを合わせる。要件はNetflix/配信代理店の最新仕様を必ず確認
> - 米国展開のため **"Green Battery" の米国での商標状況**、および広告に出すURL（.co.jp か 米国向けLP か）をクライアントに要確認

---

## 1. コンセプト
**"The energy we throw away could power tomorrow."**
米国の広大な太陽光・風力の風景で「せっかくの再エネが捨てられている」という気づきを一瞬で提示 → 系統用蓄電池がそれを蓄える → 夜の街を灯す、へと15秒で駆け上がる。スケールと希望で"信頼できる大きな会社"に見せる。

### 英語タグライン3案（ロゴ横に編集で合成）
1. **"Store the future."**
2. **"Don't waste the sun. Store it."**
3. **"Powering what's next."**

### エンドカードの出し分け（用途別・任意）
- Netflix一般枠: ロゴ＋タグラインのみ（クリーンに）
- 投資家・商談用の別バージョン: 末尾に小さく `Partner with us — {米国向けURL【要確認】}` を追加（Netflix入稿版には入れない）

---

## 2. 構成（15秒・4ブロック）
15秒はVOを詰め込まない。**英語ナレーションは合計で短く（約12〜16語）**、あとはテロップと映像で見せる。

| # | 秒 | 役割 | 映像（画像） | 英語ナレーション(VO) | 英語テロップ |
|---|---|---|---|---|---|
| S1 | 0–4 | フック／問題提起 | 夕暮れ、米国の広大な太陽光＋風力（画像A） | "Every day, clean energy goes to waste." | — |
| S2 | 4–9 | ソリューション | 系統用蓄電池施設へゆっくり寄る（画像B） | "We store it." | GRID-SCALE ENERGY STORAGE |
| S3 | 9–13 | ビジョン／価値 | 夜、貯めた電力が街を灯す（画像C） | "Powering what's next." | — |
| S4 | 13–15 | ロゴ／CTA | 朝焼け＋施設シルエット→ロゴ（画像D） | （VOなし／ロゴのみ） | ロゴ＋タグライン |

> ナレーション総量の目安: 上記で約11語。落ち着いた低め〜中音域の信頼感ある声（米国ネイティブ推奨）。ゆっくり、間を活かす。

---

## 3. フェーズ1: DALL·E 3 プロンプト（実写風シネマティック・英語）

### 共通ルール（この案件版）
- **施設記述ブロックを1つ確定し、施設が映る全カット（B・C・D）で一字一句コピーする**（施設の見た目を統一）
- 看板・ラベルに文字を入れない（`no readable text, no logos`）
- 全プロンプト末尾を固定: `cinematic, photoreal, ultra realistic, natural lighting, epic scale, 4k`

**施設記述ブロック（確定・全カットにコピー）:**
`a large row of modern grid-scale battery storage units, clean white containers with green accent panels, arranged neatly beside a vast American solar and wind farm, distant high-voltage transmission towers, wide open plains under a big sky`

### 画像A｜S1用（米国の広大な再エネ・夕暮れ）
```
A vast American renewable energy landscape at golden dusk, endless rows of solar panels and tall wind turbines stretching to the horizon across wide open plains, warm orange sky, gentle lens flare, epic aerial establishing shot, a subtle sense of unused energy fading in the air, cinematic, photoreal, ultra realistic, natural lighting, epic scale, 4k
```

### 画像B｜S2用（蓄電池施設へ寄る）
```
A large row of modern grid-scale battery storage units, clean white containers with green accent panels, arranged neatly beside a vast American solar and wind farm, distant high-voltage transmission towers, wide open plains under a big sky, soft daylight, powerful cinematic wide shot, no readable text, no logos, cinematic, photoreal, ultra realistic, natural lighting, epic scale, 4k
```

### 画像C｜S3用（夜、街を灯す）
```
A large row of modern grid-scale battery storage units, clean white containers with green accent panels, arranged neatly beside a vast American solar and wind farm, distant high-voltage transmission towers, wide open plains under a big sky, at night, a large American city skyline glowing warmly on the horizon, subtle green energy light flowing from the facility toward the city, hopeful powerful atmosphere, no readable text, no logos, cinematic, photoreal, ultra realistic, natural lighting, epic scale, 4k
```

### 画像D｜S4用（朝焼け・ロゴ用余白）
```
A large row of modern grid-scale battery storage units, clean white containers with green accent panels, arranged neatly beside a vast American solar and wind farm, distant high-voltage transmission towers, wide open plains under a big sky, silhouetted against a beautiful sunrise, warm hopeful golden light, epic wide cinematic shot, leave large empty space in the upper center for a logo, no readable text, no logos, cinematic, photoreal, ultra realistic, natural lighting, epic scale, 4k
```

---

## 4. フェーズ2: Kling プロンプト（各カット・英語）
動きは1カット1つ。末尾固定: `slow motion, cinematic, photoreal, no text`

### S1（0–4s）→ 画像A（画像から動画）
```
slow cinematic aerial push-in over the vast solar and wind farm as the golden sunset light shifts gently and the turbines slowly rotate, slow motion, cinematic, photoreal, no text
```

### S2（4–9s）→ 画像B（画像から動画）
```
slow cinematic dolly push-in toward the battery storage facility under soft daylight, slow motion, cinematic, photoreal, no text
```

### S3（9–13s）→ 画像C（画像から動画）
```
green energy light flows from the facility toward the distant city as the city skyline lights brighten, slow motion, cinematic, photoreal, no text
```

### S4（13–15s）→ 画像D（画像から動画）
```
slow gentle push-in on the facility silhouette as the sunrise light grows warmer, slow motion, cinematic, photoreal, no text
```

---

## 5. フェーズ3: 編集指示
1. S1→S4 を時系列連結。カット間は 0.3〜0.5秒のクロスディゾルブ（15秒はテンポ良く。ダレさせない）
2. **音楽**: 静かに始まり、S2〜S3で希望的・力強く盛り上がるシネマティック／オーケストラ。米国のプレミアム広告のトーン。ラウドネスはNetflix規定に合わせる
3. **カラーグレーディング**: S1は夕景の寒色寄り→S2でグリーンを差し色→S3-S4で暖色の希望トーン。**企業カラーのグリーンをアクセントに統一**
4. **ナレーション**: 米国ネイティブ、信頼感のある落ち着いた声。上表の英語VO（合計約11語）
5. **テロップ**: 端正なサンセリフ（Helvetica/Founders系）。英語。S2に `GRID-SCALE ENERGY STORAGE`
6. ラスト2秒（S4）で**ロゴ＋英語タグライン**を編集で合成。ロゴは画像Dの上部余白へ
7. **書き出し**: Netflix入稿仕様に準拠（尺きっかり15.0秒／16:9／1080p以上・可能なら4K／H.264 or ProRes／ラウドネス規定）。詳細はNetflix/代理店の最新仕様を確認

---

## 6. 制作チェックリスト
- [ ] 施設記述ブロックが B・C・D で一字一句同じ
- [ ] 全プロンプトに文字・ロゴ・実在ブランド名が入っていない（no readable text, no logos）
- [ ] ナレーション・テロップに未確認の数値・実績・顧客名が入っていない
- [ ] **投資リターン／利回りを約束・示唆する表現がない**（米国広告・証券規制リスク回避）
- [ ] 英語表記が American English（spelling/語法）で統一
- [ ] DALL·E末尾が cinematic, photoreal, ultra realistic, natural lighting, epic scale, 4k
- [ ] Kling末尾が slow motion, cinematic, photoreal, no text
- [ ] 各Klingの動きが1つだけ
- [ ] ロゴ・社名・タグラインは編集で合成する前提
- [ ] 尺きっかり15秒／Netflix技術要件に書き出しを合わせた
- [ ] 「イメージ映像」であることをクライアントと共有済み
- [ ] 納品前にクライアント確認を通す

---

## 7. 制作前にクライアントへ確認したいこと
1. Netflix（米国）の**広告入稿の技術仕様**（尺・解像度・コーデック・ラウドネス・字幕要否）— 代理店経由なら代理店の指定
2. **ロゴデータ（透過PNG）とブランドカラー**（グリーンのカラーコード）
3. 英語ナレーションの**最終文言**と、入れてよい数値・実績の有無（投資リターン表現は不可の前提）
4. 米国向けに出す**URL/ドメイン**（.co.jp か 米国向けLPか）と、"Green Battery" の**米国での商標状況**
5. 投資家・商談用の**別エンドカード**（`Partner with us` 版）を作るか
6. 実在施設の映像を一部使いたいか（あれば提供素材と差し替え）
