# LSAT U redesign decisions: Brainstorm / Discovery Notes

Date: 2026-09-28 · Goal: Settle the remaining independent product decisions for the student and teacher redesign before the implementation spec.
Status: Wayfinder decisions complete; legacy browser-only recovery deferred outside the first release
Context sources: [Wayfinder decision map](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/155); [platform adoption game plan](2026-09-27-lsatu-platform-adoption-game-plan.md); [student experience design](2026-09-28-lsatu-student-experience-design.md); [Practice Exams discovery](2026-09-26-practice-exams-discovery.md).

## Summary / key decisions

Earlier approved choices are in the linked decision map and discovery notes. Joshua directed Admissions to be locked now because it is not prepared, with access kept for Joshua and admins only. That lock was published and verified in a signed-in student view: the rail item is disabled with a lock, and the direct URL shows "Not open yet." He said not to wait for a current-student prototype test before the build spec. For a new timed exam, a failed account save should keep a device backup and pause the exam and clock with a visible problem until saving works. Joshua remained confused by the old browser-only progress question after a second explanation. No product choice was recorded for its display. Preserve ownerless records without assigning them to any account and leave any later recovery policy flagged.

## Q&A log

### Round 1

#### Q1 - Connection drops during an exam
- Asked: If an answer cannot save to the student's account, should the exam and clock pause after keeping a temporary device copy?
- Recommended: Pause and display the failed save until account saving succeeds.
- Captured: Joshua asked why an exam would save and whether saving is always safe. No connection-loss decision was made.
- Flags: Superseded by Joshua's answer to Q5 in Round 2.

#### Q2 - Older browser-only exams
- Asked: Should old browser-only exam copies with no student owner remain untouched but stay out of signed-in Attempts until ownership can be established?
- Recommended: Yes; never attach an ownerless copy to the next account that signs in.
- Captured: Joshua said he was not sure what the question meant. No legacy-exam display or migration decision was made.
- Flags: Explain the old versus new storage distinction with a concrete example before asking again. Owner: assistant.

#### Q3 - Admissions access
- Asked: Should Admissions remain available to every signed-in account, as it is now?
- Recommended: Keep current access unless Joshua wants a new restriction.
- Captured: Joshua said Admissions should get locked very soon, "right now," because it is not prepared. This rejects the recommendation to leave access open.
- Flags: Superseded by Joshua's admin-only, immediate-access answer to Q7 in Round 2.

#### Q4 - Current-student prototype test
- Asked: Should the build spec wait for one current student to complete prototype task walks?
- Recommended: Yes.
- Captured: Joshua said, "No, don't wait." The current-student prototype test is not a prerequisite to the build spec.

### Round 2

#### Q5 - Failed account save during a timed exam
- Asked: If internet loss prevents an answer and the student's place from saving to their account, should the app keep a temporary device backup and pause the clock and next question until saving works again?
- Recommended: Yes, pause and show the save problem.
- Captured: Joshua accepted the recommendation. This is a user-confirmed connection-loss rule for new account-backed attempts.

#### Q6 - Older browser-only progress with no owner
- Asked: Should an old browser-only exam progress record with no student ID remain untouched but stay out of every signed-in account's Attempts list?
- Recommended: Preserve but hide it from account Attempts until ownership can be established.
- Captured: Joshua invoked wait-what and asked what "old exam copy" and "shared" meant. No policy choice was made.
- Flags: Explain that this means a student's saved answers and place from a pre-change full exam, stored in one browser without an account ID. "Shared" was an illustrative risk, not a claim that Joshua's students share devices. Owner: assistant.

#### Q7 - Admissions access while unfinished
- Asked: Who should still be able to open Admissions after the immediate lock?
- Recommended: Joshua and admins only.
- Captured: Joshua accepted the recommendation. The unfinished Admissions route should deny students while remaining available to Joshua/admins; he requested the lock now, not after the redesign.

### Round 3

#### Q8 - Old exam progress without a student ID
- Asked: Should pre-change full PrepTest progress saved in one browser without a student ID remain untouched there and stay out of every account's Attempts list?
- Recommended: Preserve without assigning an owner.
- Captured: Joshua said, "im confused." No product decision about whether to display or recover these old records was made. The assistant stopped asking the same question.
- Flags: Ownerless progress cannot safely be attached to any account. Preserve it without reassignment; defer any optional recovery or local display design until concrete evidence and a clearer user need exist. Owner: assistant/product team.

### Round 4

#### Q9 - Progress calculation rule

- Proposed: Diagnostic accuracy uses the first saved, graded answer to each distinct LR or RC question. Repeats remain in History and volume, while Inspect and blind-review answers stay out of diagnostic accuracy. Keep the already approved 7/14/21/30/All filter, disclose numerator, denominator, sources and missing coverage, and use only explicit assignment links. Student and teacher views share the calculation.
- Captured: Joshua said, "yes thats good." This accepts the Progress recommendation; the existing Analytics and History screens have conflicting calculations and require a shared rebuild.
- Flags: Keep LR and RC separate, show insufficient evidence below three eligible questions per breakdown, and label three to nine as an early signal. These are implementation details in the adoption plan.

### Round 5

#### Q10 - Teacher/admin access while viewing a student

- Context: The earlier plan called View student experience a read-only preview.
- Captured: Joshua corrected it: "I want to have total access to do whatever I want as the teacher. and admin." Teacher/admin controls therefore remain available while viewing a selected student's experience. The earlier read-only restriction is superseded.
- Follow-up asked: If Joshua answers a question there, should it count in that student's score and history?
- Captured: Joshua chose "No, keep teacher answers separate." Teacher practice is attributed to the teacher/admin account and excluded from the student's attempts, accuracy, completion, and review state. Other changes Joshua makes to the student record remain teacher/admin actions with visible attribution.
- Flags: The implementation needs authorized admin read/write paths scoped to the selected student; it must not silently replace the signed-in identity with the student's account.

## Open flags (pending input)

- Older browser-only runs: no user display/recovery choice after two explanations. Preserve the underlying local data; do not attach it to any account or include it in account Attempts. Recovery/import is outside the first release and can be revisited only with a concrete, safe proposal. This is a scoped deferral, not a claim that Joshua chose a recovery design.
- Admissions lock: app commit `dcd75e3` was pushed to `main` and published through Lovable. The signed-in student rail showed a disabled Admissions item with a lock, and `/classroom/admissions` showed "Not open yet" on the live site. Admin access passed the route test; a live admin account was not used.

## Wayfinder completion check, 2026-09-28

- All decision tickets #156-#162 and #164 are resolved. #163 was closed after Joshua chose not to wait for a current-student prototype test.
- #160 sets the new account-backed exam contract and safely defers ownerless legacy-run recovery. Latest `origin/main` contains account-backed full PrepTest sync, while the older dirty feature checkout retains a browser-only runner. The approved blocking save-failure pause across timed LR/RC and live backend verification remain build work. Plan from `main`, not the feature checkout.
- No further product answer is required before an implementation spec and blocker-aware tickets. The final Impeccable review belongs after functional student and teacher slices are built.
