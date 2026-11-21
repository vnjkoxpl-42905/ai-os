// Region screenshots for visual review. Run: node shoot-regions.mjs  (writes out/previews/region-*.png)
import { createRequire } from 'node:module';
import path from 'node:path';
const require = createRequire('C:/Users/Joshu/dev/lsatu/package.json');
const { chromium } = require('playwright-core');
const ROOT = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1'));
const FILE = 'file:///' + path.join(ROOT, 'out/famous-flaws.html').replace(/\\/g, '/');
const PREV = path.join(ROOT, 'out/previews');
const W = Number(process.argv[2] || 1280);
const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: W, height: 900 } });
const page = await ctx.newPage();
await page.goto(FILE);
await page.evaluate(async () => { await document.fonts.ready; document.querySelectorAll('.reveal').forEach((e) => e.classList.add('in')); });
await page.waitForTimeout(500);
const tag = W < 600 ? 'm' : 'd';
const shots = {
  hero: 'header.hero',
  cake: '.fx-cake',
  grid: 'section:has(.fx-grid)',
};
for (const [n, sel] of Object.entries(shots)) await page.locator(sel).first().screenshot({ path: path.join(PREV, `region-${tag}-${n}.png`) });
for (const id of ['necessary-vs-sufficient', 'causal', 'sleight-of-hand', 'internal-contradiction']) {
  await page.click(`.fx-card[data-target="flaw-${id}"]`);
  await page.waitForTimeout(250);
  await page.locator(`#flaw-${id}`).screenshot({ path: path.join(PREV, `region-${tag}-panel-${id}.png`) });
}
await page.locator('.fx-matrix').screenshot({ path: path.join(PREV, `region-${tag}-matrix.png`) });
await page.locator('.fx-mechs').screenshot({ path: path.join(PREV, `region-${tag}-mechs.png`) });
await browser.close();
console.log('done', W);
