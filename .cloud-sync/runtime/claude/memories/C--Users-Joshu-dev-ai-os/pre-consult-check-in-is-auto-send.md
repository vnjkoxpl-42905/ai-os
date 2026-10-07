---
name: pre-consult-check-in-is-auto-send
description: The 30-minute-before "Consultation check-in" email is pre-authorized to send with no approval, via the pre-consultation-check-in skill; consultations are identified by title alone, never by Cal.com link or UID.
metadata:
  type: feedback
---

On 2026-09-11 Joshua granted standing permission for the `pre-consultation-check-in`
skill (canonical at `dev/ai-os/.agents/skills/pre-consultation-check-in`, junctioned
into `~/.claude/skills` and both catalogs) to send his fixed "Consultation check-in"
email 30 minutes before each Cal.com consultation without a per-send approval. The
skill lists, then schedules, then reports; it does not ask. Record of every booking:
`wiki/PRE-CONSULT-LOG.md`; sends also land in `wiki/send-ledger.md`.

Identification is the title regex `^Consultation\s+between\s+Joshua\s+and\s+(.+)$`
(70/70 true, 0/171 false on 241 events). `@Cal.com` UIDs and `cal.com/booking`
links both produce false positives (Complimentary sessions, paid LSAT Session
bookings), so never "loosen to any Cal.com booking". "Sofia session" is a paid
session, not a consultation.

**Why:** He sends this identical email 201 times over; the identification rule is
exact; the only value of an approval step was friction. An earlier automation sent
these at T-30 through 2026-09-03 and then stopped, leaving a gap he noticed.
**How to apply:** For this one email, "schedule the check-ins" means do it. For any
other email the [[ai-os-safety-rules]] still hold. Fire time is a Windows scheduled
task running a plain script (no LLM); if the laptop is off through the whole T-30
window the row goes `missed` and he sends by hand. The skill never creates calendar
events; test scaffolding that created events on 2026-09-11 annoyed him.
