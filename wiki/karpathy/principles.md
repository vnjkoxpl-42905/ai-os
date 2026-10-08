---
type: synthesis
subject: Karpathy evolving principles across reviewed source domains
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, evidence]
sources:
  - ../sources/karpathy/llm-wiki.md
  - ../sources/karpathy/autoresearch-readme.md
  - ../sources/karpathy/micrograd-readme.md
  - ../sources/karpathy/jobs-readme.md
  - ../sources/karpathy/animals-vs-ghosts.md
  - ../sources/karpathy/blog/understand-backprop.md
  - ../sources/karpathy/lectures/vmj-3s1tku0.md
  - ../sources/karpathy/lectures/q8sa3rm6cki.md
  - ../sources/karpathy/blog/recipe.md
  - ../sources/karpathy/lectures/l8prsuu81pu.md
  - ../sources/karpathy/blog/undergraduate-study-advice.md
  - ../sources/karpathy/lectures/zdusfxrajke.md
  - ../sources/karpathy/lectures/t3yj5hkimq0.md
  - ../sources/karpathy/blog/verifiability.md
  - ../sources/karpathy/lectures/7xtgnnlpymi.md
  - ../sources/karpathy/x/experiment-design-failures.md
  - ../sources/karpathy/x/claude-coding-notes.md
  - ../sources/karpathy/x/voice-context.md
  - ../sources/karpathy/lectures/96jn2ocofls.md
  - ../sources/karpathy/x/teacher-contribution.md
  - ../sources/karpathy/lectures/kwsvtq7dziu.md
  - ../sources/karpathy/blog/bitcoin-from-scratch.md
  - ../sources/karpathy/blog/microgpt.md
  - ../sources/karpathy/blog/vibe-coding-menugen.md
  - ../sources/karpathy/x/objective-and-simplicity.md
  - ../sources/karpathy/x/explicit-local-memory.md
  - ../sources/karpathy/blog/phd-survival-guide.md
  - ../sources/karpathy/blog/power-to-the-people.md
---

# Principles connect mechanisms, evidence and responsibility

These are evolving, attributed observations compiled from the reviewed writings, lectures, interviews, repository documents and captured own-author X texts. They are topic navigation, not a competing seven-rule system or a claim to reproduce private thoughts. [Rules](rules.md) owns the separate Prompt 3 rule selection; [methods](methods.md) turns these observations into concrete procedures. Full-corpus semantic review is still underway, so the coverage map below remains part of this page.

## Maintain knowledge instead of reconstructing it

The gist's proposed knowledge pattern is persistent compilation:

> The knowledge is compiled once and then *kept current*, not re-derived on every query.

[Raw gist](../../raw/sources/karpathy-brain/raw/github/gists/442a6bf555914893e9891c11519de94f/llm-wiki.md), “The core idea”; [source summary](../sources/karpathy/llm-wiki.md).

## Reduce the surface that an experiment changes

autoresearch makes a project-specific case for a bounded mutable surface:

> The agent only touches `train.py`. This keeps the scope manageable and diffs reviewable.

[Raw README](../../raw/sources/karpathy-brain/raw/github/repos/karpathy/autoresearch/README.md), “Design choices”; [source summary](../sources/karpathy/autoresearch-readme.md). The local interpretation is easier attribution of outcomes and clearer review, not a mandate that all projects use one file.

## Keep an educational implementation small

micrograd connects a compact implementation with potential educational use:

> Both are tiny, with about 100 and 50 lines of code respectively.

> Potentially useful for educational purposes.

[Raw README](../../raw/sources/karpathy-brain/raw/github/repos/karpathy/micrograd/README.md), opening; [source summary](../sources/karpathy/micrograd-readme.md). The proposed benefit is inspectability; it is not a reviewed learning-outcome claim.

## Avoid promoting estimates into stronger predictions

jobs qualifies its generated scores:

> The scores are rough LLM estimates (Gemini Flash via OpenRouter), not rigorous predictions.

[Raw README](../../raw/sources/karpathy-brain/raw/github/repos/karpathy/jobs/README.md), “What AI Exposure is NOT”; [source summary](../sources/karpathy/jobs-readme.md).

## Preserve uncertainty and competing research directions

The author explicitly qualifies the Animals vs Ghosts argument:

