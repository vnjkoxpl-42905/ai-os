# PR #197 independent review

Reviewed 2026-10-02. Repository: vnjkoxpl-42905/lsatu-684d89db. Head: 890be999f90ad630c993a1a4a83dd5ce1a506c0f. Verdict: corrections required before merge or publication.

## What works in the reviewed source

LR previews are stamped with their composition, stale previews cannot launch, exact picks are retained, and launch IDs are deduplicated. RC reports actual passage counts and loaded question counts, validates custom pace, requires acknowledgment for undersized sets, and prevents simultaneous Start clicks. Source changes respect the assigned ownership boundary.

## Required corrections

1. **P1: uncertain creation can be bypassed.** In `src/features/rc/components/RcHubSurface.tsx:458-484`, pending creation is checked only for identical current passage IDs. Choosing another set bypasses it. Keeping IDs but changing timing or reveal also changes the configuration used by recovery. Capture the complete immutable launch request, including actor and route scope. Resolve the original uncertain request before another creation. Test changed IDs, timing, and reveal after failed creation plus failed read-back.
2. **P1: recovery can select an unrelated existing drill.** At lines 509-515, a matching in-progress drill started up to two minutes before the click can be accepted. The predicate omits source, practice-test leg, and protected sitting identity. Use persisted request identity where available; otherwise establish a pre-create baseline and recover only a uniquely new, exact-scope candidate. An older matching row is not evidence of the attempted save. Test an older matching drill and different test legs.
3. **P2: bind async launch/recovery to the account.** Delayed create/read-back replies can navigate after the account changes. Capture the actor, check it after awaits, and invalidate pending state and account-derived history on actor change. Test delayed responses across an account switch.

Do not remove these safeguards to make tests pass. Keep runner/backend changes separate if a persisted request identity requires broader scope. Do not change official question-bank content.

## Independent verification

- Four focused suites passed: 71 tests, including QuestionPicker, LR composition, RcHubSurface, and RC summary.
- Independent typecheck and production build passed; postbuild checked 769 files. Build emitted asset/chunk warnings.
- Independent source review found the defects above; passing existing tests does not cover those scenarios.
- Claude's reported 356 tests and full-suite baseline comparison were not independently rerun in this review.
- Real signed-in Start, save, resume, results, and RLS recovery acceptance remain outstanding.
- Attempt mode/source persistence remains outside this builder slice; #171 must stay open.

## Browser and release status

The Claude Code web session's file viewer opened and rendered its verification Markdown file. Its separate Changes panel displayed "No changes to show." The committed source was independently read from GitHub in an isolated checkout.

PR #197 was open, draft, and mergeable when checked. This review did not merge, push, deploy, publish, send a Claude prompt, spend credits, or redeem usage. Mergeability does not establish release readiness.
