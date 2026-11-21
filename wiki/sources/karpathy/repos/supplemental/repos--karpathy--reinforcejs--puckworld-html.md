---
type: source
subject: "repos/karpathy/reinforcejs/puckworld.html"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-preserved-text-read
---

# repos/karpathy/reinforcejs/puckworld.html

Captured repository text; ownership does not establish individual authorship. Original date: 2015-04-19T02:35:59Z (created); pushed 2019-02-18T20:11:56Z. Captured: 2026-10-08T09:35:29.110210Z.

[Immutable raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/reinforcejs/puckworld.html). SHA-256 `eb0a80a235133468d1a0c578895ec55295885a7f42c70018f0b2322a0cdad401`. Manifest hash match: True.

## Reviewed content

PuckWorld uses position, velocity and relative target positions with discrete thruster actions; reward trades green-target proximity against a pursuing red hazard. UI exposes exploration, replay pointer, TD error, smoothed rewards and pretrained loading. Teaching reduces DQN to regression on bootstrapped targets, contrasts per-action versus shared multi-output forward passes, and explains replay and clipped TD-error gradients. It explicitly says target-network copies were removed after no substantial benefit in simple toy examples, a scoped brevity tradeoff rather than a universal recommendation. Limits include sparse rewards, naive exploration and discrete actions. Text describes four actions while code allows five including no thrust. Editable agent spec is eval-based historical demo code, not adopted execution.

> **Periodic Target Q Value Updates**. The last modification suggested in Mnih et al. also aims to reduce correlations between updates and the immediately undertaken behavior. The idea is to freeze the Q network once in a while into a frozen, copied network \\(\hat{Q}\\) which is used to only compute the targets. This target network is once in a while updated to the actual current \\(Q\\) network. That is, we use the target network \\(r\_t + \gamma \max\_a \hat{Q}(s\_{t+1},a)\\) to compute the target, and \\(Q\\) to evaluate the \\(Q(s\_t, a\_t)\\) part. In terms of the implementation, this requires one additional line of code where we every now and then we sync \\(\hat{Q} \leftarrow Q\\). I played around with this idea but at least on my simple toy examples I did not find it to give a substantial benefit, so I took it out of REINFORCEjs in the current implementation for sake of brevity.

## Limits

Complete preserved text read, lines 1-636. No captured code executed or linked sources inspected. Static source review does not establish current correctness, performance or compatibility.
