# Drill hub: plan to reach 20/20 audit and 40/40 critique

Written 2026-09-08 by Claude (Fable 5.1) for hand-off to another executor. Starting point: run 2 of [[DRILL-HUB-IMPECCABLE-AUDIT-2026-09-08-RUN2]], published as commit f791016. Audit 16/20, critique 31/40. The surface brief is `projects/lsatu/.impeccable/surfaces/drill-hub.md`; nothing in this plan contradicts it, and any step that changes a rule in it also updates it.

Joshua reviews the work after it is done. Do every step, in order, and write the report in Part 6 at the end. Do not skip a step because it seems small; the score is made of small things.

---

## Part 0. Ground rules for the executor

Read this whole part before touching a file.

**Where things are**

| Thing | Path |
|---|---|
| Repo root (run every command here) | `C:\Users\Joshu\dev\ai-os\projects\lsatu` |
| Page | `src/pages/AcademyMainhub.tsx` (hero is `MainhubHero`, around lines 70 to 225) |
| Today computation | `src/components/mainhub/useTodayFocus.ts` |
| Today card | `src/components/mainhub/TodayFocusPanel.tsx` |
| Practice card | `src/components/mainhub/PracticeInsightStage.tsx` |
| Insight slides | `src/components/mainhub/insightSlides.ts` |
| Hub CSS (the `.drill-observatory-*` block, lines ~840 to ~2060) | `src/components/classroom/classroom.css` |
| Classroom shell (menu button, sidebar) | `src/components/classroom/shell/ClassroomLayout.tsx` and the `.classroom-mobile-menu-button` rules at classroom.css lines ~2430 and ~3114 |
| Jump row | `src/components/questionfinder/QuestionJump.tsx`, `questionJump.css` |
| Search trigger | `src/components/questionfinder/QuestionFinder.tsx`, `questionFinder.css` |
| Section switch | `src/components/drill/SectionToggle.tsx` |
| Theme context (adds `.light` to `<html>`; default is **light**, not dark. `ClassroomLayout.tsx` separately toggles `html.dark`, which is what `classroom.css` keys on. Corrected 2026-09-09.) | `src/contexts/ThemeContext.tsx`, `src/components/classroom/shell/ClassroomLayout.tsx` |
| Surface brief | `.impeccable/surfaces/drill-hub.md` |
| Tests for the page | `src/pages/AcademyMainhub.test.tsx`, `src/pages/AcademyMainhub.section.test.tsx`, `src/components/mainhub/TodayFocusPanel.test.tsx` |
| Copy rules | `C:\Users\Joshu\dev\ai-os\wiki\teaching-voice.md` and `wiki/COPY-CORRECTIONS.md` |

**Commands you will run over and over**

```bash
npm run typecheck
```
```bash
npx vitest run src/pages/AcademyMainhub.test.tsx src/pages/AcademyMainhub.section.test.tsx src/components/mainhub
```
```bash
bash .claude/safe-push.sh
```

**Rules**

1. Work on `main`. Commit after every work package (WP) with a message that says what changed and why. End every commit message with the line `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`.
2. Push only with `bash .claude/safe-push.sh`. Never `git push` directly, never force.
3. Joshua publishes from Lovable himself after each push. Say "pushed, ready to publish" and wait. Verify on production (`https://lsatprep.study/classroom/drill`) only after he says it is published.
4. You cannot sign in anywhere. Do not try. Local `npm run dev` will show a sign-in page. All visual measurement happens on production after Joshua publishes, in the Claude in-app browser, with the scripts in Part 1.
5. No em-dashes in anything a student can read: copy, placeholders, aria-labels. Use a comma, a colon, or a period.
6. Nothing that carries text goes below `--observatory-ink-50` on a card. Do not create new ink steps below 50.
7. Every interactive element is at least 44px tall by its own box. No pseudo-element hit areas.
8. Do not add a second door to the builder. The console is the one door.
9. Do not change what data is shown, how assignments are computed, or anything in messages. Messages are out of scope by Joshua's decision.
10. `!important` count in classroom.css goes down with every WP, never up. Check with:
```bash
grep -c '!important' src/components/classroom/classroom.css
```
11. Do not invent numbers in the final report. Every number comes from a script in Part 1 or a command output. If you could not measure something, say so.
12. When a step says "STOP AND ASK", stop and ask Joshua. Otherwise do not ask; decide and note the decision in the report.

---

## Part 1. Measurement scripts (run on production, in the in-app browser)

Open `https://lsatprep.study/classroom/drill` signed in as Joshua (he is signed in on that browser). Run each script with the browser's JavaScript tool. Record the output verbatim in the report.

### 1a. Contrast scan

