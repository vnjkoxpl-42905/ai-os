# Post-session Home review log

Host/planner/builder: Codex. Reviewer/inspector: Claude CLI configured default; no explicit model override. Plan: `C:/Users/Joshu/dev/ai-os/brainstorms/2026-10-27-post-session-home.plan.md`. Three plan rounds, two fix rounds, two fresh inspections. Diagnostics: `research/2026-10-27-post-session-home/`.

User authorized private Drive copy and post-session Home integration. Existing no-commit/push/publish boundary retained. Drive copy tooling began independently before app integration plan review; private copy authorization is not a claim of independent code approval. Backend activation requires separate Lovable deployment confirmation after a concrete tested result exists.

Implementation baseline: e4035d9c; previous local Home redesign remains uncommitted and must be preserved. Review scope is this integration, not a clean approval of all earlier Home changes.

Round 1 started: `review/claudex-l46sd4t9/result.json` (awaiting verdict).

## claudex-l46sd4t9

```json
{
  "verdict": "REVISE",
  "summary": "I reviewed the plan against the Calendar client and the existing worker-ticket callers. The plan has gaps in credential-to-owner binding, ticket design, and cutoff, cursor and rescheduling semantics. I did not inspect the Drive tooling, the migration set or the Home UI in depth. No tests were run.",
  "findings": [
    {
      "id": "F1",
      "severity": "high",
      "path": "supabase/functions/_shared/googleCalendar.ts:17-26",
      "evidence": "getAccessToken uses one global refresh token from env (GOOGLE_CALENDAR_REFRESH_TOKEN). The plan says admin-JWT requests bind the owner to the caller. Nothing ties the caller to the calendar behind that token. Any admin with a JWT can run a sync that reads the one global calendar and writes tasks and attendee emails under their own owner ID. If a second admin exists, or the owner row differs from the token's account, student session data lands under the wrong owner.",
      "fix": "Store the Google account email or calendar ID the token represents, either in settings or as an explicit single-owner config. On each run, verify that the settings.owner_id matches that configured owner and that calendars.get('primary').id matches the settings calendar. Refuse to run if they differ. Do not accept an arbitrary admin as the owner. Add a unit test for the mismatch."
    },
    {
      "id": "F2",
      "severity": "high",
      "path": "supabase/functions/gcal-sync-pull/index.ts:61-68",
      "evidence": "The plan says to reuse the established ticket pattern. The existing pattern calls consume_booking_worker_ticket(_token, _worker), which has no owner argument. The RPC is also not defined in any file under supabase/migrations (grep found only call sites), so its atomicity, expiry and one-use behaviour could not be verified. The plan requires tickets that are owner-bound and checked atomically. Reusing the booking RPC gives neither property. Extending it risks weakening the existing booking workers.",
      "fix": "Add a separate table and RPC for this worker, for example teacher_worker_tickets with owner_id, worker, expires_at and used_at. The RPC should do an atomic UPDATE ... WHERE used_at IS NULL AND expires_at > now() RETURNING owner_id. Restrict it to service_role with REVOKE from public, anon and authenticated. Have the function take the owner from the returned row, not from the request body. Locate and cite the existing ticket RPC definition before claiming it is reused."
    },
    {
      "id": "F3",
      "severity": "medium",
      "path": "plan: Worker / cursor",
      "evidence": "Cutoff, cursor and overlap are underspecified. When a recurring instance is rescheduled, its Calendar event ID may stay the same and the start time changes. The plan says rescheduled events are not labelled ended but gives no rule for tasks that already exist. A task created for an ended session whose event is later moved to the future could be shown as ended. Tasks created before activation_cutoff could appear if the overlap window reaches back past the cutoff. The scan also needs a bound on how far an overlapping window or an old-event revisit can go. Without one, a long outage causes an unbounded Calendar scan.",
      "fix": "State these rules and test them: (a) a task is created only if end >= activation_cutoff and end <= now; (b) the scan window is [max(cutoff, last_success_window_start - overlap), now]; (c) a source-time change on an existing task sets an explicit rescheduled state and does not delete the task; (d) the window has a maximum size, with chunking across runs for longer outages, and a cursor that advances only after the chunk completes."
    },
    {
      "id": "F4",
      "severity": "medium",
      "path": "plan: Worker / matching",
      "evidence": "The plan matches by exact normalized email against the live roster and holds events with ambiguity. It does not define the rules for the cases that cause wrong attachments. These include the teacher's own email as an attendee, multiple student attendees on one event, Gmail dot and plus aliases, a roster email shared by two accounts, and an archived student. Without these rules, group sessions or aliased addresses either create a wrong task or are silently dropped.",
      "fix": "Define the matching rules and add tests. Exclude the owner and resource calendars. Require exactly one roster match among non-declined attendees. Treat more than one match as an ambiguous, held task. Resolve identity through the live roster email and the aliases recorded in the folder-link metadata, with no fuzzy matching. Hold events that match archived or deleted students."
    },
    {
      "id": "F5",
      "severity": "medium",
      "path": "plan: Data and security",
      "evidence": "The plan calls for revoking broad RPC execution and enforcing admin ownership in mutations. It does not say how handle/reopen is protected from concurrent writes, nor how manual checklist changes survive the worker upsert. If the worker does INSERT ... ON CONFLICT DO UPDATE SET with the full row, manual fields can be overwritten. A client that writes handled_at directly could also forge or back-date handled history.",
      "fix": "Have the worker upsert call a SECURITY DEFINER function, or an explicit column-list ON CONFLICT DO UPDATE that excludes handled_at, the checklist and the notes. Give the client SECURITY DEFINER mutation RPCs that use auth.uid() and an admin check. Set handled_at server-side with now(). Reject direct UPDATE on those columns with RLS or column privileges. Add a cross-owner denial test for each RPC."
    },
    {
      "id": "F6",
      "severity": "low",
      "path": "plan: Transcript links",
      "evidence": "The control that attaches a Google Doc link explicitly accepts a user-supplied URL or ID. The plan does not require validation. An arbitrary URL stored and rendered as a link could be a javascript: or phishing URL. A Doc ID parsed loosely could also point at a document in another account.",
      "fix": "Accept only https://docs.google.com/document/d/<id> URLs and extract the ID with a strict regex. Store the ID and rebuild the URL from it. Render links with rel=noopener noreferrer and target=_blank. Add a test that rejects non-Docs and javascript: inputs."
    }
  ],
  "coverage": [
    "The plan text in full.",
    "supabase/functions/_shared/googleCalendar.ts, lines 1-150.",
    "Ticket usage in gcal-sync-pull, gcal-reconcile and single-session-outbox, by grep.",
    "A grep of supabase/ for the worker-ticket RPC definition. It found call sites only."
  ],
  "limitations": [
    "I did not read the uncommitted Home components, hooks or tests.",
    "I did not inspect the Drive setup tooling, because it lives in the vault outside this worktree.",
    "I did not inspect the full migration history, the existing RLS helpers or the admin-auth utilities.",
    "I could not verify the ticket RPC behaviour because its definition is absent from the migrations in this worktree.",
    "I ran no tests, builds or previews."
  ]
}
```

