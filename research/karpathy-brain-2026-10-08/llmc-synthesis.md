# llm.c authored-source semantic coverage

Updated 2026-10-08. This separate ledger owns 94 files excluded from the repo agent's remaining selector; eight previously full-read files stay in its ledger.

Complete model reads and physical source pages: 14. Unread: 80. All source hashes were verified against the capture manifest before compilation. No source code was executed.

## Observations supported by fully read sources

The training launch recipes make architecture, data paths, batch size, scheduling and stopping conditions explicit. CUDA recipes use a completion marker and resume loop, while the Python recipe supplies a comparable PyTorch launcher. Timing and cost comments are historical estimates, not local measurements.

This is compilation coverage, not a claim that the repository has been tested or that source recipes should be executed in Joshua's environment. No persona rule is derived solely from these launch files.

## Source pages

- [dev/data/edu_fineweb.sh](../../wiki/sources/karpathy/repos/llmc/dev--data--edu-fineweb-sh.md)
- [dev/data/fineweb.sh](../../wiki/sources/karpathy/repos/llmc/dev--data--fineweb-sh.md)
- [dev/download_starter_pack.sh](../../wiki/sources/karpathy/repos/llmc/dev--download-starter-pack-sh.md)
- [dev/eval/summarize_eval.py](../../wiki/sources/karpathy/repos/llmc/dev--eval--summarize-eval-py.md)
- [dev/loss_checker_ci.py](../../wiki/sources/karpathy/repos/llmc/dev--loss-checker-ci-py.md)
- [scripts/multi_node/run_gpt2_124M_fs.sbatch](../../wiki/sources/karpathy/repos/llmc/scripts--multi-node--run-gpt2-124M-fs-sbatch.md)
- [scripts/multi_node/run_gpt2_124M_mpi.sh](../../wiki/sources/karpathy/repos/llmc/scripts--multi-node--run-gpt2-124M-mpi-sh.md)
- [scripts/multi_node/run_gpt2_124M_tcp.sbatch](../../wiki/sources/karpathy/repos/llmc/scripts--multi-node--run-gpt2-124M-tcp-sbatch.md)
- [scripts/pyrun_gpt2_124M.sh](../../wiki/sources/karpathy/repos/llmc/scripts--pyrun-gpt2-124M-sh.md)
- [scripts/run_gpt2_124M.sh](../../wiki/sources/karpathy/repos/llmc/scripts--run-gpt2-124M-sh.md)
- [scripts/run_gpt2_1558M.sh](../../wiki/sources/karpathy/repos/llmc/scripts--run-gpt2-1558M-sh.md)
- [scripts/run_gpt2_350M.sh](../../wiki/sources/karpathy/repos/llmc/scripts--run-gpt2-350M-sh.md)
- [scripts/run_gpt2_774M.sh](../../wiki/sources/karpathy/repos/llmc/scripts--run-gpt2-774M-sh.md)
- [scripts/run_gpt3_125M.sh](../../wiki/sources/karpathy/repos/llmc/scripts--run-gpt3-125M-sh.md)