```js
(() => {
  const L = ([r,g,b]) => { const f = c => { c /= 255; return c <= 0.03928 ? c/12.92 : ((c+0.055)/1.055)**2.4; }; return 0.2126*f(r)+0.7152*f(g)+0.0722*f(b); };
  const parse = s => { const m = (s.match(/[\d.]+/g)||[]).map(Number); return { rgb: m.slice(0,3), a: m.length > 3 ? m[3] : 1 }; };
  const over = (top, a, under) => top.map((c,i) => Math.round(c*a + under[i]*(1-a)));
  const bgOf = el => { let n = el, stack = []; while (n && n.nodeType === 1) { const { rgb, a } = parse(getComputedStyle(n).backgroundColor); if (a > 0) stack.push({ rgb, a }); if (a >= 1) break; n = n.parentElement; } let out = [255,255,255]; for (let i = stack.length-1; i >= 0; i--) out = over(stack[i].rgb, stack[i].a, out); return out; };
  const ratio = (a, b) => { const x = L(a), y = L(b); return (Math.max(x,y)+0.05)/(Math.min(x,y)+0.05); };
  const root = document.querySelector('.drill-observatory-root') || document.body;
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
  const fails = [], seen = new Set(); let count = 0, node;
  while ((node = walker.nextNode())) {
    const t = node.textContent.trim(); if (!t) continue;
    const el = node.parentElement; if (seen.has(el)) continue; seen.add(el);
    const cs = getComputedStyle(el); if (cs.visibility === 'hidden' || cs.display === 'none') continue;
    const r = el.getBoundingClientRect(); if (r.width === 0 || r.height === 0) continue;
    const fg = parse(cs.color); const fgRgb = fg.a < 1 ? over(fg.rgb, fg.a, bgOf(el)) : fg.rgb;
    const bg = bgOf(el); const c = ratio(fgRgb, bg);
    const size = parseFloat(cs.fontSize), bold = parseInt(cs.fontWeight) >= 700;
    const large = size >= 24 || (size >= 18.66 && bold);
    const need = large ? 3 : 4.5; count++;
    if (c < need) fails.push({ text: t.slice(0,40), ratio: +c.toFixed(2), need, color: cs.color, bg: `rgb(${bg})`, cls: el.className.toString().slice(0,60) });
  }
  return { checked: count, fails };
})()
```

Caveat: text over a photograph reports the scrim colour, not the photo. For the hero (and Today, until WP-A removes its photo), also zoom the screenshot and confirm by eye that the lightest part of the photo under any text still reads. If unsure, darken the scrim.

Second caveat, added 2026-09-09 after it fired: `bgOf` walks **ancestors**, so text sitting on an absolutely positioned **sibling** is measured against whatever is behind that sibling. The section switch's active label reports 1.06:1 and is really 11.79:1. Both caveats are the same fault, which is that the scan reads the cascade rather than the pixels. A fail here is a question. See RUN3 §7.5.

### 1b. Target size scan

```js
(() => {
  const els = [...document.querySelectorAll('.drill-observatory-root a, .drill-observatory-root button, .drill-observatory-root [role="button"], .drill-observatory-root input, .drill-observatory-root select, .drill-observatory-root [tabindex="0"]')];
  const small = els.filter(e => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0 && r.height < 44; })
    .map(e => ({ text: (e.innerText || e.getAttribute('aria-label') || '').trim().slice(0,30), w: Math.round(e.getBoundingClientRect().width), h: Math.round(e.getBoundingClientRect().height), cls: e.className.toString().slice(0,50) }));
  return { total: els.length, under44: small };
})()
```
Everything on this page must be 44 by height. The active option of the section switch may report oddly because it sits on an absolutely positioned indicator; check it by eye if it appears.

### 1c. Focus ring scan

```js
(() => {
  const els = [...document.querySelectorAll('.drill-observatory-root a, .drill-observatory-root button, .drill-observatory-root input, .drill-observatory-root select, .drill-observatory-root [tabindex="0"]')];
  const bad = [];
  for (const e of els) { e.focus({ preventScroll: true }); const cs = getComputedStyle(e); const ok = (cs.outlineStyle !== 'none' && parseFloat(cs.outlineWidth) >= 2) || cs.boxShadow.includes('inset'); if (!ok && document.activeElement === e) bad.push({ text: (e.innerText||e.getAttribute('aria-label')||'').trim().slice(0,30), outline: cs.outline, shadow: cs.boxShadow.slice(0,50) }); }
  document.activeElement.blur();
  return { total: els.length, noRing: bad };
})()
```
Browsers apply `:focus-visible` only on keyboard focus, so this script can over-report. If it lists many, confirm manually: press Tab from the top and screenshot each stop. The manual check is the one that counts.

Added 2026-09-09: the `>= 2` width test can never pass in the in-app browser. A `div` created on the spot with `border: 2px solid` reports `1.6px` from `getComputedStyle` while its `height: 20px` reports 20; every width in that pane is scaled by 0.8 before it is reported. Press Tab once for real to arm the keyboard heuristic, then read `outline-style` and `box-shadow` and take the width from the source. See RUN3 §7.6.

