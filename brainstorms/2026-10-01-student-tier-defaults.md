# Student tier defaults: Brainstorm / Discovery Notes
Date: 2026-10-01
Goal: Define clear default feature presets for Tier 1, Tier 2 and Tier 3.
Status: Interview in progress.

## Summary / key decisions
- Joshua confirms Tier 1 must enable every feature.
- Tier 2 should enable a defined subset; Tier 3 should enable fewer features.
- Exact subsets are pending this interview.
- Prior interview: brainstorms/2026-09-22-student-access-tiers.md. Prior Tier 2 was custom switches, not a settled middle preset. This request reopens that default.
- Prior decisions retained provisionally: manual tier selection; no automatic payment grants or expiry; assigned work authorizes its own runner; per-student overrides persist.

## Q&A log
### Starting request: fixed defaults
- Captured: “Tier one should have all enabled, tier two should have certain ones enabled, and tier three should have even less.”
- Requested investigation: explain “TA worksheets,” including how many if applicable.

## Open flags (pending input)
- Current preset and TA worksheet implementation research -> Jay 2.
- Tier 2 and Tier 3 intended student use and exact switches -> Joshua.

### Q1 — Tier 3 default
- Captured: Tier 3 enables only Classroom, Messages, Schedule and booking, and Export.
- All other feature switches default off.
- This adds Export to the earlier three-feature floor.
- Assigned-work runner behavior remains a prior decision, not re-confirmed by this answer.
- Follow-up requested: explain what a TA worksheet is before deciding further.

### Research — TA worksheets and current presets
- Verified in local origin/main source, not a fresh production database check: TA means Teaching Assistant assignments. Approving a Teaching Assistant draft creates a student-specific worksheet with HTML content, optional assets/PDF, and sometimes response fields/answer key.
- No fixed worksheet catalogue/count. Each worksheet is an assignment created for a student.
- TA switch is redundant for assigned worksheets: AssignmentGate allows the owning student to open their assigned TA worksheet even when the switch is off. It does not grant a browseable catalogue.
- Current Tier 2 applies no switch changes. Switching from Tier 1 to Tier 2 therefore retains everything on.
- Current Tier 3 excludes Export, so Joshua’s new preset requires a change when implementation is authorized after discovery.
