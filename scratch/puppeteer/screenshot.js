const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: 'new' });
  const viewports = [
    { width: 1440, height: 900, name: '1440x900' },
    { width: 1366, height: 768, name: '1366x768' },
    { width: 1280, height: 800, name: '1280x800' },
    { width: 1024, height: 768, name: '1024x768' },
    { width: 390, height: 844, name: '390x844' }
  ];

  const page = await browser.newPage();
  
  for (const vp of viewports) {
    await page.setViewport({ width: vp.width, height: vp.height });
    await page.goto('https://lsatprep.study/classroom/drill?section=lr', { waitUntil: 'networkidle0', timeout: 30000 });
    // Wait a bit extra for dynamic content
    await new Promise(r => setTimeout(r, 3000));
    await page.screenshot({ path: `screenshot_${vp.name}.png`, fullPage: false });
  }

  await browser.close();
})();
