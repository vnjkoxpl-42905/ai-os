---
type: source
subject: Source-grounded expert teaching agents
created: 2026-10-08
updated: 2026-10-08
aliases: [I Built Another Andrej Karpathy Using Claude]
tags: [ai-workspace, claude, teaching-agent, llm-wiki]
sources:
  - ../../raw/sources/clips/i-built-another-andrej-karpathy-using-claude/I Built Another Andrej Karpathy Using Claude.md
---

# Turn an expert's sources into a tested teaching method

Joshua requested complete ingestion of **I Built Another Andrej Karpathy Using Claude** on 2026-10-08. The entire supplied description and timestamped transcript, 0:00 to 10:43, was read. This summary records what the presenter claims and distinguishes those claims from verified behavior in Joshua's workspace.

## Source identity and preserved evidence

- Original video: [I Built Another Andrej Karpathy Using Claude](https://www.youtube.com/watch?v=bvGptCLDhyo).
- Creator: Nate Herk, inferred from self-linked social accounts and promotion in the clip; original channel metadata not independently retrieved.
- Publication and exact capture dates: unknown. Relative dates such as “May of this year” remain relative claims.
- Ingested: 2026-10-08.
- Evidence: [unchanged local clip](<../../raw/sources/clips/i-built-another-andrej-karpathy-using-claude/I Built Another Andrej Karpathy Using Claude.md>), [provenance](../../raw/sources/clips/i-built-another-andrej-karpathy-using-claude/PROVENANCE.md), [hash manifest](../../raw/sources/clips/i-built-another-andrej-karpathy-using-claude/SHA256SUMS).
- SHA-256: `3c453f7be66ee3cf67cc63c4439c8bf477726c213a1aaa763f35e271e39a2d8c`; size: 17,093 bytes.
- Inbox original retained. Preserved archive matches its bytes.

## The source's goal is demonstrated understanding

At 0:44–2:14, the presenter distinguishes this from a voice imitation: the intended agent uses an expert's explaining, building and checking habits to help a learner understand work rather than accept convincing code. He proposes collecting expertise, compiling it into usable knowledge and wiring it into skills and agents. At 10:21 he attributes an understanding-versus-outsourcing maxim to Karpathy; that original quotation was not independently checked here.

The promised benefit is an explanation tied to executable examples, assumptions and observable results. Building a persona does not prove expert equivalence, prevent hallucination or reproduce a person's full mind.

## Four broad stages contain six described prompts

The narration advertises four steps, then explicitly says there are six prompts at 2:42. These are different levels of description, not six recovered verbatim instructions. The full prompt text appears on screen according to the presenter; it is absent from the supplied Markdown.

| Prompt described | Source segment | What the presenter says to do | Expected artifact |
|---|---|---|---|
| 1. Acquire evidence | 2:42–3:42 | Gather blogs, lecture transcripts, GitHub repositories and X posts; select a tool per source, run source-specific agents in parallel and record what was obtained | Raw evidence folders by source plus an acquisition inventory |
| 2. Compile knowledge | 3:42–5:37 | Supply the LLM Wiki gist, leave raw files untouched, compile linked source/topic/principle/method pages, maintain index and log | Navigable wiki with evidence and reciprocal links |
| 3. Derive behavior | 5:41–6:42 | Extract operating rules; anchor each in an exact quote and its source; label inference when direct support is missing | Evidence-backed rules with source/timestamp links |
| 4. Package retrieval and teaching | 6:42–7:38 | Make a specialist subagent and a teaching skill; include communication style, task loop and a checklist with one line per rule | Agent definition and skill entry point |
| 5. Require execution evidence | 7:38–8:09 | Add a finish-time hook that blocks completion when newly written code has not been run | A proposed run gate and its executable enforcement |
| 6. Test real behavior | 8:09–9:26 | Exercise construction/teaching and delivery review; define done, predict results, run, show failures, fix and compare | Test cases and an execution/review receipt |

The four broad stages are acquisition, compiled knowledge plus grounded behavior, executable verification, and testing on real work. A maintenance ingest loop follows at 9:26–10:21.

## The seven reported rules require their own evidence

At 5:53–6:42, the presenter reports these seven rules:

1. **Build to demonstrate understanding:** use a working construction instead of a purely verbal explanation.
2. **Start with the main term:** make the smallest important piece work, then add one complication at a time.
3. **Predict, run, compare:** state expected behavior before execution and compare it with the observed result, including silent quality failures.
4. **Show a broken version:** use a deliberate or retained bug to explain what failed and why.
5. **Prove claims:** provide observable evidence instead of merely declaring success.
6. **State assumptions:** expose important guesses and resolve consequential ambiguity.
7. **Prefer simplicity:** retain complexity only when it earns its place.

These are the video's synthesis of Karpathy's material, not seven independently authenticated quotations from Karpathy. The underlying quotes and citations are not supplied. No rule became Joshua's personal preference or active runtime instruction during this ingestion.

## Acquisition details are claims about the demonstration

At 2:42–3:42, the presenter names `youtube-transcript-api` and `yt-dlp` for YouTube captions and `twitterapi.io` for X. He reports posts since 2023, roughly $1 in X API cost, a 45–60 minute acquisition run and more than 700,000 words. Those are demo-specific claims, not a verified current price, reproducible completeness guarantee or local acquisition result. No expert corpus was downloaded here, and no paid source was used.

The wiki reportedly contains a source page per contribution, topics, principles, methods, explanation and debugging behavior. Rules cite sources and source pages point back to rules (4:43–5:37). Obsidian is described as the visual interface, not a necessary execution component. Compare the existing [LLM Wiki source](llm-wiki-pattern.md) and [current schema](../../system/schema/llm-wiki.md).

**Primary-method check, 2026-10-08:** the [Karpathy LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), created 2026-04-04, was checked during this ingestion. It supports the underlying immutable-source, persistent synthesis, schema, ingest/query/lint and index/log method. This is separate supporting evidence for the wiki mechanism; it does not authenticate the video's seven rules, employment claims or finish hook.

## The demonstrations test different failure modes

**Tokenizer construction, 8:09–8:38:** the agent reportedly defines done, builds a minimal byte-pair tokenizer on a tiny input, predicts output, executes, inspects output, demonstrates a break, repairs it and lists what ran, what changed and the relevant rules. This is a sequence described in the transcript, not code executed or independently inspected here.

**Client-delivery review, 8:38–9:26:** a YouTube-comment script reportedly passed the initial Claude test but failed on emoji in a normal Windows terminal before creating files. The specialist predicts and reproduces that environment-specific failure, trims unnecessary code and runs old and revised versions side by side to compare behavior. The useful lesson is to test the delivery environment and preserve required outcomes when simplifying. A test in one terminal does not prove all deployment settings work.

The finish hook is described at 7:41 as enforcement. Its code, tracked execution state, false-positive behavior, permission handling and bypass resistance are not in the clip. Therefore ingestion cannot certify that it enforces what the presenter promises.

## Maintenance updates behavior through new evidence

At 9:26–9:55, the presenter describes supplying a new link to an ingest skill: check the raw collection, create a source page, update affected pages and rules, then refresh index, hot cache and log. A new source reportedly adds clarification behavior to rule six. Another tentative rule gains a second supporting source and is promoted. The two-source threshold is his demonstration's choice, not a universal validation standard or current AI OS policy.

## What changes here, and what does not

The [expert teaching workflow](../../references/ai-workspace/expert-teaching-workflow.md) preserves all substantive steps, proposes a local mapping and separates the existing wiki infrastructure from an unimplemented specialist agent/run gate. The [AI workspace hub](../../references/ai-workspace/index.md) routes this outside generic LSAT curriculum.

No hooks, skills, agents, expert collection, project runtime rules or personal voice standards were installed or altered. No new folder architecture was adopted. Joshua's [selected LSAT teaching voice](../../references/lsat-teaching-voice-standard.md) remains authoritative for LSAT adaptations.

## Evidence gaps that remain explicit

- Original six prompt texts, on-screen files and source-to-rule quotation table are unavailable in the clip. The table above summarizes their described purposes; it is not a transcription of those prompts.
- The video description's promotional AI OS template opt-in link was not accessible through the browser retrieval tool during this ingest. No linked package was inspected or signup performed.
- The clip says its description links the LLM Wiki gist, but the supplied description contains no such URL. The separately checked canonical gist must be treated as additional evidence, not an embedded link recovered from this clip.
- The opening claims about Karpathy's Anthropic employment and OpenAI founding role need primary verification before repetition as biography. Relative timing, original social posts and the claimed quotation need their own originals.
- Video frames were not inspected: the local watch tool lacks `yt-dlp`, `ffmpeg` and `ffprobe`. No installation, paid transcription or account signup was performed.
- Code examples, expert corpus, run hook and quality improvements were not locally reproduced. This is complete coverage of the supplied text, not complete visual/video or implementation verification.
