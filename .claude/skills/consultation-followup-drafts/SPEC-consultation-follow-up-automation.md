# Consultation Follow-Up Automation

How the post-consultation follow-up gets detected and drafted automatically. Companion to "Post-Consultation Follow-Up Template.md". Runs daily, drafts only, never sends.

## The trigger signal

Every consultation is a Google Calendar event titled "Consultation between Joshua and {Name}" with the student as an attendee. After the call, Google attaches a **"Notes by Gemini"** Google Doc to the event. That attachment is the reliable "the call actually happened" signal, and the doc contains a Summary, the student's details, and a Next steps list.

So a consultation is ready for follow-up when ALL of these are true:
1. The event is in the past (call already happened).
2. The event has a "Notes by Gemini" attachment (or a linked Transcript doc).
3. No follow-up / next-steps email has been sent to that attendee since the call.

## What the Gemini notes give us (maps straight to the email)

From a real one (Isabella Lorenzo, Jun 17):
- **Details to mirror:** diagnostic 143-147, target 167 for scholarships, platform LSAT Demon, September exam.
- **Next steps (Joshua's action items):** "Send details: booking link and payment," "Invite to platform," plus student actions like "Register for the September exam."

The drafter pulls the score/timeline/platform/goal to personalize the recap line, and uses the action items to confirm which links to include (session vs package, platform signup, form).

## The daily pipeline

1. Calendar: list events titled "Consultation" from the last ~4 days that are in the past.
2. For each, check for a "Notes by Gemini" / Transcript attachment. If none yet, skip (call may not have happened, or notes not generated). 
3. Read the Gemini doc; extract the student's name/email, the details to mirror, and the next-steps items.
4. Gmail: check for an existing thread with that attendee and whether a next-steps email already went out since the call. If already sent, skip.
5. Draft the follow-up using "Post-Consultation Follow-Up Template.md" (default Variant A; Variant C if cost/comparison came up in notes), personalized from the transcript. Create it as a Gmail draft (reply in the existing thread if one exists, otherwise a new email to the attendee). Do NOT send.
6. Report: student, the detail mirrored, which variant, and that a draft is waiting. Flag anything uncertain.

## Guardrails

- Draft only. Joshua reviews and sends.
- One follow-up per consultation. Never draft a second if one was already sent.
- If no Gemini notes exist yet, do nothing (wait for the next run).
- If the student already booked/paid before the follow-up ran, switch to the onboarding note instead of the sales-y next-steps email.
