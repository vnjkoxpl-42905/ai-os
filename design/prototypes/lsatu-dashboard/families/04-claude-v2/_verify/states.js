// First-screen captures of every page in each non-full state.
const { chromium } = require('C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/playwright');
const fs = require('fs');
const BASE = 'http://localhost:8120/LSAT-U-Dashboard-Three-Directions-v2/';
const OUT = 'C:/Users/Joshu/Downloads/LSAT-U-Dashboard-Three-Directions-v2/_verify/states';
const pages = ['lamplight/student', 'lamplight/teacher', 'carrel/student', 'carrel/teacher', 'marginalia/student', 'marginalia/teacher'];
(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const b = await chromium.launch({ channel: 'msedge' });
  for (const st of ['loading', 'empty', 'error']) {
    let i = 0;
    for (const p of pages) {
      const ctx = await b.newContext({ viewport: { width: 1440, height: 900 } });
      const page = await ctx.newPage();
      const errs = [];
      page.on('pageerror', (e) => errs.push(e.message));
      await page.goto(`${BASE}${p}.html?state=${st}`, { waitUntil: 'networkidle' });
      await page.waitForTimeout(2600);
      await page.screenshot({ path: `${OUT}/${st}-${i++}.png` });
      if (errs.length) console.log(st, p, 'ERR', errs.join(' | '));
      await ctx.close();
    }
  }
  await b.close();
  console.log('done');
})();
