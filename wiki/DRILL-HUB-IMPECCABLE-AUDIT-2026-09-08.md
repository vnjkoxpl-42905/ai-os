# Drill hub: impeccable audit and critique (2026-09-08)

Target: `/classroom/drill` on production (lsatprep.study), signed in as Joshua. LR section, default stage, the Build a Set launcher stage, desktop (~740px pane) and phone (375px). Source: `src/pages/AcademyMainhub.tsx`, `src/components/mainhub/PracticeInsightStage.tsx`, `src/components/mainhub/TodayFocusPanel.tsx`, `src/components/drill/SectionToggle.tsx`, `src/components/questionfinder/QuestionJump.tsx`, `src/components/drill/QuestionPicker.tsx`, and the `.drill-observatory-*` block of `src/components/classroom/classroom.css`.

Register: product. Every number below was measured in the live DOM, not read off the token file. Related: [[COPY-CORRECTIONS]], [[teaching-voice]].

---

## Part 1: Technical audit

### Audit Health Score

| # | Dimension | Score | Key finding |
|---|---|---|---|
| 1 | Accessibility | 1 | Question-jump labels render at 1.07:1; hero CTA has no focus ring; most micro-labels sit below 4.5:1 |
| 2 | Performance | 3 | Four backdrop-filter surfaces and one height transition; images are lean (37 KB + 13 KB WebP) |
| 3 | Responsive | 2 | Today rails overflow 57px past a 375px viewport; fixed menu button covers content under 1024px |
| 4 | Theming | 2 | Tokens exist but JSX carries literal rgba/hex; the hub ignores the theme toggle; 206 `!important` in the file |
| 5 | Anti-patterns | 2 | Glass on four surfaces, 60px shadows, three type families, a rotating metric carousel |
| **Total** | | **10/20** | **Acceptable, significant work needed** |

### Anti-patterns verdict

Partial pass. Nobody would say "AI made this" at first glance: the horizon photo is real, the copy says what each button does, and the switch is a switch rather than tabs. But the recipe underneath is the 2025 "premium dark dashboard" lane: serif display over a space photo, uppercase mono micro-labels tracked at 0.18em, glass panels with hairline rings, a pill CTA, and an auto-rotating insight carousel with dots. Four surfaces use `backdrop-filter` (console, Today primary, Today rails, Today quiet). Card shadows run to `0 24px 60px`. DESIGN.md names all three of those as defects in the Workroom and reserves the serif for the Hall. Either this hub is a sanctioned scoped world and needs its own surface brief under `.impeccable/surfaces/`, or it is a seam leak. Today it is undocumented, which makes it the latter by default.

### Executive summary

- Score 10/20.
- Issues: P0 1, P1 7, P2 7, P3 4.
- Top five:
  1. The Test / Section / Question row is inked ivory on the cream stage. Labels measure 1.07:1. It is invisible.
  2. The fixed "Open classroom menu" button sits over page content on every viewport under 1024px, covering the launcher title and the "Practice tools" label.
  3. The primary CTA (Start Smart Drill) shows no focus indicator when focused.
  4. On a phone, the Today rails render 432px wide inside a 375px viewport and truncate assignment titles.
  5. The observatory ink ladder puts every label at or below `ink-48` under 4.5:1 on the card black. That is most of the page's labels.

### Detailed findings

