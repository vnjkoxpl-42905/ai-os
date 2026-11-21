---
type: source
subject: "repos/karpathy/neuraltalk2/train.lua"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-preserved-text-read
---

# repos/karpathy/neuraltalk2/train.lua

Captured repository text; ownership does not establish individual authorship. Original date: 2015-11-20T01:27:58Z (created); pushed 2017-11-07T05:59:20Z. Captured: 2026-10-08T09:35:08.442880Z.

[Immutable raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk2/train.lua). SHA-256 `6cedecd27ff244feff9d27cea594d1ffbdef625ce63144599b44e2ea9687d375`. Manifest hash match: True.

## Reviewed content

Caption training orchestrates VGG loading or checkpoints, shared recurrent clones, feature expansion, optional CNN finetuning, clipping, optimizer updates, decay and held-out validation. Saves thin model on improved CIDEr or negative validation loss; records histories/predictions. Stops on large relative loss explosion. Historical hyperparameters and correctness not reproduced.

> -- use CIDEr score for deciding how well we did

## Limits

Complete preserved text read, lines 1-403. No captured code executed or linked sources inspected. Static source review does not establish current correctness, performance or compatibility.
