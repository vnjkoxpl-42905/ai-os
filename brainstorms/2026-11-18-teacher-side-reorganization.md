---
type: brainstorm
subject: Why the LSAT U teacher side feels chaotic, and the decisions that would fix it
created: 2026-11-18
status: proposal, nothing built
sources:
  - brainstorms/2026-09-27-teacher-command-center.md
  - brainstorms/2026-10-28-teacher-home-build-review.md
  - design/reviews/classroom-quality-20261028/REPORT.md
  - design/reviews/classroom-quality-20261028/viewport-1440.png
  - design/principles.md
---

# Teacher side: diagnosis and proposed decisions

Evidence limits: the newest teacher render on disk is 2026-10-28 (viewport-1440.png, a synthetic local shell). The live admin view was not inspected on 2026-11-18 because the browser pane is signed in as the student account. Structural claims come from the current source (`src/App.tsx`, `TeacherWorkspaceShell.tsx`, `components/classroom/home/teacher/`).

## Root causes

1. **Two teacher homes and two shells.** Classroom Home renders a teacher desk (`TeacherHomeView` / `TeachingDesk`), and `/teacher/today` renders a second one (`DeskTodaySurface`) inside the Teacher Workspace shell, which has its own eight-room sidebar (Today, Inbox, Payments, Students, Library, Reading Center, Teaching Assistant, Insights). The classroom sidebar also mixes student destinations (My Work, Practice, Review, Progress) with a Teaching group. Joshua does not know which home is the real one, and neither does the layout.
2. **The schedule appears three times on one screen.** The count strip, the seven-day strip with its day list, and the Next up agenda all show the same sessions. Repetition reads as clutter and violates the plan's own rule ("never a second contradictory schedule").
3. **Too many competing emphasis devices.** The charcoal Assign work button, a charcoal session card, a selected charcoal day tile, tinted Open follow-up pills, ↗ link arrows on nearly every row, count badges and a four-cell count strip with zeros. The design principle says reserve charcoal for one action; the render uses it three times.
4. **No single reading order.** Counts, then calendar, then work, while the rail carries agenda, decisions and payments. The spec's own first question ("what needs my action, and which student am I preparing for next?") is answered below the fold.
5. **Every surface has a different grammar.** Rows, cards, tiles, pills and link-arrows coexist; section titles alternate between Fraunces and Outfit.

## Proposed decisions (Joshua to confirm)

| # | Decision | Recommendation |
|---|---|---|
| D1 | One teacher home | Keep the Classroom teacher Home as the only home. `/teacher/today` redirects to it. |
| D2 | One teacher navigation | When signed in as teacher, the sidebar shows teaching destinations only: Home, Students, Inbox, Library, Payments, Insights. Student views are reached through "View as student", not mixed into the sidebar. Reading Center and Teaching Assistant move under Library / tools. |
| D3 | One schedule on Home | Keep a single agenda ("Next up", 3 rows). Drop the seven-day strip from the teacher Home (Schedule is a page). Drop the count strip; counts live on their own section heads. |
| D4 | Fixed reading order | 1 Next session with Prepare. 2 After-session work. 3 Decisions (payments + access, one list). 4 My list. 5 Messages and email. Same order on phone. |
| D5 | One emphasis | Charcoal only for the single primary action (Prepare for the next session, or Assign work when nothing is scheduled). Every other row uses the same quiet row grammar: name, absolute time, one plain-text status, one text action. No ↗ arrows on internal links. |
| D6 | One row grammar everywhere | Students, payments, tasks and messages all use the same hairline row and type scale. Fraunces for the greeting and section titles only. |
| D7 | Empty means hidden | A section with nothing to do collapses to a single line ("No payment decisions"); zero counts never get a cell. |

## Next steps if approved

Start with D1 to D3 (structure). They remove the most chaos and change no data contracts. Then D4 to D7 as one visual pass, checked at 1440 and 390 with real signed-in data.
