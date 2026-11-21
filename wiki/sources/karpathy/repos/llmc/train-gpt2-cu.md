---
type: source
subject: "llm.c / train_gpt2.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: train_gpt2.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.747560Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_gpt2.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `c85ab07c2b0f35229a2ab2e3547dce3598190303341d6529c2ef4b0ac042cafa`

## What the complete source contains

Evidence: `recompute: less memory but less speed.` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_gpt2.cu)). The main CUDA trainer supports explicit memory/computation tradeoffs: retaining activations, recomputing GELU, or recomputing GELU plus layer normalization. Fused residual normalization and optional cuDNN attention reduce separate work or stored attention state.

Evidence: `safe default: do keep master weights in fp32` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_gpt2.cu)). Model activations/parameters follow configured precision while optimizer moments and optional master weights are FP32. Allocation can fall back to managed memory with an explicit performance warning.

Evidence: `Accumulate gradients from this layer in a background stream.` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_gpt2.cu)). Micro-batches accumulate scaled gradients; only the last micro-step launches layer-wise multi-GPU gradient reduction. ZeRO stage 1 updates local optimizer shards and gathers updated parameter shards.

Evidence: `we only want to weight decay the 2D tensors` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_gpt2.cu)). AdamW applies decay to embedding and matrix tensors, leaves one-dimensional scale/bias tensors undecayed, and receives global gradient-norm clipping. Optional loss/gradient z-score thresholds can skip an update.

Evidence: `a checkpoint contains: model weights, optimizer/dataloader state, and a DONE file` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_gpt2.cu)). Checkpointing writes common model weights on rank zero, optimizer/RNG/loader state per rank, and a DONE marker after a barrier. Resume reconstructs master-weight rounding from saved RNG state and restores shuffled shard/sample positions.

Evidence: `we use dense attention, not the alternating dense/banded attention of GPT-3` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_gpt2.cu)). Descriptor-based initialization supports GPT-2 and GPT-3-sized configurations but explicitly differs from original GPT-3 attention. Initialization follows the PyTorch tensor order and scales residual projection weights.

Evidence: `note this is still somewhat wasteful because we don't have a KV cache!` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_gpt2.cu)). The training CLI provides validation, optional HellaSwag scoring, checkpoint retention, a single-batch debugging mode, scheduling, throughput/MFU estimates, and rank-zero autoregressive sanity samples without a KV cache.

## Interpretation and limits

Read all 104647 decoded characters through EOF; raw byte hash verified. No training, CUDA, NCCL, checkpoint resume, or benchmark executed. Bit-perfect resume is a source goal, not a demonstrated guarantee here. This file contains scalar loss/norm NCCL AllReduce calls with count sizeof(float), which is four elements rather than one; do not treat source review as multi-GPU acceptance. CLI documentation and parsing differ for some multi-node flags, and numerical/cadence values are not comprehensively validated. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
