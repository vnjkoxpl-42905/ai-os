---
type: source
subject: "repos/karpathy/neuraltalk2/convert_checkpoint_gpu_to_cpu.lua"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-preserved-text-read
---

# repos/karpathy/neuraltalk2/convert_checkpoint_gpu_to_cpu.lua

Captured repository text; repository ownership does not establish individual authorship. Original date: 2015-11-20T01:27:58Z (created); pushed 2017-11-07T05:59:20Z. Captured: 2026-10-08T09:35:08.424778Z.

[Immutable raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk2/convert_checkpoint_gpu_to_cpu.lua). SHA-256 `c73da9ee101ddf0390762fe7c64245aaf1788e60ead94084a70704e34a342398`. Manifest hash match: True.

## Reviewed content

GPU-to-CPU checkpoint conversion replaces cudnn convolution/pooling/ReLU with nn equivalents and strips gradients/clones. Credits Michael Partheil adaptation and includes an interactive debugger in the LM branch.

> -- these functions are adapted from Michael Partheil

## Limits

Complete preserved text read, lines1-98. No code or shell command was executed. Captured outcomes and configured checks do not establish local correctness, safety, performance or compatibility. No personal rule is derived solely from this file.
