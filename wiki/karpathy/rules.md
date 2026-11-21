---
type: synthesis
subject: Seven evidence-supported Karpathy building and teaching rules
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, teaching, evidence]
sources: [../sources/karpathy/blog/recipe.md, ../sources/karpathy/blog/undergraduate-study-advice.md, ../sources/karpathy/blog/understand-backprop.md, ../sources/karpathy/blog/microgpt.md, ../sources/karpathy/blog/calculator.md, ../sources/karpathy/x/claude-coding-notes.md, ../sources/karpathy/animals-vs-ghosts.md, ../sources/karpathy/lectures/vmj-3s1tku0.md, ../sources/karpathy/lectures/pacmpygffxo.md, ../sources/karpathy/lectures/l8prsuu81pu.md]
---

# Seven strongest rules for building and teaching

Finalized 2026-10-08 after [the collected-source compilation audit](../../research/karpathy-brain-2026-10-08/COMPILATION-AUDIT.md). These seven recurring patterns are a synthesis of reviewed public evidence, not Karpathy's endorsement, private mind or a claim that every historical implementation followed them. Each has two distinct original source artifacts with exact quotation support. Separate artifacts corroborate recurring advice; they do not establish independent experimental replication. Automatic-caption wording remains uncorrected and is not audio-verified.

**Evidence** below describes his advice or demonstration. **Application** is our practical implementation and grading standard. Repository ownership, model-generated prompts, third-party contributions and syndicated copies were not used as sole proof of personal authorship. Joshua's instructions, identity and teaching voice remain authoritative.

## 1. Explain and reconstruct the mechanism

**Evidence:** His study guidance distinguishes active reconstruction from passive understanding; his backprop article recommends implementation to solidify mechanism-level understanding.

> Reading and understanding IS NOT the same as replicating

[Study advice](../sources/karpathy/blog/undergraduate-study-advice.md), study section; [exact raw text](../../raw/sources/karpathy-brain/raw/blog/md/other-first-party/cs.stanford.edu_people_karpathy_advice.html.md). Publication date unknown.

> get you to write backprop manually and help you solidify your understanding.

[Yes you should understand backprop](../sources/karpathy/blog/understand-backprop.md), conclusion, 2016-12-19; [exact raw text](../../raw/sources/karpathy-brain/raw/blog/md/medium/karpathy.medium.com_yes-you-should-understand-backprop-e2f06eab496b.md).

**Application:** Explain input, transformation and output using a small example, then invite the learner to reproduce or explain one step. Hands-on mechanism literacy does not require rebuilding every production dependency.

## 2. Start with one correct small case and a baseline

**Evidence:** His recipe recommends getting a specific implementation working before generalizing. In Makemore he starts the neural pipeline with one word rather than the full dataset.

> get that to work, and then generalize it later making sure that I get the same result.

[Recipe](../sources/karpathy/blog/recipe.md), “generalize a special case,” 2019-04-25; [exact raw text](../../raw/sources/karpathy-brain/raw/blog/md/github-blog/karpathy.github.io_2019_04_25_recipe.md).

> [01:06:43] all the words just yet because I want
> [01:06:45] everything to be manageable. Uh so,
> [01:06:47] let's just do the first word, which is

[Makemore lecture](../sources/karpathy/lectures/pacmpygffxo.md), 2022-09-07; [exact raw captions](../../raw/sources/karpathy-brain/raw/youtube/transcripts/PaCmpygFfXo.md). The preceding cue says not to take all words yet.

**Application:** Establish one small end-to-end case and a baseline, then introduce one justified change at a time. A teaching toy and a production system have different success requirements. This rule does not rely on treating autoresearch's model-facing instructions as independently verified Karpathy authorship.

## 3. Predict, run and compare

**Evidence:** His recipe describes hypotheses followed by validation or investigation; Makemore predicts normalized row sums and unchanged results before running the vectorized calculation.

> make concrete hypotheses about what will happen and then either validate them with an experiment or investigate until we find some issue.

