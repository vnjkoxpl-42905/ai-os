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

## Open flags (pending input)
- Which stats appear on Home and where the numbers come from (Analytics data vs new queries) -> Joshua decides, Claude checks feasibility
- Student-view screenshot of Home -> Claude (needs a student test account or impersonation route)
