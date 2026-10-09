---
type: synthesis
subject: Karpathy evolving methods across reviewed source domains
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, methods]
sources:
  - ../sources/karpathy/llm-wiki.md
  - ../sources/karpathy/autoresearch-readme.md
  - ../sources/karpathy/micrograd-readme.md
  - ../sources/karpathy/jobs-readme.md
  - ../sources/karpathy/blog/recipe.md
  - ../sources/karpathy/lectures/l8prsuu81pu.md
  - ../sources/karpathy/lectures/pacmpygffxo.md
  - ../sources/karpathy/blog/undergraduate-study-advice.md
  - ../sources/karpathy/blog/microgpt.md
  - ../sources/karpathy/lectures/vmj-3s1tku0.md
  - ../sources/karpathy/lectures/zdusfxrajke.md
  - ../sources/karpathy/repos/autoresearch-program.md
  - ../sources/karpathy/x/experiment-design-failures.md
  - ../sources/karpathy/lectures/t3yj5hkimq0.md
  - ../sources/karpathy/x/claude-coding-notes.md
  - ../sources/karpathy/x/voice-context.md
  - ../sources/karpathy/lectures/7xtgnnlpymi.md
  - ../sources/karpathy/lectures/ewvnqjaaohw.md
  - ../sources/karpathy/lectures/96jn2ocofls.md
  - ../sources/karpathy/blog/vibe-coding-menugen.md
  - ../sources/karpathy/blog/append-and-review.md
---

# Methods make a small result inspectable, testable and reusable

This evolving synthesis joins the reviewed domains into concrete building, teaching, research and knowledge-maintenance methods. Each attributed pattern has preserved quotation support. Suggested local steps are adaptations, not quotations or evidence that they ran here. [Rules](rules.md) owns Prompt 3 selection; [execution status](../../research/karpathy-brain-2026-10-08/VIDEO-PROMPT-EXECUTION.md) owns what was installed and tested. All saved repository files are accounted for in the [compilation audit](../../research/karpathy-brain-2026-10-08/COMPILATION-AUDIT.md). Machine payload processing, missing media and uncollected upstream material have separate limits.

## Compile a source and preserve its evidence

The LLM Wiki gist states:

> These are immutable — the LLM reads from them but never modifies them.

[Raw gist](../../raw/sources/karpathy-brain/raw/github/gists/442a6bf555914893e9891c11519de94f/llm-wiki.md), “Architecture”; [source summary](../sources/karpathy/llm-wiki.md). Here, the existing schema implements that ownership boundary; the gist does not replace it.

## Evaluate and retain or discard each experiment

autoresearch's introduction describes a repeated run-and-evaluate loop:

> It modifies the code, trains for 5 minutes, checks if the result improved, keeps or discards, and repeats.

[Raw README](../../raw/sources/karpathy-brain/raw/github/repos/karpathy/autoresearch/README.md), introduction; [source summary](../sources/karpathy/autoresearch-readme.md). A candidate adaptation is to define edit scope, run budget, metric and retention criteria before an experiment. This workspace has not installed or run that loop.

## Compare calculated values with a reference

micrograd describes its correctness check:

