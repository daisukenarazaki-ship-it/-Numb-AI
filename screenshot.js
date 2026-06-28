const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({
    executablePath: '/opt/pw-browsers/chromium',
    args: ['--use-gl=angle','--use-angle=swiftshader','--enable-webgl','--ignore-gpu-blocklist']
  });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1440, height: 900 });
  await page.goto('file:///home/user/-Numb-AI/index.html');
  await page.mouse.move(720, 380);
  await page.waitForTimeout(2000);
  await page.screenshot({ path: '/tmp/claude-0/-home-user--Numb-AI/0ee5fc8f-51cd-521f-bbee-6dd53338c470/scratchpad/desktop.png' });
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto('file:///home/user/-Numb-AI/index.html');
  await page.waitForTimeout(2000);
  await page.screenshot({ path: '/tmp/claude-0/-home-user--Numb-AI/0ee5fc8f-51cd-521f-bbee-6dd53338c470/scratchpad/mobile.png' });
  await browser.close();
})();