> And I say both of these with double digit percent uncertainty and cheer the work of those who disagree, especially those a lot more ambitious bitter lesson wise.

[Raw article](../../raw/sources/karpathy-brain/raw/blog/md/bearblog/karpathy.bearblog.dev_animals-vs-ghosts.md), author's discussion; [source summary](../sources/karpathy/animals-vs-ghosts.md).

## Make the mechanism visible before relying on it

The backpropagation article argues that automatic machinery does not remove the need to understand its failure modes. The teaching inference is mechanism literacy for diagnosis, not rebuilding every dependency.

> Backpropagation is a leaky abstraction

[Evidence and raw provenance](../sources/karpathy/blog/understand-backprop.md). The TensorFlow examples are historical. Related demonstrations: [micrograd](../sources/karpathy/lectures/vmj-3s1tku0.md) and [Backprop Ninja](../sources/karpathy/lectures/q8sa3rm6cki.md).

## Begin with a special case that can be checked

The training recipe recommends moving from a specific implementation toward a general one. Minimal cases keep the moving parts inspectable.

> generalize a special case

[Evidence and raw provenance](../sources/karpathy/blog/recipe.md). This is a neural-training method with dated optimizer advice, not a universal prescription for every project. [GPT-2 reproduction](../sources/karpathy/lectures/l8prsuu81pu.md) provides the small-batch debugging example.

## Understanding should survive reconstruction

His study advice distinguishes recognizing an explanation from reproducing it. This supports asking a learner to reconstruct a mechanism or solve a new example.

> Reading and understanding IS NOT the same as replicating

[Evidence and raw provenance](../sources/karpathy/blog/undergraduate-study-advice.md). University-exam habits and personal health advice do not become Joshua teaching policy. The [Tokenizer lecture](../sources/karpathy/lectures/zdusfxrajke.md) offers a concrete implementation exercise.

## A running program is weaker evidence than the intended result

The GPT-2 lecture checks an incorrect accumulation implementation against a batched calculation, then shows matching gradients after fixing the normalizer. Equality to the intended reference is the informative result.

> [02:43:32] that the U gradients are now identical

[Evidence and raw provenance](../sources/karpathy/lectures/l8prsuu81pu.md). The code was demonstrated in the source, not executed by this compilation. [WaveNet](../sources/karpathy/lectures/t3yj5hkimq0.md) separately demonstrates a broadcasting bug that runs.

## Check whether the objective can really be verified

Verifiability argues that repeatable, checkable outcomes shape which tasks can improve through optimization. The inferred design principle is to inspect the feedback function before relying on more trials.

> Software 2.0 easily automates what you can verify.

[Evidence and raw provenance](../sources/karpathy/blog/verifiability.md). This is an argument about optimization opportunity. The [Deep Dive](../sources/karpathy/lectures/7xtgnnlpymi.md) qualifies learned reward scorers with gaming examples.

## Compare improvements against a fair baseline

His captured agent-experiment account identifies missing baselines and ablations. The supported conclusion is that an improved score alone does not establish a new research contribution.

> they don't create strong baselines and ablate things properly

[Evidence and raw provenance](../sources/karpathy/x/experiment-design-failures.md). Post 2027521323275325622, 2026-02-27. Captured text is reviewed; upstream archive completeness and linked results are not certified.

## Keep assumptions and missing intent explicit

His coding notes identify silent assumptions as a recurring agent failure. Clear input and observable success criteria help make delegation reviewable.

> The most common category is that the models make wrong assumptions on your behalf and just run along with them without checking.

[Evidence and raw provenance](../sources/karpathy/x/claude-coding-notes.md). Post 2015883857489522876, 2026-01-26. His [voice-context note](../sources/karpathy/x/voice-context.md) supplies a complementary personal practice, not proof dictation always works.

## Accountability remains with the person using the tool

His lecture explicitly assigns responsibility for checking and owning the final product to the user. Fluency and apparently strong reasoning do not remove that duty.

> [03:30:58] check their work and own the product of

[Evidence and raw provenance](../sources/karpathy/lectures/7xtgnnlpymi.md). Read this with the next raw line, 03:31:00, which completes “your work.” [Sequoia](../sources/karpathy/lectures/96jn2ocofls.md) also distinguishes professional quality from a quick prototype.

## Teacher input can organize what an assistant cannot originate

