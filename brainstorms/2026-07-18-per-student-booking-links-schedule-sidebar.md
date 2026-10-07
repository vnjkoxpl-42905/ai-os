---
type: brainstorm
subject: Per-student booking links on the teacher Schedule sidebar Brainstorm / Discovery Notes
updated: 2026-07-18
aliases: []
---

# Per-student booking links on the teacher Schedule sidebar: Brainstorm / Discovery Notes
Date: 2026-07-18 · Goal: Nail down exactly how per-student booking/scheduling links should appear and behave on the teacher Schedule page (`/teacher/schedule`) left sidebar, before writing code.

## Context (from code, already read)
- Booking system is fully custom (NOT Cal.com/Calendly). Layers:
  - Teacher pass manager: `src/pages/teacher/BookingPasses.tsx` at `/teacher/booking-passes`. Creates private link `/schedule/pass/<token>`; copy/rotate/revoke. Passes keyed by name/email typed into a form (NOT student_id currently, though the `create` edge action accepts `student_id`).
  - Student booking: `src/pages/BookingPass.tsx` at `/schedule/pass/:token`. Pulls Google Calendar slots, books, debits a credit, creates Meet event.
  - Backend: edge functions `booking-pass`, `booking-pass-admin`; tables `booking_passes`, `booking_pass_redemptions`, `schedule_events`, `gcal_sync_state`.
- Teacher Schedule page `src/pages/teacher/TeacherSchedule.tsx`: left sidebar is `HubStudentList` ("Pick a student"); right is a per-student month calendar for classroom items (notes/recaps). Nav in `TeacherShell.tsx` lines 39-40 has both "Schedule" and "Booking passes" as separate items.
- `booking-pass-admin` create accepts `student_id`; the UI form does not pass it yet.
- Known gap: no cancellation flow (credit refund) — TODO at BookingPass.tsx:314.

## Summary / key decisions
- **Q1: One link per student, create-if-missing.** Pick student in sidebar → see their booking link + Copy button. No link yet → "Create booking link" button. Rotate/revoke inline. Not a fresh link every click; not the full manager.
- **Q2: Keep `/teacher/booking-passes` as the full-list overview.** Add the per-student quick control on the Schedule sidebar for day-to-day. Two surfaces share one backend.
- **Process:** user invoked `/grill-me-codex` → after interview, write PLAN.md and have Codex adversarially review before code.
- **Q3: Panel at top of the right pane.** Selecting a student shows a compact booking card above the month calendar (link/grant + Copy + Rotate + credits). Sidebar stays a clean student list.
- **Q4: Quick-create defaults** = 5 credits, 60-min, no expiry. Custom via full page.
- **Q5: One active pass per student, backend-enforced.** Creating a new grant auto-revokes any prior active pass for that student.
- **Q6→Q7 PIVOT: booking is built INTO the student's in-app calendar (`/schedule`).** Logged-in student books directly (identified by auth), NO token URL. Teacher "grants booking access" from the Schedule panel.
- **Q8: No access = hide booking entirely** (no dead buttons).
- **Q9: No student self-cancel** (handled off-app via Joshua).
- **Q10: Exactly one reschedule per session**, student-initiated, no credit change.

### FINAL SHAPE
Teacher `/teacher/schedule`: per-student panel (top of right pane) to grant/ensure ONE active booking pass (5/60/none default), see credits, copy link, rotate, revoke. Backend enforces one active pass per student_id.
Student `/schedule`: if they have an active pass, a "Book a session with Joshua" surface shows open slots (Google freeBusy via booking backend) and books directly (auth-identified). Each booked upcoming session can be rescheduled once. No cancel. No pass = no booking UI.
Backend: authenticated student booking path (new `student-booking` edge fn or auth mode) resolving pass by `auth.uid()`; shared slot/book/reschedule/redeem logic; migration adds `reschedule_count` to redemptions + partial unique index for one-active-pass-per-student.

