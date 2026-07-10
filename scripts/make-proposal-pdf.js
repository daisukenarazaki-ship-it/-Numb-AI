// 提案書HTML → PDF 書き出し（無料・外部ツール不要）
// 使い方: PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1 npm install playwright
//         node scripts/make-proposal-pdf.js [入力.html] [出力.pdf]
// プリインストールのChromiumを使うため、環境により executablePath は自動探索します。
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const SRC = process.argv[2] || path.join(__dirname, '../docs/cm-plans/green-battery-proposal.html');
const OUT = process.argv[3] || SRC.replace(/\.html?$/, '.pdf');

function findChromium() {
  // Claude Code on the web のプリインストール場所を優先探索
  const base = '/opt/pw-browsers';
  try {
    const dir = fs.readdirSync(base).find(d => /^chromium-\d+$/.test(d));
    if (dir) {
      const p = path.join(base, dir, 'chrome-linux/chrome');
      if (fs.existsSync(p)) return p;
    }
  } catch (_) {}
  return undefined; // 見つからなければ Playwright 既定
}

(async () => {
  const inner = fs.readFileSync(SRC, 'utf8');
  // Artifact用の本文のみHTMLを完全な文書に包む。印刷はライトテーマ固定。
  const html = `<!doctype html><html lang="ja" data-theme="light"><head><meta charset="utf-8">
    <meta name="viewport" content="width=1120">
    <style>html,body{margin:0;padding:0} @media print{ .wrap{max-width:1000px} }</style>
  </head><body>${inner}</body></html>`;

  const browser = await chromium.launch({ executablePath: findChromium() });
  const page = await browser.newPage({ viewport: { width: 1120, height: 1600 } });
  await page.setContent(html, { waitUntil: 'load' });
  await page.emulateMedia({ media: 'print' });
  await page.waitForTimeout(400);
  await page.pdf({
    path: OUT, format: 'A4', landscape: true, printBackground: true,
    margin: { top: '8mm', bottom: '8mm', left: '8mm', right: '8mm' }, scale: 0.78,
  });
  await browser.close();
  console.log('PDF written:', OUT, Math.round(fs.statSync(OUT).size / 1024) + ' KB');
})().catch(e => { console.error(e); process.exit(1); });
