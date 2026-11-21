---
type: source
subject: "GitHub source repos/karpathy/convnetjs/demo/image_regression.html"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/demo/image_regression.html]
semantic-status: complete-named-text-read
---

# repos/karpathy/convnetjs/demo/image_regression.html

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/demo/image_regression.html), SHA-256 `5ba034218104dc346429337e75eed7f7f712b62da3609142a2e07319bccb5b82`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
<html> <head> <title>ConvNetJS demo: Image Painting</title> <link href='http://fonts.googleapis.com/css?family=Cabin' rel='stylesheet' type='text/css'> <link rel="stylesheet" href="css/style.css"> <link rel="stylesheet"
```

Convnet demos expose architecture, optimization controls, training loss, test predictions and representations in the browser. Toy 2D classification paints generalization boundaries and cycles through internal neurons. CIFAR describes augmentation and greater difficulty; its state-of-art and pretrained accuracy numbers are historical claims, not current verified performance. Image painting maps coordinates to RGB and explicitly qualifies compression as impractical, reporting deeper models better empirically at fixed parameter budget. CSS distinguishes layer types and stats with fixed desktop layouts. User-edited architecture is eval-based; these demos are educational source evidence rather than safe arbitrary-code execution patterns.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
<html>
<head>
<title>ConvNetJS demo: Image Painting</title>
<link href='http://fonts.googleapis.com/css?family=Cabin' rel='stylesheet' type='text/css'>
<link rel="stylesheet" href="css/style.css">

<link rel="stylesheet" href="css/jquery-ui.min.css">
<script src="js/jquery-1.8.3.min.js"></script>
<script src="js/jquery-ui.min.js"></script>

<script src="../build/convnet.js"></script>
<script src="js/image_regression.js"></script>

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
#gallery img {
  width: 195;
  height: 195px;
  display: inline-block;
}
</style>

</head>

<body>

<div id="wrap">
<h1><a href="http://cs.stanford.edu/people/karpathy/convnetjs/">ConvnetJS</a> demo: Image "Painting"</h1>

<p>This demo that treats the pixels of an image as a learning problem: it takes the (x,y) position on a grid and learns to predict the color at that point using regression to (r,g,b). It's a bit like compression, since the image information is encoded in the weights of the network, but almost certainly not of practical kind :)</p>
<p>
  Note that the entire ConvNetJS definition is shown in textbox below and it gets eval()'d to create the network, so feel free to fiddle with the parameters and hit "reload". I found that, empirically and interestingly, deeper networks tend to work much better on this task given a fixed parameter budget.
</p>

<p>Report questions/bugs/suggestions to <a href="https://twitter.com/karpathy">@karpathy</a>.</p>

<textarea id="layerdef" style="width:100%; height:250px;"></textarea>
<br /><br  />
<input id="buttontp" type="submit" value="reload network" onclick="reload();" style="width: 200px; height: 30px;"/>

<div style="float: right;">
Choose your own image: 
<input id="f" type="file" />
</div>

<br>

<div style="background-color: #EEE; padding: 10px; margin-top: 10px;">
<div style="float: left; margin-left: 200px;">
  Original Image<br>
  <canvas id="canv_original"></canvas>
</div>
<div style="float: left; margin-left: 10px;">
  Neural Network output<br>
  <canvas id="canv_net"></canvas>
</div>

<div style="clear:both;"></div>
</div>

<br>
<div id="report"></div>
<br>

<div id="lr">Learning rate:</div>
<div id="slider"></div>
<div>The learning rate should probably be decreased over time (slide left) to let the network better overfit the training data. It's nice to not have to worry about overfitting.</div>

<br><br>
<div>
  You can upload your own image above (click Choose File), or you can click on any of the images below to load them.
</div>
<div id="gallery">
  <img src="imgs/cat.jpg" class="ci" />
  <img src="imgs/esher.png"  class="ci" />
  <img src="imgs/pencils.png" class="ci" />
  <img src="imgs/usa.png"  class="ci" />
  <img src="imgs/fractal.jpg"  class="ci" />
  <img src="imgs/dora.jpg" class="ci" />
  <img src="imgs/rubiks.jpg" class="ci" />
  <img src="imgs/earth.jpg" class="ci" />
  <img src="imgs/fox.png" class="ci" />
  <img src="imgs/twitter.png" class="ci" />
  <img src="imgs/reddit.jpg" class="ci" />
  <img src="imgs/chip.jpg" class="ci" />
  <img src="imgs/jitendra.jpg" class="ci" />
  <img src="imgs/tesla.jpg" class="ci" />
  <img src="imgs/rainforest.jpg" class="ci" />
  <img src="imgs/chess.png" class="ci" />
  <img src="imgs/gradient.png" class="ci" />
  <img src="imgs/battery.jpg" class="ci" />
  <img src="imgs/starry.jpg" class="ci" />
</div>

<br><br>
<p>Go <a href="http://cs.stanford.edu/people/karpathy/convnetjs/">back to ConvNetJS</a></p>

</div>

</body>
</html>


```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
