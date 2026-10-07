# Study-tools final review dispositions

The Claude build and two delegated fix rounds are complete. Codex took over bounded correctness fixes, with separate independent inspection. All source remains uncommitted in the isolated study-tools checkout. This is not a whole-ticket completion claim.

Final review claudex-n2v0sqqz dispositions:

- F1: RC touch visibility fixed in RcChoiceRow; hover:none explicitly exposes cross-out controls. Focused regression covers the class and selected-answer behavior.
- F2: RC selected answers are effectively uneliminated and their cross-out controls are disabled. RcPlayer also rejects selected-letter elimination. This matches LR and does not write attempts.
- F3: Automatic removal of stored entries is deliberately excluded. Joshua requires confirmation for deletion, and the work order prohibits deletion. Current-question clear and individual bookmark removal are explicit user actions. Storage remains bounded and is disclosed; failed saves preserve page-only edits. No cross-device or indefinite-storage claim is made.
- F4: Independent source inspection disproved the proposed production auth-hydration path. Both routes pass through DrillAssignmentGate and ProtectedRoute; unresolved auth cannot mount the runner. Same-actor refresh retains the actor key. Do not broaden the wrapper on the basis of direct ungated test mounting.
- F5: Incorrect reviewer inference, corrected after browser verification. LR already binds officialSearchTerm to the shared toolbar and OfficialQuestionPane. Typing Democracy highlights the matching stimulus text in the real canonical PT155-S4-Q20 canvas. No new find implementation is required simply because a search for findQuery returned no matches. Existing LR and RC find controls are preserved. #179 remains open for its other acceptance requirements.

For fresh Claude inspection, independently verify the Codex follow-up production changes and relevant tests, including RcChoiceRow touch/selected-answer behavior, RC reducer-derived persistence, restore-through-selection, precise clear, failed device-save overlays, and actor-switch isolation. Read all changed files and tests. Do not infer execution from source. Host owns tests and browser verification.