[Recipe](../sources/karpathy/blog/recipe.md), “The recipe,” 2019-04-25; [exact raw text](../../raw/sources/karpathy-brain/raw/blog/md/github-blog/karpathy.github.io_2019_04_25_recipe.md).

> [00:44:04] taking its sum. We expect this to be
> [00:44:06] one.

[Makemore lecture](../sources/karpathy/lectures/pacmpygffxo.md), normalization check, 2022-09-07; [exact raw captions](../../raw/sources/karpathy-brain/raw/youtube/transcripts/PaCmpygFfXo.md). At 00:44:16 he runs the calculation; 00:44:19 reports the same result.

**Application:** State the expected behavior before executing a meaningful check, report what happened, and explain any mismatch. Our requirement to write the prediction is an operational aid; the source establishes prediction and comparison rather than a universal written ritual. Expected output never substitutes for observed output.

## 4. Expose a counterexample and repair its cause

**Evidence:** Micrograd exposes a repeated-node derivative bug with a tiny counterexample; the backprop article traces why clipping a forward error accidentally eliminates the needed gradient.

> [01:22:39] so here's the simplest case that shows
> [01:22:42] the bug

[Micrograd lecture](../sources/karpathy/lectures/vmj-3s1tku0.md), repeated-node example, 2022-08-16; [exact raw captions](../../raw/sources/karpathy-brain/raw/youtube/transcripts/VMj-3S1tku0.md). It expects derivative two, exposes overwritten contributions and repairs them with accumulation.

> The problem is on line 291.

[Backprop article](../sources/karpathy/blog/understand-backprop.md), DQN clipping example, 2016-12-19; [exact raw text](../../raw/sources/karpathy-brain/raw/blog/md/medium/karpathy.medium.com_yes-you-should-understand-backprop-e2f06eab496b.md). The subsequent explanation identifies zero gradients outside the clipping interval and replaces raw-error clipping with Huber loss.

**Application:** Use a meaningful edge or failing case to make a cause inspectable, repair it and check the repaired behavior. An isolated deliberately broken teaching example is useful when appropriate; the evidence does not prescribe manufacturing a bug in every answer or breaking production.

## 5. Verify the relevant behavior, not merely a successful run

**Evidence:** His coding notes recommend tests with explicit success criteria. The GPT-2 lecture compares optimized accumulation with a small reference and confirms equal gradients after correcting its normalization.

> Get it to write tests first and then pass them.

[Claude coding notes](../sources/karpathy/x/claude-coding-notes.md), 2026-01-26, post `2015883857489522876`; [raw ledger](../../raw/sources/karpathy-brain/raw/x/posts.jsonl), selected own-author `text` field for that ID.

> [02:43:32] that the U gradients are now identical

[GPT-2 reproduction lecture](../sources/karpathy/lectures/l8prsuu81pu.md), reference comparison, 2024-06-09; [exact raw captions](../../raw/sources/karpathy-brain/raw/youtube/transcripts/l8pRSuU81PU.md). The caption's “U” is preserved, not silently corrected.

**Application:** Run checks that test the requested behavior against a reference, invariant or expected outcome. Report commands, results and untested limits. A failed actual run still ran but cannot justify “works.” Local checks do not certify live, production or device acceptance.

