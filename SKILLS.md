# Banana Technology 副業Skill集

副業（AI CM制作 / サイト運用 / 営業）の定型作業を、どのClaudeモデルでも再現できる手順書（Skill）にしたもの。
実体は `.claude/skills/` にあり、このリポジトリを Claude Code で開くと自動で読み込まれる。

## Skill一覧

| Skill | 入力 | 出力 | 目安時間削減 |
|---|---|---|---|
| `/cm-plan` | 商材カテゴリ＋商品情報（不足は自動補完） | CM企画一式（カット割り・DALL·E 3プロンプト5枚・Klingプロンプト5本・編集指示）→ `docs/cm-plans/` | プロンプト設計 2〜3時間 → 10分＋確認 |
| `/works-update` | YouTube URL | `index.html` のWorksカード追加＋コミット（push前に人間確認） | 30分 → 5分 |
| `/sales-doc` | 案件情報＋文書タイプ | 初回返信/提案書/見積もり/納品メール → `docs/sales/` | 30〜60分 → 10分＋【要確認】埋め |

## 呼び出し方（Opus 4.8 などの普段のモデルで）

1. **Claude Code でこのリポジトリを開いている場合**: そのまま `/cm-plan` のようにスラッシュコマンドで呼ぶか、「化粧水のCM企画を作って」のように話す（description で自動発動する）
2. **他のプロジェクトや claude.ai チャットで使う場合**: 該当する `.claude/skills/〇〇/SKILL.md` の本文をそのまま貼り付けて「この手順書に従って」と依頼する
3. **どのプロジェクトでも使えるようにする場合（個人Skill化）**:
   ```bash
   mkdir -p ~/.claude/skills
   cp -r .claude/skills/* ~/.claude/skills/
   ```

## 別リポジトリに移したい場合

このセッションのGitHub権限では新規リポジトリを作成できなかったため、Skillは本リポジトリに置いている。
分離したくなったら GitHub で空リポジトリ `numb-ai-skills` を作ってから:

```bash
mkdir numb-ai-skills && cp -r .claude SKILLS.md numb-ai-skills/
cd numb-ai-skills && git init && git add -A && git commit -m "Import skills" \
  && git remote add origin git@github.com:daisukenarazaki-ship-it/numb-ai-skills.git && git push -u origin main
```

## 安全ルール（全Skill共通）

- **push・送信・公開・課金はSkillが勝手にやらない。** works-update のpush（＝GitHub Pages公開）と営業メール送信は必ず人間が最終確認する
- 金額・納期は人間が確定する（`【要確認】` マーカーが残る文書は下書き）
- 実在の人物・ブランドをプロンプトや文書に入れない
- クライアント情報を Works・プロンプト・コミットメッセージに転記しない

## 週次の運用手順（2026-07-08以降、Fable 5なしで回す）

1. **案件が来たら** → `/sales-doc` で初回返信 →（受注方向なら）`/cm-plan` で企画一式 → `/sales-doc` で提案書。企画のカット割り表は提案書に転載する
2. **動画が完成したら** → YouTubeに限定公開/公開でアップ → `/works-update` にURLを渡す → 差分を確認してpush
3. **月1メンテ** → 実際に使って引っかかった点（Klingで破綻した動き、DALL·Eの拒否など）を該当Skillの「NG例」表に1行追記する。Skillは使うたびに賢くなる資産として育てる
