---
name: send-booking-link
description: >
  Draft the booking-link email to a student and log the follow-up loop. Use
  when Joshua says "send <student> their booking link", "send booking links to
  X, Y, Z", "get <student> scheduled", or asks who still needs one. Wraps the
  lookup / draft / send / log pipeline that has been hand-orchestrated one
  student at a time. Drafts by default; sends only on an explicit go-ahead.
allowed-tools: Bash Read Write Edit Glob Grep
---

# Send booking link

Four steps that were being done by hand, seven times in a single session:
look up the email, draft in Joshua's voice, send, log the open loop. This does
all four, in order, for one student or a batch.

## 1. Look up — never guess an address

The roster is generated; rebuild it first so it reflects current folders.

```
python3 system/scripts/build-roster.py
```

Then read `students/roster.generated.md` for the student's **email** and
**booking link**. Both must be present before drafting.

- **No email recorded** → stop. Do not guess, do not search for a plausible
  address. Tell Joshua the student's page has no `email:` in frontmatter.
- **No booking pass** → stop. The roster's "No booking pass" section lists
  these. Booking access has to be granted before there is anything to send.
- **Pass `exhausted`** → stop, and say so. The link is live but has no credits
  left, so the student lands on "you've used all your sessions". Sending it is
  worse than sending nothing. Credits have to be added first.
- **The URL slug is not the folder slug.** `yahunatan-zetvy` is
  `/book/yahunathan`. Always read it from the roster; never derive it.
- **Email disagrees with the backend** → stop and ask which is current. The
  roster surfaces these rather than picking one.

The roster's booking columns are read **live** from `booking_passes` on every
rebuild, so they are current as of the rebuild and revoked passes are already
excluded. That is why step 1 rebuilds first.

## 2. Draft in Joshua's voice

Route through `wiki/teaching-voice.md`. This is student-facing copy, so the
voice rules are not optional.

Shape: short, warm, no overselling. Own any delay in the first line if there
has been one, give the real reason in a clause, move to the next step. Hand
them the link plainly. No em-dashes. No AI-slop vocabulary.

Personalize from the student's folder — `teaching-notes.md`, `open-loops.md`,
their `<slug>.md` — so the email refers to where they actually are (what they
were last working on, what they said they wanted). A generic blast is the thing
this skill exists to avoid.

## 3. Draft, then stop

**Default is draft, not send.** Anything a student or prospect reads is drafted
and never sent unless it is a pre-approved template and Joshua has said go.

The safety flag is `--draft`. It is the difference between a draft and a sent
email, so it is never omitted on the first pass.

```
gws gmail +send --to <email> --subject "<subject>" --body "<text>" --draft
```

Show Joshua the drafted text. Send only after an explicit go-ahead, and only
for the students he named — the same command with `--draft` removed:

```
gws gmail +send --to <email> --subject "<subject>" --body "<text>"
```

Use `--dry-run` first if you are unsure the command is well-formed. Note
`--body` takes the text inline, not a file path.

For a batch, draft **all** of them and present the set for one approval, rather
than asking per student. Never send a batch on a single "yes" unless he says
"send them all" plainly.

## 4. Log the loop

Append to `students/<slug>/open-loops.md`, matching the existing format:

```
- [YYYY-MM-DD] Sent booking-link email (/book/<slug>). Loop: confirm they schedule; follow up if no booking within ~5 days.
```

Use the real date (`date +%F`). If it was drafted but not sent, say `Drafted`
rather than `Sent` — a wrong entry there is worse than no entry.

`open-loops.md` is a **primary** file: append, never rewrite.

Then append one line to `wiki/send-ledger.md`, which is the single surface that
answers "did X get their email":

```
| YYYY-MM-DD HH:MM | <slug> | booking link (/book/<slug>) | drafted | — |
```

Status becomes `sent` only when it actually goes out. The per-student log
carries the follow-up loop; the ledger carries whether it was sent.

## Hard rules

- **Never send without an explicit go-ahead.** Draft is the default, always.
- **Never invent an email address or a booking slug.** Missing data stops the
  run; it does not get filled in with a guess.
- **Never write to `*.generated.md`.** The roster is rebuilt, not edited.
- **Log what actually happened.** Drafted is not Sent. If a send fails, log the
  failure rather than the intent.
- One student's email never mentions another student.
- If Joshua asks "who still needs a booking link", answer from the roster's
  gap sections — that is what they are for — and do not draft anything until
  he picks.
