# Lecture compilation has useful evidence and explicit unread sections

Compiled 2026-10-08. Seventeen physical source pages exist under [lecture sources](../../wiki/sources/karpathy/lectures/): 15 original channel caption files and two external 2026 interview mirrors. The 15 originals are **12 spoken lectures plus three music/animation caption files**, not 15 spoken lectures. **Fifteen files have complete preserved-text review**: the three music-caption files and twelve spoken-source texts, including both interview mirrors. **Two remain bounded**. Media and linked code were not inspected or executed. The [coverage ledger](lecture-semantic-coverage.jsonl) records actual reviewed ranges and SHA-256 values. All 15 physical byte hashes differ from the old manifest, but every CRLF-to-LF normalized hash matches it exactly. Physical hashes and normalization are recorded separately; raw bytes remain untouched.

Prompt 2's requirement to compile everything has **not** been satisfied by indexing these files. The original transcript corpus contains 325,686 words. Source pages explicitly identify unread sections; raw evidence was never edited. This distinction must remain visible in the central coverage and execution report.

## Direct lecture evidence for rule derivation

| Candidate method | Direct source and reviewed evidence | Scope and qualification |
|---|---|---|
| Expose the mechanism before abstraction | [Micrograd](../../wiki/sources/karpathy/lectures/vmj-3s1tku0.md), opening through 00:08:09, begins with scalar operations and separates mathematical understanding from tensor efficiency. [Backprop Ninja](../../wiki/sources/karpathy/lectures/q8sa3rm6cki.md), opening through 00:05:28, replaces automatic tensor backprop with an exercise to expose hidden errors. | Independent lectures corroborate a teaching method. Both distinguish an exercise from production implementation. |
| Start small and progress explicitly | [Makemore introduction](../../wiki/sources/karpathy/lectures/pacmpygffxo.md), opening, promises a stepwise construction. [Tokenizer](../../wiki/sources/karpathy/lectures/zdusfxrajke.md), 00:23:51-00:57:34, progresses from a tiny symbolic sequence through byte operations to a working BPE implementation. | Simplification is for inspectability; the full Tokenizer review also distinguishes learned BPE, regex boundaries and explicit special tokens. |
| State a target or prediction and compare real output | [GPT-2 reproduction](../../wiki/sources/karpathy/lectures/l8prsuu81pu.md), opening plus 00:03:02-00:07:08, loads the reference target and inspects weights; validation data is separate from training. [Tokenizer](../../wiki/sources/karpathy/lectures/zdusfxrajke.md), BPE core, predicts 20 fewer tokens for 20 pair replacements, checks counts, and verifies round trips on unseen text. | The source demonstrates checks. This compilation did not reproduce their runs. |
| Make failure observable and repair its cause | [Micrograd](../../wiki/sources/karpathy/lectures/vmj-3s1tku0.md), 01:22:00-01:25:32, exposes the repeated-node gradient bug; predicted derivative two differs from actual one, and gradient accumulation fixes the cause. [Tokenizer](../../wiki/sources/karpathy/lectures/zdusfxrajke.md), core, exposes invalid UTF-8, then an empty/single-token encoding failure and repairs those cases. | Failure examples support debugging by counterexample. They do not require intentionally breaking every production task. |
| Understand before increasing architectural complexity | [Activations and gradients](../../wiki/sources/karpathy/lectures/p6sfmutpumc.md), opening, pauses expansion to understand activation/gradient behavior. [MLP](../../wiki/sources/karpathy/lectures/tch_1bhy58i.md), opening, introduces the next architecture in response to limitations of the existing count baseline. | The evidence concerns neural-network teaching sequence, not a universal ban on complex tools. |
| Add complexity in response to a demonstrated limitation | [MLP](../../wiki/sources/karpathy/lectures/tch_1bhy58i.md), opening, identifies exponential context-table growth. [WaveNet](../../wiki/sources/karpathy/lectures/t3yj5hkimq0.md), opening, motivates deeper fusion and longer context. | Closely related series episodes may be weaker independent corroboration than a blog plus lecture; seek cross-domain evidence for the final seven. |
| Delegate independent work and review it | [No Priors interview](../../wiki/sources/karpathy/lectures/kwsvtq7dziu.md), opening through 00:04:27, discusses independent larger changes assigned to separate agents. [Sequoia interview](../../wiki/sources/karpathy/lectures/96jn2ocofls.md), complete preserved text, distinguishes professional quality-bar preservation, detailed specifications, oversight and meaningful user identifiers from merely generating working code. | Speaker attribution is contextual and mirrors are not audio-verified. Do not treat host introductions as his statements. Sequoia supports responsibility and oversight but does not independently establish every No Priors parallel-agent detail. |

