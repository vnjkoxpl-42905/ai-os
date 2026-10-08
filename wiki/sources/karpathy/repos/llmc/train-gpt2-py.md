---
type: source
subject: "llm.c / train_gpt2.py"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: train_gpt2.py

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.753215Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_gpt2.py) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `757d0cea0d48cbc4c7d7d70371f955d49cdf3a7cfb4c87701a720c2fe0905c34`

## What the complete source contains

Evidence: `Python -> C bridge utilities` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_gpt2.py)). The PyTorch reference defines GPT-2 with tied embeddings, seeded initialization, manual or flash causal attention, Hugging Face checkpoint transpose checks, and export formats for FP32/BF16 weights, tokenizer and forward/backward reference state.

Evidence: `addition of gradients corresponds to a SUM` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_gpt2.py)). Training scales each microbatch loss to preserve a mean objective, synchronizes DDP gradients only on the final microstep, clips gradients, and applies warmup/cosine learning-rate scheduling. Optimizer groups decay matrix/embedding parameters but not biases or normalization, with optional stage-one redundancy handling.

Evidence: `default settings will overfit a tiny batch` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_gpt2.py)). The default ten-step run deliberately overfits one small batch to produce a C comparison reference; CLI options support longer runs, validation, samples, precision and compilation. Distributed loading partitions contiguous uint16 shards. Final memory reporting still calls CUDA unconditionally, and FP16 scaling is not implemented here; no export, download, training or runtime compatibility was executed.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
