---
type: source
subject: "repos/karpathy/reader3/server.py"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-preserved-text-read
---

# repos/karpathy/reader3/server.py

Captured repository text; ownership does not establish individual authorship. Original date: 2025-11-18T02:37:00Z (created); pushed 2025-11-18T02:37:51Z. Captured: 2026-10-08T09:35:26.005644Z.

[Immutable raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/reader3/server.py). SHA-256 `e72dd1a0ae3b1a03f13d1802e440c0e576537c094b279cfe35b4e97812a9f99c`. Manifest hash match: True.

## Reviewed content

Local FastAPI reader caches ten pickled books, discovers processed directories, renders chapter navigation and serves book images using basenames. Shortcut endpoint calls read_chapter without its required request argument, a static inconsistency. Pickles and HTML are not independently validated or executed.

> Cached so we don't re-read the disk on every click.

## Limits

Complete preserved text read, lines 1-110. No captured code executed or linked sources inspected. Static source review does not establish current correctness, performance or compatibility.
