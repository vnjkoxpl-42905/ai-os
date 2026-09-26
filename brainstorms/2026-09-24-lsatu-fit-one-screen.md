# LSAT U: every page fits one screen (2026-09-24)

Date: 2026-09-24 (resumed 2026-09-25) · Goal: every Classroom page and the Question screen fit and read well on any screen size, with no scrolling for the must-see parts.
Status: Drill page + Home PUBLISHED 2026-09-25 (PR #135, merge e1207da, bundle index-BETDQJRn.css); Question screen in grilling Round 9 (Q9.1 locked 2026-09-25)
Context sources: src/components/classroom/CONTEXT.md, measured live in Joshua's Chrome 2026-09-24

## Why pages feel zoomed in
Chrome zoom is 100%. Windows display scaling is 125% (its default on 1080p laptops), so a
1920x1080 screen gives the page 1536x695 CSS px. Measured in his Chrome: devicePixelRatio 1.25,
innerWidth/innerHeight 1536x695. Most students on Windows laptops see the same.

## Names (written into the app glossary, src/components/classroom/CONTEXT.md)
- **Home**: `/classroom`. "home", "homepage", "dashboard" all mean this.
- **Drill page**: `/classroom/drill`, the Drill item under Home. Always said with "page".
  A plain "drill" is a set of questions a student works through.
- **Question screen**: the split view where a question is answered (`/drill`). RC version is
  the RC question screen.
- The Activity Centre's old "Homepage" is now **Activity start page**.

## Decisions
1. Target 1536x695. Also check a big monitor (~1920x950) and a narrow window (rail folds to menu).
2. Drill page first screen, no scrolling: finder row, Smart Drill, Build the drill you need,
   Resume your drill, Top priority, first two Assigned work items. Accuracy trend may scroll.
3. Home first screen, sized for a student WITH homework: greeting with name on one line, what's
   due + Continue, Smart Drill / Timed section, Assigned work card, latest message, AND Next
   seven days.
4. Same layout and design, tightened. If that cannot meet 2 or 3, show Joshua a specific
   rearrangement before building it.
5. Tighten only on short screens; big monitors keep today's roomy look.
6. Build on a branch, send before/after screenshots at 1536x695 and a big monitor. Nothing ships
   to lsatprep.study until Joshua approves.

## Order
Drill page, then Home, then the Question screen (own grilling round: auto-fit text per question,
15px floor, LR columns scroll independently like RC), then the Classroom rail (low priority).

## Carry-over
PR vnjkoxpl-42905/lsatu-684d89db#135 (branch fix/fit-viewport) holds an untested first pass on the
Question screen and Drill hero. Not merged; it becomes the starting branch.

## Q&A log
Rounds 1-6 (2026-09-24) are summarised in Decisions above: names, target 1536x695, first-screen lists, tighten-not-rearrange, short-screen-only tightening, screenshot approval.

### Round 7 (2026-09-25)
- Joshua, in his words: "it should be able to fit into any and adjust perfectly. It should never make any errors." He does not know the current sizes and wants the optimal visual result on all screens.
- Effect: decision 1 (one target, 1536x695) becomes the reference point, not the only size. Decision 5 (tighten only on short screens) is superseded by whatever Round 7 settles about continuous adjustment.
- Fact found: Playwright is installed (playwright.config.ts, e2e/smoke.spec.ts), so an automated size sweep is feasible.

#### Q7.1 - Devices
- Captured: laptops and desktops only. Tablets and phones out of scope.
#### Q7.2 - Continuous vs fixed steps
- Recommended: continuous. Captured: "choose whichever you think is better, but avoid making it fixed in a way that interferes with its ability to be continuous." -> continuous scaling; any breakpoint used must not break the continuity.
#### Q7.3 - What gives first on a small screen
- Captured: recommended order accepted. Home drops, in order: Next seven days, latest message, Smart Drill / Timed section buttons; greeting, what's due and Assigned work always stay. Drill page drops, in order: second Assigned work item, Top priority, Resume; finder row, Smart Drill, Build the drill always stay.
- Note: this refines decision 3 (Next seven days must be on Home's first screen) to "on the first screen at the reference size and larger; first to fall below on smaller screens".
#### Q7.4 - Text floors
- Captured: Joshua has no reference point; I set floors from the visual verification loop. Starting point: body 14px, headings 20px, comfortable click targets.
#### Q7.5 - Large monitors
- Captured: recommended option. Content grows to a maximum width then centres; text grows slightly to a cap; structure should use the extra room to look better, not stretch.
#### Q7.6 - Proof
- Captured: "perfect" means as solid as possible, not literally error-free. Verification is a visual loop in the Claude Code browser while working, not necessarily Playwright. Before/after screenshots to Joshua still stand (decision 6).

## Summary update after Round 7
- Supersedes decision 5 (tighten only on short screens): layouts now scale continuously with window width and height.
- Decision 1 becomes the reference size (1536x695), checked alongside small laptop, big monitor, narrow window.

### Round 8 (2026-09-25)
- Tested on a real tester student account (live site plus injected styles). Spacing alone left Home at 872px for that student, 177 over the 695 fold.
- Captured: Joshua approved the rearrangement after seeing it live: Assigned work and latest message side by side, four quick starts on one row, assigned rows full width. Result 672px. Built as commit 1296716 on fix/fit-viewport.
- The tester-account flag is resolved (tester account used).

### Round 9 (2026-09-25) - Question screen
- Starting state, measured live at 1536x695 on the tester account: page 931 tall, choice E ends at 768, header/breadcrumb/toolbar take the top 248px. LR frame does not pass fillViewport, so the whole page scrolls; RC fills the viewport with independent column scroll.
- Data (all 3,965 LR questions, characters): stimulus p50 388 / p90 547 / max 868; stem + five choices p50 630 / p90 955 / p99 1,520 / max 2,050. The right (choices) column is the pressure, not the stimulus.
- Joshua is worried about breaking things. Risks were laid out for both options; neither touches student data (display only, branch, approval before publish).

#### Q9.1 - What gives when a question is too long
- Joshua, in his words: "Ideally it should aim to be in scope of sight always." Goal: the full question and all five choices visible with no scrolling; scroll is a rare fallback only.
- Locked: (1) compress header, breadcrumb and toolbar (~248px to ~100px); (2) give the choices column more width, the stimulus column has room to spare; (3) tighter gaps between choices without shrinking click targets. No change to text size and never override the student's text-size setting.
- Locked: measure first. After 1-3 are built, measure every one of the 3,965 LR questions rendered at each laptop size and report the count that still overflows plus the list.
- Deferred to that measurement: for the remaining overflow, either shrink text on those questions only (15px floor) or scroll the choices column with a clear "more below" cue.
- Locked: a student who raised their own text size keeps it; their column scrolls if needed.

- Chrome measured live 2026-09-25, 1536x695, tester, /drill?mode=type-drill&qids=PT101-S2-Q1: "Welcome" row 0-35, breadcrumb + Answer/Explanation/Pause row 35-80, dark gap 80-96, toolbar (Directions, find, highlighters, text size, timer, notes) 97-150, question area 150-684 (card has min-h-[700px]), question-number strip 686-737, End/Previous/Next row 737-809, bottom padding to 829. Previous/Next sits entirely below the fold: every LR question needs a scroll just to move on. Chrome totals ~295px of 695.

#### Q9.2 - How the controls shrink
- Locked (Joshua: "yes lock all four"): (1) Previous/Next always on screen, pinned to the bottom, question area takes the remaining height; (2) question-number strip and End/Previous/Next merge into one bottom bar (~50px, was 123); (3) "Welcome" text and Tutor switch fold into the title row; (4) trim toolbar and dark-gap padding. Every button stays and keeps its behaviour. Target: controls ~150px, question area ~545px at 1536x695.

#### Q9.3 - Which screens
- Locked (Joshua: "all five, go ahead and build it"): the shared OfficialDrillFrame change applies to all five users: LR Question screen, RC question screen, Blind Review, section review walk-through, Recall section stage. Each checked at every laptop size.
- Grilling round 9 closed 2026-09-26. Build on a new branch off main.

## Open flags (pending input)
- Temp preview hook: removed 2026-09-25 (__fitPreview.ts deleted, ClassroomHome.tsx hand-reverted to HEAD).
- supabase/functions/mcp/index.ts in the lsatu-fit worktree: Joshua approved the restore, but `git checkout --` is blocked by the permission deny list. Still gutted; Joshua to run the restore himself. Never commit it.
- Tester account's started Smart Drill session: left as is (Joshua, 2026-09-25).
