---
type: source
subject: "repos/karpathy/neuraltalk2/cv/killall.sh"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-preserved-text-read
---

# repos/karpathy/neuraltalk2/cv/killall.sh

Captured repository text; repository ownership does not establish individual authorship. Original date: 2015-11-20T01:27:58Z (created); pushed 2017-11-07T05:59:20Z. Captured: 2026-10-08T09:35:08.468657Z.

[Immutable raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk2/cv/killall.sh). SHA-256 `cc91f9b3381ee761ab48977e0e83da4b96dfd3075e9a00bb555a55e811a6d8e2`. Manifest hash match: True.

## Reviewed content

Shell pipeline kills screen-associated processes; not executed.

> screen -ls  | grep ak | cut -d. -f1 | awk '{print $1}' | xargs kill

## Limits

Complete preserved text read, lines1-2. No code or shell command was executed. Captured outcomes and configured checks do not establish local correctness, safety, performance or compatibility. No personal rule is derived solely from this file.
