---
type: source
subject: Karpathy repository source context
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [llm-wiki, karpathy, source-context]
sources:
  - ../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/model.py
---

# repos/karpathy/nanoGPT/model.py

Original: [captured source](https://github.com/karpathy/nanoGPT). Capture: 2026-10-08T09:35:04.134861Z. Attribution: karpathy; classification: `authored_code`.

Archived: [physical raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/model.py). SHA-256: `7c01703240dbec5d554527dc666e35b3df8391d0b117fddc07afcf325a21d11c`.

## Source account

```text
all of it in this single file.
```

Single-file pre-normalized GPT implementation combines causal SDPA/manual attention, GELU feed-forward blocks, learned token/position embeddings, tied output weights, residual initialization, loss, context cropping, and pretrained GPT-2 import with Conv1D weight transposes. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/model.py).

```text
Any parameters that is 2D will be weight decayed
```

AdamW groups matrices/embeddings with decay and one-dimensional parameters without decay, enabling fused AdamW when supported on CUDA. Generation crops context and uses temperature/top-k multinomial sampling without KV caching; MFU is an A100-based estimate. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/model.py).

## Limits

Code not executed; configured checks are not passing test evidence. This source does not independently establish Karpathy personal beliefs. Raw unchanged.
