---
type: source
subject: "llm.c / train_llama3.py"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: train_llama3.py

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.766175Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_llama3.py) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `b49f74b5c429676f930cede4f4539197e65b24705d4e23ade8bb79bb38200816`

## What the complete source contains

Evidence: `LLaMA reference code explicitly implemented RMSNorm so we copy pasted it` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_llama3.py)). The credited Meta-derived Llama 3.1 reference adds RMS normalization, rotary query/key positions with scaled frequencies, grouped-query attention, SwiGLU projections and optional inference KV caching, with explicit grouped-head divisibility constraints.

Evidence: `Only the 8B-base model is supported for now` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_llama3.py)). Loading supports the specific 3.1 eight-billion base model via Hugging Face or a Meta checkpoint, including key renaming, Q/K unpermutation and projection concatenation. A tokenizer bounds long whitespace/nonwhitespace runs and supplies reserved/stop tokens; generation uses nucleus sampling and truncates at stop tokens.

Evidence: `It is not *permuted*` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/train_llama3.py)). Distributed training reads ordered uint32 version-seven shards, scales accumulated losses, clips gradients and schedules AdamW. The optional C bridge stores configuration in an int32 header, including fractional normalization/FFN fields, so export fidelity needs validation. Training requires CUDA and compatible model access/data; no checkpoint, export, text generation or correctness test was executed.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
