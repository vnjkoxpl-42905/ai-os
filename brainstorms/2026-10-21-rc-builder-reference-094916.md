# RC Builder Reference: Brainstorm / Discovery Notes
Date: 2026-10-21
Goal: Adapt selected strengths of Joshua's Desktop HTML reference into a simpler RC builder without copying it wholesale.
Status: in progress
Context sources: Current RC builder conversation; C:/Users/Joshu/Desktop/LSAT U RC Builder.html; current local preview.

## Summary / key decisions
- User confirmed: use the supplied HTML as inspiration, not a complete copy. Interview requested before implementation.
- Previously confirmed: LR stays unchanged; RC uses its neutral black-and-cream identity, compact controls, right drawer, separate Review and Start, preserved safety and save semantics.
- No new design choices have been confirmed in this interview.

## Design tree
- Primary screen structure and first decision.
- Visual qualities to borrow from the reference.
- Boundary between essential controls and drawer details.
- Dependent: exact layout, manual picker transition, responsive behavior, final shared-understanding confirmation.

## Q&A log
Awaiting first round.

## Open flags (pending input)
- Which reference qualities to adopt -> Joshua after source analysis.
- Browser blocks file protocol; visual rendering not verified -> agent limitation.
## Reference analysis (source-derived, not visually verified)
- Strongest idea: separate intent and method on the left from a compact practical setup on the right.
- Prototype exposes count/timing; other settings are summaries and drawer controls.
- Its manual picker, Review, launch and backend behavior are incomplete; do not copy its functionality.
- Preserve existing Apply/Cancel drafts, exposure safeguards, eight-passage capacity, exact/settings save distinction, and Review/Start.
- Prior capture consulted: brainstorms/2026-10-20-rc-builder-refinement-interview.md. Its confirmed semantics remain unless explicitly revised.

### Round 1 (pending answers)
#### Q1 - Composition
- Asked: Borrow the split composition with a short heading and selection dropdown on the left, compact setup on the right, and stacked mobile layout?
- Recommended: Yes. Borrow the hierarchy, reduce the oversized introduction, retain neutral LSAT U styling.
- Captured: Pending.
#### Q2 - Basic controls versus refinement
- Asked: Show count, timing and Show answers as basic controls; make Topic and Difficulty directly editable summary values, with detailed filters in the right drawer?
- Recommended: Yes. Keep choices accessible while reducing simultaneous form controls. Do not bury answer timing.
- Captured: Pending.
#### Q3 - Manual workflow
- Asked: Retain immediate picker opening when Pick specific passages is chosen, then return to the same setup with selected titles and Preview drill?
- Recommended: Yes. Avoid the prototype's extra Browse passages step. Apply/Cancel preserve existing semantics.
- Captured: Pending.

### Round 1 answers and authorization
- Captured: User supplied screenshot for visual reference, then explicitly approved the two-button switch and asked to implement an improved version and show it in Codex browser.
- Supersedes Q1 dropdown recommendation: use Choose for me / Pick passages switch, as screenshot.
- Confirmed direction: split intent/setup composition, compact controls, right drawer, primary Preview, existing Review/Start and safeguards preserved.
- Scope: local implementation and browser demonstration; no deployment authorized.
- Status: shared direction confirmed; implementation authorized.