## claudex-3ckg6yhf

```json
{
  "verdict": "REVISE",
  "summary": "The revision resolves the first-round findings F1 to F6 at plan level: owner and Google email pinning, a separate owner-bound ticket table, chunked cursors, exact-email matching, source-only upsert with revisioned RPCs, and strict Docs URL parsing. I found three new defects in the revised text: a cursor race, missing Calendar list parameters, and a conflict between worker and manual transcript writes. The plan is not yet implementation-safe on these points. I verified nothing against source, because no implementation exists yet.",
  "findings": [
    {
      "id": "R2-1",
      "severity": "medium",
      "path": "plan: Worker / covered_through",
      "evidence": "The plan has no run lock or monotonic cursor rule. If a cron tick overlaps a slow run, or a retry and a scheduled call both hold valid tickets, both runs scan the same chunk. A run finishing late can then write an older chunk end over a newer covered_through. The next run rescans harmlessly, but a stale writer can also overwrite last-error or last-success state and mislead the Home status. A rewind past the cutoff is also possible if the write is not guarded.",
      "fix": "Take a per-owner advisory lock or a lease row at the start of each run, and return 'busy' if it is held. Advance the cursor with a compare-and-set: UPDATE ... SET covered_through = :new WHERE covered_through = :expected AND :new > covered_through. Never move the cursor backwards. Add a test for two concurrent runs."
    },
    {
      "id": "R2-2",
      "severity": "medium",
      "path": "plan: Worker / Calendar scan",
      "evidence": "The plan relies on recurring instance IDs and on cancelled events, but it does not require the list parameters that make them appear. Without singleEvents=true, recurring series return as one master event and instance IDs are not produced. Without showDeleted=true, cancelled events are omitted from the list, so cancellations are only found through the 20-task revisit. A 24-hour overlap also misses events created or edited later that ended earlier than 24 hours ago, such as a session added after the fact or an attachment added days later, until the revisit rotation reaches them (which only covers existing unhandled tasks).",
      "fix": "Specify singleEvents=true, showDeleted=true, orderBy=startTime and maxResults paging for the scan. Add a second pass with updatedMin set to the last successful run time, so late-created or late-edited events inside the covered range are found. Test a recurring series, a cancelled instance and a late-created event."
    },
    {
      "id": "R2-3",
      "severity": "low",
      "path": "plan: Worker / Transcript links",
      "evidence": "The source-only upsert includes the transcript Doc ID, because it is derived from the Calendar attachment. The teacher can also attach a Doc explicitly. The plan does not say which wins. A later resync that finds no attachment, or a different one, can silently overwrite or clear the teacher's manual link. Two attachment candidates arriving later can also flip an auto-linked task back to needs review.",
      "fix": "Store the transcript source as 'auto' or 'manual'. The worker may write transcript fields only when the source is not 'manual'. Manual changes go through a revisioned RPC and are recorded in the task-event history. Test that a resync after a manual attach leaves the manual link in place."
    }
  ],
  "coverage": [
    "Full revised plan text.",
    "Host dispositions for the first-round findings F1 to F6.",
    "Calendar scan, cursor, ticket and transcript semantics checked against the plan only.",
    "Round-1 reading of googleCalendar.ts and the existing ticket callers, carried forward."
  ],
  "limitations": [
    "No implementation exists, so nothing was checked against source.",
    "I did not inspect the Drive copy tooling in the vault, which is outside this checkout.",
    "I did not run tests or previews.",
    "The existing booking ticket RPC definition is absent from this repository's migrations, so it remains unverified. The revised plan avoids it."
  ]
}
```