## Q&A log
### Q1 — Behavior of the per-student link control
- Asked: When you pick a student, what should the booking-link control do?
- Captured: **One link, create-if-missing.** Each student has ONE booking link. Selected → show link + Copy (+ Rotate/Revoke inline). If none, "Create booking link" button. Implies: passes must be keyed to `student_id` (booking-pass-admin `create` already accepts it; must dedupe/find existing per student).
- Flags: none

### Q2 — Fate of the standalone Booking passes page
- Asked: Keep or remove `/teacher/booking-passes`?
- Captured: **Keep as full-list overview.** Standalone page stays as the all-students management view; Schedule sidebar gets the per-student quick control. Both hit the same backend.
- Flags: none

### Q3 — Placement of the control
- Asked: Where does the per-student link control appear?
- Captured: **Compact panel at the top of the right pane**, above the month calendar, shown when a student is selected. Sidebar stays a plain list. Card holds: link + Copy, Rotate, and credits remaining.
- Flags: none

### Q4 — Defaults for quick-created passes
- Asked: What defaults when creating a link from the Schedule panel?
- Captured: **Quick-create, one click**: 5 credits, 60-min sessions, no expiry. Rotate/Revoke after. Custom credits/length/expiry still available on the full `/teacher/booking-passes` page.
- Flags: none

### Q5 — Which pass shows when a student has several
- Asked: A student may have multiple passes over time. Which does the panel show?
- Captured: **One active enforced by backend.** At most one active pass per student. Creating a new link auto-revokes any prior active pass for that student. Panel always shows exactly 0 (→ Create) or 1 active pass.
- Implications: (a) `booking-pass-admin` `create` must, for a given `student_id`, revoke existing active passes in the same transaction before inserting the new one. (b) Add a `get_for_student` / `list?student_id=` action returning the active pass (or null). (c) Consider a partial unique index `UNIQUE (student_id) WHERE status='active' AND student_id IS NOT NULL` to enforce at DB level — **flag for Codex**: does this break the existing standalone page which can create name/email-only passes with NULL student_id? NULL student_id rows are exempt from the partial index (multiple NULLs allowed), so should be safe, but confirm.
- Flags: DB-level enforcement vs app-level → decide in plan; Codex to stress-test race + NULL student_id interaction.

