# Spot confirmed-fixes release review log

## 2026-10-25: authorized build and inspection 1

User authorized implementation of confirmed problems, design-principle updates, Claude final review and isolated publication. Host and builder Codex; final inspector fresh Claude session requested claude-opus-5-5. Based on prior completed independent all-48 audit, with host dispositions. No separate implementation-plan review is claimed. Inspection stays on; maximum two completed inspections and two fix rounds. No model substitution, paid Lovable prompts or live grader calls.

Plan: 2026-10-25-spot-confirmed-fixes-release.md. Build worktree: C:/Users/Joshu/dev/ai-os-projects/lsatu-spot-confirmed-fixes-20261025, base 73dd27e2c68ed9a9b46af274a1366c2817f7030c. Eight staged app paths, no unrelated source files. Shared vault design/principles.md links the dated audit and app-owned surface brief.

Host verification: 230 focused tests, typecheck and build passed. Browser component fixture inspected at four widths with screenshot readback, first-hint visibility boundary and 15 targeted item explanations. Proof and limits: handoffs/claudex/spot-confirmed-fixes-20261025/proof.md. Vite generated MCP dirt restored, devserver stopped before inspection.

Fresh inspection result path: handoffs/claudex/spot-confirmed-fixes-20261025/claudex-rcf2d02c/result.json. Pending; no approval inferred from launch. External content-release helper is hash-bound in plan and only patches canonical items/instructions/subtitle after approval, with exact ID/slug/updated_at compare-and-swap. All four existing assignment snapshots remain untouched. Full reviewer response must be retained and dispositions recorded before release.

## Inspection 1: REVISE; dispositions and fixes
Observed model claude-opus-5-5. Accepted F1 medium and separated display recognition from strict instant matching, with regression coverage for Q31/Q38/Q5. Accepted F2/F3 low and pinned source hash with RuntimeError guards plus precise ID/state/snapshot accounting. Three mocked publication guards passed under python -O. Rejected F4's claim that no router link exists: exact file C:/Users/Joshu/dev/ai-os/design/principles.md line 29 already contains it; it belongs to the separate vault, not this app PR. Updated plan accordingly. Nine-file final scope adds observatory.test.ts. Final 231 tests/typecheck/build passed; generated MCP file restored.
Full response:

