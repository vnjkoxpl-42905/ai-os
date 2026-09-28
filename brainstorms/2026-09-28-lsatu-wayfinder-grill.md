# LSAT U redesign decisions: Brainstorm / Discovery Notes

Date: 2026-09-28 · Goal: Settle the remaining independent product decisions for the student and teacher redesign before the implementation spec.
Status: in progress
Context sources: [Wayfinder decision map](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/155); [platform adoption game plan](2026-09-27-lsatu-platform-adoption-game-plan.md); [student experience design](2026-09-28-lsatu-student-experience-design.md); [Practice Exams discovery](2026-09-26-practice-exams-discovery.md).

## Summary / key decisions

Earlier approved choices are in the linked decision map and discovery notes. Joshua directed Admissions to be locked now because it is not prepared, with access kept for Joshua and admins only. He said not to wait for a current-student prototype test before the build spec. For a new timed exam, a failed account save should keep a device backup and pause the exam and clock with a visible problem until saving works. Joshua remained confused by the old browser-only progress question after a second explanation. No product choice was recorded for its display. The assistant will preserve ownerless records without assigning them to any account and leave any later recovery policy flagged.

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

## Open flags (pending input)

- Older browser-only runs: no user display/recovery choice after two explanations. Preserve the underlying local data; do not attach it to any account. Revisit only with a concrete safe recovery proposal.
- Admissions lock implementation and live verification: assistant. Joshua chose an immediate admin-only lock; the current code still allows any signed-in account.
