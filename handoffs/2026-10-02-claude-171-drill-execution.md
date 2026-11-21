# Execute the remaining drill setup contract for ticket #171

## Assignment and delivery

Implement a substantial, bounded slice of LSAT U audit ticket #171: LR/RC builder accuracy and launch clarity, truthful counts/timing, and regression proof of existing score-free Inspect. This is not ownership of the whole ticket or a runner rewrite. Deliver reviewed source, meaningful tests, browser evidence, and a draft PR. Codex will independently review and integrate it. Do not publish or merge.

Current source inspection found that LR already freezes `previewedQids` for launch, and RC already retains inspected ordered passage IDs. Preserve and test those implementations. The concrete RC defects to address first are timing estimates based on requested count rather than actual hand-picked count, weak custom-time validation, and the lack of one authoritative inspected-set launch summary. Verify each finding against your current main before editing.

Repository: `vnjkoxpl-42905/lsatu-684d89db`.
Ticket: https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/171
Parent requirements: #165; decision source: #155.

Codex owns #176 appointment preparation/recap/follow-up links, booking history, and their backend release. You own this drill slice in a separate cloud checkout and branch. Do not copy Codex's unpublished branch into your branch.

## 1. Establish current truth before changing code

1. Start from current remote `main` in your cloud checkout. Record its SHA. Preserve unrelated commits.
2. Read repository `CLAUDE.md`, `AGENTS.md`, and applicable directory instructions. Never replace these files.
3. Read ticket #171, `docs/specs/2026-09-28-competitor-audit-coverage.md`, and `docs/implementation-plans/2026-09-26-lr-drill-setup.md`. The older brief supplies composition/design requirements; its historical draft-PR/status text is not evidence of current implementation.
4. Trace the actual LR and RC setup, preview, launch, resume, Inspect, and result paths. Produce a short acceptance-gap table in `docs/implementation-plans/2026-10-02-drill-171-verification.md`: requirement, current implementation, missing behavior, planned edit, verification.
5. Reuse working behavior. Do not rebuild shipped screens or declare a historical gap still present without checking it.

## 2. Ownership and exclusions

Start with these existing files and their directly relevant tests:

- `src/components/drill/QuestionPicker.tsx`
- `src/components/drill/LrQuestionInspectList.tsx`
- `src/lib/lrDrillSetComposition.ts` and its tests
- `src/lib/lrDrillFilters.ts` and its tests
- `src/components/drill/QuestionPicker.test.tsx`
- `src/features/rc/components/RcHubSurface.tsx` and its tests
- A new pure builder-summary helper and tests under `src/features/rc/lib/`, if necessary
- Narrow builder styles in `src/features/rc/rc.css`, preserving player styles
- Your own verification document named above

This is the implementation allowlist. Read callers and existing tests elsewhere, including SavedSets, to understand integration. Proposed changes outside this list go into a separate follow-up patch description for Codex. If source structure has changed, document the equivalent owning path before implementation.

Do not modify Schedule, session-chain libraries/hooks/panels, booking functions, teacher dossier session panels, migrations, database policies, generated Supabase types, question-bank content, protected timed exam writers, or shared app routing/authentication. Do not edit `Drill.tsx`, `RcPlayer.tsx`, Progress persistence, shared coverage ledgers, or Codex verification records. Do not rewrite Review, Progress, weekly settings, AI coaching, or study tools. A necessary shared-file change must be listed as a separate proposed patch for Codex instead of silently widening ownership.

## 3. Required composition behavior

### Exact LR picks

1. A PT/section/question selection adds the canonical question ID to the proposed set; it does not navigate away or launch immediately.
2. Search is discovery only. It never silently replaces the set or changes the remaining-pool filter contract.
3. Exact picks occupy guaranteed places. Changing filters must not remove them. Show picks that fall outside current remaining-pool filters plainly.
4. Deduplicate canonical IDs. An exact pick cannot reappear through the sampled pool.
5. If exact picks exceed requested size, explain the mismatch and block launch until corrected. Never truncate them silently.
6. Fill remaining places only from the valid filtered pool. Exclude exact IDs before calculating remaining availability.
7. If the pool is insufficient, disclose the actual shortage and block launch. Never pad with unrelated questions or label an incomplete set ready.
8. Preserve supported pasted references/ranges, reporting invalid or unresolved references without silently accepting a different question.

### Preview and launch identity

1. Use one composition result for preview and launch. Once the student previews a sampled set, launching must use those same canonical IDs and order rather than rerandomizing.
2. A composition-relevant change invalidates the old preview visibly. Recompute deliberately before launching.
3. Freeze the launch snapshot before asynchronous persistence. A late save/reply cannot launch a newly edited set under the old preview.
4. Validate all IDs against the loaded bank before launch. During unavailable/failed bank reads, show Retry and block claims of exact availability.
5. Preserve existing run persistence. Continue opens the acknowledged saved run rather than creating a second one.

### RC units