{
  "verdict": "REVISE",
  "summary": "The release is mostly sound, but one medium defect needs fixing before approval, plus three low items.\n\nWhat works:\n- The Q5 boundary fix handles `causal, caused` without quotes, and comma-separated pairs still split correctly.\n- The reveal uses the saved item's own key, safely falls back for unkeyed or malformed keys, and leaves other activities unchanged.\n- The Q7/Q26 rewrites and the explanation edits keep the authored thresholds and modality.\n- The external helper only writes the canonical items, instructions and subtitle. Its PATCH is compare-and-swap on ID, slug and updated_at, and a trigger already bumps updated_at.\n\nThe medium defect: the new \"refer to Coach\" rules in confidentPair are also used by readAnswer. That function drives the Observatory's after-feedback display. Valid wider clauses that contain another type's indicator, and whole-prompt quotations, are now shown to students as \"Not yet identified\". This happens after any verdict other than correct, including \"unchecked\". So local non-confidence becomes a visible error, which acceptance item 2 forbids.\n\nLow items:\n- The helper does not check the authored content hash.\n- Its verify mode misses assignments that are missing, new or have changed status.\n- The required link from the shared design-principles router to the audit is not in the release manifest, and I could not find it elsewhere.",
  "findings": [
    {
      "id": "F1-observatory-shared-span-shown-as-missed",
      "severity": "medium",
      "path": "src/features/activity-centre/worlds/observatory/observatory.ts",
      "evidence": "Lines 361-363 add two rejections to validUnit inside confidentPair: an exact whole-prompt match, and any unit containing another keyed type's indicator. matchedKinds (291-298) calls confidentPair, and readAnswer (233-246) uses matchedKinds to compute `drawn` and `missed`. registry.tsx:243 calls readAnswer whenever the item is answered, not revealed and the verdict is not correct (so partial, incorrect or unchecked). ObservatoryStage.tsx:267-270 then shows 'Not yet identified: …'. Example: on Q31 a student writes `comparative, \"heavier\"; causal, which is why the foundry cast the alarm bell in the larger mould`. That causal clause is an exact source span containing 'which is why', so it was drawn before this change. It also contains the comparative indicator 'larger', so it is no longer drawn. If the Coach returns partial or unchecked, the stage tells the student Cause is 'Not yet identified' even though they quoted a valid clause. The same happens for Q38 `conditional, only where the canopy is denser than sixty percent`, Q36 `comparative, lasts longer when the mortar is softer than the brick`, Q40's `so a coupon with a thicker oxide layer than the control…`, and whole-prompt answers. The spec says to refer such spans rather than treat them as errors, and never to mark a local false as wrong.",
      "fix": "Separate instant-credit confidence from recognition for display. For example, add a `strict` flag to confidentPair: matchesCredited uses strict=true (the new whole-prompt and shared-span rejections), while readAnswer/matchedKinds-for-display uses the previous rule (exact source span containing an own indicator). Alternatively, report such types to the stage as 'unconfirmed' rather than missed. Add a test that readAnswer still draws Q31's 'which is why … larger mould' clause and Q38's conditional clause, and that no 'Not yet identified' line appears for them."
    },
    {
      "id": "F2-helper-does-not-pin-authored-hash",
      "severity": "low",
      "path": "C:/Users/Joshu/dev/ai-os/handoffs/claudex/spot-confirmed-fixes-20261025/content-release.py",
      "evidence": "Lines 21 and 55 read the source from the mutable working tree (REPO/SOURCE) and PATCH content(authored) without checking that the file still hashes to the reviewed 4911d51f…cd14, or that it matches the merged commit. The plan pins that hash but leaves enforcement to a separate manual step. Any later edit to the working tree would be published without notice. The asserts also disappear under `python -O`.",
      "fix": "In apply mode, compute sha256 of the source bytes and abort unless it equals 4911D51FD1E04A189FD7B14AC1C40A7D31919D82C2350C1D12BC5B611F75CD14. Preferably also read the content via `git show <merged HEAD>:SOURCE` and compare. Replace `assert` with explicit checks that raise."
    },
    {
      "id": "F3-verify-ignores-missing-or-changed-assignments",
      "severity": "low",
      "path": "C:/Users/Joshu/dev/ai-os/handoffs/claudex/spot-confirmed-fixes-20261025/content-release.py",
      "evidence": "Line 65 only compares snapshot hashes for assignments that are both still present and in `before` (`for a in metadata if a['id'] in before`). It does not notice a recorded assignment that has disappeared, a new assignment, or changes to status, started_at or completed_at. The receipt's 'assignmentsPreserved: len(before)' therefore overstates what was checked.",
      "fix": "Assert that the set of IDs is unchanged, or report differences explicitly. Compare status, started_at and completed_at along with snapshotHash, and set assignmentsPreserved from the count actually verified."
    },
    {
      "id": "F4-design-router-link-not-in-release",
      "severity": "low",
      "path": ".impeccable/surfaces/src-features-activity-centre.md",
      "evidence": "Acceptance item 6 requires a link from the existing shared design-principles router to the dated audit (research/2026-10-25-spot-all-questions-claude-review.md). The eight-file manifest changes only the surface brief, and its new section does not link the audit. Searching AI OS markdown found the audit filename only in wiki/log.md, not in any design-principles router.",
      "fix": "Add the audit link to the existing design-principles router, and either include that file in the allowlist or record where it was committed. Alternatively, link the audit from the new surface-brief section."
    }
  ],
  "coverage": [
    "Plan text and the full tracked diff for all 8 manifest files",
    "observatory.ts: answerPairs boundary, matchedKinds, readAnswer, confidentPair, matchesCredited, parseSignal and KIND_PATTERNS, traced by hand for Q5, Q26, Q28, Q31, Q34, Q35, Q36, Q38 and Q40",
    "Consumers of the grading path: registry.tsx fastPath and the readAnswer call, and ObservatoryStage.tsx drawn/missed rendering",
    "CoachFeedback.tsx reveal logic, compared with the ActivityItem answer_key type and the Edge readAnswerKey validation (unique types, non-empty indicators)",
    "Edge activity-coach answerKey.ts and grading.ts: how grading_rubric is consumed and that the TYPE_PATTERNS copy is unchanged",
    "spot-the-relationship.json: all prompts and credited answers listed; keys for Q7, Q26, Q38, Q41 and Q42 and all required_parts entries; rubric addition",
    "answerKey and CoachFeedback test additions, including the narrowed Q35 clause expectation",
    "External content-release.py, proof.md and the canonical-target-diff.json path list (content fields only); updated_at trigger on activities in migrations"
  ],
  "limitations": [
    "I could not run tests, typecheck or build. The 230/230 pass and build claims in proof.md are unverified by me.",
    "I did not check the manifest SHA256 values against the files on disk.",
    "I did not open the screenshots, build-final.log, canonical-baseline-diff.json values, the source receipt or the assignment JSON contents. I reviewed only the canonical-target-diff path list.",
    "I could not see live database state, RLS for admin PATCH, or production behavior. There is no live AI grader evidence for the new rubric line.",
    "I did not locate the shared design-principles router file, so F4 rests on a negative search of AI OS markdown.",
    "I did not exhaustively check every one of the 48 items for overlap between own and other indicators. The keyed-answer-per-item test is claimed to cover the canonical cases."
  ]
}

