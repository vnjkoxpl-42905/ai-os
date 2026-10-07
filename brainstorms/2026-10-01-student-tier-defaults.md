# Student tier defaults: Brainstorm / Discovery Notes
Date: 2026-10-01
Goal: Define clear default feature presets for Tier 1, Tier 2 and Tier 3.
Status: Interview in progress.

## Confirmed specification (2026-10-01)

| Feature | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| Drill | On | Off | Off |
| Practice tests | On | Off | Off |
| Classroom | On | On | Off |
| Messages | On | On | On |
| Schedule and booking | On | On | On |

- These are the only five visible permission switches.
- Drill OR Practice tests includes Wrong answers, Flagged questions, and Progress and history automatically. No independent switches.
- Remove TA worksheets and Export switches; downloads remain part of accessible features.
- Activities and Bootcamps are accessible only through explicit student assignments with Classroom access (Tier 1 and Tier 2 defaults). No general access switches. Tier 3 has communication only.
- Tier 2 can open and complete explicitly assigned drills and sections through Classroom without independent practice access.
- Selecting a tier applies its actual preset. Manual overrides remain saved. No payment grants or expiry.
- Earlier Q&A is provenance; this confirmed specification supersedes earlier alternatives.
- Implementation is in progress in sibling lsatu-tier-defaults worktree. No real student access has been changed during QA.

## Initial request / discovery history
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

### Q6 — Correct Progress and history dependency
- Captured: Joshua explicitly excludes Activities from enabling Progress and history.
- Corrected rule: Drill OR Practice tests automatically enables Progress and history.
- Supersedes Q5’s Activities OR Practice tests OR Drill rule.
- Unified review dependency: Drill OR Practice tests includes Wrong answers, Flagged questions, and Progress and history, with no independent toggles for those three.
- Tier 2 proposed preset remains unanswered.

### Q7 — Activities are assignment-only
- Captured: Activities should be accessible only when Joshua assigns them to the student from the admin side.
- Remove Activities as a tier/access toggle.
- The specific assignment authorizes access to that activity; no general Activities catalogue access through a tier.
- Applies across all tiers, including Tier 1. Tier 1 “everything enabled” now means all remaining tier-controlled features, not unassigned Activities.
- Remaining visible switches: Drill, Practice tests, Bootcamps, Classroom, Messages, Schedule and booking.
- Activities do not enable Progress and history.
- Tier 2 and Bootcamp access policy remain pending.

### Q8 — Bootcamps are assignment-only
- Asked: should Bootcamps follow Activities, assigned access with no toggle?
- Captured: Joshua confirmed “yes it is the same for bootcamp.”
- Remove Bootcamps from tier switches. An admin assignment grants access to that specific bootcamp across every tier.
- Remaining tier-controlled switches: Drill, Practice tests, Classroom, Messages, Schedule and booking.
- Drill OR Practice tests automatically includes Wrong answers, Flagged questions, Progress and history.
- Activities and Bootcamps remain assignment-only, irrespective of tier.
- Open decision: what separates Tier 2 from Tier 1 now that Activities and Bootcamps are no longer tier-controlled?

### Q9 — Tier 2 clarification requested
- Joshua’s message contained both “add the drill for Tier 2” and an explicit statement that Tier 2 should have only Classroom, messaging, schedule and booking, with no Drill or tests.
- Working interpretation from the explicit feature list: Tier 2 has Classroom, Messages, Schedule and booking; Drill and Practice tests off. The contradictory opening was surfaced for clarification.

### Q10 — Tier 3 reduced floor
- Captured: “Tier 3 should only give access to schedule and booking and message.”
- Confirmed Tier 3: Messages and Schedule and booking enabled; Classroom, Drill and Practice tests disabled.
- Supersedes earlier Tier 3 Classroom floor.
- Proposed final distinction: Tier 1 all five; Tier 2 Classroom/Messages/Schedule and booking; Tier 3 Messages/Schedule and booking.
- Need confirmation of Tier 2 interpretation before implementation because Q9’s conflicting Drill statement remains unresolved explicitly.

### Q11 — Tier 2 confirmed, assigned runners preserved
- Captured: Tier 2 should not have independent Drill or Practice test access.
- Joshua can explicitly assign specific drills or sections through Classroom, and Tier 2 students can open and complete those specific assignments.
- Assignment access must not unlock the general Drill or Practice tests feature.
- Final presets: Tier 1 all five switches; Tier 2 Classroom/Messages/Schedule and booking; Tier 3 Messages/Schedule and booking.
- Implement assigned drill/section authorization separately from general practice permission.
- Discovery of tier defaults is complete. Implementation requested (“Let’s fix it”) and pending.


### Implementation interpretation — Tier 3 assignment links
- Latest explicit Tier 3 “only Messages and Schedule and booking” supersedes the earlier inferred blanket “assignments across every tier” wording.
- Tier 1 and Tier 2 have Classroom and can open explicitly assigned activities, bootcamps, drills and sections.
- Tier 3 does not regain learning access through an old assignment URL while Classroom remains off.
- Activities and Bootcamps remain assignment-only; there is no general switch in any tier.


### Release checkpoint
- Source commit 5b5d5b0 prepared locally; not pushed.
- 54 focused tests, final build/postbuild, typecheck and targeted lint passed for that commit.
- Database policy installed and readback verified; no bulk real-student profile changes.
- Final Home inspection found assigned Activities still filtered by retired activity flag. Push stopped before any frontend release; correcting Home filter and locked mobile overlay.
- Existing saved independent access is preserved. Selecting a tier reapplies its new preset.

### Final release preparation
- Latest clarification reconfirmed Tier 2: general Drill and Practice tests off; explicitly assigned drills and sections open only their assigned scope through Classroom.
- Final source: 5b5d5b0 and e17c05f. All 69 focused tests passed, final production build/postbuild passed, and required push typecheck passed.
- Safe push merged three upstream question-data corrections and pushed release 411267d to main. Lovable import/publication verification pending.
- Database tier policy is installed; existing student independent flags were not bulk changed.


### Completed release
- Final copy commit 99aa43d10b69ee529c70e5564faeef9a75bfb09d pushed after required typecheck; final production build/postbuild passed.
- Lovable imported exact final commit and manual Publish succeeded. Live Students page verifies all five controls and corrected assignment-only help text. Live database readback verifies derived review policy and Classroom default=false.
- Screenshot: C:/Users/Joshu/dev/ai-os-projects/lsatu-tier-defaults/.impeccable/live/tier-controls-live.png.
- 69 focused tests passed; no real learner permission edits made for verification. Tier 2 assigned-runner scope checked in component tests, not a production student session.
- Separate account-reset Edge Function deployment remains skipped because its required Lovable agent route may spend credits and no immediate credit authorization was given. This does not block the released tier-selection policy.

