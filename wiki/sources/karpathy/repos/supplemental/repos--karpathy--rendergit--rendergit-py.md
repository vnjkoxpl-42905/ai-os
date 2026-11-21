---
type: source
subject: "repos/karpathy/rendergit/rendergit.py"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-preserved-text-read
---

# repos/karpathy/rendergit/rendergit.py

Captured repository text; ownership does not establish individual authorship. Original date: 2025-08-20T03:25:28Z (created); pushed 2025-08-21T19:12:34Z. Captured: 2026-10-08T09:35:30.327945Z.

[Immutable raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/rendergit/rendergit.py). SHA-256 `66bdbe9565987c90960440e775c6aa4b7b90f9ab1528d8f419aa53a3a2bb4c5b`. Manifest hash match: True.

## Reviewed content

Repository rendering CLI shallow-clones to staging, records HEAD, excludes binary/large/VCS files and symlinks, then creates human HTML navigation and an LLM CXML text view with raw file boundaries. Defaults to 50 KiB per file and lists skipped files; flattening is deliberately incomplete. Markdown rendering, skip diagnostics, search and cleanup were reviewed statically, not run.

> Flatten a GitHub repo into a single static HTML page for fast skimming and Ctrl+F.

## Limits

Complete preserved text read, lines 1-520. No captured code executed or linked sources inspected. Static source review does not establish current correctness, performance or compatibility.
