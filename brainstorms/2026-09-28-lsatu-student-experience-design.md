# LSAT U student experience, first visual version

Date: 2026-09-28  
Status: design prototype, not an app change  
Companion: [platform adoption game plan](2026-09-27-lsatu-platform-adoption-game-plan.md)  
Prototype: [clickable student view](prototypes/lsatu-student-experience.html)

## What the current student screen tells us

Joshua's 2026-09-28 screenshot shows a recognizable LSAT U Home: warm surfaces, a greeting, a prominent overdue assignment, quick actions, assigned work, a message from Joshua, and a seven-day strip. These are useful starting points. It also shows the cost of the current rail: Home, Drill, Practice Exams, Assigned work, Notes and recaps, Bootcamps, Activities, Review, Analytics, Admissions, History, Messages, and Schedule all compete at the same level. The Home hero and large assigned-work card leave little room to see the next study decision and its reason together.

The student design keeps the product's warm tone and the approved Home v3 direction. It makes the next action, assigned work, and teacher message easier to scan in the first viewport. The page is a sample interface, so its names, dates, counts, and question references are illustrative and must not be interpreted as live student data.

## One rail, with destinations students can predict

| Current student entry | Proposed place | Access detail |
|---|---|---|
| Home | Home | Next action, assignments, teacher message, review due, and week ahead. |
| Drill | Practice > Drills | Smart Drill stays one action away from Home and Practice. |
| Practice Exams / Testing Centre | Practice > Timed Sections / PrepTests | The timed launch screen names the clock and requires a deliberate start. |
| Assigned work | My Work > To do / Completed | Each work row links to the right Practice, Activity, or test surface. |
| Notes and recaps | My Work > Notes & recaps | Notes and recaps retain their own record types and context. |
| Bootcamps | Library > Bootcamps | Continue and progress appear on the item card. |
| Activities | Library > Activities | The assigned instance also appears in My Work. |
| Review, Wrong answers, Flagged | Review > To review / Wrong answers / Flagged | A single queue explains why each question is there. |
| Analytics and History | Progress > Overview / History / Topics | Counts disclose the included source and sample size. |
| Admissions | Library > Admissions | Visible only to students with the existing access right. This is a proposed location, not a feature removal. |
| Messages | Persistent Inbox control in the top bar, with full thread view | Badge and recent message remain visible from Home. Preserve direct message links. |
| Schedule | Schedule | The next session and Book a session are visible without leaving the student shell. |
| Find question | Persistent top-bar search | Keep exact PT/S/Q and text lookup, then return to the originating page. |

The seven primary rail destinations are Home, My Work, Practice, Review, Progress, Library, and Schedule. Settings and account controls stay with the profile. A student with restricted access sees only allowed tabs, using existing permission rules. Existing deep links and saved rail preferences need migration as specified in the main game plan.

## Student screen behavior

1. **Home answers what to do next.** The first recommendation states its source, why it is next, and a single Continue action. A message and a second assignment stay nearby. A short review-due line links directly into Review. The seven-day strip stays, but it does not crowd out the work.
2. **My Work is the teacher relationship.** To do, Completed, and Notes & recaps show assignment source and state. A student's own note is not presented as a teacher recap. An unstarted assignment appears before any attempt exists.
3. **Practice separates stakes.** Drills, Timed Sections, PrepTests, and Saved sets are local tabs. Timed work gets a start summary. Inspecting a known question is clearly different from scoring a new attempt.
4. **Review is a task, then a record.** To review leads. Wrong answers and Flagged let students audit the queue. The question view keeps the first answer, any blind answer, written diagnosis, explanation, Joshua's note, and a deliberate Mark reviewed action.
5. **Progress explains a next action.** Summary cards link to the underlying attempts and to a relevant review or drill. Empty data says there is not enough evidence, rather than displaying zero accuracy.
6. **Library holds longer-lived material.** Lessons, Activities, Bootcamps, and permission-gated Admissions live here. Assigned Activities also appear in My Work so the student can find them through either task or resource context.
7. **Schedule closes the loop.** Preparation links to the upcoming session, which links to the recap and follow-up work. Booking remains a clear action.

## Visual decisions for this version

- The rail target is 248 to 256 px with seven full labels, one active state, and no second permanent navigation column. This is a prototype target to test at laptop widths.
- The top bar carries search and Inbox. Search is a task shortcut; Inbox's unread count is persistent without making Messages an eighth primary destination.
- The first Home row uses a compact recommendation panel rather than the screenshot's tall welcome block. It keeps the warm gradient and dark work card as LSAT U accents, while letting the assigned list and message enter the first viewport.
- Local tabs sit directly below each page title. Their active states and URL state should match; the static prototype demonstrates the interaction, while production must retain browser history and direct links.
- Main buttons name the exact action: Continue assignment, Start timed section, Open recap, Mark reviewed. Labels for first answer, correct answer, and review state use words as well as color.
- Responsive behavior preserves question reading width. On phones the rail becomes a drawer, cards stack, and the top bar keeps Inbox and search available.

## What to validate before adopting the design

Walk one current student through finding an assigned Activity, opening a recap, starting a timed section, reviewing a flagged question, and booking a session. Repeat on a 1024 px laptop and a phone. Confirm the student can locate Inbox quickly despite its move to the top bar. Inspect actual access tiers before placing Admissions or any other gated tab. Keep the approved Home v3 data and chart rules; this prototype does not replace that implementation brief.
