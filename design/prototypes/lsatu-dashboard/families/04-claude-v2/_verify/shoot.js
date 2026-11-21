// Full-page screenshots of the three directions at desktop and phone widths.
// usage: node shoot.js [filter] [state]
const { chromium } = require('C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/playwright');
const path = require('path');
const fs = require('fs');

const BASE = 'http://localhost:8120/LSAT-U-Dashboard-Three-Directions-v2/';
const OUT = 'C:/Users/Joshu/Downloads/LSAT-U-Dashboard-Three-Directions-v2/screenshots';
const filter = process.argv[2] || '';
const state = process.argv[3] || 'full';
const pages = ['lamplight/student', 'lamplight/teacher', 'carrel/student', 'carrel/teacher', 'marginalia/student', 'marginalia/teacher']
  .filter((p) => p.includes(filter));
const widths = (process.argv[4] || '1440,390').split(',').map(Number);

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch({ channel: 'msedge' });
  for (const p of pages) {
    for (const w of widths) {
      const ctx = await browser.newContext({ viewport: { width: w, height: w > 600 ? 900 : 844 }, deviceScaleFactor: 1 });
      const page = await ctx.newPage();
      const errors = [];
      page.on('pageerror', (e) => errors.push(e.message));
      page.on('console', (m) => { if (m.type() === 'error') errors.push(m.text()); });
      await page.goto(BASE + p + '.html' + (state !== 'full' ? '?state=' + state : ''), { waitUntil: 'networkidle' });
      await page.waitForTimeout(2600);
      // walk down the page so scroll-triggered reveals fire, then settle back at the top
      const h = await page.evaluate(() => document.documentElement.scrollHeight);
      for (let y = 0; y < h; y += 500) { await page.evaluate((yy) => window.scrollTo(0, yy), y); await page.waitForTimeout(140); }
      await page.waitForTimeout(1600);
      await page.evaluate(() => window.scrollTo(0, 0));
      await page.waitForTimeout(400);
      const overflow = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
      const name = `${p.replace('/', '-')}-${w}${state !== 'full' ? '-' + state : ''}.png`;
      await page.addStyleTag({ content: '.sample-bar{display:none!important}' });
      await page.screenshot({ path: path.join(OUT, name), fullPage: true });
      console.log(name, 'h=' + h, 'overflowX=' + overflow, errors.length ? 'ERR ' + errors.join(' | ') : 'ok');
      await ctx.close();
    }
  }
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
