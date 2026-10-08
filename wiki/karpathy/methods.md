---
type: synthesis
subject: Karpathy project methods from five reviewed texts
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, methods]
sources: [../sources/karpathy/llm-wiki.md, ../sources/karpathy/autoresearch-readme.md, ../sources/karpathy/micrograd-readme.md, ../sources/karpathy/jobs-readme.md]
---

# Project methods are evidence, not installed workflows

This partial Prompt 2 page compares four fully read documents. Code, notebooks, data payloads and runtime behavior have not been reviewed or executed. Methods remain attributed examples and local interpretations.

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

## Distinguish preserved input from derived judgments

jobs labels its HTML evidence:

> Raw HTML pages from BLS (source of truth, ~40MB)

It qualifies the generated scoring layer:

> The scores are rough LLM estimates (Gemini Flash via OpenRouter), not rigorous predictions.

[Raw README](../../raw/sources/karpathy-brain/raw/github/repos/karpathy/jobs/README.md), “Key files” and “What AI Exposure is NOT”; [source summary](../sources/karpathy/jobs-readme.md). The local adaptation is to trace each judgment to its inputs and retain the limits of its method. The BLS payload itself is outside this starter's semantic coverage.

Return to [index](index.md), [principles](principles.md) or [hot page](hot.md).
