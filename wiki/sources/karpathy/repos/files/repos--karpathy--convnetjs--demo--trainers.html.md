---
type: source
subject: "GitHub source repos/karpathy/convnetjs/demo/trainers.html"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/demo/trainers.html]
semantic-status: complete-named-text-read
---

# repos/karpathy/convnetjs/demo/trainers.html

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/demo/trainers.html), SHA-256 `727fb2c79dcf90a99dbf72e8c567830e96b7b623a949358ef198973b9e180159`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
<!doctype html> <html lang="en"> <head> <meta charset="utf-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"> <title>ConvNetJS Trainer Comparison on MNIST</title>
```

Convnet dot-product layers implement convolution weight sharing and dense connectivity explicitly, with chain-rule data/weight gradients, JSON serialization and separate bias decay. Optimized convolution credits mdda and acknowledges direct-array speed versus modularity tradeoffs. Dropout openly calls itself inefficient and distinguishes training from prediction; prediction multiplies by drop probability rather than retention probability, equivalent only at the default half, so general correctness is not claimed. Input is an identity layer and export supports browser or Node. Speedtest times a declared forward-only convolution; trainer prose is personal historical experience qualified by tuning, not a verified universal ranking.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <title>ConvNetJS Trainer Comparison on MNIST</title>
  <meta name="description" content="">
  <meta name="author" content="">
  <link rel="stylesheet" href="css/style.css">

<script src="js/jquery-1.8.3.min.js"></script>
<script src="../build/vis.js"></script>
<script src="../build/util.js"></script>
<script src="../build/convnet.js"></script>
<script src="mnist/mnist_labels.js"></script>
<script src="js/trainers.js"></script>

</head>
<body>
  <div id="wrap">
  <h2 style="text-align: center;"><a href="http://cs.stanford.edu/people/karpathy/convnetjs/">ConvNetJS</a> Trainer demo on MNIST</h2>
  <h1>Description</h1>
  <p>
    This demo lets you evaluate multiple trainers against each other on MNIST. By default I've set up a little benchmark that puts SGD/SGD with momentum/Adam/Adagrad/Adadelta/Nesterov against each other. For reference math and explanations on these refer to Matthew Zeiler's <a href="http://www.matthewzeiler.com/pubs/googleTR2012/googleTR2012.pdf">Adadelta paper</a> (Windowgrad is Idea #1 in the paper). In my own experience, Adagrad/Adadelta are "safer" because they don't depend so strongly on setting of learning rates (with Adadelta being slightly better), but well-tuned SGD+Momentum almost always converges faster and at better final values.
  </p>
  <p>Report questions/bugs/suggestions to <a href="https://twitter.com/karpathy">@karpathy</a>.</p>

  <textarea id="layerdef" style="width:100%; height:400px;">
  </textarea>
  <br /><br  />
  <input id="buttontp" type="submit" value="re-run" onclick="reload();" style="width: 300px; height: 50px;"/>

  <h1>Loss vs. Number of examples seen</h1>
  <canvas id="lossgraph" width="800" height="400"></canvas>

  <h1>Testing Accuracy vs. Number of examples seen</h1>
  <canvas id="testaccgraph" width="800" height="400"></canvas>

  <h1>Training Accuracy vs. Number of examples seen</h1>
  <canvas id="trainaccgraph" width="800" height="400"></canvas>

  </div>
</body>
</html>




```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
