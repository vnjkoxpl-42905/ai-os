# Read, Recall, Colour: full audit, critique and fix plan

Date: 2026-09-09. Method: `$impeccable audit` then `$impeccable critique` over the whole drill: the door (library and section pages), the briefing page, the runner, the handover and marking wait, and the Report Card. Four surfaces, one journey. Evidence: source read in full (about 9,000 lines), the dev server at localhost driven in the in-app browser (lab at `/activity-lab`, harnesses at `/src/dev/section-launch-preview.html` and `/src/dev/report-card-preview.html`), contrast computed from rendered colours through a canvas, and the impeccable 4.1.0 detector on files and rendered URLs. Related: [[RRC-BRIEFING-CRITIQUE-2026-09-08]], [[COPY-CORRECTIONS]], [[ASSIGN-AN-ACTIVITY]].

What was not possible: the browser pane returned black frames for scrolled or emulated screenshots, so below-the-fold and phone checks are DOM-measured rather than eyeballed. The briefing page has no harness and was audited from code. The overlay mode of the detector does not exist in 4.1.0 (`impeccable live` is a variant tool needing a config file), so the rendered-URL scan replaced it. The first-run walkthrough card and the phone "Next stimulus" button are not rendered by the lab.

## Part 1: Audit (technical)

### Scores by surface

| Surface | A11y | Perf | Responsive | Theming | Anti-patterns | Total /20 | Band |
|---|---|---|---|---|---|---|---|
| Door and briefing | 2 | 2 | 3 | 2 | 2 | 11 | Acceptable |
| Runner (stage, ready beat, pause, leave, finish) | 2 | 3 | 3 | 2 | 4 | 14 | Good |
| Marking wait and Report Card | 2 | 3 | 3 | 3 | 3 | 14 | Good |
| **Journey** | **2** | **3** | **3** | **2** | **3** | **13** | **Acceptable** |

Issue counts across the journey: P0 3, P1 16, P2 24, P3 15. The three P0s are copy and flow, not pixels, and they are in Part 2.

### Anti-patterns verdict, per surface

- **Door:** not first-order slop (nobody guesses "LSAT drill, lavender dusk over a meadow"), but caught by the second-order reflex: the editorial-serif, mono-label, pastel-sky, floating-demo-card lane is the saturated one. Countable tells: two identical card grids (four step cards at `section-launch.css:772-830`, three comparison cards at `:1206-1253`), traffic-light window dots on the demo card (`:362-380`), a glass chip with `backdrop-filter` (`:211-225`), a hero-metric stat strip (`:1436-1482`, mitigated by honest data), hover lifts with shadows on three controls (`:286`, `:795`, `:1426`), a drenched gradient closing panel (`:1575`), and the chip restating the H1 verbatim (`SectionLaunchFrame.tsx:279-283`). Also, the door is built on cream, the colour the same owner vetoed for the Report Card as "overdone and too AI looking". That is a brief-level contradiction.
- **Runner:** clean. A deliberate LawHub mirror; familiarity is the feature. The only tells are under the surface: 13 raw slate hex literals in `section.css` and a Helvetica Neue stack that renders as Arial on the Windows laptops students use.
- **Report Card:** pass with two hits. `border-l-2 border-[var(--rc-signal)]` on the next-step sentence (`SectionReportCard.tsx:511`) is the banned side stripe, in the colour the brief reserves for sound. The console header (52px band, stat sentence, three figures) is the hero-metric shape, saved only by the band leading and each figure carrying a sentence. Four nested bordered boxes inside the card (`:318`, `:742`, `:987`, `:1004`).

### P1 findings (fix before the next student runs one)

**Accessibility, measured in the browser**

1. Runner focus ring is `rgb(29 29 31 / 0.35)`: 2.17:1 on white, 2.15:1 on the footer, 1.00:1 on the indigo field where the walkthrough's Hide button sits. `section.css:243`. WCAG 1.4.11 needs 3:1.
2. Runner Pause and Leave are 62x30 and 59x29 on desktop, 54x30 and 51x29 on a phone, and the phone rule shrinks their padding further. `section.css:73-109`, `:262-270`. PRODUCT.md binds 44x44 by being that size.
3. Runner ready-beat countdown "Starting in 3" is `#94a3b8` on white, 2.56:1 at 13px. `section.css:523`.
4. Runner Pause button border `#cbd5e1` on white is 1.48:1, the control's only boundary.
5. Leave dialog has `aria-modal` but no focus trap and no Escape: three Tabs land on the page behind it; Escape leaves it open. `SectionStage.tsx:275-300`.
6. Runner has zero headings; "Stimulus 1 of 23" is a span. Report Card has zero headings and unnamed sections; the 52px band label is a `p`. `SectionReportCard.tsx:489-497`.
7. Door demo play button is 28x28 and its focus ring is white on paper, 1.05:1, and it is the first Tab stop on the page. `RecallDemo.tsx:170-178`, `section-launch.css:330, :423`.
8. Door crumb "Library" (the exit) is 55x17. Drawer tabs are 43px. `section-launch.css:185-197`, `:1063-1077`.
9. Door demo step label carries `aria-live="polite"` inside a loop that cycles every 1.5 to 4.2 s for as long as the page is open. `RecallDemo.tsx:163-165`.
10. Door heading outline is H1, H3, H2 (H1, six H4, H2 with the drawer open). `SectionLaunchFrame.tsx:346, 429, 455, 502`.
11. Report Card ticks 30x45 at 1180 and 29x45 at 375; transport 34px; Hear it, Previous, Next 26px; summaries 16px; dispute link 16px. `report-card.css:119-131, :229, :356`; `SectionReportCard.tsx:743, :804, :1185`.
12. Run-history band inks fail AA: 3.79:1 and 3.85:1 on the lab ground, 4.24 and 4.31 on the Workroom page, and the band is colour-only. `SectionRunHistory.tsx:48-53`.
13. Handover subtitle `#64748b` on the warmed ground is 4.17:1. `section.css:645`.
14. Ledger ticks expose only "Stimulus N"; band, recital and ungraded state are invisible to a screen reader. `SectionReportCard.tsx:659-673`.

**Correctness**

15. Focus-set chips are off by one: `(s.item_order ?? i) + 1` on a 1-based `item_order`, so "Stimulus 5" names stimulus 4 everywhere else on the card. `SectionReportCard.tsx:1257`. Unrendered by harness and lab.
16. Upload-failed flow: when the recording fails to upload but the rows saved, `onComplete` fires at once, so the sentence "Your recording did not reach us, open this section again from the same browser" is replaced within a frame by "Marking your run", and three minutes later by "Still being marked, it will be here when you come back", which is false until she reopens the section in that browser. `SectionRunner.tsx:1030-1040`, `SectionReport.tsx:86-89`.

**Performance (door)**

17. 191 to 196 animations run at rest, 170 of them per-path transforms on grass blades inside one `will-change` layer, plus the demo's `setInterval` and per-frame typewriter, none gated on visibility. `section-launch.css:147-157`, `MeadowScene.tsx:203-216`. A scroll-interpolated `blur(14px)` on the 96px headline layer. `SectionLaunchFrame.tsx:181, :277`.

### P2 findings (next pass)

- Runner: `section.css` has 13 distinct slate hex literals beside its 7 tokens; `.ac-section` is not recorded as a sanctioned world in DESIGN.md or the surface brief, and DESIGN.md's question lock says Outfit while the runner mirrors LawHub's Fraunces. Record or code needs a ruling. `.is-finishing` copies `hsl(38 36% 93%)` by value.
- Runner: the goal is never on screen. The CSS for a lighter goal beside the clock (`section.css:283-286`) is dead; the stage only renders elapsed. She cannot pace against a target she cannot see.
- Runner: the ready beat says "Say something to check your microphone" but lasts 3 s and does not wait for a level; dead input is reported only after two silent windows of 8 s or more.
- Runner: `kbd space` hint still renders on a coarse pointer beside the on-screen button.
- Runner: the walkthrough's coach-step labels are 0.66 and 0.68rem, under the 11px floor.
- Marking wait: no `role=status`, no elapsed time, no re-ask after the 3-minute give-up, no way to tell Joshua, and a permanently refused grade is indistinguishable from a slow one. `SectionReport.tsx:64-137`.
- Report Card: four `role=status` nodes mount with their text already present, so most readers announce nothing. `:728, :1170, :1178, :1272`.
- Report Card: raw judge enum "partial" rendered in "The whole thing, text off screen: partial". `:1006`.
- Report Card: "run" and "try" in student copy where CONTEXT.md says Attempt. Ten uses across three files.
- Report Card: body lines measured at 89 to 117 characters despite the 72ch measure; some column escapes it.
- Report Card: 22 ticks are 22 Tab stops before any content; roving tabindex would make it one.
- Report Card: transport and pill borders at 1.25 and 1.28:1 against PRODUCT.md's 3:1 boundary rule.
- Door: 30 hex and 28 rgba literals outside the token block; `#cfc9bd` seven times unnamed; `#e3ded2` and `#2a2450` used raw where tokens exist.
- Door: control edges at 1.32:1 (`.sl-close`, attempt rows, demo button).
- Door: hero is 1216px tall on a 375x812 phone; the demo card is cut at the fold; page height 6,186px on the section page.
- Door: on a phone the four step cards are tabs whose shared panel sits about 1,500px below; tapping Step 2 gives no visible feedback.
- Door: 57 bare `.sl-*` rules in a global bundle; `.sl-drawer` is also a Specimen Lab class.
- Briefing: `h2` inside `summary` (the 2026-09-08 Sam finding, still open); "Press space" shown to coarse-pointer users; `useNoKeyboard` is not used on this page.
- Sub-11px labels throughout: 15 instances at 10px on the card, 4 to 8 at 10.5px on the door, a 9px mono label at `report-card.css:147`.