> To run the unit tests you will have to install [PyTorch](https://pytorch.org/), which the tests use as a reference for verifying the correctness of the calculated gradients.

[Raw README](../../raw/sources/karpathy-brain/raw/github/repos/karpathy/micrograd/README.md), “Running tests”; [source summary](../sources/karpathy/micrograd-readme.md). This supports a reference-comparison method in this project, not a claim that its current tests passed here.



Historical counterevidence matters. The preserved neuraltalk2 beam-search comment explicitly acknowledges incomplete certainty and accepts plausible output plus apparent performance:

> it seems to work, doesn't crash, gives expected looking outputs, and seems to
> improve performance, so I am declaring this correct.

[Raw LanguageModel.lua](../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk2/misc/LanguageModel.lua), `sample_beam` introduction; [source page](../sources/karpathy/repos/supplemental/repos--karpathy--neuraltalk2--misc--LanguageModel-lua.md). The preceding line says, “Not 100% sure it's correct, and hard to fully unit test to satisfaction, but”. This is historical repository evidence, not a universal biographical claim. The seven rules are an evidence-supported operational synthesis of recurring advice and demonstrations; they do not assert that every past implementation followed rigorous verification. REINFORCEjs separately labels unfinished policy-gradient implementations “buggy implementation, doesnt work...” and excludes their exports. [Source page](../sources/karpathy/repos/supplemental/repos--karpathy--reinforcejs--lib--rl-js.md).

## Distinguish preserved input from derived judgments

jobs labels its HTML evidence:

> Raw HTML pages from BLS (source of truth, ~40MB)

It qualifies the generated scoring layer:

> The scores are rough LLM estimates (Gemini Flash via OpenRouter), not rigorous predictions.

[Raw README](../../raw/sources/karpathy-brain/raw/github/repos/karpathy/jobs/README.md), “Key files” and “What AI Exposure is NOT”; [source summary](../sources/karpathy/jobs-readme.md). The local adaptation is to trace each judgment to its inputs and retain the limits of its method. BLS payload files were machine-processed, not semantically reviewed as Karpathy's personal statements; see the [compilation audit](../../research/karpathy-brain-2026-10-08/COMPILATION-AUDIT.md).

## Build the smallest end-to-end case first

The recipe names special-case generalization as a technique. Suggested local sequence: define one input and expected output, make that path work, inspect the data and loss, then introduce one change and check it.

> generalize a special case

[Evidence and raw provenance](../sources/karpathy/blog/recipe.md). Use the [GPT-2 source](../sources/karpathy/lectures/l8prsuu81pu.md) for the single-batch/device examples and [Makemore](../sources/karpathy/lectures/pacmpygffxo.md) for the count-model baseline. These are adaptations, not claims those runs occurred here.

## Teach a tiny mechanism, then require an independent attempt

The study advice distinguishes replication from passive understanding. Suggested sequence: explain one toy transformation, predict an output, let the learner attempt it, compare, and only then generalize.

> Reading and understanding IS NOT the same as replicating

[Evidence and raw provenance](../sources/karpathy/blog/undergraduate-study-advice.md). [microgpt](../sources/karpathy/blog/microgpt.md), [micrograd](../sources/karpathy/lectures/vmj-3s1tku0.md), and [Tokenizer](../sources/karpathy/lectures/zdusfxrajke.md) provide teaching mechanisms. Preserve Joshua domain-specific pedagogy.

## Verify an optimization against the simple reference

The GPT-2 lecture fixes gradient accumulation and verifies equality with its batched reference. Suggested local sequence: retain the simple calculation, compare outputs or gradients, check boundary cases, then measure speed separately.

> [02:43:32] that the U gradients are now identical

[Evidence and raw provenance](../sources/karpathy/lectures/l8prsuu81pu.md). The same lecture reports unresolved compiler and data-order issues. Its later C-versus-PyTorch check is source evidence, not a local benchmark.

## Define a protected baseline before autonomous experiments

The autoresearch instructions require a baseline first. Suggested design: state the editable surface, protected evaluator, metric, compute budget, acceptance policy and crash reporting before allowing repeated experiments.

> Your very first run should always be to establish the baseline

[Evidence and raw provenance](../sources/karpathy/repos/autoresearch-program.md). Repository ownership does not prove individual authorship of every line. This does not start an indefinite training run or spend compute.

## Inspect the measurement before accepting the result

His experiment account criticizes missing baselines and ablations. Suggested review: compare the same task and evaluator, record compute/runtime changes, examine contamination and distribution shifts, and distinguish observed gain from its proposed cause.

> they don't create strong baselines and ablate things properly

[Evidence and raw provenance](../sources/karpathy/x/experiment-design-failures.md). [GPT-2 reproduction](../sources/karpathy/lectures/l8prsuu81pu.md) explicitly retains dataset and evaluation caveats; [WaveNet](../sources/karpathy/lectures/t3yj5hkimq0.md) compares matched parameter counts. No source evaluation was rerun here.

## Supply missing intent before requesting a large patch

His coding notes warn about unchecked assumptions. Suggested local sequence: provide relevant files and constraints, ask for the intended result and unresolved assumptions, define visible success, then work in increments whose changes can be reviewed.

> The most common category is that the models make wrong assumptions on your behalf and just run along with them without checking.

[Evidence and raw provenance](../sources/karpathy/x/claude-coding-notes.md). This is a dated experiential account, not proof of every model failure rate.

## Use voice to capture context, then inspect the interpretation

His voice-context post describes a personal way to convey more intent. Suggested local sequence: dictate the goals and constraints, have the assistant restate them cleanly, correct the restatement, then use it as a brief.

> Sometimes the LLM needs more bits

[Evidence and raw provenance](../sources/karpathy/x/voice-context.md). Post 2079610838143623371, 2026-07-21. This is a context practice, not a mandate to install a transcription product or assume dictated names are correct.

## Use tools for exact results and check their inputs

The Deep Dive advises code for arithmetic rather than trusting mental calculation. Suggested local sequence: pass the actual values, inspect the program, run it, examine assumptions and output, and preserve the result with its input.

> [01:56:02] and I would say use code and uh that's

[Evidence and raw provenance](../sources/karpathy/lectures/7xtgnnlpymi.md). [How I Use LLMs](../sources/karpathy/lectures/ewvnqjaaohw.md) adds silent imputation and misleading numerical-output examples. A tool result is only as relevant as its inputs and assumptions.

## Separate a prototype from a production acceptance walk

The Sequoia interview names responsibility even when going faster. Suggested review of a real app: test identity mapping, payment/account association, persistence, refresh/retry behavior and production configuration as separate paths.

> [00:16:16] Um, you are, um, you're still responsible for your software just as before, but can you go faster? And spoiler is you can, but how do you, how do you do that properly?

[Evidence and raw provenance](../sources/karpathy/lectures/96jn2ocofls.md). [MenuGen](../sources/karpathy/blog/vibe-coding-menugen.md) contains the payment-identity and durability examples. Interview text is not independently audio-verified; the edited blog mirror is not an independent replication.

## Capture cheaply, then deliberately revisit

His personal note article favors a single text note. The transferable local procedure is low-friction capture followed by review, rescue, merging and reconsideration, while keeping this vault's existing domain homes.

> One text note ftw.

[Evidence and raw provenance](../sources/karpathy/blog/append-and-review.md). His Apple Notes preference differs from this organized vault. It does not authorize flattening immutable raw evidence or student folders.

## Ingest a source into existing knowledge

The gist's suggested intake reads and integrates a source rather than stopping at indexing. Local route: preserve raw, read it, update its source page and relevant topics, update the index, and append the log under the existing schema.

> the LLM reads the source, discusses key takeaways with you, writes a summary page in the wiki, updates the index

[Preserved gist](../../raw/sources/karpathy-brain/raw/github/gists/442a6bf555914893e9891c11519de94f/llm-wiki.md), Operations; [source page](../sources/karpathy/llm-wiki.md). The gist is modular; [the current schema](../../system/schema/llm-wiki.md) owns this workspace's implementation.

## Answer through the index and keep valuable results

The gist distinguishes retrieval from accumulation: answer with citations, then file a useful comparison or connection into maintained knowledge. Local route: index, relevant pages, raw evidence when needed, qualified answer, durable update.

> good answers can be filed back into the wiki as new pages.

[Preserved gist](../../raw/sources/karpathy-brain/raw/github/gists/442a6bf555914893e9891c11519de94f/llm-wiki.md), Operations; [source page](../sources/karpathy/llm-wiki.md). The gist is modular; [the current schema](../../system/schema/llm-wiki.md) owns this workspace's implementation.

## Lint contradictions, stale claims and missing connections

The gist proposes recurring health checks. Local route: inspect contradictory generations, freshness, inbound links, missing topics and unresolved evidence gaps; report uncertainty before adjudicating conflicts.

> contradictions between pages, stale claims that newer sources have superseded, orphan pages with no inbound links

[Preserved gist](../../raw/sources/karpathy-brain/raw/github/gists/442a6bf555914893e9891c11519de94f/llm-wiki.md), Operations; [source page](../sources/karpathy/llm-wiki.md). The gist is modular; [the current schema](../../system/schema/llm-wiki.md) owns this workspace's implementation.

## Coverage and attribution map

This synthesis uses conclusions from the reviewed source pages, not all collected bytes as personal beliefs. Consult the coverage ledgers for the reviewed files and processing limits:

- [Writings](../../research/karpathy-brain-2026-10-08/blog-synthesis.md): preserved blog text, historical course revisions, personal guides and fiction, with authorship qualifications.
- [Lectures and interviews](../../research/karpathy-brain-2026-10-08/lecture-synthesis.md): all 17 preserved texts fully read; 14 spoken-source texts and three music/animation caption files. Audio, diagrams and missing speech are unverified.
- [Repository and X evidence](../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md): all saved repository files are accounted for with text/payload distinctions; all selected captured own-author X bodies are reviewed. Exhaustive upstream X coverage remains unverified.
- [Supplemental repositories](../../research/karpathy-brain-2026-10-08/repo-supplemental-synthesis.md): all 175 selected paths reviewed, including 24 decoded notebooks (three exact duplicates) and two empty files; embedded images and local execution remain outside coverage.
- [llm.c](../../research/karpathy-brain-2026-10-08/llmc-synthesis.md): reviewed reference implementations, memory/compute choices and checker limitations. Repository ownership does not establish individual contributor authorship.
- [Payloads](../../research/karpathy-brain-2026-10-08/github-payload-synthesis.md): generated dependencies, training text, parameters and government HTML have integrity/structure records; mechanical processing does not turn them into Karpathy beliefs or full model semantic reads.

CS231n course/team texts, guest tutorials, third-party libraries, BLS pages, generated prompts and fictional narration are not attributed as personal doctrine. Historical provider rankings and prices remain dated. A quotation establishes what the preserved source says, not factual truth, successful local execution or a present capability. Related papers and linked media need independent review. Joshua's voice, policies and canonical routes remain authoritative.

Return to [index](index.md), [principles](principles.md), [methods](methods.md), [rules](rules.md) or [hot page](hot.md).
