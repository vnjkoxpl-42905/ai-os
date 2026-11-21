---
type: source
subject: "llm.c / doc/layernorm/layernorm.py"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: doc/layernorm/layernorm.py

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.159560Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/doc/layernorm/layernorm.py) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `a34670b6ae6e971efe3ffd1fc447ebd32c31678c7c792bcafb8659e78542873b`

## What the complete source contains

Evidence: `recompute the norm (save memory at the cost of compute)` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/doc/layernorm/layernorm.py)). The educational layer-normalization implementation caches inputs, weights, mean and reciprocal standard deviation and recomputes normalized activations in backward.

Evidence: `fakeloss.backward()` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/doc/layernorm/layernorm.py)). It compares hand-derived gradients with PyTorch autograd on a small random tensor, prints maximum errors, and exports forward/backward references to a binary file for C checking. Printing errors is not an assertion of tolerance or evidence of a passing run.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
