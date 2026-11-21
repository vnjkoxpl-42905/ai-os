// Lists elements whose right edge passes the viewport at a given width.
const { chromium } = require('C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/playwright');
(async () => {
  const url = 'http://localhost:8120/LSAT-U-Dashboard-Three-Directions-v2/' + process.argv[2] + '.html';
  const w = Number(process.argv[3] || 390);
  const b = await chromium.launch({ channel: 'msedge' });
  const p = await (await b.newContext({ viewport: { width: w, height: 844 } })).newPage();
  await p.goto(url, { waitUntil: 'networkidle' });
  await p.waitForTimeout(2500);
  const out = await p.evaluate((vw) => [...document.querySelectorAll('body *')]
    .map((e) => ({ e, r: e.getBoundingClientRect() }))
    .filter(({ r }) => r.right > vw + 1 && r.width > 0)
    .slice(0, 15)
    .map(({ e, r }) => `${e.tagName.toLowerCase()}.${[...e.classList].join('.')} right=${Math.round(r.right)} w=${Math.round(r.width)}`), w);
  console.log(out.join('\n') || 'no overflow');
  await b.close();
})();
