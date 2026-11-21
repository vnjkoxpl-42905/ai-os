---
type: source
subject: Nate Herk video building a Karpathy-style LLM wiki in Obsidian with Claude Code and Fable 5
created: 2026-10-14
updated: 2026-10-14
aliases: ["Fable 5 + Karpathy's LLM Wiki is Basically Cheating", Nate Herk LLM wiki video, Nate Herk Fable wiki demo]
tags: [ai-workspace, second-brain, llm-wiki, karpathy, obsidian, ingest]
evidence: "../../raw/sources/clips/fable-5-karpathy-llm-wiki-nate-herk/Fable 5 + Karpathy's LLM Wiki is Basically Cheating.md"
sha256: c396865a8f716c8d1acf5bae9fc8cb1f13e5baaca973f008a270d115fc861bc2
sources: [../../raw/sources/clips/fable-5-karpathy-llm-wiki-nate-herk/PROVENANCE.md]
contradictions: []
---

# Nate Herk's LLM wiki demo: ai-os already compiles, the new idea is tuning ingest rules per wiki

"Fable 5 + Karpathy's LLM Wiki is Basically Cheating" is a YouTube video by Nate Herk ([YouTube](https://www.youtube.com/watch?v=hQvwMj7IJe4)). The channel is inferred from the aiautomationsociety.ai links in the description. The publication date is unknown; the inbox file was last modified 2026-10-14. The full description and auto-caption transcript (captions run to 14:33) were read on 2026-10-14. It is a setup walkthrough: Obsidian vault, Karpathy's idea file as the schema, then two ingests. It follows his [Claude second-brain walkthrough](claude-ultimate-second-brain-nate-herk.md) and [GPT-6 Astra version](gpt-6-astra-ultimate-second-brain-nate-herk.md).

Evidence: [archived clip, provenance and hashes](../../raw/sources/clips/fable-5-karpathy-llm-wiki-nate-herk/PROVENANCE.md). SHA-256 `c396865a8f716c8d1acf5bae9fc8cb1f13e5baaca973f008a270d115fc861bc2`.

## What he says

- **The demo (0:00).** He shows his YouTube videos ingested into an LLM wiki and viewed in Obsidian's graph. Each video page carries a summary, key takeaways, tools and techniques. He follows backlinks from GitHub to Vercel to Claude Code. He says he did not connect the concepts himself; he told Claude Code to fetch the videos and ingest them.
- **A visual layer over the same data (1:22).** One prompt asked Fable to turn the wiki into a beginner-friendly HTML concept map. He says Fable handled the "emotional" brief better than Opus 4.8, and that an earlier Opus 4 version took nearly a day and felt overwhelming. Both run on the same underlying wiki.
- **Several wikis inside one AI OS (2:58).** He keeps a YouTube transcript wiki and a second wiki of all internal and external meeting recordings. He says the meeting wiki informs his community posts, LinkedIn posts and emails. He asked Fable for "a story about the past 6 months" and got a one-shot visual report with subscriber stats, revenue, churn and funnel (3:27 to 4:24). His point: more data helps only if it is routed well (4:46).
- **Where it started (5:09).** Karpathy's post on LLM knowledge bases, with Obsidian as the front end. Setup: install Obsidian, create a vault (he keeps his vaults inside his AI OS project), open it in VS Code and run Claude Code there (5:25 to 6:26). An aside on Fable usage limits follows (6:26); not relevant here.
- **The setup prompt (6:58 to 7:29).** Paste Karpathy's gist, then ask Claude to act as the LLM wiki agent: create the `CLAUDE.md` schema, the index, the log, folder conventions and a first ingest example. He says Fable is overkill for this and Opus is "probably a better call" for routine ingest (7:29).
- **Structure emerges per wiki (7:58 to 9:12).** The YouTube wiki grew folders for comparisons, concepts, sources, techniques and tools. The meetings wiki stayed flat, and "maybe at some point" a sweep will add folders (8:25). He argues flat is sometimes better because the AI can search it easily. Raw holds inputs; one source can become five to ten wiki pages; the index is a table of contents; the log records ingests.
- **Incremental maintenance (9:19 to 9:31).** The log shows batch ingests. The AI needs the index, the log and the backlinks to crawl the wiki.
- **Two ingests (10:04 to 11:57).** A fresh vault started with concepts, entities and sources folders. He dragged a PDF (a Claude Fable 5 and Mythos 5 system card) into raw and pasted a URL (an OpenAI GPT-5.6 preview) into the chat. He reports about 10 to 12 minutes, 20 cross-linked pages, and a flagged comparison problem: the two labs benchmarked against different baselines and harnesses. The wiki added a topics folder; entities included models and labs.
- **Why it works: routing (12:47).** Routing rules tell agents where to look so they do not waste time and tokens. He frames `CLAUDE.md` as the router.
- **Review and tune after batch ingests (13:14 to 13:32).** Check the organization after a batch. If you dislike it, change the ingest rules. Each of his wikis has different structure and rules by data type (meeting transcripts, personal data, proposals). It must make sense to the human too.
- **Portability (14:02).** It is plain Markdown, so a Hermes agent or Codex can use it as well.
- **Close (14:18).** Points to his second-brain levels video.

## Mentions in source

> "if you don't like how things are happening, then update the rules in the way that you ingest" (13:32)

> "every LLM wiki that I've set up, they have different structures and a little bit different rules" (13:32)

> "sometimes keeping this flat is actually better" (8:36)

> "Fable's probably overkill for this" (7:29)

## How it compares with ai-os (interpretation)

Checked on disk 2026-10-14. Decisions are recorded in the [second-brain adoption ledger](../../references/ai-workspace/second-brain-adoptions.md).

| His idea | Here | Verdict |
|---|---|---|
| Raw, wiki, index, log; `CLAUDE.md` as router | [Vault schema](../../system/schema/llm-wiki.md), `wiki/index.md`, `wiki/log.md`, the routing map in `CLAUDE.md` | Already |
| Separate wikis per data type inside the AI OS | One connected vault with domain homes. A nested sub-wiki such as `wiki/karpathy/` (it has its own index, log and rules) is the compatible form | Conflicts |
| Let structure emerge per wiki, flat or foldered | Lint proposes a subfolder or hub once a category grows. Never an automatic move; the schema says "No bulk move or rename is implied" | Adapted |
| Review after batch ingests and tune the rules per wiki | Every ingest report closes with a "schema suggestion" line | Adopted |
| Ingest a URL by pasting a link | URL route: Firecrawl scrape into `raw/inbox/`, then normal intake | Adopted |
| HTML concept maps; "story of the last 6 months" reports | Not built | Later |
| A cheaper model for routine ingest | Model choice is per session | Low priority hint |
| Plain Markdown that any agent can read | Claude and Codex already share the vault | Already |

- **The core loop is not new here.** Ingest, index, log and routing already exist. What this video adds is a habit: after a batch, look at what the ingest produced and adjust the rules. That habit now lands as one line at the end of each ingest report rather than as a separate review step.
- **His meeting wiki maps to a domain home, not a new vault.** Student and consultation transcripts already route through `transcript-intake` into `students/`, which keeps them out of the general wiki pipeline by design.
- **Emergent structure stays advisory.** Letting the model regroup folders on its own would move pages that other pages link to. A lint suggestion keeps Joshua in the decision.

Related: [LLM Wiki pattern](llm-wiki-pattern.md), [second-brain levels](../../references/second-brain-levels.md), [AI workspace hub](../../references/ai-workspace/index.md).

## Limits

- Auto-captions. Likely mis-hearings: "N&amp;N" (probably n8n), "cloud code" (Claude Code), "Tropic" (Anthropic), "Andre Karpathy" (Andrej). His project names are spelled three ways ("Herc brain", "Herk 2", "Herc 2"). "GPT-5.6 soul" is probably the Sol model; the [GD4AI README](gd4ai-obsidian-llm-wiki.md) lists a GPT-5.6 Sol series. "Thor", who tweeted about Fable limits, is unidentified.
- His results (20 pages from two sources, 10 to 12 minutes, the model comparisons) are his claims from his own run. None was reproduced here.
- Fable pricing and usage-limit claims (6:26) were not checked.
- The on-screen prompts, index and wiki pages were not visible in the clip text; only the spoken description was available.

## Queue record

- Done 2026-10-14: AQ-006 Build a one-shot "last six months" visual report from the vault and live systems. Built `research/six-month-story-2026-10-14/index.html` from read-only Calendar, Stripe and LSAT U pulls; Cal.com not pulled. Check: three figures spot-checked against live systems, all matched. Not yet saved as a skill (only if Joshua wants it again).

Declined 2026-10-26: AQ-004. Keep existing models: the saved benchmark does not establish cheaper-model equivalence. No unsupported model switch or new benchmark claim. [Implementation record](../../research/2026-10-26-source-implementation/REPORT.md).