### 1d. Headings, em-dashes, overflow, width

```js
(() => {
  const hs = [...document.querySelectorAll('.drill-observatory-root h1, .drill-observatory-root h2, .drill-observatory-root h3, .drill-observatory-root h4')].map(h => h.tagName + ': ' + h.innerText.trim().slice(0,40));
  const em = (document.querySelector('.drill-observatory-root')?.innerText.match(/\u2014/g) || []).length;
  const wide = [...document.querySelectorAll('.drill-observatory-root *')].filter(e => e.getBoundingClientRect().right > window.innerWidth + 1).map(e => e.className.toString().slice(0,50)).slice(0,10);
  return { viewport: window.innerWidth, docWidth: document.documentElement.scrollWidth, headings: hs, emDashes: em, pastRightEdge: wide };
})()
```
`docWidth` must equal `viewport`. `pastRightEdge` must be empty. Headings must read h1 then h2s, no skips.

### 1e. Glass and important counts (run locally, not in the browser)

```bash
grep -c 'backdrop-filter' src/components/classroom/classroom.css; grep -c '!important' src/components/classroom/classroom.css
```

### 1f. Viewports to measure at

Resize the in-app browser to each and run 1a to 1d at each: 375 wide (phone), 390, 768 (tablet), 1024, 1280, 1536. Take one full-page screenshot at 375 and at 1280 for the report. Scroll to the bottom at 375 and screenshot again (this catches the menu button problem).

### 1g. Baseline

Before any change: run 1a to 1e at 375 and 1280 on the current production build (f791016). Save the outputs in the report under "Baseline". Expected: contrast fails 0, under44 empty, headings h1/h2/h2/h2, em-dashes 0, backdrop-filter 8 lines (4 surfaces), important 200.

---

## Part 2. What each lost point is, and which WP fixes it

| Score row | Now | Target | Work packages |
|---|---|---|---|
| Audit 2 Performance | 3 | 5 | WP-A (glass down to one surface), WP-B (photos, fonts, Lighthouse) |
| Audit 3 Responsive | 3 | 5 | WP-C (menu button), WP-D (1024 date, phone copy, six-viewport sweep) |
| Audit 4 Theming | 3 | 5 | WP-E (`!important` to zero in the observatory block), WP-F (dark toggle honoured) |
| Audit 5 Anti-patterns | 3 | 5 | WP-A (one photograph, no glass on Today), WP-G (label count, text-shadow reliance) |
| Critique 2 Real-world language | 3 | 5 | WP-H (copy pass) |
| Critique 3 Control and freedom | 3 | 5 | WP-I (Escape, back, section memory) |
| Critique 4 Consistency | 3 | 5 | WP-J (type scale tokens, one icon size, one radius set) |
| Critique 5 Error prevention | 3 | 5 | WP-K (jump row validation, disabled-state reasons) |
| Critique 7 Flexibility | 3 | 5 | WP-L (shortcut hints, resume last drill) |
| Critique 8 Aesthetic and minimal | 3 | 5 | WP-A, WP-G, WP-D |
| Critique 9 Error recovery | 3 | 5 | WP-M (every fetch has a retry and a plain sentence) |
| Critique 10 Help | 2 | 5 | WP-N (inline "what this is" disclosure, first-run line, help link) |

Order of execution: A, B, C, D, E, F, G, H, I, J, K, L, M, N. Push and publish after A+B, after C+D, after E+F, after G+H+I+J, after K+L+M+N. That is five publishes. Measure after each publish and record.

---

## Part 3. Work packages

Each WP has: Why, Steps, Done when. Do the steps in order.

### WP-A. One photograph, glass on one surface only

**Why.** Four `backdrop-filter` surfaces cost paint time on phones (Performance) and the "glass card over photo" look is the single strongest tell of the aesthetic family (Anti-patterns, Aesthetic). The hero keeps its photograph; the Today card becomes flat near-black like the practice card. Glass stays only on the hero console, which sits over the photo.

**Steps.**
1. In classroom.css find the rule that puts the eclipse photograph behind Today. Search for `drill-observatory-today` near `background-image` or `url(`. Note the selector.
2. Remove the photograph and the scrim `::before` from Today. Give Today the same surface as the practice card: `background: var(--observatory-surface-card)`.
3. `.drill-observatory-today-primary` (line ~1821): delete the two `backdrop-filter` lines. Change `background` to `rgba(244, 241, 234, 0.04)` (a faint lift on flat black), keep the ring.
4. `.drill-observatory-today-rail` (line ~1867): delete the two `backdrop-filter` lines. Background `rgba(244, 241, 234, 0.035)`. Hover: background `rgba(244, 241, 234, 0.06)`, no 24px shadow, keep the 2px lift.
5. `.drill-observatory-today-quiet` (line ~1888): delete the two `backdrop-filter` lines. Same background as the rail.
6. `.drill-observatory-console` (line ~1383): keep the blur. Reduce to `blur(12px)`.
7. Text inside Today no longer sits on a photo, so remove every `text-shadow` inside Today (search `text-shadow` between the Today selectors). Text shadows stay only in the hero.
8. Run 1e locally: `backdrop-filter` count must be 2 lines (one surface, plus its `-webkit-` twin).
9. Re-run contrast (1a) after publish. Any Today text now measured against `#08080b` plus the faint lift must still pass 4.5. If a label fails, raise its ink step (never below ink-50).
10. Update the surface brief: in "The ground", change "Two of the three cards carry a photograph" to "One card, the hero, carries a photograph"; in "Depth", change the glass sentence to "Glass appears only on the hero console."