### P3 (if time)

Em dashes in unrendered error branches (`SectionProgress.tsx:48, :68`; `SectionReportCard.tsx:1273`); duplicate selectors and dead rules in `section-launch.css` (`.sl-dr-note`, `.rd-method-head`, briefing `.sl-chip`); `will-change` on the static grain layer; `.rd-meta` hidden under 640px so phones lose the clock; "Read, Recall, Colour" three times in the first viewport; console.error on the expected failed-history state; whole-card re-render on every audio `timeupdate` (`SectionReportCard.tsx:138`); stop affordance lost when navigating while a clip plays (`:466, :710`); shadcn Button inside `.rc` takes the corridor's emerald; the lab passes no `onAdvance` so the phone button cannot be looked at.

### Positive findings, keep these

- Runner footer contract: left says what she is doing, right says what Space does next, and it is true in every state (verified: working, recall, beat, paused).
- Leave dialog copy names the cost in her own elapsed time and defaults to Keep going.
- Every failure copy tells the truth about whose fault it is (mic refused, upload failed, "the marking is wrong, not you").
- Reduced motion is handled at three layers on the door and blankets the card and the handover.
- Text contrast inside `.rc` is measured and true (lowest 5.63:1); door text is lowest 4.79:1.
- Only the open stimulus renders on the card: 223 elements for 22 stimuli, one lazy audio element.
- Keyboard model on the door's tablists is correct: roving tabindex, arrows, Home, End, live `aria-labelledby`.
- No horizontal overflow at 375, 768 or 1280 on any surface.
- The stimulus leaves the DOM during recall and during a pause, so a screen reader cannot read what she is meant to have looked away from.

## Part 2: Critique (design)

### Design health score (journey)

| # | Heuristic | Score | Key issue |
|---|---|---|---|
| 1 | Visibility of system status | 3 | Runner exemplary. The marking screen polls silently, then "Still being marked" with no time and no path. |
| 2 | Match system / real world | 2 | "Read" means step 1 on the door, step 4 on the ready beat, "found the move" on the card. "The move" is never defined before the card. |
| 3 | User control and freedom | 2 | Pause exists and works; every pre-run surface says it does not. No resume after refresh. Done is the only action while marking. |
| 4 | Consistency and standards | 1 | Three definitions of Colour, two names for step 4, silent vs out-loud reading, "No pause button" vs a Pause button, "91% carried" on the door vs no arithmetic on the card, three type systems, four labels for Start. |
| 5 | Error prevention | 3 | Leave confirm, mic gate, dead-input detection, phone warning. Gap: the walkthrough coaches the faults the judge penalises. |
| 6 | Recognition rather than recall | 3 | The card asks her to recognise "a Read", "the move", "coloured", which the door never taught under those names. |
| 7 | Flexibility and efficiency | 2 | The section page re-scrolls the whole method on run four; 3 s beat cannot be skipped; 22 tab stops on the card. |
| 8 | Aesthetic and minimalist | 3 | Runner near perfect. Chip restates the H1; counts row restates the drawer; card console is a stat block. |
| 9 | Error recovery | 2 | Upload and mic copy is excellent. A slow or refused grade has no recovery path; that is the shape of the 8-hour incident. |
| 10 | Help and documentation | 3 | Plenty of help; it contradicts itself. |
| **Total** | | **24/40** | **Acceptable** |

### Anti-patterns verdict (combined)

Design review and detector agree on: the chip restating the H1, the two card grids, the side stripe on the card, the hero-metric console, the hover lifts, sub-11px labels, and the three em dashes in unrendered branches. The detector added: white and apricot text over the `#a89fe0` gradient stop measuring 2.4:1 and 2.0:1 on the tell diorama and the closing panel (`section-launch.css:843, :1575`), hero copy over the meadow SVG at 1.1 to 1.6:1 median on the tagline, and the 89 to 117 char lines on the card. Detector false positives: the playhead bar flagged as a side tab (`report-card.css:278`, functional, only while playing), and every font-size and colour finding inside the two sanctioned worlds. Note `section-launch.css` is on the detector's ignore list, so its static findings never surface; only the rendered scan catches them.

### Cognitive load

Door library 3 of 8 fail (moderate); door section 3; briefing 1; runner 1 (the strongest surface); marking 0 but nothing to decide; Report Card 4 (critical, partly intrinsic: six movements per stimulus plus three figures plus a list plus 22 ticks plus terms the door never used).

### Emotional journey

Calm on the door, then the largest type below the hero, at the decision point, is "Twenty-five minutes. No pause button." and it is false. The briefing lowers her shoulders well. The ready beat asks her to read 30 words in 3 seconds under a heading that says "Recording now" beside a clock at 0:00, which is the first contradiction she meets inside the drill and the class of the 37-minute incident. The run is the best part. The end, after 25 unbroken minutes, is three grounds in ten seconds (cream, shell chrome, plum), a static "This takes a minute", and if the grade is slow, "Still being marked" with a button labelled Done at 9:29pm and a flat "Check back shortly" in the library. A perfect run gets the same headline as a faulty one. Peak-end rule: the peak is the run; the end is a shrug.

### Priority issues

**[P0] The product says she cannot pause, then gives her a Pause button.** Five denials (`SectionLaunchFrame.tsx:553`, `SectionLibraryLaunch.tsx:58`, `SectionLaunch.tsx:329`, `SectionBriefingPage.tsx:143`, `instructions.json rules[0]`, plus `coach.ts:90` "no stopping") against a working Pause shipped in d3c096f. Decide which is true; if Pause stays, one sentence about what it does, rendered from one source. `$impeccable clarify`.

**[P0] Four surfaces teach three methods.** Step 1: "Read silently" (door, JSON) vs "Read it, out loud in pieces" (`coach.ts:62`) vs the card scolding her for reading aloud. Step 3: "React. A doubt, a joke" (door) vs "what that piece is doing in the argument, evidence, conclusion" (`coach.ts:62`), which is the pasteable label the judge marks as "no reaction of your own". Step 4: "The Recall" (door) vs "your Read" (`SectionStage.tsx:421`, a retired name per ADR 0012 and CONTEXT.md) vs "Your Read" and "the move" on the card. The walkthrough is shown only to first-timers and coaches them into the two faults the card then lists. One JSON renders the step names and one-line definitions on all four surfaces. `$impeccable clarify`, then `$impeccable document`.

**[P0] The ending has no design when the grade is slow or missing.** After 3 minutes: "Still being marked", a Done button, then a flat library row. No elapsed time, no estimate, no notification, no way to tell Joshua, no way to re-ask, and a refused grade looks the same as a slow one. This is the exact face of the 8-hour incident. `$impeccable harden`.

**[P1] Three grounds in ten seconds at the handover**, driven by a stale comment that still calls the card "warm paper". Warm toward `--rc-page`; render the marking wait inside `.rc`. `$impeccable polish`.

**[P1] Numeracy policy differs by surface.** "Held 82%" on the console and "91% carried" in the library against "no Detail arithmetic" on the stimulus; "Recalled 73/75" on the door counts recordings, not recall; the Time verdict keys off `within_time` while the number shown is elapsed (harness shows 28:32 "Inside the time" and 24:00 "Over the goal"). Pick one policy. `$impeccable distill`.

**[P1] Em dashes and raw palette.** `coach.ts:62, 67, 80, 85`; `SectionReportCard.tsx:1273`; `SectionProgress.tsx:48, 68`; 13 slate literals in `section.css`. `$impeccable polish`.

