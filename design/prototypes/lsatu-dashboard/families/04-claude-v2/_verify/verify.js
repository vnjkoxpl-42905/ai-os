// Pass-3 verification: keyboard walkthrough, reduced motion, read counts, all states, console errors.
// Writes _verify/report.json and focus screenshots to _verify/focus/.
const { chromium } = require('C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/playwright');
const fs = require('fs');
const path = require('path');
const BASE = 'http://localhost:8120/LSAT-U-Dashboard-Three-Directions-v2/';
const OUT = __dirname;
const pages = ['lamplight/student', 'lamplight/teacher', 'carrel/student', 'carrel/teacher', 'marginalia/student', 'marginalia/teacher'];
const report = {};

async function open(b, url, opts = {}) {
  const ctx = await b.newContext(Object.assign({ viewport: { width: 1440, height: 900 } }, opts));
  const page = await ctx.newPage();
  const errors = [];
  page.on('pageerror', (e) => errors.push('pageerror: ' + e.message));
  page.on('console', (m) => { if (m.type() === 'error' && !/favicon|404/.test(m.text())) errors.push('console: ' + m.text()); });
  await page.goto(url, { waitUntil: 'networkidle' });
  return { ctx, page, errors };
}

// what currently has focus, and whether a visible focus indicator is drawn
const focusInfo = (page) => page.evaluate(() => {
  const el = document.activeElement;
  if (!el || el === document.body) return null;
  const cs = getComputedStyle(el);
  const r = el.getBoundingClientRect();
  const label = (el.getAttribute('aria-label') || el.textContent || el.value || el.placeholder || '').replace(/\s+/g, ' ').trim().slice(0, 48);
  const visible = (cs.outlineStyle !== 'none' && parseFloat(cs.outlineWidth) > 0) || cs.boxShadow !== 'none' || el.matches(':focus-visible');
  return { tag: el.tagName.toLowerCase(), cls: (el.className && el.className.baseVal === undefined ? el.className : '').toString().slice(0, 40), label, outline: `${cs.outlineStyle} ${cs.outlineWidth}`, ring: visible, onScreen: r.width > 0 && r.height > 0 };
});

const count = (page, sel) => page.evaluate((s) => { const e = document.querySelector(s); return e ? e.textContent.trim() : null; }, sel);

