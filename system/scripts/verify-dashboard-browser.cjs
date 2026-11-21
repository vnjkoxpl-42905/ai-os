// Headless visual checkpoints for the existing local dashboard prototypes.
// Usage: node system/scripts/verify-dashboard-browser.cjs [URL] [OUTPUT-DIRECTORY]
const { chromium } = require('C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/playwright');
const fs = require('node:fs');
const path = require('node:path');
const url = process.argv[2] || 'http://127.0.0.1:8120/LSAT-U-Dashboard-Three-Directions-v2/carrel/student.html';
const out = path.resolve(process.argv[3] || 'output/playwright/dashboard-check');

(async () => {
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch({ channel: 'msedge', headless: true });
  const results = [];
  try {
    for (const width of [1440, 390]) {
      const context = await browser.newContext({ viewport: { width, height: 900 }, deviceScaleFactor: 1 });
      try {
        const page = await context.newPage();
        const errors = [], failedResponses = [], failedRequests = [];
        page.on('pageerror', e => errors.push(e.message));
        page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
        page.on('response', r => { if (r.status() >= 400) failedResponses.push({ status: r.status(), url: r.url().split('?')[0] }); });
        page.on('requestfailed', r => failedRequests.push({ url: r.url().split('?')[0], error: r.failure()?.errorText }));
        const response = await page.goto(url, { waitUntil: 'load', timeout: 30000 });
        if (!response?.ok()) throw new Error(`Main page did not load: ${response?.status()}`);
        await page.evaluate(() => document.fonts.ready);
        const clockBefore = await page.evaluate(() => window.gsap?.globalTimeline.time() ?? null);
        // Let the page's own animations run. Never seek or complete timelines.
        await page.waitForTimeout(1800);
        const clockAfter = await page.evaluate(() => window.gsap?.globalTimeline.time() ?? null);
        const height = await page.evaluate(() => document.documentElement.scrollHeight);
        for (let y = 0; y < height; y += 700) {
          await page.evaluate(y => window.scrollTo(0, y), y);
          await page.waitForTimeout(180);
        }
        await page.waitForTimeout(800);
        await page.evaluate(() => window.scrollTo(0, 0));
        const metrics = await page.evaluate(() => ({
          viewportWidth: innerWidth,
          documentWidth: document.documentElement.scrollWidth,
          horizontalOverflow: document.documentElement.scrollWidth - innerWidth,
          overflowingElements: [...document.querySelectorAll('body *')].filter(el => {
            const r = el.getBoundingClientRect();
            return r.width > 0 && (r.right > innerWidth + 1 || r.left < -1) && getComputedStyle(el).position !== 'fixed';
          }).slice(0, 12).map(el => ({ tag: el.tagName, id: el.id, class: String(el.className).slice(0, 100) })),
        }));
        const screenshot = path.join(out, `viewport-${width}.png`);
        await page.screenshot({ path: screenshot, fullPage: true });
        results.push({ url, ...metrics, clockBefore, clockAfter, errors, failedResponses, failedRequests, screenshot });
      } finally { await context.close(); }
    }
  } finally { await browser.close(); }
  fs.writeFileSync(path.join(out, 'report.json'), JSON.stringify(results, null, 2));
  console.log(JSON.stringify(results, null, 2));
  // A completed capture is not a passing UI check.
  if (results.some(r => r.horizontalOverflow > 0 || r.errors.length || r.failedResponses.length || r.failedRequests.length)) process.exitCode = 2;
})().catch(e => { console.error(e.message); process.exitCode = 1; });