**[P2] The ready beat.** 30 words in 3 seconds, the retired term, "Recording now" before the clock. Make it "Microphone on. Starting in 3." plus the level bar; move the sentence to the briefing foot. `$impeccable distill`.

**[P2] Card console.** Hero-metric block, side stripe in the signal colour, 22 tab stops, 28px ticks. Lead with the band and Next time; demote the figures to one line; roving tabindex; 44px ticks. `$impeccable layout`.

### Persona red flags

- **Alex (fourth section):** re-scrolls the full method every visit (only the library is `sectionsFirst`); cannot skip the beat; no Held trend anywhere; 22 tab stops.
- **Jordan (first-timer):** told to read silently, then out loud, then scolded for out loud; Colour defined two ways then graded a third; "given your Read" and "the move" undefined; the beat paragraph unreadable; "Check back shortly" with no time. She will assume she did it wrong.
- **Sam (screen reader):** runner good (Space on the document, status on the instruction, stimulus removed on recall). Red flags: the demo's perpetual live region, a dialog that does not trap focus or close on Escape, no headings on the runner or the card, ticks that say nothing about the band, 10px labels.
- **Casey (phone):** warned and let through, correctly. Pause is in the top rail out of thumb reach; the hero is 1.5 screens; step taps update a panel 1,500px away; `.rd-meta` with the clock is hidden under 640px; a Surface with a keyboard also gets the phone treatment because `pointer: coarse` matches touch laptops.
- **Riley (stress):** refresh or close loses the run with only the generic prompt; browser Back on an SPA route may unmount the runner without the Leave dialog (not verified, must be); mic denied and upload failed are handled; grade never arrives is unhandled; the upload-failed sentence is overwritten within a frame.
- **The 9pm paying client:** "How long?" Nobody says budget 40 minutes (mic prompt, beat, 25 to 28 minutes, 1 to 3 marking, ten minutes reading the card). "Can I stop if my roommate walks in?" Four surfaces say no; the button says yes.

### Questions to consider

1. If the runner honestly has a Pause, why is "No pause button" the largest line above Start? Which one is the drill?
2. What if the door's step cards, the briefing list and the walkthrough card were one component fed by one JSON, so the method could not drift?
3. Does the console need "Held 82%" when the per-stimulus copy already decided arithmetic is the wrong unit? What does the card look like if it opens with Next time?
4. What should she see at 9:31pm when marking has not come back, what should Joshua see, and is the Sweep visible to either of them?
5. Is the marking wait the last screen of the drill or the first screen of the shell? It is dressed as the shell in the middle of the drill's world.
6. The runner `.ac-section` is a LawHub mirror that no record sanctions, and DESIGN.md's question lock says Outfit. Is the mirror the rule for RRC, and should the record say so?

## Part 3: Fix plan

Ordered so each step is safe on its own and the student-facing truth is fixed first. Every step ends with `npm run typecheck` and the Activity Centre tests; the copy steps also need `npm run content:push` because `rules[0]` lives in Postgres (see [[lsatu-content-lives-in-postgres]]).

**Step 1. One truth about pausing (P0, copy only, one hour).** Decision needed from Joshua: keep Pause. Assuming yes: replace the six statements with one sentence, "You can pause. The text hides and the clock stops while you are away, and you cannot go back to a stimulus." Files: `SectionLaunchFrame.tsx:553`, `SectionLibraryLaunch.tsx:58`, `SectionLaunch.tsx:148, :329`, `SectionBriefingPage.tsx:143`, `coach.ts:90`, `instructions.json rules[0]` then `content:push`. Add a test that greps rendered door and briefing text for "cannot pause" and "No pause". `$impeccable clarify`.

**Step 2. One method, one source (P0, half a day).** Put the four step labels and one-line definitions in `read-recall-colour-section.instructions.json` only, and render them in `SectionLaunchFrame` step cards, `SectionBriefingPage` list, and `coach.ts` walkthrough. Rewrite `coach.ts` WORKING[0] to "Read it silently, a piece at a time. Look away, tell it back, then react to it." Rewrite `SectionStage.tsx:421` to "once when you have read it all, once when you have recalled it." On the card, use "The Recall" for the step and define "the move" once in the console before using it. Remove the four em dashes from `coach.ts` in the same edit. Add the CONTEXT.md avoid-list as a test over rendered copy. `$impeccable clarify` then `$impeccable document` to update CONTEXT.md and the surface brief.

**Step 3. The slow-grade ending (P0, one day).** `SectionReport.tsx`: `role=status` on the copy; minutes elapsed and "usually 1 to 3 minutes"; after give-up, "Check again" restarts polling, "Back to the library" replaces Done, and the copy says the marking continues in the background. `SectionLibrary` row for a completed-but-ungraded attempt becomes a link back to this screen with "run at 21:03, marking since 21:29". Add an inbox message on grade completion (server side, `grade-rrc-section`) and a "Tell Joshua" draft with the attempt id. Fix the upload-failed race in `SectionRunner.tsx:1030-1040`: when `uploadFailed`, do not call `onComplete`; keep the finished screen with the recovery sentence and the exit button. Schedule the sweeper or run `scripts/rrc-ungraded.ts` daily until it is (ADR 0021). `$impeccable harden`.

**Step 4. Runner accessibility (P1, half a day).** `section.css`: focus ring `2px solid var(--sec-ink)` offset 2 on paper and a cream ring on the indigo field; Pause and Leave `min-height: 44px` with padding, and keep 44 on the phone rule; ready-count and handover subtitle inks at 4.5:1 (`--sec-chrome`); Pause border `--sec-chrome`. `SectionStage.tsx`: Escape closes the confirm, Tab is trapped inside it, `inert` on the paper while it is open; a visually hidden `h1` "Read, Recall, Colour, PT105 Section 2" in the header; hide the `kbd` hint when `noKeyboard`. Show the goal beside the clock (the dead CSS at `section.css:283` already styles it): "12:34 of 25:00". `$impeccable harden`, `$impeccable clarify`.

**Step 5. Report Card correctness and structure (P1, one day).** `SectionReportCard.tsx:1257` off-by-one; heading outline (h1 band, h2 stimulus, h3 movements, `aria-labelledby` on sections); tick names carry band and state; one always-mounted status region; roving tabindex on the ledger; 44px on ticks, transport, pills, summaries, dispute; remove the `border-l-2` stripe at `:511`; flatten the four inner boxes; map `recall.verdict` to words; "Attempt" for "run"; fix the 72ch escape. Tokenise `SectionRunHistory.tsx` band inks at 4.5:1 on both grounds and add a band word. `$impeccable harden`, `$impeccable distill`, `$impeccable colorize`.

**Step 6. Door accessibility and performance (P1, one day).** `RecallDemo.tsx`: drop `aria-live`, 44px play button with an ink focus ring inside the card, `tabIndex=-1` or move the scene after the copy in DOM order. `SectionLaunchFrame.tsx`: 44px crumb, 44px drawer tabs, H2 on method, slab and close, H3 drawer title, essay headings H3. `MeadowScene.tsx` and `section-launch.css`: gate every loop on visibility (`whileInView` or `animation-play-state`), sway a few groups instead of 170 paths, drop or cap the headline blur at 4px, take `will-change` off the grain. Fix the two gradient-stop contrast failures (`:843`, `:1575`) by darkening the bottom stop or moving the text off it. `$impeccable harden`, `$impeccable optimize`.

**Step 7. Handover and the numbers (P1, half a day).** `section.css:612`: warm to `--rc-page`; update the SectionRunner comment; render the marking wait inside `.rc`. Decide the numeracy policy with Joshua: either the section figure is allowed (say it identically on door and card, rename "Recalled" to "Recorded") or the console leads with band and Next time. Reconcile the Time verdict to the number shown. `$impeccable polish`, `$impeccable distill`.

**Step 8. Ready beat (P2, one hour).** "Microphone on. Starting in 3." with the level bar; the sentence moves to the briefing foot; hold the beat until the level has moved once or 6 s, whichever is first, so "check your microphone" is a real instruction. `$impeccable distill`.

**Step 9. Door quieter and tokens (P2, half a day).** Remove the three hover lifts, the traffic-light dots and the glass chip; 3:1 edges on `.sl-close` and attempt rows; name `#cfc9bd`, `#d9d3c6` and the shadow rgba values as `--rd-*`; replace the four raw values that already have tokens; scope every rule under `.sl`. `$impeccable quieter`, `$impeccable colorize`.

