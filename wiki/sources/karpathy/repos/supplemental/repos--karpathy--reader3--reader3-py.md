---
type: source
subject: "repos/karpathy/reader3/reader3.py"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-preserved-text-read
---

# repos/karpathy/reader3/reader3.py

Captured repository text; ownership does not establish individual authorship. Original date: 2025-11-18T02:37:00Z (created); pushed 2025-11-18T02:37:51Z. Captured: 2026-10-08T09:35:25.997009Z.

[Immutable raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/reader3/reader3.py). SHA-256 `06323e6eb9f0ab9c10c3d81e2696129d2ec5247f94019a5464aa0a898932d0ab`. Manifest hash match: True.

## Reviewed content

EPUB conversion separates physical spine files from logical nested TOC entries, extracts metadata/images and produces cleaned HTML plus plain text for search/LLM context. It replaces existing output directories, strips selected tags and serializes a dataclass Book to pickle. Static sanitation is not a full security guarantee; no books processed or outputs removed.

> text: str         # Plain text for search/LLM context

## Limits

Complete preserved text read, lines 1-313. No captured code executed or linked sources inspected. Static source review does not establish current correctness, performance or compatibility.
