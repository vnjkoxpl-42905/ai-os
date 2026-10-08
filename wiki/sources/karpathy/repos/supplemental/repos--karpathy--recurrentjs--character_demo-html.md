---
type: source
subject: "repos/karpathy/recurrentjs/character_demo.html"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-preserved-text-read
---

# repos/karpathy/recurrentjs/character_demo.html

Captured repository text; ownership does not establish individual authorship. Original date: 2014-12-18T20:26:27Z (created); pushed 2016-11-04T15:42:55Z. Captured: 2026-10-08T09:35:27.232340Z.

[Immutable raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/recurrentjs/character_demo.html). SHA-256 `d3caa2c053a696957644d5f0f2840ed25c47f8ce216e94b9f14d09097ed2b727`. Manifest hash match: True.

## Reviewed content

Browser character-generation demo constructs character vocabulary, learned letter embeddings, RNN/LSTM hidden layers and next-character softmax cross-entropy. Interactive learning-rate/temperature controls show speed, training perplexity, samples and greedy decoding; save/load retains weights and optimizer cache. Central-difference gradient-check function exists but UI handler is commented out, and signed relative error only logs positive discrepancies. Large embedded Paul Graham essay sentences are third-party training data, not Karpathy beliefs; all preserved lines including that dataset were read. Intro aims at startup-wisdom generation through memorization, not verified factual-persona replication. Historic pretrained perplexity claim is author prose, not rerun proof.

> The demo is pre-filled with sentences from <a href="http://www.paulgraham.com/articles.html">Paul Graham's essays</a>, in an attempt to encode Paul Graham's knowledge into the weights of the Recurrent Networks. The long-term goal of the project then is to generate startup wisdom at will. Feel free to train on whatever data you wish, and to experiment with the parameters. If you want more impressive models you have to increase the sizes of hidden layers, and maybe slightly the letter vectors. However, this will take longer to train.<br><br>

## Limits

Complete preserved text read, lines 1-2027. No captured code executed or linked sources inspected. Static source review does not establish current correctness, performance or compatibility.
