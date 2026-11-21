# Plan: Teacher Home v2, "the observatory"

## Goal
Redesign the whole teacher Home prototype (`design/prototypes/teacher-home/home-mockup.html`, unchanged) into one sophisticated, otherworldly, top-tier page built around the eclipse orb, with strip version A (studio ledger, `strip-versions/compare.html`) incorporated. Output: `design/prototypes/teacher-home/home-v2/index.html`, self-contained (inline CSS/JS, no network). Joshua gets a list of every improvement.

## Locked (brainstorms/2026-11-18-teacher-side-visual-direction.md, memory, design/principles.md as revised 2026-11-18)
Eclipse hero + follow-up gauge + week-load meter (1B); after-session card stack (2A); message faces as a bento widget (5B/10A); dock pill with search + Assign work (lit), Messages, Calendar, Students, panels rising from the dock (4A/8A); tactile pressed objects (6B); students on Home: next session + homework status + gone quiet (Q11 A+C). Near-white ground, one charcoal anchor family, serif numerals, hairlines, at most one muted dot, beige only as a faint streak. Status in one ink tone via shape/weight, never hue. No em dashes. Text >= 12px.

## Audit of the current mockup (what v2 fixes)
1. Orb is decoration: the sun is clipped off the card edge, orbit rings cut, one stray planet, countdown static. It is not connected to anything else on the page.
2. Two type systems collide: bold sans h1 and sans numerals in hero/gauge vs serif in the strip.
3. Uppercase tracked micro labels on every card (principles warn against this spread).
4. Every card lifts on hover although most are not interactive: false affordance.
5. After-sessions stack: large empty space, ghost cards clipped, unicode ticks, unclear four-step bar.
6. Messages: faces only, no preview text, "!" badge meaning unclear, clickable divs without focus.
7. Week load: bars have no values; today is an outlined (inverted) bar that reads as "empty"; 11px labels.
8. Follow-up gauge: arc with no scale; "3 left of 6" split from it.
9. Bento rows uneven; dead whitespace; at narrow widths the hero and widgets stack without rhythm.
10. Dock overlaps content and truncates the search placeholder on narrow screens; panels list static text.
11. Charcoal values inconsistent (#15181a, #131718, #16191b, #0b0d0e).
12. Greeting has no summary of the day.
13. Strip: replace with version A.

## Design direction
One idea: **the eclipse is the page's light source.** The hero is a night window; the rest of the page is near-white paper lit by it.
- **Hero (span full width at top on desktop, 2/3 + 1/3 split):** the eclipse fully inside the card: black disc with a thin white limb and a soft corona (layered radial gradients, slow 12s breathing on the corona only, off under reduced motion). Three concentric hairline orbits. **Today's sessions are planets on the orbit**, placed by time (09:00 to 21:00 mapped to an arc); the next session's planet is lit, past ones hollow, with a small serif label. Countdown is live (updates each minute from a fixed "now" of 10:00 in the fixture, so the prototype is deterministic). Left side: serif display "5 h 0 min" numerals, "until Lydia Park, 3:00 pm", one white tactile button "Open Lydia's prep" (real button, opens the dock panel for Students as a stand-in).
- **Instruments (right third, dark glass, same family as hero):** follow-up gauge with tick scale and the number inside the arc ("3 of 6"); week-load meter with values on hover/focus and today as the solid tallest bar with a lamp streak, not an outline.
- **Paper widgets below:** After sessions (one front card fully legible: name, when, four named steps as segmented chips "Transcript, Notes, Recap, Next work" with done/undone shape; two thin edges behind it, nothing clipped); Messages (faces + one-line preview of the latest message each; badge count only, enquiry shown as the word "Enquiry"); Next seven days = strip A, with a faint time-of-day tick under each session (idea taken from B) and the gone-quiet ledger.
- **Type:** serif (Iowan/Palatino/Georgia stack) for all display text and numerals; Inter/system for working text. Sentence-case small labels at 13px, weight 600, no uppercase tracking.
- **Material:** one charcoal scale (--night-0 #0e1112, --night-1 #15191b, --night-2 #1f2427), one ink #15181a for paper. Hover lift only on interactive elements; cards are still. Pressed states reduce shadow. Focus ring visible on both paper and night.
- **Dock:** same five controls; on <= 820px it collapses to search icon button + Assign work + a "More" button that opens the same panel list; never overlaps content (body gets bottom padding equal to dock height). Panels: real lists of buttons; Esc closes and returns focus; panel is a labelled dialog (non-modal).
- **Greeting:** serif "Good morning, Joshua" and one summary line: "3 sessions this week, 3 follow-ups, 2 students gone quiet."

## Shared fixture
Now = Wed 18 Nov 2026 10:00. Sessions: Lydia Park Wed 15:00 homework done; Celia Moreno Thu 13:00 half; Zoë Adams Fri 17:00 done. After sessions: Celia (yesterday, transcript + notes done), two more waiting. Messages: Celia "Can we move Friday to 5?", Ivory "Here is my PT 156 review sheet", Dakota "Thanks for the drill!", Priya enquiry "Hi, I'm looking for LSAT tutoring". Gone quiet: Ivory Chen 6 days, Avneet Singh 9 days, Dakota Reyes no session booked, homework not started. Follow-ups 3 of 6. Week load Mon..Sun 2,4,5,3,2,1,0 (13 total).

## Acceptance criteria
1. Opens over http and file:// with no console errors and no network requests.
2. Orb is fully inside the hero at 1280, 1000 and 375 widths; both Wednesday planets sit at their 15:00 and 19:00 positions; countdown text derives from the fixture and the simulated clock.
3. No horizontal scroll and no clipped content at 375; dock never covers the last content (checked by scrolling to bottom).
4. Every interactive element is a button/link/input, keyboard reachable with visible focus; dock panel opens, Esc closes and returns focus.
5. No hue-coded status; status glyphs plus text. No em dashes. No text under 12px.
6. prefers-reduced-motion stops the corona animation.

## Verification
In-app browser via `teacher-home-static` (port 8134): screenshots at 1280 / 1000 / 375; JS checks for scrollWidth, element bounds of the orb within the hero, font-size scan (min >= 12px), focus/Esc test; grep for em dash. Then fresh Codex inspection.

## Non-goals
No LSAT U code, no real data, no change to home-mockup.html or the brainstorm decisions; the dock set stays (Joshua may revise later).

## Revisions after Codex round 1 (these override earlier text)
- **THV2-01 counts.** Week load counts every calendar session (tutoring + consultations), Mon 16 to Sun 22: 2,3,2,3,2,1,0 = 13. Wed (today) has 2: Lydia Park 15:00 and a Consultation 19:00. The strip shows the next session per student for the 6 students on Home (3 booked + 3 in the quiet ledger). Greeting line: "13 sessions this week. Next is Lydia Park at 3:00 pm." Hero planets = Wednesday's 2 sessions. All counts derive from one fixture in JS.
- **THV2-02 search.** Desktop: inline labelled search input in the dock. <=820px: a search icon button opens a dock panel containing the same labelled input, focused on open. Matching is local over the fixture (student names and question refs "PT 156 S2 Q14", "PT 105 S2 Q3", "PT 140 S1 Q22"), case-insensitive substring; results are buttons that show a one-line "Would open ..." confirmation in the panel; no match shows "No match for '<q>'". Other panels (Assign work, Messages, Calendar, Students): rows are buttons that show the same in-panel confirmation; purely informational rows are text.
- **THV2-03 surfaces.** One surface manager: at most one popover open (dock panel or strip session detail). Opening one closes the other. Each records its opener element; Escape or the visible Close button closes the open surface and returns focus to that opener. On open, focus moves to the panel's first control (search input when present). The hero "Open Lydia's prep" button opens the Students panel scrolled to Lydia, opener = that button; mobile More opens a panel listing Messages, Calendar, Students as buttons that swap the panel content.
- **THV2-04 clock.** Simulated clock starts at Wed 10:00 and advances with real elapsed time (1:1), re-rendering each 30 s. Countdown targets the next session that has not started. From 15:00 to 16:00 Lydia's planet shows "In session" and the hero reads "In session with Lydia Park"; after that the target is the 19:00 Consultation; after 20:00 the hero reads "No more sessions today" and points to Celia, Thu 1:00 pm. A `?t=HH:MM` query sets the start time for testing.
- **THV2-05 quiet rule.** Gone quiet = no activity 5+ days: Ivory Chen (6), Avneet Singh (9). Dakota Reyes appears in the same ledger row under a separate label "Needs booking: no session booked, homework not started". Greeting never states a gone-quiet count other than derived from the rule.

## Revisions after Codex round 2 (override earlier text)
- **THV2-06.** Bars scale by actual count. Today (Wed) is marked by the solid treatment with a lamp streak and the label "Today", not by height. Earlier "today as the solid tallest bar" is replaced.
- **THV2-07.** Desktop: typing in the dock search keeps focus in the input; results render in the panel below; ArrowDown moves into the results, ArrowUp from the first result returns to the input, Escape closes and keeps focus in the input. The "focus the first control" rule applies only to panels opened by a button. Mobile More: choosing Messages/Calendar/Students swaps content and moves focus to the new content's heading (tabindex=-1); Escape or Close returns focus to the visible More button.
- **THV2-08.** Events have [start, end) intervals: Lydia 15:00 to 16:00, Consultation 19:00 to 19:45. One function `state(now)` returns {current, next}. Hero, planets, countdown, greeting line and hero action all derive from it: during an event "In session with X" (action: "Open X's prep" for students, "Open consultation notes" for the consultation); otherwise countdown to next; after the last Wednesday event, "No more sessions today", next = Celia Moreno Thu 13:00, action "Open Celia's prep".
- **THV2-09.** One calendar fixture with stable ids (e.g. s-lydia-1118, c-1118-1900). The strip is built from events filtered to type=tutoring for the 6 Home students, renders every qualifying session per date, and resolves detail and focus return by id.

## Revisions after Codex round 3 (override earlier text)
- **THV2-10.** The hero action is chosen by the current/next event id. Student event: opens the Students panel focused on that student's row (name, next session, homework status, "Would open prep" confirmation button). Consultation event: opens the Calendar panel focused on that consultation's row, showing fixture notes "Prospect: Priya N. Wants a 165+, test in January. No notes taken yet." with the same confirmation button. Opener is the hero button in both cases.
- **THV2-11.** Strip selection: for each Home student, take the earliest tutoring event with start >= now within Nov 18 to 24; then group those by date (several students on one day allowed). Ids drive detail and focus return. This replaces "renders every qualifying session per date".

## Revisions after Codex round 4 (override earlier text)
- **THV2-12.** Strip selection uses end > now (not start >= now), so a session in progress stays in the strip until it ends. The strip heading "Next seven days" has tabindex=-1. Clock refreshes re-render the strip without moving focus when the focused element still exists (re-found by id). If a refresh removes the opener of an open detail, the detail stays open and Close/Escape returns focus to the strip heading.
