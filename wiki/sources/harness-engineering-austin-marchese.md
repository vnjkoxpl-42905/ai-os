---
type: source
subject: Austin Marchese video on harness engineering, the domain layer built on top of Claude Code
created: 2026-10-14
updated: 2026-10-14
aliases: [Stop Prompting Claude. Start Harness Engineering, Austin Marchese harness engineering video, domain harness]
tags: [ai-workspace, second-brain, harness, skills, feedback-loop]
evidence: "../../raw/sources/clips/harness-engineering-austin-marchese/Stop Prompting Claude. Start Harness Engineering.md"
sha256: ed91a1b7630ac008a8bed1235e88b9dae47d8aa959eb8bb108a17f4dee21587b
sources: [../../raw/sources/clips/harness-engineering-austin-marchese/PROVENANCE.md]
contradictions: []
---

# Austin Marchese's harness engineering: ai-os is already a domain harness; the missing part was logging retrieval misses

"Stop Prompting Claude. Start Harness Engineering" is a YouTube video by Austin Marchese ([YouTube](https://www.youtube.com/watch?v=bIYWxYm5cOY)). The channel is inferred from the clau.de/austin.marchese link. The publication date is unknown; the inbox file was last modified 2026-10-14. The full description and auto-caption transcript (captions run to 16:15) were read on 2026-10-14. He says Anthropic sponsored the video (4:57).

Evidence: [archived clip, provenance and hashes](../../raw/sources/clips/harness-engineering-austin-marchese/PROVENANCE.md). SHA-256 `ed91a1b7630ac008a8bed1235e88b9dae47d8aa959eb8bb108a17f4dee21587b`.

## What he says

- **Why harnesses matter (0:31 to 1:14).** He cites Meta's Muse and the Grok Bot as harnesses whose ease of use drove adoption, and attributes to Pieter Levels a remark that a recent Y Combinator batch was all harness and hardware startups.
- **The output equation (1:14 to 2:42).** Output equals model plus prompt, multiplied by the base harness (for example, Claude Code). He says the leaders add a domain harness on top: their own layer built from deep knowledge of their own workflow.
- **Pick a domain (2:52 to 4:51).** He attributes to a McKinsey report three roles: makers (build models), takers (use vendor tools as shipped) and shapers (build a layer on someone else's model). Shape what you already do; design for one user, yourself.
- **Sponsor segment (4:57 to 6:55).** Anthropic product changes: chat and Cowork merged, design, docs and slides inside conversations, shared context across chats. Vendor claims, not checked.
- **Build the harness, do not reinvent (7:05 to 8:42).** Claude already does 90 to 95% of what you need; build only the domain layer. He lists eight parts: rules, skills, MCP servers, context (a knowledge graph helps at scale), hooks, sub-agents, the interface, and a feedback mechanism. Rule two: keep it simple.
- **Example: an internal knowledge harness (9:10 to 11:35).** It answers only from documents you provide. Two skills: `KB answer`, which answers only from local context, and `KB sync`, which pulls context in from Google Drive, Notion or similar through MCP. A one-page web interface has Sync and Send buttons and a feedback control; when an answer misses context, you add the missing data and ingest it.
- **The interface is the most important layer (12:29 to 14:20).** The same capabilities feel different through different interfaces. He prefers a local web page: he says it runs on your Claude subscription instead of API credits, it is fast to change (he edits his with a pencil icon), and it can later scale to a team.
- **The "Karpathy curve" (14:46 to 15:50).** He attributes to Karpathy a view that the model is the least interesting part of the stack and the real work is data curation, task decomposition and organizational adaptation. Winners build the best harness for their own situation.

## Mentions in source

> "One called KB answer that only pulls its answer from local context provided" (9:53)

> "if you're missing context, it's easy to know and then add it to the system" (10:14)

> "Then there's hooks. These are scripts that run on specific events, such as a blocking command or running a test after an edit." (7:45)

> "Claude already does 90 to 95% of what you needed" (7:13)

## How it compares with ai-os (interpretation)

Checked on disk 2026-10-14. Decisions are recorded in the [second-brain adoption ledger](../../references/ai-workspace/second-brain-adoptions.md).

| His idea | Here | Verdict |
|---|---|---|
| Eight harness parts | Rules: `CLAUDE.md` and `AGENTS.md`. Skills: the catalog plus activated copies. MCP: few on purpose; CLIs (`gws`, `gh`, Firecrawl) preferred. Context: `wiki/`, `corpus/`, `students/`. Hooks: `.claude/settings.json` and a git pre-commit hook. Sub-agents: `agents/`. Interface: terminal and Obsidian. Feedback: `wrapup`, lint, `level-up` | Present in some form |
| `KB answer`: answer only from local documents | A "not wiki-backed" label in `second-brain-query` when the answer does not come from the vault | Adopted |
| `KB sync`: copy Drive or Notion into the knowledge base | Live systems stay authoritative and are read live, per [connections](../../connections.md) | Deliberately different |
| Feedback: missing context goes back into ingest | Retrieval misses are logged as query entries with a Miss line so routing gets fixed | Adopted |
| A local web interface with buttons | No dashboard; see [obsidian-command-center](../../references/obsidian-command-center.md) | Not yet evaluated |
| Keep it simple; extend Claude Code instead of rebuilding it | ai-os is built on Claude Code and Codex, not on raw APIs | Not yet evaluated |

- **In his terms, ai-os is already a domain harness.** All eight parts exist in some form, built for one user. The video names the parts; it does not add a new one.
- **Syncing copies of live systems would recreate the stale-context problem.** His `KB sync` pulls external documents into the knowledge base. Here, Cal.com, Calendar, Supabase, Stripe and Gmail stay the authority, and the brain mirrors them only with a date and the system checked.
- **The feedback loop is the piece worth taking.** A question the wiki could not answer is evidence that routing or coverage failed. Logging it as a Miss turns that failure into a fix list.

Related: [7 Claude hacks video](7-claude-hacks-austin-marchese.md), [Karpathy's method video](stop-prompting-claude-karpathy-method-austin-marchese.md), [Claude plus Codex](../../references/claude-plus-codex.md), [six automation steps](automate-99-percent-work-claude-austin-marchese.md), [Matt Pocock's skill process](matt-pocock-system-claude-skills-austin-marchese.md), [AI workspace hub](../../references/ai-workspace/index.md).

## Limits

- Auto-captions. Likely mis-hearings: "Grockbot" and "Grockpot" (Grok Bot, per the description), "Peter Levelvels" (probably Pieter Levels), "McKenzie" (probably McKinsey), "Carpathy" (Karpathy), "hardness" (harness), "dumerism" (doomerism), "claw design" and "clawed docs" (Claude design and docs).
- Unverified: the Pieter Levels quote, the McKinsey makers, takers and shapers report, the "Karpathy curve" as a Karpathy concept (no source is shown), Anthropic's product changes, and his claim that a local app can use a Claude subscription instead of API credits.
- His full build prompt was on screen and is not in the clip text.