## Inspection 2: APPROVED
Fresh observed model claude-opus-5-5, snapshot cd7edf102b99506c1b8fd6b9cf33074523b6298aaf4ff2b89e5d2a98b84ad622. No source edits after approval. R2-F1 accepted as an existing low-priority unquoted wider-clause parsing limitation, not a regression; defer rather than invalidate approval. R2-F2 accepted as a receipt-baseline caveat if preflight is rerun. Mitigation for this release: do not rerun preflight, and independently confirmed assignments-observed.json and assignments-before.json are identical before apply. The helper itself writes no assignments. No third inspection needed. Full response:

{
  "verdict": "APPROVED",
  "summary": "The final nine-file diff matches the plan's acceptance criteria. The Q5 boundary fix keeps comma-separated pairs and the swapped-pair rejection working. The focused-quotation filter applies only to matchesCredited, so the illustration still recognises Q31/Q38 wider clauses and the Q5 whole prompt. When filtered answers are not credited they go to Coach and are never marked wrong. I traced each real prompt that contains a comma: the whole-prompt check cannot be bypassed by splitting the prompt into comma or 'and' pieces, because the pieces either contain another type's indicator or contain no indicator. The reveal reads only the saved item's own structured key and falls back to credited_answers for unkeyed or malformed history. Non-Spot activities are unchanged. Q7 and Q26 no longer have comparative ambiguity, and their keys and traps were updated with them. The corrected explanations keep the right threshold, modality and sufficient/necessary direction; Q45's 'Provided' is correctly described as sufficient, not necessary. The release helper only changes items, instructions and subtitle on the exact ID, slug and updated_at, re-reads the result, and enforces the source hash with a RuntimeError check. The router link is at principles.md:29. I found only two low-severity edge cases, neither material.",
  "findings": [
    {
      "id": "R2-F1",
      "severity": "low",
      "path": "src/features/activity-centre/worlds/observatory/observatory.ts",
      "evidence": "answerPairs line 284: the lookahead `(?=\\s*[:,]|\\s+\\S)` still splits before an unquoted type word that is followed by more text. For Q5, 'Causal, caused the smoke to back into the reading room' becomes an empty 'Causal' pair plus a pair whose 'caused' is stripped as a label, leaving remainder 'the smoke to back…'. The answer gets no local credit, which is acceptable, but readAnswer (registry.tsx:243) also reports causal as missed. So a valid unquoted wider clause shows as not yet identified, against acceptance 2. The quoted form and 'Causal: caused the smoke…' work. The base code behaved the same way, so this is not a regression, and no test covers it.",
      "fix": "After splitting, merge a pair that is only a label into the next part when that part starts with a type word that also appears in the statement as a keyed indicator. Alternatively, skip the boundary when the type word that follows is a keyed indicator of the item. Add a readAnswer test for the unquoted clause form."
    },
    {
      "id": "R2-F2",
      "severity": "low",
      "path": "C:/Users/Joshu/dev/ai-os/handoffs/claudex/spot-confirmed-fixes-20261025/content-release.py",
      "evidence": "Lines 32-37 and 54: when canonical-observed.json exists, preflight re-checks only canonical content and updated_at, then overwrites assignments-before.json with the current assignment metadata. It never compares that metadata against assignments-observed.json. If an assignment's snapshot or state changed between observation and the last preflight, verify (lines 69-78) compares against the new baseline. It would report 'preserved' relative to the last preflight, not the original observation. The helper writes no assignments, so the risk is only the accuracy of the receipt.",
      "fix": "In preflight, when assignments-observed.json exists, require that the current metadata matches it, or report differences, before rewriting assignments-before.json. Or have verify compare against assignments-observed.json as well."
    }
  ],
  "coverage": [
    "Read the full diff for all nine manifest files",
    "Read observatory.ts answerPairs, matchedKinds, confidentPair, indicatorIn, readAnswer and matchesCredited in full context",
    "Traced callers: registry.tsx fastPath (matchesCredited) and stage reading (readAnswer), ActivityLab readAnswer, activityCoachAnswerKeyPayload parity test (KIND_PATTERNS vs Edge TYPE_PATTERNS). Checked that the Edge Function has no pair-splitting copy",
    "Traced the focused filter and whole-prompt guard by hand against every authored multi-type prompt and every single-type prompt containing a comma (Q2, Q3, Q26, Q27, Q28, Q31, Q32, Q36, Q38, Q40, Q47 and others)",
    "Checked the boundary regex against existing test strings (Q27/Q29 forms, the label-only causal at end of string, colon and space separators)",
    "Checked the CoachFeedback reveal's validation of the historical key, its fallback and the non-Spot path",
    "Checked required_parts and indicator alternatives so that joining with 'or' is consistent with local credit",
    "Reviewed the Q3, Q7, Q12, Q14, Q15, Q18, Q21, Q23, Q24, Q26, Q38, Q41, Q42 and Q45 explanation and key edits for modality and threshold",
    "Read content-release.py (preflight/apply/verify, CAS PATCH, source-hash guard), the path list in canonical-target-diff.json, and proof.md",
    "Confirmed the router link at C:/Users/Joshu/dev/ai-os/design/principles.md:29"
  ],
  "limitations": [
    "I could not run tests, typecheck or build; the 231-pass and exit-0 claims in proof.md are not verified by me",
    "I could not compute SHA-256 hashes, so the manifest hashes and the external helper hash B8331BF2… are not independently confirmed",
    "I did not open canonical-baseline-diff.json, the screenshots, the build logs or test-content-release.py in detail",
    "I did not observe live database state, PostgREST behaviour for the updated_at equality filter, RLS scope of assignment reads, or the production deployment",
    "No live AI grader quality or signed-in learner interaction was assessed"
  ]
}

## Publication complete
Verified all staged file hashes and external publisher hash before commit; no post-approval source edits. Commit 8346dfc3ae443169f7c3f24f50f1f30d7e73d459, PR #240, merge eaf82e506bbeb3b5e86f1310f98bad3e818b926a. Lovable latest_commit_sha matched merge before free deployment. New production asset entry and all three markers verified. Canonical activity content CAS succeeded, fresh readback exactly matches source, all four assignment snapshots/states unchanged. Receipt: handoffs/claudex/spot-confirmed-fixes-20261025/release.json. No paid prompts, live grader tests, student-record writes, unrelated files or unreviewed source.

