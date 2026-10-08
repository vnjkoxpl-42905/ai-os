---
type: source
subject: "Karpathy video 7xTGNNLPyMI"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, youtube]
sources: ["../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/7xTGNNLPyMI.md"]
semantic-status: complete-preserved-text-no-media-review
---

# Deep Dive into LLMs like ChatGPT

Original: [7xTGNNLPyMI](https://www.youtube.com/watch?v=7xTGNNLPyMI); channel Andrej Karpathy. Upload date 2025-02-05. Captured2026-10-08, compilation2026-10-08. Automatic English captions, not verified against audio.

[Physical raw Markdown](../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/7xTGNNLPyMI.md). SHA-256: `b127900e83876f0ebb13cc6af552bcde0c629dd206a93812a7116406e80c9f34`. Physical byte hash differs from the older manifest. CRLF-to-LF normalized SHA-256 matches its hash `61f6be536e32cce457d96e755bcf4e8baf94054bffa793eac29883e9a27d2817` exactly. Raw bytes were preserved; normalized matching does not make the physical byte hashes identical.

## Reviewed evidence

The reviewed opening frames the talk as a general-audience mental model of LLM construction and sharp edges, beginning with pretraining data. It seeks a diverse large quantity of high-quality documents and describes filtering. Later cognitive, post-training and reinforcement-learning sections remain unreviewed.

> [00:00:12] is to give you kind of mental models for

> [00:00:14] thinking through what it is that this

## Sequential continuation through 00:40:18

The opening traces raw web collection through content extraction, language filtering, deduplication and personal-information removal. Dataset language choices affect which languages a later model can learn.

> [00:04:31] code almost for these web pages but what

Tokenization trades vocabulary size for sequence length. He moves from bits to bytes to merged symbols and stresses that token IDs are identifiers rather than numerical magnitudes.

> [00:09:14] sequence length is actually going to be

Next-token training adjusts parameters so observed continuations receive higher probabilities. The neural network is a fixed mathematical expression whose learned parameters differ from the transient context input.

> [00:18:30] going to go into a little bit of of

Inference repeatedly samples and appends tokens, producing statistical remixes that may or may not match training passages. Conversation with a trained model is distinguished from updating its fixed weights.

> [00:28:00] this one and this

His concrete GPT-2 training demonstration monitors loss and periodic generated samples. Hardware rental and cost estimates are dated examples, not current resource quotations.

> [00:35:26] sequence in particular every single line

## Further evidence from the complete sequential review

Base models are document continuers; assistant behaviour requires a different conversation dataset. He demonstrates lossy memorization, stochastic continuation, and post-cutoff inventions rather than treating a fluent answer as evidence.

> [00:48:49] notice one more thing that I want to

He explains supervised fine-tuning through human-curated worked conversations, including synthetic assistance and labeling instructions. Assistant identity is an externally supplied training convention, not proof of a persistent inner person.

> [01:12:26] responses uh following those labeling

His hallucination discussion separates confidence from correctness. Model-specific factuality probing and refusal training mitigate unknown answers; search supplies explicit evidence to the current context rather than relying only on parameter memory.

> [01:25:02] said searching the web uh we're going to

For document questions he prefers putting the actual text in the context. The chapter demonstration contrasts direct access with imperfect weight recollection.

> [01:40:05] built up as you have a conscious

Intermediate calculations distribute work across tokens. For exact arithmetic, counting, and spelling he prefers code execution and checking the code over trusting mental arithmetic; his bigger-number example fails under an immediate-answer constraint.

> [01:55:59] so actually probably what I do is

His reinforcement-learning explanation uses a school analogy: background exposition, worked examples, then practice against known answers. Rollouts explore solutions; reinforcement changes future likelihood of successful routes. This is a high-level cartoon, not a complete executable optimizer.

> [02:24:57] discovering for itself what kinds of

He interprets the DeepSeek R1 examples as learned checking and backtracking strategies rather than only expert imitation. Early-2025 model availability, pricing, and comparative rankings here are dated examples, not current recommendations.

> [02:31:57] because you wouldn't know what to put

He separates easily verifiable answers from creative tasks whose quality cannot be checked by equality. RLHF substitutes a learned preference scorer for exhaustive human judgment; he presents the easier-discrimination explanation as his hypothesis.

> [02:58:17] writing joke writing or any other

He warns that a learned reward model can be exploited by optimization. His contrast with simple verifiable scoring motivates checking the real objective rather than celebrating a surrogate reward alone.

> [03:03:50] should have a very low score and it will

He calls the uneven capability profile Swiss cheese and keeps responsibility with the user: tools and first drafts require checking, including apparently easy failures. This applies even to reasoning models.

> [03:09:16] many of them and you don't want to trip

He forecasts multimodal and longer-running supervised agents and identifies finite context as a pressure toward future test-time learning research. These are forecasts made in the lecture, not verified present deployment facts.

> [03:11:56] going to start to see what's called

He uses leaderboards as a starting point, then tests models on actual tasks. He also describes newsletters, X, hosted inference, and local smaller models as his dated access and tracking habits.

> [03:17:11] feel like a lot of people for example

He closes by requiring verification and ownership of the final work even while using models frequently for acceleration.

> [03:30:56] that so use them as tools in the toolbox

## Coverage and interpretation

Status: **complete-preserved-text-no-media-review**. Sequentially reviewed every preserved transcript line, 1-5858. Audio and video were not reviewed, so omitted or miscaptioned speech remains unknown.

The quoted passages support local teaching/building methods only within their stated scope. Captions contain recognition errors; quotations preserve those errors rather than silently correcting them. No linked code, papers, diagrams or media was independently executed or inspected. Source upload dates do not establish current tool capabilities.

Related: [Karpathy index](../../../karpathy/index.md), [principles](../../../karpathy/principles.md), [methods](../../../karpathy/methods.md).
