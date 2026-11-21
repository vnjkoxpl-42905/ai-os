# Sections post-section rebuild: build in progress

**Date:** 2026-11-20
**Tags:** lsat-u
**Plan:** `C:/Users/Joshu/dev/lsatu-sections/plans/sections-post-section-rebuild.md` (approved after 8 Codex rounds; Joshua's 4 decisions recorded)
**Audit:** `docs/audits/2026-11-18-sections-post-section-review-audit.md`

## Where the work is
- Worktree `C:/Users/Joshu/dev/lsatu-sections`, branch `feat/sections-post-section-rebuild` off `origin/main` (fde63d8f). Not pushed. No PR yet.
- `node_modules` there is a junction to `C:/Users/Joshu/dev/lsatu/node_modules` (`npm ci` fails on main: lock file out of sync with two `@lovable.dev` plugins). Remove the junction before deleting the worktree.
- Baseline worktree `C:/Users/Joshu/dev/lsatu-baseline` (detached at origin/main, also a node_modules junction) exists only to compare test failures. Safe to remove.
- Main already has 21 failing test files. List: `C:/Users/Joshu/dev/baseline-fails.txt`. This branch adds no new failures.

## Done and verified
1. **Live SQL applied 2026-11-20 on Joshua's "Yes, run it".** File `docs/implementation-plans/artifacts/2026-11-20-sections-post-section-rebuild.sql` (SHA256 602727ff...). Checked live afterwards:
   - 3 new columns exist on `section_history`.
   - The 4 functions are security definer, with no execute for `anon` and execute for `authenticated`.
   - RLS is on for `standalone_section_sittings` and `section_review_records`, and `authenticated` cannot insert or update either table.
   - 39 existing history rows are untouched.
2. **PGlite verification:** `node scripts/verification/sections-post-section-rebuild-sql.mjs --pglite-module <scratchpad pglite>`, 70 checks pass. PGlite has a single connection, so true concurrency (the advisory lock) is not exercised.
3. **Phase 1 client (commit 4th from top).** `src/lib/sectionCloseout.ts`:
   - In `handleFinishSection` (Drill.tsx), a standalone or assigned full section (`isStandalonePoolKey(genericResumeKey)`) closes out through `close_standalone_section_v1` instead of `commitSessionAttempts`.
   - `LRSectionResults` receives `savedHistoryId` and writes nothing. It only emails, and only when the row was created now.
   - Tests: `sectionCloseout.test.ts`.
4. **Phase 2 client.** `src/lib/sectionReviewRecord.ts`:
   - Prediction and BR save through the two functions when `sectionHistoryId` is set.
   - BR no longer writes `attempts` rows on that path. The legacy `saveBRResults` is still used when no history id exists.
5. **Phase 2.7:** every `attempts` reader has `.not('br_selected', 'is', true)`. Guard test: `src/lib/attemptsReaders.test.ts`.
6. **Phase 3.1:** `src/lib/sectionRelease.ts`.
   - `sectionHistory.ts` merges review records (`mergeReviewRecords`) and drops BR-sealed rows. This covers SectionHistoryList, StudentWorkPanel, ReviewQueue and `fetchOwnedSectionHistoryItem`.
   - `withoutBrSealedRows` is applied in `practiceSectionAttempts`, `firstAnswerSources`, `studentAnalytics` and `RecentPerformanceWidget`. RecentPerformanceWidget also now hides unfinished practice-test legs (new finding).
   - On a failed lookup it fails closed and hides rows.

## Deviations from the plan (tell Joshua)
- **Phase 1.3 is only partly built.** The sitting is opened at finish, not at section start, and resume storage keys are not yet bound to the sitting id, so there is no adoption on start. Close-out is still atomic and retry-safe. Not yet done: a stale tab can still overwrite resume answers (pre-existing behaviour).
- **Attempts written by the new close-out omit `confidence`.** The SQL insert has no column for it. Adding it means a SQL change, which needs Joshua's approval.
- **BR grading differs for questions left untouched in BR.** They keep their first-pass result. Previously they counted as wrong when not in `brResults`. Whole-section BR passes every question, so in practice this is the same.
- **Not browser-verified yet.**

## Remaining, in order
- **3.2–3.4:** route `/review/section/:historyId` with a `SectionReport` built from saved data.
  - Extract the LRSectionResults display parts into `src/components/section-report/`.
  - Walk adapter `sectionHistoryToWalkSession`. `SectionReviewWalk` grades from the saved `correctAnswer`.
  - "Do blind review" later for unsealed rows, via `EnhancedBlindReview` then `saveSectionBlindReview`.
- **3.5:** `/testing/attempts/section/lr/:id` resolves a history id and redirects to the report. A resume-only id keeps the score page with the label "saved summary". Protected "View section report" (`PracticeExamPages.tsx:243`) links to the report (F1).
- **4:** `mergeSectionIntoJournal` in `reviewQueueModel.ts`:
  - Add regret and changed-in-BR items from review records.
  - Merge with journal items only on a matching `sitting_id`; journal items now carry `sitting_id`.
  - `SectionReviewDetail` becomes a redirect to the report.
- **5:** `listPracticeSectionAttempts` dedupe against sittings (`adopted_from_record_id`), a conformance test, `src/pages/CONTEXT.md` plus `src/components/drill/CONTEXT.md`, and `wiki/log.md`.
- **Then:**
  - Browser-verify as a test student on dev server 8080: a standalone section, an assigned section (sealed until BR), retry after a forced failure, a protected-path report. Screenshots at the responsive matrix, light and dark.
  - Push with `bash .claude/safe-push.sh` (check how it handles the 21 baseline failures) and open the PR. Never merge without Joshua.
  - After merge: free `deploy_project` and prove it live, per standing rule.

## Handoff prompt
```
Read C:/Users/Joshu/dev/ai-os/handoffs/2026-11-20_sections-rebuild-build.md and continue the sections rebuild in C:/Users/Joshu/dev/lsatu-sections from "Remaining, in order". Read the plan first.
```