**Done when.** One photo on the page, `backdrop-filter` appears on one selector, contrast scan 0 fails at 375 and 1280, tests pass, brief updated.

### WP-B. Photo, fonts, and a Lighthouse number

**Why.** Performance 5 needs evidence, not a feeling. Get a Lighthouse mobile performance score on the hub and fix whatever it names.

**Steps.**
1. Find the hero photograph asset: search classroom.css for `url(` inside the `.drill-observatory-hero` rule (line ~1034). Note the file and its size on disk (`ls -la` the path under `public/` or `src/assets/`).
2. If the file is over 250 KB or is a PNG/JPEG without a modern alternative: create a WebP at the display size (the hero is at most 1200px wide; export at 1600px for retina, quality 80) with `npx sharp-cli` or `cwebp`. If neither tool installs, STOP AND ASK. Reference the WebP with a fallback: use `image-set()` in the CSS background, or switch the hero to an `<img>` with `<picture>` if that is simpler. Keep the crop identical.
3. Fonts: find where Fraunces, JetBrains Mono, and Outfit are loaded (search `index.html` and `src/index.css` for `fonts.googleapis` or `@font-face`). Ensure `display=swap` (Google) or `font-display: swap` (self-hosted). Add `<link rel="preconnect">` for the font host in `index.html` if missing.
4. Check the hub does not animate a layout property: search the observatory block for `transition:` lines that include `height`, `width`, `padding`, `margin`, `top`, `left`. Change each to `transform` or `opacity`, or remove the transition.
5. Run Lighthouse on production in mobile mode. If the Chrome DevTools MCP is available, use `lighthouse_audit` on `https://lsatprep.study/classroom/drill`. If it is not, install and run it locally against production:
```bash
npx lighthouse https://lsatprep.study/classroom/drill --preset=perf --form-factor=mobile --only-categories=performance --output=json --output-path=./lighthouse-drill.json --chrome-flags="--headless"
```
   Note: the page needs a signed-in session, so an unauthenticated Lighthouse run may land on the sign-in page. If the report's `finalUrl` is not `/classroom/drill`, say so in the report and use the DevTools MCP route instead, or STOP AND ASK.
6. Record the performance score, LCP, CLS, TBT. Fix anything Lighthouse names that is inside the hub (not the shell). Target: performance 90+, CLS under 0.05.
7. Delete `lighthouse-drill.json` before committing.

**Done when.** A recorded Lighthouse mobile score for the hub, WebP hero (or a note that the asset was already small), fonts swap, no layout-property transitions in the block.

### WP-C. The phone menu button stops floating over content

**Why.** On phones the menu button is `position: fixed` at 16px/16px, so once the student scrolls it sits on top of "Your practice" and the Today card. This is the one Responsive defect that is a real usability problem.

**Steps.**
1. In `ClassroomLayout.tsx` around line 1019 the button is rendered as a direct child of the root. Wrap it in a bar: `<div className="classroom-mobile-bar">` containing the button and, to its right, a small text label with the section name (there is an `activeSection` value already in scope; render its display label, or "Drill" on the drill root). Keep the button's `aria-label`.
2. In classroom.css, add:
```css
.classroom-root .classroom-mobile-bar { display: none; }
@media (max-width: 1023px) {
  .classroom-root .classroom-mobile-bar {
    align-items: center;
    background: var(--classroom-page);
    border-bottom: 1px solid var(--classroom-line);
    display: flex;
    gap: 12px;
    height: 56px;
    padding: 0 12px;
    position: sticky;
    top: 0;
    z-index: 70;
  }
  .classroom-root.classroom-root-drill .classroom-mobile-bar { background: var(--classroom-drill-page); }
  .classroom-root .classroom-mobile-menu-button { position: static; }
  .classroom-root .classroom-column { padding-top: 16px; }
  .classroom-root.classroom-root-drill .classroom-stage { padding-top: var(--observatory-space-4); }
}
```
   Check the existing rule at classroom.css ~3114 (`padding: 72px 0 90px`) and the drill stage rules at ~1984 and ~2014 (`padding-top: 72px`). Change those 72px values to 16px, because the bar now takes its own space. Do the same for `.classroom-root-schedule` at ~3119.
