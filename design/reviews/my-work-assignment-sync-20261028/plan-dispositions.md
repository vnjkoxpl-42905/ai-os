# Dispositions after s0dh6j6g

Accept F1-F11. The revised plan now distinguishes the weekly-plan publisher from curriculumSchedule, recaps/messages from assignment alerts, delayed in-app delivery from immediate inbox/email, reused PT row issuance from retry identity, and legacy generic alerts from exactly mapped item alerts.

F1: two-phase schema with activation off, then verified frontend, then activation. New frontend writers explicitly persist policy. Legacy defaults are not flipped under cached clients; activation rejects stale legacy teacher inserts/reactivations before creating work with a Refresh error. Existing PT edge defaults auto (it never notifies), source-backed mirrors inherit native policy, updated SQL MCP functions explicitly set policy. Student reads remain open. Test cached old writer before/after activation. This chooses a version gate rather than guessing which legacy generic summary belongs to which source rows.

F2: server-owned issuance counters on source and Classroom records; source/mirror canonical resolution agrees, genuine reactivation increments, progress/retries do not. PT source+mirror paths tested without edge deployment.

F3: preserve one generic immediate weekly-plan-ready summary without future task content, with explicit publication group and suppressed per-item pings. Separate curriculumSchedule day bundles notify only at their unlock. Test both seven-day flows.

F4/F5: explicit assignment type allowlist; recaps/announcements do not get a second assignment alert. Scheduled individual/bundle/ReadingCenter work sends no immediate bell, inbox or email; only in-app delivery occurs at unlock. No deferred email worker or historical sends.

F6: existing rollback may remove only rows created in the same failed attempt. Delete triggers cancel pending events; recovery waits ten minutes beyond bounded client timeout and rechecks source/publication. Finalization begins outside the rollback boundary, so notification failure cannot delete committed work. No host deletion of existing records.

F7/F9/F10: exact work/issuance identity carried to ambiguous destinations; a PT listing cannot read all PTs. Legacy exact routes are mapped; generic unmappable summaries retain click-to-read. A group clears when all delivered members are read, or when its explicit collection is successfully loaded from the alert; collection acknowledgment clears only the alert, never document receipts. Individual remaining unread labels stay true.

F8/F11: remove obsolete link/unread unique index in both live and repo-baseline tests; durable per-issuance delivery identity replaces it. delivered_at persists independently of notification row deletion. No redelivery after dismiss/delete.

No feature implementation or production data changes yet. Prior visual changes are safely committed72077d75 and merged with current origin/main in localaabb5f197bc85ce7cb10a5c54e671130f5b9e647; unrelated dirty MCP source remains excluded. Please review the updated plan, not treat these dispositions as implementation proof.

## Round 2 claudex-x6smy4ku
All five findings accepted. N1 dedicated protected columns and trusted-only reactivation; N2 source-authoritative nonthrowing PT mirror inheritance and exact edge replay tests; N3 live locked schedule eligibility and reschedule updates; N4 retain activation-off cohort for rechecked release; N5 bounded complete writer inventory/static payload tests and active-gate payload verification. Plan refinements appended before implementation GO. Final independent implementation inspection remains mandatory.