### Q6 — Delivery of the link → PIVOT
- Asked: How does the created link reach the student?
- Captured (user's redirect, verbatim intent): "in their calendar they should have the ability to schedule it — it should be integrated into their current calendar." → **The student should NOT receive a raw pasted link. Booking should be built INTO the student's own in-app calendar.** Student opens their calendar (`/schedule`) and can schedule a session with Joshua right there.
- Code finding: student page `src/pages/Schedule.tsx` at `/schedule` ALREADY EXISTS — month/week/day calendar, `GoogleCalendarPanel`, `TodayAgenda`. It has NO booking/slot/pass ability today. The pivot = surface booking slots + "book a session" inside this existing student calendar, reusing the `booking-pass` edge function's slots/book actions.
- **Reframed feature:** (1) Teacher side: per-student booking-link/entitlement control on `/teacher/schedule` (grants the student the ability to book, sets credits). (2) Student side: a "Book a session" surface embedded in `/schedule` that shows Joshua's open slots and books — no token URL needed for logged-in students; the student is identified by auth.
- **Big open question for user (Q7):** does the student still need the token link at all, or does an authenticated student book directly (pass keyed to their student_id, no URL to paste)? This changes the auth model of `booking-pass` (currently token-gated, anonymous).
- Flags: booking-pass edge fn is currently token-only/anonymous → needs an authenticated path keyed to student_id if students book from inside the app. → Codex to review auth change.

### Q7 — Student booking auth model (THE pivot fork)
- Asked: How does a logged-in student book from their calendar?
- Captured: **Book directly, no link needed.** Logged-in student opens `/schedule`, sees "Book a session with Joshua" + open slots + credits remaining, and books. Identified by their auth session (student_id). NO token URL. Teacher grants booking access + credits via the Schedule panel.
- Implications:
  - Backend: need an AUTHENTICATED booking path. Options: (a) new edge fn `student-booking` that authenticates via JWT, finds the caller's active `booking_passes` row by `student_id = auth.uid()`, and reuses the same slots/book/redeem logic as `booking-pass`; or (b) extend `booking-pass` to accept an authenticated mode (no token, resolve pass by auth.uid()). Prefer (a) to keep the anonymous token path untouched, OR refactor shared slot/book/redeem into `_shared/` and call from both. → Codex to weigh.
  - Teacher "create booking link" becomes "grant booking access": creates/ensures an active pass keyed to student_id with default 5 credits / 60 min / no expiry. The token link still exists (for the standalone page / non-account users) but is not the student's primary path.
  - Student `/schedule` (`src/pages/Schedule.tsx`) gains a booking surface (button → slots sheet → book), reusing slot rendering logic conceptually from `BookingPass.tsx`.
  - Access gating: which students can book? Presence of an active pass = they can book. Teacher grants it. (No pass → no booking UI, or a "ask Joshua for access" empty state.) → confirm in Q8.
- Flags: Codex to review new auth path + shared-logic refactor + RLS (student may only read their own pass, only book their own).

### Q8 — Student with no booking access
- Asked: What does a student with no active pass see on their calendar?
- Captured: **Hide booking entirely.** No pass → calendar looks exactly as today, no Book button. Booking UI appears only after Joshua grants access (creates active pass). Matches "no dead buttons / don't expose unavailable actions" product rule.
- Flags: none

### Q9 — Cancellation policy
- Asked: Can a student cancel, and what happens to the credit?
- Captured: **No student self-cancel.** Students cannot cancel in-app. Cancellations happen off-app (student messages Joshua; he adjusts Google Calendar / pass). → No refund logic, no time-cutoff, no credit-return path needed. Simplifies build.
- Flags: none

### Q10 — Reschedule policy
- Asked: Can a student reschedule a booked session?
- Captured: **Exactly ONE reschedule per session.** A student may move a booked session to another open slot at most once. After that one reschedule, it's locked (further changes go through Joshua). No credit change on reschedule.
- Implications:
  - `booking_pass_redemptions` needs a reschedule counter/flag, e.g. `reschedule_count int NOT NULL DEFAULT 0` (or `rescheduled_at timestamptz`). Enforce `reschedule_count < 1` before allowing a move. → schema change (small migration).
  - Reschedule flow: pick new slot → conflict re-check (freeBusy + exclusion constraint) → PATCH the same Google event to the new time (keep same Meet link) → update `schedule_events` + `booking_pass_redemptions.start_at/end_at` → increment counter → send updated invite (sendUpdates=all). Must be atomic-ish with rollback like `book`.
  - The exclusion constraint `no_overlapping_bookings` on booked redemptions: moving start/end must not collide; the UPDATE will be checked by the constraint. Handle the conflict error → "that time was just taken."
  - UI: on a booked upcoming session in the student calendar, show a "Reschedule" action ONLY if `reschedule_count < 1` and session is far enough out (reuse the 60-min lead rule). After use, hide it.
- Flags: Codex to review reschedule atomicity, one-time enforcement (race: two concurrent reschedules), and Meet-link preservation.

### Code finding — data model (resolved by reading code, not asked)
- `booking_passes.student_id uuid REFERENCES auth.users(id) ON DELETE SET NULL` is a REAL column (migration 20260708111013) and is in generated types. `booking-pass-admin` `create` action already accepts `student_id`.
- **Implication: NO schema migration needed** for the core feature. Per-student lookup = query `booking_passes` by `student_id`. Gaps to close in code: (a) the existing create UI doesn't pass `student_id`; (b) `booking-pass-admin` has no "find existing pass for student" / list-by-student action yet — needs a `list` filter or new action; (c) HubStudentList rows key by `class_id`, but the student's real `auth.users` id is `student_id`/`user_id` on the row — must map correctly.

## Codex review round 1 — VERDICT: REVISE (12 findings)
Codex (gpt-5.6) adversarial review of PLAN.md. Key catches:
1. Partial unique index: NULL behavior correct, BUT migration must first resolve pre-existing duplicate active student_id rows, and account for stale 'active' rows past expiry (auto-expire only happens on read).
2. **Copyable link impossible for existing passes** — only `token_hash` stored, raw token shown once on create/rotate. `get_for_student` can't rebuild the URL. → USER DECISION Q11: **DROP the link entirely.** Teacher panel = grant/manage access (credits, revoke), no copyable link. Token link stays only on standalone page.
3. Do NOT add student SELECT policy on `booking_passes` — RLS can't hide `token_hash` column → would leak the bearer hash. Use edge-fn safe DTO / restricted view instead.
4. Reschedule flow not atomic: concurrent requests both patch Google + clobber DB, loser's rollback undoes winner. Need locked conditional DB update + explicit Google compensation.
5. `reschedule_booking` must check conflicts against BOTH `booking_pass_redemptions` AND `schedule_events`, excluding the redemption's own event (exclusion constraint alone is insufficient — matches how `redeem_booking_pass` checks both).
6. Meet preservation: patchEvent sends partial JSON; must preserve attendees+conferenceData, handle deleted/cancelled Google events, use etag/stale-write guard.
7. Revoke-then-insert NOT atomic across two supabase-js calls → must be ONE DB RPC with per-student lock + 23505 handling.
8. Service-role auth: every action must derive identity from verified JWT, never trust caller-supplied ownership fields; scope pass by student_id=user.id, redemption via that pass; use verified user's email. This IS the security boundary (service role bypasses RLS). Add negative-authz tests.
9. **Student calendar can't read `schedule_events`** — migration 20260712074608 made it admin-only, but `GoogleCalendarPanel.tsx:109-123` queries it for all users. Need a student-safe event source (scoped edge-fn booking history). (Implies student calendar's Google panel may already be broken for non-admins — verify.)
10. Integration: specify where booked sessions render in `Schedule.tsx` and how reschedule attaches; don't let students inherit admin-only sync/edit from GoogleCalendarPanel.
11. Shared refactor: extract only pure slot-gen + carefully parameterized pipeline AFTER tests; don't let token identity and auth identity cross paths.
12. Add tests: dup active passes pre-migration, concurrent creates, concurrent reschedules, reschedule cancelled/failed/others' redemption, stale Google events, PATCH failure, DB reject after PATCH, second reschedule, expired/revoked, no-pass student sees nothing.

