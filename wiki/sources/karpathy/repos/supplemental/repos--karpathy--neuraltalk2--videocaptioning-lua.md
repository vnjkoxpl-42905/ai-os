---
type: source
subject: "repos/karpathy/neuraltalk2/videocaptioning.lua"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-preserved-text-read
---

# repos/karpathy/neuraltalk2/videocaptioning.lua

Captured repository text; ownership does not establish individual authorship. Original date: 2015-11-20T01:27:58Z (created); pushed 2017-11-07T05:59:20Z. Captured: 2026-10-08T09:35:08.446335Z.

[Immutable raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk2/videocaptioning.lua). SHA-256 `e7d5eb500a86ea801a45995b19ac2740b0cd9ec2ffce8f56844003be3b17c6a3`. Manifest hash match: True.

## Reviewed content

Real-time webcam captioning loads a checkpoint, crops/normalizes BGR camera frames, samples captions and overlays text in an OpenCV window until a keypress. Beam-size help explicitly says more is not always better. No camera accessed or checkpoint executed.

> cmd:option('-beam_size', 2, 'used when sample_max = 1, indicates number of beams in beam search. Usually 2 or 3 works well. More is not better. Set this to 1 for faster runtime but a bit worse performance.')

## Limits

Complete preserved text read, lines 1-142. No captured code executed or linked sources inspected. Static source review does not establish current correctness, performance or compatibility.