3. The bar is sticky, so it stays at the top while scrolling but is part of the flow. Confirm the jump row starts right under it with no overlap at 375.
4. Every other classroom section (Home, Messages, Schedule, Workspace) shares this shell. Open each on production at 375 after publish and screenshot the top. Nothing may overlap the bar. If a section had its own 72px allowance somewhere else, adjust it.
5. The bar text: mono label style is wrong here (this is the shell, not the hub). Use the shell's own label style, `--classroom-meta-text`, 13px, weight 500.

**Done when.** At 375 and 768, scrolled to the bottom of the hub, the menu button is in a bar above the content and covers nothing. All five classroom sections screenshot clean at 375.

### WP-D. 1024px date, phone console copy, six-viewport sweep

**Steps.**
1. Date at 1024: in `AcademyMainhub.tsx` line ~90, compute a short label too: `monthShort` with `{ month: "short", day: "numeric" }`. Render both spans: `<span className="drill-observatory-date-long">` and `<span className="drill-observatory-date-short">`. In classroom.css: `.drill-observatory-date-short { display: none; }` and inside `@media (min-width: 900px) and (max-width: 1099px) { .drill-observatory-date-long { display: none } .drill-observatory-date-short { display: inline } }`. Result at 1024: "TUESDAY · SEP 8 · 2026" on one line.
2. Console copy on phones (the paragraph at AcademyMainhub.tsx ~line 213 runs five lines at 375). Replace the LR sentence with: "Pick PrepTests, question types, and difficulty. See the exact set before you start." Replace the RC sentence with: "Pick PrepTests, topics, and difficulty. Choose the passages or let the set fill itself." These are shorter on every viewport, so no phone-only variant is needed.
3. The fallback hero paragraph (no assignment, line ~161) is fine at 375; leave it (WP-H rewrites its words).
4. Sweep: after publish, run Part 1 at all six widths. Fix anything that wraps badly, overlaps, or overflows. Typical culprits: the Next up facts line at 375 when the source name is long (let it wrap, it is `flex-wrap`), the section switch beside the search at 768.
5. Add a test in `AcademyMainhub.test.tsx` that the short and long date spans both render (query by text matching `/\d{4}$/`).

**Done when.** Six viewports measured clean, date one line at 1024, console paragraph at most three lines at 375.

### WP-E. `!important` to zero inside the observatory block

**Why.** 200 `!important` declarations exist to beat shadcn's Card and Button styles. Theming 5 needs the cascade to work without force.

**Steps.**
1. Understand why they are there: `Card` and `Button` from `src/components/ui/` apply Tailwind utility classes (`rounded-lg border bg-card shadow-sm`, `inline-flex h-10 px-4 ...`). Tailwind utilities have single-class specificity; the observatory rules are also mostly single-class, so the author used `!important` to win. The fix is specificity, not force.
2. Wrap every observatory selector in the block (lines ~840 to ~2060) with the root: `.drill-observatory-root .drill-observatory-cta { ... }` has (0,2,0) and beats any utility. Do this mechanically with a script, not by hand. Write `scripts/observatory-specificity.mjs` that:
   - reads classroom.css,
   - for every rule between the line containing `.drill-observatory-root {` and the line containing `/* end observatory */` (add that comment marker at the end of the block first, after the reduced-motion rule at ~2055),
   - for each selector in a rule's selector list that starts with `.drill-observatory-` and is not already prefixed, prefixes `.drill-observatory-root `,
   - strips ` !important` from every declaration in that range,
   - writes the file back and prints counts.
   Media queries inside the range are handled the same way (the script only touches selector lines and declaration lines; braces stay).
3. Run the script once. Run typecheck and tests. Publish (with WP-F). Then measure: screenshot at 375 and 1280 and compare to the WP-D screenshots side by side. Anything that changed shape means a rule lost to a utility. Find the rule, raise its specificity by one more class (for example `.drill-observatory-root .drill-observatory-hero .drill-observatory-cta`), never by `!important`.
4. Known hot spots to check first after the script: the CTA (`h-10` and `px-4` from Button), the console start button, the hero Card (`rounded-lg border shadow-sm`), the practice Card, Today's inner Card, the `min-height` on the hero grid.
5. The rules for `.classroom-root.classroom-root-drill ...` (lines ~840 to ~980) are outside the observatory root; leave their `!important`s for this WP but count them separately in the report.
6. Target: `grep -c '!important'` on the file drops from 200 to under 30, and zero of the remaining are inside the observatory block. Record before and after counts.
7. Update the surface brief "Known debt": remove the `!important` line and replace it with one sentence: "Observatory rules are scoped under `.drill-observatory-root` and win by specificity, not `!important`."

**Done when.** Zero `!important` between the observatory markers, page looks identical at 375 and 1280 to the WP-D screenshots, tests pass.

### WP-F. The hub honours the theme toggle

