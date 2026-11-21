---
type: source
subject: Austin Marchese tier list of ten pieces of AI advice, from LLM knowledge bases to verification
created: 2026-10-14
updated: 2026-10-14
aliases: ["7 Claude Hacks That Feel Illegal (And 3 to Avoid)", Austin Marchese AI advice tier list, Austin Marchese context fridge video]
tags: [ai-workspace, second-brain, skills, context, verification]
evidence: "../../raw/sources/clips/7-claude-hacks-austin-marchese/7 Claude Hacks That Feel Illegal (And 3 to Avoid).md"
sha256: 179cefa1606321f8d382063ffb8ed89a9959faac9a73414842d5021c6112e5ad
sources: [../../raw/sources/clips/7-claude-hacks-austin-marchese/PROVENANCE.md]
contradictions: []
---

# Austin Marchese's AI advice tier list: stale context is the one new check for ai-os

"7 Claude Hacks That Feel Illegal (And 3 to Avoid)" is a YouTube video by Austin Marchese ([YouTube](https://www.youtube.com/watch?v=hsbr0IoFZJ8)). The channel is inferred from the AUSTINM referral code. The publication date is unknown; the inbox file was last modified 2026-10-08. The full description and auto-caption transcript (captions run to 17:21) were read on 2026-10-14. Despite the title, the video ranks ten strategies from S tier to F tier. The inbox held two byte-identical copies with the same SHA-256: the original (modified 2026-10-08) and a re-clip ending in " 1.md" (modified 2026-10-14). One archive covers both; neither inbox copy was removed.

Evidence: [archived clip, provenance and hashes](../../raw/sources/clips/7-claude-hacks-austin-marchese/PROVENANCE.md). SHA-256 `179cefa1606321f8d382063ffb8ed89a9959faac9a73414842d5021c6112e5ad`.

## What he says

- **D tier: switch to free open-source models (0:27 to 1:53).** You pay for AI with money, time or output quality; cheap models cost the other two. He says today's token prices are subsidized by venture money. Optimize token use instead (a pitch for his plugin).
- **A tier: turn repeatable workflows into skills (1:59 to 3:15).** "Own the intelligence, not rent it": a skill is a file you own and can move from Claude to Codex. Do not collect skills like Pokémon. His four-step method: do the task, ask the AI to make a skill from that conversation, run the skill, then correct the output and ask it to enhance the skill.
- **C tier: give AI as much context as possible (3:16 to 4:09).** Context is like a fridge: one good item is easy to find, an overstuffed fridge is not, and one spoiled item makes everything smell. His rule: relevant context helps; outdated or conflicting context hurts. He offers a prompt that reviews every context file and flags stale ones.
- **S tier: build an LLM knowledge base (4:15 to 5:08).** His "internal OS" has `/raw` for unprocessed material and `/wiki` for extracted learnings, which works like a table of contents. A question checks the wiki first and goes to the right raw file only when it needs more.
- **Sponsor (5:35 to 7:09).** A payments platform; not relevant.
- **F tier: if you can build it, build it (7:24 to 8:32).** Do not rebuild cheap software you already pay for; his own CRM rebuild was abandoned after 10 hours. Ask whether a project is a "10x move or a 2x move".
- **A tier: plan before you build (8:52 to 9:52).** Use plan mode or "interview me". Scrutinize the plan, but do not over-plan; he quotes Brian Armstrong, "Action produces information."
- **F tier: automate everything (10:09 to 11:39).** He credits Elon Musk with five steps: question every requirement, delete parts of the process, simplify, accelerate cycle time, and only then automate. "Automating a broken process just produces garbage at scale."
- **B tier: use multiple agents (12:20 to 14:10).** More agents means more context switching. Three tactics: ask for sub-agents when a task splits into independent parts; run parallel threads only for small surface tasks, not deep work; give each agent a distinct area so they do not overlap.
- **D tier: chase new AI tools (14:12 to 15:20).** New tools cause decision fatigue and relearning. Keep one main workspace plus two or three tools for specific problems.
- **S tier: give AI a way to check its own work (15:20 to 16:51).** He attributes to the creator of Claude Code a claim that self-checking gives two to three times better output. Ask for a verification plan inside the plan; define the output structure up front; after big changes ask "How can I manually verify this?"

## Mentions in source

> "Relevant context helps. Outdated or conflicting context hurts." (3:41)

> "it'll check the wiki first, and when it needs more information, it knows exactly which raw file to look for" (4:40)

> "Based on this conversation, enhance the skill." (2:58)

> "give each agent a unique task so that you can avoid overlap" (13:41)

## How it compares with ai-os (interpretation)

Checked on disk 2026-10-14. Decisions are recorded in the [second-brain adoption ledger](../../references/ai-workspace/second-brain-adoptions.md).

| His idea | Here | Verdict |
|---|---|---|
| Context is a fridge: stale or conflicting context hurts | Always-loaded context (`CLAUDE.md`, the memory index) plus [`wiki/hot.md`](../hot.md), which the retrieval order reads first and which measured 122,010 bytes on 2026-10-14 | Adopted: a staleness check on always-loaded context in lint, and a size check on `wiki/hot.md` |
| LLM knowledge base is S tier; read the wiki first, then raw | The retrieval order in `CLAUDE.md` and the [vault schema](../../system/schema/llm-wiki.md) | Already |
| Build a skill by doing the task, then improve it each run | `CLAUDE.md`: "When a skill run exposes a gap, improve the skill before moving on." | Already |
| Verification plans | The `verification-before-completion` skill | Already |
| Musk's five steps before automating | `level-up` enforces "Eliminate first" before any build ([Three Ms](../../references/3ms-framework.md)) | Already |
| Split work across agents only in clean partitions | `CLAUDE.md`: delegate bulk work to sub-agents; never two runtimes on the same file | Already |
| Do not collect skills you do not use | The catalog is inert storage and skills run only once activated by copy | Not yet evaluated |

- **Most of this list is already practice here.** The knowledge base, skill refinement, planning, verification and agent partitioning all have an owner in `CLAUDE.md` or a skill.
- **The fridge is the useful warning.** Every line of always-loaded context costs attention on every message, and a stale line misleads quietly. `wiki/hot.md` is the first file in the retrieval order, so its size and freshness matter most; at 122 KB it is far from a quick read.
- **Musk's steps are covered in spirit, not word for word.** `level-up` puts elimination first and building last, which is the core of his list.

Related: [harness engineering video](harness-engineering-austin-marchese.md), [Karpathy's method video](stop-prompting-claude-karpathy-method-austin-marchese.md), [six automation steps](automate-99-percent-work-claude-austin-marchese.md), [Matt Pocock's skill process](matt-pocock-system-claude-skills-austin-marchese.md), [AI workspace hub](../../references/ai-workspace/index.md).

## Limits

- Auto-captions. Likely mis-hearings: "Wopp" (the sponsor, Whop per the description), "paralyzing" (parallelizing), "Cloud Code" (Claude Code), "Knowledgbase" (a description typo).
- Unverified claims: venture-subsidized token prices and a possible 20x price rise, the two-to-three-times quality figure attributed to the creator of Claude Code, and his biography and audience numbers.
- His stale-context audit prompt and on-screen knowledge base were not visible in the clip text.
- The tier assignments are his opinion, not measured.
