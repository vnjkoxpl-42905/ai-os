---
type: source
subject: "GitHub source repos/karpathy/forestjs/README.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/forestjs/README.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/forestjs/README.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/forestjs/README.md), SHA-256 `07818e56be43e262d2bc383e6f912f27b639c739a7cc02ab2d1fb6d89c0dc04b`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
# forestjs Andrej Karpathy July 2012 forestjs is a Random Forest implementation for Javascript. Currently
```

Cryptos presents a zero-dependency educational Bitcoin implementation and compares SHA-256 with a reference tool; it explicitly restricts use to education and distinguishes partial transaction/header verification from a complete full node. Demonstration keys are source examples, not private workspace credentials. Deep-vector-quantization separates attempted VQVAE reproduction, data-driven initialization needed to avoid index collapse, finicky Gumbel tuning and unfinished DALL-E work; reconstruction loss alone is qualified evidence. EigenLibSVM documents a dense linear-kernel wrapper with a tiny installation demo. Find-birds separates resumable rate-limited social-graph acquisition from reports that can use partial results, while historical Twitter credentials/API instructions are not current recommendations. ForestJS makes weak learners pluggable and advises cross-validation of depth/tries; its universal tree-count and dimensionality statements remain historical source opinions. Gitstats is a small generated-repository-activity visualization. HN Time Capsule stages historical retrieval, prompts, paid analysis, parsing and HTML rendering; it is explicitly 99-percent vibe-coded and unsupported, so hindsight grades are model judgments rather than verified prediction accuracy.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

````text
# forestjs
Andrej Karpathy
July 2012

forestjs is a Random Forest implementation for Javascript. Currently only binary classification is supported. You can also define your own weak learners to use in the decision trees.

## Online GUI demo

Can be found here: http://cs.stanford.edu/~karpathy/svmjs/demo/demoforest.html

Corresponding code is inside /demo directory.

## Usage

The simplest use case:
```javascript
<script src="./svmjs/lib/randomforest.js"></script>
<script>
forest = new forestjs.RandomForest();
// data is 2D array of size NxD. Labels is 1D array of length D
forest.train(data, labels); 
// testInstance is 1D array of length D. Returns probability
labelProbability = forest.predictOne(testInstance);
// testData is 2D array of size MxD. Returns array of probabilities of length M
labelProbabilities = forest.predict(testData);
</script>
```

The library supports arbitrary weak learners. Currently implemented are a decision stump (1-dimensional decisions) and 2D decision stumps.

```javascript
options.trainFun = function(data, labels, ix, options) {
  
  // create some decision rule based on data and labels.
  // Only use data at indeces given in ix. Ignore the rest of the data.
  // this is done for efficiency.
  
  // save parameters that describe your model
  model.parameter1= p1;
  model.parameter2= p2;
  return model;
  
}
options.testFun = function(inst, model) {
  
  // use model.parameter1 and model.parameter2 to return a 1 or -1 for
  // example instance inst. This determines if it will be passed down
  // left or right in the tree.
  
  return inst[0] > model.parameter1 ? 1 : -1; // silly example
}

forest.train(data, labels, options); // will train forest with the custom weak learners above
```
## Options

There are 3 main options that can be passed in to training:
```javascript
options = {};
options.numTrees = 100; // defaults
options.maxDepth = 4;
options.numTries = 10;
forest.train(data, labels, options);
```

numTrees: You want to set this as high as you can computationally afford. Performance scales linearly with this parameter.

maxDepth: The depth of each of the trees in the forest. If your data is complicated, or has high dimension, you may want to increase this. If this is set too high, you may start to overfit but having many trees can help compensate for this. maxDepth is also the number of decisions that will be done on each data instance. Space complexity inreases exponentially (base 2, as these are trees) with this parameter and time complexity increases linearly.

numTries: The number of random hypotheses that decision stump learners that come default with this implementation will generate when training. If this is too high, you will start to overfit as nodes will lose variety. If you're using your own weak learners trainFun and testFun, ignore this.

It is best to cross-validate maxDepth and numTries. For numTrees, the more the better always.

## Pros and cons

Random Forests are awesome: They train extremely quickly and at testing time they are even faster. In general this is a great and flexible algorithm and forms a standard benchmark in Kaggle, for example. The only place these can suffer is if your dimensionality is too high (>20 or so) but this can be addressed with appropriate choice of weak learner at nodes. One possibility is to select random 10 dimensions and train a small logistic regression with early stopping at every node.

## License
MIT

````

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
