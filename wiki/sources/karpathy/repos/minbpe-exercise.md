---
type: source
subject: "The tokenizer exercise adds one complication at a time"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source]
sources: [../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/minbpe/exercise.md]
semantic-status: complete-named-text-read
---

# The tokenizer exercise adds one complication at a time

Repository owner: Andrej Karpathy; per-line authorship not independently verified. Original: https://github.com/karpathy/minbpe. Publication date unknown; captured and compiled 2026-10-08. [Preserved evidence](../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/minbpe/exercise.md), SHA-256 `43128753154c19fa8acbf99fdfab3c5c87644f4b5de87fd48832649b195618f8`. Captured commit and license are in the [manifest](../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## What this source says

> Retrain your tokenizer and compare the results before and after.

The exercise starts with train, encode and decode for BasicTokenizer, adds regex boundaries, then compares results with cl100k_base. It calls out recovering merge ranks and byte permutations as two compatibility problems. Special tokens are optional; code-point-based SentencePiece is a further extension.

## Interpretation and limits

This is an instructional progression. No GPT-4 parity or working implementation is certified by reading it.

Related: [Karpathy hub](../../../karpathy/index.md). Coverage and cross-source conclusions: [repo/X synthesis](../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
