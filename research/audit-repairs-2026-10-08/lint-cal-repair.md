# Historical link recovery and Cal.com sweep repair

Verified 2026-10-08. Findings F20 and F24 from the full AI OS audit.

## Historical evidence remains unchanged

The wiki history was not rewritten. Seven distinct retired application-worktree destinations (eight occurrences) have surviving dated documents in the current application checkout. Exact copies of those surviving documents are retained here, with SHA-256 and source paths in [historical-links.json](historical-links.json). Their filenames/date match the historical destinations, but byte identity with the deleted worktree generation is not established. The resolver only accepts a recovery when the recorded hash still matches.

Recovered navigation:

- [2026-09-30-foundation.md](historical-evidence/lsatu-connected-experience/docs/agent/verification/2026-09-30-foundation.md) from `../../lsatu-connected-experience/docs/agent/verification/2026-09-30-foundation.md`.
- [2026-09-30-timed-pt-writer-readiness.md](historical-evidence/lsatu-connected-experience/docs/implementation-plans/2026-09-30-timed-pt-writer-readiness.md) from `../../lsatu-connected-experience/docs/implementation-plans/2026-09-30-timed-pt-writer-readiness.md`.
- [2026-10-01-study-tools-179-verification.md](historical-evidence/lsatu-study-tools-179/docs/implementation-plans/2026-10-01-study-tools-179-verification.md) from `../../lsatu-study-tools-179/docs/implementation-plans/2026-10-01-study-tools-179-verification.md`.
- [2026-10-01-activity-ai-admission-readiness.md](historical-evidence/lsatu-ai-grading-integrity/docs/implementation-plans/2026-10-01-activity-ai-admission-readiness.md) from `../../lsatu-ai-grading-integrity/docs/implementation-plans/2026-10-01-activity-ai-admission-readiness.md`.
- [2026-10-01-progress-history-173-verification.md](historical-evidence/lsatu-progress-173/docs/implementation-plans/2026-10-01-progress-history-173-verification.md) from `../../lsatu-progress-173/docs/implementation-plans/2026-10-01-progress-history-173-verification.md`.
- [2026-10-01-week-settings-180-verification.md](historical-evidence/lsatu-week-settings-180/docs/implementation-plans/2026-10-01-week-settings-180-verification.md) from `../../lsatu-week-settings-180/docs/implementation-plans/2026-10-01-week-settings-180-verification.md`.
- [2026-10-02-drill-171-codex-release.md](historical-evidence/lsatu-review-197/docs/implementation-plans/2026-10-02-drill-171-codex-release.md) from `../../lsatu-review-197/docs/implementation-plans/2026-10-02-drill-171-codex-release.md`.

The machine profile was already present at `system/windows-machine-profile.md`; lint had omitted top-level system records from basename indexing. Two other targets resolve to actual files in this project's native Claude memory. Two backtick-delimited examples are now ignored as examples. No placeholder pages were created.

Structural lint now reports **0 findings across 48 wiki Markdown pages**. This is link/provenance structure coverage, not proof that every claim is current or every historical direct link is navigable in Obsidian. Use the recovered links above for the retired destinations.

## Cal.com errors no longer appear as an empty sweep

The report-only sweep checks HTTP success, API success, valid JSON, booking shape and cursor pagination. It uses the current documented list version `2026-05-01`, advances `nextCursor`, rejects missing/repeated cursors and stops with failure after 100 pages per status. A 30-second request timeout bounds stalled calls. It deduplicates bookings by UID across upcoming/past lists. No zero-booking conclusion is printed until both statuses finish successfully. Pending status is described as requiring review, not proof of failed payment.

Cancellation remains an explicit existing `--cancel` operation and was not invoked. No live API call, booking cancellation or payment change was performed for these repairs. The old cancellation endpoint version remains unchanged; no write-side API migration is claimed.

The list pagination implementation follows [official Cal.com documentation](https://cal.com/docs/api-reference/v2/bookings/get-all-bookings).

## Checks passed

- `py system/scripts/test_wiki_maintenance.py`: 4 tests, including hash tampering, actual/missing native memory, inline examples versus actual broken links, and top-level system records.
- `node --test scripts/calcom-pending-sweep.test.mjs`: 5 tests, including HTTP 401, invalid JSON/API errors, multi-page cursor traversal, deduplication, valid empty completion, malformed response/record, missing/repeated cursors and page-cap failures.
- `py system/scripts/wiki-maintenance.py --lint`: 48 pages, zero findings.

Remaining limits: historical worktree byte identity is unverified; machine-local memory is not automatically navigable inside Obsidian; no live Cal.com read or cancellation compatibility test was run.
