---
type: source
subject: "llm.c / test_gpt2.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: test_gpt2.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.724913Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/test_gpt2.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `a58906578a7ec5856b481458478b10436f29982ab27e5e5a0863e5c2b1e71280`

## What the complete source contains

Evidence: `return allok ? EXIT_SUCCESS : EXIT_FAILURE;` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/test_gpt2.cu)). The current mixed-precision integration harness combines logits, per-parameter gradients, ten rounded reference losses, and checkpoint/state reload comparisons into its final exit status.

Evidence: `logit_accuracy_threshold = 25.0f` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/test_gpt2.cu)). BF16/lower-precision comparisons explicitly use loose, manually selected thresholds with uncertainty about hardware effects or latent bugs. The reload test checks matching input tokens and exact losses over ten continuation steps, but source configuration is not evidence those tests ran or passed.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
