# LSAT U: every page fits one screen (2026-09-24)

Grilled with Joshua. Status: agreed plan, not built yet.

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
