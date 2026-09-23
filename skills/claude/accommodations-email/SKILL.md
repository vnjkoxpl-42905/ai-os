---
name: accommodations-email
description: >
  Send Joshua's LSAT accommodations email ("Request for Accommodations") to a
  student, with the LSAC Qualified Professional Form PDF attached. Use when
  Joshua says "send the accommodations email to X", "run/execute the
  accommodations skill for X", "send X the accommodations form", or names a
  student plus accommodations. Pre-approved template: invoking it for a named
  student IS the go-ahead to send. Logs the send to wiki/send-ledger.md.
allowed-tools: Bash Read Edit Grep
---

# Accommodations email

A fixed template Joshua approved on 2026-09-23. It's based on his 2026-09-19 send to
Celia; the only changes are the registration line and the "Other" note on the
experimental-section item. Everything else is his wording. **Do not rewrite it**:
no voice pass, no cleanup, no added steps. If the wording needs to change, Joshua
changes `assets/body.html`.

Files:
- `assets/body.html`: the email body. `{FIRST}` and `{ITEMS}` are the only placeholders.
- `assets/2026-2027-qualified-professional-form_final_accessible.pdf`: the attachment
  (LSAC form, revised 5/2026, sha256 `14f3a40e…caf47c`).
- `scripts/send.py`: fills in the body and sends it through `gws gmail +send` with the PDF attached.

## 1. Find the recipient

Joshua gives a name. Look it up in `students/roster.generated.md` first. If the name isn't
there or has no email, rebuild it once with `python system/scripts/build-roster.py --offline`
(a few seconds) and look again.

Not in the roster (a prospect or a new student, e.g. Gianna Jean on 2026-09-23)? Search Gmail
for their name and read the From/To headers:

```
gws gmail users messages list --params '{"userId":"me","q":"<name>","maxResults":10}'
gws gmail users messages get --params '{"userId":"me","id":"<id>","format":"metadata","metadataHeaders":["From","To"]}'
```

Use the address only if every message that matches the name agrees on it. If you found it in
Gmail but the student's page has an empty `email:`, fill it in so the next lookup is instant.

- **No email found** → stop and ask. Never guess an address.
- **Two possible addresses** → stop and ask which one.
- `{FIRST}` is their first name as Joshua writes it (e.g. "Celia").

## 2. Choose the accommodations list

By default the list is the four standard items:

1. 100% extra time (double time)
2. Stop/start breaks
3. Permission to read aloud
4. Removal of Experimental Section

If Joshua names different accommodations for this student, pass each one with `--item`.
The script adds `(Has to be written under "Other")` to any experimental-section item on its
own, so don't type that note yourself.

## 3. Send

Invoking this skill for a named student is the go-ahead. Do one dry run first so a
broken command never reaches a student, then send:

```
python skills/claude/accommodations-email/scripts/send.py --to <email> --first <First> --dry-run
python skills/claude/accommodations-email/scripts/send.py --to <email> --first <First>
```

(For a custom list, add `--item "..."` once per line on both commands.)

Use `--draft` instead of sending only if Joshua says "draft" or you have any doubt about
the recipient.

Subject is always `Request for Accommodations`. It goes out as a new email, not a reply.

## 4. Log it

Append one row to `wiki/send-ledger.md`, with the message id from the `gws` output:

```
| YYYY-MM-DD HH:MM | <slug> | Request for Accommodations (QP form attached) | sent YYYY-MM-DD | to <email>; skill accommodations-email; items: default or custom list; Msg <id> |
```

If they're a student, also append a line to `students/<slug>/open-loops.md` (create it if
missing, append only):

```
- [YYYY-MM-DD] Sent accommodations email + QP form. Loop: confirm they registered for a test date and submitted before the accommodation deadline.
```

Log what actually happened: `drafted` or `failed` if the email didn't go out.

## Keeping it current

- LSAC revises the Qualified Professional Form each testing year. From June 2027 on,
  download a fresh copy from https://www.lsac.org/document-library/133, replace the PDF in
  `assets/` and update `PDF` in `scripts/send.py` and the hash above.
- Background on the LSAC process (deadlines, categories, why "Other") is in
  `wiki/ACCOMMODATIONS-REQUEST-TEMPLATE.md`. It is for Joshua, not for the email.

## Hard rules

- Never change the email wording on your own.
- Never send without the PDF attached. The script refuses to run if the file is missing.
- One student per send. No CC or BCC to other students.
