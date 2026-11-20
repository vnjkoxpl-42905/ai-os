---
type: synthesis
subject: One vault or several: what the second-brain sources agree on, and ai-os today
created: 2026-11-20
updated: 2026-11-20
aliases: [one vault vs many, second-brain consensus, vault split decision, vault count]
tags: [ai-workspace, second-brain, vaults, decision-pending]
sources:
  - sources/every-level-of-a-claude-second-brain-nate-herk.md
  - sources/claude-ultimate-second-brain-nate-herk.md
  - sources/steal-my-ai-os-setup-5-tips-nate-herk.md
  - sources/agentic-os-setup-10x-claude-code-chase-ai.md
  - sources/new-agentic-os-standard-claude-5-robonuggets.md
  - sources/self-improving-claude-knowledge-base-one-prompt-robonuggets.md
  - sources/new-way-build-second-brain-claude-nick-saraev.md
  - sources/obsidian-in-24-minutes-tina-huang.md
  - sources/gpt-6-astra-ultimate-second-brain-nate-herk.md
---

# One vault or several: the sources, and what ai-os does today

Written 2026-11-20 from a full read of 14 clips captured that day plus the 16 earlier second-brain source pages and `Second_Brain_Prompt.pdf`. The first half is source claims, attributed. The second half is local state, checked on disk 2026-11-20. **No decision is made here;** it is an input to a grilling session (see Open decision).

## What the sources say about vault count

| Source | Stance |
|---|---|
| Nate Herk ([Herk 2](sources/claude-ultimate-second-brain-nate-herk.md), [five levels](sources/every-level-of-a-claude-second-brain-nate-herk.md), [five tips](sources/steal-my-ai-os-setup-5-tips-nate-herk.md)) | One repo. Other projects nested inside as "other worlds". Level chosen per folder. Several wikis (YouTube, meetings, business) segmented inside it to cut bloat and confusion. The [Astra clip](sources/gpt-6-astra-ultimate-second-brain-nate-herk.md) says he started "separate vaults" over time but "just to start, you could do" one; it does not say these are separate Obsidian vaults. The 2026-07-16 brainstorm found they were Obsidian windows on subfolders. |
| [Chase AI](sources/agentic-os-setup-10x-claude-code-chase-ai.md) | One designated folder; an `index.md` at every level; folder names "somewhat arbitrary". Obsidian optional. |
| RoboNuggets ([ARMS](sources/new-agentic-os-standard-claude-5-robonuggets.md), [Fable 5](sources/ultimate-second-brain-arms-robonuggets.md), [one prompt](sources/self-improving-claude-knowledge-base-one-prompt-robonuggets.md)) | One workspace folder of 35,000 to 60,000 files, organised by department routers. The one-prompt design is one `knowledge-base/` per topic. No vault splitting. |
| [Tina Huang](sources/obsidian-in-24-minutes-tina-huang.md) | Shows three separate demos (likely separate vaults, inferred) with no design argument. Level 2 is one shared vault written by agents on several machines. |
| [Nick Saraev](sources/new-way-build-second-brain-claude-nick-saraev.md) | Not a vault: a single retrieval store with per-source connectors. |
| Jeff Su, Austin Marchese, [Karpathy pattern](sources/llm-wiki-pattern.md) | One root; a knowledge map inside `CLAUDE.md`. |

**Reading:** no source recommends splitting vaults to fix speed, and none measured scale. Where knowledge is split, it is by domain inside one workspace, each with its own index and rules, to make retrieval narrower. Obsidian slowness is never the stated reason.

## The common thread

1. **A router and an index at each level.** `CLAUDE.md` points to areas; each area has its own index or router file.
2. **Immutable sources, compiled pages, outputs apart.** Raw never edited; the agent writes the wiki; finished deliverables have their own place.
3. **Retrieve before reading.** Indexes, plain-text scoring, summaries written at ingest; do not dump everything into context.
4. **Upgrade on pain only.** Lowest level that removes a real problem; vectors and graphs only for a felt miss. Vector search suits needle lookups, not summaries or aggregates.
5. **Audit and lint for freshness.** Stale and conflicting facts are the main failure; segment by domain to reduce them.

## What ai-os has and lacks (checked on disk 2026-11-20)

| Has | Lacks or never adopted |
|---|---|
| `CLAUDE.md`/`AGENTS.md` routers; schema; raw, wiki, index, log, hash dedup, manual lint ([schema](../system/schema/llm-wiki.md)) | A single processed registry; a separate outputs folder; scheduled lint (declined 2026-10-14) |
| Deterministic helper `system/scripts/query-brain.py`; Smart Connections as optional aid | Ingest-time summaries with the likely question, exact-fix "atoms", recency decay ([Saraev](sources/new-way-build-second-brain-claude-nick-saraev.md)) |
| `audit` skill; `grill-me` skill ([Nate Herk's version](sources/grill-me-skill-10x-claude-code-nate-herk.md) adds nothing structural) | Audit checks for index truth versus disk and five freshness states ([Herk tips](sources/steal-my-ai-os-setup-5-tips-nate-herk.md)); expertise versus situational context split |
| Evidence-lock hook script | Not registered in `.claude/settings.json`, so not active |

## Local problems that exist whatever the vault count

Checked 2026-11-20: `wiki/index.md` is 1,159,899 bytes and 4,119 lines, with 3,842 lines pointing at `wiki/sources/karpathy/` mirrors; `wiki/log.md` is 926,889 bytes; `wiki/sources/karpathy/` holds 4,258 files; the ledger says the index was cut to about 31 KB on 2026-10-14 and it has regrown (cause not investigated). The earlier documented stall was different: on 2026-10-23 about 473 MiB of generated chat markdown exhausted Obsidian's memory and was moved out ([repair status](../research/computer-health/2026-10-23/repair-status.md)). Which current folder is slowing Obsidian is **not measured**; the index and the Karpathy mirrors are the leading suspects. Also: Google Drive is not mounted (no G: drive) and `git status` shows 6,262 changed or untracked paths, so two backup paths are weak.

## Decisions already on record

One vault, 2026-07-16 (after a grilling); stay at Level 2, 2026-07-17; separate vaults per data type declined 2026-10-14 with a nested sub-wiki named the compatible form; one connected vault is advice, not a lock (2026-10-07). See [decisions log](../decisions/log.md) and [adoption ledger](../references/ai-workspace/second-brain-adoptions.md).

**Joshua, 2026-11-20:** the 2026-10-14 decline of separate vaults was not a definitive rule. He was still learning and wants the best setup. Treat it as open, not as a constraint. (The 2026-07-16 one-vault decision followed a full grilling; whether it also stands is part of the open decision.)

## Options (agent synthesis, not a decision)

- **A. Keep one vault, shrink what Obsidian indexes.** Hub the 3,842-row index, ignore or relocate the Karpathy mirrors, ignore `corpus/`, `skills/`, `system/`, trim the log. Cheap, reversible, measurable.
- **B. Add a second Obsidian window on a subfolder for AI-setup material.** Nate's own pattern. No file moves.
- **C. A real second vault for AI-setup intake with a router pair.** Cost: a second intake against the "one inbox" rule, cross-vault retrieval and sync conventions ([levels reference](../references/second-brain-levels.md) says this is justified only by a real access or workflow boundary), and it revisits the provisional 2026-10-14 decline.
- **D. Split by file type.** No source supports it.

Lean from this synthesis: A first, then re-measure; C only if AI-setup material turns out to have a real boundary of its own.

## Open decision

Unresolved. To be settled by grill-me; log in [decisions](../decisions/log.md) only if it locks.
