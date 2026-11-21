---
type: source
subject: Tina Huang video on Obsidian basics and three levels of AI integration (second brain, AI database, LLM wiki)
created: 2026-10-14
updated: 2026-10-14
aliases: [Obsidian in 24 Minutes, Tina Huang Obsidian video, three levels of Obsidian and AI]
tags: [ai-workspace, second-brain, obsidian, llm-wiki]
evidence: "../../raw/sources/clips/obsidian-in-24-minutes-tina-huang/Obsidian in 24 Minutes.md"
sha256: d589e9f46ceee678d3d552797c11c1018bc33b2f8e79f37bdc15348ed03e5d7f
sources: [../../raw/sources/clips/obsidian-in-24-minutes-tina-huang/PROVENANCE.md]
contradictions: []
---

# Tina Huang's three levels of Obsidian plus AI: ai-os already runs level three

"Obsidian in 24 Minutes" is a YouTube video by Tina Huang ([YouTube](https://www.youtube.com/watch?v=4Hvkv_I8QDE)); she names herself at 1:49. The publication date is unknown; the inbox file was last modified 2026-10-14. The description and the auto-caption transcript (to 24:13) were read in full on 2026-10-14. On-screen summary slides and the quiz questions were not in the clip text.

Evidence: [archived clip, provenance and hashes](../../raw/sources/clips/obsidian-in-24-minutes-tina-huang/PROVENANCE.md). SHA-256 `d589e9f46ceee678d3d552797c11c1018bc33b2f8e79f37bdc15348ed03e5d7f`.

## What she says

- **Obsidian basics (1:19 to 5:05).** A vault is one local folder of Markdown files. Features she walks through: wikilinks and unresolved "stub" links, local and full graph view, search, community plugins, themes, embeds, metadata with table, Kanban and dashboard views, and the command palette. Obsidian Sync is one of the few paid features and is end-to-end encrypted.
- **Level 1, AI second brain (6:39 to 10:46).** You write the notes; the AI reads them. She points Claude Cowork at her vault for questions and Codex when she wants to build something from it (a "is this video worth filming" checklist). For full privacy she names open-source harnesses with local models. Community plugins are a second way in: she names Smart Connections and Copilot without demonstrating either (9:47). She credits Tiago Forte and Nick Milo for the second-brain idea.
- **Level 2, AI database (12:22 to 16:17).** The reverse: agents write into the vault and you read. Her bots log food from a photo, write process docs and Pomodoro logs; Obsidian Sync shares the vault across a laptop, a Mac Studio and a VPS. She then asks an agent for productivity advice grounded in that logged data. She recommends this level first for people who do not take notes.
- **Level 3, LLM wiki (16:32 to 23:50).** Karpathy's pattern: raw sources the LLM never edits, a wiki the LLM owns, and a schema file (`CLAUDE.md` or `AGENTS.md`). Three operations: ingest, query, lint. Two special files: `index.md` (catalog) and `log.md` (append-only history). Her Hermes agent runs an "LLM wiki" skill fed through a Telegram bot. She says Claude Code is the best-documented route and that the idea file is vague on purpose, so any agent can implement it.
- **Retention (24:13).** She ends with a quiz because immediate review aids retention.

## Mentions in source

> "Level one is just pointing your AI at Obsidian." (6:39)

> "Stuff like smart connections and co-pilot." (9:47)

> "For level two, it's the other way around. This is about AI writing notes into your Obsidian vault" (12:22)

> "Obsidian is treated as the IDE, the LLM acts as the programmer, and the vault itself is the code base." (16:32)

## How it compares with ai-os (interpretation)

Checked on disk 2026-10-14.

| Her level or idea | Here | Verdict |
|---|---|---|
| Level 1: point an agent at the vault | Claude Code and Codex both open `dev/ai-os` through the `CLAUDE.md` / `AGENTS.md` router | Already here |
| Smart Connections as a plugin route | **Already here.** Joshua installed Smart Connections 4.7.2 and Smart Context 3.3.2 on 2026-10-14 (`.obsidian/plugins/`), with local embeddings in the git-ignored `.smart-env/`. The same day the line "there is no semantic search and none is needed" was removed from `CLAUDE.md` and `AGENTS.md`. How agents should use it is open: see AQ-010 in the [AI action queue](../../references/ai-workspace/action-queue.md) | Already here; role unsettled |
| Level 2: agents write logs into the vault | Agents write generated files and ledgers (`wiki/log.md`, `wiki/hot.md`, `students/` records); live systems stay authoritative per [connections](../../connections.md) rather than being copied in | Already here in the narrower form the vault allows |
| Level 3: LLM wiki with raw, wiki, schema, index, log, lint | The [LLM Wiki pattern](llm-wiki-pattern.md) and [schema](../../system/schema/llm-wiki.md), with `second-brain-ingest`, `-query` and `-lint` | Already here |
| Obsidian Sync across machines | GitHub sync and the Drive backup ([sync setup](../../setup/github-sync/README.md)) | Different route, same need covered |
| End-of-lesson quiz for retention | LSAT U recaps and drills already include recall steps (for example RRC's "The Recall") | Already here; not queued |

- **Her ladder matches the existing levels page.** Her three levels map onto levels 1 and 2 of the [second-brain levels reference](../../references/second-brain-levels.md); she does not cover graphs or always-on automation. Semantic search (level 3 there) only appears as a plugin name.
- **Nothing new to build from the method itself.** The useful action is to settle what the newly installed Smart Connections is for, which the video does not answer.

Related: [Dan Martell's AI brain](ai-system-so-smart-dan-martell.md), [Nate Herk's LLM wiki demo](fable-5-karpathy-llm-wiki-nate-herk.md), [GD4AI wiki plugin](gd4ai-obsidian-llm-wiki.md), [Jeff Su on personal agents](personal-agents-clearly-explained-jeff-su.md), [Obsidian command center](../../references/obsidian-command-center.md), [second-brain adoption ledger](../../references/ai-workspace/second-brain-adoptions.md).

## Limits

- Auto-captions: "Jan Spark", "Jen Spark" and "GenSpark" are the sponsor Genspark; "Claude Cohere" and "Co-work" are Claude Cowork; "Aura ring" is likely Oura. Her model names ("Deep Seek V4 Pro", "Qwen 3.6 36B") were not checked.
- Her claims about Obsidian's user count and security are unverified.
- Smart Connections and Copilot are only named, not shown; nothing here tests either plugin.


## Queue record

Done 2026-10-26: AQ-010. Settled operational role under delegated judgment: Smart Connections remains an optional Obsidian aid, with catalog/alias retrieval and the bounded helper serving agents. No claim of semantic-search quality comparison. [Implementation record](../../research/2026-10-26-source-implementation/REPORT.md).
