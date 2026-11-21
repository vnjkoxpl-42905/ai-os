# PR #191 independent verification

Reviewed 2026-10-02 against `brainstorms/2026-10-02-schedule-176-execution-spec.md`.
PR: https://github.com/vnjkoxpl-42905/lsatu-684d89db/pull/191
Baseline: `124fee3a4f14952c5b05abcf3bedd18dd22d1f18`.
Head: `3d2fb5efd29678a1efd9a04af6b3de1c50734e6c`.
Isolated checkout: `C:/Users/Joshu/dev/lsatu-review-191`.
Verdict: REVISE. No merge, source fixes, publication, production mutation, Claude messages, credits or weekly-reset controls performed.

## Release blockers

1. Session associations disappear during ordinary work saves. `src/hooks/useBootcampProgress.ts:66-82` replaces metadata with only bootcamp_id/progress, erasing the new session_chain on the next autosave. New model permits bootcamp_module links. `src/lib/markNoteRead.ts:30-34` writes cached metadata wholesale, so opening a note can erase a newer teacher link or restore a removed association. CAS on the new writer alone does not protect against later blind writers. Fix compatible metadata writers with fresh merge/CAS and meaningful interleaving regressions, or gate affected association writes until safe.
2. Teacher association is not server-controlled. Existing own-row student-update guard allows arbitrary metadata changes. A student can forge/move/remove a session association which the teacher projection accepts. No foreign-data exposure was found because item/booking ownership is filtered. Still violates the specified teacher-controlled contract. Backend prerequisite must be explicit and mutation gated until supported; do not claim frontend controls enforce server authorization.
3. `src/pages/MyWorkNotesPage.tsx:125` silently returns null on itemsFailed. Failed session-link reads disappear without a retry notice. Handle item-source failure distinctly and add a regression; current test covers booking failure only.

## Additional gaps

- Canceled bookings are recognized by the panel but omitted by the normal student calendar adapter. Without a saved deep link or linked note/recap, canceled sessions containing only drills are not discoverable. Provide a verified history selection path.
- Teacher query keys and writer epoch bind to subject but omit actor. Selected-student remount protects student switching; actor-switch safety is not demonstrated. Include actor context and regression coverage before claiming it.
- `git diff --check BASE HEAD` fails for a new blank line at EOF, `src/hooks/useSessionChain.ts:301`. Claude's clean-working-tree diff check missed committed whitespace.

## Independent proof

- 125/125 tests across 11 files passed: new model/hook/panel/Schedule route tests, TodayAgenda, Notes, scheduleEntries, booking adapter, classroomItems/helper routes, DossierWork.
- Full typecheck passed.
- Production build passed; canonical-content postbuild checked 769 files.
- Scoped ESLint: zero errors, one existing Notes exhaustive-deps warning.
- All changed source/test/CSS/fixture files reviewed through two independent read-only reviewers plus host inspection. Verification document and screenshot inventory inspected; teacher mobile-dialog screenshot viewed.
- Known generated build churn restored only in this initially clean review checkout: public/data/_bank.generated.json, public/data/finder-address-index.json, supabase/functions/mcp/index.ts.

Browser screenshots supplied by Claude are mocked isolated panel evidence, not independent real-account/full-Schedule/dossier/Notes-shell acceptance. No fresh live task walk was performed: material source blockers already prevent release approval. No whole-ticket completion claim. Claude's disclosed limitations were useful but do not waive required safety gates. A passing test suite does not cover the identified missing scenarios.

## Revised-head review, 2026-10-02

Head: b729407d3515cb2eabb3681617aa7e25f24f9124. This checkpoint supersedes the earlier source verdict for 3d2fb5e; it does not certify deployment or close #176.

Verdict: bounded read-only frontend slice passes independent source review. The complete session-linking feature is not ready for publication. Teacher add/move/remove controls are gated off in production pending a server guard/RPC. No backend migration is included in this PR.

Corrections verified: note-read and bootcamp writes fresh-read metadata, recompute changes, and condition writes on updated_at with bounded retries; regression tests exercise actual writers. Notes exposes loading, failures, stale data and retry. Past/canceled sessions have a selection path. Teacher query/cache/writer context includes actor and student. Stored associations are labeled unverified. Committed whitespace check passes.

Independent verification: 143 tests across 13 files passed; full typecheck and production build passed; scoped ESLint has zero errors and one existing Notes exhaustive-deps warning. Two read-only reviewers found no remaining material defect in the bounded data/UI scope. Build-generated churn in the initially clean review checkout was restored only for the three known generated files.

Limits: Claude-supplied mocked full-page screenshots were inspected; no independent live real-account browser walk was performed. Server mutation protection and real-account acceptance remain outstanding. History is limited by the existing latest-30 booking query. Claude documents a preexisting 10px Schedule header/tabs overflow at 390px with doubled text. No merge, publication, deployment, credit spend, or weekly-usage reset was performed.
