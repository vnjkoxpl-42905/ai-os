---
type: source
subject: "GitHub source repos/karpathy/neuraltalk2/cv/README.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk2/cv/README.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/neuraltalk2/cv/README.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk2/cv/README.md), SHA-256 `dd20f963a7bebb462c44c2ed55d4872a08d84270d48a82a397ad36df09d4db51`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
## Cross-validation utilities ### Starting workers on different GPUs I thought I should do a
```

Neuraltalk documentation separates feature extraction, model inference and HTML visualization, warns on distribution mismatch, and uses log probabilities as a rough confusion indicator rather than guaranteed truth. Its architecture separates dataset APIs, batching, optimizers and generator modules. The root explicitly deprecates the NumPy code in favor of GPU-batched Neuraltalk2 and restricts tested-platform claims to Ubuntu; an unresolved Python-versus-Matlab feature-reproduction issue remains visible. Matlab/Python feature reference docs point to Caffe and VGG third-party models and describe starter code rather than a ready utility. Status and checkpoint folders are operational outputs. Neuraltalk2 cross-validation tools isolate each worker GPU, give runs distinct IDs, write checkpoints to shared storage and inspect outcomes in notebooks before changing search ranges; the notebook is explicitly hacky. Documented infinite worker loops were read, not executed.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

````text

## Cross-validation utilities

### Starting workers on different GPUs

I thought I should do a small code dump of my cross-validation utilities. My workflow is to run on a single machine with multiple GPUs. Each worker runs on one GPU, and I spawn workers with the `spawn.sh` script, e.g.:

```bash
$ ./spawn 0 1 2 3 4 5 6
```

spawns 7 workers using GPUs 0-6 (inclusive), all running in screen sessions `ak0`...`ak6`. E.g. to attach to one of these it would be `screen -r ak0`. And `CTRL+a, d` to detach from a screen session and `CTRL+a, k, y` to kill a worker. Also `./killall.sh` to kill all workers.

You can see that `spawn.sh` calls `runworker.sh` in a screen session. The runworker script can modify the paths (since LD_LIBRARY_PATH does not trasfer to inside screen sessions), and calls `driver.py`.

Finally, `driver.py` runs an infinite loop of actually calling the training script, and this is where I set up all the cross-validation ranges. Also note, very importantly, how the `train.lua` script is called, with 

```python
cmd = 'CUDA_VISIBLE_DEVICES=%d th train.lua ' % (gpuid, )
```

this is because otherwise Torch allocates a lot of memory on all GPUs on a single machine because it wants to support multigpu setups, but if you're only training on a single GPU you really want to use this flag to *hide* the other GPUs from each worker.

Also note that I'm using the field `opt.id` to assign a unique identifier to each worker, based on the GPU it's running on and some random number, and current time, to distinguish each run.

Have a look through my `driver.py` to get a sense of what it's doing. In my workflow I keep modifying this script and killing workers whenever I want to tune some of the cross-validation ranges.

### Playing with checkpoints that get written to files

Finally, the IPython Notebook `inspect_cv.ipynb` gives you an idea about how I analyze the checkpoints that get written out by the workers. The notebook is *super-hacky* and not intended for plug and play use; I'm only putting it up in case this is useful to anyone to build on, and to get a sense for the kinds of analysis you might want to play with.

### Conclusion

Overall, this system works quite well for me. My cluster machines run workers in screen sessions, these write checkpoints to a shared file system, and then I use notebooks to look at what hyperparameter ranges work well. Whatever works well I encode into `driver.py`, and then I restart the workers and iterate until things work well :) Hope some of this is useful & Good luck!
````

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
