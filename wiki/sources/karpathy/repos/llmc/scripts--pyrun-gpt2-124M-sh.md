---
type: source
subject: "llm.c / scripts/pyrun_gpt2_124M.sh"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: scripts/pyrun_gpt2_124M.sh

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.297342Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/scripts/pyrun_gpt2_124M.sh) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `4c2d31ae8defdeeaf4c7cf7f22427c9b732b4b9d18c590a0b4011ce6d1632149`

## What the complete source contains

Evidence: `torchrun --standalone --nproc_per_node=8 train_gpt2.py` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/scripts/pyrun_gpt2_124M.sh)). The PyTorch comparison launcher selects eight local workers; its comment explains using plain Python for a single GPU.

Evidence: `--model d12` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/scripts/pyrun_gpt2_124M.sh)). The recipe sets the d12 architecture, bfloat16, compilation, tensor cores and FlashAttention, with 524288 total tokens per batch and 18865 iterations on FineWeb10B.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
