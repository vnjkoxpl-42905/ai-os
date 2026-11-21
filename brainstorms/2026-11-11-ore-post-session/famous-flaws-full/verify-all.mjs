// Independent proof for out/famous-flaws.html. Run: node verify-all.mjs
// It parses sources/05_compiled_content_voiced.md itself (not out/flaws.data.json) and owns the closed
// table of permitted adaptations. No browser and no dependencies. Exits non-zero on any failure.
import { readFileSync } from 'node:fs';
import { pathToFileURL } from 'node:url';
import path from 'node:path';

const ROOT = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1'));
const rd = (p) => readFileSync(path.join(ROOT, p), 'utf8').replace(/\r\n/g, '\n');
const SEC = '§';

const source = rd('sources/05_compiled_content_voiced.md');
const tsSrc = rd('sources/flaws.ts');
const shell = rd('shell/note-shell.html');
const page = rd('out/famous-flaws.html');
const manifest = JSON.parse(rd('out/adaptations.json'));

const results = [];
const check = (name, ok, detail = '') => results.push({ name, ok: !!ok, detail });

// ---------------------------------------------------------------- scope
const iNote = source.indexOf('## Note 2 · Famous Flaws Catalog');
const iMech = source.indexOf('## Invented · Answer Choice Disguise Library');
const iMatrix = source.indexOf('## Invented · Flaw vs. Flaw Disambiguation Matrix');
const iEnd = source.indexOf('**END OF VOICE-LOCKED CONTENT**');
let scope = source.slice(iNote, iEnd);

