// Natural-speed motion capture: screenshots sampled in real time while each page plays and is used.
// Nothing is forced to its end. usage: node record.js [filter]
const { chromium } = require('C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/playwright');
const fs = require('fs');
const path = require('path');
const BASE = 'http://localhost:8120/LSAT-U-Dashboard-Three-Directions-v2/';
const OUT = path.join(__dirname, 'video');
const filter = process.argv[2] || '';

const drag = async (p, sel, dx, steps = 8) => {
  const bb = await p.locator(sel).first().boundingBox();
  const x = bb.x + bb.width * .45, y = bb.y + bb.height * .45;
  await p.mouse.move(x, y); await p.mouse.down();
  for (let i = 1; i <= steps; i++) { await p.mouse.move(x + (dx * i) / steps, y + i); await p.waitForTimeout(16); }
  await p.mouse.up();
};

const flows = {
  'lamplight-student': { page: 'lamplight/student', fn: async (p) => { await p.waitForTimeout(2200); await p.hover('.q-row >> nth=0'); await p.waitForTimeout(500); await p.click('.q-look >> nth=1'); await p.waitForTimeout(1800); } },
  'lamplight-teacher': { page: 'lamplight/teacher', fn: async (p) => { await p.waitForTimeout(2200); await p.click('.q-look >> nth=0'); await p.waitForTimeout(1800); } },
  'carrel-student': { page: 'carrel/student', fn: async (p) => { await p.waitForTimeout(2200); await drag(p, '.icard.is-front .icard__blurb', -260); await p.waitForTimeout(1300); await p.click('.icard__tab >> nth=0'); await p.waitForTimeout(1300); await p.click('[data-act="read"]'); await p.waitForTimeout(1000); } },
  'carrel-teacher': { page: 'carrel/teacher', fn: async (p) => { await p.waitForTimeout(2400); await p.click('#find'); await p.keyboard.type('webb', { delay: 90 }); await p.waitForTimeout(2200); } },
  'marginalia-student': { page: 'marginalia/student', fn: async (p) => { await p.waitForTimeout(3200); await p.hover('.tok >> nth=1'); await p.waitForTimeout(900); await p.click('[data-act="read"]'); await p.waitForTimeout(1200); } },
  'marginalia-teacher': { page: 'marginalia/teacher', fn: async (p) => { await p.waitForTimeout(3000); await p.hover('.tok >> nth=1'); await p.waitForTimeout(900); await p.selectOption('#who', 'Celia Moreno'); await p.waitForTimeout(1200); } },
  'carrel-student-phone': { page: 'carrel/student', vw: 390, touch: true, fn: async (p) => { await p.waitForTimeout(2000); await p.locator('#stack').scrollIntoViewIfNeeded(); await p.waitForTimeout(300); await drag(p, '.icard.is-front .icard__blurb', 220, 6); await p.waitForTimeout(1500); } },
  'marginalia-student-phone': { page: 'marginalia/student', vw: 390, touch: true, fn: async (p) => { await p.waitForTimeout(2600); await p.locator('#note-1 .note__toggle').scrollIntoViewIfNeeded(); await p.waitForTimeout(300); await p.click('#note-1 .note__toggle'); await p.waitForTimeout(1200); } },
};

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch({ channel: 'msedge' });
  for (const [name, f] of Object.entries(flows)) {
    if (!name.includes(filter)) continue;
    const vw = f.vw || 1440;
    const ctx = await browser.newContext({ viewport: { width: vw, height: vw > 600 ? 900 : 844 }, hasTouch: !!f.touch, isMobile: !!f.touch });
    const page = await ctx.newPage();
    const errors = [];
    page.on('pageerror', (e) => errors.push(e.message));
    const dir = path.join(OUT, name);
    fs.rmSync(dir, { recursive: true, force: true }); fs.mkdirSync(dir, { recursive: true });
    let run = true, k = 0; const t0 = Date.now(); const stamps = [];
    await page.goto(BASE + f.page + '.html', { waitUntil: 'commit' });
    const loop = (async () => { while (run) { const b = await page.screenshot({ type: 'jpeg', quality: 70, scale: 'css', timeout: 3000 }).catch(() => null); if (b) { fs.writeFileSync(path.join(dir, String(k).padStart(3, '0') + '.jpg'), b); stamps.push(Date.now() - t0); k++; } } })();
    await f.fn(page);
    run = false; await loop;
    await ctx.close();
    fs.writeFileSync(path.join(dir, 'stamps.json'), JSON.stringify(stamps));
    console.log(name, k + ' frames', 'avg ' + Math.round((stamps.at(-1) || 0) / Math.max(1, k)) + 'ms', errors.length ? 'ERR ' + errors.join(' | ') : 'ok');
  }
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