## claudex-tlzy9r02

```json
{
  "verdict": "APPROVED",
  "summary": "The plan now addresses all three round-2 findings. R2-1 is covered by the owner lease, the current-token check on every write, and the compare-and-set monotonic cursor. R2-2 is covered by the explicit list parameters (singleEvents, showDeleted, orderBy, paging) and the updatedMin late-change pass with a frozen-start checkpoint. R2-3 is covered by manual/auto transcript provenance with revisioned attach. I found no new material defects at plan level. Two items for implementation to watch are not blockers. First, the updatedMin checkpoint should be backed off slightly from the frozen run start, to tolerate clock skew with Google. Second, the lease TTL should exceed the longest expected page-fetch time, so a slow but healthy run is not treated as stale.",
  "findings": [],
  "coverage": [
    "Full revised plan text.",
    "Host dispositions for round 2 (R2-1 to R2-3).",
    "Cross-check of the lease, cursor, late-change pass, transcript provenance and ticket sections against the earlier findings F1 to F6 and R2-1 to R2-3."
  ],
  "limitations": [
    "This is a plan-level review only. No app, migration or worker implementation exists yet, so nothing was checked against source.",
    "I did not inspect the Drive copy tooling in the vault, which is outside this checkout, so it needs its own independent review.",
    "The existing booking ticket RPC definition is not in the repository migrations, so it remains unverified. The plan avoids relying on it.",
    "I ran no tests, builds or previews. The approval does not extend to later edits or to the implementation."
  ]
}
```

