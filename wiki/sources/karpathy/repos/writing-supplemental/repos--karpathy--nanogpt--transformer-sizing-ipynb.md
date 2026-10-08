---
type: source
subject: Karpathy repository source context
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [llm-wiki, karpathy, source-context]
sources:
  - ../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/transformer_sizing.ipynb
---

# repos/karpathy/nanoGPT/transformer_sizing.ipynb

Original: [captured source](https://github.com/karpathy/nanoGPT). Capture: 2026-10-08T09:35:04.161482Z. Attribution: karpathy; classification: `authored_notebook_with_generated_outputs`.

Archived: [physical raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/transformer_sizing.ipynb). SHA-256: `1d2285cb3dccc5b62a4b256e6cda579e0e13aea3a58d5fbb19b8c4f0262a4630`.

## Source account

```text
this notebook assumes bias=False just for simplicity
```

Notebook estimates GPT parameter counts, FP32 model/AdamW memory, matrix FLOPs, MFU and a training-time budget, comparing captured estimates with historical outputs. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/transformer_sizing.ipynb).

```text
TODO estimate LOAD/STORE costs
```

Bandwidth analysis remains unfinished. Captured runtime and memory comparisons are notebook outputs, not measurements performed during ingestion. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/transformer_sizing.ipynb).

## Limits

All 17 authored cells and textual outputs read through EOF; JSON machine-parsed, no embedded images. Estimates assume the stated GPT configuration and A100 throughput. Not rerun or independently benchmarked. This source does not independently establish Karpathy personal beliefs. Raw unchanged.
