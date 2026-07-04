---
name: works-update
description: YouTube URLを受け取り、index.html の Works セクションに実績カードを追加してコミットする。「この動画をWorksに載せて」「実績を追加して」と言われたら使う。push（＝GitHub Pages公開）前に必ず人間の確認を取る。
---

# /works-update — YouTube URL → Worksカード追加

## このSkillがやること
-Numb-AI リポジトリの `index.html` にある Works セクションへ、新しい実績カードを**1枚追加**し、コミットする。

## やらないこと（重要）
- **確認なしの push**。`main` への push は GitHub Pages への**公開**を意味する（`.github/workflows/deploy.yml` が動く）。push 前に必ず追加内容を見せて人間のOKを取る
- 既存カードの編集・削除・並べ替え
- `index.html` の Works セクション以外の変更

---

## STEP 1: 入力の確認

| 項目 | 必須? | 未指定時 |
|---|---|---|
| YouTube URL または動画ID | **必須。無ければここだけ質問して止まる** | — |
| タイトル | — | 動画の内容をユーザー発言から推測。不明なら「AI Video Sample」とし【要確認】を付ける |
| カテゴリ表記 | — | STEP 4 の規則で選ぶ |
| 説明文（日本語） | — | STEP 4 の規則で書く |

## STEP 2: 動画IDを抽出する
以下のどのURL形式でも `[A-Za-z0-9_-]{11}` の11文字IDを取り出す:
- `https://www.youtube.com/watch?v=ID`
- `https://youtu.be/ID`
- `https://www.youtube.com/shorts/ID`
- `https://www.youtube.com/embed/ID`
- ID単体（11文字）

11文字ちょうどで抽出できなければ、URLをそのまま示して「このURLからIDを特定できませんでした」とユーザーに聞く。**推測でIDをでっち上げることは禁止。**

## STEP 3: 検証（コードを書き換える前に必ず全部やる）
1. **重複チェック**: `grep 'data-yt="{ID}"' index.html` — ヒットしたら「既に掲載済み」と報告して**終了**（何も変更しない）
2. **サムネイル存在チェック**: `curl -sI -o /dev/null -w "%{http_code}" "https://img.youtube.com/vi/{ID}/hqdefault.jpg"` が `200` であること。`404` なら動画が非公開/ID誤りの可能性。**カードは追加せず**その旨を報告して終了。（ネットワークが無い環境ではスキップし、完了報告に「サムネ未確認」と書く）

## STEP 4: カードのテキストを決める（判断基準）
- **カテゴリ表記**: 既存の形式に必ず合わせる — 大文字英語で `分野 · 種別`（中黒 `·` を使う）。既存の値から選ぶのが基本:
  - `AI VIDEO · PRODUCTION`（汎用のAI動画）
  - `AI MODEL · PRODUCTION`（AIモデル・人物もの）
  - `TV CM · COSMETICS` のように `TV CM · {業界英語1語}`（CM作品）
- **タイトル**: 商品名 or ブランド名（英字推奨、最大25文字）
- **説明文**: 日本語40〜70文字。既存カードのトーンに合わせる（例: 「〇〇のAI制作CMサンプル。企画・映像生成・編集までワンストップで対応。」）。誇張・実在クライアント名の捏造は禁止

## STEP 5: カードを挿入する
`index.html` 内の `<div class="works-scroll">` の**直後**（＝先頭カードの前、最新が先頭）に、次のHTMLを**そのままの構造で**挿入する。`{ID}` は2箇所とも同じIDにする:

```html
        <div class="work-card fu">
          <div class="work-thumb work-video" data-yt="{ID}"
               style="background-image:url('https://img.youtube.com/vi/{ID}/hqdefault.jpg'); background-size:cover; background-position:center;">
            <div class="work-overlay"></div>
            <div class="work-play-btn">▶</div>
            <span class="work-play-hint">クリックで再生</span>
          </div>
          <div class="work-body">
            <div class="work-cat">{カテゴリ表記}</div>
            <h3>{タイトル}</h3>
            <p>{説明文}</p>
          </div>
        </div>
```

### NG例
| NG | 理由 |
|---|---|
| `<iframe>` を直接書く | click-to-play方式（`data-yt` をJSが拾う）が壊れる |
| `fu` クラスを外す | スクロール時のフェードイン演出が消える |
| `data-yt` と `background-image` のIDが不一致 | サムネと再生動画がズレる |
| `maxresdefault.jpg` を使う | 動画によっては404になる。`hqdefault.jpg` 固定 |
| works-scroll の外に挿入 | レイアウト崩壊 |

## STEP 6: 検証してからコミット
1. `grep -c 'class="work-card fu"' index.html` が**変更前より1増えている**こと
2. 追加した `data-yt` のIDと `img.youtube.com/vi/{ID}` のIDが一致していること
3. `python3 -m http.server 8000` でローカル表示できる環境なら目視確認（できなければ diff 確認で代替）
4. コミット: メッセージは `Add work: {タイトル} (YouTube {ID})`

## STEP 7: 人間の確認 → push
**push はまだしない。** 追加したカードのHTMLと、タイトル・カテゴリ・説明文をチャットに示し、
「このまま push（＝サイト公開）してよいですか？」と確認する。
OKが出たら `git push -u origin {現在のブランチ}`。**`main` に直接いる場合も、公開してよいか必ず確認してから push する。**

## 完了報告のしかた
- 追加したカードの内容（タイトル/カテゴリ/説明/ID）
- 検証結果（重複なし・サムネ200・カード数+1）
- push したか、確認待ちか
