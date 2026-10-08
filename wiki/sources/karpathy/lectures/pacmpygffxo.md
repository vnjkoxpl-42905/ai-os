---
type: source
subject: "Karpathy video PaCmpygFfXo"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, youtube]
sources: ["../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/PaCmpygFfXo.md"]
semantic-status: complete-preserved-text-no-media-review
---

# The spelled-out intro to language modeling: building makemore

Original: [PaCmpygFfXo](https://www.youtube.com/watch?v=PaCmpygFfXo); channel Andrej Karpathy. Upload date 2022-09-07. Captured2026-10-08, compilation2026-10-08. Automatic English captions, not verified against audio.

[Physical raw Markdown](../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/PaCmpygFfXo.md). SHA-256: `f5b8901d3c6e399ac9beee841472f9f573aee26e4d15d14a9318fc62748f66a9`. Physical byte hash differs from the older manifest. CRLF-to-LF normalized SHA-256 matches its hash `a95698b6c2f06a5308e58b44d0bd82036b3ed1d3cb6f18b585952df3a745c708` exactly. Raw bytes were preserved; normalized matching does not make the physical byte hashes identical.

## Reviewed evidence

He begins with a weak character bigram model, explicitly discarding earlier context, and constructs it from a blank notebook. Dataset inspection and individual-word examples establish what the model is allowed to know.

> [00:05:55] at a time.

He counts adjacent characters, including boundary information, before introducing neural networks. A count-matrix visualization reveals wasteful separate start/end tokens and motivates replacing them with one dot token.

> [00:09:22] bigrams, and we can print them.

Poor generated names are checked against an untrained uniform baseline. He explains a one-character name through the model's limited context rather than assuming bad-looking output proves an implementation failure.

> [00:35:14] though it's so terrible is

Precomputing normalized probability rows removes repeated work, but he checks a row sum and exact seeded samples after vectorization. He then deliberately drops keepdim to demonstrate a silent broadcasting bug that runs while normalizing the wrong direction.

> [00:44:04] taking its sum. We expect this to be

He urges respect for broadcasting semantics and inspection of intended dimensions because these bugs are subtle. Correct computation is checked before the efficiency improvement is accepted.

> [00:49:14] So, then

He derives likelihood, log likelihood and average negative log likelihood from individual examples to establish a single model-quality objective. A zero-count unseen bigram produces infinite loss, which added-count smoothing makes finite.

> [00:57:45] normalized log likelihood.

The neural-network implementation first uses one word with five training examples. He checks tensor constructors, integer label types, one-hot float conversion and a matrix-multiplication element against the corresponding dot product.

> [01:06:43] all the words just yet because I want

He interprets outputs as logits, exponentiates and normalizes them into probabilities, then computes differentiable negative log likelihood. This preserves the preceding model's observable semantics while changing how its parameters are learned.

> [01:24:44] So,

After resetting gradients, backward computation and a weight update, he recomputes the forward pass and confirms the loss decreases. The full dataset is introduced only after the five-example pipeline works.

> [01:41:49] and that would be the update to the

He predicts the neural bigram model should converge near the count model's loss, then explains their shared one-character information limit. Larger context makes explicit count tables impractical, motivating the more extensible neural framework.

> [01:44:48] something around what we had originally,

He relates weights near zero to uniform softmax probabilities and adds a quadratic penalty to encourage smoother distributions. This is the lesson's conceptual comparison to count smoothing, not a general proof that L2 regularization exactly equals additive smoothing or label smoothing.

> [01:51:33] be exactly uniform.

Finally he checks generated samples from both formulations. The architecture can grow later while logits, softmax, loss and gradient-based optimization keep their role.

> [01:55:05] P in memory, so this is fine.

## Coverage and interpretation

Status: **complete-preserved-text-no-media-review**. Reviewed line ranges: 1-3420, sequentially in bounded chunks. All preserved caption text was read; original audio/video accuracy and missing speech were not independently verified.

The quoted passages support local teaching/building methods only within their stated scope. Captions contain recognition errors; quotations preserve those errors rather than silently correcting them. No linked code, papers, diagrams or media was independently executed or inspected. Source upload dates do not establish current tool capabilities.

Related: [Karpathy index](../../../karpathy/index.md), [principles](../../../karpathy/principles.md), [methods](../../../karpathy/methods.md).
