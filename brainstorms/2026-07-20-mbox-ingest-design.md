---
type: brainstorm
subject: Mbox Ingest Design Brainstorm / Discovery Notes
updated: 2026-07-20
aliases: []
---

# Mbox Ingest Design: Brainstorm / Discovery Notes

Date: 2026-07-20 · Goal: Design the ingest of the 3,318-message mbox into the second brain, so the business half of the brain exists and the teaching-to-business join becomes real.

## Context going in

- Architecture settled earlier today in `2026-07-20-second-brain-architecture.md`: four-tier distillation layer, Tier 2 playbooks per curriculum topic, one unified graph built after ingest.
- The mbox is the **only** remaining source of new material. Verified 2026-07-20: `Practice_Test_Reports/` and `Student_Specific_Homework/` are empty across every student; `teaching-notes.md` + `email-correspondence.md` + `open-loops.md` + `assignment-log.md` total roughly 5,400 words across all students combined. Transcripts are already distilled, `corpus/` is already synthesized.
- A prior plan exists and was never executed: `2026-07-19-takeout-deep-ingest-emulation.md`, ten locked decisions.

## Resolved by inspection (no interview needed)

- **Authoritative source:** `/Users/joshuaf/ai-os/raw/sources/private/takeout/Takeout/Mail/All mail Including Spam and Trash.mbox` (1,121,343,193 bytes, 2026-07-16). Byte-identical to the copy on the Desktop.
- **Excluded:** the two 1.4GB copies at `Takeout/Drive/Trash/` (2026-03-23). Older, and already ruled out by the 07-19 plan as the stale Drive-Trash mbox.
- **Message count:** 3,318 (`grep -c '^From '`).
- Goodnotes ruled out of scope by Joshua, 2026-07-20. Not a source.

## Summary / key decisions

(running synthesis, updated as we go)

## Q&A log

### Q1 — do the 07-19 decisions still stand?
- Asked: pending
- Captured: pending

## Open flags (pending input)

- Sequence question 13 from the architecture interview (ingest before graph) was never explicitly answered. Proceeding on the assumption that ingest is first, since Joshua asked "what are you going to ingest first".
- Moving `graph-imports/distillates/` out to the vault root still needs an explicit yes.
