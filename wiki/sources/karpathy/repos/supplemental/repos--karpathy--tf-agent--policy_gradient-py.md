---
type: source
subject: "repos/karpathy/tf-agent/policy_gradient.py"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-preserved-text-read
---

# repos/karpathy/tf-agent/policy_gradient.py

Captured repository text; ownership does not establish individual authorship. Original date: 2016-09-30T08:30:55Z (created); pushed 2017-07-21T23:23:54Z. Captured: 2026-10-08T09:35:38.285678Z.

[Immutable raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/tf-agent/policy_gradient.py). SHA-256 `84008b64713920e737409757a895f9fd7a421d359bb3527ef7b5df16e1dcb3db`. Manifest hash match: True.

## Reviewed content

Historical TensorFlow actor-critic example preprocesses Atari frames, stacks motion context, collects episode rollouts, discounts rewards and combines policy/value/entropy losses with Adam and gradient clipping. Old Gym/TensorFlow interfaces and loss-shape behavior are not locally validated; no game or training executed.

> """ implements a simple policy gradient (actor critic technically) agent """

## Limits

Complete preserved text read, lines 1-138. No captured code executed or linked sources inspected. Static source review does not establish current correctness, performance or compatibility.
