# Drill hub, run 3

Written 2026-09-09 by Claude (Opus 5), executing [[DRILL-HUB-PERFECT-SCORE-PLAN-2026-09-08]] from Part 1g. Run 2 is [[DRILL-HUB-IMPECCABLE-AUDIT-2026-09-08-RUN2]]: audit 16/20, critique 31/40.

Every number below comes from a script, a command, or a measurement on production. Where something could not be measured, it says so instead of guessing.

## 1. Commits

| Hash | What |
|---|---|
| `ce2ddb7` | WP-A + WP-B. Today loses the photograph and all glass; hero image preloaded at `fetchpriority=high`. |
| `13bb1dd` | WP-C + WP-D. Menu button moves into a sticky bar; the dateline prints twice and CSS picks one. |
| `a82333a` | WP-C correction. The classroom stacks below 1024 so the bar stops squeezing the room. |
| `3eb6803` | WP-E. 188 `!important` removed; the observatory wins by specificity. |
| `5fd1074` | Motion. Ease-out curve, jump-row hover, three transition lists corrected. |
| `afb15a3` | WP-G. Three hero contrast failures fixed; shadows quieted; label cull. |
| `6109c2f` | WP-H + WP-I + WP-L. Copy pass, Escape leaves a stage, `/` opens search. |
| `daa41d8` | WP-J + WP-K + WP-M + WP-N. Icons normalised, failed hero made truthful, one explainer. |
| `7c6306d` | Cycle 6. The hero's ivory rule scoped to the greeting column instead of four named lines. |
| `2e312e4` | The two rules cycle 6 taught, written into the surface brief. |

`70056d3` is not mine. A concurrent session's broad `git add` swept my uncommitted motion edits into it, so that commit carries motion work its message does not mention. Recorded here because the commit log alone would mislead.

## 2. Baseline (Part 1g)

Production build `f791016`, measured at 375 and 1280 before any change.

- Contrast fails: **0** reported (see §6 for why that number was wrong)
- Targets under 44px: **0** of 16
- Headings: `h1 / h2 / h2 / h2`, no skips
- Em-dashes: **0**
- `docWidth` equals viewport at both widths; nothing past the right edge
- `!important` in `classroom.css`: **200**
- `backdrop-filter`: **8** declarations across 4 surfaces

## 3. Cycle 1 — WP-A, WP-B (`ce2ddb7`, published)

Today renders `rgb(8,8,11)` with `background-image: none`. Exactly one glass element remains (`.drill-observatory-console`, `blur(12px)`). `/mainhub/hub-horizon.webp` is present in `link[rel=preload]`. `!important` 200 → 192. `backdrop-filter` 8 → 2 declarations.

WP-B steps 1–4 were already satisfied and were verified rather than assumed: the hero webp is 37 KB behind `image-set`, fonts already load `display=swap` behind `preconnect`, and no transition in the block animates a layout property. The real fix was the preload: a signed-in mobile trace showed the LCP element is `.drill-observatory-hero`, its background image queued at 5,260 ms of a 6,542 ms LCP while downloading in only 550 ms.

**LCP after the preload was never measured.** The 6,542 ms figure is the pre-fix baseline only. The chrome-devtools browser wipes its profile on restart and lands signed out; the in-app browser returns no `largest-contentful-paint` entries at all. Performance therefore stays at 3 in §8.

