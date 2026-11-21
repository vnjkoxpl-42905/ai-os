# Claude Opus 5.5 neutral dashboard review

Verified actual completed run on 2026-10-24. Requested and observed model: `claude-opus-5-5`. Claude Code 2.1.309. Read-only artifact review; no browser execution. Verdict: **REVISE**.

Pass 2 stays in the requested neutral family: near-white canvas, charcoal hero, dark top rail, rounded week strip, and slate used only as small functional highlights. There is no rainbow drift. The library and recent-practice cards add real study utility, the score arithmetic adds up (9+6+5 = 20 of 10+8+8 = 26), saved and opened references persist with try/catch fallbacks, and the week strip supports arrow keys, Home and End. It still needs a revision for concrete defects. (1) Choosing a work row swaps the hero, and nothing restores Negation Station. The swap also overwrites a shared panel, so Friday's 'Continue your work' opens the wrong task. (2) craft.js and the pass-two CSS disagree about the hero object. Its opacity tween is overridden by !important, and its inline transform freezes the responsive scale at whatever width the page loaded. (3) Several nav links go to the wrong sections. (4) At 768px the work-row arrows sit in the middle of the row, and the sculpture collides with the folio panel. (5) The schedule contradicts itself: a drill marked 'Due Friday' is scheduled for Wednesday the 28th. Smaller issues: the variable-font weights, 7–8px labels on desktop too, the 'Find a question' button and profile both disappear on mobile, and every sample question has A as its answer. The parent's known items (tiny mobile labels, the floating right score at 390) are not repeated here.

## Findings

### F1-hero-swap-state (high)

Path: `C:/Users/Joshu/Downloads/LSAT-U-Dashboard-New-Directions/06-refined-studio/app.js`

app.js:10. Clicking a [data-task] row (Find the flaw / Reading recall) permanently rewrites #task-title, the folio, the bars and .saved. It also mutates the global panels.continue to 'Your selected work'. No control brings back Negation Station: it isn't in the work list, and Friday's agenda action (app.js:7,9 → openPanel('continue')) now opens the overwritten panel. The day detail still says 'Negation Station · 12 minutes left', so the panel and the text disagree. The chosen row also stays listed under 'Next in your work', so the same task appears twice. 'Joshua's note' (data-open=guide) still talks about negation for the swapped task. The same agenda path runs for Monday/Wednesday, which call [data-task].click() and swap the hero again.

Fix: Treat the hero as a function of one selected-task state. Keep Negation Station as a task entry, put the inactive tasks in the list, and hide the active one from it. Store each task's continue panel and guide text in taskData instead of mutating panels.continue. Map Friday's agenda to that task explicitly. Optionally persist the selected task in localStorage.

### F2-gsap-css-conflict-orbit-art (medium)

Path: `C:/Users/Joshu/Downloads/LSAT-U-Dashboard-New-Directions/06-refined-studio/craft.js`

craft.js:5 tweens .orbit-art to opacity .55/.24 and rotate -24deg. Pass-two CSS (style.css:67-70) sets opacity:1!important, .6!important and .7!important, so the opacity tween does nothing. The same CSS sets transform:none at desktop and scale(.8)/(.65)/(.52) at ≤1100/≤800/≤560. GSAP writes an inline transform, which beats non-important stylesheet rules. As a result: (a) with motion on, users get an extra -24deg on top of .paper-sculpture's rotateZ(-25deg), while reduced-motion users get a different composition; (b) the scale GSAP parses at load is frozen inline, so resizing or rotating the device across breakpoints no longer applies the responsive scale. The 1440 capture's steep, roughly diamond tilt is consistent with the combined rotation, but I can't confirm from a still which branch ran.

Fix: Choose one source of truth. Either drop the opacity/rotate tween and animate only a wrapper (for example .paper-sculpture) with transform values that don't collide with the breakpoint transforms, or move the breakpoint scale onto a child element. Set the final pose in CSS so the motion and reduced-motion compositions match. Remove the unused opacity targets.

### F3-768-art-folio-collision (medium)

Path: `C:/Users/Joshu/Downloads/LSAT-U-Dashboard-New-Directions/06-refined-studio/style.css`

pass-2-768.png: the question-mark sculpture sits behind the top-left of the translucent 'YOUR PLACE' folio. The folio has backdrop-filter and a translucent background (style.css:62), so the object shows through and crowds the label. Source: style.css:69 (≤800) .orbit-art{right:100px;opacity:.6!important;transform:scale(.65)} against the 150px folio column (style.css:64).

