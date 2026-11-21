// Keyboard-focus a key control on each page and photograph the ring in context.
const { chromium } = require('C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/playwright');
const T = {
  'lamplight/student': ['.q-look', '.paper .btn-ink'], 'lamplight/teacher': ['.q-look', '#find'],
  'carrel/student': ['.icard__tab >> nth=1', '#stack'], 'carrel/teacher': ['#drum', '.check >> nth=1'],
  'marginalia/student': ['.tok >> nth=1', '.cta'], 'marginalia/teacher': ['.tok >> nth=0', '#who'],
};
(async () => {
  const b = await chromium.launch({ channel: 'msedge' });
  for (const [p, sels] of Object.entries(T)) {
    const page = await (await b.newContext({ viewport: { width: 1440, height: 900 } })).newPage();
    await page.goto('http://localhost:8120/LSAT-U-Dashboard-Three-Directions-v2/' + p + '.html', { waitUntil: 'networkidle' });
    await page.waitForTimeout(2600);
    let k = 0;
    for (const s of sels) {
      const el = page.locator(s).first();
      await el.scrollIntoViewIfNeeded();
      await page.keyboard.press('Tab'); // switch the page into keyboard modality
      await el.focus();
      await page.waitForTimeout(500);
      const bb = await el.boundingBox();
      await page.screenshot({ path: `focus/${p.replace('/', '-')}-ring${k++}.png`, clip: { x: Math.max(0, bb.x - 40), y: Math.max(0, bb.y - 40), width: Math.min(1440, bb.width + 80), height: Math.min(900, bb.height + 80) } });
    }
    await page.context().close();
  }
  await b.close(); console.log('done');
})();