A captured reply describes a teacher contribution as a small unique input that an AI may understand when supplied. This is a hypothesis about course construction and teacher judgment, not an established learning-outcome result.

> Teacher input is the unique sliver of contribution

[Evidence and raw provenance](../sources/karpathy/x/teacher-contribution.md). Post 2030387285250994192, 2026-03-07; surrounding reply context is incomplete. [No Priors](../sources/karpathy/lectures/kwsvtq7dziu.md) discusses the related simplification and curriculum limits.

## Educational minimality is separate from production readiness

His Bitcoin exercise explicitly excludes production use. Teaching implementations can reveal mechanisms while leaving security, compatibility, scale and operational checks to other work.

> Please don’t use this anywhere close to anything that touches production.

[Evidence and raw provenance](../sources/karpathy/blog/bitcoin-from-scratch.md). This is a 2021 test-network tutorial. [microgpt](../sources/karpathy/blog/microgpt.md) and [MenuGen](../sources/karpathy/blog/vibe-coding-menugen.md) add educational and real deployment contrasts.

## Simplify while watching cost as well as quality

His captured experiment-objective reply includes simplicity alongside loss, runtime and memory concerns. This supports treating a small score gain and added operating burden as a tradeoff.

> keep a sense of simplicity/aesthetics

[Evidence and raw provenance](../sources/karpathy/x/objective-and-simplicity.md). Post 2029957088022254014, 2026-03-06. Fixed-time autoresearch and loss-plus-time policies are distinct experiment designs, not one universal formula.

## Keep knowledge owned and navigable

His captured local-memory discussion states ownership directly. Combined with the retained LLM Wiki evidence above, this motivates inspectable files and maintained links rather than inaccessible personalization.

> The data is yours.

[Evidence and raw provenance](../sources/karpathy/x/explicit-local-memory.md). Post 2040572272944324650, 2026-04-04. This does not authorize changing Joshua cloud, backup or secret-storage decisions.

## Communicate one supported contribution

The PhD guide asks a paper to identify a single new contribution. The practical communication inference is a concrete central point with controlled evidence, rather than collecting unrelated improvements into a persuasive story.

> The paper sells a single thing that was not obvious or present before

[Evidence and raw provenance](../sources/karpathy/blog/phd-survival-guide.md). This is personal academic guidance from 2016, not an immutable writing rule for all formats.

## Broader assistance still has reliability limits

His societal argument describes broad model assistance as fallible. The useful reading is expanded individual reach with verification, not replacement of expertise by unchecked output.

> versatile but also shallow and fallible

[Evidence and raw provenance](../sources/karpathy/blog/power-to-the-people.md). The essay is dated 2025-04-07; its capability, cost and organizational forecasts are source claims rather than current measurements.

## Coverage and attribution map

This synthesis uses conclusions from the reviewed source pages, not all collected bytes as personal beliefs. Consult the live ledgers for evolving counts and exact unread paths:

- [Writings](../../research/karpathy-brain-2026-10-08/blog-synthesis.md): preserved blog text, historical course revisions, personal guides and fiction, with authorship qualifications.
- [Lectures and interviews](../../research/karpathy-brain-2026-10-08/lecture-synthesis.md): all 17 preserved texts fully read; 14 spoken-source texts and three music/animation caption files. Audio, diagrams and missing speech are unverified.
- [Repository and X evidence](../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md): reviewed named files and all selected captured own-author X bodies; remaining repository files and upstream X completeness are separate limits.
- [llm.c](../../research/karpathy-brain-2026-10-08/llmc-synthesis.md): reviewed reference implementations, memory/compute choices and checker limitations. Repository ownership does not establish individual contributor authorship.
- [Payloads](../../research/karpathy-brain-2026-10-08/github-payload-synthesis.md): generated dependencies, training text, parameters and government HTML have integrity/structure records; mechanical processing does not turn them into Karpathy beliefs or full model semantic reads.

CS231n course/team texts, guest tutorials, third-party libraries, BLS pages, generated prompts and fictional narration are not attributed as personal doctrine. Historical provider rankings and prices remain dated. A quotation establishes what the preserved source says, not factual truth, successful local execution or a present capability. Related papers and linked media need independent review. Joshua's voice, policies and canonical routes remain authoritative.

Return to [index](index.md), [principles](principles.md), [methods](methods.md), [rules](rules.md) or [hot page](hot.md).
