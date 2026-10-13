---
type: source
subject: Nate Herk video, setting up an AI OS in Codex with GPT-6 Astra
created: 2026-10-12
updated: 2026-10-12
aliases: [I Turned GPT-6 Astra Into the Ultimate AI Second Brain, AIS-OS resource pack clip]
tags: [ai-workspace, second-brain, codex, four-cs, skills]
sources: [../../raw/sources/clips/gpt-6-astra-ultimate-second-brain/PROVENANCE.md]
---

# The AIS-OS starter kit in Codex: every skill he gives away is already on this machine

"I Turned GPT-6 Astra Into the Ultimate AI Second Brain" is a YouTube video by Nate Herk ([YouTube](https://www.youtube.com/watch?v=yysILVsfLFM), published on or after 2026-09-07, clipped 2026-10-08). The full description and transcript (about 19:31) were read on 2026-10-12. It is the Codex version of his [Claude second-brain walkthrough](claude-ultimate-second-brain-nate-herk.md).

Evidence: [archived clip, provenance and hashes](../../raw/sources/clips/gpt-6-astra-ultimate-second-brain/PROVENANCE.md). SHA-256 `57f95f791170feb5104bb948638681ecf01170da6a05d9ecd15655bdee62256b`.

## What he says

- **Four Cs again (2:12).** Context is slow-changing facts (goals, offer, audience); connections are live tools (email, Slack, ClickUp, finance). Three tests that the OS is working: it answers a teammate's question better than you, you stop switching tabs, and you stop trying to remember things.
- **Free resource pack (4:51).** Five skills from his community: `onboard` (builds the folders and asks seven questions), `audit` (Four Cs score, saved to `audits/` each run), `link` (adds routing to `AGENTS.md`), `level-up` (turns an audit into the next automation) and `3d-brain` (renders the knowledge as an interactive graph). `grill-me` is added to the kit later. His demo scored 30/100 on day one.
- **AGENTS.md is the router (5:43).** Same content as `CLAUDE.md`; a few core rules (concise, bullets, no em dashes, Oxford comma) and then mostly a routing map. Copy `CLAUDE.md` to `AGENTS.md` when moving to Codex.
- **Loop (13:41).** Audit, level up, build, repeat. The hard part is getting knowledge out of your head; use grill-me on one topic per session.
- **Wikis (15:26).** Paste Karpathy's LLM Wiki gist and ask for a wiki. He now keeps separate vaults for YouTube videos, business and meeting transcripts.
- **Model choice (17:28).** Astra is overkill for most knowledge work and burns the weekly limit; try a cheaper model and lower effort for routine skills. Same advice as his [Sonnet vs Opus test](sonnet-5-5-vs-opus-5-5-nate-herk.md).

## How it compares with ai-os (interpretation)

Checked on disk 2026-10-12:

| His kit | Here |
|---|---|
| `onboard`, `link`, `3d-brain` | Installed in `~/.claude/skills/` (home, Claude only). Not in the vault catalog. |
| `audit`, `level-up`, `grill-me` | Installed in home and in both catalogs (`skills/claude`, `skills/codex`); listed as active in the root `CLAUDE.md` |
| Router `AGENTS.md` + `CLAUDE.md` | Twin files with a byte-identical routing map |
| Karpathy LLM Wiki | The vault schema, [system/schema/llm-wiki.md](../../system/schema/llm-wiki.md) |
| One vault per domain | One vault with separate domain homes (`wiki/`, `corpus/`, `students/`); see [second-brain levels](../../references/second-brain-levels.md) |

- **Nothing new to install.** Every skill in the pack is already present. `onboard`, `link` and `3d-brain` exist only as Claude home copies, so Codex does not have them; that gap is undeclared in `skills/PARITY.md`. `onboard` is a day-one tool and probably not needed now.
- **The 3D brain overlaps Graphify.** We already have Graphify for graph views ([Graphify bridge](../../references/graphify-obsidian-bridge.md)). `3d-brain` has not been run here.
- **His rule set mirrors ours**, down to "no em dashes."

## Status

Captured. No install or change made.

Related: [Claude second-brain walkthrough](claude-ultimate-second-brain-nate-herk.md), [Three Ms framework](../../references/3ms-framework.md), [AI workspace hub](../../references/ai-workspace/index.md).
