# RRC demos on the RRC homepage: Brainstorm / Discovery Notes
Date: 2026-09-11 · Goal: Decide how the three Round 7 demo films appear on the Read, Recall, Colour homepage (/activities/sections), which today shows a synthetic looping "Elm Street" demo window, and what happens to the "Watch it done" block shipped on the section briefing page (PR #114).
Status: complete (build starting 2026-09-11)
Context sources: brainstorms/2026-09-10-rrc-instructional-video-round7.md; projects/lsatu/src/features/activity-centre/components/RecallDemo.tsx (synthetic demo on the door); SectionLaunchFrame.tsx (mounts it); SectionDemos.tsx (real demos, briefing page)

## Summary / key decisions
- Synthetic Elm Street window STAYS on the homepage. Real demos are ADDED alongside it (Q1).
- Homepage progress card: show only the last 5 runs, with a link/control to see all of them (Q3). The 23 runs on his account are setup tests, not real recordings.
- REMOVE the "Twenty-five minutes. No going back. Every detail you can still hold." banner with its Choose a section button: "that's not needed" (Q4).
- Any further list of attempts lower on the page collapses to the same 5 as the progress card, with "See more" (Q4). Page is "too crowded".
- Homepage placement DECIDED: the three films go directly under the Steps 1 to 4 cards (Q5), mirroring the briefing page. Not under the Elm Street window.
- "Before you start": cut the four numbered lines, keep the two paragraphs (Q6, yes to suggestion).
- Briefing page: "Watch it done" stays where it is, after Step 4 and above the collapsed long version (Q7, yes to suggestion).
- Section list (PT1.S3, PT101.S2, ... with "Run it again"): show only 5, with a "more" control to reveal the rest (Q7 follow-up). Same rule as the progress card.
- Build list confirmed: films under step cards; progress card capped at 5 + See more; section list capped at 5 + more; close panel removed; Elm Street untouched.

## Q&A log
### Q1 - replace or sit alongside the synthetic demo
- Asked: Do the real films replace the Elm Street window or sit alongside it?
- Captured: "It should sit alongside. Don't eliminate the synthetic Elm Street window." He wants a demo on the homepage in addition to it. On the instructions page the demos "should show below all of the instructions". Repeated twice: do not remove the Elm Street window.
- Tentative / suggested: none accepted; my "replace it" suggestion rejected.
- Flags: none

### Q2 - homepage placement (still open) + NEW ITEM raised by him
- Asked: Where on the homepage relative to the Elm Street window? (suggested: directly beneath it, before the section list)
- Captured: not yet answered. While viewing the page in the in-app browser he raised a new item: the "Your sections" / "Your progress" card lists far too many rows ("Way too many sections! These can be a maximum of 4 to 5 sections for this page."). Screenshot shows 23 graded runs, rows like PT21.S3 · Sep 10, 2026 · 60 min · 97%.
- Tentative: the rows he calls "sections" look like graded RUNS (same PT102.S3 appears twice). Needs confirming whether the cap is on runs shown, or on sections offered.
- Flags: none

### Q3 - the progress card cap
- Asked: cap on runs shown, sections offered, or both?
- Captured: Runs. "This is basically the entry page." Keep the last 5, and he can click a "see all" to view all of them. His 23 runs are from setup only, not real recordings of himself.
- Flags: none

### Q4 - placement, via screenshot of the purple banner
- Asked: where do the films go (suggested: between Elm Street window and Your sections card)?
- Captured: The purple "Twenty-five minutes. No going back. Every detail you can still hold." banner "is not needed". Sentence "put it right under the..." cut off. All attempts listed after the progress bar should be "the same five we have above" with "See More"; "the page is too crowded". Wants an impeccable audit run on the page to see where the videos fit best.
- Tentative: he likely wants the films in or near where that banner sat; unconfirmed.
- Flags: exact anchor for "right under the..." -> Joshua, after the audit


## Impeccable audit of /activities/sections (2026-09-11, live site, 886px wide pane)

Page is 7,126px tall. Order and heights, measured in the in-app browser:

| Block | Top | Height | Notes |
|---|---|---|---|
| Hero (title, CTA, Elm Street window) | 0 | 1,079 | fine |
| "Your progress" card (SectionProgress) | 1,151 | 1,603 | 23 rows, one per graded run, no cap |
| Section list (SectionLibrary) | ~2,750 | 1,613 | 12 sections x ("Run it again" + attempt rows), 11 of them "not finished" test runs |
| "Before you start" aside (MethodSummary) | 4,461 | 322 | repeats the four steps in prose |
| Steps 1 to 4 cards + drawer (rd-method) | 4,783 | 1,210 | the instructions |
| "Your own words, every detail" (rd-counts) | 5,993 | 714 | Retelling / Reciting / Listing |
| Close panel "Twenty-five minutes..." (rd-close) | 6,707 | 420 | he wants it removed |

Findings (crowding first, since that is the brief):
- P1 The two run lists are 3,216px together, 45% of the page, and sit between the hero and the instructions. A new student with 0 runs sees a short empty state; Joshua's test account sees 23 + 13 rows. Cap both at 5 with a "See more" control. Owner already decided this (Q3, Q4).
- P1 The steps come AFTER the section list. Order today is hero, progress, sections, steps, examples, close. "sectionsFirst" was a deliberate choice so returning students reach the list fast, but it puts "what is this" under "your data". Not asked to change; flag only.
- P2 The method is explained three times: Elm Street loop (hero), "Before you start" prose list (aside), Steps 1 to 4 cards (rd-method). The aside is the weakest copy and is candidate for removal if the page needs air. Not decided by owner.
- P2 rd-close panel: a third "Choose a section" CTA (hero has one, section list is the thing itself). Owner: remove.
- P3 Section list uses identical repeated cards (name, 25 min, attempt, Run it again) x 12; reads as a grid. Cap fixes most of it.
- Technical: no a11y, theming or responsive defects found in this pass that bear on the placement decision; sr-only H2s are in order; touch targets on "Run it again" are 44px.

Placement recommendation for the three demo films: directly under the Elm Street window, still inside the hero's dusk world, above "Your sections". Reasons: (1) the films are the real version of what the loop above them just mimed, so adjacency makes the loop read as a sketch and the films as the proof; (2) every other slot is below 1,600 to 3,200px of the student's own run data, where an instructional asset is invisible on a return visit; (3) the rd-close slot he pointed at is at 6,707px, the bottom of the page, and is being removed anyway. Second choice: directly under the Steps 1 to 4 cards, mirroring the briefing page, if he wants the films to be "after the instructions" here too.
