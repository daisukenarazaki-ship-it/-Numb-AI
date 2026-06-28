const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage();
  
  await page.setViewportSize({ width: 390, height: 844 }); // iPhone 14
  await page.goto('file:///home/user/-Numb-AI/index.html');
  await page.waitForTimeout(1500);
  await page.screenshot({ path: '/tmp/claude-0/-home-user--Numb-AI/0ee5fc8f-51cd-521f-bbee-6dd53338c470/scratchpad/mobile.png', fullPage: false });
  
  // Hero section
  await page.screenshot({ path: '/tmp/claude-0/-home-user--Numb-AI/0ee5fc8f-51cd-521f-bbee-6dd53338c470/scratchpad/hero.png' });
  
  // Scroll to services
  await page.evaluate(() => document.getElementById('services').scrollIntoView());
  await page.waitForTimeout(800);
  await page.screenshot({ path: '/tmp/claude-0/-home-user--Numb-AI/0ee5fc8f-51cd-521f-bbee-6dd53338c470/scratchpad/services.png' });

  // Desktop view
  await page.setViewportSize({ width: 1440, height: 900 });
  await page.goto('file:///home/user/-Numb-AI/index.html');
  await page.waitForTimeout(1500);
  await page.screenshot({ path: '/tmp/claude-0/-home-user--Numb-AI/0ee5fc8f-51cd-521f-bbee-6dd53338c470/scratchpad/desktop.png', fullPage: false });

  await browser.close();
})();