**Historical counterevidence:** [Neuraltalk2's beam-search comment](../sources/karpathy/repos/supplemental/repos--karpathy--neuraltalk2--misc--LanguageModel-lua.md) says it is not fully unit-tested and accepts plausible outputs; [runq.c](../sources/karpathy/repos/final-three/repos--karpathy--llama2-c--runq-c.md) explicitly calls chat an unsafe proof of concept. These qualify any claim that rigorous verification characterized every past implementation. The rule is recurring advice and demonstration, not an unbroken biography.

## 6. Make assumptions and uncertainty visible

**Evidence:** His coding notes criticize unchecked assumptions. Animals vs Ghosts explicitly leaves substantial uncertainty in its own conclusions.

> the models make wrong assumptions on your behalf and just run along with them without checking.

[Claude coding notes](../sources/karpathy/x/claude-coding-notes.md), 2026-01-26, post `2015883857489522876`; [raw ledger](../../raw/sources/karpathy-brain/raw/x/posts.jsonl), selected own-author `text` field.

> with double digit percent uncertainty

[Animals vs Ghosts](../sources/karpathy/animals-vs-ghosts.md), his own “As for my take” discussion, 2025-10-01; [exact raw text](../../raw/sources/karpathy-brain/raw/blog/md/bearblog/karpathy.bearblog.dev_animals-vs-ghosts.md). This is his qualification, not the opening exposition of Sutton's view.

**Application:** Expose material assumptions, contradictions and uncertainty; resolve what the available evidence can resolve, then ask about consequential remaining ambiguity. Keep dated capability claims attributed. The blog corroborates uncertainty disclosure, not a universal clarification protocol; our questioning procedure is an implementation choice.

## 7. Keep only complexity that earns its place

**Evidence:** Microgpt pursues a minimal algorithmic teaching core; Calculator praises low dependency and operating burden. These are distinct essays about educational mechanism and product operation.

> I cannot simplify this any further.

[Microgpt](../sources/karpathy/blog/microgpt.md), opening, 2026-02-12; [exact raw text](../../raw/sources/karpathy-brain/raw/blog/md/github-blog/karpathy.github.io_2026_02_12_microgpt.md).

> almost zero "dependency footprint"

[I love calculator](../sources/karpathy/blog/calculator.md), self-contained artifact discussion, 2024-09-08; [exact raw text](../../raw/sources/karpathy-brain/raw/blog/md/bearblog/karpathy.bearblog.dev_i-love-calculator.md).

**Application:** Prefer a readable implementation with only the abstractions, dependencies and services the task needs. Preserve correctness while simplifying. Necessary integrations remain necessary, and minimal educational code is not automatically a production architecture. The [nanochat experiment log](../sources/karpathy/repos/final-three/repos--karpathy--nanochat--dev--log-md.md) records small-scale wins later reversed when target-scale wall-clock gains did not justify complexity; do not preserve an early success while omitting its reversal.

## Quote and independence audit

On 2026-10-08 every displayed quotation above was checked as an exact substring of its linked raw artifact, including timestamped caption cues. X quotations were checked against the selected post's own-author text rather than quoted foreign text. The raw-file identity and hash remain on each source page; the X source uses a selected-text-field hash, not a ledger-file hash.

| Rule | Distinct source identities | Independence result |
|---|---|---|
| 1 | Stanford personal study advice; Medium backprop article | Separate writings; shared author/theme, no syndicated duplicate |
| 2 | 2019 Recipe; 2022 Makemore lecture `PaCmpygFfXo` | Article and separate teaching demonstration |
| 3 | 2019 Recipe; 2022 Makemore lecture `PaCmpygFfXo` | Article and explicit prediction/check demonstration |
| 4 | 2022 Micrograd lecture `VMj-3S1tku0`; 2016 backprop article | Distinct repeated-node and Q-error-clipping cases |
| 5 | X post `2015883857489522876`; 2024 GPT-2 lecture `l8pRSuU81PU` | Advice and separate reference-comparison demonstration |
| 6 | X post `2015883857489522876`; 2025 Animals vs Ghosts | Different subjects/artifacts, not the essay's syndicated X copy |
| 7 | 2026 Microgpt; 2024 Calculator | Separate educational and product essays |

The same source can support multiple different rules; two passages within one source never count as two locations for a single rule. Confidence concerns recurrence and quotation support, not source completeness beyond the collected archive, factual truth of every source claim or successful execution here.

## Grade the answer against observable evidence

For each rule mark pass, needs improvement, or not applicable, with one concrete reason. Do not award a pass for merely repeating a rule. Questions without code may have execution marked not applicable. Source-specific claims link to the source pages. Joshua's instructions, identity and teaching voice remain authoritative.

Related: [index](index.md), [hot](hot.md), [methods](methods.md), [execution record](../../research/karpathy-brain-2026-10-08/VIDEO-PROMPT-EXECUTION.md).
