---
type: source
subject: "Karpathy video P6sfmUTpUmc"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, youtube]
sources: ["../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/P6sfmUTpUmc.md"]
semantic-status: complete-preserved-text-no-media-review
---

# Building makemore Part 3: Activations & Gradients, BatchNorm

Original: [P6sfmUTpUmc](https://www.youtube.com/watch?v=P6sfmUTpUmc); channel Andrej Karpathy. Upload date 2022-10-04. Captured2026-10-08, compilation2026-10-08. Automatic English captions, not verified against audio.

[Physical raw Markdown](../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/P6sfmUTpUmc.md). SHA-256: `2e2eff587c196512efd3abe51827628c9fbe7a9e6e72912b5b63939d30b7954c`. Physical byte hash differs from the older manifest. CRLF-to-LF normalized SHA-256 matches its hash `b1eb0438a0d9ef27f6ba98e2c1b57bdfe93aa080505f126bbb5b761120738302` exactly. Raw bytes were preserved; normalized matching does not make the physical byte hashes identical.

## Reviewed evidence

He tests initialization against the expected uniform-character loss, inspects logits at the first iteration, then reduces output confidence. The resulting loss curve removes wasteful early optimization rather than merely reporting a smaller final loss.

> [00:04:33] iteration we are recording a loss of 27

He inspects tanh activation histograms and a saturation mask to explain why flat activation tails obstruct gradients. He distinguishes saturation from an entirely dead neuron and compares related sigmoid/ReLU failure modes.

> [00:13:02] neural net and let me reintroduce The

He replaces arbitrary weight scales with a small Gaussian matrix-multiplication experiment and fan-in reasoning. Nonlinearity gains require compensation; he explicitly admits he cannot explain the origin of the tanh 5/3 default mathematically.

> [00:27:53] okay so that's great that that worked

Batch normalization is introduced as differentiable centering/scaling with learned gain and bias. It stabilizes deeper networks but couples examples within a batch, introducing a regularization effect and troublesome train/inference differences.

> [00:45:27] only at initialization uh but we don't

Inference requires fixed population statistics. He demonstrates explicit calibration, then running estimates updated outside gradient optimization, compares their resulting values, and removes the earlier linear bias because normalization subtracts it.

> [00:54:37] following what we would like to do here

The module refactor separates parameters from buffers and makes training/evaluation behavior explicit. The bonus implementation tracks variance rather than the earlier standard deviation, and its extra output attribute exists specifically for teaching diagnostics.

> [01:22:42] here we only return gamma and beta we do

He prefers update-to-parameter ratios over gradient-to-parameter ratios because actual changes include the learning rate. He plots these through time, varies learning rates and initialization, and treats the approximate 10^-3 ratio as a rough diagnostic heuristic, not a universal law.

> [01:39:42] actually coming coming in during the

Adding normalization makes forward and backward statistics less sensitive to weight scales but does not eliminate the need to calibrate update scales and learning rates.

> [01:48:40] slower than what we had with the tan

He explicitly reports that normalization did not improve this small model beyond prior results. He suspects the short context is now the bottleneck and distinguishes introducing diagnostics from completely explaining every backward-pass interaction.

> [01:53:32] too high then probably the learning rate

## Coverage and interpretation

Status: **complete-preserved-text-no-media-review**. Reviewed line ranges: 1-3123, sequentially in bounded chunks. All preserved transcript text was read; no audio or video review was performed. Missing speech or inaccurate captions cannot be ruled out.

The quoted passages support local teaching/building methods only within their stated scope. Captions contain recognition errors; quotations preserve those errors rather than silently correcting them. No linked code, papers, diagrams or media was independently executed or inspected. Source upload dates do not establish current tool capabilities.

Related: [Karpathy index](../../../karpathy/index.md), [principles](../../../karpathy/principles.md), [methods](../../../karpathy/methods.md).
