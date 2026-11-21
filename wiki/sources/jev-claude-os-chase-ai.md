---
type: source
subject: Chase AI video on a three-layer Claude OS with a Jev model router, Obsidian memory and a skill backbone
created: 2026-10-14
updated: 2026-10-14
aliases: [This NEW Jev + Claude OS Just Changed Every AI Workflow, Chase AI Jev Claude OS video, Chase AI agentic OS]
tags: [ai-workspace, second-brain, skills, obsidian, automation]
evidence: "../../raw/sources/clips/jev-claude-os-chase-ai/This NEW Jev + Claude OS Just Changed Every AI Workflow.md"
sha256: 87be4e78b58ee854342c3ad8eb88e38429be40446fd5637b57eafbdcc2af7ab3
sources: [../../raw/sources/clips/jev-claude-os-chase-ai/PROVENANCE.md]
contradictions: []
---

# Chase AI's Claude OS: mining 30 days of session logs for skills is the one step ai-os lacked

"This NEW Jev + Claude OS Just Changed Every AI Workflow" is a YouTube video by Chase AI ([YouTube](https://www.youtube.com/watch?v=EOdXR6lU5ZA)). The channel is inferred from the skool.com/chase-ai and chaseai.io links. The publication date is unknown; the inbox file was last modified 2026-10-08. The full description and auto-caption transcript (captions run to 21:58) were read on 2026-10-14. The description's chapter list puts "12:58 - Final Thoughts" after "19:59", which looks like a typo; the closing section starts near 21:58. It extends his earlier [command-center video](../../references/obsidian-command-center.md).

Evidence: [archived clip, provenance and hashes](../../raw/sources/clips/jev-claude-os-chase-ai/PROVENANCE.md). SHA-256 `87be4e78b58ee854342c3ad8eb88e38429be40446fd5637b57eafbdcc2af7ab3`.

## What he says

- **Three layers (1:08 to 2:59).** A visual layer: a custom dashboard web app, also ported to an Obsidian plugin, that runs on Claude Code or Codex, with buttons for skills and automations and tabs for audience and research. A memory layer: Obsidian, where he says the value is the file and folder structure, not the graph view, and "this is not a rag system". A skill layer, which he calls the backbone of everything.
- **Outputs feed back (3:31).** Reports and graphics on the dashboard are deliverables produced by skills, and they flow back into the system.
- **Request routing (4:31 to 8:26).** A voice request goes from the plugin or web app to a "bridge". The bridge records the request in Obsidian and runs local speech: Whisper for transcription and an open-source voice model for replies. Jev then classifies each request into three tiers. Tier 1 uses no AI at all (open a report, open the terminal); the caption has him saying "hundreds of a millisecond", which is garbled but means very fast. Tier 2 goes to a small model (Haiku or Luna). Tier 3 opens full Claude Code or Codex in a terminal. Everything, deliverables and conversations, is logged back into Obsidian.
- **What Jev is (8:52 to 10:29).** He says Jev is an AI system but not an LLM. It returns probabilities over predefined choices (his example: 92% "billing" for a refund complaint). He claims it is about 200 times faster and cheaper than an LLM for this kind of choice.
- **Build the skill backbone (10:55 to 13:48).** Turn everything you do into skills, then turn the right ones into automations. Two ways to find them. First, ask Claude Code or Codex to read their own conversation logs from the last 30+ days and propose skills; he says that one sentence is the whole prompt. Second, talk for 10 to 20 minutes about your work, then ask for skill and automation ideas. Then ask Claude to make chosen skills into routines or scheduled tasks.
- **Consolidate deliverables (14:18 to 15:13).** Put reports and metrics in one place instead of scattering them.
- **Memory and Obsidian (15:13 to 19:59).** Everything that goes in or comes out is recorded in the vault. He says Obsidian gives no "magic upgrade" to memory; the value is entirely in how files and folders are organized. He describes a Karpathy-style layout of `raw/`, `wiki/` and `outputs/`, with an example: research on AI agents lands in raw, becomes wiki articles, then a slide deck in outputs. Any structure works if both the human and the AI can navigate it. He suggests asking the AI to propose a structure, and says it will move files and folders as it sees fit. He also says to describe the vault structure and the rules for adding files in `CLAUDE.md` or `AGENTS.md` so it does not drift.
- **Dashboards for teams (20:04 to 21:28).** Buttons call a headless Claude Code or Codex, so teammates and clients can run skills without opening a terminal.
- **Pitch (3:31, 21:58).** His paid community sells the exact setup.

## Mentions in source

> "based on everything I've done over the last 30 days, are there any skills we could create?" (12:04)

> "the power of bringing Obsidian in the memory layer is not in Obsidian itself" (16:31)

> "you tell it what the vault structure looks like" (19:39)

> "it will map it out and move files and folders as it sees fit" (19:16)

## How it compares with ai-os (interpretation)

Checked on disk 2026-10-14. Decisions are recorded in the [second-brain adoption ledger](../../references/ai-workspace/second-brain-adoptions.md).

| His idea | Here | Verdict |
|---|---|---|
| Three layers: dashboard, Obsidian memory, skill backbone | Vault memory and a skill catalog; no dashboard. Already compared in [obsidian-command-center](../../references/obsidian-command-center.md) | Already compared |
| Jev routes requests to no AI, a small model or a full model | Nothing equivalent | Skipped (unverified claim) |
| Log every request and deliverable in the vault | `handoffs/`, the `chat-export` skill, [send ledger](../send-ledger.md) | Already |
| Mine the last 30 days of Claude and Codex session logs for skill candidates | A step in `level-up` | Adopted |
| `raw/`, `wiki/`, `outputs/` | Domain homes: `raw/`, `wiki/`, `corpus/`, `students/`, `references/` | Equivalent |
| Headless skill buttons on a dashboard | The command-center reference records "no dashboard buttons yet" | Skipped |
| Let the AI move files and folders as it sees fit | The schema says "No bulk move or rename is implied" | Conflicts |
| Describe the vault structure and add-file rules in `CLAUDE.md` | The routing map in `CLAUDE.md` and the [vault schema](../../system/schema/llm-wiki.md) already do this | Not yet evaluated |
| Talk for 10 to 20 minutes, then ask for skill ideas | `grill-me` and the `level-up` interview are the nearest tools | Not yet evaluated |

- **His memory message matches ours.** Structure is the value; Obsidian is a viewer. The schema already says tools improve the workflow without becoming requirements.
- **The log-mining step has a local precedent.** The [Three Ms reference](../../references/3ms-framework.md) already records a 2026-10-08 filter: collect recurring friction from session evidence before building. His version makes it a concrete prompt over the last 30 days of Claude and Codex logs, which is why it lands as a `level-up` step.
- **Moving files on the model's judgment is the part to refuse.** Pages link to each other by path, and archived evidence is immutable. A proposal Joshua approves is fine; an unattended reshuffle is not.

Related: [Nate Herk's LLM wiki demo](fable-5-karpathy-llm-wiki-nate-herk.md), [Herdr video](herdr-claude-codex-headache.md), [AI workspace hub](../../references/ai-workspace/index.md).

## Limits

- **Jev is unidentified.** The captions spell it Jev, Jeb and Jeff and attribute it to "type safer". What it is, who makes it, and his speed and cost claims (sub-second tier 1, about 200 times cheaper) could not be checked from the clip.
- Auto-captions. Likely mis-hearings: "Aentic" and "Ontic OS" (agentic OS), "clawed", "cla" and "Claw OS" (Claude OS), "Codeex" and "CODC" (Codex), "Carpathy" (Karpathy), "Coakoro" (probably the Kokoro voice model), "Babel" (probably Fable, which he names later), "Jarvis hood" (possibly a HUD).
- His statement that Karpathy "works with anthropic now I believe" (16:57) is his own hedge and was not checked.
- The on-screen dashboard and folder layout were not visible in the clip text.