> **2026-09-09.** Done on branch `wp-f-dark-stage`, PR #103, as its own piece of work. Step 2's premise was half wrong: the stage already flipped in dark; only the two stage controls did not. RUN3 §6a has the measurements. The steps below are left as written.

**Why.** The app has a light/dark toggle (`ThemeContext.tsx` adds `.light` to `<html>`; default is dark). The hub renders the same cream stage in both. Theming 5 means the room responds.

**Steps.**
1. Find where the hub's stage tokens are declared: `--observatory-stage-well`, `--observatory-stage-ink`, `--observatory-stage-muted`, `--observatory-stage-hair`, `--observatory-stage-lit` (classroom.css ~line 862 onward, under `.classroom-root.classroom-root-drill, .drill-observatory-root`). Also `--classroom-drill-page` at lines 22 (light, `#fdf8f3`) and 59 (dark, `#121019`).
2. Decide the dark stage: `--classroom-drill-page: #121019` already exists for dark. Add a dark set of stage tokens next to it in the same dark block: `--observatory-stage-well: #1a1822; --observatory-stage-ink: #ece8e1; --observatory-stage-muted: #a39e98; --observatory-stage-hair: rgba(236,232,225,0.12); --observatory-stage-lit: #211f2a`. The cards stay `#08080b` in both themes (they are already dark).
3. Make the observatory block read those tokens from the theme rather than redeclaring them. If the observatory root redeclares `--observatory-stage-*` with literal values, move the declarations up into the light and dark blocks at lines ~22 and ~59 and delete them from the observatory root.
4. The jump row and section switch use `--observatory-stage-*` (via `--qj-*` aliases in questionJump.css and the toggle rules). Confirm they follow.
5. Contrast in dark: stage muted `#a39e98` on `#1a1822` is about 6.2:1, ink is about 12:1. Verify with 1a after publish, in both themes. Toggle the theme from the account menu in the browser; if you cannot find the toggle, ask Joshua where it is.
6. Update the surface brief "The ground": "The stage is cream in light theme and near-black `#121019` in dark; the cards are `#08080b` in both." Remove the dark-toggle line from Known debt.

**Done when.** Toggling the theme changes the stage, the jump row, and the section switch; contrast passes in both; the brief says so.

### WP-G. Fewer labels, less text-shadow, quieter hero

**Why.** Anti-patterns and Aesthetic. The mono uppercase micro-label is used many times on one screen; each one is a decoration when it is not carrying a fact. Text-shadow on every hero line is doing the scrim's job.

**Steps.**
1. Count `drill-observatory-label` usages rendered on the default LR stage (search the three TSX files). List them in the report. Keep: the "Next up" facts line, the date, the "Your practice" and "Also today" card headings, the insight kicker. Remove: any label that repeats the heading above it, and any label on a control (a button says what it does in sentence case).
2. Hero text-shadows: with the scrim doing its job, reduce `text-shadow` on `.drill-observatory-greeting h1` to `0 1px 2px rgba(0,0,0,0.35)` and on `.drill-observatory-greeting p`, `.drill-observatory-next-title`, `.drill-observatory-quiet-link` to `0 1px 2px rgba(0,0,0,0.3)`. Then re-run 1a and check by eye at the lightest crop of the photo. If any hero text is hard to read, darken the scrim by 0.05 alpha rather than restoring the shadow.
3. The quiet link underline: `text-decoration-color: rgba(244, 241, 234, 0.55)` (was 0.35).
4. The CTA's `box-shadow: 0 8px 32px rgba(0,0,0,0.4)` (classroom.css ~1249): reduce to `0 6px 20px rgba(0,0,0,0.3)`.
5. Screenshot the hero at 1280 before and after; put both in the report.

**Done when.** Label count on the LR default stage is at most 6, shadows reduced, contrast still 0 fails.

### WP-H. Copy pass in the teaching voice

**Why.** Critique 2 is about the student's words, not the product's. Read `wiki/teaching-voice.md` and `wiki/COPY-CORRECTIONS.md` first.

**Steps.**
1. List every string a student sees on the hub (hero, console, practice, Today, jump row, search trigger, section switch, loading and error states). Put the list in the report with a column for the new text.
2. Rules for the new text: sentence case on buttons and headings; the verb first on buttons; say what the thing does before naming it; no "Smart" as a bare adjective without the sentence explaining it; no "instead" links that assume the student rejected the first option.
3. Specific changes:
   - Quiet link "Start a Smart Drill instead" becomes "Or practice your weakest types". RC: "Or read one passage now".
   - Fallback CTA "Start Smart Drill" becomes "Practice your weakest types". RC "Start One Passage" becomes "Read one passage".
   - Fallback paragraph: "Start with the question types you miss most, or build a drill around exactly what you want to practice." RC: "Read one passage now, untimed, with the answers after it. Or build a set of passages around what you want to read."
   - "Set up an LR drill" stays. "Set up an RC drill" stays.
   - "Analytics" and "Journal" links stay.
   - Insight action labels: check each in `insightSlides.ts` against rule 2. Rewrite any that names a screen instead of an outcome ("Open analytics" becomes "See where you lose points").
   - Today "Also today" stays. Its empty line stays.
   - Jump row placeholder stays ("PT101.S2.Q1" form).
