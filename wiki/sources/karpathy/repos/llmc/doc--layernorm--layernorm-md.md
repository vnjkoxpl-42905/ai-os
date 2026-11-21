---
type: source
subject: "llm.c / doc/layernorm/layernorm.md"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: doc/layernorm/layernorm.md

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.113768Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/doc/layernorm/layernorm.md) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `108d6c0fd21eb12693755df8f64b87aeefcd131124ec748139178459836e398b`

## What the complete source contains

Evidence: `it is algorithmically instructive` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/doc/layernorm/layernorm.md)). The tutorial starts from explicit PyTorch operations, manually derives backward gradients, compares with autograd, then removes tensor abstractions to implement the same layer in C.

Evidence: `tradeoff between memory and compute` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/doc/layernorm/layernorm.md)). It explains retaining small mean/rstd caches while recomputing larger normalized activations, distinguishes activation checkpointing from saving weights, and stresses accumulated graph gradients. It compares training with simpler single-stream llama2.c RMSNorm inference and describes extending the same reference-first process to every layer. Linked papers and code were not separately verified in this read.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
