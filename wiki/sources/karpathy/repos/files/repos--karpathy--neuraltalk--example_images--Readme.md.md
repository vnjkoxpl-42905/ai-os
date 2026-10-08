---
type: source
subject: "GitHub source repos/karpathy/neuraltalk/example_images/Readme.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/example_images/Readme.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/neuraltalk/example_images/Readme.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/example_images/Readme.md), SHA-256 `b7ddb794008eb8658e748ffdb897cb84f45ef685f79e0c0eabaabfaf401b2d1f`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "Here we explain how the framework can be used to predict sentences for arbitrary images.".

Neuraltalk documentation separates feature extraction, model inference and HTML visualization, warns on distribution mismatch, and uses log probabilities as a rough confusion indicator rather than guaranteed truth. Its architecture separates dataset APIs, batching, optimizers and generator modules. The root explicitly deprecates the NumPy code in favor of GPU-batched Neuraltalk2 and restricts tested-platform claims to Ubuntu; an unresolved Python-versus-Matlab feature-reproduction issue remains visible. Matlab/Python feature reference docs point to Caffe and VGG third-party models and describe starter code rather than a ready utility. Status and checkpoint folders are operational outputs. Neuraltalk2 cross-validation tools isolate each worker GPU, give runs distinct IDs, write checkpoints to shared storage and inspect outcomes in notebooks before changing search ranges; the notebook is explicitly hacky. Documented infinite worker loops were read, not executed.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
Here we explain how the framework can be used to predict sentences for arbitrary images.

1. Copy all images you want to predict for to one folder. For example, this folder contains multiple, collected from Reddit's r/photoshopbattles.
2. Extract the CNN features for all images with the Matlab script provided in `matlab_features_reference`, and as described with the Readme file in that folder. I want to eventually allow people to extract features with Python but for now it is needed to go through Matlab. The Matlab script needs to be pointed to a file `tasks.txt` that you should create in the same folder. I show the example in this folder as well: It lists the images that you wish to process in some order. The Matlab file will extract features into a file called `vgg_feats.mat`.
3. Now that we have the features we can run the prediction! Use the script `predict_on_images.py`. The script takes the path to a model checkpoint and the path to the folder that holds the images, the `tasks.txt`, and the features `vgg_feats.mat`. Example invocation is `python predict_on_images.py lstm_model.p -r example_images`. The script will write the html file `result.html` which you can use to visualize the results in your browser.

Note that the models are trained on a particular dataset (e.g. COCO dataset), so if you show them images they haven't seen during their training time then they will produce garbage. Along with the sentence predictions I'm also showing the log probabilities. When this is low (e.g. -10), this means that the model is confused about the image and likely won't make very good predictions. Conversely, higher numbers (such as -7) indicate that the model is relatively more confident in the outcome.

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
