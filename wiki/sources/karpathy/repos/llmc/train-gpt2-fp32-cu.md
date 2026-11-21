---
type: source
subject: "llm.c / train_gpt2_fp32.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: train_gpt2_fp32.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.757295Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_gpt2_fp32.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `93a993ded0f64a70b3d3961d7837acdeed963080b35a2794e219bbc496a5f478`

## What the complete source contains

Evidence: `all parameters use a += in the backward pass` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_gpt2_fp32.cu)). The FP32 CUDA GPT-2 trainer accumulates parameter gradients while overwriting most activation gradients, with additive handling for residual-stream contributions.

Evidence: `reuse memory, so that we need far fewer tensors for backward state.` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_gpt2_fp32.cu)). It allocates sixteen parameter tensors, twenty-one forward tensors, and only three reusable backward buffers. The forward output allocation doubles as scratch space and training logit gradients; dead forward activations are reused during reverse traversal.

Evidence: `calculate the gradients directly, saves bandwidth from probs during training` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_gpt2_fp32.cu)). A fused classifier computes cross-entropy and overwrites logits with mean-loss gradients, avoiding a separate stored probability tensor during training.

Evidence: `if (model_header[1] != 3)` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_gpt2_fp32.cu)). Checkpoint loading requires magic 20240326 and version 3 with padded vocabulary. Forward calls validate token IDs and reject B/T changes after lazy allocation; model output weights are tied to token embeddings.

Evidence: `the inference here is just for sanity checking anyway` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_gpt2_fp32.cu)). The CLI trains one epoch with periodic validation and full-context autoregressive sanity samples, rather than a KV-cache inference service. AdamW moments remain FP32 and timings synchronize GPU work.

## Interpretation and limits

Read through EOF; no training run. This is the standalone FP32 reference, distinct from the newer distributed trainer. Several tiled kernels assume divisible dimensions. Sampling exponentiates unshifted logits; CLI integers and cadence values are not comprehensively validated. It is not a production or numerical-stability guarantee. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