4. The heading in the console "Build the drill you need." stays; it is the one door and it says what it does.
5. Update tests that assert the old strings (`AcademyMainhub.test.tsx` looks for "Start Smart Drill" and similar; search the three test files for each old string).
6. Add the new strings to `wiki/COPY-CORRECTIONS.md` under a dated heading so future work does not revert them.

**Done when.** Every string in the list has been checked, tests updated and green, the corrections log has the entry.

### WP-I. Control and freedom: Escape, back, section memory

**Steps.**
1. Escape closes a stage. In `AcademyMainhub.tsx`, where `stage` is read from the URL and `closeStage` exists (~line 560), add a `useEffect` that listens for `keydown` on `window`; if `event.key === "Escape"` and `stage !== "default"` and the event target is not inside an open dialog or a text input with content, call `closeStage()`. Clean up the listener.
2. Browser back returns to the hub. Check that opening a stage uses `navigate` with a new history entry (not `replace: true`), so back works. If it uses replace, change it to push. Test by opening the builder on production, pressing the browser back button, and confirming the hub returns with the same section.
3. Section memory. When the student switches LR/RC, persist the choice in `localStorage` under `lsatu.drillHub.section`. On mount, if the URL has no `section` param, read it and apply it. Wrap the storage calls in `try/catch`.
4. Cancel in the builder keeps the student's choices for the session: if `QuestionPicker` already holds its state in a store or URL, leave it; if it resets on Cancel, note that in the report (do not build persistence for the builder in this plan).
5. Tests: one test each for Escape closing the stage and for section memory (mock `localStorage`).

**Done when.** Escape works on both stages, back works, the section is remembered across reloads, tests pass.

### WP-J. Consistency: a type scale, one icon size, one radius set

**Steps.**
1. Grep the three TSX files and the observatory block for font sizes: `text-\[`, `font-size:`. List every distinct value. There are at least 12.5px, 13.5px, 14px, 15px, 19px, 20px, 22px, and several clamps.
2. Define a scale as tokens on `.drill-observatory-root`: `--observatory-text-xs: 11px` (mono labels), `--observatory-text-sm: 13px`, `--observatory-text-base: 14px`, `--observatory-text-md: 16px`, `--observatory-text-lg: 19px`, `--observatory-text-xl: 22px`, plus the existing display token. Map every literal to the nearest token. 12.5 becomes sm, 13.5 becomes base, 15 becomes md.
3. Arrow icons: the hero CTA uses 14px (`h-3.5`), the console 16px (`h-4`), insights 13px. Make them all 14px with `strokeWidth={2}`.
4. Radii: list `border-radius` values in the block; there should be exactly three tokens (panel, inner, control) plus `999px` for pills. Replace any literal.
5. Spacing: the block already has `--observatory-space-*`. Replace any literal `px` margin or padding in the block that is not from the scale, unless it is a 1px hairline.
6. Screenshot before and after at 1280. Differences should be sub-pixel.

**Done when.** No literal font-size in the block or the three TSX files outside the tokens, icons one size, radii from tokens.

### WP-K. Error prevention

**Steps.**
1. Jump row (`QuestionJump.tsx`): the three selects (PT, section, question) should never submit an impossible combination. Confirm the question select is disabled until a section is chosen and its options come from the chosen PT and section. If the row has a Go button, disable it until all three are chosen, and add `aria-describedby` pointing at a one-line hint "Choose a PrepTest, then a section, then a question" that shows when the button is disabled. If the row navigates on the third select without a button, confirm that and leave it.
2. Hero CTA: it is `disabled` when `!primary.route && !primary.onOpen`. A disabled button with no reason is a trap. When disabled, render beneath it, in `drill-observatory-ink-60` at text-sm: the true reason. Read `useTodayFocus.ts` to see when route and onOpen are both empty and write the sentence that matches (for example "This item opens from your Classroom home.").
3. Section switch: switching LR to RC while a stage is open should not lose the stage. Check the URL handling; if switching resets `stage`, keep it.
4. Builder: not in scope beyond what the console opens. Note anything you see for later.

**Done when.** No control on the hub can be activated into a dead end without a sentence saying why.

### WP-L. Flexibility

**Steps.**
1. Keyboard shortcut hint without the badge Joshua removed: on the search trigger add `aria-keyshortcuts="Meta+K Control+K"` and a `title="Search questions (Ctrl K)"`. No visible badge.
2. Resume last drill: `useTodayFocus.ts` already knows about an in-progress drill if one exists (status "Resume drill"). If the student has an unfinished drill and no assignment, the hero CTA should be "Resume your drill" with the fallback link beneath. Read the hook; if that case already leads, confirm and note it; if not, add it as the primary when `items` is empty and a resumable drill exists. Do not fabricate a resume state; only use what the hook already loads.
3. Section memory (WP-I) counts here too.
4. Power path: pressing `/` while no input is focused opens the search. Add this in the same `keydown` effect as Escape.

