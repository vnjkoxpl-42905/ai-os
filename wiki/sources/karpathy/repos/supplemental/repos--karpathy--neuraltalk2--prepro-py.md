---
type: source
subject: "repos/karpathy/neuraltalk2/prepro.py"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-preserved-text-read
---

# repos/karpathy/neuraltalk2/prepro.py

Captured repository text; ownership does not establish individual authorship. Original date: 2015-11-20T01:27:58Z (created); pushed 2017-11-07T05:59:20Z. Captured: 2026-10-08T09:35:08.434008Z.

[Immutable raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk2/prepro.py). SHA-256 `2d187f8fadd07b691c36b346c1d8eb7e45cfa6a2749b4c93d2e48f0826c27d1b`. Manifest hash match: True.

## Reviewed content

Caption preprocessing lowercases/removes punctuation, maps rare words to UNK, shuffles reproducibly, assigns held-out splits and writes one-indexed padded caption arrays with per-image ranges and RGB resized images. Vocabulary counts are built before split assignment; data-leakage semantics need context, not a universal claim. Historical SciPy/Python 2 workflow not run.

> seed(123) # make reproducible

## Limits

Complete preserved text read, lines 1-240. No captured code executed or linked sources inspected. Static source review does not establish current correctness, performance or compatibility.
