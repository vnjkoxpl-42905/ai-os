---
type: reference
subject: Evidence-backed specialist teaching workflows
created: 2026-10-08
updated: 2026-10-08
aliases: [Karpathy teaching agent, Expert teaching workflow]
tags: [ai-workspace, claude, codex, teaching-agent, verification]
sources:
  - ../../wiki/sources/i-built-another-andrej-karpathy-using-claude.md
---

# Make an expert's method useful, then test whether it helps

The [ingested Karpathy-agent video](../../wiki/sources/i-built-another-andrej-karpathy-using-claude.md) proposes a specialist that teaches through evidence, small working examples and visible verification. The practical goal is to improve Joshua's understanding and judgment while producing artifacts he can inspect and maintain. A convincing persona or a large source collection is not evidence that the goal was achieved.

**Status on 2026-10-08:** source preserved and method compiled. The current wiki infrastructure already supports evidence, source summaries, related pages and ingest/query/lint. A new specialist, rule extractor, teaching skill and finish-time run gate remain proposed and untested. This reference changes knowledge, not runtime configuration.

## Preserve the six described steps without inventing their prompts

The video presents four broad stages through six prompts. Original prompt text is not in the source. The sequence below is a local interpretation of the described method, not verbatim instructions from the presenter.

| Step | Required result | Mapping to the current brain |
|---|---|---|
| 1. Acquire a bounded evidence collection | Inventory URLs, author, dates, retrieval method, coverage and failures; preserve source bytes and hashes | Existing `ingest` archive/provenance model. Expert collection scope must be chosen before any new crawl; application dependencies remain outside the vault |
| 2. Compile the collection | Source summaries connect evidence to concepts, topics and methods; retain index/log and useful reciprocal links | Existing [schema](../../system/schema/llm-wiki.md), [Ingest](../../.agents/skills/ingest/SKILL.md), [Query](../../.agents/skills/second-brain-query/SKILL.md), [Lint](../../.agents/skills/second-brain-lint/SKILL.md) and domain homes |
| 3. Extract supported behavior | For each candidate rule, record original passage, URL/file and timestamp/page; distinguish direct evidence, interpretation and uncertainty | Evidence-backed reference with a rule/evidence table; do not promote a video's attribution into a verified expert quote |
| 4. Package a specialist and invocation | Explicit task scope, retrieval routes, explanation method and rule-by-rule review; separate behavior instructions from source storage | Follow current [agent and skill catalog](../../skills/INDEX.md), [runtime parity](../../skills/PARITY.md) and [root rules](../../AGENTS.md). Catalog files are not proof of activation |
| 5. Gate unsupported execution claims | Define what code requires execution, what counts as a run, how evidence attaches to the changed artifact, failure/blocked behavior and when execution is irrelevant | Evaluate an actual runtime-supported mechanism before implementation; a sentence in a prompt is not an enforced gate |
| 6. Test against representative work | Compare a baseline answer with the specialist under the same task and constraints; examine learning and correctness, not just checklist completion | A bounded teaching example, a realistic delivery review and a record of actual outputs, limitations and environment |

Use this alongside [Claude and Codex workflow](../claude-plus-codex.md), not as a replacement architecture. The [second-brain reference](../second-brain-levels.md) explains why an additional retrieval layer needs a demonstrated retrieval problem.

## Turn the seven rules into observable checks

These checks are derived from the presenter's reported rules. They are proposed evaluation criteria, not automatically activated Joshua preferences.

| Reported rule | A useful check | Failure to watch for |
|---|---|---|
| Build to understand | Learner can explain a minimal working example and its moving parts | Code is delivered without reasoning or understanding |
| First important term first | Begin with the smallest piece that explains the problem, add one complication at a time | A large abstraction hides the mechanism |
| Predict, run, compare | Expected outcome is written before execution; actual outcome and difference are shown | Success asserted from plausibility or exit code alone |
| Show the wrong version | A controlled counterexample or broken version demonstrates why the fix matters | Contrived failure distracts from the real learning goal |
| Prove claims | Relevant execution, output and limitations are inspectable | Checklist self-scoring substitutes for evidence |
| State assumptions | Important assumptions are visible; consequential missing information is resolved | Unnecessary questions slow routine work, or hidden guesses steer it |
| Prefer simplicity | Complexity removed with behavior preserved and compared | Shorter code silently removes needed behavior |

