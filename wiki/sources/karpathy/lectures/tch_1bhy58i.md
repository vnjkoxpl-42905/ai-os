---
type: source
subject: "Karpathy video TCH_1BHY58I"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, youtube]
sources: ["../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/TCH_1BHY58I.md"]
semantic-status: complete-preserved-text-no-media-review
---

# Building makemore Part 2: MLP

Original: [TCH_1BHY58I](https://www.youtube.com/watch?v=TCH_1BHY58I); channel Andrej Karpathy. Upload date 2022-09-12. Captured 2026-10-08, compilation 2026-10-08. Automatic English captions, not verified against audio.

[Physical raw Markdown](../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/TCH_1BHY58I.md). SHA-256: `1f2c88cbaf286bdca3cac00208899a095e7babe7221bc7e3649adf84cd4a7808`. Physical byte hash differs from the older manifest. CRLF-to-LF normalized SHA-256 matches its hash `b3199cd6b9e15c1f7a150e43de1a93c32e2e0bc394b4df83c5c064e0f7f84329` exactly. Raw bytes were preserved; normalized matching does not make the physical byte hashes identical.

## Reviewed evidence

The reviewed introduction starts from the previous bigram baseline, identifies poor name generation and exponential growth of count tables with longer context, then motivates an MLP using Bengio et al.2003. A more complex model is introduced in response to a specific demonstrated limitation.

> [00:00:41] And this works and it's approachable.

> [00:01:11] Because if we only take a single

## Complete sequential compilation

00:03-00:09: Shared learned embeddings let related contexts transfer knowledge. The adapted character model uses a shared lookup table, hidden tanh layer, output logits and next-character likelihood. The paper has a bypass variation explicitly excluded from the lesson.

> [00:05:17] space. And so, you can transfer

00:09-00:28: Build a tiny five-name dataset first, inspect padded contexts and labels, then embed one integer before batching all inputs. A one-hot matrix multiplication and lookup are shown equivalent; indexing is faster. Concatenation is replaced by a view only after checking element-wise equality. Tensor storage, strides and shape explain efficiency rather than just asserting it.

> [00:26:17] And you can verify that this actually

00:28-00:38: Verify broadcasting of the bias, normalize logits and select target probabilities. The manual loss is replaced by cross_entropy after deriving it. Production use benefits from fused operations, simpler backward expressions and numerical stability. Extreme positive logits expose overflow; subtracting their maximum preserves softmax probabilities and avoids that overflow.

> [00:33:30] there are actually many good reasons to

00:38-00:45: Zero gradients, backpropagate and update. First overfit one small batch to check the implementation. Identical contexts with different valid next characters cannot all have zero loss. Full-data updates are slow, so minibatches trade exact gradients for more useful steps; the whole-set loss is evaluated separately from the noisy batch loss.

> [00:39:34] first five words

00:45-00:53: Rather than trust a guessed learning rate, reset initialization, search from slow updates to instability, sweep exponentially spaced rates and inspect a loss plot. Train with a reasonable rate and decay later. The notebook procedure is explicitly presented as a rough demonstration, not production optimization.

> [00:45:09] So, let's run the optimization for a

00:53-01:00: Lower training loss alone does not establish a better model. Split names into training, validation and test before constructing character examples. Train parameters on training data, choose hyperparameters using validation, and use test sparingly to avoid adapting to it. Similar train/dev losses motivate investigating underfitting.

> [00:55:38] see whichever one works best on your

01:00-01:13: Increase hidden capacity, inspect optimization, then test whether the two-dimensional embedding is a bottleneck. Learned embeddings are plotted before expanding them. The demonstration removes some magic numbers but admits its remaining tuning is haphazard; production work should run systematic experiments. The final 2.17 validation result is an exercise target, not a universal benchmark.

> [01:09:46] actually have confidence that our

01:13-end: Sampling repeatedly embeds context, computes logits and probabilities, draws the next character, shifts context and decodes until the stop token. A Colab link is offered to make the same experiments accessible without local installation.

> [01:15:10] notebook in your browser. And you can

## Coverage and interpretation

Status: **complete-preserved-text-no-media-review**. Reviewed line ranges: 1-2222, all preserved metadata and caption cues read sequentially. This covers the saved text, not audio/visual verification or missing-caption detection.

The quoted passages support local teaching/building methods only within their stated scope. Captions contain recognition errors; quotations preserve those errors rather than silently correcting them. No linked code, papers, diagrams or media was independently executed or inspected. Source upload dates do not establish current tool capabilities.

Related: [Karpathy index](../../../karpathy/index.md), [principles](../../../karpathy/principles.md), [methods](../../../karpathy/methods.md).
