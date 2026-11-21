---
type: source
subject: "repos/karpathy/reinforcejs/waterworld.js"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-preserved-text-read
---

# repos/karpathy/reinforcejs/waterworld.js

Captured repository text; ownership does not establish individual authorship. Original date: 2015-04-19T02:35:59Z (created); pushed 2019-02-18T20:11:56Z. Captured: 2026-10-08T09:35:29.118240Z.

[Immutable raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/reinforcejs/waterworld.js). SHA-256 `a8dca037a10201e206b0536c91e88e4f4c89033318fa631ec08b1c2ae3af1121`. Manifest hash match: True.

## Reviewed content

World dynamics implement vectors and line/point intersection, nearest sensor hits, 30 radial eyes, damped thrusters, boundary limits, moving food/poison and cleanup/spawning. Each tick computes observations, acts, applies dynamics/contact reward, then learns. Sensor encoding uses three object-type proximity slots plus two velocities per eye, adding own x/y velocity for 152 dimensions. Explicitly resets digestion reward before collisions; some interior-wall collision checks are commented out. This is static implementation evidence, not tested physics or a general-purpose safe environment.

> a.digestion_signal = 0; // important - reset this!

## Limits

Complete preserved text read, lines 1-411. No captured code executed or linked sources inspected. Static source review does not establish current correctness, performance or compatibility.
