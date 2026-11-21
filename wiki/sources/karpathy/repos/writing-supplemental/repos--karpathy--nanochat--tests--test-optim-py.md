---
type: source
subject: Karpathy repository source context
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [llm-wiki, karpathy, source-context]
sources:
  - ../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/tests/test_optim.py
---

# repos/karpathy/nanochat/tests/test_optim.py

Original: [captured source](https://github.com/karpathy/nanochat). Capture: 2026-10-08T09:35:02.564408Z. Attribution: karpathy; classification: `authored_code`.

Archived: [physical raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/tests/test_optim.py). SHA-256: `881c135ad8f0603f588750fdc521503e407f50918b3a59a6ea81188cacd2ad03`.

## Source account

```text
The AdamW half is checked against torch.optim.AdamW as a reference;
```

GPU-only single-rank tests compare fused AdamW against PyTorch, check bitwise repeatability, target-distance convergence, and the singular-value spread of a first Muon update. Distributed optimizer behavior is outside this test file. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/tests/test_optim.py).

## Limits

Code not executed; configured checks are not passing test evidence. This source does not independently establish Karpathy personal beliefs. Raw unchanged.
