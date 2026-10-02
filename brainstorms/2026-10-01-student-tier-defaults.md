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

### Q2 — Remove redundant switches and bundle review
- Captured: remove TA worksheets from the tier/access controls. Context interpreted as removing its toggle; deletion of assignment content is not authorized.
- Drill includes Wrong answers and Flagged questions.
- Practice tests also includes Wrong answers and Flagged questions.
- Remove independent Wrong answers and Flagged questions toggles.
- Derived access rule: either Drill OR Practice tests enables both review features.
- Joshua asks what Export does; source investigation pending.
- Tier 2’s full preset remains undecided.

### Research — Export
- Verified against local origin/main source: has_export_access has no runtime consumer gating a route or export action. It is stored and displayed, but currently changes no export behavior.
- Existing download/export actions (including assigned TA PDF download and Principle-Flaw review CSV) do not check it.
- Recommendation pending Joshua’s answer: remove this ineffective toggle and let downloads remain part of the feature the student can access.
- Implementation has not started; tier discovery continues.

### Q3 — Remove Export toggle
- Asked: remove the ineffective Export toggle and include downloads within accessible features?
- Captured: Joshua confirmed “yes.”
- Remove Export as an independent access control; downloads belong to the feature the student can access.
- Updated Tier 3 visible preset: Classroom, Messages, Schedule and booking only.
- Supersedes the earlier request to include Export as a Tier 3 switch.
- Remaining visible controls: Drill, Practice tests, Activities, Bootcamps, Progress and history, Classroom, Messages, Schedule and booking.
- Tier 2 default remains pending.

### Q4 — Pause to explain Progress and history
- Asked: approve proposed Tier 2 defaults?
- Captured: Joshua is confused by “Progress and history” and requests an explanation before continuing.
- Tier 2 preset is not approved. “everyone drilling practice tests” is ambiguous and not treated as a settled default.
- Interview questions paused while Jay 2 checks what this control actually gates.

### Research — Progress and history
- Source-verified in local origin/main: has_analytics_access gates Progress Overview, History and Topics.
- Overview summarizes practice performance, including accuracy by question type/difficulty and first answers versus repeat attempts.
- History shows past practice and question attempts, including results and time.
- Topics summarizes Logical Reasoning topic accuracy.
- Turning this access off locks those pages; it does not stop saving practice results or independently control Wrong answers/Flagged access.
- Explanation is source-based, not a fresh production UI verification.

### Q5 — Bundle Progress and history
- Captured: remove the independent Progress and history toggle.
- Automatically enable its pages when Activities OR Practice tests OR Drill is enabled.
- Joshua explicitly included Activities in this rule.
- Wrong answers and Flagged questions remain bundled with Drill OR Practice tests, per Q2; extending those to Activities has not been decided.
- Remaining visible switches: Drill, Practice tests, Activities, Bootcamps, Classroom, Messages, Schedule and booking.
- Tier 1: all seven enabled.
- Tier 3: Classroom, Messages, Schedule and booking enabled; four practice/content switches off.
- Tier 2: pending exact selection.
