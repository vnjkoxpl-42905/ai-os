---
type: source
subject: "repos/karpathy/ulogme/export_events.py"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-preserved-text-read
---

# repos/karpathy/ulogme/export_events.py

Captured repository text; ownership does not establish individual authorship. Original date: 2014-05-13T02:16:30Z (created); pushed 2020-09-17T23:08:59Z. Captured: 2026-10-08T09:35:44.575382Z.

[Immutable raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/ulogme/export_events.py). SHA-256 `26cb1228e04be6a596b0ff006baa645a6e04ae0b86fb37a3dfb162be8c60c869`. Manifest hash match: True.

## Reviewed content

Exports daily window, key-frequency and note logs into frontend JSON, rebuilding only when source timestamps are newer and preserving optional blog content. Missing or unparsable log files become empty lists. Empty date inventory is not guarded before min/max.

> # if the log files have not changed there is no need to regen

## Limits

Complete preserved text read, lines 1-116. No captured script executed. No credentials opened, APIs authenticated, monitoring started, data removed or tools installed. This static review does not establish current compatibility.
