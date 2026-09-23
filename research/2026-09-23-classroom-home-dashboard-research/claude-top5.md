# Claude's independent TOP 5 (written before seeing Codex's list)
2026-09-23. Research via Firecrawl CLI. Builds on v3; replaces nothing.

## 1. Today's session (a prescribed plan, not a menu)
**What the student sees:** inside the v3 top panel, under the greeting, one line: "Today: about 35 minutes." Below it, three stacked steps with durations and one Start button that runs them in order: (1) 4 wrong answers due for review, 10 min; (2) the assignment due today, 15 min; (3) 8 Smart Drill questions on Necessary Assumption, 10 min. Steps tick off as they finish; the panel remembers progress through the day. The existing Continue card becomes step 2 of this.
**Why world-class:** Whoop does not show a menu; it reads your recovery and recommends a day's strain ("Based on your Recovery, WHOOP recommends an optimal strain each day", https://www.whoop.com/us/en/thelocker/how-does-whoop-recovery-work-101/). A study cited there found athletes following the recommendation trained less and gained the same. For a student, the hardest decision is what to do next; the page should make it.
**Data:** `wrong_answer_journal` review dates (`wajNotesService.ts`, `reattempt_due_at`), assigned work (`useAssignedTodoFeed`), weakest type (`home_lr_type_accuracy`, planned). Fixed rules, no AI text. Launch through `drillLaunch.ts` kinds `questions`, `assignment`, `filter`.
**Effort:** M. **Risk:** a stale plan if a student practices elsewhere; recompute on focus.

## 2. Speed or understanding? (the blind review verdict)
**What the student sees:** the Last section tile grows a one-line verdict computed from the gap between timed and blind review score: gap of 3 or more → "You know more than the clock lets you show. Practice timed." with Start a timed section; gap under 2 → "The misses are understanding, not speed. Review before drilling." with Review these.
**Why world-class:** 7Sage's own framing: blind review "separates fundamentals from technique... if your BR score is significantly higher than your untimed score, you ought to do more timed sections... If not, your fundamentals are what need work" (https://7sage.com/blog/lsat-tips-perfecting-blind-review). Every LSAT student hears this; no dashboard computes it for them.
**Data:** `section_history.initial_score`, `br_score`, `br_delta` (Home adapter from the plan).
**Effort:** S. **Risk:** single-section noise; use the last 3 sections when available and say so.

## 3. Sure but wrong (confidence calibration)
**What the student sees:** a small 2x2 in the lower row: sure/unsure against right/wrong over the last 30 days, with the "sure and wrong" cell in orange: "You were sure on 9 questions you missed." One action: Review these 9.
**Why world-class:** overconfidence is the most common and least visible study failure; the fix is putting judged confidence next to the real result until "confidence follows evidence" (Structural Learning on Hacker 1998 and Kruger & Dunning, https://www.structural-learning.com/post/metacognitive-monitoring-fixing-student; medical-education calibration tool, https://journals.physiology.org/doi/full/10.1152/advan.00156.2021).
**Data:** `attempts.confidence`, `attempts.correct` (LR). Already captured, never shown on Home.
**Effort:** S to M. **Risk:** confidence may be sparsely recorded; show only above a floor.

## 4. The coach is on the page (the thing no competitor can copy)
**What the student sees:** (a) when Joshua pins a view, his one-line note sits on the insight card in his words, signed. (b) An Ask control on any insight sends that insight's evidence (types, counts, question addresses) to Joshua with the student's comment. (c) The day before a session, the Next session card gains "Bring to Thursday": questions the student flagged or got wrong while sure, auto-collected, which Joshua also sees.
**Why world-class:** LSAT U is 1:1 coaching; 7Sage, LSAT Lab and UWorld are self-serve. The dashboard should make the coach visible, not hide him in a message thread. Glossary rule respected: the control says "Ask", not Joshua's name.
**Data:** `home_insight_pins` (planned, add a `note` column), messages, flags (`flaggedService.ts`), bookings (`useStudentBooking`).
**Effort:** M. **Risk:** coach workload; notes are optional and short.

## 5. Craft you can feel: instant, quiet, keyboard-first
**What the student sees:** Home paints instantly from the last visit's cached data, then updates in place (no spinners); skeletons match the real layout on first load; numbers count up only on the first visit of the day; opening a card animates into the drill (shared-element view transition) instead of a page flash; keyboard shortcuts (Ctrl K find, S Smart Drill, T timed section, I inbox) shown on hover; everything respects reduced motion.
**Why world-class:** skeletons improve perceived speed where spinners do not (https://blog.logrocket.com/ux-design/skeleton-loading-screen-design/); Stripe treats empty and loading states as designed surfaces with a next step (https://docs.stripe.com/stripe-apps/patterns/empty-state); Linear's reputation is craft and speed (https://linear.app/now/craft).
**Data:** TanStack Query persistence (already in the app), View Transitions API.
**Effort:** M. **Risk:** view transitions are Chromium-first; progressive enhancement only.

## Blind spots in v3 and the plan
1. **Test-day phases.** The page should change mode by days to test: far out = build; final 14 days = timed sections and review; last 3 days = taper, no new material. Nothing in the plan knows the calendar.
2. **Color-only meaning.** Orange = weak, green = up. Add text or shape (arrows, labels) for colour-blind students.
3. **Freshness and trust.** Every number should say what it counts and when it updated ("Last 30 days · updated 2 min ago"). Numbers without denominators erode trust.
4. **Phone first.** Many students will open Home on a phone before a session; the v3 top panel needs a phone composition, not a stacked desktop.
5. **Joshua's mirror.** The coach should see exactly the Home a student sees, from the Hub, to coach from it.

## Considered and rejected
- Streaks and XP (Duolingo): locked out and wrong tone for adults paying for coaching.
- A composite "readiness score" (Whoop-style single number): tempting, but it would stand in for a goal score, which is locked out, and it invents precision.
- AI-written daily summary: locked out; rules only.
- Leaderboards or peer percentiles: no peer group large enough; anxiety for little gain.
