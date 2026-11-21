---
type: source
subject: "llm.c / train_gpt2.c"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: train_gpt2.c

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.738804Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_gpt2.c) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `6737a6c0945f5ac04d8fb534100506be9871df8c406995b34b84b3deec661258`

## What the complete source contains

Evidence: `clean, minimal, reference` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_gpt2.c)). The CPU reference implements GPT-2 embeddings, pre-normalized attention/MLP residual blocks, tied output embeddings, padded-vocabulary softmax and target loss using readable scalar loops with limited OpenMP. It supplies explicit reverse-order accumulated gradients and AdamW rather than an autograd dependency.

Evidence: `fallback to naive version` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_gpt2.c)). Its eight-position matrix tiling falls back for incompatible batch/time shapes. Checkpoint metadata controls contiguous parameter and activation allocation, input indices are asserted, and later forwards require the originally allocated batch/sequence shape.

Evidence: `the inference here is just for sanity checking` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_gpt2.c)). The main loop chooses local Tiny Shakespeare or TinyStories token files, samples with an intentionally wasteful full recomputation, checks validation loss periodically and performs forty-one training updates. GELU backward locally disables a problematic fast-math optimization. No model checkpoint, generated text, loss parity or runtime performance was reproduced.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
