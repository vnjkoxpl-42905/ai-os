# llm.c authored-source semantic coverage

Updated 2026-10-08. This separate ledger owns 94 files excluded from the repo agent's remaining selector; eight previously full-read files stay in its ledger.

Complete model reads and physical source pages: 76. Unread: 18. All source hashes were verified against the capture manifest before compilation. No source code was executed.

## Observations supported by fully read sources

The training launch recipes make architecture, data paths, batch size, scheduling and stopping conditions explicit. CUDA recipes use a completion marker and resume loop, while the Python recipe supplies a comparable PyTorch launcher. Timing and cost comments are historical estimates, not local measurements.

This is compilation coverage, not a claim that the repository has been tested or that source recipes should be executed in Joshua's environment. No persona rule is derived solely from these launch files.

## Teaching and engineering evidence without new persona rules

The [layer-normalization tutorial](../../wiki/sources/karpathy/repos/llmc/doc--layernorm--layernorm-md.md) explicitly calls manual operations "algorithmically instructive" and explains a "tradeoff between memory and compute". Its actual sequence is equations, PyTorch primitives, manual gradients, autograd comparison, memory indexing and C translation. The [Python reference](../../wiki/sources/karpathy/repos/llmc/doc--layernorm--layernorm-py.md) and [C companion](../../wiki/sources/karpathy/repos/llmc/doc--layernorm--layernorm-c.md) instantiate the comparison. These are related files in one tutorial, not independent authored sources for promoting a two-source personal rule.

The [encoder](../../wiki/sources/karpathy/repos/llmc/llmc--encoder-cuh.md) explicitly preprocesses inputs into CPU "buckets" to control reduction order; [CUDA utilities](../../wiki/sources/karpathy/repos/llmc/llmc--cuda-utils-cuh.md) limit deterministic global reduction to a "single block". These mechanisms show implementation choices around determinism, not an independently tested guarantee.

Source-level limitations remain visible: the [loss checker](../../wiki/sources/karpathy/repos/llmc/dev--loss-checker-ci-py.md) does not require ten extracted rows, the [C layernorm checker](../../wiki/sources/karpathy/repos/llmc/doc--layernorm--layernorm-c.md) ignores comparison return flags, and the [CPU matmul comparator](../../wiki/sources/karpathy/repos/llmc/dev--cpu--matmul-forward-c.md) uses the captured threshold `tolerance + fabs(cpu_reference[i])`. These prevent equating configured tests with production acceptance. No raw code was changed.

## Source pages