**There is no Lighthouse composite for this hub.** The CLI follows the redirect to `/auth` (perf 39, but that page's bytes are two videos totalling 5.9 MB, not the hub). The `lighthouse_audit` MCP tool excludes performance by design. Quoting 39 would be quoting the sign-in page.

## 4. Cycle 2 — WP-C, WP-D (`13bb1dd` + `a82333a`, published)

`13bb1dd` shipped a regression that every scan passed.

WP-C put the menu button in a sticky bar, but added it as a third child of `.classroom-root`, which is `display: flex` with `align-items: flex-start` — a **row**. Below the sidebar breakpoint the bar took a column of its own instead of a band across the top:

| Surface at 375 | Stage before | Stage after `a82333a` |
|---|---|---|
| Drill hub | `x:104 w:271` (content 239px) | `x:0 w:375` (content 343px) |
| Home | `x:116 w:259` | `x:0 w:375` |
| Schedule | `x:133 w:242` (calendar column 206px) | `x:0 w:375` (339px) |
| Workspace | `x:194 w:181` | `x:0 w:375` |
| Messages | bar 137px wide | bar 375px, stage 756 = 812 − 56 |

Contrast, target-size, overflow and heading scans all passed while this was live, because nothing *overflowed*: the room was squeezed, not broken. Only the screenshot sweep WP-C step 4 asks for caught it. Messages exposed a second-order bug in the first fix: in a column the bar is `flex: 0 1 auto` and a full-height sibling shrank it to 52px, so it needs `flex: none`.

All five sections re-verified clean on the published build at 375.

WP-D's stated goal was not met by `13bb1dd` either. At 1024 the *short* dateline still wrapped: the greeting column is 201px and the line measured 197px of glyphs plus 47px of tracking, so "2026" fell to a second line. Tightening tracking on the span holds it to one line at 185px, verified at 900, 1024 and 1099.

## 5. Cycle 3 — WP-E and motion (`3eb6803`, `5fd1074`, published)

`scripts/observatory-specificity.mjs` rewrites the block with a real CSS parser and is idempotent; `--check` fails if the block drifts. Output: 145 rules visited, 159 selectors scoped, **188 `!important` removed**, 4 kept.

`!important` in `classroom.css`: **200 → 4**. The four that remain are the `prefers-reduced-motion` block, where the override has to beat a later, equally specific animation rule and specificity cannot promise that. Trading an accessibility guarantee for a round number would be the wrong deal, so the plan's "zero" is deliberately not met and the reason is recorded in the brief.

Verified in the **built bundle**, not just the source: 170 scoped selector instances, one rule containing `!important`, and that rule is the reduced-motion block.

`.drill-observatory-launcher-panel` sits outside the `/* end observatory */` marker on purpose. It lands on Radix popover and select content, which renders in a portal outside the root; scoping it would have unstyled every dropdown on the page.

### WP-E changed exactly three things, and it should have

The plan's acceptance test is "the page looks identical". Screenshots could not carry that (the pane returns a blank image for any scrolled capture), so instead a computed-style fingerprint of 200 elements × 50 properties was captured at 375 and 1280 on the published pre-WP-E build and diffed after publish.

| Change | Count | Verdict |
|---|---|---|
| `fontFamily` Outfit → JetBrains Mono on the section switch | 5 | **Fix.** The brief says chips are mono; a utility was beating the rule. |
| `color` / `borderTopColor` `rgb(18,18,18)` → ivory on the hero card and console | 11 | **Fix.** shadcn's `text-card-foreground` was winning on a near-black card. |
| `width`, `marginLeft`, `gap` 8→9px | 8 | Reflow from the font change, plus the CTA's own gap winning. |

Everything else was capture artefact: the 375 baseline was taken mid `classroom-stage-enter`, so 119 boxes sit exactly 4px low; the 1280 baseline was taken before the resize settled, an 8px ancestor difference that propagates to 55 widths. Current 1280 layout matches the authored rule exactly: sidebar 336, stage 928.8, root 888.8 = stage − 16 − 24.

Contrast, targets, headings and overflow all re-verified clean at 375 and 1280 after publish.

### Motion

Two measured defects, not decoration. Most of what the plan implies is missing already existed: the section switch is a framer-motion spring honouring `useReducedMotion`, both skeletons already pulse, and there were already 14 hover and 6 press states.

**The easing curve was the wrong family.** `--observatory-motion` used `cubic-bezier(0.4, 0, 0.2, 1)`, an ease-in-out. Measured on both curves:

| Elapsed | Old | Ease-out quart |
|---|---|---|
| 10% (16ms) | 2.6% | 34.7% |
| 25% (40ms) | 23.7% | 68.9% |

Nothing visible happened for the first ~40ms of every hover.

**The three jump-row selects had no hover state at all** — `:disabled` and `:focus-visible` existed and nothing answered a pointer, against the brief's own rule. They now strengthen a ring mixed from `--qf-ink` so it reads in both tones.

**WP-E would have broken three hovers.** The CTA, practice tile and insight action change `background` on hover while their transition lists named only `transform`. A Tailwind utility was masking it; the moment the authored rules won on specificity those hovers would have snapped. Caught by auditing every hover against its transition list before publish.

Verified on production: the CTA transition is now `background-color, filter, transform` at 160ms on the quart curve, proving both that the scoped rule beat the utility and that the background fix landed.

## 6. Cycle 4 and 5 — WP-G through WP-N (`afb15a3`, `6109c2f`, `daa41d8`, published)

**All three are live.** Confirmed on production on 2026-09-09 by reading the shipped build, not by asking: the hero scrim's middle stop computes to `rgba(4,4,6,0.58)`, all four WP-G lines compute to `rgb(244,241,234)`, `--observatory-ease` is the quart curve, and the shipped `AcademyMainhub-BNfVsuJ-.js` contains `drill-observatory-explainer`, `Try again`, `Practice your weakest types`, `Read one passage` and `the question types you miss most`. Part 1 was then re-run against that build.

### Part 1, re-run on the published build

| Check | 375 | 1280 |
|---|---|---|
| Contrast fails, as the scan reports them | 1 | 1 |
| Contrast fails, real | **0** | **0** |
| Targets under 44px | 0 of 16 | 0 of 16 |
| Focus rings missing, keyboard armed | 0 of 14 focusable | 0 of 14 focusable |
| Headings | `h1 / h2 / h2 / h2` | `h1 / h2 / h2 / h2` |
| Em-dashes | 0 | 0 |
| Width | `docWidth` 375 = viewport | `docWidth` 1265 under a 1280 viewport, scrollbar only, nothing past the edge |

The single reported contrast fail is the section switch's active label, and it is the same blind spot as the photograph wearing different clothes: `bgOf` walks *ancestors*, and the pill the active label sits on is an absolutely positioned **sibling**. Measured against what is actually behind it, the active label is ivory on `rgb(51,47,44)` at **11.79:1** and the inactive option is `rgb(107,102,98)` on the `rgb(251,248,243)` track at **5.35:1**. Both pass.

Two of the sixteen controls are the jump row's dependent selects, which are `disabled` until a PrepTest is chosen. They cannot take focus, so 14 is the real denominator for the ring check, not 16.

### The five-section sweep, on the published build

Workspace, Drill, Uploads, Account and Messages at 375: each renders a full 375px stage beneath a 56px `flex: 0 0 auto` bar, `scrollWidth` 375, nothing past the right edge, `.classroom-root` in `column`. The `13bb1dd` squeeze is gone in all five, not only on the hub.

### The scan was reporting zero contrast fails while three hero lines were failing

This is the most important finding in the run. The 1a scan reads the **scrim's declared colour**, not the photograph beneath it, exactly as the plan's own caveat warns. Sampling `hub-horizon.webp` under each hero text box and compositing photo, scrim and the text's own alpha:

| Hero element | Before | After | Needs |
|---|---|---|---|
| Quiet link | **1.89** | 4.99 | 4.5 |
| Next up facts | **2.76** | 7.75 | 4.5 |
| Dateline | **4.50** | 12.62 | 4.5 |
| Greeting h1 | 3.66 | 6.11 | 3.0 |
| Next up title | 7.48 | 11.00 | 4.5 |

The horizon crop reaches `rgb(250,240,228)` and the horizontal scrim thins to 0.35 exactly there. Two fixes together, because neither is enough alone: the ink ladder's alpha steps were measured against the flat card `#08080b` and do not survive a photograph, so hero text that carries meaning is full ivory; and the scrim's middle stop goes 0.35 → **0.58**, which is the measured floor, not a guess. It still opens the middle enough for the horizon to read.

WP-G's shadow reduction is what exposed this: the old `0 2px 24px` / `0 1px 12px` at 60% had been quietly propping up text the scrim should have been carrying.

Those five rows are one crop, not a verdict for all six widths. Re-measured on the published build at 375, the same three lines read 17.33, 9.33 and 6.87. The next subsection is what that width-dependence turned out to be hiding.

### A fourth hero line was failing, and two more had never been on screen (`7c6306d`)

WP-G measured three lines, fixed those three, and named them one CSS selector each. That is the defect. The rest of the greeting column stayed on the ink ladder, and the ladder does not survive the photograph either.

The reason it went unseen is worth stating plainly: `background: cover` at `50% 78%` changes *which part of the photograph lands under the text* as the hero narrows. The bright horizon is dragged into the greeting column at phone and tablet widths and pushed out of it on a desktop. A crop measured once does not speak for the others.

Measured by sampling `hub-horizon.webp` under each element's own box, compositing both scrim stops and the text's own alpha:

| Line | Rendered when | 375 | 390 | 768 | 1024 and up |
|---|---|---|---|---|---|
| Assigned hint, ink-60 | work is assigned | **3.24** | **2.86** | **3.98** | 6.62 |
| Failed-hero paragraph, ink-70 | the load failed | **3.14** | **3.15** | 4.52 | 5.02 |
| Empty-hero paragraph, ink-70 | nothing assigned | **3.14** | **3.15** | 4.52 | 5.02 |
| Explainer summary and body, ink-70 | nothing assigned, LR | **3.14** | **3.15** | 4.52 | 5.02 |

The hint's row is measured on its own box. The three ink-70 rows do not render in the ordinary state, so they are bounded by the worst pixel anywhere in the greeting column, which is the honest number available without faking their state. The last three all arrived in `daa41d8`, *after* the contrast pass had been signed off, which is exactly how a rule that names lines rather than places goes stale.

The fix scopes the rule to `.drill-observatory-greeting` and lists the whole ladder, not just the two steps currently used, because the failure here is a step added later rather than a step wrong today.

**Published and re-measured on the shipped build**, on the element's own box, with nothing injected and nothing perturbing the layout:

| Line | 375 | 390 | 768 |
|---|---|---|---|
| Assigned hint | 3.24 → **5.84** | 2.86 → **4.90** | 3.98 → **8.49** |

All nine selectors are present in the shipped `index-D6-FizGc.css`, and the hint computes to `rgb(244,241,234)` on production. The scan at 375 is unchanged: 38 nodes checked, the one section-switch artifact, 0 targets under 44px of 16, `h1/h2/h2/h2`, 0 em-dashes, `docWidth` 375, nothing past the edge.

This also settles a discrepancy the earlier pass left open. Measuring the fix by injecting the rule and adding a stand-in paragraph gave 5.34 / 4.99 / 6.37, because the stand-in pushed the hint a few pixels along the crop. The untouched published page gives 5.84 / 4.90 / 8.49, and **4.90 at 390 is the true worst case**, which is the figure the CSS comment already quotes. The lesson is small and worth keeping: on a surface where contrast depends on which pixels sit under a box, a probe element inserted to test it changes the answer.

The console card beside the column keeps the ladder untouched: it carries its own `rgba(6,6,9,0.55)` panel and its body text already measures **8.81:1** over the same photograph. The date spans and the Next up label no longer need naming, since ink-60 on their own paragraphs now covers them.

One consequence handled rather than left: the explainer's `summary:hover` moved to full ivory, which is what the base colour now is, so the hover had nothing left to say. It says it in the underline instead. A dead hover rule reads as a working one.

### Labels

10 rendered on the default LR stage, not the 6 the plan targets. Removed: Today's second dateline (the hero already prints the full date three lines up, in the same mono treatment), and the mono uppercase treatment on the Ready / New chips, which sit inside a button — the data was always sentence case, only the CSS shouted. That lands at **7**, not 6, because three insight slides render for this account and each carries a kicker that names it. Cutting a kicker would remove the only thing identifying its insight.

### Copy (WP-H)

Six changes, logged in `wiki/COPY-CORRECTIONS.md` under 2026-09-09 so they cannot be silently reverted.

| Was | Now |
|---|---|
| Start Smart Drill | Practice your weakest types |
| Start One Passage | Read one passage |
| Start a Smart Drill instead | Or practice your weakest types |
| Read one passage instead | Or read one passage now |
| Open analytics | See where you lose points |
| Open journal | Review your missed questions |

"Instead" was the worst of them: it tells a student she declined the assigned work simply by reading past it.

### Control, flexibility, help

Escape leaves an open stage, deliberately narrow: never on the plain hub, never while something modal is open, never out of a field with content in it. Three tests, including the modal guard. `/` opens the search alongside Cmd/Ctrl+K, opening only, since `/` with the panel open is a character someone is typing. Both declared in `aria-keyshortcuts` and a `title`, no visible badge.

One explainer, a `<details>` for the student with nothing assigned. **It quotes no set size.** The plan expected ten; adaptive mode passes `questionBank.getAllQuestions()` and serves one at a time, so there is no fixed count, and the plan's own instruction is to leave it out rather than invent one.

### Error recovery (WP-M)

A real truthfulness defect: `primary` is null on error as well as on empty, so a student whose assignments failed to load was told, silently, that she had none. The hero now names the failure before offering her own practice; Today does the same for its queue. Both carry Try again, which reloads — Today is assembled from seven sources and only two are react-query backed, so invalidating queries would retry two of seven while looking like it had retried all of them.

## 6a. Cycle 7 — WP-F (`7439a1b`, `55f93bd`, PR #103 merged as `e07a1aa`, PUBLISHED 2026-09-09)

What dark theme looked like on production before the fix, measured 2026-09-09 in Chrome, signed in, `html.className === "dark"`: stage `rgb(18,16,25)`, sidebar and cards dark, and two cream slabs on the black stage — the jump row and the LR/RC switch, both `rgb(251,248,243)`. The jump row was hard-coded `tone="light"` (a fix for the earlier 1.07:1 ivory-on-cream fail, written when the stage was documented as always cream); the switch read `--observatory-stage-*`, declared once with light values.

The change:

- `classroom.css`: `html.dark .classroom-root.classroom-root-drill` declares a dark stage set: well `rgba(255,255,255,0.03)` (computes to `#191720` over `#121019`), ink `#f5f1ec`, muted `#9a938c`, hair `rgba(255,255,255,0.1)`, lit `#121019`. Values are the jump row's dark tone so the strip stays one system. Scoped to the classroom stage; `/rc` renders outside `ClassroomLayout` and never sees `html.dark`.
- `questionJump.css`: dark-tone muted `#8b837b` → `#9a938c`. It measured 4.75:1 on the hub's dark well; now 5.85:1. The light tone's muted is 5.3:1 on cream, so the two themes sit in the same band.
- `AcademyMainhub.tsx`: `tone={theme === "dark" ? "dark" : "light"}` from `useTheme`, comment rewritten. Cards untouched at `#08080b`.

Computed contrast: ink 15.76:1 and muted 5.85:1 on the well; active label `#121019` on the ivory pill 16.77:1.

Verification: typecheck clean, 89 hub tests green in 6 files, `observatory-specificity.mjs --check` OK, `!important` still 4. Rendered by injecting the identical rule and attribute on production in dark theme: desktop 1536 in Chrome, 375 in the in-app pane (`scrollWidth` 375, switch and row both `rgba(255,255,255,0.03)`, active label `rgb(18,16,25)`, inactive `rgb(154,147,140)`). Not rendered on the real build: a local dev server on a fresh origin has no session and I do not sign in. One quirk worth knowing: after an injected stylesheet changes a custom property, the switch's `transition: color 200ms` left `getComputedStyle` reporting the old colour until a forced reflow. A real theme toggle changes the `html` class, which does not have that problem, but read colours after the transition and a reflow, not before.

Measured on the shipped build (`index-J1_oHAIU.css`, Chrome, signed in, 2026-09-09, no injection): in dark, `html.className` is `dark`, stage `rgb(18,16,25)`, jump row `data-tone="dark"`, switch and row both `rgba(255,255,255,0.03)`, field labels and the inactive switch label `rgb(154,147,140)`, the active label `rgb(18,16,25)`. The live toggle: clicking Light in the account menu flipped `html` to `light`, the stage to `rgb(253,248,243)`, the row's tone to light and the switch back to cream in one step. Five-section sweep in dark: Home, Testing Centre and Messages render on their dark grounds as before; Teacher Workspace stays light gray, which `index.css` documents as theme-independent on purpose. Nothing owed.

## 6b. Post-preload LCP, measured (2026-09-09, shipped build, chrome-devtools, signed in)

Desktop, no CPU or network throttling, cold reload of `/classroom/drill?section=lr`. Raw trace kept in the session scratchpad only.

| | Baseline (pre-fix) | Now |
|---|---|---|
| LCP | 6,542 ms | **3,540 ms** |
| CLS | | 0.01 |

LCP element is the hero (`.drill-observatory-hero`), painting `hub-horizon.webp`. Breakdown: TTFB 526 ms, load delay 46 ms, load duration 66 ms, **render delay 2,902 ms (82%)**. The preload did exactly what it was for: the image is downloaded 638 ms after navigation and then waits 2.9 s for something to paint it. That something is the app boot, not the image:

1. The main bundle `index-Wf-qJ8UO.js` finishes at ~800 ms, the hub chunk `AcademyMainhub-Dh8etODA.js` at ~1,540 ms.
2. Before the hero can mount, the classroom waits on the auth and profile chain: `students`, `profiles` (four separate selects on the same row), `user_roles`, `bootcamp_kv`, each ~1.2 to 2.2 s from navigation.
3. In parallel, and competing for the same connection: `_bank.generated.json` (1.4 MB, the finding Joshua dismissed twice), 21 `PT1xx-explanations.json` files, `finder-address-index.json`, and the Messages queries, which run the full conversation fetch (`get_conversations_with_attachments`, `get_latest_messages`, participants) twice each, out to 4.5 s.
4. Fonts: the Google stylesheet at 637 ms, Fraunces and JetBrains Mono woff2 not requested until ~2.5 s and landing at ~3.4 s, which is where the hero's serif greeting gets its face.

Also flagged by the trace: an unused `preconnect` to `prod.spline.design`; 37.6 kB of assets with short cache lifetimes; no field data in CrUX.

What would move it, in order of size, none done this session: stop fetching Messages on a page that only shows an unread count; lazy-load the bank and the explanations (they are not on the hub's critical path); collapse the four `profiles` selects into one; preload the two hero font files. Each is a piece of work outside the hub's CSS and is recorded here as a finding.

*2026-09-09, later:* item 1 done on branch `perf-hub-messages-count`. Two causes, both fixed. (a) `TodayFocusPanel` called `useTodayFocus` unconditionally and discarded the result whenever the hub passed `focus` in, so every Today feed ran twice on the hub; the panel is now two components, one that owns the hook and one that only renders. (b) The feed read Messages through `useInbox`, the full six-query inbox with an attachment scan and unfiltered realtime. It now reads `useInstructorMessages`, a react-query hook that asks two questions: participants + `get_latest_messages`, then `get_conversation_participant_names` and a subject read only when something is unread. No migration. Measured on the dev build, signed in, hub remount: Messages is now `conversation_participants`, `get_latest_messages`, `get_conversation_participant_names` and nothing else; `conversations` and `get_conversations_with_attachments` no longer appear. **Still duplicated after this fix:** `notifications`, `homework_assignments`, `ta_assignments`, `students`, `profiles(display_name)`, because `ClassroomLayout` (the rail) mounts the same `useState`-based hooks the Today feed does and none of them share a cache. Converting `useNotifications` and `useStudentAssignments` to react-query with stable keys is the next boot-time item and is its own branch.

*Deployed and checked on production, 2026-09-09 ~18:40.* PR #110 merged to main as `8335e18`; the shipped hub chunk `AcademyMainhub-ZthLdZSe.js` carries the new query key. Cold reload of `/classroom/drill?section=lr` in the in-app pane, signed in, resource buffer intact (95 entries): 26 Supabase requests, the last one finishing at **2.0 s** after navigation, against 4.5 s in the §6b trace. Messages is now five small reads in total: the rail badge's `conversation_participants` + `messages` count pair, and Today's `conversation_participants` + `get_latest_messages` + `get_conversation_participant_names`. `conversations?select=*`, the all-participants read and `get_conversations_with_attachments` are gone. Not remeasured: LCP (the hidden pane returns no paint entries; a chrome-devtools trace is the way to get the number). Also visible in the same log and untouched: `students?select=class_id` five times, `profiles` six times across four column sets, `notifications` twice. Those are the auth chain and the rail/Today duplication, the next items.

*Rail/Today duplication fixed, 2026-09-11, PR #119, merged to main as `2d734ec`, not yet deployed.* `useNotifications`, `useStudentAssignments` and `useStudentTAAssignments` moved from per-mount `useState` to react-query under stable keys (`notifications` / `student-assignments` / `student-ta-assignments` + userId, staleTime 30 s). Two mounts now share one read; the optimistic flips in `useNotifications` write to the shared cache, so the bell and the Today item cannot disagree. Return shapes unchanged, no call site touched, no migration. Proof so far is tests only: `src/hooks/useSharedRailQueries.test.tsx` (two mounts → one read per table, cross-mount `markRead`, `refresh` re-reads once) plus the 23-file / 177-test sweep of every suite touching the hooks, all green. Not yet seen in a browser: the perf worktree dev server has no student session. After deploy, the production resource log should show `notifications`, `homework_assignments` and `ta_assignments` once each; the auth-chain duplicates (`students?select=class_id` ×5, `profiles` ×6) remain the last boot-time item.

*Deployed and checked on production, 2026-09-11 ~02:40.* The `student-assignments` / `student-ta-assignments` keys ship in the main bundle `index-CwOjSjGD.js` (the hooks are imported by `ClassroomLayout`, not the hub chunk `AcademyMainhub-XNNhG3Im.js`); confirmed by fetching every loaded script. Signed-in load of `/classroom/drill?section=lr` in the in-app pane, resource buffer intact (91 entries): 25 Supabase requests, `notifications`, `homework_assignments` and `ta_assignments` **once each** (were twice). First load after the deploy ended at 6.8 s because every data request started at 5.5 s behind the cold download of the new chunks; a warm reload ended at **1.7 s** (2.0 s after #110, 4.5 s in the original trace). Still duplicated and untouched: `profiles` ×6, `students` ×4 in the auth chain. Seen in passing on the dev build: Classroom Home still runs the full inbox (`conversations` ×2, `get_conversations_with_attachments` ×2) for its Messages panel; the #110 fix would apply there too.

## 7. Where the plan was wrong

Six places. Each was verified before being set aside.

1. **WP-F's premise is false, and so was this entry's.** *Correction 2026-09-09:* `ClassroomLayout.tsx` has toggled `html.dark` from the theme since `0e3dcad` (2026-09-05), so the classroom's dark palette is live and the "22 dead rules" claim below is wrong. The simulation described here removed `.light` by hand, which is not what the app does; the app adds `.dark`. The real defect was smaller: the drill stage already went near-black in dark, and only the two stage controls (jump row, section switch) stayed cream on it. Fixed on branch `wp-f-dark-stage`, PR #103, see §6a. The original text follows unedited.

   Original: **WP-F's premise is false.** `ThemeContext` adds `.light` and removes it; dark is the *absence* of a class. `classroom.css` keys its entire dark palette on `html.dark`, which nothing in the app ever sets, so 22 dark rules are dead code. Adding dark stage tokens under `html.dark`, as WP-F instructs, would have been dead on arrival too. Simulated on production by re-emitting those rules under `html:not(.light)`: `--classroom-drill-page` correctly flips to `#121019`, but `--observatory-stage-well` stays cream because the hub's stage tokens are declared unconditionally. **WP-F was not shipped.** The correct fix changes the selector for the whole classroom, all five sections, for every student in dark theme, and has never once been rendered. That is its own piece of work with its own verification pass, not a line item inside a drill-hub polish plan.
2. **The theme class is `html.dark` in CSS but `.light` in the app.** The plan's Part 0 table says `.light`; both are half right, and the mismatch is the bug above.
3. **WP-K step 2 describes an unreachable state.** `resolveItemRoute` returns a string on every branch and notifications always carry `onOpen`, so the hero CTA can never be disabled. Writing a reason sentence for it would be dead copy.
4. **WP-J's "define a scale" was already done.** A seven-step scale exists at `classroom.css:954`. The defect is literals bypassing it, not its absence, and the plan's proposed replacement values would have moved every size on the page.
5. **The 1a scan has a second blind spot, and it is structural.** The plan's caveat covers photographs. It does not cover the other case, which fires on the default stage every time: `bgOf` walks *ancestors* for a background colour, so any text sitting on an absolutely positioned **sibling** is measured against whatever is behind that sibling instead. The section switch's active label reports 1.06:1 and is actually 11.79:1. Both blind spots are the same mistake at bottom, which is that the scan reads the CSS cascade rather than the pixels. Text over a photograph, a gradient, a sibling, a `::before` or a canvas needs sampling, and nothing in the scan's output tells you which case you are in. Treat a 1a fail as a question, not an answer.
6. **1c's width test cannot pass in the in-app browser at all.** A `div` created on the spot with `border: 2px solid` reports `1.6px` from `getComputedStyle` while its `height: 20px` reports exactly 20. Every outline, offset and border width in that pane is scaled by 0.8 before it is reported, so `parseFloat(cs.outlineWidth) >= 2` is never true and 1c flags every control on the page. This is on top of the `:focus-visible` over-reporting the plan already warns about, and it is the larger of the two effects. The check that works: press Tab once for real to arm the keyboard heuristic, then read `outline-style` and `box-shadow` rather than any width, and take the width from the source. Done that way, all 14 focusable controls resolve to a solid outline or a 2px inset ring, and the shipped CSS declares `2px` on every hub focus rule.

## 8. Re-score

### Audit

| # | Dimension | Run 2 | Run 3 | Evidence |
|---|---|---|---|---|
| 1 | Accessibility | 4 | **5** | Six hero lines were failing WCAG against the photograph across six widths; all now pass on the published build, worst **4.90 at 390**, measured by sampling the image rather than the scrim. 0 targets under 44px of 16. All 14 focusable controls take a ring, confirmed with the keyboard heuristic armed. Headings h1/h2/h2/h2 at both widths. |
| 2 | Performance | 3 | **3** | Unchanged and unproven. The preload is in the published HTML, but post-fix LCP could not be measured and there is no Lighthouse number for this route. A 3 without evidence stays a 3. *2026-09-09:* measured at last, §6b. LCP 6,542 → 3,540 ms; the preload works and the render delay is the app boot (auth chain, Messages queries, the 1.4 MB bank, explanations JSON). Stays a 3: 3.5 s on an unthrottled desktop is still over the 2.5 s line, and the fixes are outside this surface. |
| 3 | Responsive | 3 | **5** | Five sections at 375 measured full-width after `a82333a`; six widths clean; the 1024 dateline holds one line at 185px in a 201px column, verified at 900/1024/1099. |
| 4 | Theming | 3 | **4** | `!important` 200 → 4, verified in the built bundle, and the observatory wins by specificity. Not a 5: the hub still does not answer the theme toggle, and §7.1 now says exactly why. *2026-09-09:* **5.** PR #103 deployed and measured in both themes on the shipped build, including the live toggle (§6a). |
| 5 | Anti-patterns | 3 | **4** | Shadows cut from 24px/60% to 2px/35%, CTA shadow from `0 8px 32px` to `0 6px 20px`, labels 10 → 7, one glass surface. Not a 5: the serif-over-photograph lane is unchanged. |
| **Total** | | **16/20** | **21/25** | |

### Critique

| # | Heuristic | Run 2 | Run 3 | Evidence |
|---|---|---|---|---|
| 1 | Visibility of system status | 4 | **5** | A failed load now says so instead of rendering as "nothing assigned"; both the hero and Today carry the sentence and a retry. |
| 2 | Match system / real world | 3 | **5** | Six strings moved from feature and screen names to outcomes; "instead" retired. Logged in COPY-CORRECTIONS. |
| 3 | User control and freedom | 3 | **4** | Escape leaves a stage with three tests including the modal guard. Back and section memory were already correct and are now recorded. Not a 5: the builder still discards a half-built set on Cancel. |
| 4 | Consistency and standards | 3 | **4** | Icons on the default stage normalised from four sizes and four stroke weights to 14px at stroke 2; radii already fully tokenised. Not a 5: nine literal font sizes still bypass the seven-step scale. |
| 5 | Error prevention | 3 | **4** | Jump row already disables each select until its predecessor is chosen, with the reason in the placeholder; verified rather than rebuilt. The one remaining trap in the plan turned out to be unreachable. |
| 6 | Recognition rather than recall | 4 | **4** | Unchanged. |
| 7 | Flexibility and efficiency | 3 | **4** | `/` added alongside Cmd/Ctrl+K, both declared in ARIA; resume already leads when it applies, from real data. |
| 8 | Aesthetic and minimalist design | 3 | **4** | Labels 10 → 7, the duplicate dateline gone, shadows quieted, the hover curve fixed so controls answer the pointer in 16ms rather than 40. |
| 9 | Error recovery | 3 | **4** | Every failing surface now states what failed and offers a retry that actually retries. Not a 5: the retry is a page reload because five of seven sources are not react-query backed. |
| 10 | Help and documentation | 2 | **4** | One explainer for the student being asked to trust the adaptive drill, quoting no invented set size. Not a 5: `MainhubHelpControl` is dead code and help reaches Joshua only through Messages in the rail. |
| **Total** | | **31/40** | **42/50** | |

Both totals are out of a larger denominator than run 2 because run 2's rows were scored 1–4 in practice; the rubric is 1–5. Comparing like for like: audit 16/20 → 21/25 is 80% against 84%; critique 31/40 → 42/50 is 78% against 84%.

## 9. Skipped, blocked, or left for Joshua

1. **WP-F: done, deployed, measured.** See §6a. Nothing owed.
2. **Nothing is left unpublished.** Cycles 4, 5 and 6 are all live and all measured on the shipped build. The last gap in this report's evidence, the cycle 6 hero fix, closed on 2026-09-09: 5.84 at 375, 4.90 at 390, 8.49 at 768, each needing 4.5.
3. **Performance is measured, not fixed.** §6b. The four boot-time findings there are the work; none is hub CSS.
4. **WP-J is partial.** Icons and radii done; nine literal font sizes remain in the three TSX files as Tailwind arbitrary values. Converting them to `text-[length:var(...)]` trades one inconsistency for a less readable one; the right fix is named Tailwind `fontSize` entries mapped to the existing tokens, which is a config change worth doing deliberately.
5. **The label count is 7, not the plan's 6.** Reason in §6.
6. **`_bank.generated.json` untouched.** 1,432 KB at app boot on every route, plus ~1.2 MB per-PrepTest explanation JSON; 144 requests / 3,291 KB on the hub. Joshua dismissed the question twice; recorded as a finding only.
7. **`public/mainhub/hub-eclipse.png` and `.webp` are now unreferenced.** Left on disk, not deleted.
8. **Screenshots are partial.** An unscrolled capture at 375 works and is what confirmed the hero by eye; scrolled captures of this page still return a blank image, and the tool produces no files to send. Every claim that would have rested on a scrolled screenshot rests on DOM geometry or pixel sampling instead, which is stated wherever it applies. This is also what let the fourth hero failure survive: the one view that renders cleanly is the one view where the line was fine.

## 10. Surface brief, what changed

Cycle 6 added two rules to the Colour section: that the ink-over-photo rule names **the greeting column, not a list of lines**, with the reason it went stale (a `cover` crop moves under the text as the hero narrows, so the same line passes at 1024 and fails at 375), and that the 1a scan has a **second blind spot** on absolutely positioned siblings. `wiki/DRILL-HUB-PERFECT-SCORE-PLAN-2026-09-08.md` Part 1 gained matching caveats on 1a and 1c so the next run does not repeat either.

Before that, `.impeccable/surfaces/drill-hub.md` gained five things: the measured statement that **the ink ladder does not hold over a photograph and the contrast scan cannot see it**, with the three failing ratios and the 0.58 floor; a Keys section for Escape, `/` and section memory; a "When it fails" section for the error states and why the retry reloads; a Help section recording that `MainhubHelpControl` is unmounted; and a rewritten Known debt entry saying the observatory wins by specificity, with the reduced-motion exception and the portal exception spelled out. The Copy section now carries the outcome-not-feature-name rule and points at COPY-CORRECTIONS.

Related: [[DRILL-HUB-PERFECT-SCORE-PLAN-2026-09-08]] · [[DRILL-HUB-IMPECCABLE-AUDIT-2026-09-08-RUN2]] · [[COPY-CORRECTIONS]]