**Step 10. Phone door (P2, half a day).** Cap the phone hero (`min(760px, 70svh)`), keep `.rd-meta` visible under 640px, render step bodies inline on one-column layouts, add the on-screen-control sentence to the briefing for coarse pointers, and consider `pointer: coarse and (hover: none)` so touch laptops keep the keyboard path. `$impeccable adapt`.

**Step 11. Records (half a day).** DESIGN.md and the surface brief: add the runner `.ac-section` as a sanctioned LawHub mirror or change the code; note the Outfit question lock exception; note that the door's cream is the owner's deliberate exception to his own card ruling, or change it. Add a detector waiver with reasons for the `.rc` ramp so the 19 advisory findings stop resurfacing. Give the lab an `onAdvance` so the phone button can be seen. `$impeccable document`.

**Step 12. `$impeccable polish` last**, then re-run `$impeccable audit` and `$impeccable critique`. Target: journey audit 17/20, critique 32/40.

## Decisions, 2026-09-09

Joshua answered the three open questions.

1. **Pause stays, and the copy tells the truth.** Not a code change. The six statements say what a pause actually does.
2. **Percentages are allowed, per stimulus and at section level.** Step 7 keeps the section figure. Say it identically on the door and the card, and rename "Recalled" to "Recorded" so the number means what it says.
3. **The runner's LawHub mirror is sanctioned.** Step 11 records `.ac-section` in DESIGN.md and the surface brief as a deliberate mirror, with the Outfit question lock noted as an exception, and tokenises the 13 raw slate hex literals as `--sec-*`.

## Step 1: done, 2026-09-09

One sentence now carries it everywhere she reads before she starts: "You can pause: the text hides and the clock stops while you are away, and you cannot go back to a stimulus."

- `SectionLaunch.tsx:329`, `SectionLibraryLaunch.tsx:58`, `SectionBriefingPage.tsx:143` and `instructions.json rules[0]` carry the full sentence.
- `SectionLaunchFrame.tsx:553` closing line is now "Twenty-five minutes. No going back." `coach.ts:90` says "You can pause if you have to, and you cannot go back."
- `instructions.json rules[5]` dropped "No breaks", which the Pause button had made false.
- Guard test: `src/features/activity-centre/pause-copy.test.ts`, 8 assertions. It fails the build on any of "no pause", "cannot pause", "never pauses", "does not pause", "no stopping", "no breaks" in the six surfaces, comments excluded, and it requires the three clauses on the four pre-start surfaces. If Pause is ever removed, delete that file in the same commit.
- `SectionBriefingPage.test.tsx` foot assertion updated from `does not pause` to the three clauses.
- `npm run content:push`: 65 rows updated, 13 activities and 52 open assignments. The 13 completed attempts were left alone, so no student's finished record changed. `content:diff` re-run confirms the database matches the file.
- Verified live in the browser at `section-launch-preview.html?state=runs` and `?state=library`: both asides render the new sentence, the closing line reads "No going back", and a regex sweep of the rendered page finds zero denial phrases.
- `npx tsc --noEmit` clean. The activity-centre suite is 2717 passing; two `worlds/` stage tests time out only when two vitest runs compete and pass in isolation, unrelated to this change.

## Step 2: done, 2026-09-09

Commit `1cd268f`, "RRC: one method, one source".

The four step names and a new one-line definition each are authored only in `read-recall-colour-section.instructions.json` and read through `recall/method.ts`. The door step cards, the briefing list, both "Before you start" asides and the walkthrough card now render from that one place.

- The walkthrough stopped coaching the two faults the card marks. It told a first-timer to read out loud, when step 1 is silent, and to say "what that piece is doing in the argument, evidence, conclusion", which is the pasteable label the judge refuses to count as a colour. It now states the four steps as a list, from the source.
- The asides were hand-written prose and had drifted into "say it back", step 2's retired student label. They are now `MethodSummary`, rendered from the source, above the four step cards.
- The fourth step is The Recall wherever it is named. The ready beat said "once when you have given your Read", which is the retired step name and not what that Space press does.
- "The move" was used on the Understood figure and every Your Read movement and defined nowhere. It is now said once, above the figures, where it also introduces the two numbers.
- Four em dashes out of `coach.ts`. "The retelling", internal vocabulary, off the card.

### Two corrections to this note's own audit

**The card's "Your Read" is not a violation, and Part 2 was wrong to call it one.** ADR 0025 (2026-09-03) is later than ADR 0012 (2026-09-01) and reinstated The Read as the second graded number: the reasoning half, against Coverage's memory half. They fail differently and the card is right to name both. Collapsing "Your Read" into "The Recall" would have erased the distinction the second number exists to make.

The cause was a stale record. `CONTEXT.md` listed "The Read" under The Recall's avoid-list as a retired name and never defined it anywhere, so every reader of the record, including this audit, concluded the card was using a dead term. CONTEXT.md now defines **The Read** and **the move** as their own entries, and a test pins The Read and The Recall apart.

**The authored rubric named the wrong half.** `coach.rubric[6]` read "Score The Recall against the captured key for that stimulus", which points the memory step at the reasoning key. ADR 0025 quotes that same sentence as "Score The Read". Restored. Nothing live was mis-graded: `grade-rrc-section` builds its own prompt and never reads `coach.rubric`, so the judge and `BAND_FLOOR` (ADR 0035) are untouched and no census re-run is needed.

### Verification

- 103 test files, 2739 tests, all passing. `npx tsc --noEmit` clean.
- New guards: `recall/method.test.ts` holds every surface to the authored steps and the CONTEXT.md avoid-list; `recall/SectionStage.coach.test.tsx` renders the walkthrough card, which the Activity Lab does not render and which is how it ran three stimuli deep into the wrong method unobserved.
- Browser: the door aside renders the four numbered steps from the source with zero retired vocabulary on the page; the Report Card defines the move at index 93 and first uses it at 364.
- `content:push`: 13 activities and 52 open assignments, 13 completed attempts left alone, `content:diff` confirms sync.

### Note on the repo

Another writer is committing to `projects/lsatu` on `main` during this work: `aa6bb7e`, `7471665`, `8ff610a`, `afb15a3` plus a merge and two Lovable "Changes" auto-commits landed alongside these two steps, and files outside the RRC area changed under the session. Nothing collided, and both RRC commits are intact on `origin/main`.

### Not yet deployed

Both steps are on `main`, which builds a Lovable preview only. The instructions text reached students the moment `content:push` ran, but the door, briefing, walkthrough and Report Card copy live in code and still show the old wording on lsatprep.study until a `deploy_project`.

## Step 3: done, 2026-09-09

Commit `3d3d999`, "RRC: an ending for the run the grader is slow to mark". The third P0.

- The marking wait says how long it has been, so four minutes and four hours stop looking identical. Both states sit in one `role="status"` region; neither was announced before.
- "Check again" restarts the polling and the ask, so the give-up is recoverable instead of terminal. The other button says where it goes rather than "Done" on a card she was never shown.
- Past the give-up she gets the run id, the one thing she could not produce herself.
- The section library row says the age: "marking for 4 minutes", or "finished 21:29, still being marked". Past ten minutes it stops saying "Check back shortly" and says "Open it and check again", which is a real instruction now that the screen has one.
- The upload-failed race is fixed. `onComplete` fired on `missingRows === 0` alone, so a run whose answers saved and whose audio did not was handed to the marking screen, overwriting its own recovery sentence within a frame and then promising a card that was never coming. The gate is now whether the recording landed; it no longer asks for a grade there is nothing to grade; and the exit stopped depending on unsaved *answers*, which had left the recording-only failure with an instruction and no button.

**A design decision worth keeping.** "Tell Joshua" is a sentence, not a button. Gating a button on `has_chat_access` means mounting `useUserPermissions`, which redirects on a lost session, into the one screen whose whole job is to stay put while a grade lands. Passing it through the caller moved the same dependency into `ActivityRunner` and broke 49 of its tests. That is the seam saying no, and the sentence does the job.

### Verification

- 103 test files, 2748 tests, all passing. `npx tsc --noEmit` clean.
- `scripts/rrc-ungraded.ts` run read-only: every finished section older than ten minutes has a complete Report Card, 13 checked. Nobody is stuck today.
- The marking screen has no browser harness and needs a real ungraded assignment to reach, so it is proved by ten render tests rather than eyeballed. Not fabricating a stuck run on his server.

### Deferred from Step 3, both needing a production action rather than a push

- The server-side inbox message when a grade lands. It is an edge-function change, and edge functions do not deploy from a push.
- Scheduling `sweep-rrc-grading` (ADR 0021). Until it is scheduled, `scripts/rrc-ungraded.ts` is still the only thing that finds a refused run, and its header now says so.

