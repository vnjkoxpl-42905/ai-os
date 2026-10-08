---
type: source
subject: "repos/karpathy/neuraltalk2/misc/LanguageModel.lua"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-preserved-text-read
---

# repos/karpathy/neuraltalk2/misc/LanguageModel.lua

Captured repository text; ownership does not establish individual authorship. Original date: 2015-11-20T01:27:58Z (created); pushed 2017-11-07T05:59:20Z. Captured: 2026-10-08T09:35:08.495277Z.

[Immutable raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk2/misc/LanguageModel.lua). SHA-256 `ece6b5932b2e23ea1c164b94a12cf3d3d0c3a1a42a8e8f40ee82a7fe8debecff`. Manifest hash match: True.

## Reviewed content

Caption language model shares recurrent clone parameters, initializes zero state, feeds image then start token, supports greedy/stochastic/temperature/beam sampling and masks variable-length caption loss. Static code includes an explicit beam-search confidence limitation: author declares it correct from plausible outputs/performance despite incomplete tests. Preserve this historical counterexample rather than forcing all code into a never-trust-looks-right doctrine.

> Not 100% sure it's correct, and hard to fully unit test to satisfaction, but
> it seems to work, doesn't crash, gives expected looking outputs, and seems to
> improve performance, so I am declaring this correct.

## Limits

Complete preserved text read, lines 1-451. No captured code executed or linked sources inspected. Static source review does not establish current correctness, performance or compatibility.