(async () => {
  fs.mkdirSync(path.join(OUT, 'focus'), { recursive: true });
  const b = await chromium.launch({ channel: 'msedge' });

  for (const p of pages) {
    const r = report[p] = { errors: [] };

    // 1. keyboard: tab through the first 40 stops
    {
      const { ctx, page, errors } = await open(b, BASE + p + '.html');
      await page.waitForTimeout(2600);
      const stops = [];
      for (let i = 0; i < 40; i++) { await page.keyboard.press('Tab'); stops.push(await focusInfo(page)); }
      r.tabStops = stops.filter(Boolean).length;
      r.tabWithoutRing = stops.filter((s) => s && !s.ring).map((s) => `${s.tag}.${s.cls} "${s.label}"`);
      r.tabOffscreen = stops.filter((s) => s && !s.onScreen).map((s) => `${s.tag} "${s.label}"`);
      r.firstStops = stops.slice(0, 12).map((s) => s && `${s.tag} "${s.label}"`);
      await page.keyboard.press('Shift+Tab');
      await page.screenshot({ path: path.join(OUT, 'focus', p.replace('/', '-') + '-focus.png') });
      r.errors.push(...errors);
      await ctx.close();
    }

    // 2. keyboard-only signature interaction
    {
      const { ctx, page, errors } = await open(b, BASE + p + '.html');
      await page.waitForTimeout(2600);
      let result = 'n/a';
      if (p.startsWith('lamplight')) {
        const before = await count(page, '.paper h2');
        await page.focus('.q-look'); await page.keyboard.press('Enter'); await page.waitForTimeout(1600);
        const after = await count(page, '.paper h2');
        const focusedIn = await page.evaluate(() => !!document.activeElement.closest('.paper'));
        result = `Enter on queue item: paper "${before}" -> "${after}", focus moved to paper: ${focusedIn}`;
      } else if (p === 'carrel/student') {
        const top = () => page.evaluate(() => document.querySelector('.icard.is-front h2').textContent);
        const before = await top();
        await page.focus('#stack'); await page.keyboard.press('ArrowRight'); await page.waitForTimeout(1200);
        const mid = await top();
        await page.keyboard.press('ArrowLeft'); await page.waitForTimeout(1400);
        const back = await top();
        const live = await count(page, '#pile-status');
        result = `ArrowRight: "${before}" -> "${mid}"; ArrowLeft back to "${back}"; live region: "${live}"`;
      } else if (p === 'carrel/teacher') {
        const front = () => page.evaluate(() => document.querySelector('.rcard.is-front .rcard__name').textContent.trim().split(' Active')[0].split(' Last')[0]);
        const before = await front();
        await page.focus('#drum'); await page.keyboard.press('ArrowDown'); await page.waitForTimeout(800);
        const after = await front();
        await page.focus('#find'); await page.keyboard.type('webb'); await page.waitForTimeout(2400);
        const found = await front();
        result = `ArrowDown: "${before}" -> "${after}"; typed "webb" -> "${found}"`;
      } else {
        await page.focus('.tok'); await page.waitForTimeout(500);
        const hot = await page.evaluate(() => ({ tok: !!document.querySelector('.tok.is-hot'), note: document.querySelector('.note.is-hot')?.id, leader: document.getElementById('leader-path').getAttribute('d')?.length > 0 }));
        result = `focus first phrase -> note hot: ${hot.note}, leader line drawn: ${hot.leader}`;
      }
      r.keyboardInteraction = result;
      r.errors.push(...errors);
      await ctx.close();
    }

    // 3. read counts: marking a message read updates the inbox count and keeps the history
    {
      const { ctx, page, errors } = await open(b, BASE + p + '.html');
      await page.waitForTimeout(2600);
      const sel = p.startsWith('marginalia') ? '#inbox-count' : '#inbox-count';
      const before = await count(page, sel);
      if (p.endsWith('student')) await page.click('[data-act="read"]');
      else await page.click('[data-act="convo"] >> nth=0');
      await page.waitForTimeout(1400);
      const after = await count(page, sel);
      const toast = await count(page, '.toast');
      r.readCount = `${before} -> ${after}; toast: "${toast}"`;
      r.errors.push(...errors);
      await ctx.close();
    }

    // 4. reduced motion: the first frame must already be the final frame
    {
      const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, reducedMotion: 'reduce' });
      const page = await ctx.newPage();
      const errors = [];
      page.on('pageerror', (e) => errors.push('pageerror: ' + e.message));
      await page.goto(BASE + p + '.html', { waitUntil: 'networkidle' });
      await page.evaluate(() => document.fonts.ready);
      await page.waitForTimeout(150);
      const a = await page.screenshot({ type: 'png' });
      await page.waitForTimeout(2800);
      const c = await page.screenshot({ type: 'png' });
      fs.writeFileSync(path.join(OUT, 'focus', p.replace('/', '-') + '-rm-early.png'), a);
      fs.writeFileSync(path.join(OUT, 'focus', p.replace('/', '-') + '-rm-late.png'), c);
      r.reducedMotionIdenticalFrames = Buffer.compare(a, c) === 0;
      r.reducedMotionGsapTweens = await page.evaluate(() => window.gsap ? gsap.globalTimeline.getChildren(true, true, false).filter((t) => t.isActive()).length : 'no gsap');
      r.errors.push(...errors);
      await ctx.close();
    }

    // 5. every state: errors, overflow at phone width, unknown counts never shown as zero
    r.states = {};
    for (const st of ['full', 'empty', 'loading', 'error']) {
      for (const w of [1440, 390]) {
        const { ctx, page, errors } = await open(b, `${BASE}${p}.html?state=${st}`, { viewport: { width: w, height: w > 600 ? 900 : 844 } });
        await page.waitForTimeout(1800);
        const overflow = await page.evaluate(() => document.documentElement.scrollWidth - innerWidth);
        const inbox = await count(page, '#inbox-count');
        r.states[`${st}@${w}`] = { overflow, inbox, errors: errors.length };
        r.errors.push(...errors.map((e) => `${st}@${w} ${e}`));
        await ctx.close();
      }
    }
    console.log(p, JSON.stringify({ tabStops: r.tabStops, noRing: r.tabWithoutRing.length, kb: r.keyboardInteraction, read: r.readCount, rm: r.reducedMotionIdenticalFrames, errors: r.errors.length }));
  }
  fs.writeFileSync(path.join(OUT, 'report.json'), JSON.stringify(report, null, 2));
  await b.close();
})().catch((e) => { console.error(e); process.exit(1); });
