---
type: source
subject: "Minbpe separates tokenizer mechanisms"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source]
sources: [../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/minbpe/README.md]
semantic-status: complete-named-text-read
---

# Minbpe separates tokenizer mechanisms

Repository owner: Andrej Karpathy; per-line authorship not independently verified. Original: https://github.com/karpathy/minbpe. Publication date unknown; captured and compiled 2026-10-08. [Preserved evidence](../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/minbpe/README.md), SHA-256 `afff7898661e44eb30ed314398ae16baa61b6fb0a5aaf386cfecb56302607521`. Captured commit and license are in the [manifest](../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## What this source says

> clean, readable and hackable

The README separates base persistence, basic byte BPE, regex category splitting and a GPT-4 compatibility wrapper. It gives train/encode/decode examples and expected tiktoken comparisons. Special-token interpretation requires explicit permission, preventing accidental treatment of user-controlled text as control tokens.

## Interpretation and limits

The complete README was read. Claims about all modern LLM tokenizers are historical source statements, not current universal facts; code, tests, linked lecture and images were not reviewed as part of this page.

Related: [Karpathy hub](../../../karpathy/index.md). Coverage and cross-source conclusions: [repo/X synthesis](../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