### Q11 (from Codex #2) — Existing-pass link UX
- Captured: **DROP the copyable link entirely.** Students book in-app (no URL needed). Teacher panel = "Grant / manage booking access" (grant, credits remaining, adjust, revoke), NO link shown for existing passes. Standalone `/teacher/booking-passes` keeps the create-time-only token link for non-account use.

## Codex review rounds 2 & 3 — converged
- Round 2 (Rev 2): REVISE, 8 findings — all implementation-spec gaps (token_hash NOT NULL blocker, migration idempotency, reschedule atomicity/compensation, crash reconciliation, error mapping, DTO enumeration, post-rotation history, calendar surfaces). Folded into Rev 3.
- Round 3 (Rev 3): REVISE, but Codex explicitly marked grant-locking (#2) and shared-core boundary (#8) RESOLVED. Remaining 8 are mechanical SQL-correctness nits: invalid 6-char SQLSTATE `PT409B`→5-char, `<>`→`IS DISTINCT FROM`, `SET search_path=public` on each RPC, compensate idempotency guard + marker clearing, reconciler retry/missing-event rules, remove GoogleCalendarPanel from student render tree, etag/If-Match acquisition (or drop it), ensure CHECK constraint exists.
- **DECISION: stopped the Codex loop at round 3.** Architecture is sound; residuals are code-time polish, captured in PLAN.md "Implementation notes — Codex R3 polish". Three rounds each cost real time/tokens; further rounds would be syntax nits, not design. PLAN.md is at `projects/lsatu/PLAN.md` (Rev 3 + impl notes). Awaiting Joshua's sign-off before any code (per grill-me-codex Act 2 end).

## Open flags (pending input)