Plan approval hash check passed b4bfca06c7c420ce40d48428263a5eb0a7553f78a54afd0d807be4f4a43280b3. Approved plan implementation delegated to backend/frontend workers with disjoint ownership. Provider observed Claude Sonnet5.5, CLI2.1.309; no override.


## Implementation inspection claudex-s5wd18eq

```json
{
  "verdict": "REVISE",
  "summary": "The design holds up on the core controls: owner-admin RLS, service-only writes, one-use tickets, lease-guarded source writes, manual transcript and match precedence, strict Doc and Drive URL parsing, and exact-email matching. I found no critical exploit. Three medium defects remain. (1) Every source refresh bumps the task revision, so the teacher's own saves will often be rejected as stale. (2) The UI can read \"up to date\" or \"No after-session tasks are waiting\" when the server job has been failing or has stopped. (3) A conflicting auto transcript is shown as a normal \"Open transcript\" link. A few low items are listed too. I did not run anything; findings come from reading the code.",
  "findings": [
    {
      "id": "F1",
      "severity": "medium",
      "path": "supabase/migrations/20261027190000_teacher_post_session.sql",
      "evidence": "teacher_post_session_source (line 104-108) does `revision=revision+1` on every update of an existing task, including a refresh where nothing changed. Pass 1 re-scans a 24h overlap every ~5 minutes, pass 2 and the 20-task revisit also touch rows, and all of them call this RPC. The home hook refetches every 60s. The teacher's checkbox, Handled or attach call sends the revision it loaded; if a sync ran in between, teacher_post_session_update raises stale_revision (40001). The UI then shows 'Could not save this change' for a valid click. Source columns cannot conflict with the teacher's fields, because the update RPC locks the row and rewrites only its own fields.",
      "fix": "Bump `revision` in the source RPC only when a user-visible field actually changed (compare with IS DISTINCT FROM), or keep a separate source_revision and let `revision` count only teacher mutations. Add an acceptance check that a no-op source refresh leaves `revision` unchanged."
    },
    {
      "id": "F2",
      "severity": "medium",
      "path": "supabase/functions/teacher-post-session-sync/index.ts; src/components/classroom/home/teacher/PostSessionWork.tsx; src/components/classroom/home/teacher/postSessionModel.ts",
      "evidence": "Several failures never reach the settings row. The Google token fetch and the calendars/primary identity check run before the lease claim, and `lease` is still undefined at that point. The `calendar_owner_mismatch` 403 and the token failure in the catch block therefore skip the finish call, so last_error is never written. A dead cron job, an expired refresh token or a failed function also writes nothing. The UI shows only the age of last_success_at and still says 'No after-session tasks are waiting.' (PostSessionWork line 58) and 'Your after-session work is up to date.' (postSessionLede line 51) even when the last success is days old. That is an error that looks like an empty queue.",
      "fix": "Record a bounded last_error / last_attempt_at through a service RPC that needs no lease, for failures before claim. In the UI, treat last_success_at older than roughly 3 sync intervals (for example 20 minutes) as stale. Show a warning and drop the 'up to date' and 'no tasks waiting' wording. Add tests for the stale and never-succeeded cases."
    },
    {
      "id": "F3",
      "severity": "medium",
      "path": "src/components/classroom/home/teacher/PostSessionWork.tsx",
      "evidence": "Line 31 shows 'Open transcript' whenever a doc id exists, otherwise it shows the needs-review text. The migration's source RPC deliberately keeps the previously linked auto doc and sets transcript_status='needs_review' when a different or multiple docs appear. In that state the teacher sees a normal transcript link to a possibly wrong document, with no review marker. This hides the conflict the plan says must be shown.",
      "fix": "When transcript_status is 'needs_review' and transcript_source is 'auto', show the link labelled 'Earlier transcript link (a different document was found \u2014 review)'. Cover it with a component test."
    },
    {
      "id": "F4",
      "severity": "low",
      "path": "docs/ops/teacher-post-session-activation.sql",
      "evidence": "The cron command hard-codes the literal URL 'REPLACE_WITH_VERIFIED_PROJECT_FUNCTION_URL/teacher-post-session-sync'. If `approved` is flipped without editing it, the script enables the settings, sets the cutoff once and schedules a job that fails every 5 minutes. The cutoff is already consumed and the existing-job check blocks a rerun. The script also does not verify that folder links were imported or that drive_root_id is set.",
      "fix": "Add `if url like 'REPLACE_WITH%' then raise exception` before any update, and fail when teacher_student_folders has no rows for the owner. Use a variable for the URL."
    },
    {
      "id": "F5",
      "severity": "low",
      "path": "supabase/functions/teacher-post-session-sync/index.ts",
      "evidence": "import_folders writes settings first, then upserts folders non-atomically. A local_slug that collides with another student's slug (unique owner/slug) throws a 500 after drive_root_id was already updated, leaving partial state. The upsert also resets aliases to only the live account email, which erases any aliases verified later. Dry-run does not detect existing-slug conflicts.",
      "fix": "Detect slug/student conflicts against existing rows in the dry-run and in the live run before any write. Report them as unresolved. Merge aliases rather than replacing them, or perform the writes in one RPC transaction."
    },
    {
      "id": "F6",
      "severity": "low",
      "path": "supabase/functions/teacher-post-session-sync/index.ts",
      "evidence": "rows() pages user_roles ordered by user_id, which is not unique (one user may have several roles), and profiles by class_id. Offset paging over a non-unique sort key can skip or duplicate rows at a page boundary. A skipped admin role row makes that admin look like a non-admin student who can be auto-matched. This is only reachable at 1000+ rows.",
      "fix": "Order by a unique key (add a secondary sort such as role, or use id), or filter user_roles server-side to role='admin'."
    },
    {
      "id": "F7",
      "severity": "low",
      "path": "supabase/functions/teacher-post-session-sync/model.ts; supabase/functions/teacher-post-session-sync/index.ts",
      "evidence": "The plan allows a transcript link from 'an existing uniquely matched ingestion ledger entry'. Only Calendar attachments are implemented, so late-arriving docs not attached to the event never link automatically. Separately, `rescheduled` is set only when stored times differ, and any past-to-past time edit is labelled rescheduled once, then silently reverts to ended on the next sync. A later move to a different past time leaves no persistent trace.",
      "fix": "Either state the ledger path as deferred in the setup doc, or implement it. Persist a rescheduled_from timestamp or an event row (task events table) so the move is recorded, not just a transient state."
    },
    {
      "id": "F8",
      "severity": "low",
      "path": "supabase/migrations/20261027190000_teacher_post_session.sql; supabase/functions/teacher-post-session-sync/index.ts",
      "evidence": "Hardening gaps. (a) The authenticated select grant on teacher_post_session_settings exposes lease_token and lease_until to the owner's browser. The token is useless without service_role, but there is no reason to expose it. (b) Ticket rows are never purged, so one accrues every 5 minutes. (c) The ticket check compares the RPC's lowercase uuid with `!== owner` from the environment, so an uppercase TEACHER_HOME_OWNER_ID would reject every scheduled run. (d) The security-definer functions use search_path=public without pg_temp last.",
      "fix": "Use column-level grants or a view that omits lease columns. Delete expired tickets in the consume RPC or the cron command. Lowercase the owner env value before comparing. Use `set search_path = public, pg_temp`."
    }
  ],
  "coverage": [
    "Fully read: the migration, the Edge Function index.ts and model.ts, the shared googleCalendar.ts, the activation and acceptance SQL, the setup doc, post-session-db-check.mjs, usePostSessionHome.ts, PostSessionWork.tsx, postSessionModel.ts, TeacherHomeView.tsx, useTeacherHome.ts, and the config.toml diff.",
    "Traced: ticket consume and worker auth path, lease claim/renew/source/finish interplay, coverage and overlap arithmetic, the two Calendar passes and checkpoint advance, matching and classification rules, transcript provenance precedence, revision handling between worker and teacher mutations, owner/admin RLS and function grants, and the Home state machine (setup, loading, error, ready, refresh failure).",
    "Confirmed that the /teacher/students/:id/notes and /work routes exist in App.tsx.",
    "Skimmed home.css additions (the post-session block at the end) and the sample-labelling in role-home-preview.tsx; read model_test.ts test names only."
  ],
  "limitations": [
    "Read-only static review. I did not run tests, Deno checks, PGlite, or the SQL, so SQL syntax, plpgsql scoping and RLS behaviour are unverified by execution.",
    "Test bodies for model_test.ts, PostSessionWork.test.tsx, TeacherHomeView.test.tsx and usePostSessionHome.test.tsx were not read in full. I can't say whether F1-F3 are already covered or contradicted by them.",
    "home.css was reviewed only for the new post-session rules. I checked no pixel rendering, no 320/390px layout, no screenshots, no contrast or keyboard behaviour. The large rewrite of earlier Home CSS was not reviewed rule by rule.",
    "Out of scope and unreviewed: the rest of src/components/classroom/home (ClassroomHome, hooks, HomeWeekStrip, useHomeEntrance/Feedback), useInbox, useUserPermissions, teacherHomeModel.ts internals, the vault Drive-copy tooling, the generated manifest, and the real Google Calendar/Drive behaviour.",
    "Live Google API semantics (timeMin/timeMax/updatedMin with showDeleted, 410 behaviour on get) were assessed from documentation knowledge, not observed. pg_cron/pg_net availability and Lovable deployment are unverified."
  ]
}
```


