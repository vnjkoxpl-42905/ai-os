// Captures real reference pages at desktop and phone width for visual study.
const { chromium } = require('C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/playwright');
const OUT = 'C:/Users/Joshu/Downloads/LSAT-U-Dashboard-Three-Directions-v2/_research/shots';
const refs = process.argv.slice(2);
(async () => {
  require('fs').mkdirSync(OUT, { recursive: true });
  const b = await chromium.launch({ channel: 'msedge' });
  for (const r of refs) {
    const [name, url] = r.split('=');
    for (const w of [1440, 390]) {
      const p = await (await b.newContext({ viewport: { width: w, height: w > 600 ? 900 : 844 } })).newPage();
      try { await p.goto(url, { waitUntil: 'networkidle', timeout: 45000 }); } catch (e) { console.log(name, 'load:', e.message.slice(0, 80)); }
      await p.waitForTimeout(2500);
      await p.mouse.wheel(0, 900); await p.waitForTimeout(1200);
      await p.screenshot({ path: `${OUT}/${name}-${w}.jpg`, type: 'jpeg', quality: 70 });
      console.log(name, w, 'ok');
    }
  }
  await b.close();
})();
