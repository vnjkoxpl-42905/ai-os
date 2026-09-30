---
name: lsat-u-platform-actions
description: Operate LSAT U from the AI OS workspace. Publish interactive Classroom lessons through the local lsat-u-lessons MCP server, use the headless admin CLI for other supported actions, verify live state, and log student assignments. In Codex, use its in-app browser for visual verification.
---

For drills, messages, student data, access, signups, due dates, unassign, and unsend, use `assign-lsatu-work`. On Windows, invoke its Node entry point directly instead of relying on Bash being on PATH.


# LSAT U Platform Actions

Joshua's workplace is this brain workspace. LSAT U operations should run headlessly when a supported tool exists. The browser is for checking what a person sees.

## Mechanism

For a self-contained interactive HTML lesson, call the `lsat-u-lessons` MCP tool `publish_interactive_lesson` with the student's exact email, the absolute HTML path, and the title. The local stdio server is `projects/lsatu/scripts/lsatu-lesson-mcp.mjs`; Codex registration is `lsat-u-lessons`. It calls `system/scripts/lsatu-admin.mjs post-lesson`, which authenticates with the workspace's existing LSAT U credentials, posts through `mcp_post_classroom_note`, verifies the new assigned item, and only then archives older notes with the same title. Start with `dry_run: true` to confirm the student and replacement IDs. MCP tools registered during a session may only appear in a new Codex session; the same Node entry point can be used directly in the current session.

The HTML must be self-contained, under 500 KB, inside AI OS, and marked with `<meta name="lsatu-interactive-lesson" ...>`. The Classroom renderer loads it in an opaque-origin sandboxed iframe with scripts and forms enabled. Ordinary notes still go through the sanitizer. If the renderer has changed, deploy the app first and verify Lovable's manual Publish completed before posting the lesson.

For visual verification in Codex, use its in-app browser at `https://lsatprep.study`; in another runtime, use its available browser. A teacher login cannot open another student's `/classroom/item/<id>` route directly. Confirm the item in the student's Teacher Workspace Notes page and in the headless `items --all` result; test slider and answer feedback in a sandboxed preview of the exact HTML. Do not claim a student-session visual check unless one was actually performed.

## UI fallback routing

The current student verification route is `/teacher/students/<student-id>/notes`. Its “Posted to their Classroom” section shows active notes and labels archived notes as hidden from the student. Use the browser's normal controls for any unsupported action, then verify the saved state through a fresh read. In Codex, use the in-app browser, not Chrome. Do not rely on old `/teacher?ws=` routes or old browser-tool names.

## Order of operations (every action)

1. **Identify the student** exactly (roster names include email; ambiguity → one
   concise clarifying question). Check `students/<name>/` for context and
   `assignment-log.md` to avoid repeats.
2. **Do the action** through MCP or the headless Node CLI when supported. Use the UI fallback only for unsupported actions.
3. **Verify it landed**: read the new item from LSAT U, confirm `assigned` and student-visible, confirm the prior same-title item is archived, and inspect the student's Teacher Workspace Notes page in Codex's browser. Check notifications where available. Confirm exactly one active copy; never resend automatically.
4. **Log it**: append to `students/<name>/assignment-log.md` (create if missing) with
   date, action, item, and evidence; drill verifications also go to
   `wiki/guided-drill-verification-log.md`.

## Guardrails

- Every action here hits **real students on prod**. Anything a student will see
  (message text, homework instructions, note bodies) is written in Joshua's voice —
  route through `wiki/teaching-voice.md`.
- If Joshua's request fully specifies the action ("assign Lydia the conditional
  drill"), execute without re-asking. If content is open-ended (a message body he
  hasn't dictated), draft it and show him before sending.
- Fail closed: if verification is ambiguous, say exactly what was and wasn't
  confirmed. Never report an action complete on the strength of a click alone.
- No student-facing action as a side effect of a different request.