// ---------------------------------------------------------------- verifier-owned adaptation table
const TABLE = [
  ['R1', 'Joshua-Named, Super Common (5)', 'Named by me, super common (5)'],
  ['R2', "it's probably Trap Pattern 4 (Wrong Flaw).", "it's probably a wrong-flaw trap."],
  ['R2', `(Trap 4 Wrong Flaw, Trap 5 Contradicted from ${SEC} 5)`, '(a wrong flaw, or one the stimulus contradicts)'],
  ['R2', `Wrong Flaw (Trap 4 from ${SEC} 5) is the trap pattern that costs`, 'Choosing the wrong flaw is the trap that costs'],
  ['R2', 'The Master Guide teaches you the flaws.', 'The list above teaches you the flaws.'],
  ['R2', 'The per-flaw disguise lists are embedded in each catalog entry above.', "The per-flaw disguise lists are in each flaw's panel above."],
  ['R3', 'Dolores vs. Victor (PT 16.2.19).', 'Dolores vs. Victor.'],
  ['R3', 'The robot engineer (PT 16.2.10).', 'The robot engineer.'],
  ['R3', 'The Ethicist meat argument (June 2007.3.21).', 'The Ethicist meat argument.'],
  ['R4', "Dr. Fauci, the government's leading expert in infectious diseases,", "The government's leading expert in infectious diseases"],
  ['R4', 'Dr. Fauci must be wrong!', 'The expert must be wrong!'],
  ['R4', 'Billy says his uncle was related to Elvis,', 'Billy says his uncle was related to a famous singer,'],
  ['R4', "Thus, Billy's uncle was not related to Elvis.", "Thus, Billy's uncle was not related to the singer."],
];
const OMIT_FIXED = [
  'Procedural-reference mode. Fifteen entries across three groups. Each entry is a quick-reference card built for a student stuck mid-drill who needs to look up a flaw fast. Modular subsections, dense bullets, voice still on.\n\n',
  ' The catalog lives next to the drills, not inside them.',
  '**Cross-link.** The Causation module covers this in depth. The catalog entry is the Flaw-recognition surface only.\n\n',
];
const OMIT_RX = [/^ · slug: `[a-z0-9-]+`$/, /^> \*\*Stage 3 implementation note:\*\*[^\n]*\n\n$/, /^### How to drill the matrix\n\n[^\n]*\n\n$/];

// R5: none expected, and the source scope must have no dashes
check('R5: no dashes in the in-scope source (so no R5 entries needed)', !/[—–]/.test(scope));
check('R5: manifest has no R5 entries', !manifest.some((m) => m.rule === 'R5'));

// manifest validation: the verifier builds the COMPLETE expected manifest and compares exact entries and multiplicities
const ALLOWED = new Set(['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7']);
let manifestOk = true; const manifestWhy = [];
const counters = {};
const G2 = ['circular-reasoning', 'internal-contradiction', 'equivocation', 'inappropriate-appeal'];
for (const id of G2) {
  const m = tsSrc.match(new RegExp(`id:\\s*'${id}'[\\s\\S]*?counterQuestion:\\s*'((?:[^'\\\\]|\\\\.)*)'`));
  counters[id] = m ? m[1].replace(/\\'/g, "'") : null;
}
const origScope = source.slice(iNote, iEnd);
const expectedKeys = [];
for (const [r, f, t] of TABLE) expectedKeys.push(`${r}|${f}|${t}`);
for (const f of OMIT_FIXED) expectedKeys.push(`R7|${f}|`);
for (const m of origScope.matchAll(/ · slug: `[a-z0-9-]+`/g)) expectedKeys.push(`R7|${m[0]}|`);
const st3 = origScope.match(/> \*\*Stage 3 implementation note:\*\*[^\n]*\n\n/);
const dr = origScope.match(/### How to drill the matrix\n\n[^\n]*\n\n/);
if (st3) expectedKeys.push(`R7|${st3[0]}|`); else { manifestOk = false; manifestWhy.push('Stage 3 note not found in source'); }
if (dr) expectedKeys.push(`R7|${dr[0]}|`); else { manifestOk = false; manifestWhy.push('How-to-drill section not found in source'); }
const tally = (arr) => arr.reduce((m, k) => m.set(k, (m.get(k) || 0) + 1), new Map());
const exp = tally(expectedKeys);
const gotKeys = [];
for (const m of manifest) {
  if (!ALLOWED.has(m.rule)) { manifestOk = false; manifestWhy.push('unknown rule ' + m.rule); continue; }
  if (m.rule === 'R6') continue;
  if (typeof m.from !== 'string' || !origScope.includes(m.from)) { manifestOk = false; manifestWhy.push('from not verbatim in source: ' + String(m.from).slice(0, 40)); continue; }
  gotKeys.push(`${m.rule}|${m.from}|${m.to}`);
}
const got = tally(gotKeys);
for (const [k, n] of exp) if ((got.get(k) || 0) !== n) { manifestOk = false; manifestWhy.push(`expected x${n}, got x${got.get(k) || 0}: ${k.slice(0, 60)}`); }
for (const [k, n] of got) if (!exp.has(k)) { manifestOk = false; manifestWhy.push(`unexpected entry: ${k.slice(0, 60)}`); }
const r6 = manifest.filter((m) => m.rule === 'R6');
const r6ok = r6.length === 4 && G2.every((id) => r6.filter((m) => m.flaw === id).length === 1 && r6.find((m) => m.flaw === id).from === null && r6.find((m) => m.flaw === id).to === counters[id]) && Object.values(counters).every(Boolean);
if (!r6ok) { manifestOk = false; manifestWhy.push('R6: need exactly one record per Group 2 flaw, equal to the parsed flaws.ts counterQuestion'); }
check('Adaptation manifest equals the complete verifier-built manifest (exact entries and multiplicities, R1 to R7)', manifestOk, manifestWhy.slice(0, 4).join('; '));
check('R6: exactly one record per Group 2 flaw, equal to parsed flaws.ts', r6ok);

// apply the verifier's own transformations to the source scope
for (const [, f, t] of TABLE) scope = scope.split(f).join(t);
for (const f of OMIT_FIXED) scope = scope.split(f).join('');
scope = scope.replace(/ · slug: `[a-z0-9-]+`/g, '');
scope = scope.replace(/> \*\*Stage 3 implementation note:\*\*[^\n]*\n\n/, '');
scope = scope.replace(/### How to drill the matrix\n\n[^\n]*\n\n/, '');

// ---------------------------------------------------------------- source counts (own parse)
const lines = scope.split('\n');
const mechAt = lines.findIndex((l) => l.startsWith('## Invented · Answer Choice'));
const matAt = lines.findIndex((l) => l.startsWith('## Invented · Flaw vs. Flaw'));
const noteLines = lines.slice(0, mechAt), mechLines = lines.slice(mechAt, matAt), matLines = lines.slice(matAt);
const LABEL = /^\*\*(Definition\.|Stimulus tells\.|Answer-choice disguises\.|Canonical worked examples?\.|The "What if" counter\.|Disambiguate from:|When it IS the right answer\.|Real LSAT phrase pairs the test exploits:|Cross-link\.)\*\*/;
const entries = []; let cur = null, mode = null, gn = 0;
const groupIntro = {}, groupHead = {};
for (const l of noteLines) {
  let m;
  if ((m = l.match(/^### Group (\d) · (.*)$/))) { gn = +m[1]; groupHead[gn] = l.slice(4); groupIntro[gn] = []; cur = null; continue; }
  if ((m = l.match(/^#### \d+ · (.*)$/))) { cur = { name: m[1].trim(), g: gn, units: [], disg: 0, ex: 0, wi: 0, di: 0, right: 0, pairs: 0 }; entries.push(cur); mode = null; continue; }
  if (l.trim() === '---') { continue; }
  if (!l.trim()) continue;
  if (!cur) { if (gn && !l.startsWith('>') && !l.startsWith('#')) groupIntro[gn].push(l.trim()); continue; }
  const lab = l.match(LABEL);
  if (lab) mode = lab[1];
  if (/^- /.test(l.trim())) {
    if (mode === 'Answer-choice disguises.') cur.disg++;
    if (mode === 'Disambiguate from:') cur.di++;
    if (mode === 'Real LSAT phrase pairs the test exploits:') cur.pairs++;
  }
  if (lab && lab[1].startsWith('Canonical worked')) cur.ex++;
  if (lab && lab[1].startsWith('The "What if"')) cur.wi++;
  if (lab && lab[1].startsWith('When it IS')) cur.right++;
  cur.units.push(l.trim());
}
const sum = (k) => entries.reduce((a, e) => a + e[k], 0);
check('Source: 15 entries', entries.length === 15, String(entries.length));
check('Source: 68 disguise phrasings', sum('disg') === 68, String(sum('disg')));
check('Source: 15 worked examples', sum('ex') === 15, String(sum('ex')));
check('Source: 11 What-if counters', sum('wi') === 11, String(sum('wi')));
check('Source: 12 Disambiguate pairs in 9 entries', sum('di') === 12 && entries.filter((e) => e.di).length === 9, `${sum('di')} in ${entries.filter((e) => e.di).length}`);
check('Source: 4 When-it-IS blocks', sum('right') === 4, String(sum('right')));
check('Source: 5 phrase pairs', sum('pairs') === 5, String(sum('pairs')));
const matRows = matLines.filter((l) => l.startsWith('| **'));
check('Source: 10 matrix rows', matRows.length === 10, String(matRows.length));
const mechHeads = mechLines.filter((l) => /^### Mechanic \d/.test(l));
check('Source: 5 mechanics', mechHeads.length === 5, String(mechHeads.length));

// ---------------------------------------------------------------- page text helpers
const decode = (s) => s.replace(/&ldquo;|&rdquo;/g, '"').replace(/&hellip;/g, '...').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"')
  .replace(/&#x([0-9a-f]+);/gi, (_, h) => String.fromCodePoint(parseInt(h, 16))).replace(/&#(\d+);/g, (_, d) => String.fromCodePoint(+d)).replace(/&amp;/g, '&');
// Structural visible-text extraction. It walks the tags, so text inside non-rendered metadata (title, desc, style,
// script), permanently hidden elements, and display:none elements is excluded. The only hidden container whose text
// counts is a panel body (class fx-body), because opening its panel exposes it.
const VOID = new Set(['area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr']);
const ALWAYS_SKIP = new Set(['style', 'script', 'title', 'desc', 'template', 'noscript']);
// Block-level tags separate words; inline tags (strong, em, span, a, code) add no space, so punctuation that follows
// an inline tag stays attached to its word and the comparison can be exact.
const BLOCK = new Set(['p', 'div', 'li', 'ul', 'ol', 'h1', 'h2', 'h3', 'h4', 'section', 'article', 'header', 'main', 'nav', 'figure', 'figcaption', 'blockquote', 'table', 'thead', 'tbody', 'tr', 'td', 'th', 'button', 'br', 'hr', 'label']);
const visible = (htmlIn) => {
  const html = htmlIn.replace(/<!--[\s\S]*?-->/g, ' ').replace(/<(script|style)\b[\s\S]*?<\/\1>/g, ' ');
  const out = []; const stack = []; let skip = 0; let m;
  const re = /<(\/?)([a-zA-Z][a-zA-Z0-9-]*)([^>]*)>|([^<]+)/g;
  while ((m = re.exec(html))) {
    if (m[4] !== undefined) { if (!skip) out.push(m[4]); continue; }
    const closing = m[1] === '/', tag = m[2].toLowerCase(), attrs = m[3] || '';
    if (BLOCK.has(tag) && !skip) out.push(' ');
    if (closing) {
      for (let i = stack.length - 1; i >= 0; i--) if (stack[i].tag === tag) { stack.splice(i).forEach((p) => { if (p.skip) skip--; }); break; }
      continue;
    }
    if (VOID.has(tag) || /\/\s*$/.test(attrs)) continue;
    let s = ALWAYS_SKIP.has(tag) || /display\s*:\s*none/.test(attrs);
    if (/(^|\s)hidden(\s|=|$)/.test(attrs)) {
      const cls = ((attrs.match(/class="([^"]*)"/) || [])[1] || '').split(/\s+/);
      if (!cls.includes('fx-body')) s = true;
    }
    stack.push({ tag, skip: s }); if (s) skip++;
  }
  return decode(out.join('').replace(/\s+/g, ' '));
};
// Exact comparison. The only normalisation is what the plan permits: case, whitespace and curly versus straight quotes.
// Digits, decimal points, symbols (such as the not-equal sign) and punctuation all count, so changing "99.9%" or
// replacing a not-equal sign with an equals sign is caught.
const norm = (s) => s.toLowerCase().replace(/[‘’]/g, "'").replace(/[“”]/g, '"').replace(/\s+/g, ' ').trim();
const stripMd = (s) => s.replace(/^> /, '').replace(/^- /, '').replace(/\*+/g, '').replace(/`/g, '');
// A source line that starts with a bold label is shown as a label element followed by its text: compare them separately.
const unitMatches = (hay, u) => {
  const t = u.trim();
  const m = t.match(LABEL);
  if (m) {
    const lab = m[1].replace(/[.:]$/, '');
    const rest = stripMd(t.slice(m[0].length)).trim();
    return hay.includes(norm(lab)) && (!rest || hay.includes(norm(rest)));
  }
  return hay.includes(norm(stripMd(t)));
};

const pageText = visible(page);
const pageNorm = norm(pageText);
const panels = [...page.matchAll(/<article class="fx-panel" id="flaw-([a-z0-9-]+)"[\s\S]*?<\/article>/g)];
check('Exactly 15 panels', panels.length === 15, String(panels.length));

// per-entry coverage: every source line of the entry appears in its own panel
const misses = [];
entries.forEach((e, i) => {
  const pn = panels[i] ? norm(visible(panels[i][0])) : '';
  if (!pn.includes(norm(e.name))) misses.push(`${e.name}: heading`);
  for (const u of e.units) {
    if (!unitMatches(pn, u)) misses.push(`${e.name}: ${stripMd(u).slice(0, 50)}`);
  }
});
// R6 counters must be in their panels
const ids = ['circular-reasoning', 'internal-contradiction', 'equivocation', 'inappropriate-appeal'];
ids.forEach((id) => {
  const pm = panels.find((p) => p[1] === id);
  if (!pm || !norm(visible(pm[0])).includes(norm(counters[id]))) misses.push(`${id}: R6 counter`);
});
check('Block coverage: every source line of every entry is in its own panel', misses.length === 0, `${misses.length} miss(es): ${misses.slice(0, 3).join(' | ')}`);

// verifier self-test (Codex FF-003): hiding a definition permanently must make the coverage check fail
{
  const defUnit = entries[0].units.find((u) => u.startsWith('**Definition.**'));
  const hiddenPanel = panels[0][0].replace('<span class="fx-label">Definition</span><p>', '<span class="fx-label">Definition</span><p hidden>');
  check('Self-test: a permanently hidden definition is NOT counted as visible', hiddenPanel !== panels[0][0] && !unitMatches(norm(visible(hiddenPanel)), defUnit) && unitMatches(norm(visible(panels[0][0])), defUnit));
  // meaning-changing substitutions must be caught (Codex FF-R03)
  const sleightIdx = entries.findIndex((e) => e.name.startsWith('Sleight'));
  const neUnit = entries[sleightIdx].units.find((u) => u.includes('≠'));
  const neMut = panels[sleightIdx][0].replace('≠', '=');
  check('Self-test: replacing the not-equal sign with an equals sign is caught', !!neUnit && neMut !== panels[sleightIdx][0] && !unitMatches(norm(visible(neMut)), neUnit) && unitMatches(norm(visible(panels[sleightIdx][0])), neUnit));
  const causalIdx = entries.findIndex((e) => e.name === 'Causal');
  const pctUnit = entries[causalIdx].units.find((u) => u.includes('99.9%'));
  const pctMut = panels[causalIdx][0].replace('99.9%', '999%');
  check('Self-test: changing 99.9% to 999% is caught', !!pctUnit && pctMut !== panels[causalIdx][0] && !unitMatches(norm(visible(pctMut)), pctUnit) && unitMatches(norm(visible(panels[causalIdx][0])), pctUnit));
  const metaPanel = panels[0][0].replace(/(<desc id="[^"]*">)/, '$1SVG-ONLY-MARKER ');
  check('Self-test: text inside an SVG desc is NOT counted as visible', metaPanel.includes('SVG-ONLY-MARKER') && !visible(metaPanel).includes('SVG-ONLY-MARKER'));
}

// group intros and headings
const ghMisses = [];
for (const g of [1, 2, 3]) {
  const gh = [...page.matchAll(new RegExp(`<div class="fx-gh" data-g="${g}">[\\s\\S]*?</div>`, 'g'))][0];
  const gt = gh ? norm(visible(gh[0])) : '';
  if (!gt.includes(norm(groupHead[g]))) ghMisses.push(`g${g} heading`);
  for (const p of groupIntro[g]) if (!gt.includes(norm(stripMd(p)))) ghMisses.push(`g${g} intro: ${p.slice(0, 40)}`);}
check('Group headings and intros are present, inside their group block', ghMisses.length === 0, ghMisses.join(' | '));

// how-to-read quote
const howto = lines.find((l) => l.startsWith('> **How to read this catalog:**'));
const hm = howto && howto.match(/^> \*\*(.+?):\*\*\s*(.*)$/);
check('"How to read this catalog" quote is present (adapted), tag and text', !!hm && pageNorm.includes(norm(hm[1])) && pageNorm.includes(norm(stripMd(hm[2]))));

// mechanics
const mechRegion = norm(visible((page.match(/<div class="fx-mechs">[\s\S]*?<\/section>/) || [''])[0]));
const mechIntroRegion = norm(visible((page.match(/The disguises<\/div>[\s\S]*?<\/section>/) || [''])[0]));
const mechMiss = [];
for (const l of mechLines) {
  const t = stripMd(l.trim());
  if (!t || t === '---' || t.startsWith('## ')) continue;
  const hd = t.match(/^### (Mechanic \d+) · (.*)$/);
  if (hd) { if (!mechIntroRegion.includes(norm(hd[1])) || !mechIntroRegion.includes(norm(hd[2]))) mechMiss.push(t.slice(0, 50)); continue; }
  if (!mechIntroRegion.includes(norm(t))) mechMiss.push(t.slice(0, 50));
}
check('Mechanics: intro, five titles, every paragraph and bullet are present', mechMiss.length === 0 && mechRegion.length > 0, `${mechMiss.length} miss(es): ${mechMiss.slice(0, 3).join(' | ')}`);

// matrix
const matRegion = norm(visible((page.match(/Flaw vs\. flaw<\/div>[\s\S]*?<\/section>/) || [''])[0]));
const matMiss = [];
for (const l of matLines) {
  const t = l.trim();
  if (!t || t === '---' || t.startsWith('## ') || /^\|\s*(Pair|---)/.test(t)) continue;
  if (t.startsWith('|')) { for (const c of t.replace(/^\||\|$/g, '').split('|')) { const cc = stripMd(c.trim()); if (cc && !matRegion.includes(norm(cc))) matMiss.push(cc.slice(0, 50)); } }
  else if (!matRegion.includes(norm(stripMd(t)))) matMiss.push(t.slice(0, 50));
}
check('Matrix: intro and all three cells of all 10 rows are present', matMiss.length === 0, `${matMiss.length} miss(es): ${matMiss.slice(0, 3).join(' | ')}`);

// ---------------------------------------------------------------- panel parts and visuals
const partMiss = [];
panels.forEach((p, i) => {
  const e = entries[i]; const h = p[0];
  const need = ['Frequency', 'Definition', 'Stimulus tells', 'Answer-choice disguises', 'Canonical worked example', 'The "What if" counter'];
  if (e.di) need.push('Disambiguate from');
  if (e.right) need.push('When it IS the right answer');
  if (e.pairs) need.push('Real LSAT phrase pairs');
  for (const n of need) if (!decode(h).includes(`>${n}`)) partMiss.push(`${p[1]}: ${n}`);
  if (!/class="fx-fig"><svg/.test(h)) partMiss.push(`${p[1]}: visual`);
  if (!/class="fx-try"/.test(h)) partMiss.push(`${p[1]}: say-first check`);
  if (!/data-slot="session-/.test(h) || !/data-slot="quote-/.test(h)) partMiss.push(`${p[1]}: session slots`);
});
check('Each panel has every part that exists for its entry, plus visual, check and slots', partMiss.length === 0, partMiss.slice(0, 4).join(' | '));
const svgs = panels.map((p) => (p[0].match(/<svg[\s\S]*?<\/svg>/) || [''])[0]);
check('15 distinct SVGs, each with title and desc', new Set(svgs).size === 15 && svgs.every((s) => /<title/.test(s) && /<desc/.test(s)));
const cake = (page.match(/class="fx-cake"[\s\S]*?<\/svg>/) || [''])[0];
check('Cake-on-Blocks SVG with title and desc, Object and Reset buttons', /<title/.test(cake) && /<desc/.test(cake) && /id="fx-object"/.test(page) && /id="fx-reset"/.test(page));
check('15 cards, 3 filter chips plus All', (page.match(/class="fx-card"/g) || []).length === 15 && (page.match(/class="fx-chip"/g) || []).length === 4);
check('Matrix check present for all 10 rows', (page.match(/class="fx-quiz"/g) || []).length === 10);
const news = (page.match(/<span class="fx-new">New example<\/span>/g) || []).length;
check('Every original example is labelled "New example" (15 + 10)', news === 25, String(news));

// session slot contract: 15 spans with class session-slot and 15 hidden quote blocks, named by flaw id
const slotOk = IDS_ALL().every((id) => new RegExp(`<span class="session-slot[^"]*" data-slot="session-${id}"></span>`).test(page) && new RegExp(`<div class="session-quote" data-slot="quote-${id}" hidden></div>`).test(page));
check('Session slots: 15 .session-slot spans and 15 hidden .session-quote blocks, named by flaw id', slotOk);
function IDS_ALL() { return ['necessary-vs-sufficient', 'causal', 'part-vs-whole', 'unproven-vs-proven-false', 'ad-hominem', 'sampling', 'circular-reasoning', 'internal-contradiction', 'equivocation', 'inappropriate-appeal', 'sleight-of-hand', 'sleazy-sales-pitch', 'universal-desires', 'value-assumptions', 'secret-downsides']; }

// SVG text bounds: estimate each label's width from its class font and make sure it sits inside the viewBox
const FONT = { t: [12.5, 0.52], tb: [14, 0.58], ts: [10.5, 0.67], cktext: [9, 0.58], blkt: [11, 0.55] };
const svgBad = [];
for (const sv of page.match(/<svg class="fx-svg"[\s\S]*?<\/svg>/g) || []) {
  const vb = (sv.match(/viewBox="0 0 (\d+) (\d+)"/) || [0, 360, 150]); const W = +vb[1];
  const sid = (sv.match(/<title id="([^"]+)-t"/) || [0, '?'])[1];
  let off = 0;
  for (const t of sv.matchAll(/<g transform="translate\((\d+) \d+\)">|<\/g>|<text class="([a-z]+)" x="([\d.]+)" y="[\d.]+" text-anchor="(\w+)">([^<]*)<\/text>/g)) {
    if (t[0].startsWith('<g transform')) { off = +t[1]; continue; }
    if (t[0] === '</g>') { off = 0; continue; }
    const cls = t[2], tx = t[3], anchor = t[4], raw = t[5];
    const [fs, k] = FONT[cls] || [11, 0.6];
    const txt = decode(raw).replace(/&#\d+;/g, 'x');
    const w = txt.length * fs * k; const x = +tx + off;
    const left = anchor === 'middle' ? x - w / 2 : anchor === 'end' ? x - w : x;
    const right = left + w;
    if (left < -1 || right > W + 1) svgBad.push(`${sid}: "${txt.slice(0, 28)}" ${left.toFixed(0)}..${right.toFixed(0)} of ${W}`);
  }
}
check('Every SVG text label fits inside its viewBox (estimated from class font and length)', svgBad.length === 0, svgBad.slice(0, 4).join(' | '));
const eq = (page.match(/<svg class="fx-svg"[^>]*aria-labelledby="equivocation-t[\s\S]*?<\/svg>/) || [''])[0];
check('Equivocation SVG description matches its labels (approves in the conclusion, penalizes in the premise)', /approves, is the sense used in the conclusion/.test(eq) && /penalizes, is the sense used in the premise/.test(eq));
check('No real public figure left in the examples (Fauci, Elvis)', !/Fauci|Elvis/.test(pageText));

// ---------------------------------------------------------------- shell identity, validator, size, text rules
const blockOf = (html, tag, from = 0) => { const a = html.indexOf(`<${tag}`, from); const b = html.indexOf(`</${tag}>`, a); return [html.slice(a, b + tag.length + 3), a, b]; };
const [shStyle] = blockOf(shell, 'style');
const [pgStyle] = blockOf(page, 'style');
check('Shell <style> block is identical to the shell', shStyle === pgStyle);
const [shScript] = blockOf(shell, 'script');
const [pgScript] = blockOf(page, 'script');
check('Shell <script> block is identical to the shell', shScript === pgScript);
const pgStyles = (page.match(/<style>/g) || []).length, pgScripts = (page.match(/<script>/g) || []).length;
check('Layer is a separate second <style> and second <script>', pgStyles === 2 && pgScripts === 2, `${pgStyles} style, ${pgScripts} script`);

// CSS visibility audit (Codex FF-R04): a stylesheet rule must not hide canonical content. Every layer rule that hides
// something has to be on this short list (hidden-state rules, answers revealed on click, the empty tag, the phone matrix
// header whose labels are repeated on each cell). The browser suite separately checks that every block renders.
{
  const layer = ([...page.matchAll(/<style>([\s\S]*?)<\/style>/g)][1] || [0, ''])[1].replace(/\/\*[\s\S]*?\*\//g, '');
  const ALLOW = new Set(['.fx-card[hidden],.fx-panel[hidden],.fx-body[hidden],.session-quote[hidden]', '.fx-body[hidden]', '.session-quote[hidden]', '.fx-session:empty', '.fx-try .rv', '.fx-quiz .rv', '.fx-matrix table.t thead']);
  const hide = /display\s*:\s*none|visibility\s*:\s*hidden|opacity\s*:\s*0(?![.\d])|font-size\s*:\s*0(?![.\d])|(^|[;\s])height\s*:\s*0(?![.\d])|max-height\s*:\s*0|clip\s*:|clip-path\s*:|text-indent\s*:\s*-/;
  const bad = [];
  for (const m of layer.matchAll(/([^{}@]+)\{([^{}]*)\}/g)) {
    const sel = m[1].trim().replace(/\s+/g, ' ').replace(/\s*,\s*/g, ',');
    if (hide.test(m[2]) && !ALLOW.has(sel)) bad.push(sel.slice(0, 50));
  }
  check('CSS audit: no layer rule hides content except the allowed hidden-state, reveal and phone-header rules', bad.length === 0, bad.slice(0, 3).join(' | '));
  const cssSelf = layer + '\n.fx-part{display:none}';
  let selfBad = 0;
  for (const m of cssSelf.matchAll(/([^{}@]+)\{([^{}]*)\}/g)) { const sel = m[1].trim().replace(/\s+/g, ' ').replace(/\s*,\s*/g, ','); if (hide.test(m[2]) && !ALLOW.has(sel)) selfBad++; }
  check('Self-test: an injected ".fx-part{display:none}" rule is caught by the CSS audit', selfBad === 1);
}

let validated = ''; try {
  const { validateInteractiveLesson } = await import(pathToFileURL(path.join(ROOT, 'tools/lsatu-lesson-validate.mjs')).href);
  validated = validateInteractiveLesson(page);
} catch (e) { validated = 'FAIL: ' + e.message; }
check('Validator passes (no outside files, fonts or links)', validated === 'famous-flaws-full', validated);
const bytes = Buffer.byteLength(page, 'utf8');
check('File under 500 KB', bytes < 500 * 1024, `${(bytes / 1024).toFixed(0)} KB`);
check('No em-dash or en-dash anywhere in the file', !/[—–]/.test(page));
const BANNED = /\b(delve|unlock|seamless|robust|game-changer|supercharge|elevate|Moreover|Furthermore|Additionally|Great question|Certainly|manual|recognition drill|conceptual note)\b/i;
check('No banned words in visible text', !BANNED.test(pageText), (pageText.match(BANNED) || [''])[0]);
check('Slots exist and the page works with them empty', /<!--SLOT:hero-kicker-->/.test(page) && page.includes('>SLOT:next-steps<'));
check('No internal references left (Trap n, section sign, PT cites, Master Guide, slug)', !/Trap (Pattern )?\d|§|PT \d+\.\d|Master Guide|slug:|Cross-link|Stage 3/.test(pageText));

// ---------------------------------------------------------------- report
const w = Math.max(...results.map((r) => r.name.length));
for (const r of results) console.log(`${r.ok ? 'PASS' : 'FAIL'}  ${r.name.padEnd(w)}  ${r.detail}`);
const failed = results.filter((r) => !r.ok).length;
console.log(`\n${results.length - failed}/${results.length} checks passed`);
process.exit(failed ? 1 : 0);
