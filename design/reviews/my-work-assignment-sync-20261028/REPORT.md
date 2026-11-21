# My Work release and synchronization

Date: 2026-10-28. Provider: Codex, at Joshua's explicit request.

## Review and checks

Independent Codex inspections covered database delivery, frontend identity/read routing, assignment writers, and the subsequent corrections. No material findings remain within the reviewed scope. PostgreSQL checks used both index baselines, silent migration replay, owner/privilege tests, and concurrent session-part and notification-claim races.

The integrated regression run passed 971 tests across 74 files. A subsequent isolated legacy Inbox-summary correction passed 32 route tests. The application typecheck and full production build passed, including the guarded main push gate. Initial release: afe73265d914e8160601f8efb5b11e36e6754b7e. Final owner-aware revision: 18fc8af7e1ff7d83defb62b9e0d8dd720f90b3a3.

## Student data preservation

Five transactional migrations were installed with delivery disabled. A sixth reviewed forward migration subsequently corrected administrator-owned read tracking while retaining cross-student ownership checks. Exact before/after digests matched across 89 owner/source groups, 31 notification owners, and all 499 messages. No existing work, completion dates, authored content, notification history, or message records were deleted or rewritten by the backfill. No historical notification burst occurred.

The owner projection audit covered 37 accounts: 339 canonical work identities, 305 currently available and 34 unavailable/future identities. It backfilled 193 defensible receipts and mapped 229 historical alerts. The 13 unmapped alerts are 10 generic Classroom summaries, one generic Inbox summary, and two activity links whose source rows no longer exist. These histories were preserved; no work was fabricated to repair deleted targets.

## Behavior

Actual foreground content loads track read state separately from assignment progress/completion. Canonical work identity and issuance keep Home, My Work, sidebar counts and associated notifications aligned. Future assignment and recap notifications wait until availability. Retries reuse durable events; concurrent session publication reuses existing parts and preserves newer authored content. Optional Inbox/email notifications are best effort with an atomic at-most-once claim; the in-app bell is durable.

## Evidence limits

The earlier desktop/tablet/phone/sidecar and normal/reduced-motion evidence uses actual components with synthetic adapters. The recovered local browser error tab was policy-blocked and was not bypassed. Real student accounts were not impersonated and no test assignments, messages or emails were sent to students. Signed-in live UI, final public bundle and activation readback are recorded below when complete.

## Publication

Initial release was published and verified with the public work-sync marker. Delivery was enabled with cron job 381 (* * * * *); an actual scheduled worker run succeeded. The final owner-aware frontend revision was published after Lovable matched SHA 18fc8af7e1ff7d83defb62b9e0d8dd720f90b3a3. The public bundle changed and contains issuance-read-owner-20261028. Delivery control records that verified SHA, cron job 381 is active, and its actual worker run succeeded. Later unrelated Progress changes landed on main after this deployment; the reviewed release remains an ancestor and the current public bundle retains its marker. Those Progress changes are outside this review.

Live opening of an existing owned unread course cleared the My Work badge from 1 to 0. It remained Assigned, completed_at stayed null, and the ten to-do assignments remained ten. Messages stayed at four unread. An already-read note preserved its original read_at while updating last_opened_at. Subsequent readback showed only expected own-account read metadata changes; other source groups, messages and notifications were unchanged.

Published notes were checked at 390, 768, 1054 and 1440 CSS viewport widths with no horizontal overflow. Desktop and phone screenshots were opened; the reduced-motion reader was also opened and inspected. Viewport and media emulation were restored. No real student accounts were impersonated.

The owner-role correction passed both six-migration PostgreSQL baselines, replay and concurrency tests. Bootcamp ownership tests passed 11/11. After the latest main integration, seven relevant suites passed 77/77, with the guarded application typecheck and production build passing. The first upload retry encountered a transient GitHub DNS failure; the subsequent guarded push succeeded.

## Final acceptance record

- Public notes page reloaded signed in and rendered successfully. Current public bundle: index-CQImAh7y.js, retaining the owner-aware marker.
- Final scheduler readback: enabled, one active minute job, successful run, 194 receipts, zero newly generated historical events, 499 messages.
- Final completion/read checks: the owned course has status assigned and completed_at null with a persisted read receipt; original note read_at retained.
- All emulation was cleared. The live notes tab remains open as the deliverable.
- The unrelated dirty supabase/functions/mcp/index.ts hash remains 5359c2de7a28b626a3d2523d83b6fbd3e1777a0d5a60bb9757ed4bb2ee446f26 and was excluded from every commit.
- Limits: no physical-device testing, impersonated student sessions, actual new production assignments, or outbound test messages/emails. Future delivery was exercised in disposable PostgreSQL; the real scheduled worker was verified without generating fictitious student work. Optional Inbox/email delivery remains best effort. Two historical activity alerts have deleted targets and remain preserved.
