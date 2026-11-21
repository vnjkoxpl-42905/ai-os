// Browser proof for out/famous-flaws.html. Run by the host: node verify-browser.mjs
// Uses the playwright-core install in the lsatu project. Writes screenshots to out/previews/.
import { createRequire } from 'node:module';
import path from 'node:path';
import { mkdirSync } from 'node:fs';

const require = createRequire('C:/Users/Joshu/dev/lsatu/package.json');
const { chromium } = require('playwright-core');
const ROOT = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1'));
const FILE = 'file:///' + path.join(ROOT, 'out/famous-flaws.html').replace(/\\/g, '/');
const PREV = path.join(ROOT, 'out/previews');
mkdirSync(PREV, { recursive: true });

const results = [];
const check = (name, ok, detail = '') => results.push({ name, ok: !!ok, detail });
const browser = await chromium.launch();

for (const [label, w, h] of [['desktop', 1280, 900], ['mobile', 375, 812]]) {
  const ctx = await browser.newContext({ viewport: { width: w, height: h } });
  const page = await ctx.newPage();
  const errors = [];
  page.on('console', (m) => { if (m.type() === 'error') errors.push(m.text()); });
  page.on('pageerror', (e) => errors.push(String(e)));
  await page.goto(FILE);
  await page.evaluate(async () => { await document.fonts.ready; });
  await page.waitForTimeout(400);

  const base = await page.evaluate(() => ({
    fonts: [...document.fonts].map((f) => f.family + ':' + f.status),
    overflow: document.documentElement.scrollWidth > innerWidth + 1,
    wide: [...document.querySelectorAll('main *')].filter((e) => !e.closest('.table-wrap') && e.getBoundingClientRect().right > innerWidth + 1).map((e) => (e.className || e.tagName) + '').slice(0, 4),
  }));
  check(`${label}: no horizontal page overflow`, !base.overflow && base.wide.length === 0, base.wide.join(','));
  check(`${label}: Outfit and both Fraunces faces loaded`, base.fonts.length >= 3 && base.fonts.every((f) => f.endsWith(':loaded')), base.fonts.join(' '));

  // filters
  await page.click('.fx-chip[data-filter="2"]');
  let vis = await page.evaluate(() => ({
    cards: [...document.querySelectorAll('.fx-card')].filter((c) => !c.hidden && getComputedStyle(c).display !== 'none').length,
    panels: [...document.querySelectorAll('.fx-panel')].filter((c) => !c.hidden && getComputedStyle(c).display !== 'none').length,
    live: document.getElementById('fx-live').textContent,
  }));
  check(`${label}: Group 2 filter shows 4 cards and 4 panels`, vis.cards === 4 && vis.panels === 4, JSON.stringify(vis));
  await page.click('.fx-chip[data-filter="all"]');
  vis = await page.evaluate(() => [...document.querySelectorAll('.fx-card')].filter((c) => getComputedStyle(c).display !== 'none').length);
  check(`${label}: All filter restores 15 cards`, vis === 15, String(vis));

  // card opens its panel; keyboard toggles it closed and open
  await page.click('.fx-card[data-target="flaw-causal"]');
  await page.waitForTimeout(300);
  let open = await page.evaluate(() => { const b = document.getElementById('body-causal'); return !b.hidden && getComputedStyle(b).display !== 'none'; });
  check(`${label}: clicking a card opens its panel`, open);
  await page.focus('#flaw-causal .fx-head');
  await page.keyboard.press('Enter');
  open = await page.evaluate(() => !document.getElementById('body-causal').hidden);
  check(`${label}: Enter on the panel header closes it`, !open);
  await page.keyboard.press('Space');
  open = await page.evaluate(() => !document.getElementById('body-causal').hidden);
  check(`${label}: Space on the panel header opens it`, open);

  // open all / close all
  await page.click('#fx-open-all');
  let n = await page.evaluate(() => [...document.querySelectorAll('.fx-body')].filter((b) => !b.hidden).length);
  check(`${label}: Open all opens 15 panels`, n === 15, String(n));
  await page.click('#fx-close-all');
  n = await page.evaluate(() => [...document.querySelectorAll('.fx-body')].filter((b) => !b.hidden).length);
  check(`${label}: Close all closes them`, n === 0, String(n));

  // every canonical block renders once the panels are open (Codex FF-R04): not display:none, not hidden, not zero-size
  await page.click('#fx-open-all');
  const unseen = await page.evaluate(() => {
    const bad = [];
    const sel = '.fx-body p, .fx-body li, .fx-body blockquote, .fx-body .fx-ask, .fx-body .fx-label, .fx-body svg, .fx-gh h3, .fx-gh p, .fx-mech h3, .fx-mech p, .fx-mech li, .fx-matrix td, .fx-matrix .fx-ask, .fx-head h3';
    document.querySelectorAll(sel).forEach((e) => {
      if (e.closest('.rv') || e.closest('.session-quote')) return;
      const cs = getComputedStyle(e), r = e.getBoundingClientRect();
      const text = (e.textContent || '').trim();
      if (cs.display === 'none' || cs.visibility === 'hidden' || parseFloat(cs.opacity) === 0 || r.width < 1 || r.height < 1 || (e.tagName.toLowerCase() !== 'svg' && !text)) bad.push((e.className || e.tagName) + ': ' + text.slice(0, 30));
    });
    return { n: document.querySelectorAll(sel).length, bad: bad.slice(0, 4) };
  });
  check(`${label}: every canonical block is rendered (no hidden, empty or zero-size element)`, unseen.bad.length === 0 && unseen.n >= 400, JSON.stringify(unseen));
  await page.click('#fx-close-all');

  // rail marker: with the next-steps section hidden, the active link is the last visible section, not the hidden one
  if (label === 'desktop') {
    await page.evaluate(() => window.scrollTo({ top: document.documentElement.scrollHeight, behavior: 'instant' }));
    await page.waitForTimeout(400);
    const rail = await page.evaluate(() => {
      const on = [...document.querySelectorAll('.rail ol li a.on')];
      const secs = [...document.querySelectorAll('main > section')].filter((s) => !s.hidden);
      const lastVisibleId = secs[secs.length - 1].id;
      return { on: on.length, href: on[0] ? on[0].getAttribute('href') : null, lastVisibleId, hiddenLink: on[0] ? on[0].parentNode.hidden : null };
    });
    check('desktop: rail marker rests on the last visible section when next steps are hidden', rail.on === 1 && rail.href === '#' + rail.lastVisibleId && rail.hiddenLink === false, JSON.stringify(rail));
    await page.evaluate(() => window.scrollTo({ top: 0, behavior: 'instant' }));
  }

  // say-first check
  await page.click('.fx-card[data-target="flaw-sampling"]');
  await page.click('#flaw-sampling .fx-reveal');
  const rv = await page.evaluate(() => getComputedStyle(document.querySelector('#flaw-sampling .fx-try .rv')).display);
  check(`${label}: say-first check reveals its answer`, rv === 'block', rv);

  // cake
  await page.click('#fx-object');
  await page.waitForTimeout(1100);
  let cake = await page.evaluate(() => ({ on: document.querySelector('.fx-cake').classList.contains('objected'), state: document.querySelector('.state-now').textContent, t: getComputedStyle(document.getElementById('cake-top')).transform }));
  check(`${label}: Object separates the blocks and the cake falls`, cake.on && /OBJECTION/.test(cake.state) && cake.t !== 'none', JSON.stringify(cake));
  await page.click('#fx-reset');
  cake = await page.evaluate(() => ({ on: document.querySelector('.fx-cake').classList.contains('objected'), state: document.querySelector('.state-now').textContent }));
  check(`${label}: Reset restores the valid state`, !cake.on && /VALID/.test(cake.state));

  // matrix: wrong then right
  const first = await page.evaluate(() => { const q = document.querySelector('.fx-quiz'); return { right: q.dataset.right, opts: [...q.querySelectorAll('.fx-opt')].map((o) => o.dataset.label) }; });
  const wrongLabel = first.opts.find((o) => o !== first.right);
  await page.locator('.fx-quiz').first().locator(`.fx-opt[data-label="${wrongLabel}"]`).click();
  let q1 = await page.evaluate(() => { const q = document.querySelector('.fx-quiz'); return { done: q.classList.contains('done'), wrong: !!q.querySelector('.fx-opt.wrong'), right: !!q.querySelector('.fx-opt.right'), rv: getComputedStyle(q.querySelector('.rv')).display, res: q.querySelector('.res').textContent }; });
  check(`${label}: a wrong matrix choice shows the right answer and the reason`, q1.done && q1.wrong && q1.right && q1.rv === 'block' && /Not quite/.test(q1.res), JSON.stringify(q1));
  await page.locator('.fx-quiz').first().locator(`.fx-opt[data-label="${first.right}"]`).click();
  q1 = await page.evaluate(() => document.querySelector('.fx-quiz .res').textContent);
  check(`${label}: the right matrix choice is marked correct`, /Correct/.test(q1), q1);

  // every matrix row has a working quiz
  const all = await page.evaluate(() => { let ok = 0; document.querySelectorAll('.fx-quiz').forEach((q) => { const o = q.querySelector('.fx-opt[data-label="' + q.dataset.right.replace(/"/g, '\\"') + '"]'); if (o) { o.click(); if (q.classList.contains('done') && q.querySelector('.fx-opt.right')) ok++; } }); return ok; });
  check(`${label}: all 10 matrix checks respond`, all === 10, String(all));

  // an unfilled next-steps slot must not expose its marker (Codex FF-007), and the slot contract holds
  const slots = await page.evaluate(() => {
    const li = [...document.querySelectorAll('ol.todo li')].find((l) => l.textContent.includes('SLOT:next-steps'));
    const sec = li ? li.closest('section') : null;
    return { hidden: !!sec && sec.hidden && getComputedStyle(sec).display === 'none', spans: document.querySelectorAll('.session-slot').length, quotes: document.querySelectorAll('.session-quote').length };
  });
  check(`${label}: empty next-steps section is hidden while unfilled`, slots.hidden, JSON.stringify(slots));
  check(`${label}: 15 .session-slot spans and 15 .session-quote blocks`, slots.spans === 15 && slots.quotes === 15, JSON.stringify(slots));

  // keyboard focus ring exists on interactive controls
  // reach a control by keyboard so :focus-visible applies (a programmatic focus() does not match it)
  await page.focus('.fx-chip[data-filter="1"]');
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  const focus = await page.evaluate(() => { const b = document.activeElement; const cs = getComputedStyle(b); return (b.className || b.tagName) + ': ' + cs.outlineStyle + ' ' + cs.outlineWidth; });
  check(`${label}: focused control shows an outline`, !/none/.test(focus), focus);

  check(`${label}: no console errors`, errors.length === 0, errors.slice(0, 2).join(' | '));

  // screenshots (reset to a clean look)
  await page.reload();
  await page.evaluate(async () => { await document.fonts.ready; document.querySelectorAll('.reveal').forEach((e) => e.classList.add('in')); });
  await page.waitForTimeout(500);
  await page.screenshot({ path: path.join(PREV, `${label}-top.png`), fullPage: false });
  await page.evaluate(() => { document.getElementById('fx-open-all').click(); });
  await page.waitForTimeout(300);
  await page.screenshot({ path: path.join(PREV, `${label}-full.png`), fullPage: true });
  await ctx.close();
}

await browser.close();
const w = Math.max(...results.map((r) => r.name.length));
for (const r of results) console.log(`${r.ok ? 'PASS' : 'FAIL'}  ${r.name.padEnd(w)}  ${r.detail}`);
const failed = results.filter((r) => !r.ok).length;
console.log(`\n${results.length - failed}/${results.length} browser checks passed`);
process.exit(failed ? 1 : 0);
