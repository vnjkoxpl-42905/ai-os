# Codex writer review, 2026-10-28

Reviewed current assignment writer libraries, inventory and teacher callers, plus merged teacher-post-session-sync source. Read-only source inspection became parent-authorized corrections after supported findings.

## Corrected findings

- TA approval gained email through the shared notifier. Added an explicit sendEmail:false channel choice, truthful email_skipped result, retained existing Inbox and canonical bell.
- Future recap/announcement message notifications were dropped by an early return while their source policy was suppressed. Callers now persist explicit message intent and finalize the durable group. SQL worker owns message queue support and PostgreSQL verification. Future delivery sends no Inbox/email.
- Native/mirror bundle writes did not share the deadline. Forwarded the same AbortSignal to the mirror. Moved the regression assertion outside the error boundary so a swallowed assertion cannot pass the test.
- Session bundle publication could duplicate parts after a saved row but failed draft flags. Replaced source creation with an admin-verified, atomic materialization RPC. Retried parts reuse their existing rows/groups, optional Inbox/email do not repeat, and canonical bells remain retryable.
- Full stale client draft_json writeback could overwrite concurrent edits. Removed it. SQL patches only the materialized part's flags and verifies p_expected_part; advisory ledger advancement stays separate.
- Recap response loss could leave a materialized source without a bell. SQL materializes/finalizes its message group atomically; the dedicated recap notifier optionally finalizes the same group while retaining existing coaching Inbox text and no email.

- Concurrent publishers could split per-part creation across one group, each sending optional notifications. Added owner-authorized durable optional-channel claim before Inbox/email. Only one attempt sends them; skipped results never claim an email or Inbox message was sent. Canonical bells remain independent and durable. Optional channels remain at-most-once best effort after claim, so network loss can omit them rather than duplicate them.

## Verification

7 files, 83 tests passed. Log: codex-writer-corrections.txt. git diff --check clean.

Test files: classroomNotify, assignWork, assignmentWriterInventory, publishSessionBundle, sessionBundleNotify, readingCenterAccess, agentActions.

New teacher-post-session-sync code contains no student assignment source writes. It writes teacher desk/session operational records through separate RPCs.

## Limits

Source and local test evidence only. No production mutation, real-student notification, publish, or commit performed by this worker. Parent owns final integrated typecheck/build/rendered evidence, database verification, independent review and release. SQL implementation and deployed old-client compatibility require database worker's final evidence.
