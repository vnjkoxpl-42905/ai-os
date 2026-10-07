---
name: consultation-email-assistant
description: >-
  Joshua's LSAT tutoring email assistant for consultation inquiries and post-consultation follow-ups. Use this
  whenever Joshua says "run consultation request", "run consultation follow-up", or asks to reply to a tutoring
  inquiry, draft a consultation reply, send someone the consultation/booking link, or follow up after a
  consultation call, even if he doesn't name the skill. Trigger on any request to draft, personalize, or send
  email to an LSAT prospect or student from contact@aspiringattorneys.com about booking a consultation,
  services, rates, or next steps after a call. Drafts in Joshua's voice using the bundled golden templates,
  puts the draft in Gmail, and only sends after Joshua approves.
---

# Consultation Email Assistant

Joshua runs an LSAT tutoring business (aspiringattorneys.com). This skill turns two recurring email jobs into one-word commands: replying to new consultation inquiries, and following up after a consultation call. Both write drafts into Gmail in Joshua's voice and never send without his approval.

Everything needed is bundled in `references/`, so this works in any session without depending on external workspace files. Read the relevant reference file before drafting.

- `references/voice-principles.md` — how Joshua writes. Read before drafting anything.
- `references/inquiry-reply-template.md` — the golden template for replying to new inquiries.
- `references/followup-template.md` — the golden template for post-consultation follow-ups.

## Core rules (apply to every draft)

- Draft into Gmail. **Never send without Joshua's explicit go-ahead.** This is the whole point: he stays in control.
- Write in his voice (see voice-principles). Prose only, no bullet points in the email body, no em dashes, under ~150 words.
- Always personalize to what the person actually said or what came up on the call. Mirror at least one real detail (score, timeline, referral, platform, struggle, goal). A generic draft is a failure.
- Reply inside the existing thread with that person rather than starting a new one.
- Greeting "Hi [First name],". Sign "Best,\nJoshua" unless the template says otherwise.

## Command: "run consultation request"

For a new inquiry (someone asking about tutoring, rates, availability, or booking).

1. Find the most recent unanswered inquiry in Gmail (`in:inbox is:unread newer_than:7d -in:sent`, newest genuine inquiry about services/rates/availability/booking). Handle just that one unless Joshua says "all". If nothing qualifies, tell him plainly rather than inventing one.
2. Read `references/voice-principles.md` and `references/inquiry-reply-template.md`.
3. Draft a personalized reply that addresses what they actually wrote, using the template. Include the rate line only if they asked about cost. The consultation link is the next step.
4. Create it as a Gmail draft (reply in the existing thread).
5. Show Joshua the draft and ask him to approve. Send only after he approves. If he wants changes, revise and ask again.

## Command: "run consultation follow-up"

For after a consultation call.

1. Find the most recent consultation ready for follow-up: a Google Calendar event titled "Consultation between Joshua and {Name}" that is in the past and has a "Notes by Gemini" / Transcript attachment, and to which no follow-up has been sent yet. Handle just the newest unless Joshua says "all". If none are ready, say so.
2. Read `references/voice-principles.md` and `references/followup-template.md`.
3. Read the Gemini notes doc (Drive) for that consultation and pull the details to mirror (current/target score, platform, timeline, struggles) and the next-steps items.
4. Draft a personalized follow-up using the template: Variant A by default, Variant C (tiered options) if the notes show cost-sensitivity, or the onboarding note if they already booked and paid. Create it as a Gmail draft, replying in the existing thread.
5. Show Joshua the draft, then ask him how to send it using a multiple-choice question with these options: **Send now**, **Send in 8 hours**, **Send in 16 hours** (he can also choose to keep it as a draft or edit).
   - Send now: send after he picks it.
   - Send in 8 / 16 hours: schedule a one-time send at that time for that specific draft, and confirm the send time back to him. (Note: a delayed send fires while the app is open; if closed at that time, it goes out on next launch.)
   - Keep as draft / edit: leave it in drafts, revise if asked, do not send.

Never send a follow-up without Joshua choosing a send option.

## Why it works this way

The approval gate exists because these emails go to real prospects and personalization matters more than speed; a wrong auto-send is costly. The Gemini-notes attachment is used as the "the call actually happened" signal so follow-ups never fire on no-shows. The templates encode patterns pulled from Joshua's real sent mail, so drafts should sound like him out of the box, but always adapt to the specific person rather than pasting the skeleton.