**[P0] Question-jump row is invisible on the stage**
- Location: `src/pages/AcademyMainhub.tsx:400` passes `tone="dark"` to `QuestionJump`; `questionJump.css:23` sets `--qj-ink: #f5f1ec` for that tone.
- Category: Accessibility, Theming.
- Impact: "Test", "Section", "Question" and the select placeholders render at 1.07:1 on `#fbf8f3`. A student cannot see the fastest route to a specific question. The CSS comment on `.drill-observatory-section-toggle` already diagnoses this exact bug for the switch and fixes it there only.
- WCAG: 1.4.3 Contrast (Minimum).
- Fix: pass `tone="light"` for QuestionJump (and check QuestionFinder's trigger, which happens to look right only because its trigger is a dark pill). Verify in browser.
- Command: `$impeccable harden`

**[P1] Fixed menu trigger overlaps content below 1024px**
- Location: `classroom.css:2295` (`.classroom-mobile-trigger`, `position: fixed; top: 16px; left: 16px; z-index: 70`). The drill stage has no top offset to clear it.
- Impact: covers the "Set up an LR drill" launcher title, the "Practice tools" label, and the first select of the jump row. The button is also 38x38, under the 44px floor.
- WCAG: 2.4.7 area, 2.5.8 target size.
- Fix: reserve a 56px top inset on the drill stage under 1024px, or move the trigger into the tools row as a flow item. Size it 44x44.
- Command: `$impeccable adapt`

**[P1] Primary CTA has no focus indicator**
- Location: `.drill-observatory-cta` in classroom.css sets `border: 0 !important` and only a shadow; measured `outline: none` while focused.
- Impact: keyboard users lose the page's most important control.
- WCAG: 2.4.7 Focus Visible.
- Fix: add `:focus-visible { outline: 2px solid var(--observatory-ink); outline-offset: 3px }`. Same check for `.drill-observatory-console-start`.
- Command: `$impeccable harden`

**[P1] Phone: Today rails overflow the viewport**
- Location: `TodayFocusPanel.tsx:585` rail rows; the rail's fixed label span and `truncate` children compute to 432px right edge in a 375px viewport. `.drill-observatory-today-inner` clips it with `overflow: hidden`, so titles are cut ("New assignment: Necessary Assumption - First To").
- Impact: the most important computed next step is unreadable on the device students check between classes.
- Fix: give the rail `min-width: 0` on every flex child and let the trailing label wrap or drop under 400px.
- Command: `$impeccable adapt`

**[P1] Micro-label contrast across the hub**
- Location: `--observatory-ink-38/42/45/48` (classroom.css:874-877) used by "Practice tools", "Insight preview", "Top priority", slide details, tile descriptions.
- Impact: measured 3.22:1 to 4.2:1 at 10 to 12.5px. Below AA for normal text. PRODUCT.md calls AA a defect gate.
- WCAG: 1.4.3.
- Fix: floor the ladder at `ink-55` (4.9:1) for any text; keep the lower steps for decoration only.
- Command: `$impeccable colorize` (contrast pass), then `$impeccable polish`

**[P1] Inactive switch option and jump selects fail contrast and size**
- Location: `.drill-observatory-section-toggle-option` `#a7a29f` on `#fbf8f3` = 2.38:1; option box 49x25px. Jump selects 94x39px.
- Fix: darken inactive to `#6b6663` or above; pad options to 44px tall; selects to 44px.
- Command: `$impeccable harden`

**[P1] Em-dash in student-facing placeholder**
- Location: `QuestionPicker.tsx:897` placeholder "Add exact questions — PT101.S2.Q1, PT101.S2.Q6".
- Impact: PRODUCT.md brand commitment, binding on utility copy.
- Fix: "Add exact questions, e.g. PT101.S2.Q1, PT101.S2.Q6".
- Command: `$impeccable clarify`

**[P1] Small targets throughout**
- Location: carousel dots 6x6 (24px hit area via pseudo-element), pause 24x24, Analytics/Journal pills 37px tall, "Find a question" 42px, "Build targeted set" 42px.
- Fix: 44px minimum by height, per DESIGN.md button rule.
- Command: `$impeccable harden`

**[P2] No h1, and headings out of order**
- Page outline: h2 "Welcome back", h3 "Build the drill you need.", h2 (assignment title inside Today). "Practice tools", "Today", "Insight preview" are paragraphs.
- Fix: h1 for the greeting, h2 for each bay's label, h3 for items.
- Command: `$impeccable harden`

**[P2] Glass and shadow against the design record**
- `backdrop-filter: blur()` on four classes, `0 24px 60px` shadows on hero, cards and Today. DESIGN.md: no shadows, no glass in the Workroom.
- Fix: decide the hub's status (see critique) and either write its surface brief or flatten.
- Command: `$impeccable document` (brief) or `$impeccable quieter`

**[P2] Height transition on the RC flip**
- `classroom.css:1486` `.drill-observatory-flip { transition: height }`. Layout property.
- Fix: animate `transform`/`opacity` and let height snap, or use `grid-template-rows` interpolation.
- Command: `$impeccable animate`

**[P2] Literal colours in JSX**
- `PracticeInsightStage.tsx` carousel dots and pause hover use `bg-[rgba(244,241,234,…)]`; `TodayFocusPanel.tsx` focus rings and skeletons likewise; `AcademyMainhub.tsx:146` `text-[#f4f1ea]`; `SectionToggle` colours in CSS as hex. DESIGN.md's Named Ground Rule.
- Command: `$impeccable extract`

**[P2] Hub ignores the theme toggle**
- The dark cards and cream stage are hard-coded; the app's dark alternate leaves the stage cream. Acceptable only if this is a scoped world with its own brief.
- Command: `$impeccable document`

**[P2] Two hero texts compete on the phone**
- Under 900px the hero stacks greeting, then console, so the two CTAs sit 220px apart with the same weight. The console's paragraph wraps to five lines on 375px.
- Command: `$impeccable adapt`

**[P3] Date without year** while Classroom Home prints "TUESDAY · SEPTEMBER 8 · 2026". One format across both mounts.
**[P3] "Pick a test" under Section and Question** is intentional (it points at the missing step) but reads as a copy error. "Choose a test first" would say why.
**[P3] 5.5 MB question bank** loads before the LR launcher draws. Already documented in code; a skeleton of the filter frame would hide the wait.
**[P3] 46 off-ramp font sizes** flagged by the detector (11.5, 12.5, 13.5, 15px). Harmless individually; they mean the observatory has its own type ramp that DESIGN.md does not know about.

### Patterns and systemic issues

- **The hub is a second design system.** Its own ink ladder, radius scale, spacing scale, type ramp, two extra families (Fraunces, JetBrains Mono), glass, shadows. None of it is in DESIGN.md or a surface brief. Every finding under Theming and Anti-patterns is a symptom of that.
- **Tone props are set per component by hand.** The switch got fixed for the cream stage, the jump row did not. One `data-tone` on the tools row would have prevented it.
- **Contrast decided by alpha, not measured.** A twelve-step alpha ladder invites picking by feel. Half the steps fail on the surface they were made for.
- **`!important` as the layering strategy.** 206 in the file. The observatory overrides shadcn's Card and Button by force, which is why the shared focus ring never reaches the CTA.

### Positive findings

- The URL carries section and stage, so refresh, Back and shared links all land correctly. The replace-once trick for the bare URL is exactly right.
- Copy is honest and specific: "Start One Passage" vs "Start Smart Drill" because the two do different things; the greeting paragraph says what the buttons do rather than "Pick up where you left off".
- The carousel has a real pause control with `aria-pressed`, and rotation stops on RC where the data would lie. WCAG 2.2.2 is met.
- Empty states are truthful: "No streak yet. Answer a few questions today to start one."
- The section switch is keyboard-correct (one tab stop, arrows move and activate, reduced motion honoured).
- Images are WebP with a PNG fallback via `image-set`; hero 37 KB, eclipse 13 KB.
- Reduced-motion block exists and stops the hover lifts.

---

## Part 2: Design critique

Assessment A was a design read of source plus the live page. Assessment B was the impeccable detector: 103 findings over the seven files, 84 advisory (off-ramp sizes, radii, colours), and warnings for one 4px side-stripe (`classroom.css:2223`, outside the drill hub), nine "overused font" hits (seven Roboto Mono outside the hub, two Fraunces on Classroom Home), and two layout transitions (one is the hub's flip). The detector caught nothing the read missed inside the hub; its warnings mostly belong to other rooms in the same stylesheet. No browser overlay run: the `[Human]` overlay needs the live server injected into a page the pane can fully render, and the pane was hidden, so I read the DOM instead.

### Design Health Score

| # | Heuristic | Score | Key issue |
|---|---|---|---|
| 1 | Visibility of system status | 3 | Today is live and `aria-live`; the launcher's error state is a bare string |
| 2 | Match system / real world | 3 | LSAT vocabulary is right; "Smart Drill" is the one label that does not say what it does |
| 3 | User control and freedom | 3 | Cancel, deterministic Back, pause; the LR/RC flip silently discards a half-built set (by decision) |
| 4 | Consistency and standards | 1 | Jump row wrong tone; date format differs from Home; three families against a one-face rule |
| 5 | Error prevention | 3 | Address syntax has a hint and live count; "Pick a test" placeholder ambiguous |
| 6 | Recognition rather than recall | 3 | Labels on everything; the carousel hides four of five insights at any moment |
| 7 | Flexibility and efficiency | 3 | Cmd-K, arrow keys on the switch, typed addresses |
| 8 | Aesthetic and minimalist design | 2 | Three doors to the same builder; hero stays above the open launcher |
| 9 | Error recovery | 2 | Launcher error is one sentence with no retry |
| 10 | Help and documentation | 2 | "Faster than clicking" is good; nothing explains what Smart Drill will do to you |
| **Total** | | **25/40** | Needs work |

### Overall impression

It is handsome and it is honest, and those are the two hard things. What it is not yet is decisive. PRODUCT.md's second principle says compute the next step, do not present a grid. This page presents, on one screen: a jump row, a search, a section switch, an adaptive CTA, a builder CTA, a builder tile, Analytics, Journal, an insight carousel with its own CTA, and then, last, the thing Joshua actually assigned. The computed next step is at the bottom right on desktop and fourth screen on a phone. The single biggest opportunity is inversion: lead with Today's "Next up", let the hero's two CTAs be the fallback for a student with nothing assigned.

### What's working

- **The switch.** One lit slot travelling between LR and RC, both labels visible, arrows work it. It reads as a physical control and the code says why.
- **Copy that admits what it does.** "Read one passage now, untimed, with the answers after it." No pitch, no metaphor, no coach voice invented to fill a gap.
- **URL as the source of truth.** Section, stage, and the RC smart-start parameters all live in the address bar. That is why the page survives refresh and sharing.

### Priority issues

**[P0] The next step is buried.**
- Why: a paying client logs in to do what Joshua assigned. Today's "Next up" sits below two hero CTAs, a tools card and a carousel. On a phone it is the fourth screen.
- Fix: promote Today's primary item into the hero when one exists ("Next up: Conditional Logic cheat sheet. Assigned by Joshua. Start"). Demote Smart Drill and Build to the bay. With nothing assigned, today's hero is the fallback.
- Command: `$impeccable shape`, then `$impeccable layout`

**[P1] Three doors to one builder.**
- Why: "Set up an LR drill" (hero console), "Build a Set" (practice tile) and "Build targeted set" (carousel action) all open the same stage. Three names for one thing teaches the student that names do not matter.
- Fix: one door, one name. Keep the hero console. Turn the practice tile into something the console is not (recent sets, or saved sets).
- Command: `$impeccable distill`

**[P1] The hero does not get out of the way.**
- Why: opening the launcher keeps the full 400px hero above it, so the student scrolls past "Set up an LR drill" (button) to reach "Set up an LR drill" (title). Same words, twice, 500px apart.
- Fix: collapse the hero to a one-line band while a stage is open, with the greeting and a Cancel.
- Command: `$impeccable layout`

**[P1] The hub's identity is undocumented.**
- Why: DESIGN.md sanctions rooms behind a wrapper class with their own brief. This room has the wrapper (`.drill-observatory-root`) and no brief, so every reviewer, and every future agent, will judge it against the Workroom's rules and fail it.
- Fix: write `.impeccable/surfaces/drill-hub.md` stating the ground (cream stage, black cards), the families (Fraunces display, JetBrains labels, Outfit body), what glass is allowed to do, and the contrast floor. Then fix the code to match the brief, not the other way round.
- Command: `$impeccable document`

**[P2] "Smart Drill" is the one label that does not say what it does.**
- Why: everything else on the page is literal. "Smart" asks the student to trust an adjective. The paragraph above it explains it; the button does not.
- Fix: "Start adaptive set" or "Drill my weakest types".
- Command: `$impeccable clarify`

### Cognitive load

Checklist failures: 4 of 8 (visible options at the first decision point 9, three routes to one action, primary action not distinguishable by weight alone on phone, progressive disclosure inverted since the launcher opens below a still-open hero). Critical band.

### Emotional journey

The photo and the serif greeting land a calm, slightly ceremonial arrival. That is intentional and it works. The valley is the next 200px: nine controls and no verdict on what to do. Peak-end: the page ends on Today, which is the best moment on it, and the one most students will not reach.

### Persona red flags

**Celia (paying client, assigned work waiting).** Logs in to start what Joshua sent. Sees two CTAs about drills she was not assigned. Scrolls, finds "Next up" in the bottom-right card. On her phone, the assignment title is clipped mid-word. She was messaging Joshua about a pending drill status yesterday; nothing here tells her that either.

**Alex (self-study power user).** Cmd-K works, typed addresses work, the switch has arrow keys. But Tab from the switch lands on Start Smart Drill with no visible ring, and the jump row's labels are invisible, so the keyboard-only path to a specific question is a guess.

**Jordan (first session, phone).** Menu button covers the first thing on the page. "Smart Drill" and "Build the drill you need" both look like the assignment. Five-line console paragraph before the button. Today is four swipes down.

### Minor observations

- "TUESDAY, SEPTEMBER 8" here vs "TUESDAY · SEPTEMBER 8 · 2026" one click away on Home.
- "Insight preview" for a new account is five near-empty slides on a seven-second timer. Consider hiding the carousel until there is a second real insight.
- The launcher's loading state is a spinner; the filter frame could draw immediately.
- Analytics and Journal are pills inside "Practice tools" though neither is a tool for practising; they are records.

### Questions to consider

- What if the hero were Today, and Smart Drill only appeared when nothing is assigned?
- Does a student need to see LR/RC, jump, search and build before seeing what Joshua assigned?
- If this room is allowed to be dark, glass and serif, where is that written, and what does the room owe the rest of the academy in return?
- What would the page look like if it had one button?

---

## Recommended actions

1. **[P0] `$impeccable harden`**: fix the jump row tone (`tone="light"`), the CTA focus ring, the em-dash placeholder, and the 44px floor on switch options, selects, pills, dots and pause.
2. **[P0] `$impeccable shape`**: decide whether Today's next step leads the hero. This is the product-principle call and needs Joshua's brief before layout work.
3. **[P1] `$impeccable adapt`**: clear the fixed menu trigger under 1024px, fix the Today rail overflow at 375px, tighten the stacked hero on phones.
4. **[P1] `$impeccable document`**: write the drill hub surface brief so the dark room is sanctioned, with its contrast floor and its allowed glass.
5. **[P1] `$impeccable colorize`**: rebuild the ink ladder against measured contrast; nothing that carries text below 4.5:1.
6. **[P1] `$impeccable distill`**: one door to the builder; collapse the hero while a stage is open.
7. **[P2] `$impeccable clarify`**: "Smart Drill" label, "Pick a test" placeholders, year in the date.
8. **[P2] `$impeccable extract`**: move the literal rgba and hex values in JSX and SectionToggle into the observatory tokens.
9. **[P2] `$impeccable animate`**: replace the flip's height transition.
10. **`$impeccable polish`**: final pass.

Re-run `$impeccable audit` and `$impeccable critique` after fixes.
