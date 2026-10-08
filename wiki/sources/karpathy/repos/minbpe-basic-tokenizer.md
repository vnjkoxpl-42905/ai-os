---
type: source
subject: "Basic BPE exposes training and decoding boundaries"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source]
sources: [../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/minbpe/minbpe/basic.py]
semantic-status: complete-named-text-read
---

# Basic BPE exposes training and decoding boundaries

Original repository: https://github.com/karpathy/minbpe. Publication date unknown; captured and compiled 2026-10-08. [Raw evidence](../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/minbpe/minbpe/basic.py), SHA-256 `d240f8b54f25d8c65e81f3da1cc7c3a390a7692cdbf62d6ff6d0c1cba1b031b8`. Commit and license: [manifest](../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json). Per-line authorship was not independently established.

## What this source says

> Does not handle any special tokens.

Training begins with UTF-8 bytes, counts adjacent pairs and repeatedly replaces the most frequent pair with a new token. Encoding follows the lowest learned merge rank and stops when no available pair exists. Decoding concatenates vocabulary bytes and uses replacement on invalid UTF-8. Regex boundaries and special tokens are explicitly excluded. The training loop assumes a remaining pair exists; no tiny-input safeguard is explicit in this source.

## Interpretation and limits

Complete named source text read. The code was not executed or numerically tested; limitations above are inspection findings, not reproduced failures. Small explicit mechanisms support learning and review without establishing general model quality.

Related: [Karpathy hub](../../../karpathy/index.md). [Coverage](../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
