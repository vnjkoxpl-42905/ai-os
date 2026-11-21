# Assign a complete student work package in one call

Use the local `lsat-u-lessons` MCP tool **assign_student_work** for one student's approved guided drills, activities, standalone drills/bootcamps and interactive HTML notes. It preflights the entire package, writes serially through the app's assignment function, verifies saved content and dates, and returns a generated audit file. No browser, Lovable, custom student transport or manual database assignment rows.

## Normal path

1. Reuse the verified student and already approved homework/note content from the conversation. Search only when a work identifier is missing: **search_assignable_work** covers current activities, published guided drills and the app's actual bootcamp registry. It understands vetted renamed activities such as General Conditionals -> Conditional Rephrase. Never infer difficulty or a conditional-only question pool from a title.
2. Call **assign_student_work once** with the whole package. Its own preflight is mandatory and happens before the first write. A separate `dry_run: true` is optional for unresolved content or a review request, not another routine ceremony after authorization.
3. Use the returned verified IDs, exact HTML hashes, dates, effective question counts/difficulties and notification outcomes. Do not re-list and re-authenticate after a successful complete readback. Inspect state only on a conflict, partial failure or unverified result.

Assignments still need Joshua's authorization. Read-only searches, previews and `verify_existing: true` do not authorize writes. Notes must already be approved; the assignment tool does not invent or approve their content. Preserve separate approval for message bodies outside standard assignment notifications. Do not include other students as a side effect.

## Access flags (2026-11-01)

Bootcamps and activities unlock per item, not by flag. Since 2026-10-02 a profile trigger forces `has_bootcamp_access` and `has_activity_access` to false, so `lsatu access` will always show them off and granting them does nothing. A bootcamp needs only Classroom access plus its assigned Classroom item (`BootcampGate`). The preflight in `system/scripts/lsatu-work-plan.ts` no longer checks the bootcamp flag. Its activity check is unchanged and unverified, so if an activity assignment fails with "lacks access for activity", check `AssignmentGate` and relax it the same way. Never hand-edit the flags.

## One structured plan

```json
{
  "id": "amanda-session-work-2026-10-25",
  "student": "amhuynh@asu.edu",
  "student_folder": "students/amanda",
  "assignments": [
    {"kind":"bootcamp","bootcamp":"unless-drill","due":"2026-11-01"},
    {"kind":"activity","activity":"conditional-rephrase","due":"2026-11-01"},
    {"kind":"guided_drill","drill":"w2-03-must-be-true-first-taste","schedule":"2026-10-25","due":"2026-11-01","level":"beginner","max_difficulty":3},
    {"kind":"interactive_note","html_file":"C:/Users/Joshu/dev/ai-os/brainstorms/2026-10-25-amanda-post-session/recap.html","title":"Rules, Facts, and What Follows"}
  ]
}
```

- One student, 1-20 items. `student_folder` is an existing folder inside AI OS `students/` and routes generated evidence there; it never creates an alternative student home.
- Guided drills require `schedule` and `due`. Keep native counts unless Joshua asks otherwise. Beginner means 1-3, intermediate 2-4 and advanced 3-5; `max_difficulty` is a hard live-pool ceiling. Pinned content overrides level selection and is checked directly.
- Activities and bootcamps default to immediate availability with no due date when those fields are omitted. Dates are strict Gregorian YYYY-MM-DD, interpreted in America/Toronto including DST. Do not use a UTC string slice as the local date.
- Notes use a complete marked self-contained HTML file within AI OS, under 500 KB, and publish immediately. Reuse the same embedded lesson marker for revisions. A revised note is verified before only older matching-marker versions are hidden.
- `dry_run: true` previews with no student mutation. `verify_existing: true` verifies existing exact content and refuses any missing or changed item; it never assigns, archives or notifies. The flags cannot be combined.

## Current chat has old MCP definitions

New tools may appear only after the chat reloads. The immediate fallback is still the real MCP, one command:

```powershell
node system/scripts/lsatu-mcp-call.mjs assign_student_work --file students/amanda/assignments/plan.json
```