## Implementation inspection claudex-o6z16xuy

```json
{
  "verdict": "REVISE",
  "summary": "I read the migration, the Edge Function (index.ts and model.ts), the activation, acceptance and setup docs, the post-session hook, model and component, and the route targets. The schema, RLS, grants, lease, ticket and cursor design generally match the plan. I found one correctness defect that can silently lose a real session task and a few smaller defects. I could not run any tests or SQL.",
  "findings": [
    {
      "id": "F1",
      "severity": "medium",
      "path": "supabase/functions/teacher-post-session-sync/model.ts:105-110",
      "evidence": "For new tasks, `classify` applies the title exclusion `/consultation|consult call|personal|out of office|holiday/i` before it looks at the roster match. A real roster student's event titled e.g. \"Personal statement session\" or \"Holiday LSAT session\" returns null and never creates a task. `covered_through` still advances, so the session is permanently lost with no needs-match task and no error. The plan says a title may classify an event but must not override a verified student attendee.",
      "fix": "Apply the title exclusions only when there is no roster/alias match. Alternatively, drop the loose words `personal` and `holiday` and anchor the pattern to whole phrases. Add model tests for a matched student with those words in the title."
    },
    {
      "id": "F2",
      "severity": "medium",
      "path": "supabase/functions/teacher-post-session-sync/index.ts:89-93, 312-318",
      "evidence": "`teacher_post_session_attempt` is called for every authenticated action, including `status`, `folder_links` and `import_folders`. It sets `last_error=null` and `last_attempt_at`. An admin polling `status` or `folder_links` therefore erases a real sync error that Home is showing. A failed import (for example `invalid_manifest`, or an exception in the import RPC) writes `sync_failed_retry_pending` into the sync status, so Home says \"calendar connection needs attention\" for a non-sync failure.",
      "fix": "Call the attempt RPC only when the action is `sync`, and for the failure write only in a sync path. Do not clear `last_error` at attempt start. Clear it on a successful finish only."
    },
    {
      "id": "F3",
      "severity": "low",
      "path": "supabase/functions/teacher-post-session-sync/model.ts:116-119",
      "evidence": "A session-like title alone (`/session|tutoring|lsat lesson/`) creates a needs_match task. An event with no attendees, such as a solo \"Planning session\" or \"Webinar session\" block, also creates one. The plan allows holding an unmatched event only when the source explicitly identifies it as a teaching session with guests. This produces false follow-up tasks on the primary calendar.",
      "fix": "Require at least one non-teacher, non-declined guest to hold an unmatched event. Alternatively, require an explicit marker such as a configured color, extended property, or booking-system id."
    },
    {
      "id": "F4",
      "severity": "low",
      "path": "supabase/migrations/20261027190000_teacher_post_session.sql:86-89; supabase/functions/teacher-post-session-sync/index.ts:69-75",
      "evidence": "The scheduled ticket path and `teacher_post_session_claim` never re-check that the owner still holds the admin role. If the pinned owner is demoted, the cron job keeps using the global Google token until `enabled` is manually turned off. The plan binds the worker to an admin owner.",
      "fix": "Add `public.has_role(_owner,'admin')` to the claim's WHERE clause and to `teacher_worker_consume`. Alternatively, check it in the handler for ticket requests."
    },
    {
      "id": "F5",
      "severity": "low",
      "path": "supabase/functions/teacher-post-session-sync/model.ts:35-52",
      "evidence": "The plan allows a transcript link from \"an existing uniquely matched ingestion ledger entry\". Only Calendar attachments are implemented. The setup doc (docs/ops/teacher-post-session-setup.md) says this is deferred. That is honest, but it is a spec gap. Also, the title filter `/gemini|notes|transcript/i` rejects a valid native Doc attachment with any other title, so it stays \"waiting\" with no review flag.",
      "fix": "Keep the deferral documented. Optionally, mark a lone unmatched Google Doc attachment as needs_review instead of leaving it silently waiting."
    }
  ],
  "coverage": [
    "Migration: tables, RLS, grants, revokes, home/update/claim/renew/source/finish/attempt/import RPCs, and the ticket consume function.",
    "Edge Function index.ts (auth paths, owner pin, calendar identity, import, sync orchestration, error handling) and model.ts (classify, coverage, transcript, runWorker paging and passes).",
    "docs/ops activation SQL, acceptance SQL (read through, not executed) and setup doc.",
    "supabase/config.toml verify_jwt=false rationale.",
    "usePostSessionHome.ts, postSessionModel.ts and PostSessionWork.tsx: state handling, URL sanitising, link rel attributes and route targets. The `/teacher/students/:id/notes` and `/work` routes exist in src/App.tsx.",
    "Plan items traced: lease, cursor, rescheduled/cancelled handling, and manual-vs-auto transcript provenance."
  ],
  "limitations": [
    "I did not execute any tests, SQL or Deno checks and make no claim that any pass.",
    "I did not read these in-scope files: home.css (only the diff), TeacherHomeView.tsx, TeacherHomeView.test.tsx, teacherHomeModel.ts, useTeacherHome.ts, model_test.ts, usePostSessionHome.test.tsx, PostSessionWork.test.tsx, post-session-db-check.mjs and role-home-preview.tsx. They are unreviewed.",
    "I did not read the out-of-scope `_shared/googleCalendar.ts`, so I did not verify that `listEvents`/`getEvent` pass the parameters through or that errors carry a `.status`. Whether the 404/410 branch works depends on that.",
    "The live Google Calendar and Drive behaviour, the pg_cron/pg_net availability and the deployed project identity are unverified. The Drive manifest and import tooling live outside the repo and were not inspected.",
    "I only partly checked the SQL semantics by reading, with no real PostgreSQL run."
  ]
}
```