**Done when.** Shortcuts documented in ARIA, `/` opens search, resume leads when it applies, nothing new is fabricated.

### WP-M. Error recovery

**Steps.**
1. List every data source the hub reads: `useTodayFocus` (assignments), `useStudentAnalytics` (insights), the question bank for the launcher, RC history. For each, find what the UI does when the request fails.
2. Each failure gets: one plain sentence saying what did not load, and a "Try again" button that refetches (TanStack Query exposes `refetch`; the launcher already has "Reload the question bank"). Use `drill-observatory-insight-link` styling for the button so it is 44px and has a focus ring.
3. Today: if assignments fail, the hero must not pretend there is nothing assigned. Render the fallback paragraph plus the sentence "Your assigned work did not load. Try again." with the button. `useTodayFocus` returns `hasError`; use it.
4. Insights: if analytics fail, the practice card shows the sentence and button in place of the list, not the streak slide.
5. Offline: if `navigator.onLine` is false at mount, show one line at the top of the hero: "You are offline. Your last loaded work is shown." Only if the app already has an online listener pattern elsewhere; otherwise skip and note.
6. Tests: mock a failed `useTodayFocus` (hasError true) and assert the sentence and button render.

**Done when.** Every source has a failure sentence and a retry, verified in tests; no failure renders an empty or misleading state.

### WP-N. Help

**Why.** Critique 10 was 2. Nothing on the hub explains what an adaptive drill is, what Today means, or how to get help. Three small pieces fix it without adding a documentation page.

**Steps.**
1. Inline disclosure under the fallback paragraph (no assignment): a `<details>` styled as a quiet link, summary "How the adaptive drill picks questions". Body, three sentences: "It looks at the question types you miss most often and pulls from those first. Each set is ten questions. Your results feed the next set." Confirm the ten with the drill code (`/drill` adaptive mode, search for the set size); if it is not ten, write the true number. If you cannot find it, leave the count out.
2. Under the hero when an assignment leads, add one line in `drill-observatory-ink-60` after the facts: "Assigned work shows here first. Your own practice is below." Show it only the first three times the student sees the hub with an assignment; count in `localStorage` under `lsatu.drillHub.assignedHintSeen`. Wrap in `try/catch`.
3. Help link: the hub has `MainhubHelpControl` (a message thread to Joshua). Make sure it is reachable from the hub with a visible control labelled "Ask Joshua". If it is already in the dock, confirm the label and its 44px size; if it is not, do not add a new floating button. Note the state in the report.
4. Tests: the disclosure renders in the no-assignment state and is absent when an assignment leads.

**Done when.** A student with nothing assigned can learn what the adaptive drill does without leaving the page; a student with an assignment is told why it leads; help is one labelled control away.

---

## Part 4. Publish and verify cycle (five times)

After each group (A+B, C+D, E+F, G+H+I+J, K+L+M+N):

1. `npm run typecheck` clean.
2. `npx vitest run src/pages/AcademyMainhub.test.tsx src/pages/AcademyMainhub.section.test.tsx src/components/mainhub` green. Paste the summary line in the report.
3. `git add -A && git commit` with a message naming the WPs.
4. `bash .claude/safe-push.sh`. Paste its last line.
5. Tell Joshua: "Pushed <hash>. Ready to publish." Wait.
6. After he confirms: hard-reload production, confirm the build is new (the hero shows the change you made), then run Part 1 at 375 and 1280 (all six widths on the last cycle). Record everything under a heading for that cycle.
7. If anything regressed (a contrast fail, a target under 44, an overflow), fix it before starting the next group.

---

## Part 5. Re-score

After the fifth cycle, re-score every row in the two tables using the same rubric as the run 2 report. For each row write one sentence of evidence tied to a script output or screenshot. A 5 without evidence is a 3. If a row cannot honestly reach 5, say what would be needed and why it was not done.

---

## Part 6. Report

Write `C:\Users\Joshu\dev\ai-os\wiki\DRILL-HUB-IMPECCABLE-AUDIT-2026-09-08-RUN3.md` with these sections, in this order:

1. Commits (hash and one line each).
2. Baseline outputs (Part 1g).
3. One heading per publish cycle with the script outputs and screenshots (send the screenshots to Joshua with SendUserFile too).
4. The two score tables, run 2 versus run 3, with evidence sentences.
5. Decisions you made where the plan said "decide and note".
6. Anything skipped, blocked, or left for Joshua, with the reason.
7. The updated surface brief diff summary.

Then send Joshua the tables and the skipped list in chat.
