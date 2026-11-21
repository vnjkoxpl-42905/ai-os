---
type: source
subject: "GitHub source repos/karpathy/EigenLibSVM/Readme.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/EigenLibSVM/Readme.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/EigenLibSVM/Readme.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/EigenLibSVM/Readme.md), SHA-256 `985a60107520404f7f43e0a09adcc8332413946a8579311a7ff22d5567d4d924`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
# EigenLibSVM Andrej Karpathy 1 May 2012 This is a small C++ wrapper to call
```

Cryptos presents a zero-dependency educational Bitcoin implementation and compares SHA-256 with a reference tool; it explicitly restricts use to education and distinguishes partial transaction/header verification from a complete full node. Demonstration keys are source examples, not private workspace credentials. Deep-vector-quantization separates attempted VQVAE reproduction, data-driven initialization needed to avoid index collapse, finicky Gumbel tuning and unfinished DALL-E work; reconstruction loss alone is qualified evidence. EigenLibSVM documents a dense linear-kernel wrapper with a tiny installation demo. Find-birds separates resumable rate-limited social-graph acquisition from reports that can use partial results, while historical Twitter credentials/API instructions are not current recommendations. ForestJS makes weak learners pluggable and advises cross-validation of depth/tries; its universal tree-count and dimensionality statements remain historical source opinions. Gitstats is a small generated-repository-activity visualization. HN Time Capsule stages historical retrieval, prompts, paid analysis, parsing and HTML rendering; it is explicitly 99-percent vibe-coded and unsupported, so hindsight grades are model judgments rather than verified prediction accuracy.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

````text
# EigenLibSVM
Andrej Karpathy
1 May 2012

This is a small C++ wrapper to call libsvm if you use the Eigen matrix library.
Dependencies consist of libsvm and eigen3 library.
Current support is only for dense matrices with linear kernel svm.

## Usage

```c++
vector<int> yhat;
SVMClassifier svm;
svm.train(X, y);
svm.test(X, yhat);
```

where X is an `Eigen::MatrixXf` NxD matrix, y is an `Eigen::MatrixXf` Nx1 matrix of
labels (-1 or 1), or a `vector<int>` of labels. You can also save and load the models:

```c++
svm.saveModel("tmp_model");  
svm.loadModel("tmp_model");  
```

there is now also functionality to directly get the weights:
```c++
Eigen::MatrixXf w;
float b;
svm.getw(w, b);
Eigen::MatrixXf margin= ((X * w).array() + b).matrix(); // yhat = sign(margin)
```

See demo for details.

## Install

```
$ sudo apt-get install libsvm-dev  
$ sudo apt-get install libeigen3-dev  
$ git clone git@github.com:karpathy/EigenLibSVM.git  
$ cd EigenLibSVM  
$ mkdir build  
$ cd build  
$ cmake ..  
$ make  
$ ./svm_test  
```

where the last line will run a tiny demo that makes sure everything installed ok
(it runs almost instantly)

## License
BSD

````

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
