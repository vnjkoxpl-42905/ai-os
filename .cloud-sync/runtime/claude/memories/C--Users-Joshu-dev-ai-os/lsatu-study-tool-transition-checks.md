---
name: lsatu-study-tool-transition-checks
description: Required prevention checks for LSAT U stateful UI builds after the 2026-10-01 study-tools review.
type: feedback
---

Joshua explicitly requested on 2026-10-01 that Claude retain the study-tools review lessons and adjust its procedure to prevent recurrence. Apply this to future stateful UI work, including annotations, bookmarks, answer controls, drafts, settings, and resumed sessions.

Before implementing, specify the owner of each state value (actor, canonical question, session), its lifetime, persistence path, and behavior on failure. Before handing work back, verify the transitions below with meaningful regression tests and browser checks where needed:

- Account isolation: changing a storage key is insufficient if mounted component state still belongs to the previous actor. Gate on resolved authentication and reset/remount all actor-owned state on an actual actor change. Test A to B and logout/login while mounted, including returning to A; never carry A's marks into B or save them under B's key.
- Failed persistence: retain the current in-memory edits after a failed save. A later edit must build on that current state, not reload the stale persisted snapshot and discard earlier unsaved edits. Test two or more edits with writes failing, then recovery. Disclose device-only/unsaved state accurately.
- Selected-answer invariant: the selected answer must not become crossed out, disabled, or cleared by an auxiliary cross-out action. Preserve existing answer behavior; selecting a crossed-out option must restore it where that is the established runner contract. Test selected-option cross-out and crossed-out-option selection in both LR and RC.
- Reducer persistence: persist the actual committed next state rather than a stale closure or guessed pre-dispatch snapshot. Verify rapid toggles, reload, and current-question clear while preserving other questions and bookmarks. Study aids must not create attempts or alter grading.
- Touch and keyboard: hover-only controls are insufficient. Verify visible, labeled actions with hover:none, actual narrow layout, keyboard activation, and restoration. A desktop screenshot cannot establish touch usability.
- Review accuracy: trace the existing component/state path and use a concrete UI example before declaring functionality absent. The claim that LR find was missing was incorrect; officialSearchTerm and the real stimulus search already supported it. Correct false findings rather than expanding scope to implement duplicate features.

These are release evidence requirements, not a promise that memory prevents every bug. Keep file ownership separate from Codex, preserve student records, run the agreed focused suite/typecheck/build, and obtain independent inspection of the final mixed snapshot after fixes. Report blocked browser checks and unpublished work explicitly.

Evidence: C:/Users/Joshu/dev/lsatu-study-tools-179/docs/implementation-plans/2026-10-01-study-tools-179-verification.md. Initial Claude build and two fix rounds were followed by Codex corrections; the final combined suite passed 311 tests. Do not attribute every final correction solely to Claude or claim the pending narrow-pane check passed.

Additional prevention lesson from the 2026-10-01 weekly/settings review: anonymous legacy device settings have no proven account owner. Do not automatically assign them to the first login. Partial ownership-marker writes or swallowed marker-read failures can copy them into another account. Preserve legacy bytes and fail closed; test every individual storage read/write failure. Teacher publication must acknowledge source/item/backlink writes before final published status, preserve exact partial records for retry, and guard delayed local settlements by originating actor AND student. Cached valid work stays visible during background failure.


Further publication review lesson: stable plan/task IDs do not make a downstream assignment writer idempotent. Trace every nested writer and rollback. A committed write with a lost response must not be retried as a new assignment; block ambiguous creation or use a real stable receipt. Do not claim draft invisibility if shared helpers create visible mirrors. Publication state/recovery must be keyed by actor plus student, and the next write must check the real authenticated actor, not just metadata or a student-only epoch. Test same-student teacher switches and suppress stale notifications.
