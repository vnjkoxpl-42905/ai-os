---
type: source
subject: "GitHub source repos/karpathy/llm.c/dev/eval/README.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/eval/README.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/llm.c/dev/eval/README.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/eval/README.md), SHA-256 `582293f5dc0c314670b9bb6884b2c0ccbe87aba675469aad7b9434185a51117a`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "# eleuther eval readme The goal here is to run the Eleuther Eval harness exactly".

The council frontend README is an unchanged React/Vite template voice, not personal Karpathy opinion. Llm.c CUDA development begins with a naive kernel, compares CPU reference outputs on GPU, times launch configurations, then substitutes a measured faster kernel; documented complexity and runtime tradeoffs are explicit. Data scripts own per-dataset cache directories and share helpers. The evaluation README pins a harness version for comparability and admits unresolved bfloat16 scoring and unexpectedly expensive runtime issues instead of hiding them. The root llm.c README keeps simple frozen CPU/fp32 references alongside fast production-oriented kernels, cross-checks logits/loss/training trajectories against PyTorch, supplies a stepwise layernorm tutorial, and distinguishes platform-specific distributed launch options without declaring one universally superior. It explicitly may reject 2-percent performance for 500 lines and an exotic dependency, while accepting a standard one-line library call. These are project constraints rather than universal bans on dependency use.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

````text
# eleuther eval readme

The goal here is to run the Eleuther Eval harness exactly in the same way as that used in the [huggingface LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard).

The starting point is a `.bin` file trained by llm.c. We now have to export it to a huggingface model and then evaluate it.

To export the model, use [export_hf.py](export_hf.py). See its documentation up top. Eample usage, from this directory:

```bash
cd dev/eval
python export_hf.py --input model.bin --output output_dir
```

Where you point to your model .bin file, and huggingface files get written to output_dir. The script can optionally also upload to huggingface hub. One more post-processing that is advisable is to go into the `output_dir`, open up the `config.json` there and add one more entry into the json object:

```
"_attn_implementation": "flash_attention_2"
```

To use FlashAttention 2. We had trouble evaluating in bfloat16 without using FlashAttention 2 (the scores are much lower, and this was never fully resolved). This is a temporary hack/workaround.

Now that we have the model in huggingface format, we download the Eleuther Eval Harness repo and run it. Head over to the parent/root directory of the llm.c repo and:

```bash
git clone https://github.com/EleutherAI/lm-evaluation-harness/
cd lm-evaluation-harness
git checkout b281b0921b636bc36ad05c0b0b0763bd6dd43463
pip install -e .
```

And then run the run_eval.sh script:

```bash
./dev/eval/run_eval.sh output_dir result_dir
```

Where output_dir can either be local output dir (above), or a huggingface repo name.This will write eval json objects to `./lm-evaluation-harness/results/results_dir`. It will print the results into console, e.g. for a 774M model we see:

```
----------------------------------------
arc_challenge_25shot.json      : 30.4608
gsm8k_5shot.json               : 0.1516
hellaswag_10shot.json          : 57.8072
mmlu_5shot.json                : 25.8682
truthfulqa_0shot.json          : 35.7830
winogrande_5shot.json          : 59.3528
----------------------------------------
Average Score                  : 34.9039
```

But you can additionally get these results later by running `summarize_eval.py`:

```bash
python dev/eval/summarize_eval.py lm-evaluation-harness/results/results_dir
```

The same information will be printed again.

For some reason, the evaluation is quite expensive and runs for somewhere around 1-3 hours, even though it should be a few minutes at most. This has not been satisfyingly resolved so far.
````

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
