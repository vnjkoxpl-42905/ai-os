---
type: synthesis
subject: How Joshua's second brain should be set up, from all second-brain sources, and the top-tier practices ai-os does not do yet
created: 2026-11-20
updated: 2026-11-20
aliases: [second brain setup playbook, how to set up the vault, top-tier second brain practices, what ai-os is missing]
tags: [ai-workspace, second-brain, setup, decision-pending]
sources:
  - second-brain-one-vault-vs-many.md
  - sources/every-level-of-a-claude-second-brain-nate-herk.md
  - sources/steal-my-ai-os-setup-5-tips-nate-herk.md
  - sources/agentic-os-setup-10x-claude-code-chase-ai.md
  - sources/new-agentic-os-standard-claude-5-robonuggets.md
  - sources/ultimate-second-brain-arms-robonuggets.md
  - sources/self-improving-claude-knowledge-base-one-prompt-robonuggets.md
  - sources/new-way-build-second-brain-claude-nick-saraev.md
  - sources/grill-me-skill-10x-claude-code-nate-herk.md
  - sources/llm-wiki-pattern.md
---

# How the second brain should be set up

Written 2026-11-20 from the second-brain source pages listed above and the [one vault or several](second-brain-one-vault-vs-many.md) synthesis. Source claims are attributed; local state was checked on disk 2026-11-20. Nothing here is decided. It feeds the grilling in `brainstorms/2026-11-20-ai-setup-vault-organization.md`.

## The plain picture

Think of the vault as a library.

| Library part | ai-os file | What it does |
|---|---|---|
| Front desk sign: "LSAT stuff is upstairs, students are in room 3" | `CLAUDE.md` | Tells the AI which area to go to. Loads every message. |
| A floor directory in each area | an `index.md` per folder | Lists what is in that area, one line each. The AI reads it before opening pages. |
| The catalog for the whole building | `wiki/index.md` (the "master list") | One line per wiki page, so the AI can find a page without opening thousands of files. |
| The archive in the basement | `raw/` | Original clips and exports. Never edited. |
| The shelves | `wiki/`, `corpus/`, `students/` | Pages the AI writes from the originals. |
| The diary | `wiki/log.md` | Dated record of every change. |
| A sticky note on the desk | `wiki/hot.md` | What was happening last session. |

Every source agrees on this shape. The disagreements are about extras.

## What every source agrees on (and ai-os already does)

1. One folder holds everything. No source splits vaults to fix speed.
2. A router file at the top, a small index at each level.
3. Originals stay untouched; the AI writes summaries from them.
4. Look things up before reading; never load everything.
5. Add machinery (search engines, graphs, schedules) only when a real problem shows up.

ai-os has 1 to 4. Number 5 is where it has drifted: some files grew too big to be useful.

## Top-tier practices ai-os is not doing yet

Ranked by value for effort, highest first. Each says what it looks like here.

| # | Practice | Who teaches it | What it would look like in ai-os | Status |
|---|---|---|---|---|
| 1 | **Every index stays small** (a directory, not an encyclopedia) | Chase AI, Nate Herk, Karpathy | `wiki/index.md` under about 60 KB (done 2026-11-20). Still too big: `skills/INDEX.md` 345 KB, `wiki/log.md` 931 KB. Split the skill index by area; move old log entries to dated yearly files. | Partly done |
| 2 | **Index-truth audit** (does the list match what is on disk?) | Nate Herk | A report-only script that flags pages on disk missing from an index, and index lines pointing at nothing. Would have caught the index regrowing to 1.16 MB. | Not built |
| 3 | **Ingest-time summary with the likely question** | Nick Saraev | When a source is filed, its page gets one line: "Answers: what should I measure before adding a graph?" The AI searches those lines first. The existing source pages already end with an example question; making it a front-matter field makes it searchable. | Half there |
| 4 | **"Atoms": exact fixes and decisions saved verbatim** | Nick Saraev | One file per hard-won fix ("Cal.com pending = unpaid, link expires in 30 min"). ai-os does this already in native memory; the gap is that memory is only visible to Claude, not Codex or you in Obsidian. | Mostly done |
| 5 | **Freshness labels** (fresh, drifting, frozen, retired) | Nate Herk | A `freshness:` field on pages about live things (pricing, schedules, tools). Lint flags "fresh" pages untouched in 60 days. | Not built |
| 6 | **A processed-sources registry** | RoboNuggets | One generated file listing every raw source and the page it became. Today you can only tell by searching for the hash. Ends the "is this clip already done?" question. | Not built |
| 7 | **An outputs folder** | Chase AI, RoboNuggets | Finished deliverables (reports, decks, exports) in one place, separate from knowledge. Today they scatter across `research/`, `handoffs/` and project folders. | Not built; low value |
| 8 | **A scheduled weekly check, report only** | RoboNuggets ("dream sequence") | A weekly routine that runs lint plus the index-truth audit and writes a report to `audits/`. It changes nothing; you approve fixes. The earlier "no scheduled lint" decision (2026-10-14) was about the AI rewriting pages unattended, which this avoids. | Declined before; report-only form is new |
| 9 | **Backtrack on a miss** | Nate Herk | When the AI fails to find something, it writes down where it looked and where it should have looked, then fixes the router. `references/second-brain-levels.md` describes this; nothing enforces it. | Described, not used |
| 10 | **Working backups** | (local need, not a source) | Drive is not mounted and 6,262 paths are uncommitted. A second brain you can lose is not a second brain. | Broken |

## What not to do (sources agree, or evidence is thin)

- A second Obsidian vault for speed: no source does it for that reason.
- Vector search or a knowledge graph now: they help with needle lookups and question chains; no felt miss yet ([five levels](sources/every-level-of-a-claude-second-brain-nate-herk.md)).
- Letting the AI rewrite its own rules on a schedule: no review gate ([one-prompt KB](sources/self-improving-claude-knowledge-base-one-prompt-robonuggets.md)).
- Dashboards: RoboNuggets and Chase AI both put them at 10 to 30 percent of the value, after the files are right.

## The direction (recommendation, not locked)

1. **Fix backups first** (Drive sign-in, commit in small pieces).
2. **Keep one vault.** Shrink the three oversized files (index done; log and skill index next).
3. **Add the index-truth audit, run weekly, report only.** This is the guard that stops things regrowing.
4. **Add the likely-question line and the processed registry** to the ingest step.
5. **Revisit a second vault only if** Obsidian is still slow after 2 and 3, or AI-setup notes turn out never to link to LSAT or student notes.

## Open decision

Unresolved. See the brainstorm file above; log in [decisions](../decisions/log.md) only when Joshua locks it.
