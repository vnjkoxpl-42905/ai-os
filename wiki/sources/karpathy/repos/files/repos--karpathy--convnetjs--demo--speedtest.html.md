---
type: source
subject: "GitHub source repos/karpathy/convnetjs/demo/speedtest.html"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/demo/speedtest.html]
semantic-status: complete-named-text-read
---

# repos/karpathy/convnetjs/demo/speedtest.html

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/demo/speedtest.html), SHA-256 `88353bce5415339fc9d0446f8da75dc8ee6df4f834b0bef7aa179992844ef4b3`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
<!doctype html> <html lang="en"> <head> <meta charset="utf-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"> <title>Simple speed test</title> <meta name="description"
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
  <title>Simple speed test</title>
  <meta name="description" content="">
  <meta name="author" content="">

<script src="../build/convnet.js"></script>

<script>

function logEvent(str) {
  console.log(str);
  var d = document.createElement('div');
  d.innerHTML = str;
  document.getElementById('result').appendChild(d);
}

n = 0;
dtall = 0;
function runExample() {

  var t0 = +new Date();
  layer.forward(x);
  //layer.backward();
  var t1 = +new Date();
  var diff = t1 - t0;
  dtall += diff;
  n++;

  logEvent('ran example ' + n + ' in ' + diff + 'ms, estimated average = ' + (dtall / n).toFixed(3) + 'ms');
}

function start() {

  // Conv Layer definition used in convnet benchmarks
  opt = { in_sx:128, in_sy:128, in_depth:3, sx:11, filters:96, stride: 1, pad: 0};
  layer = new convnetjs.ConvLayer(opt);
  x = new convnetjs.Vol(128, 128, 3);

  run1i = setInterval(runExample, 5); // start
}
</script>
</head>
<body>
  <button onclick="start()">Convolution Test Start</button>
  <button onclick="window.clearInterval(run1i);">Stop</button>
  <div id="result"></div>
</body>
</html>




```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
