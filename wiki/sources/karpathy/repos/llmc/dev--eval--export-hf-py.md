---
type: source
subject: "llm.c / dev/eval/export_hf.py"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/eval/export_hf.py

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.041660Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/eval/export_hf.py) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `12be528f1ee16f8a625b166af0c995579f6dd41ceb2d22ea1b266f5c9cc11ab8`

## What the complete source contains

Evidence: `version 3 = fp32, padded vocab` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/eval/export_hf.py)). The exporter reads a versioned llm.c checkpoint with FP32 or bfloat16 tensors and maps layer weights into a Hugging Face GPT-2 model, transposing attention and MLP matrices and tying token/output embeddings.

Evidence: `model.save_pretrained(output` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/eval/export_hf.py)). It saves the model and standard GPT-2 tokenizer locally, offers optional hub upload and a CUDA generation demonstration. Captured vocabulary slicing and CLI bool handling need validation before practical use; neither export nor upload was run.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
