# Claude Opus 5.5 independent visual critique

Observed model: claude-opus-5-5. Verdict: REVISE. Screenshots reviewed through Claude Read, not a live browser.

The design has moved well past "bland and neutral." Its strengths are a confident cobalt resume hero, an excellent cream "Continue at prompt 6" pill, the orange full stops on "Ada." and "Station.", restrained top navigation, the large numeral reference selector (155 / 1 / 01), and an honest demo caption. It is not yet a top-tier product, for three reasons:

1. **Color decorates cards instead of meaning something.** There are four saturated surfaces of near-equal weight, plus a blue selected day.
2. **Small, hard-to-read type.** The type jumps from 48–76px display text straight to 9–12px text. Every practical fact (session time, durations, progress, items to revisit) sits at the bottom of that range.
3. **The planning tools are pushed down and thin.** The seven-day calendar comes last, below the library, and its cells show nothing but dates.

**Diagnosis:** a bento grid of attractive mood cards that don't tell the student anything specific.

**The one move that would give it its own identity:** make the orange full stop the brand's "you are here" mark. Use one orange token, and give it one job: where the student currently is. It would appear on:
- the headline periods
- a 12-tick progress rail in the hero, where the current tick is the full stop
- today's dot in the calendar
- the "revisit" marker on the progress card

Pair that with color tied to meaning: blue for logical reasoning (LR), lilac for reading comprehension (RC), coral for tutor sessions and yellow for review. Then the color system teaches the interface instead of decorating it.

**Mismatch between the brief and what was shown:** the brief describes a pale aqua background, a yellow question studio, a charcoal resume hero and editorial serif type. The pass-1 screenshots and current source show:
- a warm off-white page background (`--paper oklch(96.3% .007 90)`)
- a cobalt hero
- a coral session card
- a yellow progress card
- a lilac library

The serif (Newsreader italic) appears only in "Make it yours." and in dialogs. The source colors match the screenshots.

**Known issues, as seen:** at 390px the knot overlaps "Negation", and at 1440px its quad facets are clearly visible. Neither is counted as a finding below.

## F1-micro-type (high)

The type scale has no readable middle tier. Display sizes are 48/64/73/44px (h1 at style.css:4, hero h2 and session date at :5-6, library h2 at :9). Everything practical is 9–12px:
- `.tutor-line div>span` ("7:15 pm · 60 minutes") is 10px.
- `.assignment-end` ("20 min") is 10px.
- `.hero-bottom` ("5 of 12 complete", "About 15 minutes") is 10px.
- `.practice-footer` ("1 question to revisit") is 10px.
- `.metadata`, `.day>span`, `.demo-caption`, `.question-ticket>small` and `.sculpture-label` are 9px.
- At ≤900px `.metadata` drops to 8px, and at ≤370px `.day>span` drops to 7px.
- The body base is 14px; every size is in px with no rem.

In pass-1-1440.png the session time, durations and items to revisit are the faintest, smallest text on screen, while the tagline "A good question changes everything." is 26px. This fails the typeset reference (body text at least 16px, a consistent ratio, rem units) and its point that hierarchy should follow importance.

**Recommended fix**

Add rem tokens and use them everywhere:
`:root{--t-cap:.75rem;--t-meta:.8125rem;--t-body:1rem;--t-lead:1.125rem;--t-h3:1.375rem;--t-h2:2rem;--t-display:4rem}`

- Set a hard minimum of 12px: delete every 7/8/9/10px declaration in style.css lines 4–18.
- Make actionable facts bold, not tiny:
  - `.tutor-line div>span{font:600 var(--t-lead)/1.3 var(--body);font-variant-numeric:tabular-nums}`
  - `.assignment-end>span{font:600 var(--t-meta) var(--body);font-variant-numeric:tabular-nums;color:var(--ink)}`
  - `.hero-progress>span,.practice-footer{font-size:var(--t-meta)}`
- Demote decorative copy instead: delete `.sculpture-label` and cut the session h2 to `var(--t-h3)`.
- Set `body{font-size:1rem}`.

## F2-week-buried-and-empty (high)

