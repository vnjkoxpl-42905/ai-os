# Visual design critique: LSAT U student dashboard, three directions vs. the 2026-10-22 handoff

## Problems during this review

1. **The fresh browser capture failed, and it overwrote files.** `capture.cjs` requests `http://127.0.0.1:5191/LSAT-U-Dashboard-Three-Directions-v2/<dir>/student.html`. The server now serves the directions at `/<dir>/student.html`, so all 12 captures came back as 404 pages. The script still wrote its 12 `*-top.png` files, so any earlier top-viewport PNGs with those names in `research/2026-10-23-dashboard-final-audit/` have been replaced with 404 screenshots. It also rewrote `independent-layout-report.json`. In that report, `docHeight == viewport` and `nav: []` both come from the 404 page, not the designs. I didn't edit the script. The fix is to change the URL path in line 6, but that's your call.
2. **Phone motion sheets weren't inspected.** Bash was denied, so I couldn't list `_verify/video/`, and my guesses at the phone sheet filenames didn't exist. My mobile scores come from the static 390 px full-page renders only.
3. **Model and effort:** I'm running as Opus 5.5 (`claude-opus-5-5`). I can't set or confirm the "Medium" effort setting from inside the session.

## Images inspected

- `Three-Directions-v2/screenshots/lamplight-student-1440.png`, `lamplight-student-390.png`
- `screenshots/carrel-student-1440.png`, `carrel-student-390.png`
- `screenshots/marginalia-student-1440.png`, `marginalia-student-390.png`
- `_verify/video/lamplight-student-sheet.png`, `carrel-student-sheet.png`, `marginalia-student-sheet.png` (desktop contact sheets, 13 to 17 frames each)
- `Handoff-2026-10-22/student-dashboard.png`, `student-dashboard-390.png`
- `research/2026-10-23-dashboard-final-audit/lamplight-student-1440-top.png` (the 404 capture, used only to diagnose the failure)

I didn't read any source code, critiques, `AUDIT.md`, or transcripts. The 390 px full pages were downscaled to about 200 to 270 px wide when displayed, so I judged mobile at the level of composition, not small text.

## Rubric (100 points)

| Criterion | Weight | What it measures |
|---|---|---|
| Hierarchy and first-screen focus | 25 | Does tonight's task win the first screen? Do messages, calendar and nav sit at the right weight? |
| Typography and readability | 20 | Typeface character, scale, contrast, small-text legibility |
| Spacing and composition | 15 | Grid, proportions, balance, dead space, page length |
| Distinctiveness and coherence | 20 | Originality, and whether one idea holds the page together without kitsch |
| Motion and interaction design | 10 | Does motion carry meaning? Entrance order, feedback |
| Mobile adaptation | 10 | Does the idea survive at 390 px, or does it just stack? |

| | Hierarchy /25 | Type /20 | Spacing /15 | Distinct. /20 | Motion /10 | Mobile /10 | **Total** |
|---|---|---|---|---|---|---|---|
| **Lamplight** | 21 | 15 | 10 | 18 | 8 (medium confidence) | 7 | **79** |
| **Marginalia** | 18 | 18 | 13 | 15 | 6 (medium-low) | 7 | **77** |
| **Carrel** | 16 | 15 | 9 | 13 | 8 (medium) | 6 | **67** |
| **Handoff baseline** | 20 | 15 | 11* | 8 | not scored | 7* | **61/90** (about 68/100 scaled) |

\*The baseline images show only about one viewport (1131×821 and 390×900), so its lower page and mobile scores are partial. It has no motion evidence, so motion isn't scored.

The motion scores come from 13 to 17 sparse frames per direction, not continuous video. Read them as ±2. They can't speak to easing, timing or jank.

## Facts measured from the images (not taste)

- **Page heights:** Lamplight 1440 renders at 2700 px tall and 3907 px on mobile. Carrel is about 1880 and 3416. Marginalia is 2085 and 2919.
- **Background seam:** Lamplight and Carrel both show a hard background-tone break at exactly y≈900 in the desktop full-page render. That's the capture's viewport height, so it's probably a gradient sized to the viewport. It may be a capture artifact, but if a user scrolling sees it too, it's a real flaw.
- **Clipped mobile nav:** Lamplight and Marginalia clip the nav at the right edge ("Lib…"). Carrel drops "Library" from the visible row.
- **Clipped Carrel tabs:** Carrel's card tabs truncate on desktop ("Flaw questions, ...", "Recap: sufficient" cut by the next card).
- **Prototype toolbar overlap:** a fixed toolbar sits bottom-right in all motion frames and covers content (in Lamplight it covers "Session recap: suffi…"). It's prototype chrome, not part of the design, and isn't scored.
- **Blank first frame:** Marginalia's first frame is almost blank, showing only the nav and footer line. Its content renders after load.