Search uses the same client with `search_assignable_work` and a JSON arguments file. Do not rebuild a per-student transport or call raw assignment tables.

## Reuse and failure behavior

### Change dates on existing work

Use `node system/scripts/lsatu-admin.mjs reschedule-plan <plan.json>` for an authorized change to existing homework, activity and guided-drill dates. This edits existing records with exact student/source IDs, expected old dates/status, compare-and-swap, full preflight and readback. Optional `--dry-run` performs no writes. Guided source `scheduled_for`/`unlock_at` and Classroom dates are kept together; homework/activity dates live on Classroom only. It preserves progress and sends no replacement notification. The generated audit records any partial failure and conditional rollback. Inspect it before retrying an ambiguous failure. Example plan: `students/ore/assignments/2026-10-25-reschedule-after-section.json`.

Do not pass changed dates to `assign_student_work` to simulate rescheduling: that tool creates or reuses work by its scheduled identity. Earlier notification text retains earlier dates. Direct activity/guided links do not provide a completion prerequisite or a universal availability lock; explain the intended order and obtain approval for any corrective message or revised note delivery.

A repeat reuses matching existing work without notifying again. Compare stable content IDs and dates, not only titles. Historical completed work remains intact. An ambiguous match, conflicting dates/levels/pins or duplicate active content stops the package before writes. If a later write or verification fails, the response retains completed IDs and notification results. Do not replay a notification failure or assume a failed audit write means the assignment did not land.

The generated JSON audit is the machine delivery record. `audit_file` points to it. It contains exact outcomes, timing and source commit; no credentials. Keep valuable human context in the existing student ledger, but routine delivery does not need another custom proof script or a second operational read.

## Why the runtime is fast and isolated

The MCP shares one writer queue; separate MCP clients share one process lock. An automation-owned checkout is cached by origin/main commit under the sibling application directory. Git refresh is briefly cached; changes to the deployed question pool and student assignments are still checked live. Minimal Vite configuration loads the app APIs without the Lovable plugin that rewrites tracked MCP files. Unrelated shared operational edits are never restored or discarded. Dirty cache entries are preserved and a clean entry is selected.

The orchestration signs in once, resolves the student once and loads the deployed question bank once when needed. The app's own assignWork may perform additional per-item reads. Network and notification calls still take time; do not promise zero latency. Cold checkout preparation is a one-time cost per new app commit. Return measured runtime/cold-versus-warm metrics rather than calling an untested path instant.

Legacy guided MCP tools and the legacy lesson-publishing MCP tool route through the same engine. Direct old `lsatu-admin.mjs post-lesson` is a legacy path with a separate lock; do not run it concurrently with the unified publisher. Use the batch MCP for normal work.


## Measured verification, 2026-10-25

The actual local MCP verified Amanda's four assignments and three published notes together, including exact note hashes, counts/difficulties and local dates. It used one sign-in, one student lookup and one deployed-bank read. Every entry returned already_assigned or already_current and notification:not_resent. No new student work or notifications were generated for testing.

- Fresh sparse cache: 14.311 seconds end to end; checkout preparation 5.908 seconds.
- Immediate cached repeat: 4.634 seconds end to end; application verification 2.765 seconds.
- The earlier full checkout took 43.050 seconds just to prepare, so new caches exclude the unnecessary public question-bank files.

Evidence: `students/amanda/assignments/2026-10-25-recap-homework/mcp-sparse-fast-path-benchmark.generated.json`. Sixteen focused runtime/plan/date tests pass. Live catalog search resolved the legacy General Conditionals name to the verified live Conditional Rephrase ID. Legacy guided preview also passed through the unified MCP engine.

These are read-only existing-item benchmarks, not timing or delivery proof for new assignments. New writes use the app's existing assignWork and note RPC, and include normal notification/network latency. No fresh production assignment or browser acceptance test was added for this engineering change. The broader skills checker remains blocked by six unrelated missing CLAUDE.md peers under a preserved handoff node_modules link; targeted edited-skill links and copy routing pass. Existing shared operational hook edits were preserved.
