# Spot the Relationship: one-turn Lovable repair

Joshua authorized one paid build prompt on 2026-10-13. This is the exact prompt submitted to the existing LSAT U project. No additional paid prompts or grading tests are authorized.

```text
Finish the Spot the Relationship grading upgrade end to end in this LSAT U project. Implement, verify, and deploy the necessary Lovable Cloud backend changes in this single build turn. Do not stop after adding database fields or writing a plan. Do not change unrelated features.

Verified current state:
- Main includes the released Observatory repairs (916f195e) and newer unrelated Reading Center work. Preserve both.
- Live activity slug spot-the-relationship, id 12251bd3-d260-4108-bc35-bcf478e483e6, has 48 items. Each now has answer_key with relationships [{type, indicators, connects, why}], traps, context_benchmark, and sometimes required_parts.
- instructions.coach now has grading_rubric as well as the older rubric and partial_rule. The sole unstarted assignment has these additions; both completed assignments remain unchanged.
- These database additions have not been captured in the repository content.
- A captured-model-request test shows structuredKeyReachesModel=false and newGradingRubricReachesModel=false, while oldRubricPresent, explanationPresent, creditedAnswerPresent, and firstAttemptHintRule are true.
- Existing instant grading/dials and admission tests pass.

Repair these concrete gaps:

1. Authoritative grading payload and receipt identity.
The canonical payload in supabase/migrations/20261001120000_activity_ai_admission_v1.sql (activity_ai_source_v1) currently excludes item.answer_key. supabase/functions/activity-coach/grading.ts likewise has no structured-key field in its CanonicalPayload, destructuring or user prompt.
Read the complete key from the authenticated, authorized source snapshot server-side, validate it, and carry it through to the model. Include relationship types, accepted indicators, connections, reasons, traps, contextual benchmark and required parts.
Include the complete key in canonical receipt identity, source-change checks, cache reuse and second-attempt source confirmation. An answer-key-only change must invalidate obsolete cached judgments and prevent dispatch/finish under a changed key. Preserve existing ownership, revocation, budget, idempotency and concurrency protections.
Use a new migration; do not edit applied migrations. Fail safely before any provider call for malformed upgraded keys. Keep an explicit legacy path for unrelated activities and historical snapshots without structured keys. Never replace an old assignment's key with the current activity definition when its snapshot differs.

2. Make the model use the actual rubric.
grading.ts currently spreads only brief.rubric and ignores coach.grading_rubric. Establish explicit precedence: consume the upgraded relationship grading rules when present, with compatible legacy handling when absent. Validate them server-side.
Grade each type with its own indicator, not as a bag of independently occurring words.
Correct requires all required types with valid indicators and no invented or contradictory pair.
Partial applies to genuine valid work with missing types, missing indicators, indicator-only answers or mislabelled pairs.
Incorrect means neither the types nor indicators demonstrate valid recognition.
Accept equivalent names, capitalization, quotation styles and reasonable wider spans. Required separated comparative phrases need both halves. Apply this consistently to items 25, 34, 39, 40, 43 and 48.
Comparisons may refer to another object, a numeric benchmark or an earlier state clear from context. Count distinct types, not every separate claim.
On the first unsuccessful attempt, give a useful hint without quoting the key's indicators or listing the missing types. Student answers remain untrusted data, never instructions.

3. Resolve content contradictions and keep one source of truth.
Import and validate the live structured keys into src/features/activity-centre/content/spot-the-relationship.json so the repository and database agree; preserve reviewed question wording and indicators.
Item 36 currently treats identifying only "softer than" as a comparative trap, although one valid indicator per type is sufficient. Accept "conditional, when; comparative, softer than; causal, drives". Explain "longer" as another valid comparison, not a required second indicator whose omission is penalized.
The older rubric groups "provided" with necessary-condition words. Separate sufficient language ("if", "provided", "whenever") from necessary language ("only if", "requires", "depends on", "contingent on"). Correct the active rubric without reversing any reviewed key.
Audit all 48 keys for the same conflicts and for accurate complete connections. All 48 must have useful student-facing explanations. Expand earlier count-only or difficulty-only notes (including item 29) using their authored connections and reasons. Do not merely count or rename the relationships. Keep wording plain, precise and free of production notes and em dashes.

4. Final explanation and instant grading.
The grader receives the full key and explanation privately. The student sees no key or completed explanation during the question or first retry.
After resolution, including a correct answer, show authored reasoning explaining every required type, its indicator and what it connects. Retain the credited-answer reveal at its existing appropriate point and preserve the hint/retry flow.
Keep the current instant-correct path, affirmative-only and conservative. Do not mark an incomplete, swapped or conflicting pair correct. Ambiguous answers go to the Coach. Keep successful instant answers free of model calls and retain the earned dials and restored run progress.
Avoid two divergent grading keys: validate parity or consume the same reviewed structured contract while preserving historical fallback.

5. Verification and deployment in this one turn.
Add and run meaningful tests:
- All 48 structured keys agree with reviewed types, indicators, complete connections and split-phrase requirements.
- Capture the actual server-to-model request in a mocked provider test. Assert the complete structured key, upgraded rubric, explanation and attempt number are present. Assert malformed keys stop before the provider call.
- PostgreSQL tests proving key-only changes invalidate cache/source identity, including dispatch, finish and second-attempt checks. Use an isolated test fixture or rollback transaction; do not alter real student attempts.
- Exact correct, type-only, indicator-only, missed type, invented type, swapped pairs, conflicting extra pairs, contextual comparison and split-indicator cases. Distinguish deterministic contract checks from actual model accuracy.
- First-failure hint boundaries and complete final explanations for instant and AI-resolved answers; restore earned dials after reopening.
- Typecheck, focused regression tests and production build; inspect the rendered explanation flow at desktop and phone width.

Synchronize the live activity and only eligible unstarted assignments with no responses. Preserve completed and in-progress assignments, grades and attempts. Verify saved content by fresh readback.
Apply the migration and deploy activity-coach through Lovable Cloud's supported deployment path; commit all source and migration changes to GitHub. Do not revert main, reset history or overwrite unrelated work.
Do not run additional paid grading/model tests beyond this authorized build turn. Use mocked providers for the test matrix. Do not send student messages or notifications.
Leave frontend publication to our free publish-and-verification step after review.

Return exact changed files, commit SHA, migration/deployment results, test results, one sanitized captured payload showing the new fields, assignment preservation results, and any remaining limitation. Do not claim live AI accuracy from mocks or call anything deployed without checking it.
```
