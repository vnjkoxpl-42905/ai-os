# Classroom Home visual upgrade: Brainstorm / Discovery Notes
Date: 2026-09-23 · Goal: decide how to take the LSAT U Classroom Home (lsatprep.study/classroom) to another level visually
Status: in progress
Context sources: live page inspected in the in-app browser (signed in as Joshua, teacher view); `projects/lsatu/src/components/classroom/home/` (ClassroomHomeView.tsx, home.css, homeModel.ts, useClassroomHome.ts); public landing `src/components/auth-landing/academy.tsx` for contrast

## Inspection findings (verified 2026-09-23)
- Look: warm cream background, orange accent, serif greeting ("Good morning, Joshua Fisseha"), mono uppercase eyebrows, soft drifting glows and a shine sweep.
- Stack, top to bottom: search box, date eyebrow, greeting + status line, latest message preview ("FROM YAHUNATHAN", 2 NEW), "Start a section" RRC card, "Next session / Nothing booked" card, "Next seven days" strip.
- Page ends right after the 7-day strip. Everything sits in one column at roughly 700px, so on a wide screen the right side is empty.
- Bug: the decorative glows (`.classroom-home-glow-a`, `-glow-b`, `.classroom-home-shine`) extend past the viewport. scrollWidth 998 vs 907 viewport, so there is a horizontal scrollbar.
- The public landing page is a different, dark "academy" look (marble bust, gold, point cloud). The Classroom is light and warm. The two do not share a visual language.
- Not yet seen: the student view of Home (only the teacher view was inspected).

## Summary / key decisions
- 2026-09-23 round 7: Joshua can pin a view per student. Inbox as Home panel + bell everywhere, all six kinds, his messages pinned. Top actions: continue assigned work, Smart Drill, timed section; Question finder on top. Next seven days strip kept exactly as it is today.
- 2026-09-23 round 6: the app picks the view automatically by fixed rules (no AI text); one main insight plus two or three small ones. No new one-question security rule; Home just gives quick access to Smart Drill and assigned work.
- 2026-09-23 round 5: the performance area adapts to each student's work and assignments (types, sections, bootcamps, RC, or other lenses), not a fixed chart.
- 2026-09-23 round 3: Home centers on section results, no goal score, one-question-at-a-time Smart Drill and assignments, fast access to questions and sections, one centralized inbox for messages and notifications. Sleek and high-end.
- Light warm page, two dark anchor cards. Stats: latest PT, questions this week, sessions left, days to test, goal dial. Weakest types by name. Student view first. Restrained motion, reduced-motion safe. Scrollbar fixed separately. (2026-09-23)
- Nothing is borrowed from the public landing page (auth-landing). The Classroom Home keeps its own identity. (Joshua, 2026-09-23)

## Q&A log
### Round 0 (unprompted)
#### Q0 - Landing page influence
- Captured: "I don't want to take anything from the authentic page." (dictation for auth page). No visual borrowing from the dark academy landing.

### Round 1 (asked, not answered directly)
Q1 to Q6 were asked (student vs teacher first, feeling, desktop right column, visual vs new content, motion, scrollbar fix). Joshua replied with six reference dashboards instead. Read from that reply, tentatively: yes to more content and a multi-card layout (Q3, Q4). Q1, Q2, Q5, Q6 still open.

### Round 2 - Reference board (Joshua, 2026-09-23)
Joshua supplied six dashboards: "take inspiration from all of them and see what features we can incorporate", build components from each, then "a master version", and possibly redesign Home around these features. Use Claude Design.