The brief names weekly planning as a core task, but `.week-section` comes last in the DOM, after the 500px library slab (index.html:15). In pass-1-1440.png it sits at y≈1700–1870, about two screens down.

Each `.day` cell (min-height 99px) shows only the weekday, the numeral and a 4px dot. The plan behind it (Mon recall, Wed "Find the flaw", Fri saved questions in app.js:39) is only visible by clicking one day at a time to update the agenda (app.js:42).

- The dot color `#b9b6bb` on the paper background is about 1.8:1, below the 3:1 non-text contrast requirement.
- Today's date is shown four times: the right side of the greeting, the 73px "24" in the session card, the selected SAT 24 cell, and the agenda's "Saturday, October 24".
- The desk rows never say which day they are planned for, so the desk and the week are disconnected.

**Recommended fix**

Move `<section class="week-section">` directly after `.opening-grid` and render the task inside each cell. In app.js:41, render:
`<button class="day" data-kind="lr"><span>WED</span><strong>28</strong><em class="day-task">Find the flaw<small>LR · 20m</small></em></button>`

CSS:
- `.day{min-height:128px;align-items:flex-start;padding:12px;justify-content:space-between}`
- `.day-task{font:600 .75rem/1.3 var(--body);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;padding-left:8px;border-left:3px solid var(--kind)}`
- Set `--kind` by `[data-kind]`: lr = blue, rc = lilac ink, session = coral ink.
- Empty days get a dashed outline with "+ Add intention".

Add "Wed"/"Mon" to `.assignment-end` in the desk rows.

At ≤680px:
- `.week{grid-auto-flow:column;grid-template-columns:none;grid-auto-columns:minmax(76px,1fr);overflow-x:auto;scroll-snap-type:x mandatory}`
- `.day{scroll-snap-align:start}`

Drop the separate agenda panel, or keep it only for the add-intention action.

## F3-color-without-meaning-and-competing-ctas (medium)

The cobalt hero, coral session, yellow progress and lilac library each get a hue by card, not by meaning. The desk-row art is coral for LR and lilac for RC, while the hero, which is also LR, is blue. Eight unrelated orange values compete for the accent:
- `#ec754f` (h1 period)
- `#ffbd94` (hero period)
- `#ffbb95` (progress)
- `#ffbf9b` (day dot)
- `#ed6b37` (focus)
- `#e36543` (notification)
- `#f18457`, `#bd4d2c` (art)

In pass-1-1440.png, the coral card's 73px "24" is the second-heaviest mark on the page, competing with "Negation Station." for what is only today's date. The ink-on-coral "Prepare for your session" button has more contrast than the cream-on-blue "Continue at prompt 6". The full-width black "Open sample question" repeats that weight, so the eye has three primary calls to action.

**Recommended fix**

Use semantic tokens:
`--lr:var(--blue);--rc:oklch(52% .14 293);--tutor:oklch(55% .13 32);--review:oklch(55% .1 80);--mark:oklch(68% .17 42)`

- Replace every orange hex with `var(--mark)`; keep one lighter variant, `--mark-on-blue`.
- Recolor `.coral-art` to the LR hue so the desk, week chips and hero agree.
- Demote the session card:
  - Make the large numeral the time: "7:15" with "pm · tonight".
  - `.session h2{display:none}` (or cut it to 1.125rem).
  - `.session .button{background:transparent;color:#472924;box-shadow:inset 0 0 0 1.5px #472924}`
- Make `.reference-submit` a secondary style too: `background:#fff;color:#2f263a;box-shadow:inset 0 0 0 1px #d7cfdf`.
- The hero CTA is then the only filled primary button above the fold.

## F4-hero-spends-space-on-spectacle-not-the-next-prompt (medium)

In index.html:9 the knot takes `grid-template-columns:1fr 42%` (style.css:5), about 400px of the most valuable surface. The only copy beside it is the filler "A different angle. A clearer argument." and a generic tagline.

The actual next prompt is known in app.js:34-35 (with progress=5, prompt 6 is "Every volunteer attends the briefing."), but the student never sees it before clicking.

Progress is a 3px bar 145px wide (`.progress-track`), which is hard to read in pass-1-hero-1440.png.