## Step 4: done, 2026-09-09

Commit `8120fdf`, "RRC: what the drill room owed a keyboard". First P1 step.

- **The focus ring was invisible.** Graphite at 35 per cent is 2.17:1 on the paper and 1.00:1 on the indigo field, where the walkthrough's Hide button sits. Now solid ink, measured in the browser at 17.74:1 on the paper, with a paper ring on the field at 17.35:1. WCAG 1.4.11 wants 3:1.
- **The leave dialog now does what `aria-modal` claimed.** Escape closes it and Escape means keep going; Tab is trapped; the rest of the screen goes `inert`. The other half was in the runner: the Space handler had no guard, so with focus behind the dialog the drill kept advancing underneath a question about throwing the run away. A focus trap alone would not have caught that.
- **44px pointer targets, 46px rail.** Pause and Leave are 62x30 and 59x29, wide enough already and short only in height. Given as a centred overlay rather than `min-height`, because the rail is a grid row and growing the controls grows the header, which went 46px to 96px once before. Measured live: 44px hit box, visual size and rail height unchanged.
- **The goal is on screen.** `.ac-section-clock i` had been styled for it since the clock shipped and nothing ever rendered it, so she paced a 25-minute section against a target she could not see. Reads "12:34 of 25:00", against her own goal so an accommodation is not paced against the standard one.
- A visually hidden `h1` on a screen whose heading list was empty. Ready countdown off `#94a3b8` (2.56:1), handover sentence off `#64748b` (4.17:1 on the warmed ground it lands on), Pause border off `--sec-rule` (1.48:1, and the control's only boundary): all now `--sec-chrome` at 10.35:1. No "space" hint on a device with no Space key.
- The Activity Lab gets the section name and the goal, without which those two were the only things on this surface nobody could look at.

### Verification

- 104 test files, 2759 tests, all passing. `npx tsc --noEmit` clean. New file `SectionStage.a11y.test.tsx`, 9 tests.
- Measured in the running app: hit boxes 44px, Pause border `rgb(51 65 85)`, clock "12:34 of 25:00", heading "Read, Recall, Colour, PT105.S2", and the three contrast ratios above computed in the page.
- Scrolled screenshots come back blank from the browser pane, as in the audit itself, so these are DOM-measured rather than eyeballed.

### Note on the dev server

The old `lsatu-dev` on port 60738 died with the previous session. Restarted under the same launch config; it now serves on **50772** (8080 was in use, autoPort).

## Step 5: mostly done, 2026-09-09

Commit `b1a3f37`, "RRC: the Report Card says what it means, and can be read by keyboard".

- **The focus set named the wrong stimulus.** `item_order` is the authored position and 1-based, which is how the ledger, the open stimulus and its heading all read it; the chips read it as `(item_order ?? i) + 1`. She was sent to run stimulus 15 again over a fault in 14, with the ledger beside it disagreeing. Nothing tested the focus set at all, which is how it shipped. The new test is mutation-checked: put the bug back and it fails with "Stimulus 12" where 11 was meant.
- **The card had no heading of any kind.** The two lines that were already the title become one `h1` rather than a third being invented, so the pixels do not move; the open stimulus is the `h2` its movements hang from, and the movements are `h3`. Verified in the browser: starts at h1, ten headings, no skipped levels.
- **The ledger was twenty-two tab stops.** Now a toolbar with a roving tabindex: Tab lands on the open stimulus, arrows move, Home and End go to the ends, focus follows selection. Its ticks said only "Stimulus N", so band and recital were carried by colour and shape alone.
- **Run history band inks** were 3.79 and 3.85 on the lab ground, 4.24 and 4.31 on the Workroom page, colour-only. Darkened and measured live: 5.53/6.34, 5.35/6.13, 6.26/7.17, with the band said in a word.
- The `border-l-2` side stripe is gone. Transport pills 34px to 44px. "Hear it" and the disclosure summaries take the runner's centred-overlay target, since both sit inline and cannot grow their boxes.

### Left undone in Step 5, not claimed

The always-mounted status region, mapping `recall.verdict` to words, "Attempt" for "run", the 72ch escape, and flattening the four nested bordered boxes.

### A product call, not a CSS one

The ledger ticks stay under 44px **wide** deliberately. Twenty-two to twenty-six of them at 44px is 968 to 1144px inside an 820px card. They are 44 tall and clear WCAG 2.5.8's 24x24 with their gaps; meeting PRODUCT.md's stricter 44x44 would stop the ledger being a single-glance picture of the run, which is the whole point of the surface.

**Answered 2026-09-09: leave them.** Joshua's call. `PRODUCT.md` now carries the carve-out, so a future audit reads this as settled rather than as an open defect: a dense row of marks that exists to be read at a glance is the one place the house standard yields.

### Verification

104 test files, 2767 tests, all passing. `npx tsc --noEmit` clean.

### The other writer pushed this one

`b1a3f37` reached `origin/main` without me pushing it: the concurrent session committed `776f69b` and `ece5480` (practice-test clock work) on top and pushed all three together. Same hazard as `afb15a3` earlier, in the other direction. Every commit in this run is authored "Joshua Fisseha", so authorship does not separate the two sessions. If both are going to run at once, they need separate branches.

## Deployed to production, 2026-09-09

`deploy_project` on Lovable project `53b9a6f2-aba7-4ae4-8dd1-fa5b8aab4d76`, deployment `f7c537b2-0da8-4a7c-8ad2-241b613cfa06`. Fired only after `get_project` reported `latest_commit_sha` `b1a3f376…` (Step 5) with status `ready` and no error, so the build was not one commit behind.

**Verified against the live site, not assumed.** The production bundle hash moved from `index-BSzneK4F.js` to `index-Bv9106bQ.js`. All 375 JS chunks and all CSS chunks were pulled from lsatprep.study and searched:

| Marker | Step | Live |
|---|---|---|
| "You can pause: the text hides" | 1 | yes, twice |
| "Nothing is spoken yet." | 2 | yes |
| "The move is what an argument runs on" | 2 | yes |
| "marking carries on whether or not you stay" | 3 | yes |
| "quote this run" | 3 | yes |
| "once when you have given The Recall" | 4 | yes |
| "The run, stimulus by stimulus" | 5 | yes |
| `2px solid var(--sec-ink)` | 4 CSS | yes |
| `ac-section-coach-steps`, `sl-aside-steps` | 2 CSS | yes |
| `rc__title` | 5 CSS | yes |

And the old strings are gone from every chunk: "cannot pause the", "once when you have given your Read", "say it back in your own", the old focus ring `29 29 31 / 0.35`, and the card's `border-l-2 border-[var(--rc-signal)]` stripe.

A first pass looked negative because the RRC code is code-split: `index-*.js` carries none of it. The markers live in `ActivityRunner-*`, `SectionReportCard-*`, `activity-centre-*`, `report-card-*` and `CompletionSummary-*`. Anyone re-checking a deploy here has to grep the chunks, not the index.

**What went out with it.** `776f69b` and `ece5480`, the concurrent session's practice-test clock work, sat between Step 4 and Step 5 on `main`. Deploying `main` shipped them too. Not reviewed or tested here.

**Not in this deploy.** Edge functions never deploy from a push or from `deploy_project`. `supabase/functions/grade-rrc-section/index.ts` has uncommitted local changes from another session and was not touched.

## Step 6: done, 2026-09-09

Commit `b0dd1e6`, "RRC: the door stops running for nobody, and the exit comes first". Built on branch `rrc-step-6` as `53dea8a`, reviewed as [PR #101](https://github.com/vnjkoxpl-42905/lsatu-684d89db/pull/101), rebase-merged to `main` the same day at Joshua's request. The merged tree is byte-identical to the reviewed commit. Measured on the harness at 1280x900 and again at 375x812, before and after.

### What the door was spending

| | Before | After |
|---|---|---|
| Animations running at rest, top of page | 187 | 19 |
| Animations running once the hero is scrolled past | 187 | 0 from the hero |
| Blade animations | 170, one per `<path>` | 6, one per group |
| Headline scroll blur | `blur(14px)` | `blur(4px)` |
| `will-change` on the static grain layer | `transform` | `auto` |

The grass now sways by `skewX` about the ground line instead of rotating each blade about its own base. Rotating six groups would have lifted the far blades off the ground line; skew leans the tips and leaves every base planted. Verified: the group transform is `matrix(1, 0, ±0.028, 1, 0, 0)`, base drift 0px, tip vertical drift 0px. The picture is unchanged. Blades per group: 33, 33, 29, 27, 26, 22, on six durations from 4.9s to 7.1s with negative delays so they are out of phase on the first frame.

Gating is a `data-still` attribute driven by `useInView` on three roots: `.mw`, `.rd-demo` and `.rd-method`. The demonstration's `setTimeout`, `setInterval` and per-frame typewriter stop with it and pick up from the beat they were on.

### What it owed a keyboard

- The live region is gone from the demonstration's step label. It turned over every 1.5 to 4.2 seconds for as long as the door was open.
- The scene moved last in the DOM. It is painted by z-index, so nothing moved visually, and the first four tab stops are now Library, Start the section, Read the full instructions, then the demo's Play button. Play used to be first, ahead of the way out.
- Targets, proved by hit-testing all four edges at both widths: Play 28x28 to **44x44**, crumb 55x17 to **73x47**, drawer tabs 43px tall to **58x47**. Drawn sizes unchanged; the targets are explicit overlays, the same way Step 4 did the runner's rail.
- `.rd-hero-top` lifted above `.rd-hero-copy`. They shared a layer and the copy came later in the DOM, so at 375px it sat over the bottom half of the exit's target: 73x32 instead of 73x47. Found only because the phone width was checked separately.
- The demo's focus ring was the hero's white on cream paper at 1.05:1. It is ink now, scoped to the card.
- The outline ran H1, H3, H2, and H1 then six H4s with the drawer open. Every section down the page now owns a level-2 heading carrying the exact string its `aria-label` already carried, so no accessible name changed, and the essay headings moved to H3.

### A third correction to this note's own audit

**The two gradient-stop contrast failures do not exist.** `section-launch.css:843` and `:1575` were reported from the rendered detector scan. The detector compared each text colour against its container's terminal gradient stop without knowing where in the box the text actually sits. Measured positionally in the browser:

| Text | Detector | Actually sits on | Measured |
|---|---|---|---|
| Tell diorama caption | 2.4:1 on `#a89fe0` | `rgb(62,54,106)` at 29% down | **10.82:1** |
| Closing panel line | 2.0:1 on `#a89fe0` | `rgb(42,36,79)` at 37% down | **14.35:1** |
| Its emphasis | | `rgb(47,40,86)` | **11.31:1** |
| Closing panel button | | its own opaque `#f6f3ea` chip | **16.1:1** |

Nothing is drawn on the pale end of either gradient, and the tell diorama's bubble paints its own opaque `#1a1635` regardless. No change made. The lesson repeats Step 2's: a finding taken from a record or a tool rather than from the rendered pixel can send a fix at something that was never wrong. Darkening those gradients would have flattened the dusk for nothing.

### Guards

- New `SectionLaunchFrame.a11y.test.tsx`, 5 assertions: the outline starts at H1 and skips no level, open and closed; no live region in the demonstration; the exit precedes the Play button; every loop still until its surface is on screen.
- `section-launch.css.test.ts` gains 6: grouped sway rather than per-blade, skew rather than rotation, the three `data-still` pause rules, the grain's `will-change`, the scoped ink focus ring, the three overlay targets, and the hero layer order.

### Verification

105 test files, 2778 tests, all passing. `npx tsc --noEmit` clean.

### Records

`PRODUCT.md` gains the two target-size rulings this needed. Dense glanceable rows are where the 44x44 house standard yields, which settles the ledger question above. A deliberate transparent overlay is a real target, proved by hit-testing, where wrapped text still is not.

### Separate branches, at last

Joshua's call, 2026-09-09: one branch per session. This step is the first to use it. Nothing here can reach production on the other session's push, which is what happened to Step 5. The working tree is still shared, so a branch protects this session and not the other one; a worktree would be the fuller fix if both sessions keep running together.

## Step 7: done, 2026-09-09

Commit `9cdc04f`, "RRC: one clock, one name for a number, one ground out of the drill room". Built on branch `rrc-step-7` as `2be5831`, reviewed as [PR #102](https://github.com/vnjkoxpl-42905/lsatu-684d89db/pull/102), rebase-merged to `main` the same day. The merged tree is byte-identical to the reviewed commit.

### The Time verdict disagreed with the time above it

Three surfaces answered the same question from three places and none checked the answer against the figure beside it. The card read the stored `within_time`; `runStats` preferred it and recomputed only when it was missing; nothing compared either to `total_seconds`. `recall/sectionClock.ts` derives it once now, from the two numbers she can see. The grader writes the flag from exactly that comparison, so nothing changes for a run graded since the flag existed.

| Harness | Time | Goal | Before | After |
|---|---|---|---|---|
| `state=faults` | 28:32 | 25 min | "Inside the time" | **"Over the goal"** |
| `state=clean` | 24:00 | 25 min | "Over the goal" | **nothing, because she made it** |
| a row predating the flag | any | any | *no verdict at all* | the verdict |

The third row is the one nobody had seen. `within_time` is optional; on a row written before it existed the value is `undefined`, which is neither `true` nor `false`, so both branches on the card were skipped and a student got a time, a goal, and silence between them.

### A test was wrong in the same shape as the bug

`runStats.test.ts` asserted, in its own comment, that 1450 and 1665 seconds are both inside 25:00. 25:00 is 1500 seconds; 1665 is 27:45. The fixture carried `within_time: true` to match the mistaken arithmetic, and the implementation trusted the stored flag, so the error was invisible from both ends and the assertion passed for the wrong reason. The fixture is now 1465, which is inside the clock **and** outside `within_goal`, so the test proves what its name claims. A second test pins the contradiction directly.

This is the third time in this run that a stored or written record, rather than the rendered thing, was the source of a wrong belief. Step 2 was a stale `CONTEXT.md`; Step 6 was a detector reading a gradient's terminal stop; this was a comment doing arithmetic.

### One name for a number

- **"Recalled" is "Recorded"** in the stat strip, the run table and `SectionStats`. It counts stimuli she spoke into, judged or not. A student could record every stimulus in a section and recall almost nothing on any of them, and the door called that "Recalled 73/75".
- **The door's run table gains Held**, the card's own section figure under the card's own name: `Date | Time | Held | Recorded | Stimulus by stimulus`, no horizontal overflow at 1280. The library's table (`SectionRunHistory`) already said Held and Understood, so the section page was the surface out of step.
- **Per stimulus the figure sits beside the words**: "95% held. Almost all of it came back." Joshua's decision, 2026-09-09. The 2026-09-08 ruling is untouched and not in conflict: it bans Detail arithmetic ("20 of 21 details"), not the percentage.

### Three grounds in ten seconds, now one

The field warmed to the Activity Centre's cream `rgb(244,239,231)`. The marking wait then drew a cream Centre panel on the violet ground the report phase paints. Then the card arrived. The field now warms to what `.rc-ground` actually paints, and the wait is drawn inside `.rc`, so it is the card's own surface and the card replacing it is a change of content rather than of place.

Contrast improves either way, measured through a canvas: the handover inks are 14.18:1 and 8.28:1 on the new ground, and the wait's are 15.8:1, 6.34:1 and 5.63:1 on the card's page.

### A correction to the plan's own instruction

Step 7 above says to warm to `--rc-page`. That is the **card**, not the page behind it. `.rc-ground` is declared one step darker on purpose so the card still reads as a card, and warming to `--rc-page` would have left exactly the same visible step, one shade smaller. The handover copies a value it cannot reference, since neither colour is in scope for the other's stylesheet, so `recall/section.css.test.ts` now holds the copy to the original.

### Guards

`recall/sectionClock.ts` (the derivation and why), `recall/section.css.test.ts` (the handover warms to what the report phase paints, and not to the Centre's cream), plus new assertions in `SectionReport.test.tsx` (the wait is on the card's ground), `SectionReportCard.test.tsx` (a pre-flag row still gets a verdict; a stored flag does not outvote the printed time) and `runStats.test.ts`.

### Verification

106 test files, 2784 tests, all passing. `npx tsc --noEmit` clean.

One self-inflicted detour worth recording: a JSX comment placed as the first thing inside `return (` is a syntax error, and it went in after the last typecheck of that file, so seven test files failed to collect before it was caught. Run `tsc` after the last edit, not after the last interesting edit.

Next: Step 8, the ready beat.

## Step 8: done, 2026-09-09

Branch `rrc-step-8`. The beat is now the one thing only the beat can do.

- **"Microphone on." and the bar, nothing else.** The thirty-word instruction ("One take, all the way through, out loud. Space twice per stimulus...") left the beat and sits at the foot of the briefing, where she has as long as she likes. The foot also stops saying the timer starts the moment she presses Start, which was no longer true once the beat existed.
- **The check is real.** `VoiceLevel` gains `onHeard`, fired once on the first reading above the noise floor. The runner holds the count until that fires or `MIC_CHECK_SECONDS` (6) runs out, whichever is first, and the check's clock starts when the microphone opens rather than at mount, so a slow permission prompt cannot eat it. A zero-second beat has no check, which is what every existing test relies on.
- **Three states, three sentences.** Holding: "Say something to check your microphone." with no count showing, because a number ticking beside "say something" says the opposite. Heard: "Heard you." and "Starting in 3". Expired unheard: "Nothing heard yet. Check it is not muted." and the count. The footer status announces the one transition that matters ("Heard you. The section starts after the count.").
- **One bar at a time.** During the beat the bar renders in the panel at 160x4, where she is looking; once running it is back on the rail at 34x3. It is the same element and the same ink, and it still never reads as a score.
- Measured in the in-app browser on the new `section-beat-preview.html` harness (`?state=holding|heard|unheard|refused|running`): panel bar 160x4, no rail bar during the beat, one rail bar once running.
- Tests: three new beat tests (holds unheard, counts once the check runs out, counts as soon as it hears her, the last through a fake `AudioContext`). The old "actually counts once the ready beat is over" test opts out of the check, since jsdom has nothing for it to hear through. Suite 106 files / 2787 tests, `tsc` clean.

Worth knowing: the "heard" test cannot be written with a polling query. The footer status also says "Heard you", so `getByText(/heard you/i)` finds two elements; the exact string "Heard you." finds the panel.

Next: Step 9, the quieter door and its tokens.

## Step 9: done, 2026-09-09

Branch `rrc-step-9`, off `main` rather than off Step 8, so the two can merge in either order.

- **The three hover lifts are gone.** Start, the step cards and the section Go button change colour on hover and nothing else; the transitions list only the property that still moves. The step card's hover is now a 3:1 edge instead of a 4px rise and a 44px shadow.
- **The traffic-light dots and the glass chip are gone**, CSS and markup. The chip restated the H1 verbatim in a `backdrop-filter` pill; the title says it once now.
- **3:1 edges.** New `--rd-edge` (`#8b879a`: 3.43 on paper, 3.14 on cream, 3.03 on paper-2) on `.sl-close` and the attempt rows, whose only boundary measured 1.32:1. Close hovers to ink. A flat attempt row is not a control and keeps `--rd-line`, stated explicitly.
- **Tokens.** `--rd-key-edge` and `--rd-key-edge-soft` name the seven `#cfc9bd` and three `#d9d3c6`. Five `*-rgb` triplets (ink, on-dark, marigold-ink, apricot, shadow) carry every shadow and wash rgba, so each one is visibly a palette colour at an alpha. Raw `#e3ded2`, `#2a2450`, `#1a1635` and `#f3c9a0` now use the tokens that already existed, and the two `var(--x, fallback)` forms lost their fallbacks. 32 rgba literals became 3 (the token definitions).
- **Scoping.** The eleven `.mw` meadow rules are now `.sl .mw`; the file's header no longer claims a scope it did not have.
- Measured in the in-app browser on the launch harness, `?state=runs` and `?state=library`: close and attempt borders `rgb(139, 135, 154)`, flat rows `rgb(227, 222, 210)`, transitions `background 0.2s` / `border-color 0.2s`, no chip, no dots, meadow under `.sl`.
- Component suite 33 files / 313 tests, `tsc` clean. The stylesheet test's own assertions (`.mw-blades g {`, `.mw[data-still]`) still hold as substrings of the scoped selectors.

Not done in this step: the remaining 37 hex literals (gradient stops, the demo bar's `#fbf9f3`, the apricot tints) have no token to point at; naming them is a palette decision, not a cleanup.

Next: Step 10, the phone door.

## Step 10: done, 2026-09-09

Branch `rrc-step-10`, off `rrc-step-8` because both touch the briefing foot. Its PR is based on `rrc-step-8`; retarget to `main` once #105 merges.

- **The plan's cap did not hold, and the plan was wrong about why the hero was tall.** `min(760px, 70svh)` was applied and measured at 375x812: the demonstration card is 597px tall on a phone and sits absolutely at the bottom of the hero, so a 568px space put it under Start (demo top 340, Start 388 to 440). The 760px was never dead space; it was room reserved for the card. So on a phone the scene's box dissolves instead: `.mw { display: contents }`, its planes still paint the whole panel (sky measured 1214px over a 1145px panel), and `.mw-stage` becomes a static block after the copy with its parallax transform neutralised. The hero is now exactly as tall as what is in it: 1145px, from 1216, with no overlap and the card starting the line after "Read the full instructions".
- **`.rd-meta` stays on the phone**, wrapped to its own line: "PT105.S2 · 25 stimuli · est 25 min", 17px, visible at 375.
- **Step bodies are inline on one column.** The card already carried the whole body, clamped to four lines; under 640px the clamp is lifted (measured 135px scrollHeight = clientHeight).
- **The briefing names the button.** On a coarse pointer with no hover, the foot adds: "On a touch screen there is no Space bar. The run shows a button at the foot of the page instead, Next stimulus and then Recall full stimulus, and it does the same thing." The door's laptop warning is unchanged; this is the instruction, not the warning.
- **`NO_KEYBOARD_QUERY` is `(pointer: coarse) and (hover: none)`.** A touch laptop with its keyboard attached matched `pointer: coarse` alone and got the phone treatment beside a working Space bar. Both no-keyboard tests mock by comparing against the exported constant, so they hold unchanged.
- One consequence to know: with `display: contents` the scene's root has no box, so `useInView` never sees it and the grass sway stays paused on phones. That is the battery-correct answer and was not sought separately.
- Tests: two briefing tests (names the button on touch, silent otherwise), stylesheet test pinned to the three phone rules. Suite 106 files / 2790 tests, `tsc` clean. Measured at 375x812 and at the pane's 722px.

Next: Step 11, the records.

## Step 11: done, 2026-09-09

Branch `rrc-step-11`, off `main`, independent of the other three open PRs.

- **DESIGN.md carries both rulings.** Under Tertiary: `.ac-section` is a sanctioned LawHub mirror, not a world and not Workroom chrome, the same mirror `OfficialDrillFrame` is; and the door's cream is the owner's deliberate exception to his own Report Card veto, three days apart on the same owner's brief. Under Typography's Named Rules: the Question Lock has one exception and it is the mirror, since the test-day stimulus is Fraunces at 19px.
- **The surface brief gains a runner section** ("Read, Recall, Colour runner, section mode") and a cream note on the door section.
- **Thirteen raw slate literals are `--sec-*` tokens** (`--sec-rule-2`, `--sec-fill`, `--sec-paper-2`, `--sec-ink-2`, `--sec-ink-3`, `--sec-mark`, and two stray `#cbd5e1` folded into the existing `--sec-rule`). Fifteen lines changed; the only hexes left are the twelve definitions and two in comments.
- **Detector waiver, verified.** Three `ignoreValues` entries (colour, font-size, radius, value `*`) for `report-card.css`, each with the reason: a sanctioned world's palette and type scale being outside DESIGN.md is what a sanctioned world is, and its contrast is measured (lowest 5.63:1). Then, once Joshua asked, three more for `recall/section.css` added through `impeccable ignores add-value --file --reason`, with the mirror as the reason. Measured with `impeccable detect` 4.1.0 (it runs through `npx`; I had wrongly said it was not installed): `report-card.css` 6 advisory notes to 0 on the file scan (the 19 in the audit came from the rendered-URL scan, not re-run); `section.css` 10 advisory notes to 0. The one anti-pattern left on the card is the playhead stripe at `report-card.css:297`, which the audit already ruled functional and only visible while playing; it is not waived, on purpose, so the ruling stays visible.
- **The lab passes `onAdvance`**, the same act as its Space handler. Measured on `/activity-lab` at 375x812 with touch emulation: the button renders at 127x60 reading "Recall full stimulus", a tap hides the stimulus, the status reads "Say the whole argument back from memory.", and the label turns to "Next stimulus". The `kbd` hint is absent on the coarse pointer.
- Runner suite 30 files / 287 tests, `tsc` clean.

Next: Step 12, `$impeccable polish` then the audit and critique re-run.

## Step 12: done, 2026-09-09

Branch `rrc-step-12`, an integration branch: `main` plus Steps 8, 10, 9 and 11 merged in that order (10 is stacked on 8), then the polish, then the re-run. Its PR carries all five steps; merging it closes #105, #106, #107 and #109 by content.

### The polish

- **Copy.** Three em dashes out of student copy (`SectionProgress.tsx:48, :68`, `SectionReportCard.tsx:1383`); none remain in anything rendered. "Attempt" where the door and the wait said "run" (Last attempt, no attempts yet, first attempt, Marking your attempt, graded Attempts), "held" where the library row said "carried", so the figure has one name from the row to the card. The Recall verdict in words ("The whole thing, text off screen: partly there.") instead of the enum. The closing line no longer hardcodes twenty-five minutes or says "No going back" six hundred pixels under "You can pause". The three controls that said "Choose a section" on a page with one section say "Your attempts", and so does the slab's heading. The judge's reason for a Read renders only when the Read did not match; under "You found the move" it read as a correction of a right answer.
- **The card's own primary control.** `.rc__cta` replaces the corridor's shadcn Button for Done, Run these again, Check again and Back to the Activity Centre; the shell's emerald no longer reaches a world whose brief vetoes it. Measured: 44px, console colour on console ink, the same pill as every other control there.
- **Status regions mounted from the start.** The dispute control's three states were three elements swapped in and out; the focus-set fault and "Following your recording" were mounted with their text already present. Each is now one region, always there, whose text is the thing that changes. Measured: two `role=status` regions in the card, both empty at rest.
- **The measure.** `.rc__measure` capped the column, not the prose in the open stimulus, which ran 625px at 14px, 83 to 104 characters a line. Prose inside `.rc__movement` is capped at 60ch (Lexend's zero is 8.5px, so 72ch was 612px and about 80 real characters; 60ch is 510px and 66).
- **Stylesheet hygiene.** `.sl-dr-note` (dead, two rules, no markup) deleted; `.rd-slab`, `.sl-brief` and `.sl-briefing-page` each declared once instead of twice.

### Two defects the re-run found in this session's own work

- **Steps 9 and 10 fought when merged.** Step 9 scoped the meadow under `.sl`; Step 10's phone rules were not scoped, so `.sl .mw` won from outside the media query and the phone hero collapsed to 456px with the demonstration back over Start. Neither branch showed it alone. Fixed by scoping the phone rules the same way; the stylesheet test now pins `.sl .mw` and `.sl .mw-stage`. Measured after: hero 1114px, no overlap.
- **The beat harness measured a layout the product never ships.** `sectionBeatPreview.tsx` imported only `section.css`, so `sr-only` had no rule and the hidden `h1` was a 321x59 block in the rail. Found by Assessment A. It now imports `index.css` like the other two harnesses; hidden heading 1x1, rail 54px.

### Detector configuration, corrected twice

Assessment B found the `.rc` type-scale waiver covered `report-card.css` but not the same sizes written as Tailwind `text-[15px]` in `SectionReportCard.tsx` and `SectionReport.tsx` (20 advisories), and that the `section-launch.css` entry in `ignoreFiles` suppressed nothing on its own but hid 69 sanctioned-world advisories once removed. Both worlds now carry the same shape of waiver the runner got in Step 11: value `*` for colour, font-size and radius, scoped to the file, with the sanctioned-world reason, added through `impeccable ignores add-value --file --reason`. The blunt `ignoreFiles` entry is gone, so a real anti-pattern in the door surfaces again. Final `impeccable detect --json` over the six door, card and runner files: 1 finding, the playhead stripe at `report-card.css:348`, left unwaived on purpose (functional, only while playing).

### Audit, re-run

Method: DOM measurement on the three harnesses at the pane's 722px and at 375x812, contrast through a canvas against the actual rendered ground, `document.getAnimations()` at rest, heading outlines, target boxes with their overlays, plus the detector.

| Dimension | Before | After | Evidence |
|---|---|---|---|
| Accessibility | 2 | 3 | Worst text contrast: card 5.63:1, door 5.32:1 (11px step label), beat 4.76:1. Heading outlines in order on door, beat and card. Status regions always mounted. 44px on every rail, drawer and card control, by box or overlay. Left: `.rc__hear` at 26px tall (clears 2.5.8, not the house 44). |
| Performance | 3 | 3 | Door 17 animations at rest at 722px, 11 at 375 (from 187); card 0; beat 1. Left: the card re-renders on every audio `timeupdate`; the door's scroll-reveal and headline parallax are decorative. |
| Responsive | 3 | 3 | No horizontal scroll at 375. Phone hero content-sized, meta visible, step bodies inline. Left: hero still 1114px on an 812px screen; 27 text nodes under 12px at 375 (the mono labels, sanctioned). |
| Theming | 2 | 3 | Every named role is a token in all three worlds. Raw literals left: door 22 (gradient stops and tints with no token to point at), card 1, runner 24 (LawHub values, waived as the mirror). |
| Anti-patterns | 3 | 3 | Chip, dots, hover lifts, side stripe gone; detector 1 finding and it is a false positive. Assessment A still names the console's Held / Understood / Time trio as the hero-metric template, the three-card Retelling grid with an inverted card, the closing gradient panel, and the scroll-reveals. |
| **Journey** | **13** | **15** | **Good. Target was 17; not met.** |

### Critique, re-run

Two isolated assessments. A: an LLM design review from source and the live harnesses, in its own tab. B: the detector, CLI only. Neither saw the other.

| # | Heuristic | Before | After | Key issue now |
|---|---|---|---|---|
| 1 | Visibility of status | 3 | 3 | The rail says "Recording" while the beat's footer says "The section has not started." Both true; contradictory to read. |
| 2 | Match system / real world | 2 | 2 | "The move" needs a glossary mid-console; "Out loud" is a crumb category that appears nowhere else. |
| 3 | User control and freedom | 2 | 3 | Pause, Escape stays, Check again, Leave with a real confirm. |
| 4 | Consistency and standards | 1 | 1 | Scored before the naming fixes above landed (Last attempt, held, Marking your attempt, Your attempts). Still: "details carried" in the demo, "Coverage" in the console glossary. |
| 5 | Error prevention | 3 | 2 | The unheard beat counts her in anyway. See the open question. |
| 6 | Recognition over recall | 3 | 3 | The hint "space recall full stimulus" is a fragment. |
| 7 | Flexibility and efficiency | 2 | 3 | Roving tabindex on the ledger, Home/End on the beats. A returning student still gets a 4,400px door. |
| 8 | Aesthetic and minimalist | 3 | 2 | The method is taught six times before stimulus one; console 848px tall before the first stimulus opens. |
| 9 | Error recovery | 2 | 4 | Refused mic, upload failure, slow grade, dispute: each names the consequence and a way forward. |
| 10 | Help and documentation | 3 | 3 | `rules` never render on the briefing page while its lede says "skim the rules above". |
| **Total** | **24** | **26** | **Acceptable. Target was 32; not met.** |

Cognitive load: 3 failures of 8 (the method section offers 7 options, the console 22 ticks plus figures plus glossary, the open stimulus 8 controls). Detector: 1 primary, 0 advisory after the config fix, the primary a false positive. Assessment A found no em dashes in rendered copy and every measured contrast above AA.

### Why the targets were missed, honestly

The twelve steps fixed what was false, unreachable or broken. What is left is structural and was never in the plan: the door teaches the method six times (demo, four cards, drawer, essay, aside, briefing, coach) and is 4,400px tall; the console gives the verdict three ways in its first 80px; the runner's beat and rail say two true things that contradict. Those are shape decisions, not polish, and each is a `$impeccable shape` conversation with Joshua rather than a fix.

### Open question for Joshua

Assessment A's third priority: when the six-second check expires unheard, the beat now says "Nothing heard yet. Check it is not muted." and counts her in anyway. That is what Step 8's spec asked for ("until the level has moved once or 6 s, whichever is first"), and it is also the run the whole apparatus exists to prevent, a Report Card of zeros discovered at minute twenty-one. Joshua's answer, 2026-09-09: hold, and add Start anyway. Done on `rrc-step-12`: an unheard check now holds with "Nothing heard yet. Check it is not muted, then say something. Or start anyway." and three controls, Start anyway, Ask again, Leave this section. Only she starts the count. Tests: holds unheard past the beat's length; counts once she presses Start anyway. Heuristic 5 (error prevention) should re-score at 3.

### Recommended next, in order

1. `$impeccable shape` the door: keep the demo and the four cards, send "Read the full instructions" to the briefing page, drop the drawer and `MethodSummary`. Assessment A's first question.
2. `$impeccable distill` the console: one number she carries to the door, and the door's strip shows it.
3. `$impeccable clarify` the last two names: "details carried" (`RecallDemo.tsx`) and "Coverage" (`SectionReportCard.tsx` glossary).
4. `$impeccable optimize` the card: gate `setPositionMs` on the active line changing rather than on every `timeupdate`.
5. The Step 3 production actions, still outstanding: the inbox message on grade completion (edge function) and scheduling `sweep-rrc-grading` (ADR 0021).