Fix: Between 561 and 800px, hide .orbit-art or move it fully behind the copy column, away from the folio (for example right:auto;left:55%; or display:none). Alternatively make the folio fully opaque so nothing reads through it.

### F4-nav-targets (medium)

Path: `C:/Users/Joshu/Downloads/LSAT-U-Dashboard-New-Directions/06-refined-studio/index.html`

index.html:3 (desktop nav and #mobile-nav): 'Library' → #practice (the 'A little extra?' link, not the library card #question-picker). 'Progress' → #progress, which is the session-card aside (index.html:9), not recent practice #recent. 'Review' → #work, the assignment list. 'Practice' and 'Library' share a target. The .active class never moves. Mobile users depend entirely on these links.

Fix: Point Library to #question-picker, Progress/Review to #recent and Practice to #practice (or the practice panel). Give the session aside its own id. Optionally update the .active/aria-current state on hashchange or with an IntersectionObserver.

### F5-768-row-arrow-placement (low)

Path: `C:/Users/Joshu/Downloads/LSAT-U-Dashboard-New-Directions/06-refined-studio/style.css`

pass-2-768.png: the ↗ arrows on 'Find the flaw.' and 'Reading recall.' sit just after the titles, mid-row, instead of at the right edge. Cause: .row-time (which carries margin-left:auto) is hidden at ≤800 (style.css:5, :32), and .row-arrow{margin-left:auto} is only set at ≤560 (style.css:6). The same capture shows the session card's 'Prepare ↗' and 'With Joshua · 60 minutes' wrapping onto two lines.

Fix: Set .row-arrow{margin-left:auto} at ≤800 (or always). In the session footer at 561–800, add white-space:nowrap to the button, or drop the duplicate 'With Joshua · 60 minutes' line (see F9).

### F6-schedule-contradiction (medium)

Path: `C:/Users/Joshu/Downloads/LSAT-U-Dashboard-New-Directions/06-refined-studio/index.html`

index.html:9 marks Find the flaw 'Guided drill · 8 questions · Due Friday'. Today is Friday, October 23 (edition line). The week strip and day data (index.html:14, app.js:7) schedule 'Guided practice / Find the flaw' for Wednesday the 28th, after the due date. The hero also says '15 minutes' while Friday's detail says '12 minutes left'. That reads as remaining vs total but isn't labelled.

Fix: Make the due date and the schedule agree (for example 'Due Wednesday'), and label the hero time as total ('15 min total') or show remaining time in both places.

### F7-variable-font-weight (low)

Path: `C:/Users/Joshu/Downloads/LSAT-U-Dashboard-New-Directions/06-refined-studio/style.css`

style.css:1 declares the Manrope and Newsreader variable fonts without a font-weight range or font-display. With the descriptor omitted it defaults to 400, so Chromium/Edge clamps the wght axis and synthesizes the 600/650 weights used throughout (.eyebrow, .utility-heading, .session-time, .question-ask). That gives faux-bold labels and a possible flash of invisible text.

Fix: Add font-weight:200 800 (the ranges these variable files ship with) and font-display:swap to each @font-face rule.

### F8-desktop-micro-type-contrast (low)

Path: `C:/Users/Joshu/Downloads/LSAT-U-Dashboard-New-Directions/06-refined-studio/style.css`

This is separate from the parent's mobile-label item: desktop also ships 7–8px text. Examples: .library-index small 7px #718092 on #fff (about 4.0:1, below 4.5:1), .saved-slips small 7px, .console-label 8px, .set-score>span 8px ('View sample ↗', an action cue), .review-next .eyebrow 8px (style.css:62,67). The pass-2-1440.png capture shows these as barely legible.

Fix: Set a 10–11px floor for every label/meta role on all breakpoints and darken #718092 to at least about #5f6b7a. Make 'View sample' at least 11px, or drop it and rely on the row hover/arrow.

### F9-mobile-lost-entry-points (low)

Path: `C:/Users/Joshu/Downloads/LSAT-U-Dashboard-New-Directions/06-refined-studio/style.css`

style.css:63 hides .rail-picker at ≤1100, overriding the icon-only treatment intended at ≤560 (style.css:42). style.css:42 hides .avatar at ≤560. #mobile-nav (index.html:3) has neither 'Find a question' nor profile. pass-2-768.png and pass-2-390.png show only Inbox and Menu in the rail. Ctrl+K also has no visible hint on these widths. Separately, opening Inbox sets the badge to '0' but leaves the pill visible, and the count isn't persisted.

Fix: Restore the icon-only picker button at ≤1100 (move display:none out of the 1100 rule, or re-enable it at ≤800). Add Profile and Find a question links to #mobile-nav. Hide the inbox badge when the count is 0 and give the button an accessible unread label.

### F10-sample-answer-key (low)

Path: `C:/Users/Joshu/Downloads/LSAT-U-Dashboard-New-Directions/06-refined-studio/app.js`

app.js:14: all three examples have answer:0, so A is always correct, and the choices aren't shuffled. Feedback text is keyed on the literal title string 'The community garden' (app.js:28), which is brittle. For a study tool this teaches a pattern rather than reasoning.

Fix: Vary the correct index across the samples, and store per-question correct/incorrect feedback strings on each example object instead of branching on the title.

### F11-library-card-preamble (low)

Path: `C:/Users/Joshu/Downloads/LSAT-U-Dashboard-New-Directions/06-refined-studio/index.html`

index.html:11; pass-2-390.png and tools-2-390.png. Before the first control the card stacks a utility heading, a 45px display headline, a decorative 'Q / THE REFERENCE DESK' watermark, a tagline, a rule and an 'OPEN BY REFERENCE 01 / FIND' label. After the selects, 'Selected reference 155 / 1 / 01' repeats values already visible in them. On a 390px screen the picker starts well below the card top. The product lens asks that tools disappear into the task.

Fix: Drop the Q watermark and the 01 / FIND label, cut the headline to about 28–32px, and remove or merge the reference-preview row into the Preview button label (for example 'Preview 155 · S1 · Q01').

### F12-folio-aria-and-session-duplication (low)

Path: `C:/Users/Joshu/Downloads/LSAT-U-Dashboard-New-Directions/06-refined-studio/index.html`

index.html:6: .folio is a generic div with aria-label='5 of 12 prompts complete'. aria-label is not announced on generic elements, so screen readers read '06 /12' with no context. index.html:9: the session card repeats 'With Joshua · 60 minutes' right under '7:15 pm 60 minutes' and the 'Saturday, with Joshua.' heading.

Fix: Add role='group' (or put the label in visible or sr-only text) so the folio reads 'Prompt 6 of 12, 5 complete'. Remove the duplicate session footer text and keep only the Prepare action.

### F13-load-choreography (low)

Path: `C:/Users/Joshu/Downloads/LSAT-U-Dashboard-New-Directions/06-refined-studio/app.js`

app.js:2 runs a staggered 650ms page-load entrance plus 600ms scroll reveals that start from opacity .5. craft.js:5 adds a 1.15s object entrance and pointer parallax. The animate/product lenses call for 150–250ms state motion and no load choreography. None of this conveys state. Reduced motion is correctly guarded (the reduced flag, CSS @media at style.css:7/59).

Fix: Remove the load and scroll reveals. Keep only short state transitions (task swap about 200ms, day detail, dialog). If the object stays, give it at most a single subtle settle with no parallax.

## Actual coverage

- Images actually read with Read: artifacts/pass-2-1440.png (1440x2421), artifacts/pass-2-768.png (768x3221), artifacts/pass-2-390.png (390x3589), artifacts/tools-2-390.png
- Source read in full: index.html, app.js, craft.js, style.css (lines 1-71, all)
- Asset existence checked by Glob: lib/gsap.min.js and the three variable font files
- Design lenses read: design-critique/SKILL.md, impeccable reference product.md, color-and-contrast.md, typeset.md, animate.md
- Traced shared state: panels.continue mutation, selectedDay/agenda dispatch, savedRefs/openedRefs localStorage paths and rollback, prep note persistence, filter/hidden rows, kind-switch↔native select sync, dialog focus restore, Ctrl+K handler, nav hash targets
- Checked CSS cascade order across the layered override blocks for .orbit-art, .rail-picker, .avatar, .row-arrow, .accuracy-total, .day small
- Data checks: recent-practice totals and answer strips agree with scores; week/day data compared with work rows

## Limits

- No live browser interaction, test run or animation observation. Motion findings come from source; stills can't show animation, and whether GSAP ran during the Edge captures is inferred, not confirmed.
- Screenshots are pass-2 captures. The source I read matches them on every point I checked (row arrows at 768, hidden rail picker/avatar, floating score at 390), but I can't rule out pass-3 edits happening at the same time.
- Contrast ratios are hand-computed from hex values, not measured from rendered pixels. The faux-bold variable-font behavior is based on known Chromium handling of a missing font-weight descriptor, not seen in the capture.
- The attached original 'refined dashboard' reference wasn't among the readable files. Fidelity to the neutral family is judged from the plan's description: near-white canvas, charcoal hero, top nav, rounded week strip.
- lib/gsap.min.js confirmed present but not read.
- Parent-identified items (tiny mobile labels, floating right score at 390) are left out as already known.
