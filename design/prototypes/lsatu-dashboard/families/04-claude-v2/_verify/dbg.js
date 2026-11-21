const { chromium } = require('C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/playwright');
(async () => {
  const b = await chromium.launch({ channel: 'msedge' });
  const p = await (await b.newContext({ viewport: { width: 1440, height: 900 } })).newPage();
  await p.goto('http://localhost:8120/LSAT-U-Dashboard-Three-Directions-v2/carrel/teacher.html', { waitUntil: 'networkidle' });
  await p.waitForTimeout(2600);
  const snap = () => p.evaluate(() => [...document.querySelectorAll('.rcard')].map((c) => (c.classList.contains('is-front') ? '*' : '') + c.querySelector('.rcard__name').firstChild.textContent.trim()).join(' | '));
  console.log('start', await snap());
  await p.focus('#drum'); await p.keyboard.press('ArrowDown'); await p.waitForTimeout(800);
  console.log('down ', await snap());
  await p.focus('#find'); await p.keyboard.type('webb');
  for (let i = 0; i < 6; i++) { await p.waitForTimeout(400); console.log('t' + i, await snap()); }
  await b.close();
})();
