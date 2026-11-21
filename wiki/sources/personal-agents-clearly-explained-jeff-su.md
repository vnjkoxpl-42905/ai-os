---
type: source
subject: Jeff Su video comparing chatbots, do-it-yourself agents with memory files, and proactive personal agents
created: 2026-10-14
updated: 2026-10-14
aliases: [Personal Agents Clearly Explained, Jeff Su personal agents, DIY agents vs personal agents, Jeff OS]
tags: [ai-workspace, agents, memory, privacy]
evidence: "../../raw/sources/clips/personal-agents-clearly-explained-jeff-su/Personal Agents, Clearly Explained.md"
sha256: 47a99d516cb4f21030ff9be64a3308c3468dd71ab536f111a539befb49c8955f
sources: [../../raw/sources/clips/personal-agents-clearly-explained-jeff-su/PROVENANCE.md]
contradictions: []
---

# Jeff Su on personal agents: a folder of memory files you own beats a proactive app you rent

"Personal Agents, Clearly Explained" is a YouTube video by Jeff Su ([YouTube](https://www.youtube.com/watch?v=HdI_aYzgJIg)), inferred from the jeffsu.org links. The publication date is unknown; the inbox file was last modified 2026-10-14. The description and the auto-caption transcript (to 15:18) were read in full on 2026-10-14.

Evidence: [archived clip, provenance and hashes](../../raw/sources/clips/personal-agents-clearly-explained-jeff-su/PROVENANCE.md). SHA-256 `47a99d516cb4f21030ff9be64a3308c3468dd71ab536f111a539befb49c8955f`.

## What he says

- **Three categories (0:30 to 3:30).** Chatbots handle one-off tasks with no memory. "DIY agents" (he names ChatGPT Work, Codex, Claude Code, Gemini Spark) read and update files you have given them, so a new health report is filed, compared with five years of history and written back into a health memory file. "Personal agents" (Meta's Muse, ChatGPT dots, xAI's Grok bot as captioned) are the proactive version: they message you before you ask.
- **How DIY agents work (3:56 to 7:37).** Rules, preferences and memory live in plain text files the agent reads when a task calls for them. His "Jeff OS" home folder has 100+ files in 30+ area folders that the agent wrote for him. One governance file makes every reply end with a "what's next" section of his remaining actions. Examples: a family `memory.md` that catches a brother's shellfish allergy; a trip request that pulls travel preferences, a Notion people database, calendar conflicts and project deadlines.
- **Personal agents (8:01 to 12:00).** They come ready-built: Muse interviewed him about sleep and created a goal and a bedtime checklist. Its system files look like his (`agent.md`, `memory.md`). The real difference is proactivity: they watch continuously on their own cloud computers, so they catch things a once-a-day scheduled task would miss. Downsides: immature, one standardized system, and lock-in that grows with what the agent knows.
- **Privacy (12:31).** He treats it as personal preference; for private personal agents he names OpenClaw and Hermes with local models and notes they are hard to set up and cannot run the strongest models.
- **Choice (13:44).** Personal agent for the easiest start; DIY agent for power, tailoring and portability. He expects labs to fold proactive features into their DIY agents.

## Mentions in source

> "personal agents are just the proactive version of DIY agents." (2:39)

> "I tell the AI my preference once, it writes it down, and it follows the rule forever." (4:27)

> "the more a personal agent knows about you, the harder it will be to switch to another one." (12:00)

> "my Jeff OS home folder is just a bunch of folders and text files." (14:20)

## How it compares with ai-os (interpretation)

Checked on disk 2026-10-14.

- **ai-os is his DIY agent, built further.** One Markdown vault read by both Claude Code and Codex through `CLAUDE.md` and `AGENTS.md`, native automemory, and domain homes. His portability argument is the reason the vault keeps dual-runtime parity ([PARITY](../../skills/PARITY.md)).
- **Proactivity exists in narrow, approved slots.** The pre-consult check-in and accommodations email are pre-authorized sends; everything else drafts. His "always watching" agent would conflict with draft-by-default and the send-only-on-"send" rule, so it is not queued.
- **His "what's next" reply rule** is a personal preference, not a method claim. Joshua's root rules already say to state what was skipped and why; not queued.
- **Nothing actionable.** No queue item was added from this source.

Related: [Jeff Su's file rulebook](stop-organizing-files-yourself-jeff-su.md), [Tina Huang's Obsidian levels](obsidian-in-24-minutes-tina-huang.md), [Chase AI's Claude OS](jev-claude-os-chase-ai.md), [second-brain adoption ledger](../../references/ai-workspace/second-brain-adoptions.md).

## Limits

- Auto-captions: "Rockbot" and "GrokBot" are presumably Grok; "Cloud Code" is Claude Code; "claw.md" is likely `CLAUDE.md`. The product names Muse, dots and Gemini Spark were not checked against official sources.
- Claims about personal agents running on dedicated cloud computers are his description, unverified.