## Lamplight: ranked 1st (79)

**Strongest elements**
- **The lamp is a hierarchy device, not decoration.** The one lit cream card on a dark navy field is the clearest "do this now" of any version, the baseline included. The light itself marks the focus.
- **The interaction carries the metaphor.** "Pick one to look at under the lamp" works: in the motion frames, choosing a row dims the Negation Station card, swaps "Read Joshua's notes on PT105 S2" into the light, and returns the old item to the list. That's the best idea in the whole set: the main slot is a stage you can recast, not a fixed hero.
- **Entrance motion has meaning.** The light cone turns on before the card arrives, the progress squares fill in, and list rows warm when hovered.
- **The calendar treatment is the most original in the set.** "The week, by evening" shows each day as a window: warm amber for work due, cool blue for a session with Joshua, dark for nothing listed. You can read the week from colour alone. It also turns the "nothing listed is not free" disclaimer into part of the visual logic.
- **Typography has character.** The display serif in "Good evening, Ada." and "Negation Station" feels premium and evening-quiet. The progress bar of twelve squares, with the sixth marked by a dash, reads instantly.

**Weakest elements**
- **Unbalanced composition below the hero.** The card ends around y≈670 while the right column runs to about y≈1215. That leaves roughly 550 px of empty dark space under the lamp at 1440. It reads as unfinished, not as deliberate negative space.
- **The greeting competes with the card.** Both are large serif blocks side by side, so the eye goes back and forth. The greeting should step down, or the card should claim more width.
- **Low-contrast small text.** Grey sans on navy ("Due Friday at 9:00 pm", "Posted October 20", the section captions) is small and dim. It's the main readability weakness.
- **Generic pieces.** The outlined pill buttons ("Open", "Mark done") and Joshua's message box are generic dark-UI parts and don't belong to the lamp world. The message is the second most important thing on the page and looks like a settings panel.
- **"Thirty-eight evenings to test day" spends a full-width section on a thin dotted line** that says little more than the number already does. The empty windows are close to invisible, and "Practice on your own" is a plain bordered box.
- **The page is long:** 2700 px desktop and 3900 px mobile.

**Compared with the baseline:** the baseline's dark due-today card, in the same structural position, is a plain block. Lamplight takes the same priority and makes it atmospheric and interactive. It loses the baseline's compact right rail, where search, Smart Drill, Inbox, next session and countdown sit together. In Lamplight those are pushed far below the fold.

**Mobile:** this is the best idea transfer of the three. The lamp and card hold up, and the week windows turn into horizontal light strips, which is a good adaptation. The cost is length, and the nav clips.

## Marginalia: ranked 2nd (77)

**Strongest elements**
- **The best typography of the four.** The serif body is set large and dark. Small-caps run-ins ("TONIGHT", "THREE MORE", "JOSHUA WROTE", "YOUR NEXT SESSION") lead each section, Joshua's message is an italic pull quote, and footnote numbers tie each sentence to its sidenote. It's the most readable page and the most "teaching brand".
- **The most disciplined grid.** It's a strict three-column layout: a gutter label (Tonight / After that / From Joshua / Ahead / The week), the text column, and numbered sidenotes. The sidenote numbers line up with their references.
- **A content-first design.** The dashboard reads as a short letter about your evening. That's a truly different idea, and it suits a tutor-led product.
- **The week as a dotted-leader table of contents** ("Thu 22 ……… Negation Station") is elegant and quiet.
- **The 38-day tick ruler** has taller ticks for weeks and a pencil mark for Saturday's session. It's the most information-dense countdown in the set, and it's tiny.
- **Motion:** hovering a footnote highlights its sidenote and draws a connector line, and the tally marks draw in. The motion is fitting but subtle.

**Weakest elements**
- **The task isn't an object.** Apart from the blue "Continue at prompt 6" button, nothing on screen has visual weight. Tonight's work is a sentence among sentences, so you have to read to scan.
- **Too many underlines.** Nearly every noun is an underlined blue link, so nothing stands out.
- **Visually quiet, close to flat.** No depth, no surfaces, almost no colour. It's refined, but it isn't striking, and at a glance it looks like a document, not a product home.
- **Unanchored right column.** The sidenotes leave gaps (about y 1300 to 1680) and get no visual emphasis.
- **Weak calendar at a glance.** The week list is lovely to read but slow to scan, because "nothing listed" days carry the same weight as filled ones.
- **Loading flash.** The near-blank first frame suggests content pops in rather than being choreographed.

**Compared with the baseline:** Marginalia is better typographically and more original, but its hierarchy is weaker. The baseline's dark card wins the "what do I do right now" glance.

