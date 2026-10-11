---
name: lsat-u-platform-actions
description: Perform any LSAT U platform action for Joshua directly from the brain workspace — assign guided drills, homework, or activities; post classroom items and notes; send inbox messages; ingest session notes — by driving the deployed app (lsatprep.study) through his logged-in Chrome admin session, verifying the result, and logging it to the student's folder. Trigger on "assign <student> …", "post … to <student>", "message <student>", "send <student> homework", "give <student> an activity", or any request to make something happen on the platform from here.
---

## Current AI OS execution contract

Resolve the actual host browser/CLI before use, preserve marker-based idempotency, exact recipient/action verification and live readback. Do not replace a working transport simply because a reference names another runtime.

# LSAT U Platform Actions

Joshua's workplace is this brain workspace, not the app's admin UI. This skill makes
Claude the operator: he says what should happen to a student on LSAT U, Claude drives
the deployed platform to make it happen, verifies it landed, and records it.

## Mechanism

Use the **claude-in-chrome** browser tools against `https://lsatprep.study` with
Joshua's logged-in Chrome admin session. There is no agent path to the prod Supabase
backend (Lovable-managed, not in MCP scope) — the browser + admin JWT IS the API.
Do not insert rows backend-style; act through the same UI flows Joshua would use,
unless he explicitly asks for a backend repair.

**React controlled-input rule (hard-won 2026-07-16):** `form_input` sets DOM values
but often does NOT update React state, leaving submit buttons silently disabled and
producing zero network traffic. For every form:

1. Click the field and type with real keystrokes (`computer` type action); for
   `<select>`s, click to focus then choose with keyboard (first-letter + Enter) or a
   real option click.
2. Before clicking submit, confirm the button is actually enabled (full-opacity, or
   check `disabled` via read_page).
3. After clicking, confirm via `read_network_requests` that the mutation actually
   fired (POST to `…supabase.co/functions/v1/…` or `/rest/v1/…`) and returned 2xx.
   A UI that merely looks done is not evidence.

## Routing — where each action lives

All under `/teacher` (Teacher Desk). Workspaces via `?ws=`: `people` / `students`,
`library`, `messages`/`inbox`, `admin`, `gmail`, `drive`.

| Action | Surface |
|---|---|
| Assign a guided drill | `/teacher?ws=library&tab=guided-drills` → drill card → Assign. **Delegate to the `guided-drill-assignment` skill** for selection/QA/logging — it is the specialist; this skill is the router. |
| Assign homework / quiz | Teacher Desk library or the student's detail page (`TeacherStudentDetail`) → assign flow → creates classroom item + notification |
| Assign an activity (e.g. Negation Station) | Library activities surface → Assign; verify resume + notification (see `wiki/tasks.md` activity-centre notes) |
| Post a classroom item / note | Student detail page → classroom/dossier tabs |
| Message a student | `ws=messages` (admin side of the 1:1 inbox); supports PDF attachments |
| Ingest a session transcript | `/teacher/session-ingest` (Phase 1A form: Doc URL + student + optional Gmail message id) or the scan/resolve queue on the same page |
| Review/publish a session bundle | Student detail → dossier/review tabs (`SessionBundleReview`); publish is approval-gated |

If a flow's exact clicks are unknown, discover them live with read_page/find on the
real surface — do not guess selectors from memory, and do not invent UI that isn't
there.

## Order of operations (every action)

1. **Identify the student** exactly (roster names include email; ambiguity → one
   concise clarifying question). Check `students/<name>/` for context and
   `assignment-log.md` to avoid repeats.
2. **Do the action** through the UI per the routing table, honoring the React rule.
3. **Verify it landed**: the mutation request returned 2xx AND the UI reflects it
   (item appears in the student's classroom list / message thread / queue). For
   assignments, verify the notification surface where checkable. For any message
   or student-facing text, compare the sent bubble with the approved draft in the
   recipient-facing view. Check paragraph breaks, list lines, and intentional
   spacing. Confirm that exactly one copy landed. If the rendering differs or
   duplicates appear, report the mismatch; do not claim success or resend
   automatically.
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
