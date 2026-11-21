# Teacher side visual direction: Brainstorm / Discovery Notes
Date: 2026-11-18 · Goal: Agree a clear structure and visual direction that makes the LSAT U teacher side calm, beautiful and useful, before building.
Status: in progress
Context sources: brainstorms/2026-11-18-teacher-side-reorganization.md (proposed D1-D7); brainstorms/2026-09-27-teacher-command-center.md; design/principles.md; design/reviews/classroom-quality-20261028/REPORT.md

## Summary / key decisions
(none confirmed yet; D1-D7 are proposals Joshua asked to change)

## Scope (Joshua, 2026-11-18)
- Focus is the **current teacher Home page** (Classroom Home when signed in as Joshua), not the whole teacher workspace. "Make this top tier." It is "chaotic", "not useful", "not organized".
- Joshua wants **the dock bar on the teaching side** (the floating Practice / Booking / Messages / Search bar the student Home has).
- Round 1 questions D1-D7 / Q1-Q6 (earlier draft, about two homes and sidebar) were superseded by this scope before being answered.

## Current-state audit (rendered 2026-11-18)
Rendered from `main` f35eb05 in a dev-only preview (`/dev/teacher-home-preview`, sample data, 1440x900). Not the live signed-in page.
- Page is ~3,350px tall: about four laptop screens of one long stack.
- First screen is a greeting card plus a full-width charcoal "eclipse" animation with a countdown ("Next session in 5 hr 0 min"). The decoration takes most of the first screen; the only work shown is one line ("3 sessions need your follow-up").
- Charcoal is used four times: Assign work button, eclipse panel, "Recaps to finish" tile, Celia's follow-up card.
- Header actions: Assign work, Messages (3), and an oddly full-width "More" pill.
- Three summary tiles (Recaps to finish 3 / New students 0 / Unread 3) repeat sections further down, including a zero.
- The next session appears three times: eclipse orbit label, eclipse caption ("Then Celia Moreno… Thursday"), and Next up.
- Numbered kickers ("01 · FOLLOW UP", "02 · INBOX AND NEW STUDENTS", "03 · STUDENTS") add a fourth layer of labels.
- Lower half is an uneven two-column patchwork: Correspondence beside an empty "New students 0" card, My list half-width beneath, then a mixed "Students at a glance" (recent activity, search, four account actions, recent results).
- An unmatched payment in the sample data (Alex Rivera, CA$240) does **not appear on Home** at all; payment decisions are not visible on the page.
- ↗ arrows on nearly every internal link.

## Q&A log
### Round 1 (superseded draft, not answered)
Questions on two homes, sidebar, first question, week strip, look, density. Replaced by Round 2 after scope narrowed.
### Round 2
#### Q1 - The eclipse
- Asked: keep the charcoal eclipse/countdown on teacher Home or retire it?
- Recommended: retire it for a compact Next session row.
- Captured: **Keep it.** Joshua likes it ("keep it"). Recommendation rejected.
#### Q2 - Teacher dock actions
- Asked: which actions go in the teacher dock?
- Captured: the dock must give "an easy way to go to a question and such" (quick jump to a question). Other dock actions not yet chosen.
- Tentative (agent): "go to a question" = the existing Find a question finder (`QuestionFinder`). Confirm.
#### Q3/Q4 - First screen and payments
- Captured: **No payments on the front page.** "Not necessary, not useful", and he does not want redundancy. Home must be "easy to visually follow".
#### Q5/Q6 - Students at a glance, layout
- Captured (core direction, Joshua's words paraphrased): he does not want "just lists"; the current Home "has no structure", is "just a list". He wants "cool pieces like the globe", "widgets", "visual pieces" and "artifacts" that make it very good, but lacks the exact words. Asked to use grill-with-docs to find shared vocabulary.
- Flags: exact vocabulary for the widget style -> resolve in grill-with-docs glossary round.

### Round 3 - vocabulary (grill-with-docs)
Visual vocabulary board built: `design/prototypes/teacher-home/vocabulary.html` (served locally at /teacher-vocabulary.html). Candidate terms, all **proposed, not agreed**: A Widget (not a list), B Hero instrument, C Bento grid, D Glance tiles, E Progress rings, F Day ribbon, G Card stack, H Score bars, I Face cluster + activity strip, J Tactile, K Dock.
Evidence carried in: design/principles.md says widgets must connect to real teaching decisions; "more installed effects are not themselves useful widgets."
Answers (2026-11-18, Joshua's words where it matters):
- Likes **hero instruments**: "useful, innovative visuals and powerfully useful". "I like heroes a lot especially." Wants "other nifty things".
- Likes **bento grids** "in that mix".
- Likes **score bars** ("some").
- Likes **tactile** ("the idea of tactile").
- **Dock** "is amazing".
- Wants "those kinds of mixes", and wants Claude to "keep asking me visually" about features because he lacks the technical words.
- Not chosen / not mentioned: D glance tiles, E rings, F day ribbon, G card stack, I face cluster. Treat as open, not rejected.
- Glossary terms agreed and written to `design/GLOSSARY.md`: Widget, Hero instrument, Bento grid, Score bars, Tactile, Dock.

### Round 4 - visual choices per feature
Choice board: `design/prototypes/teacher-home/choices.html`. Answered 2026-11-18:
- Q1 **1B**: eclipse hero plus two mini instruments (follow-up gauge, week-load meter). Recommendation accepted.
- Q2 **2A** card stack. Joshua first said after-session work is unclear and he "usually handle[s] that on Claude anyway, so we can remove that", then "actually, do the 2A". Flag: confirm it stays once seen in the full mockup.
- Q3 **Rejected 3B** student cards with score bars: "I don't know what that is useful for." Whether Home shows students at all is open.
- Q4 **4A labelled pill + integrated search field.** Everything "should be able to pop up and be very organized and easy to see"; pop-ups must be "very easy to use" and accessible.
- Q5 **5B** faces with badges.
- Q6 **6B** pressed object. Recommendation accepted (6C dark glass reserved for hero instruments, tentative).

### Round 5 (asked 2026-11-18, awaiting answers)
Q7 students on Home at all; Q8 dock pop-up shape; Q9 which dock buttons; Q10 where the faces sit.
Answered 2026-11-18 (dictation partly garbled):
- Q7 **Students stay on Home**, "but it needs to be like more" than a thin face row. Recommendation (none) rejected. Flag: what "more" means -> Joshua, round 6.
- Q8 **8A** panel rising from the dock.
- Q9 **Keep the four** (Assign work lit, Messages, Calendar, Students) + search, "for now". He suspects it may be too many and will revise after seeing it.
- Q10 **10A** message faces as a bento widget.

### Round 6 (asked 2026-11-18, awaiting answers)
Q11 what the student widget shows.
- Answered: **A + C**: each student's next session with a homework-done dot, plus a highlight for students quiet 5+ days. "Go forward": full mockup at `design/prototypes/teacher-home/home-mockup.html`.

### Mockup feedback (2026-11-18)
- Colour coding (green/yellow/red dots, orange quiet tint, orange bar) "looks like a crayon box". Wants the current sleek, elegant charcoal + near-white scheme. Rule: **status by shape and weight in one ink tone, never by hue.** Applied to the mockup.

## Open flags (pending input)
- Live admin view not inspected on 2026-11-18 (browser pane signed in as student) -> Joshua to sign in as admin on localhost:8133 if live check wanted

### Approval (2026-11-18)
- Joshua approved Teacher Home v2 "observatory" (`design/prototypes/teacher-home/home-v2/index.html`) and strip version A (studio ledger). This is the reference for the LSAT U teacher Home build.