"Joshua's note ↗" uses an external-link arrow for an in-page dialog (app.js:44 `note`). So do "Explore this sample ↗" and "Saved 0 ↗". This works against the product reference's "earned familiarity".

**Recommended fix**

Add a preview of the next prompt next to the CTA:
`<figure class="next-prompt"><figcaption>Prompt 6 · Negate this</figcaption><blockquote id="next-sentence">Every volunteer attends the briefing.</blockquote></figure>`

Style it:
- `.next-prompt{background:oklch(50% .2 270);border-radius:16px;padding:18px 20px;max-width:340px}`
- `blockquote{font:italic 1.375rem/1.3 Newsreader,serif;margin:6px 0 0}`
- Fill it from `drillPrompts[(progress-5)%3].sentence` inside `updateProgress()`.

Set the sculpture column to 32%, or let the knot sit partly behind the card at `opacity:.9`. Delete `.sculpture-label`.

Replace the bar with 12 ticks:
- `.progress-track{display:grid;grid-template-columns:repeat(12,1fr);gap:3px;height:6px;background:none}`
- Render 12 `<i>` elements, with done = `#d5d9ff` and current = `var(--mark)`. The current tick becomes the signature full stop.

Swap ↗ for → (or nothing) on controls that open dialogs.

## F5-progress-card-misleads (medium)

"Small steps. Visible progress." plots three different skills as one rising series:
- Oct 21: Reading comprehension, 5/8
- Oct 22: Argument structure, 6/8
- Oct 23: Necessary assumptions, 9/10

The data is in app.js:37 and the bars in index.html:13. The x-axis says only "21 22 23", so the chart implies improvement that the data doesn't show. A student could read RC→LR differences as growth.

The unselected bars (`#e5c97f` on the yellow card) are about 1.3:1 and nearly invisible in pass-1-1440.png. That fails 3:1 for graphical objects.

The one actionable item, "1 question to revisit", is 10px footer text, and its link says "Explore this sample" rather than naming the question.

**Recommended fix**

Reframe the card around review.

- Header: "1 to revisit". Then a full-width button: "PT 155 / S1 / Q1 · Necessary assumptions →" that calls `question(bank[sets[currentSet].question])`.
- Below it, show per-skill accuracy as labelled horizontal meters:
  `<div class="skill"><span>Assumptions</span><meter min=0 max=10 value=9></meter><b>9/10</b></div>`
  with a track of `#e9d39a` and a fill of `#786038`.
- Alternatively, show a real same-skill trend.
- If vertical bars stay: label them with skill abbreviations (NA, AS, RC), not bare dates, and set unselected bars to `#b8964a` or darker (≥3:1 on the card).

## F6-mobile-missing-spaces (medium)

pass-1-library-390.png shows two run-together lines: "Find it.Question it." and "The ones you saved.The ones you’re still thinking about."

style.css:17 (≤680px) sets `.library-intro h2 br{display:none}` and `.library-intro p br{display:none}`. The markup at index.html:14 has no whitespace around those `<br>` tags (`Find it.<br>Question it.`, `The ones you saved.<br>The ones…`). Hiding the break therefore joins the sentences.

**Recommended fix**

Put a real space before each break in index.html:14: `Find it. <br>Question it. <br><em>…` and `The ones you saved. <br>The ones…`.

Alternatively, wrap each line in `<span class="line">` with `.line{display:block}` on desktop and `display:inline` on mobile, leaving a trailing space inside each span.

## F7-mobile-above-the-fold-budget (low)

In pass-1-hero-390.png, the hero (about 455px) and session card (about 350px) together take about 830px before any assignment, calendar or library appears.

The session card's two-column layout (style.css:17, `.session{grid-template-columns:1fr 1fr}`) squeezes the tagline h2 into four lines at 22px. Meanwhile "7:15 pm · 60 minutes" stays at 10–11px.

On mobile the calendar comes after the desk, the progress card and the full library console.

**Recommended fix**

