---
type: source
subject: "GitHub source repos/karpathy/convnetjs/demo/autoencoder.html"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/demo/autoencoder.html]
semantic-status: complete-named-text-read
---

# repos/karpathy/convnetjs/demo/autoencoder.html

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/demo/autoencoder.html), SHA-256 `7304a726834c2e61128f3049b81bdd28d9f98114a61fae8de5ff5fd642bbcb9b`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
<!doctype html> <html lang="en"> <head> <meta charset="utf-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"> <title>ConvNetJS MNIST demo</title> <meta name="description"
```

Char-rnn utilities explicitly credit adapted parameter flattening code and preserve shared storage across timestep clones; OneHot caches the identity matrix. Convnet build concatenates a declared layer order and minifies via YUI. Autoencoder demo explains a bottleneck as the mechanism forcing useful compressed representations and exposes live loss, neurons and snapshots. MagicNet demo explicitly states CSV assumptions, separates training/validation/test roles, cross-validates architectures and ensembles selected models, with export/import. The explanatory demos support interactive inspection and held-out evaluation; external datasets and borrowed utilities are not independently authored philosophy, and no browser training was performed.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <title>ConvNetJS MNIST demo</title>
  <meta name="description" content="">
  <meta name="author" content="">
  <link rel="stylesheet" href="css/style.css">
</head>

<script src="js/jquery-1.8.3.min.js"></script>
<script src="../build/vis.js"></script>
<script src="../build/util.js"></script>
<script src="../build/convnet.js"></script>


<script src="mnist/mnist_labels.js"></script>
<script src="js/autoencoder.js"></script>

<body>
  <div id="wrap">
  <h2 style="text-align: center;"><a href="http://cs.stanford.edu/people/karpathy/convnetjs/">ConvNetJS</a> Denoising Autoencoder demo</h2>
  <h1>Description</h1>
  <p>
    All the other demos are examples of Supervised Learning, so in this demo I wanted to show an example of Unsupervised Learning. We are going to train an autoencoder on MNIST digits.
  </p>
  <p>
    An autoencoder is a regression task where the network is asked to predict its input (in other words, model the identity function). Sounds simple enough, except the network has a tight bottleneck of a few neurons in the middle (in the default example only two!), forcing it to create effective representations that compress the input into a low-dimensional code that can be used by the decoder to reproduce the original input.
  </p>
  <p>Report questions/bugs/suggestions to <a href="https://twitter.com/karpathy">@karpathy</a>.
  </p>
  <h1>Training Stats</h1>
  <div class="divsec" style="270px;">
    <div class="secpart">
      Current image: <img id="input_image" src=""></img><input id="buttontp" type="submit" value="pause" onclick="toggle_pause();"/>
      <div id="trainstats"></div>

      <div id="controls">
        Learning rate: <input name="lri" type="text" maxlength="20" id="lr_input"/>
        <input id="buttonlr" type="submit" value="change" onclick="change_lr();"/>
        <br />
      </div>

      <input id="buttondj" type="submit" value="save network snapshot as JSON" onclick="dump_json();"/><br />
      <input id="buttonlfj" type="submit" value="init network from JSON snapshot" onclick="load_from_json();"/><br />
      <textarea id="dumpjson"></textarea>
    </div>
    <div class="secpart">
      
      <div>
        Loss:<br />
        <canvas id="lossgraph">
        </canvas>
        <br />
        <input id="buttoncg" type="submit" value="clear graph" onclick="clear_graph();"/>
      </div>

    </div>
    <div>
      <textarea id="newnet" style="width:100%; height:100px;"></textarea><br />
      <input id="buttonnn" type="submit" value="reload" onclick="change_net();" style="width:200px; height: 40px;"/>
    </div>

    <div style="margin-top: 1px solid #000; margin-top:20px;">
      <div id="layer_ixes"></div>
      <input id="buttoncycle" type="submit" value="cycle through visualized neurons at selected layer (if more than 2)" onclick="cycle();" style="height: 40px;"/>
      <div id="cyclestatus"></div>
      <div style="text-align:center;"><canvas id="embedding" width="500" height="500"></canvas></div>
    </div>

    <div style="clear:both;"></div>
  </div>

  <div class="divsec">
  <h1>Network Visualization</h1>
    <div id="visnet"></div>
  </div>

  </div>  
</body>
</html>




```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