Components pulled from each (Claude's reading, tentative until confirmed):
1. **Notton (dark, mountain hero):** full-width atmospheric photo band under a top stat bar; row of four dark chart tiles (bars, donut, line, ranked list). Borrow: one image-led hero band, a row of equal-height data tiles.
2. **Homies Lab (warm cream/yellow):** "Good Morning" greeting with the date under it, a stat row of 3-4 big numbers with small labels, a gauge dial on the right, a schedule card with tabs (Meetings/Tasks/Events), a line chart with an arrow button, small leave-balance tiles. Closest to the current palette. Borrow: big-number stat row in the hero, gauge, tabbed schedule card, mini metric tiles.
3. **Coders (mono, black and white):** pill-shaped top widgets (time, weather, search), Gantt-style timeline, a dark "Team" block with progress bars. Borrow: black accent cards among white ones, pill widgets, a timeline row.
4. **WeatherWise (dark sky photo):** huge light-weight number, a smooth curve across the week with a glowing dot on today, glass side panel. Borrow: the week strip as a curve with a glowing "today" point, big thin numerals.
5. **Mountain chart dashboard (dark with white rail):** a light left rail of stacked numbers against a dark main area; charts that turn into landscape illustration. Borrow: charts with illustrative depth (mostly decorative).
6. **Be.run (cream, black, yellow):** "Hi, Amanda!" greeting, overlapping blurred bubble chart, a dark month calendar with done/scheduled dots, a goal gauge, a progress bar with a marker, habit rows with segmented progress bars. Borrow: dark calendar card with done/scheduled states, a goal gauge, segmented progress per question type or bootcamp.

Data reality check: Home's model (homeModel.ts) currently has work rows, a hero task with progress, messages, next session, a booking link, and the seven-day week. No score trend, streak or per-type accuracy is wired to Home yet (the Analytics page holds that). Any stat tiles in the master design need a data source decision.

### Master design v1 (Claude, 2026-09-23, tentative until Joshua reviews)
Canvas: https://claude.ai/artifact/6zF3FgewiMA7pCZSk766Xt (two boards: Master Home, and What each reference gives us).
Master Home, top to bottom: pill top bar (search, days-to-test, streak) / hero card with greeting, four big stats and a goal gauge / three cards: Up next (progress bar with marker), Practice test trend (line + glowing point + goal line), dark Training days calendar / Where the points are (segmented bars per question type) beside From Joshua and a black Next session card / Next seven days drawn as a curve with a glowing today point.
Built on the current tokens (cream #f8f1e7, orange #ff8906, ink #332f2c, Fraunces / Outfit / JetBrains Mono). All numbers are bracketed samples.

### Round 2 answers (Joshua, 2026-09-23): "yes to all, go with your recommendations"
- Q1 Direction: light and warm, with two dark cards (calendar, next session). No all-dark page.
- Q2 Numbers on Home: latest PT score, questions this week, sessions left, days to test, goal dial. Cut streak and LR accuracy.
- Q3 Weakest question types shown by name, leading into Smart Drill: yes.
- Q4 Student Home first, teacher view follows: yes.
- Q5 Motion: count-up numbers, cards settle in, gentle pulse on glowing dots; all off under prefers-reduced-motion.
- Q6 Sideways scrollbar: fix now as a separate change on its own branch.

### Data feasibility (sub-agent research, 2026-09-23, verified by file refs only)
- Questions this week: EXISTS, daily_stats.questions_answered; sum last 7 days. Low effort.
- Sessions left: EXISTS, useStudentBooking().pass.credits_remaining, already called on Home. Trivial.
- Days to test: EXISTS, profiles.test_date (nullable) + existing daysUntil() helper. Low.
- Weakest question types: EXISTS, RPC attempt_accuracy_rollup (used by Analytics). Low; needs a minimum-question floor.
- Calendar study days: EXISTS via daily_stats rows with questions > 0; session dates from useStudentBooking bookings. Low.
- Latest PT + trend: PARTIAL. practice_test_runs table exists but nothing writes it; in-app runs live in localStorage; imported scores in student_external_metrics (pt_score). Medium.
- Goal and starting score: PARTIAL. Only bands in profiles.onboarding (target_score_band, last_score_band), can be "not sure".

### Round 3 answers (Joshua, 2026-09-23) - supersedes parts of Round 2 Q2
- "Focus on the section results instead of the latest PT score or recent drills." Section results replace the PT card and trend. Data: section_history (initial_score/total, br_score/br_total, br_delta, time_taken_ms, by_qtype_json, pt, section, completed_at). Supersedes Round 2 Q2's "latest PT score".
- "Don't include the goal score on the page." Goal dial removed. Supersedes Round 2 Q2's goal dial. (Round 3 Q1 and Q2 about PT saving and exact goal score are now moot.)
- Smart Drill: "an option to access the smart drill where they can click and open one question at a time for security", and the same for homework and assignments he assigns. One question opens at a time, never a whole set on screen.
- "A sleek, high-end design that allows quick access to questions or sections for practice."
- "The messaging and notifications should be centralized in one place." One inbox on Home for coach messages and system notifications.
- Round 3 Q3 (empty states) not answered; Claude applies the recommendation (one line + one action) as tentative.

### Facts checked before Round 4 (Claude, 2026-09-23)
- A `notifications` table already exists (title, body, type, link, read) with `useNotifications` hook; written by classroomNotify, sessionBundleNotify, markNoteRead. Coach messages live separately (Inbox / Messages). Centralizing = one surface that reads both.
- Joshua asked (via /grill-me) to keep refining before anything is built. The master design canvas update for round 3 is paused.

### Round 4 (asked Q1-Q8; Joshua answered Q1 and Q2 together, 2026-09-23)
#### Q1/Q2 - What the results area shows, and from which work
- Recommended: last 3-5 full sections as cards (Q1a); full sections only (Q2).
- Captured (supersedes Round 3 "focus on the section results"): "It doesn't have to be practice tests or sections. It can be more of a focus on something specific, like the performance on general question types." It must include Smart Drill, sections, guided drills, "whatever they work with... really to be specific to them." "It doesn't have to be limited to one type of information."
- Decision: the results area is a personal performance view by question type, fed by all of a student's work, not one source.
- Fact (Claude checked): the `attempts` table records each answered question with `qtype`, `mode`, `correct`, `time_ms`, `confidence`; `attempt_accuracy_rollup` already sums it by type. Which modes write to `attempts` (Smart Drill, sections, guided drills, bootcamps) still to be confirmed per mode.
#### Q3-Q8 - not yet answered (one-at-a-time rule and its reason, homework rule, inbox location, inbox contents, top 3 actions, what leaves Home)

### Round 5 (asked Q1-Q9; Joshua answered the performance-view branch, 2026-09-23)
#### Q1-Q3 - What the performance view shows
- Recommended: accuracy + trend per question type, last 30 days, click opens Smart Drill on that type.
- Captured (refines Round 4): "it can be different variations depending on what's useful for the student based on where they've been assigned." "It should depend on what they've been doing and what they've done." "Whether it's based on their work history or something creative, it doesn't have to strictly be question types. These can be sections, question types, or any other format."
- Decision: the performance area is adaptive. It picks the lens that fits each student's recent work and assignments (question types, sections, bootcamp, RC passages, or other), rather than one fixed chart.
- Open: how the lens is chosen, how many insights show, whether Joshua can steer it.
#### Q4-Q9 - still unanswered (one-question rule reason, homework rule, inbox location and contents, top 3 actions, what leaves Home)

### Round 6 answers (Joshua, 2026-09-23)
#### Q1 - Who picks the view
- Recommended: app chooses, Joshua can override.
- Captured: "The app should choose." Automatic. Override by Joshua was not confirmed.
- Flags: whether Joshua wants a per-student override -> Joshua
#### Q2 - How many views
- Captured: recommendation accepted. One main insight, two or three smaller ones under it.
#### Q3 - How the view is chosen
- Captured: fixed rules. No AI-written line.
#### Q4 - "One question at a time"
- Captured: Smart Drill already is one question at a time. "I'm not sure how smart drilling has to do with anything right now." There is no new security rule to design.
- Correction: Claude misread Round 3 ("for security") as a request for a new lockdown rule. Supersedes Round 3's Smart Drill line and Round 4 Q3/Q4 and Round 5 Q4/Q5; those questions are closed. What remains from Round 3 is quick access to Smart Drill and to assigned work from Home.

### Round 7 answers (Joshua, 2026-09-23)
#### Q1 - Override
- Captured: automatic by default, "I want to have the option to pin stuff if I want to." Joshua can pin a view for a student. Resolves the Round 6 override flag.
#### Q2 - Inbox location
- Captured: both. A panel on Home and a bell on every Classroom page, one shared list.
#### Q3 - Inbox contents
- Captured: recommendation. All six (Joshua's messages, new assignments, graded work, session reminders, booking changes, new notes and recaps), Joshua's messages pinned on top.
#### Q4 - Top 3 actions
- Captured: recommendation. Continue assigned work, Smart Drill, start a timed section. Open-a-specific-question stays in the top search bar (Question finder).
#### Q5 - Next seven days
- Captured: "The next seven days thing, I want to keep this there. That should not be removed in the design." "I don't want you to change anything." The current week strip stays exactly as it is today. Supersedes the curve version in master design v1.
- Tentative (Claude): the month calendar from design v1 is dropped, since Joshua kept the current strip instead. Confirm.

### Round 8 - after Codex plan review (Joshua, 2026-09-23)
- Plan: brainstorms/2026-09-23-classroom-home-PLAN.md, review log alongside (3 rounds, gpt-6-astra medium, no APPROVED verdict, no open disagreement).
- Captured: "yes to all three": Flagged + Needs review shelves in the launcher; Review these next to Try new ones; session reminders 24h and 1h before. "update the design first" before any build.

### Design v2 published (Claude, 2026-09-23)
Canvas version 5: new boards Home.dc.html (v2 Classroom Home) and Launcher.dc.html (interactive Question / Section / By type tabs, Needs review and Flagged shelves). v1 boards kept and labelled superseded. Next: Joshua reviews v2, then build choice (Codex builds phase 1, Claude builds, or stop).

## Open flags (pending input)
- Confirm every practice mode (Smart Drill, timed sections, guided drills, bootcamps, RC) writes to `attempts` -> Claude
- Which stats appear on Home and where the numbers come from (Analytics data vs new queries) -> Joshua decides, Claude checks feasibility
- Student-view screenshot of Home -> Claude (needs a student test account or impersonation route)

### Round 9 - v2 build too uniform (Joshua, 2026-09-23)
- Captured: the built phase 1 "is too uniform, like smart drills, time section... still not to the level of what I want." Compared against the six references.
- Captured: model roles. gpt-6-astra helps design and write the spec; building uses gpt-6-sol at low effort. (Saved to memory: codex-model-roles.)
- Cause (Claude): the phase 1 spec banned new data, so only equal text cards were possible; the v2 design also repeated equal-size cards. Not the model.
- Decision: "yes, start v3 and pull the insight data in." v3 design on the canvas first (astra critiques design only), then one build that includes the insight data (phase 2 pulled forward), built by gpt-6-sol low. PR #133 stays unmerged, to be superseded.

### Dual research (Claude + Codex astra, blind, 2026-09-23)
Joshua asked for independent Firecrawl research by both, top 5 each, cross-grading, then a ranking. Output: research/2026-09-23-classroom-home-dashboard-research/. Agreed 7: diagnosis-to-action; coaching attached to the work; finishable Today sequence; review then fresh check; confidence calibration; truthful visual evidence; fast/stable/accessible release bar. Unresolved for Joshua: first place, and Today as host vs optional route.
Still open from before: Q1 left menu (keep vs slim), Q2 empty-state rules. Joshua replied "*" (unclear) and then moved to research.

### Round 10 (Joshua, 2026-09-23)
#### Q1 - What leads the main insight card
- Recommended (Claude): coach note first.
- Captured: "Codex has a better idea than you for question one. I'm not gonna write a note for everybody's work; that's ridiculous." Decision: diagnosis-to-action leads the card. Coach notes are occasional, never expected per student; the page must be complete with no note at all.
- Consequence: feature #2 narrows to Ask with evidence + an optional note only when Joshua pins a view; no workflow that asks Joshua to annotate.
#### Q2-Q7 - not yet answered
#### Q2-Q7 - Claude and Codex converged (Joshua asked them to agree between themselves; to be confirmed via the codex-review plan)
- Q2 Today: optional shortcut; every card works alone, permanently.
- Q3 Registry: Claude drafts 4-8 finding-level mappings (specific diagnosis rule -> verified resource, with reason); Joshua reviews once; unmapped findings open their evidence instead of a made-up recommendation.
- Q4 Confidence: audit existing ratings first (when collected, coverage); no new tap everywhere. If coverage is thin, pilot an optional tap in untimed practice only.
- Q5 Session brief: yes; student-chosen, explicit share, visible beside the booking in the Hub, no obligation to reply.
- Q6a Menu: keep today's full shared menu.
- Q6b Empty states: 1-2 types -> labelled simple result; no practice -> invitation; no assignment -> hide; no session -> compact Book a session (not hidden); loading/failed never shown as empty.
- Q7 Build split: first = v3 layout, honest visuals, quality bar, small registry + diagnosis-to-action, Ask as evidence-attached draft in the existing inbox, sure-but-wrong only if the audit passes. Second = session brief, then review + fresh check, then Today.
- Joshua then asked for /codex-review to perfect the plan with these positions.
