---
type: source
subject: "GitHub source repos/karpathy/convnetjs/demo/regression.html"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/demo/regression.html]
semantic-status: complete-named-text-read
---

# repos/karpathy/convnetjs/demo/regression.html

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/demo/regression.html), SHA-256 `b696fe6bb60c36c6a74a832557cfc6b2762da4d6e292c83b12d7880cecbe8b87`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
<html> <head> <title>ConvNetJS demo: Classify toy 2D data</title> <link href='http://fonts.googleapis.com/css?family=Cabin' rel='stylesheet' type='text/css'> <link rel="stylesheet" href="css/style.css">
```

Trainer comparison feeds the same sampled training and test examples to seven optimizers, keeps separate rolling loss/train/test windows and visualizes curves. Networks initialize independently, so this does not control initialization confounding or establish a universal optimizer ranking. MNIST prose claims historical Ubuntu-Chrome speed and random crop averaging, whereas current shared code disables its augmentation flags and contains a nonaugmentation bug; the captured generations conflict explicitly. Regression explains squared-error mechanics and invites editable architecture and visible layer outputs. Historical numbers and UI statements were not silently promoted over actual implementation.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
<html>
<head>
<title>ConvNetJS demo: Classify toy 2D data</title>
<link href='http://fonts.googleapis.com/css?family=Cabin' rel='stylesheet' type='text/css'>
<link rel="stylesheet" href="css/style.css">

<script>
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

      ga('create', 'UA-3698471-21', 'stanford.edu');
      ga('send', 'pageview');

</script>

<script src="js/jquery-1.8.3.min.js"></script>
<script src="js/npgmain.js"></script>
<script src="../build/convnet.js"></script>
<script src="js/regression.js"></script>

<style type="text/css">
canvas { 
    border: 1px solid #555;
    margin-top: 10px;
}
#wrap {
  width: 800px;
  margin-right: auto;
  margin-left: auto;
  margin-bottom: 200px;
}
</style>

</head>

<body onLoad="NPGinit(10);">

<div id="wrap">
<h1><a href="http://cs.stanford.edu/people/karpathy/convnetjs">ConvnetJS</a> demo: toy 1d regression</h1>

<p>The simulation below is a 1-dimensional regression where a neural network is trained to regress to y coordinates for every given point x through an L2 loss. That is, the minimized cost function computes the squared difference between the predicted y-coordinate and the "correct" y coordinate. Every 10th of a second, all points are fed to the network multiple times through the trainer class to train the network.</p>

<p>The simulation below will eval() whatever you have in the text area and reload. Feel free to explore and use ConvNetJS to instantiate your own network!</p>

<p>Report questions/bugs/suggestions to <a href="https://twitter.com/karpathy">@karpathy</a>.</p>

<textarea id="layerdef" style="width:100%; height:250px;">
</textarea>
<br /><br  />
<input id="buttontp" type="submit" value="change network" onclick="reload();" style="width: 300px; height: 50px;"/>

<div style="float: right;">
Number of points to generate:  <input type="text" name="num_points" id="num_data" value="20">
<input type="submit" value="regenerate data" style="height:50px;" onclick="regen_data();" />
</div>

<br />
<p style="color: red">Add data points by clicking!</p>
<br />
<input type="checkbox" name="draw_layer_outputs" id="layer_outs">
Also draw outputs of a layer (click layer button below) in red.
<br /><div id="layer_ixes"></div>

<canvas id="NPGcanvas" width="800" height="500">Browser not supported for Canvas. Get a real browser.</canvas>

<p>Go <a href="http://cs.stanford.edu/people/karpathy/convnetjs/">back to ConvNetJS</a></p>

</div>

</body>
</html>


```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
