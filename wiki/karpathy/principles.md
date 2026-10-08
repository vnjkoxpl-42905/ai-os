---
type: synthesis
subject: Karpathy candidate principles from reviewed sources
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, evidence]
sources: [../sources/karpathy/llm-wiki.md, ../sources/karpathy/autoresearch-readme.md, ../sources/karpathy/micrograd-readme.md, ../sources/karpathy/jobs-readme.md, ../sources/karpathy/animals-vs-ghosts.md]
---

# Candidate observations need wider evidence

The observations below preserve the initial five-source compilation. The current operational synthesis is [seven reviewed rules](rules.md), with two distinct source locations per rule. Additional domain coverage is linked from [the index](index.md). Full-corpus reading remains incomplete; these initial observations are not a second competing rule set.

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

Return to [index](index.md), [hot page](hot.md) or [methods](methods.md). None of these observations overrides Joshua's voice, policies or decisions.
