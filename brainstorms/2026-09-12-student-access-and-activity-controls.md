# Student Access and Activity Controls: Brainstorm / Discovery Notes
Date: 2026-09-12 · Goal: Define the teacher-facing controls for student access, activity visibility, and duration-based access in LSAT U.

## Summary / key decisions

- A teacher should be able to open a student and see the last time the student was active.
- A teacher should be able to inspect the student's question and drill activity, with the exact scope and detail still to be defined.
- A teacher should be able to toggle a student's platform access off from the teacher workspace.
- Turning access off is an immediate, reversible suspension. The student's account, history, assignments, and messages remain intact.
- Turning access off must not send the student an email.
- A suspended student may reach an access-inactive notice, but every product area is locked: drills, questions, assignments, notes, messages, and normal sidebar navigation.
- The student list or communication area should provide an easy numeric control for setting an access duration in days, with the exact behavior still to be defined.
- The behavior when clicking a teacher's name in the teacher workspace is reported as needing a fix; the intended destination still needs clarification.

## Q&A log

### Q0 — Initial request
- Asked: User initiated product discovery and invited a `/grill-me` interview.
- Captured: Add student last-active visibility, comprehensive student activity history, a reliable teacher-workspace student detail interaction, an access on/off toggle, and a quick numeric days control for access duration.
- Flags: Exact meanings, permissions, data detail, and expiration behavior remain to be resolved with Joshua.

### Q1 — Meaning of turning access off
- Asked: Should access-off immediately block all LSAT U content while preserving the student's account, history, assignments, and messages?
- Captured: Yes. The student loses access immediately, but the account and all associated history, assignments, and messages remain intact. The action is reversible rather than deletion. It should not email the student, unlike the current behavior.
- Flags: Define the exact suspended-student screen and any content or actions that remain available.

### Q2 — Suspended-student experience
- Asked: Should a suspended student retain messaging, or see only an inactive-access screen?
- Captured: Lock everything. The state should resemble having no platform access before onboarding. The student gets no drills, questions, assignments, notes, messages, or other product areas. They should quickly understand that access is inactive. No normal sidebars should remain visible.
- Flags: Final wording and whether the blocking screen includes a contact method or only a sign-out action.

## Open flags (pending input)
