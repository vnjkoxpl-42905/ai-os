---
type: source
subject: "llm.c / test_gpt2_fp32.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: test_gpt2_fp32.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.731571Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/test_gpt2_fp32.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `69b867bfa18189793b79d4100c9d2217fca36e4a7805232728fca22f8bb40e02`

## What the complete source contains

Evidence: `disable TF32 for testing` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/test_gpt2_fp32.cu)). The FP32 CUDA integration test disables TF32, loads Python-exported tensors, compares target-free output logits over the unpadded vocabulary, and runs ten fixed-reference training steps.

Evidence: `check_tensor(calculated_grads_memory` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/test_gpt2_fp32.cu)). It prints a whole-parameter gradient comparison but does not combine its returned flag into allok. Loss/logit flags are reported, yet main returns zero regardless. Those source-level gaps prevent treating process success as comprehensive numerical acceptance; no GPU test ran.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