1. Disclose whether requested size means passages or questions.
2. Preview the exact selected passages and associated canonical question IDs.
3. Display the actual launched question count and passage count separately.
4. Respect existing passage grouping and supported selection rules. Do not silently cut a passage or promise an exact question count the composition cannot provide.
5. Reuse the same preview/launch snapshot principle. Do not add unsupported RC selection controls merely for visual parity with LR.
6. Show requested passages, available passage pool, and actual inspected passages/questions separately. Use loaded content for actual question counts. Make hand-picked override explicit; it is not LR-style exact picks plus automatic fill.
7. Calculate estimated and selected timing from the actual selected passage count. Invalid custom time stays editable, explains the problem, and cannot launch; normalize valid values consistently with the existing input contract.
8. If the existing adaptive selector returns fewer passages, either block until adjusted or require explicit acknowledgment of the actual smaller set before Start. The launch summary must never claim the requested count was supplied.
9. A pending Inspect result after a setting change cannot restore stale selection. Missing/misordered/failed content cannot enable Start. Inspect must not expose correct-answer indicators, answer keys, or explanation blocks.
10. Preserve existing `start=1`, `returnTo`, assignment, `ptRun`/`ptLeg`, and canonical manual-section adoption contracts and their tests. Assigned auto-launch need not be forced through the manual Inspect flow.

## 4. Launch modes and Inspect

1. Before start, show the actual supported mode and feedback cadence using plain labels. Distinguish Training/Challenge from timed Test and Inspect from a scored sitting.
2. Preserve the existing mode/source/timing/reveal fields passed to launch. LR's current builder does not expose new timing/feedback mode choices; do not invent controls or claim Training/Test persistence the runner cannot honor. Explain actual current semantics and document broader mode persistence gaps for Codex. No new backend column or protected-writer change.
3. Inspect must load exact content without creating scored attempts, completion records, answer-history entries, Review episodes, or Progress evidence. Trace every writer invoked by its path, including indirect mount/unmount effects.
4. Inspect can use existing read-only study interactions. Opening a question must never submit an answer.
5. Keep answer selection, submission, blind-answer and Reveal controls as already supported. Do not introduce a broad runner-feedback redesign in this task. Document runner changes that require a separately owned slice.
6. Keep Smart Drill's existing one-click behavior. Adaptive current-question state must use the actual current question ID, not assume the queued index identifies it.

## 5. Error, identity and accessibility behavior

- Initial read failures cannot appear as a zero-sized exact pool. Preserve existing selections on a recoverable refresh failure, but disable unverified launch.
- Duplicate clicks cannot create duplicate launches. A save with unknown outcome must recover the exact persisted run before offering a new creation.
- Existing actor/subject separation remains intact. A late result after an account change cannot launch or display the prior actor's saved run.
- Preserve canonical return routes and saved state when inspecting and returning to setup.
- Use existing classroom tokens and components. No new visual theme or copied competitor branding.
- Inputs, add/remove controls, preview and launch must work with keyboard and visible focus. Loading/error text must be understandable without color alone.
- Avoid horizontal page overflow; preserve readable question text and mobile summary placement.

## 6. Required verification

Write regression tests for actual behavioral risks, not assertions that mirror implementation details:

1. Exact picks survive excluding filters and appear exactly once in preview and launched payload.
2. Too many picks and an insufficient remaining pool block launch.
3. Preview/launch share exact IDs and order; filter edits invalidate the prior snapshot.
4. A delayed save cannot launch a subsequently edited composition; duplicate-click and actor-switch handling preserve identity.
5. RC passage/question units and actual counts agree with launched content.
6. Inspect produces no scoring/history/completion writes. Assert writer non-invocation and unchanged evidence in the available integration harness.
7. Load failure/retry preserves editable selections without a false available count.
8. Persisted mode/source survives resume using the current supported contract.

Run relevant existing suites plus added tests, `npm run typecheck`, scoped lint, and `npm run build`. At minimum run `QuestionPicker.test.tsx`, `lrDrillSetComposition.test.ts`, `lrDrillFilters.test.ts`, `RcHubSurface.test.tsx`, and existing SavedSets Inspect tests if present. Inspect generated build churn and retain only intended source changes. Do not alter bank data to satisfy a test. Report preexisting warnings separately.

Run the real application and inspect the changed UI at approximately 390, 820, 1280 and 1440 CSS pixels, plus a docked pane near 700 pixels and doubled text. Verify exact picks, shortage, preview, loading failure/retry and Inspect return paths. Record measured viewport, screenshot/DOM evidence and actual action results. A mocked harness does not prove real authentication, backend permission or persistence.

If cloud browser/auth tools cannot perform a required check, complete the source and tests, state the exact limitation, and leave that acceptance item pending for Codex. Never claim live verification from static output or mock data. Do not use real student accounts, submit new real answers, call paid AI, or modify historical work for a demo.

## 7. Delivery and release boundary

1. Review your final diff for regressions, scope creep, unhandled async identity and accidental Inspect writers. Fix findings and rerun affected checks.
2. Commit only this task on your isolated branch. Never reset, force-push, revert or publish `main`.
3. Respect repository push controls. Do not run a helper that pushes `HEAD:main`. If an allowed draft-PR branch push is unavailable, return commits/patch and explain the limitation instead of bypassing controls.
4. Create a draft PR if permitted by the cloud environment. Do not merge, close #171, deploy an Edge Function, install SQL, or publish Lovable.
5. Report base/final SHA, branch/PR, changed files, before/after behavior, exact checks and results, browser evidence, unresolved acceptance items and proposed follow-up scope.
6. Update the verification document with a requirement-by-requirement evidence table. Distinguish local source completion from production acceptance.

Never redeem or activate Joshua's Claude weekly-usage reset. Do not change billing or usage settings. Lovable credit spending is not authorized by this handoff.

## Completion standard

The deliverable is a reviewable, tested drill setup/Inspect implementation that satisfies the above supported contracts, with every unverified requirement explicitly identified. A PR, successful build or confident summary alone does not establish ticket completion. Codex will independently inspect, integrate and verify the production release.