**Mobile:** the sidenotes collapse into numbered "① Negation Station  Open" rows after each paragraph. That's consistent, but it drops the sidenote descriptions, so the margin idea mostly disappears. What's left reads as a long article.

## Carrel: ranked 3rd (67)

**Strongest elements**
- **The most tactile interaction.** In the motion frames, the card stack drags and flings with rotation, and tabs choose the top card. "Mark read" stamps a postmark on the envelope and shows a toast, and the flip clock ticks from 37 to 38. The feedback is well made.
- **A powerful greeting.** The heavy grotesk "Good evening, Ada." on sage is the boldest first impression. Sage, cream and red-orange is a confident palette, and it's distinct from the other two.
- **The most legible calendar cells.** Large day numbers and real event chips, with the session as a black pill, make it the fastest of the three week treatments to read.

**Weakest elements**
- **Too many metaphors.** On one screen: a card stack, a lined index card, a red "DUE TONIGHT" rubber stamp, an envelope with an "1 UNREAD" postage stamp, a flip clock, a ticket stub, a spiral-bound calendar, and a stopwatch "35:00". Each is well drawn, but together they look like a toy desk. The result is less refined, not more. The other two directions each commit to one idea.
- **Hierarchy suffers.** The envelope is almost as big as the task card, and the red accents (stamp, unread, ticket stub, Today) compete for urgency. The eye is pulled to the ticket and envelope as hard as to the task.
- **Wasted space in the main card.** About 40% of its height is empty ruled lines. The envelope uses a large panel for a two-line message.
- **Errors you can see:** clipped tabs, the 900 px seam, and a "1 of 4 Drag the top card aside" helper line floating loose under the card.
- **Messy entrance order.** In the first frame, the countdown and ticket are visible before the card and envelope exist, so the page assembles out of priority order.

**Compared with the baseline:** Carrel is more striking and more interactive, but its hierarchy is worse. The baseline is calmer and clearer about tonight's task.

**Mobile:** the stacking is serviceable, but the flip clock sits alone with its label below it, the envelope eats a full screen, and the decorative weight grows as the width shrinks.

## The baseline (handoff, 2026-10-22)

Its strengths: a clear dark due-today card with a "5 of 12 prompts" readout, a compact right rail (search, Smart Drill, Timed section, Inbox, next session, 38 days), and a Georgia-style serif greeting with an italic *Ada*. It's efficient and correct, but it looks like a generic shadcn layout, with no surfaces, depth or idea of its own. It's the floor all three directions should beat. On distinctiveness, all of them do. On first-glance hierarchy, only Lamplight does.

## What to take forward, and what to drop

**Recommendation:** build on **Lamplight**, and take the typography and margin system from **Marginalia**. From **Carrel**, take only its feedback moments.

**Take:**
1. **Lamplight's swappable main slot** (pick a row, it moves under the lamp). It's the best original idea in the set.
2. **Lamplight's week of windows**, made a bit more legible: brighten the empty windows slightly and use Carrel-size day numbers.
3. **Lamplight's entrance order:** light first, then card, then progress filling.
4. **Marginalia's small-caps run-ins and gutter labels**, used as Lamplight's section lead-ins in place of grey sans captions. This also fixes Lamplight's dim small text.
5. **Marginalia's numbered sidenotes with the hover connector**, as the treatment for the "After this" list next to the lit card.
6. **Marginalia's italic pull quote for Joshua's message**, in place of Lamplight's settings-style box. The message should look written.
7. **Marginalia's tick ruler** in place of Lamplight's full-width "Thirty-eight evenings" section. It says more in a fraction of the space.
8. **Carrel's postmark on "Mark read"**, recast in Lamplight's world (for example, the note dims as if the lamp moved off it). Keep the idea that marking something read leaves a visible mark.

**Drop:**
- Carrel's envelope, flip clock, ticket stub, spiral binding, stopwatch and lined-paper filler. Each is charming, but together they're kitsch, and they cost hierarchy.
- Marginalia as the whole page structure. As prose, the main task never becomes an object you can spot in a second.
- The unbalanced Lamplight layout under the lamp. Fill the left column (for example, the sidenoted "After this" list) or narrow the grid.
- Viewport-sized backgrounds that seam at 900 px.

**If you only get one:** Lamplight. It's the only direction that's striking, original and coherent, and that also improves on the baseline's first-glance hierarchy. Marginalia is the close second and the better reading design. Carrel is the most fun to click, but it's the weakest as a design.

## Limits of this review

- My scores are visual judgements. The measured facts are listed separately above.
- I didn't judge backend completeness, data accuracy or whether actions persist, and none of that affected the scores.
- Teacher pages weren't reviewed.
- I didn't see hover states beyond what the contact sheets show.