At ≤680px, compress the session card to one strip:
- `.session{display:flex;flex-wrap:wrap;gap:12px;padding:16px 18px}`
- `.session-date,.session h2,.prep-peek{display:none}`
- `.tutor-line strong::after{content:' · tonight 7:15'}`, or render the time in the DOM.
- `.session .button{width:auto;flex:1}`

Give the hero `min-height:auto`.

Put the mobile order in the DOM: hero → week strip (horizontal scroll, see F2) → desk → review → library.

## F8-count-and-filter-inconsistency (low)

The nav shows "My work 3" (index.html:5), but the section header says "On your desk 02" (index.html:12), and pass-1-1440.png shows both values.

The All/LR/RC filter (app.js:45) hides rows but never updates `.count-badge`, so filtering to LR still says "02" while one row is visible.

A three-option segmented filter for two items adds controls without adding use.

**Recommended fix**

Derive both counts from one source. Count the hero, which is also assigned work, consistently as 3 in both places, or say 2 in both.

In the filter handler, set `$('.count-badge').textContent=String($$('[data-assignment]:not([hidden])').length).padStart(2,'0')`.

Alternatively, remove the segmented filter until there are at least 5 items.

## F9-sculpture-entrance-cost (low)

This is a source-only review; motion was not observed.

`animate()` runs a 1150ms rotation entrance (sculpture.js:126). The product and animate references allow no page-load choreography and cap feedback at 500ms.

Each frame:
- rebuilds and sorts about 23,040 quads (rings=320 × sides=72, :12-13, :92-100)
- fills and strokes each quad (:111-118)
- through a CSS `filter:blur(0.55px)` on the canvas (:9)

On mid-range phones this likely competes with the first tap on "Continue at prompt 6". Reduced motion is correctly respected (:19, :129, :151).

**Recommended fix**

Paint only the settled pose. Delete the entrance, or cap it at 450ms and render at about 120×28 resolution while it animates, painting full resolution once on settle.

Better: pre-render the knot once to an offscreen canvas or a static WebP at 2x, and drop the per-frame blur filter. The facet-smoothing work already planned could use per-vertex Gouraud-style gradients or a pre-rendered image instead of the blur.

## Coverage

Images opened with Read (all 4 requested): C:/Users/Joshu/Downloads/LSAT-U-Dashboard-New-Directions/05-studio/artifacts/pass-1-1440.png, pass-1-hero-1440.png, pass-1-hero-390.png, pass-1-library-390.png
Source read in full: index.html, style.css (all media queries 1550/1430/1120/900/680/370, hover and reduced-motion blocks), app.js (all actions, state, week/chart/filter/reference-form logic), sculpture.js (mesh, painter sort, entrance animation, observers)
Reference lenses read and applied: design-critique SKILL.md (first impression, usability, hierarchy, consistency, accessibility), impeccable product.md (one primary CTA, no display fonts in data, motion that conveys state), color-and-contrast.md (accent rarity, 3:1 for graphical objects, semantic palette), typeset.md (16px body minimum, rem scale, tabular-nums), animate.md (durations, no load choreography, reduced motion)
Traced shared state beyond the brief's list: updateProgress/updateShelf/updatePrep writers, the day/agenda selection flow, filter vs count badge, and the runtime replacement of the shelf h3 text (the source says 'Keep these close' and the screenshot shows 'Try a sample question', which matches updateShelf at app.js:29)
Compared the brief's description with the screenshots and source: the color and serif description does not match; the source colors match the screenshots

## Limits

No browser execution. Hover, focus, dialog, keyboard and motion behavior were not observed live. All motion and performance findings come from reading the source.
Contrast ratios are hand estimates from hex/OKLCH values (dot about 1.8:1, unselected bars about 1.3:1), not measured with a checker tool.
Only the 1440 and 390 widths were captured. The 900px and 1120px breakpoints, the 370px rules and the dialogs were reviewed from CSS only.
The source may have changed since the pass-1 screenshots. Visual findings are tied to the screenshots; no source-versus-image mismatch was found beyond the runtime shelf heading text.
The known issues (mobile sculpture overlapping text, faceted surfaces) are acknowledged but deliberately not counted as findings.
The full 1440 screenshot was downscaled for display (1440x2014 shown at 1430x2000), so pixel positions are approximate.