- [.github/workflows/ci.yml](../../wiki/sources/karpathy/repos/llmc/-github--workflows--ci-yml.md)
- [.github/workflows/ci_gpu.yml](../../wiki/sources/karpathy/repos/llmc/-github--workflows--ci-gpu-yml.md)
- [.github/workflows/ci_tests.yml](../../wiki/sources/karpathy/repos/llmc/-github--workflows--ci-tests-yml.md)
- [Makefile](../../wiki/sources/karpathy/repos/llmc/Makefile.md)
- [dev/cpu/matmul_forward.c](../../wiki/sources/karpathy/repos/llmc/dev--cpu--matmul-forward-c.md)
- [dev/cuda/Makefile](../../wiki/sources/karpathy/repos/llmc/dev--cuda--Makefile.md)
- [dev/cuda/adamw.cu](../../wiki/sources/karpathy/repos/llmc/dev--cuda--adamw-cu.md)
- [dev/cuda/benchmark_on_modal.py](../../wiki/sources/karpathy/repos/llmc/dev--cuda--benchmark-on-modal-py.md)
- [dev/cuda/crossentropy_forward.cu](../../wiki/sources/karpathy/repos/llmc/dev--cuda--crossentropy-forward-cu.md)
- [dev/cuda/crossentropy_softmax_backward.cu](../../wiki/sources/karpathy/repos/llmc/dev--cuda--crossentropy-softmax-backward-cu.md)
- [dev/cuda/encoder_backward.cu](../../wiki/sources/karpathy/repos/llmc/dev--cuda--encoder-backward-cu.md)
- [dev/cuda/encoder_forward.cu](../../wiki/sources/karpathy/repos/llmc/dev--cuda--encoder-forward-cu.md)
- [dev/cuda/gelu_backward.cu](../../wiki/sources/karpathy/repos/llmc/dev--cuda--gelu-backward-cu.md)
- [dev/cuda/gelu_forward.cu](../../wiki/sources/karpathy/repos/llmc/dev--cuda--gelu-forward-cu.md)
- [dev/cuda/global_norm.cu](../../wiki/sources/karpathy/repos/llmc/dev--cuda--global-norm-cu.md)
- [dev/cuda/matmul_backward.cu](../../wiki/sources/karpathy/repos/llmc/dev--cuda--matmul-backward-cu.md)
- [dev/cuda/nccl_all_reduce.cu](../../wiki/sources/karpathy/repos/llmc/dev--cuda--nccl-all-reduce-cu.md)
- [dev/cuda/permute.cu](../../wiki/sources/karpathy/repos/llmc/dev--cuda--permute-cu.md)
- [dev/cuda/residual_forward.cu](../../wiki/sources/karpathy/repos/llmc/dev--cuda--residual-forward-cu.md)
- [dev/data/data_common.py](../../wiki/sources/karpathy/repos/llmc/dev--data--data-common-py.md)
- [dev/data/edu_fineweb.sh](../../wiki/sources/karpathy/repos/llmc/dev--data--edu-fineweb-sh.md)
- [dev/data/fineweb.py](../../wiki/sources/karpathy/repos/llmc/dev--data--fineweb-py.md)
- [dev/data/fineweb.sh](../../wiki/sources/karpathy/repos/llmc/dev--data--fineweb-sh.md)
- [dev/data/hellaswag.py](../../wiki/sources/karpathy/repos/llmc/dev--data--hellaswag-py.md)
- [dev/data/mmlu.py](../../wiki/sources/karpathy/repos/llmc/dev--data--mmlu-py.md)
- [dev/data/tinyshakespeare.py](../../wiki/sources/karpathy/repos/llmc/dev--data--tinyshakespeare-py.md)
- [dev/data/tinystories.py](../../wiki/sources/karpathy/repos/llmc/dev--data--tinystories-py.md)
- [dev/download_starter_pack.sh](../../wiki/sources/karpathy/repos/llmc/dev--download-starter-pack-sh.md)
- [dev/eval/export_hf.py](../../wiki/sources/karpathy/repos/llmc/dev--eval--export-hf-py.md)
- [dev/eval/run_eval.sh](../../wiki/sources/karpathy/repos/llmc/dev--eval--run-eval-sh.md)
- [dev/eval/summarize_eval.py](../../wiki/sources/karpathy/repos/llmc/dev--eval--summarize-eval-py.md)
- [dev/loss_checker_ci.py](../../wiki/sources/karpathy/repos/llmc/dev--loss-checker-ci-py.md)
- [dev/test/Makefile](../../wiki/sources/karpathy/repos/llmc/dev--test--Makefile.md)
- [dev/test/device_file_io.cu](../../wiki/sources/karpathy/repos/llmc/dev--test--device-file-io-cu.md)
- [dev/test/test_outlier_detector.c](../../wiki/sources/karpathy/repos/llmc/dev--test--test-outlier-detector-c.md)
- [dev/unistd.h](../../wiki/sources/karpathy/repos/llmc/dev--unistd-h.md)
- [dev/vislog.ipynb](../../wiki/sources/karpathy/repos/llmc/dev--vislog-ipynb.md)
- [doc/layernorm/layernorm.c](../../wiki/sources/karpathy/repos/llmc/doc--layernorm--layernorm-c.md)
- [doc/layernorm/layernorm.md](../../wiki/sources/karpathy/repos/llmc/doc--layernorm--layernorm-md.md)
- [doc/layernorm/layernorm.py](../../wiki/sources/karpathy/repos/llmc/doc--layernorm--layernorm-py.md)
- [llmc/adamw.cuh](../../wiki/sources/karpathy/repos/llmc/llmc--adamw-cuh.md)
- [llmc/attention.cuh](../../wiki/sources/karpathy/repos/llmc/llmc--attention-cuh.md)
- [llmc/cublas_common.h](../../wiki/sources/karpathy/repos/llmc/llmc--cublas-common-h.md)
- [llmc/cuda_common.h](../../wiki/sources/karpathy/repos/llmc/llmc--cuda-common-h.md)
- [llmc/cuda_utils.cuh](../../wiki/sources/karpathy/repos/llmc/llmc--cuda-utils-cuh.md)
- [llmc/cudnn_att.cpp](../../wiki/sources/karpathy/repos/llmc/llmc--cudnn-att-cpp.md)
- [llmc/cudnn_att.h](../../wiki/sources/karpathy/repos/llmc/llmc--cudnn-att-h.md)
- [llmc/dataloader.h](../../wiki/sources/karpathy/repos/llmc/llmc--dataloader-h.md)
- [llmc/encoder.cuh](../../wiki/sources/karpathy/repos/llmc/llmc--encoder-cuh.md)
- [llmc/fused_classifier.cuh](../../wiki/sources/karpathy/repos/llmc/llmc--fused-classifier-cuh.md)
- [llmc/gelu.cuh](../../wiki/sources/karpathy/repos/llmc/llmc--gelu-cuh.md)
- [llmc/global_norm.cuh](../../wiki/sources/karpathy/repos/llmc/llmc--global-norm-cuh.md)
- [llmc/layernorm.cuh](../../wiki/sources/karpathy/repos/llmc/llmc--layernorm-cuh.md)
- [llmc/logger.h](../../wiki/sources/karpathy/repos/llmc/llmc--logger-h.md)
- [llmc/matmul.cuh](../../wiki/sources/karpathy/repos/llmc/llmc--matmul-cuh.md)
- [llmc/mfu.h](../../wiki/sources/karpathy/repos/llmc/llmc--mfu-h.md)
- [llmc/outlier_detector.h](../../wiki/sources/karpathy/repos/llmc/llmc--outlier-detector-h.md)
- [llmc/rand.h](../../wiki/sources/karpathy/repos/llmc/llmc--rand-h.md)
- [llmc/sampler.h](../../wiki/sources/karpathy/repos/llmc/llmc--sampler-h.md)
- [llmc/schedulers.h](../../wiki/sources/karpathy/repos/llmc/llmc--schedulers-h.md)
- [llmc/tokenizer.h](../../wiki/sources/karpathy/repos/llmc/llmc--tokenizer-h.md)
- [llmc/utils.h](../../wiki/sources/karpathy/repos/llmc/llmc--utils-h.md)
- [llmc/zero.cuh](../../wiki/sources/karpathy/repos/llmc/llmc--zero-cuh.md)
- [profile_gpt2.cu](../../wiki/sources/karpathy/repos/llmc/profile-gpt2-cu.md)
- [profile_gpt2cu.py](../../wiki/sources/karpathy/repos/llmc/profile-gpt2cu-py.md)
- [scripts/multi_node/run_gpt2_124M_fs.sbatch](../../wiki/sources/karpathy/repos/llmc/scripts--multi-node--run-gpt2-124M-fs-sbatch.md)
- [scripts/multi_node/run_gpt2_124M_mpi.sh](../../wiki/sources/karpathy/repos/llmc/scripts--multi-node--run-gpt2-124M-mpi-sh.md)
- [scripts/multi_node/run_gpt2_124M_tcp.sbatch](../../wiki/sources/karpathy/repos/llmc/scripts--multi-node--run-gpt2-124M-tcp-sbatch.md)
- [scripts/pyrun_gpt2_124M.sh](../../wiki/sources/karpathy/repos/llmc/scripts--pyrun-gpt2-124M-sh.md)
- [scripts/run_gpt2_124M.sh](../../wiki/sources/karpathy/repos/llmc/scripts--run-gpt2-124M-sh.md)
- [scripts/run_gpt2_1558M.sh](../../wiki/sources/karpathy/repos/llmc/scripts--run-gpt2-1558M-sh.md)
- [scripts/run_gpt2_350M.sh](../../wiki/sources/karpathy/repos/llmc/scripts--run-gpt2-350M-sh.md)
- [scripts/run_gpt2_774M.sh](../../wiki/sources/karpathy/repos/llmc/scripts--run-gpt2-774M-sh.md)
- [scripts/run_gpt3_125M.sh](../../wiki/sources/karpathy/repos/llmc/scripts--run-gpt3-125M-sh.md)
- [test_gpt2.c](../../wiki/sources/karpathy/repos/llmc/test-gpt2-c.md)
- [test_gpt2_fp32.cu](../../wiki/sources/karpathy/repos/llmc/test-gpt2-fp32-cu.md)
