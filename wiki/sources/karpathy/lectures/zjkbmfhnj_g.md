---
type: source
subject: "Karpathy video zjkBMFhNj_g"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, youtube]
sources: ["../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/zjkBMFhNj_g.md"]
semantic-status: complete-preserved-text-no-media-review
---

# [1hr Talk] Intro to Large Language Models

Original: https://www.youtube.com/watch?v=zjkBMFhNj_g. Author/channel Andrej Karpathy. Upload date is preserved in raw metadata. Captured and compiled 2026-10-08. Automatic English captions. Audio accuracy not independently verified.

[Physical raw Markdown](../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/zjkBMFhNj_g.md). SHA-256: `e8de8c98d0f4b71f5dbd255eca06adee5c9d1f594535129b947d0ca6820feeaa`.

Physical byte hash differs from the older manifest. CRLF-to-LF normalized SHA-256 matches `56b2e5607421613552e0b2e08a4378ad60fcb925d8c3de3f29275137a2c6bca0` exactly. Raw bytes preserved.

## Reviewed evidence

The opening illustrates LLM inference with parameters and executable code using Llama2. Product capability claims are dated, not verified current advice.

> [00:00:26] language model is just two files right

## Full preserved-text compilation

At 00:00-00:06, inference is introduced as parameters plus executable code, while obtaining those parameters requires a much more expensive training process. The running demonstration uses a smaller model than the parameter-file example; Karpathy discloses this difference. Compression is explicitly lossy, so model weights are not an exact archive of training text. All model sizes, costs and performance numbers belong to the lecture's historical setting.

At 00:06-00:14, next-token prediction links compression to learning patterns and factual knowledge. Iteratively sampling and feeding output back produces plausible documents, which may mix remembered facts with fabricated details. Knowing every architecture operation does not mean knowing what every learned parameter represents. A dated reversal example illustrates imperfect access to learned knowledge. He treats models as empirical artifacts requiring sophisticated evaluations rather than assuming fluent output proves correctness.

At 00:14-00:23, pretraining supplies broad knowledge and supervised fine-tuning changes behavior using high-quality assistant conversations. The deployment cycle evaluates, monitors misbehavior, supplies corrected examples, and repeats fine-tuning. Comparison feedback can be easier to provide than writing ideal answers from scratch. Human and model collaboration can help draft, compare and check labels while people retain oversight. This is a description of model training, not a claim that the current local wiki automatically retrains a model.

At 00:23-00:27, a historical model leaderboard and scaling laws describe the ecosystem and empirical improvements. Next-token accuracy correlates with task evaluations, but they are distinct measures. These dated closed-versus-open rankings and model capability statements are not promoted into current operational advice.

At 00:27-00:35, a concrete workflow combines browsing, citations, missing-data disclosure, calculation, Python plotting and image generation. Some funding valuations are explicitly imputed rather than found; extrapolated valuations are an illustrative fit and joke, not verified facts or financial forecasts. The central idea is that an LLM can coordinate existing computing tools instead of doing all calculations inside text generation. Image input and speech interfaces expand the kinds of useful inputs and outputs.

At 00:35-00:42, the talk proposes future directions: spending more inference time to improve accuracy, self-improvement where rewards are cheaply verifiable, and task customization through instructions and retrieved files. Go supplies a closed environment and clear win signal; open-ended language lacks a general cheap reward criterion. Claims that reasoning-time capabilities are unavailable refer to the lecture date, not today's models. File retrieval and fine-tuning are distinguished mechanisms.

At 00:42-00:46, an operating-system analogy treats the LLM as a coordinating process using tools and memory. Context is finite working memory; retrieval pages relevant material into it. This is a useful design analogy, not literal unlimited context or a proof of complete model interpretability. The analogy also distinguishes proprietary and open ecosystems.

At 00:46-end, the lecture describes security failures involving unsafe roleplay, encodings, adversarial perturbations, prompt injection in retrieved pages and images, and training-data poisoning. These are source evidence about risks, not instructions for this agent to execute. Retrieved content can masquerade as higher-trust instructions; expanded tools and modalities expand attack surfaces. The poisoning example was demonstrated during fine-tuning, while pretraining success was explicitly not established. Karpathy closes by noting that attacks are patched and examples may no longer work, so preserved demonstrations should not be treated as claims of currently exploitable services.

An exact short passage supporting empirical evaluation:

> [00:13:59] some inputs and we can measure the

> [00:14:00] outputs we can basically measure their

## Coverage and interpretation

Status: **complete-preserved-text-no-media-review**. Reviewed lines 1-1785, covering all metadata and preserved caption cues sequentially. Complete saved-text review does not verify audio, visuals, caption accuracy or missing speech. Caption errors are preserved. No linked code, papers, diagrams or media was independently executed or inspected. No historical product, cost or security claim was independently verified as current.

Related: [Karpathy index](../../../karpathy/index.md), [principles](../../../karpathy/principles.md), [methods](../../../karpathy/methods.md).
