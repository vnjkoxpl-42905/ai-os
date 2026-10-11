---
name: morning-brief
description: >
  Daily inbox triage that produces one ranked queue of drafted replies. Use when
  Joshua says "morning brief", "what needs a reply", "catch me up on email",
  "run the brief", "am I behind", or at the start of a working day. Sweeps
  Gmail, classifies what is waiting, drafts each reply in his voice, and logs
  every draft to the send ledger. Never sends.
allowed-tools: Bash Read Write Edit Glob Grep
---

## Current AI OS execution contract

Before creating a draft, check actual Gmail thread/sent/draft state with the stable event/thread/recipient key. Reuse an existing unsent draft. Update ledger status only from fresh authoritative evidence.

# Morning brief

**19% of every email Joshua writes is an apology for replying late.** That is a
throughput problem, not a voice problem. This skill exists to stop the backlog
forming: one pass each morning that turns "I'm behind on email" into a review
queue he can clear in fifteen minutes.

The output is a **ranked queue of drafts**. He reviews and sends. Nothing goes
out on its own, ever.

## 1. Sweep

Pull what is actually waiting. Default to unread plus anything in the last few
days he has not answered.

```
gws gmail +triage --max 40 --format json
gws gmail +triage --query 'is:unread' --max 40 --format json
gws gmail +triage --query 'newer_than:5d -from:me' --max 40 --format json
```

Read individual messages only where the subject line is not enough:

```
gws gmail +read --id <message-id> --headers
```

Do not read all forty. Read the ones you are about to draft for. Context spent
on messages that need no reply is context not spent on the drafts.

## 2. Classify

Sort every waiting message into exactly one bucket. The bucket decides who
drafts it and how urgent it is.

| Bucket | What it looks like | Route to |
|---|---|---|
| **Consultation follow-up** | had a consult, no reply sent | `consultation-followup-drafts` |
| **New inquiry** | first contact, asking about tutoring | `consultation-inquiry-drafts` or `inbound-tutoring-replies` |
| **Active student** | current student, in `students/roster.generated.md` | draft here, using their folder |
| **Scheduling** | reschedule, cancel, availability | draft here; check the calendar first |
| **Payment** | invoice, receipt, billing question | **flag only, do not draft** |
| **Noise** | newsletters, receipts, platform notifications | drop, do not surface |

Rebuild the roster first so "is this an active student" is answerable:

```
python3 system/scripts/build-roster.py
```

Payment is flag-only on purpose. Money messages carry real consequences and
Stripe is the authority, not the inbox — surface them for Joshua and stop.

## 3. Rank

Order the queue by cost of continued silence, not by arrival time:

1. **Aging consultations** — someone who consulted and has heard nothing. This
   is where the named drops happened (Susan, Muhammad, Alexandria, Mehvish).
2. **Active students waiting on an answer** — a student blocked on him.
3. **New inquiries** — decays fast; a lead cold after a few days is usually lost.
4. **Scheduling** — time-sensitive but usually quick.
5. **Everything else.**

Within a tier, oldest first. State each item's age in days, because age is the
whole point.

## 4. Draft

Every draft routes through `wiki/teaching-voice.md`. Non-negotiable — this is
student- and prospect-facing copy.

- Personalize from the student's folder (`teaching-notes.md`, `open-loops.md`).
  A reply that does not know where they are in their prep is worse than a slow
  one.
- If the reply is late, own it in the first line, give the real reason in one
  clause, move to the fix. Do not over-apologize; that is the register he
  already uses.
- No em-dashes. No AI-slop vocabulary.
- Where an existing skill owns the category, **invoke it** rather than
  re-deriving its template.

Create each as a real Gmail draft so he can send from his own client:

```
gws gmail +send --to <email> --subject "<subject>" --body "<text>" --draft
```

`--draft` is the safety flag. It is never omitted here. This skill has no
send step at all.

## 5. Log every draft

Append one line per draft to `wiki/send-ledger.md`, status `drafted`:

```
| 2026-07-20 08:14 | lydia | reply re: RC pacing question | drafted | morning brief |
```

If it concerns a student, also append the loop to
`students/<slug>/open-loops.md`.

Status only becomes `sent` when Joshua actually sends it and says so. Do not
pre-log a send that has not happened — a wrong ledger line is worse than a
missing one.

## 6. Present

Give him the queue, tightest possible:

```
Morning brief — <date>. <N> waiting, <M> drafted.

1. [consult, 6d] Susan — no follow-up since her consultation. Draft ready.
2. [student, 2d] Lydia — asked about RC pacing. Draft ready.
3. [lead, 1d] <name> — asking about availability. Draft ready.

Flagged, not drafted:
- [payment] <name> — invoice question. Needs your call.

Nothing else needed a reply.
```

Then stop. Do not send. Do not ask which to send one at a time — he reviews the
drafts in Gmail and sends what he wants.

## Hard rules

- **Never send.** Drafts only, always. There is no approved auto-send path here.
- **Never draft a payment or billing reply.** Flag it and stop.
- **Never invent a recipient address.** Use the roster or the original message.
- **Log drafts as `drafted`, never as `sent`.**
- **Do not surface noise.** A brief that lists twenty newsletters trains him to
  ignore the brief.
- If a message needs a decision only Joshua can make, put it in the flagged
  list rather than guessing at a draft.
- Read only the messages you are drafting for.
