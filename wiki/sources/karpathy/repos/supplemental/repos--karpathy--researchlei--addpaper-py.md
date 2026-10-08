---
type: source
subject: "repos/karpathy/researchlei/addpaper.py"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-preserved-text-read
---

# repos/karpathy/researchlei/addpaper.py

Captured repository text; ownership does not establish individual authorship. Original date: 2013-05-01T19:12:29Z (created); pushed 2013-05-03T19:26:12Z. Captured: 2026-10-08T09:35:31.525398Z.

[Immutable raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/researchlei/addpaper.py). SHA-256 `08a7ade5e22d24a445cc5cf16ee37c9240913606529037c22b37d42a748cd3e1`. Manifest hash match: True.

## Reviewed content

Historical Python 2 paper ingestion asks the user to confirm a Microsoft Academic Search record, deduplicates paper IDs in pickle storage, paginates citations and references in batches of 100, and limits requests to 1000. PDF download is followed by explicit human confirmation or manual fallback, then thumbnail/top-word/JSON/resource commands. The appid file convention and printed credential-bearing URLs are historical practices, not an adopted setup. External commands, PDFs and APIs were not executed.

> isok = raw_input("download good? y/n: ")

## Limits

Complete preserved text read, lines 1-246. No captured code executed or linked sources inspected. Static source review does not establish current correctness, performance or compatibility.
