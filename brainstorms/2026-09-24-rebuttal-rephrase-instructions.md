# Rebuttal Rephrase Instructions: Brainstorm / Discovery Notes
Date: 2026-09-24 · Goal: Make the Rebuttal Rephrase instructions clear, visually useful, and faithful to the student task.
Status: in progress
Context sources: `wiki/teaching-voice.md`; `projects/lsatu/src/features/activity-centre/content/rebuttal-rephrase.json`; current local Activity Lab preview; screenshots supplied in chat.

## Summary / key decisions

- User wants to review the drill visually and have the screenshot guidance fit naturally into its instructions.
- The teaching move in the screenshots: locate a referential rejection such as “this is not so,” identify the specific opposing claim, and state what the author argues for in a clear sentence with specific nouns.
- Prior local implementation already added the poetry example, specific-noun guidance, evidence/conclusion distinction, response-box hint, and a database migration. User says the presentation still needs to be made visually clear and checked in the drill.
- User previously clarified that special highlighting should be removed while preserving original indicator words. Keep that constraint.
- Deployment and application of the migration are not authorized by this request; project instructions require separate confirmation for Lovable deployment and any action that may spend credits.

## Q&A log

### Round 1

#### Q1 - Where instructions appear
- Asked: Should the full explanation appear only before a run, or remain visible on each question?
- Recommended: Teach the method and worked example on the intro screen, then use only a short specific-noun reminder in the answer field. This keeps the question stimulus free of cues.
- Captured: Pending Joshua's answer.
- Tentative: Keep the actual question screen single-column with no pivot highlighting, consistent with the prior request.
- Flags: None.

#### Q2 - Visual organization
- Asked: Should the intro be reorganized into a three-step visual flow with a labelled worked example and a compact “keep the meaning exact” note?
- Recommended: Yes. Replace the large overlapping Before/After treatment and long six-rule list for this drill with a scannable three-step sequence: find the rejection, name the opposing claim, state the author's position. Show the screenshot's poetry example as a card with separate labels for argument, conclusion phrase, credited answer, and evidence distinction. Stack it cleanly on mobile.
- Captured: Pending Joshua's answer.
- Tentative: Keep the given poetry example as the worked example because it contrasts conclusion and evidence directly.
- Flags: None.

## Open flags (pending input)

- Confirm the instruction placement and visual structure before implementation -> Joshua.

#### Joshua's clarification after Round 1
- Captured: Keep the material on the intro screen. The teaching copy should not be part of the large title/header; present it as instructions. Joshua also raised the possibility of an instruction page that appears when Start is pressed, so the exact Start sequence remains open.
- Answer to Q1: Keep teaching on the intro screen; present it as instructions, not a header.
- Q2: Not explicitly answered yet. The request to make it easy to follow supports a clearer layout, but the exact visual treatment remains to confirm.
