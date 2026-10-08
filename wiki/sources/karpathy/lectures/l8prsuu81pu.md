---
type: source
subject: "Karpathy video l8pRSuU81PU"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, youtube]
sources: ["../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/l8pRSuU81PU.md"]
semantic-status: complete-preserved-text-no-media-review
---

# Let's reproduce GPT-2 (124M)

Original: [l8pRSuU81PU](https://www.youtube.com/watch?v=l8pRSuU81PU); channel Andrej Karpathy. Upload date 2024-06-09. Captured2026-10-08, compilation2026-10-08. Automatic English captions, not verified against audio.

[Physical raw Markdown](../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/l8pRSuU81PU.md). SHA-256: `47f139585778df18bfa379799038062320cbad808e38fb55d56609c07d15d94b`. Physical byte hash differs from the older manifest. CRLF-to-LF normalized SHA-256 matches its hash `432a3702b8dce00bbc073e70c30ee5fc2519bc8426ed267846b9656926d9d499` exactly. Raw bytes were preserved; normalized matching does not make the physical byte hashes identical.

## Reviewed evidence

He starts with the reproduction target and reference checkpoint, implements a compact GPT-2 class, then verifies that the released weights can be loaded and generate coherent completions. This establishes the model family before training new weights.

> [00:12:50] want to write this from scratch
> [00:12:51] ourselves so we're going to be
> [00:12:53] implementing the GPT model here in
> [00:12:54] parallel and as our first task let's
> [00:12:57] load the gpt2 124 M into the class that
> [00:13:01] we're going to develop here from scratch

The architecture explanation separates attention communication from per-token MLP computation and uses a clean pre-normalized residual path for optimization. Exact reproduction retains the historical approximate GELU rather than silently substituting a newer choice.

> [00:19:53] communication operation it is where all
> [00:19:55] the tokens and there's 1,24 tokens lined
> [00:19:58] up in a sequence and this is where the
> [00:20:00] tokens communicate this is where they
> [00:20:02] exchange information so attention is a
> [00:20:06] um aggregation function it's a pooling

When generated text differs from the high-level Transformers pipeline, he checks equivalent lower-level sampling on both implementations. He reports that the pipeline discrepancy remains unexplained, rather than claiming every interface matches.

> [00:40:26] just like blabber on right in all these
> [00:40:27] cases now one thing you will notice is
> [00:40:29] that these Generations are not the
> [00:40:31] generations of hugging face here and I
> [00:40:35] can't find the discrepancy to be honest
> [00:40:37] and I didn't fully go through all these

He begins training with a tiny Shakespeare batch and checks the expected uniform-token cross-entropy scale. The point is a small debugging baseline before introducing the real corpus and distributed run.

> [00:55:27] covered this in previous videos but our
> [00:55:29] vocabulary size is
> [00:55:31] 50257 at initialization of the network
> [00:55:34] you would hope that um every vocab
> [00:55:37] element is getting roughly a uniform
> [00:55:40] probability uh so that we're not

He catches the CPU/CUDA data mismatch and explains that a tensor device conversion returns a new tensor. Once fixed, he checks that the model can overfit one batch before moving to fresh batches.

> [01:00:26] device um it's not stateful it doesn't
> [01:00:30] convert it to be a device it instead uh
> [01:00:33] returns pointer to a new memory which is
> [01:00:35] on the device so you see how we can just
> [01:00:37] do model that two a device that does not
> [01:00:39] apply to tensors you have to do buff

He discovers that loading equal-valued tensors missed GPT-2 weight tying: the input embedding and output classifier must share storage. He checks data pointers, traces the original implementation, and joins both gradient contributions.

> [01:07:21] that to 50, 257 to get the Lis for the
> [01:07:24] next token so they're both the same
> [01:07:27] shape but more than that actually if you
> [01:07:29] look at um comparing their elements um
> [01:07:33] in pytorch this is an element wise
> [01:07:35] equality so then we use do all and we

Initialization follows released code where the paper is vague, with a residual-depth scale motivated by a simple variance-growth experiment. He explicitly retains approximations and double-initialization quirks rather than presenting the reproduction as perfectly faithful in every detail.

> [01:17:20] caveat here so
> [01:17:23] here a mod initialization which accounts
> [01:17:26] for the accumulation on the residual
> [01:17:27] path with model depth is used we scale
> [01:17:30] the weight of residual layers of
> [01:17:31] initialization by factor of one over squ

Performance work follows a working model. He inspects the actual A100 hardware, records a baseline, synchronizes the GPU before timing, and measures tokens per second. Published peak arithmetic speed does not equal end-to-end speed when memory traffic dominates.

> [01:33:54] actually the GPU is still running
> [01:33:56] because it takes it time to actually
> [01:33:57] work through the work that was scheduled
> [01:34:00] to run and so you're just building up a
> [01:34:03] queue for the GPU and so actually if you
> [01:34:05] need to you want to wait toat data

He trades precision for measured throughput using TF32 and BF16 autocast, distinguishes range from mantissa precision, and acknowledges uncertainty about exactly which operations autocast converts. These hardware and PyTorch capability statements describe the lecture environment.

> [01:47:19] know exactly what's in B flat 16 what's
> [01:47:22] in float 32
> [01:47:23] we could go in and we could start to
> [01:47:24] scrutinize it um but these are the kinds
> [01:47:27] of rules that pytorch has internally and
> [01:47:29] unfortunately they don't documented very

He explains torch.compile through reduced Python overhead and fewer memory round trips. A pointwise GELU example illustrates kernel fusion; streaming chunks through on-chip memory is the mechanism, not merely reducing arithmetic.

> [01:59:01] picture of what's Happening Here is that
> [01:59:03] we take these inputs which live by
> [01:59:05] default on the global memory and now we
> [01:59:08] need to perform some calculation so we
> [01:59:10] start streaming the data from the um
> [01:59:12] Global memory to the uh chip we perform

FlashAttention illustrates an algorithmic rewrite beyond compiler pointwise fusion: avoid materializing the large attention matrix with an online softmax. He checks that the optimization still reaches approximately the same loss while becoming faster.

> [02:05:46] to use this compound up and uh let's
> [02:05:49] wait for a few moments before torch comp
> [02:05:51] compile gets around to it and then let's
> [02:05:53] remember that we achieved 6.05 661 I
> [02:05:58] have it here that's the loss we were
> [02:06:00] expecting to see and we took 130

Padding vocabulary size to a hardware-friendly multiple performs more arithmetic yet runs faster in his measurement. He checks the unused rows and extra classifier probabilities and identifies boundary-kernel costs; the size of the gain depends on the PyTorch version.

> [02:10:57] used so we swing up to the inet and we
> [02:11:00] see that it's used inside the embedding
> [02:11:01] table of course so all the way at the
> [02:11:03] bottom of the Transformer and it's used
> [02:11:05] at the classifier layer all the way at
> [02:11:06] the top of the Transformer so in two

He borrows GPT-3 optimizer details because GPT-2 training documentation is sparse, adding gradient clipping, warmup/cosine decay, and decay groups. He explicitly skips batch-size ramping and does not exactly reproduce the GPT-3 decay horizon. The relationships among these settings are described as a deeper topic.

> [02:34:18] the Epsilon and so on these are very
> [02:34:20] complicated uh mathematical
> [02:34:22] relationships in the optimization
> [02:34:24] literature and um for the most part I'm
> [02:34:27] in this video I'm just trying to copy
> [02:34:29] paste the settings that open AI used but

Gradient accumulation is verified against a toy batched regression calculation. The first implementation is wrong because summing microbatch means loses the global mean normalizer; dividing by accumulation steps restores matching gradients.

> [02:42:22] just a mean squ error um which in this
> [02:42:25] case because there's only a single
> [02:42:26] example is just this term here so that
> [02:42:28] was the loss in the zeroth eration same
> [02:42:30] in the first third and so on and then
> [02:42:33] when you do the loss. backward we're

For distributed training he reasons about eight concurrent interpreters, rank-specific data, averaged gradients, and master-only logging. He avoids per-microstep synchronization, but explicitly calls directly toggling a DDP internal variable fragile.

> [03:04:20] then basically we only want to
> [03:04:23] synchronize we only want this variable
> [03:04:25] to be true when it is the final
> [03:04:28] iteration in all the other iterations
> [03:04:31] inside the micr steps we want to be
> [03:04:33] false so I just toggle it like this so

He investigates differing single-GPU versus multi-GPU numbers through data-loader boundary effects and verifies a smaller setting where the values match. A run succeeding is not his only check.

> [03:09:29] GPU and the H GPU process will end up um
> [03:09:33] resetting in a slightly different Manner
> [03:09:35] and so our batches are slightly
> [03:09:36] different and so we get slightly
> [03:09:38] different numbers but one way to
> [03:09:39] convince yourself that this is okay it

The real training corpus is a 10B-token FineWeb-Edu sample, pretokenized into shards with a held-out validation shard. He fixes an integer-division preprocessing error and upgrades the loader, then adds validation and samples before the serious run.

> [03:17:26] sharting it is just kind of um nicer
> [03:17:28] from that
> [03:17:30] perspective and uh yeah so we'll just
> [03:17:32] let this run this will be probably um
> [03:17:36] 30ish minutes or so and then we're going
> [03:17:38] to come back to actually train on this

He separates the sampling RNG from the training RNG. When torch.compile breaks generation and evaluation, he disables it for those paths, records the unresolved problem, and points to incremental Git history rather than hiding the failure.

> [03:27:37] compile my model I get a really scary
> [03:27:39] error from pytorch and I have no idea
> [03:27:41] how to resolve it right now so probably
> [03:27:43] by the time you see this code released
> [03:27:45] or something like that maybe it's fixed
> [03:27:47] but for now I'm just going to do end

HellaSwag is evaluated in a form the small model can perform: completion losses with masks rather than assuming it understands multiple-choice labels. He reports discrepancies with an external evaluation harness as unresolved.

> [03:37:42] more thing called Uther harness which is
> [03:37:44] a very piece of infrastructure for
> [03:37:46] running evals for language models and
> [03:37:48] they get slightly different numbers and
> [03:37:50] I'm not 100% sure what the discrepancy
> [03:37:52] is for these um it could be that they

He compares validation loss and HellaSwag against reference checkpoints, but warns that different data distributions and possible evaluation contamination limit the result. His suspected data-order periodicity is a hypothesis, not a confirmed diagnosis.

> [03:46:11] looking at the training curve instead of
> [03:46:12] the validation curve so long story short
> [03:46:15] this is not a perfect eval and there's
> [03:46:16] some caveats here uh but at least we
> [03:46:19] have some confidence that that we're not
> [03:46:20] doing something completely wrong and

Longer training improves the measured score, but he proposes shuffling documents and shards across epochs to avoid repeated accidental ordering. More thorough evaluation across math, code, and languages is still needed before broad capability conclusions.

> [03:50:03] want to look into extensions where you
> [03:50:05] actually permute the data uh randomly
> [03:50:08] you permute the documents around in
> [03:50:10] Every Single Shard on every single new
> [03:50:12] Epoch um and po even permute the
> [03:50:16] shards and that would go a long way into

A saved model checkpoint is different from exact training resumption: the latter also needs optimizer moments and RNG state. Pretraining yields a document continuer; chat behaviour would require a separate conversational fine-tuning stage, which the lecture does not implement.

> [03:53:48] yourself one more thing I added to The
> [03:53:50] Code by the way is this chunk of code
> [03:53:52] here so basically right after we
> [03:53:54] evaluate the validation loss if we are
> [03:53:56] the master process in addition to
> [03:53:58] logging the validation loss every 5,000

He compares a specialized C/CUDA implementation with its PyTorch reference and aligns losses and gradient norms before discussing speed. This does not prove every general-framework configuration is optimally tuned.

> [03:58:49] step and so P started to Stepping here
> [03:58:53] and as you can see we're running at
> [03:58:54] about 223,000 tokens per second here and
> [03:58:57] about 185,000 tokens per second here um
> [03:59:03] so quite a bit slower but I don't have
> [03:59:05] full confidence that I exactly squeezed

He closes with explicit remaining issues: data periodicity, compiler failures in generation/evaluation, and epoch permutation. The source is a demonstrated engineering progression with known limitations, not an assertion of a perfect final system.

> [03:59:46] ground and we built everything from
> [03:59:48] scratch so as a brief summary we were
> [03:59:50] looking at the gpt2 and GPT 3
> [03:59:55] papers we were looking at how you set up
> [03:59:57] these training runs uh and all the
> [03:59:59] considerations involved we wrote

## Exact excerpts for cross-source rule checks

> [02:43:28] equivalent so when I run this you see

> [02:43:32] that the U gradients are now identical

> [00:40:56] and if I do this and I run that then I

> [00:40:59] am getting the same results so basically

> [00:41:03] the model internals are not wrong it's

> [03:46:12] the validation curve so long story short

> [03:46:15] this is not a perfect eval and there's

> [03:46:16] some caveats here uh but at least we

## Coverage and interpretation

Status: **complete-preserved-text-no-media-review**. Sequentially reviewed every preserved transcript line, 1-6149. Audio and video were not reviewed, so missing or miscaptioned speech remains unknown.

The quoted passages support local teaching/building methods only within their stated scope. Captions contain recognition errors; quotations preserve those errors rather than silently correcting them. No linked code, papers, diagrams or media was independently executed or inspected. Source upload dates do not establish current tool capabilities.

Related: [Karpathy index](../../../karpathy/index.md), [principles](../../../karpathy/principles.md), [methods](../../../karpathy/methods.md).
