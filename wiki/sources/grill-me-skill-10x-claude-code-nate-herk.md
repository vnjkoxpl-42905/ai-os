---
type: source
subject: Nate Herk on the grill-me skill and checkpointed brainstorm files
created: 2026-11-20
updated: 2026-11-20
aliases: [The Skill That 10x'd My Claude Code Projects, Nate Herk grill-me]
tags: [ai-workspace, skills, grill-me, brainstorms]
evidence: ../../raw/sources/clips/grill-me-skill-10x-claude-code-nate-herk/clip.md
sha256: 4551c3fd4e77289a199e0c8e0a113c8189fecd0b373305f10423427207d8f827
contradictions: []
sources:
  - ../../raw/sources/clips/grill-me-skill-10x-claude-code-nate-herk/PROVENANCE.md
---

# Getting knowledge out of your head is the hard part; grill-me does it

Nate Herk, [The Skill That 10x'd My Claude Code Projects](https://www.youtube.com/watch?v=c0kaKxM2pHg). Undated (he mentions Opus 4.8, which hints at the era); about seven minutes. [Preserved text](../../raw/sources/clips/grill-me-skill-10x-claude-code-nate-herk/clip.md), [provenance](../../raw/sources/clips/grill-me-skill-10x-claude-code-nate-herk/PROVENANCE.md), [hash manifest](../../raw/sources/clips/grill-me-skill-10x-claude-code-nate-herk/SHA256SUMS).

## What the source says

- Matt Pocock's original is four or five sentences: interview me, walk the decision tree, recommend an answer for each question, ask one at a time, explore the codebase instead of asking when you can.
- Nate adds a checkpoint after every answer into a `brainstorms/` folder at the project root, one markdown file per topic. The file holds discovery notes, key decisions, a Q&A log and open flags. At the end it offers to update related skills and docs. Unanswerable items are flagged for a named person and the session can be resumed later.
- His reason for checkpointing: a long grilling fills the context window and he worried the model would misremember early answers.
- His illustration is that a skill built without it climbs from about 70 to 95 percent over 10 to 30 iterations, while one built after grill-me starts near 90 percent. He calls it a "horrible visual"; it is not a measurement.

## What this adds here

Nothing structural. The vault's [grill-me skill](../../skills/claude/grill-me/SKILL.md) already writes `brainstorms/{date}-{slug}.md` with a header, running summary, Q&A log and open flags, checkpoints per round (from [Matt Pocock's skills v1.2](matt-pocock-skills-v1-2.md)), read-back, supersede-not-overwrite, resume and a stop rule. One inferred gap: the vault skill merges into context pages only for AI-OS sessions and does not explicitly offer, at the end of every session, to update the related skill and reference docs. The idea is already summarised in [Nate's second-brain video](claude-ultimate-second-brain-nate-herk.md).

## Coverage

Read in full on 2026-11-20 by a read-only research pass. No earlier copy exists. Skool plugs and the success-rate figures (70 to 95 percent, "95 versus 80 percent") are unmeasured.
