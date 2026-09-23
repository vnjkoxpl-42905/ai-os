# LSAT U admin connector (MCP or CLI): Brainstorm / Discovery Notes
Date: 2026-09-23 · Goal: one easy, grantable way to act on LSAT U as admin (assign drills/activities/sections, message, pull analytics)
Status: in progress
Context sources: connections.md (row 7b), .claude/skills/assign-lsatu-work/SKILL.md, projects/lsatu/scripts/assign.ts

## Found on disk (facts, verified 2026-09-23)
- A CLI already exists: `projects/lsatu/scripts/assign.ts` + skill `assign-lsatu-work`. Covers --activity, --drill, --homework, --section, --message, --schedule, --due, --dry-run, bootcamps. Calls the app's own assignWork() (7 tables + email).
- Auth = Joshua's admin email/password from root `.env` -> 1h JWT. No service-role key outside Lovable.
- Gaps: no analytics commands; no way to grant access to another person without sharing Joshua's password; not an MCP (only works on this machine, in a session that knows the skill).

## Summary / key decisions
(pending)

## Q&A log

## Open flags (pending input)

### Round 1 (clarification, before answers)
- Joshua: must be headless, no browser tab, no browser login; "automatically connected."
- Verified 2026-09-23: `assign.ts --student Celia --message test --dry-run` ran headless, resolved Celia's account via .env admin login, no browser. Requirement already met on this laptop.
- Q1-Q5 still unanswered.

### Round 2 (Joshua: "supercharge this skill", do the work)
Shipped 2026-09-23 (verified by dry runs + live reads):
- `system/scripts/lsatu` front door. Writes run from `projects/.lsatu-ops` (detached worktree, fast-forwarded to origin/main each run). Fixes a live bug: the shared `projects/lsatu` checkout was on another session's branch with an uncommitted assign.ts lacking --section/--due/--set.
- `assign-many "A, B, C"`: resolves every name before writing; one bad name stops the batch.
- `system/scripts/lsatu-report.mjs`: read-only status / qtypes / sections / overdue / quiet / students, --json.
- Discovered: hosted MCP `lsat-u-mcp` v0.3.0 already live at https://atrcqxpmqrynmtvvyjju.supabase.co/functions/v1/mcp (OAuth, admin role gate). Documented in skill. Lacks drills/activities/sections/analytics.
- vite-node rewrites supabase/functions/mcp/index.ts (Lovable plugin); wrapper restores it.

## Open flags (pending input)
- Q1-Q5 from round 1 (who gets access, permission levels, sender identity, analytics wishlist, guardrails) -> Joshua. Decides whether to extend the hosted MCP (Lovable credits).
- `overdue`/`quiet` include former students; no platform "former" flag -> Joshua (archive them on platform?).

### Round 3 (2026-09-23)
- Captured: Joshua: "yes, make the connector do everything." One central place; skill and connector must not be separate implementations.
- Facts found:
  - MCP rejects the CLI's password-login JWT: @lovable.dev/mcp-js requires an OAuth client_id claim by default (requireOAuthClientClaim). Setting it false makes one token work for both.
  - assignWork() (src/lib/assignWork.ts) and its helpers are bound to the browser Supabase client singleton; running them inside the edge function needs the client passed in (refactor, default unchanged for the UI).
  - Existing MCP writes use mcp_* RPCs (migrations); new tools can reuse assignWork instead, so no new migrations.
  - Deploying the mcp edge function goes through the Lovable agent = credits -> needs Joshua's confirmation.
- Proposed design (recommendation, awaiting OK): app repo `src/lib/mcp/tools/` is the ONLY implementation. claude.ai connector, Claude Code, `lsatu` CLI and the skill are all clients of it.

### Round 4 (2026-09-23)
- Captured: Joshua: all platform operations (assign questions/tests/drills/activities, send and retrieve messages, student data) must need nothing from Lovable. "Anything that is Lovable related should not be it."
- Decision: `system/scripts/lsatu` is the one central place. Hosted MCP connector is NOT extended and not used. Supersedes Round 3 proposal.
- Added: `lsatu inbox` and `lsatu thread <student>` (verified live, read-only).
Status: complete

### Round 5 (2026-09-23)
- Captured: Joshua wants every platform operation covered, including new signups, with full access, instant.
- Built `system/scripts/lsatu-admin.mjs` (signups, access templates/grant/revoke, archive/unarchive, items, due, unassign, passes, notifications, read). Reads verified live; writes verified by --dry-run only.
- Deliberately excluded: delete student, admin role changes, schema/app code.
- Open: approve_signup RPC exists in migrations but notifications rows have no status/subject_class_id column, so that migration looks unapplied; `signups` matches by name instead -> Joshua/Lovable if the approval queue is wanted.

### Round 6 (2026-09-23) INCIDENT
- Testing `lsatu draft-send ... --dry-run` sent a REAL inbox message to Adriana Varea at 18:27: only the first line of AI TA draft a34961b6 ("Hi Adriana! Joshua wants to get you on this new weekly training rhythm starting now. Here is your plan:"). Cause: Windows npx shim splits argv at newline, dropping --dry-run. Draft not marked posted. Message not deleted (needs Joshua).
- Fix: wrapper refuses any multi-line argument. Proper fix: assign.ts reads message text from a file.
- 2026-09-23: Joshua applied messages DELETE policy via Lovable SQL editor (migration 20260630000000 had never been applied). Unsent Adriana message 48e3f798; verified gone; she had not opened the thread.