The table contains candidate synthesis, not seven automatically adopted rules. The parent should combine these direct passages with separately reviewed blog/repository evidence and enforce the prompt's two-independent-source threshold.

## What remains to read

Two sources still need sequential completion from the ledger: Deep Dive into LLMs (7xTGNNLPyMI) and GPT-2 Reproduction (l8pRSuU81PU). Twelve spoken-source texts and three music-caption files now have complete preserved-text reviews. Original audiovisual material and linked code were not reviewed by this compilation.

Three music-caption files offer no substantial rule evidence. Their physical Markdown and metadata remain retained and linked instead of being counted as spoken lectures. The collection's two silent-upload exclusions remain outside these 15 files.

The complete Sequoia interview mirror was subsequently read sequentially through its closing29:33 segment. It adds explicit responsibility for software quality, a payment-to-user identity matching counterexample, caution about code bloat and model simplification limits, and discussion of wiki questions as a way to enhance understanding. Its recalled outsourcing sentence comes from an unspecified tweet and must not be treated as his original aphorism.

Continuation2026-10-08: GPT Tokenizer is now a complete preserved-text semantic review (3506 lines). Its page covers regex boundaries, special tokens, inference-versus-training, SentencePiece byte fallback and normalization, vocabulary tradeoffs, speculative research directions and dated failure demonstrations. Original media and linked implementation remain unreviewed.


## Continuation: micrograd fully read

The complete 4,259-line preserved micrograd transcript has now been read sequentially, including outtakes. [Source page](../../wiki/sources/karpathy/lectures/vmj-3s1tku0.md) adds numerical derivative checks, manual-to-automated backpropagation, equivalence checks against smaller tanh operations and PyTorch, progressive neuron/layer/MLP composition, target-linked loss and optimization, and a second bug: failing to zero gradients between steps allowed a tiny problem to converge despite incorrect semantics. Distinguish within-pass gradient accumulation from clearing gradients between optimization steps. Low loss alone does not establish correctness. All raw bytes remain unchanged. Across the 17 preserved source files, six are completely text-reviewed and eleven remain explicitly bounded.


## Continuation: WaveNet fully read

All 1,630 preserved lines of [Building makemore Part 5](../../wiki/sources/karpathy/lectures/t3yj5hkimq0.md) are now sequentially reviewed. Particularly useful independent method evidence: shape-aware scratch prototypes, equivalence checks before replacing explicit concatenation with reshape, a single training iteration after refactoring, a broadcasting bug that runs without doing the intended computation, parameter-count-controlled baseline comparison, and explicit uncertainty about statistical significance and architectural superiority without an experimental harness. This directly corroborates mechanism-first building and testing actual semantics, while opposing claims that deeper architecture is automatically better. Seven of 17 source files are completely text-reviewed; ten remain bounded.


## Continuation: introductory LLM talk fully read

All 1,785 preserved lines of [Intro to Large Language Models](../../wiki/sources/karpathy/lectures/zjkbmfhnj_g.md) are now sequentially reviewed. Adds empirical model evaluation, deployment-feedback iteration, tool use with explicit missing and imputed data, finite context as working memory, retrieval versus fine-tuning, and treating retrieved instructions as an attack surface. Historical model rankings, unavailable-reasoning claims and security demonstrations remain dated. Eight of 17 files are completely text-reviewed; nine remain explicitly bounded.


Continuation 2026-10-08: MLP Part 2 (2222 lines), Activations and Gradients (3123), No Priors (227 long lines), and Makemore Introduction (3420) are fully read and compiled with exact raw-caption quotation support beside each synthesis paragraph. No Priors distinguishes verifiable autonomous work from jagged failures and metric overfitting. Makemore explicitly checks seeded output and row normalization after vectorization, then demonstrates the silent keepdim broadcasting bug; this supports execution checks beyond whether code runs. The remaining five sources are not yet complete.


Continuation 2026-10-08: Backprop Ninja is fully read (3152 lines). Its quoted compilation records deliberately nonzero test initialization, failed incomplete-branch checks, scalar examples before tensor formulas, fused expressions checked against the atomic derivation, and short-run reference checks before removing autograd. Four long spoken sources remain incomplete.


Continuation 2026-10-08: Build GPT (3064 lines) and How I Use LLMs (3557) are fully read and compiled. The former verifies efficient aggregation against a simple reference before extending the architecture; the latter checks cited sources, generated code, missing-data assumptions, actual numeric outputs and transcribed image values. Exact quote-supported source pages distinguish dated product observations and personal health examples from current operational or medical advice. Two texts remain incomplete.
