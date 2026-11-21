---
name: consultation-inquiry-drafts
description: "Daily sweep: draft, but do not send, personalized consultation-link replies to new LSAT tutoring inquiries"
---

# Consultation Inquiry Drafts

Find new LSAT tutoring inquiries and prepare Gmail drafts for Joshua to review. Never send. AI-generated replies remain drafts unless Joshua separately approves the exact message.

## Required context

Before drafting:

1. Read `C:/Users/Joshu/dev/ai-os/wiki/teaching-voice.md`.
2. Read `C:/Users/Joshu/dev/ai-os/context/work.md` for current offers, booking, and billing rules.
3. Use Gmail only through the `gws` CLI. Do not use Google connector MCPs.
4. If the sender may already be a student, check `students/<name>/` first. Use Gmail and other live systems only when the student file does not resolve identity or current state.

## Find eligible inquiries

Search Gmail for recent inbox threads that appear to be genuine new tutoring inquiries. A useful starting query is:

```text
in:inbox newer_than:2d -in:sent
```

Include people asking about tutoring, rates, availability, consultations, referrals, or how to begin.

Skip:

- Existing-student logistics.
- Booking and calendar notifications.
- Newsletters and spam.
- Any thread Joshua has already answered.
- Anyone who has already paid or moved past consultation. Route those cases according to their actual student and payment state.

Unread status is a clue, not proof that a reply is owed. Inspect the thread and confirm Joshua has not already responded.

## Drafting rules

Each reply must:

- React to at least one real detail from the inquiry, such as a score, test date, platform, referral, plateau, or specific struggle.
- Use a brief general acknowledgment only when the inquiry contains no useful detail.
- Invite the prospect to a free consultation using `https://cal.com/joshua-jtx5ud/consultation`.
- Explain the consultation in one short, low-pressure sentence.
- Mention the current rate, `$40/h`, only when the person asks about price, rates, cost, or affordability.
- Use a brief apology near the opening when Joshua's reply is more than about 24 hours late.
- Stay under roughly 120 words, unless the inquiry genuinely requires more.
- Use prose only, no bullets and no em dashes.
- Default to `Hi [First name],` and `Best,\nJoshua`. Use `Hey` only when the sender's tone and relationship clearly support it.
- Invite the person to reply if the booking link does not work.

Do not copy canned situation lines blindly. Mirror the person's message in natural language and follow the current teaching-voice page.

## Gmail draft behavior

Create the draft through `gws`. Reply inside the existing Gmail thread whenever one exists. Preserve the thread context and reply headers rather than starting a new conversation. Do not send.

## Report and log

Report each prospect's name, email, the detail mirrored, and that a Gmail draft is waiting for review. Flag uncertain identity, prior-contact, pricing, or student-status cases.

Append each created draft to `wiki/send-ledger.md` with status `drafted`. Gmail remains the authority for whether anything was actually sent.
