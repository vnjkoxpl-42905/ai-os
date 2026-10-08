---
type: source
subject: "Regex BPE separates ordinary input from special tokens"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source]
sources: [../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/minbpe/minbpe/regex.py]
semantic-status: complete-named-text-read
---

# Regex BPE separates ordinary input from special tokens

Original repository: https://github.com/karpathy/minbpe. Publication date unknown; captured and compiled 2026-10-08. [Raw evidence](../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/minbpe/minbpe/regex.py), SHA-256 `2f79fc32d719c5805782c441e6311c10790ba9873ee1ec7e920a2d04d3a77e38`. Commit and license: [manifest](../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json). Per-line authorship was not independently established.

## What this source says

> Encoding that ignores any special tokens.

Training counts pairs only within regex-defined chunks, preserving category boundaries. Ordinary encoding processes chunks independently. Special-token registration stores forward and inverse maps. Encoding explicitly chooses all, none, none_raise or a permitted set; the default asserts that registered special strings are absent. Allowed special strings are escaped before regex splitting, then encoded separately. Invalid token IDs raise ValueError; UTF-8 decoding uses replacement. The absence check is implemented as an assertion, so this educational code should not be certified as a hardened input boundary under optimized Python. Historical GPT pattern labels are source labels, not a verified current API contract.

## Interpretation and limits

Complete named source text read. The code was not executed or numerically tested; limitations above are inspection findings, not reproduced failures. Small explicit mechanisms support learning and review without establishing general model quality.

Related: [Karpathy hub](../../../karpathy/index.md). [Coverage](../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