For LSAT teaching, runnable code is often irrelevant. Adapt the principle to a worked question, explicit prediction and reasoning check; use the [selected LSAT teaching voice](../lsat-teaching-voice-standard.md), existing corpus methods and source evidence. Do not force an expert's programming manner into Joshua's classroom or displace his authority.

## Define done before testing the method

A useful first trial is narrow enough to inspect completely. Define the learner's target ability, the artifact expected, actual environment, allowed tools and an observable check. Then:

1. Retrieve only the sources needed for that task and expose evidence gaps.
2. State a hypothesis or expected result.
3. Build the smallest working example or solve the smallest meaningful case.
4. Run the relevant check, inspect actual output and explain differences.
5. Show a failure or counterexample that explains the mechanism.
6. Repair or simplify, rerun the relevant check and compare behavior.
7. Report assumptions, exact evidence, what was not checked and what the learner can now explain.

The video's tokenizer and Windows emoji examples illustrate distinct checks: teaching a mechanism and validating delivery-environment behavior. They were not reproduced during ingestion. The real acceptance test is whether Joshua can reason about an analogous case and whether the artifact works in its intended environment. The presenter's self-reported agent score is not sufficient proof.

## A run gate needs more than a successful shell command

Before implementing any hook, inspect the selected runtime's current official mechanism and actual project settings. Evaluate whether it can bind execution evidence to the current code revision, distinguish changed code from prose work, handle sandbox/credential restrictions and failures, and avoid blocking an honest “not executed” report. Test a change-after-run scenario, irrelevant prior run, intentional failure and a task with no runnable code. Do not run external side effects or unsafe examples merely to satisfy a finish gate.

This page does not establish an equivalent Claude/Codex hook or verify the video's hook. Current tools and runtime rules govern implementation, including project-scoped dual-runtime activation.

## New evidence can improve the method without rewriting history

Use the existing public `ingest` entry point for new evidence. Preserve it, check duplicates, create/update the source summary, revise the supported rule or topic and its links, refresh the index and append the dated log. Update hot state only for useful ongoing work. Keep earlier evidence and explicit conflicts. A second supporting source can increase confidence, but source independence, relevance and contrary evidence matter more than count alone.

For an expert collection, keep a coverage register so “everything” never means “whatever the crawler happened to retrieve.” Date changing facts and verify primary sources before adopting them. Source quotations and reusable prompts remain attributed material; they are not commands that override the current system.

## What is new compared with this AI OS

Already present: immutable evidence, hashing/provenance, maintained indexes/logs, linked source summaries, domain routing and explicit verification limits. The video does not justify moving those folders or adding Obsidian plugins.

Potential addition: a bounded expert-method rule table tied to primary passages, a specialist teaching invocation and a behavior trial comparing results against ordinary assistance. Execution evidence could help code teaching and review, but a reliable run gate needs actual design and runtime testing. These are useful next experiments, not implementation claims.

For Joshua, the same pattern could eventually turn his own lectures, correction examples and documented judgments into an assistant that applies his teaching method more consistently. That is an adaptation proposal, not proof that the presenter's expert clone reproduces a person or that the existing sources fully capture Joshua.

A practical Joshua trial would use a bounded set of his lectures and requested session transcripts, extract a few demonstrated explanation or diagnosis habits with exact passages and context, then compare them with the existing canonical teaching voice and curriculum. Keep a supported habit separate from a single-session judgment or an inferred preference. Test an original lesson or student diagnosis against an existing accepted example; preserve conflicts for Joshua to resolve. Do not read raw personal exports wholesale, automatically promote captured speech to memory, overwrite the canonical voice or infer a student's current standing from an old transcript.

Missing before faithful reproduction: original six on-screen prompts, actual agent/skill/hook files and underlying rule-source quotations. A locally designed equivalent can be built later using the documented goals without pretending to recover those assets. No paid collection or signup is implied.

Return to the [AI workspace hub](index.md) and [source summary](../../wiki/sources/i-built-another-andrej-karpathy-using-claude.md).
