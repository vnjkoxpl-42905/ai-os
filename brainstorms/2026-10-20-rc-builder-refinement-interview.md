# RC drill builder refinement: Brainstorm / Discovery Notes
Date: 2026-10-20 · Goal: Settle refinements to the selected dark RC concept and its right drawer before implementation.
Status: complete; implementation authorized locally
Context sources: Current conversation; local rc-builder-three-designs.html version 3; rc-three-concepts-review.md; completed Sonnet and Opus reviews. No canonical context updates requested.

## Summary / key decisions
User-confirmed requirements from the current request:
- Retain minimal dark LR-grounded styling and right drawer; LR itself unchanged.
- Use 'Choose your next passage' and natural plural wording; remove redundant headings.
- Main screen exposes Choose for me / Pick passages; Pick passages opens drawer directly to passage selection.
- Rename More options to Customize drill and organize the drawer clearly.
- Concise applied-setting summary includes topic, difficulty, practice history and timing.
- Answer-reveal timing readily editable, Preview drill remains primary.
- Simplify copy/spacing/hierarchy; predictable Apply/Cancel/close; preserve functionality; desktop/mobile visual checks.

Confirmed by 'yes to both go ahead and refine version 3 then check it in the codex browser on desktop and mobile':
- Refine version 3 locally first; do not replace production builder until design is confirmed.
- Choosing Pick passages opens a draft manual selection; Apply commits its mode and picks; Cancel/X/Escape/backdrop discard draft changes and preserve the prior applied mode.
- Show answer-reveal timing on the main setup next to passage count and timing.

## Q&A log
### Round 1 (answered)
#### Q1 - Deliverable scope
- Asked: Refine version 3 locally before production integration?
- Recommended: Yes; complete and visually verify the concept first, keeping production/LR unchanged.
- Captured: 'yes to both'; refine version 3 locally and check desktop/mobile in Codex browser.
- Flags: None.
#### Q2 - Mode commitment
- Asked: Apply commits manual mode and passage choices; Cancel/close restores applied mode and settings?
- Recommended: Yes; Choose for me switches back to the preserved automatic setup, while opening manual selection remains a draft until Apply.
- Captured: 'yes to both'; Apply commits manual picks and mode, Cancel/close keeps previously applied setup.
- Flags: None.

## Open flags (pending input)
- None. No canonical context updates or publication requested. Resume point: implement and visually verify the local version 3 refinements.
