---
type: source
subject: "GitHub source repos/karpathy/convnetjs/demo/css/style.css"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/demo/css/style.css]
semantic-status: complete-named-text-read
---

# repos/karpathy/convnetjs/demo/css/style.css

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/demo/css/style.css), SHA-256 `669ecbaeb62dc421753c1c5297724afc8b87ef24abf375c395f113c8f4362272`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
.layer { border: 1px solid #999; margin-bottom: 5px; text-align: left; padding: 10px; } .layer_act {
```

Convnet demos expose architecture, optimization controls, training loss, test predictions and representations in the browser. Toy 2D classification paints generalization boundaries and cycles through internal neurons. CIFAR describes augmentation and greater difficulty; its state-of-art and pretrained accuracy numbers are historical claims, not current verified performance. Image painting maps coordinates to RGB and explicitly qualifies compression as impractical, reporting deeper models better empirically at fixed parameter budget. CSS distinguishes layer types and stats with fixed desktop layouts. User-edited architecture is eval-based; these demos are educational source evidence rather than safe arbitrary-code execution patterns.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
.layer {
  border: 1px solid #999;
  margin-bottom: 5px;
  text-align: left;
  padding: 10px;
}
.layer_act {
  width: 500px;
  float: right;
}
.ltconv {
  background-color: #FDD;
}
.ltrelu {
  background-color: #FDF;
}
.ltpool {
  background-color: #DDF;
}
.ltsoftmax {
  background-color: #FFD;
}
.ltfc {
  background-color: #DFF;
}
.ltlrn {
  background-color: #DFD; 
}
.ltdropout {
  background-color: #AAA;  
}
.ltitle {
  color: #333;
  font-size: 18px;
}
.actmap {
  margin: 1px;
}
#trainstats {
  text-align: left;
}
.clear {
  clear: both;
}
#wrap {
  width: 800px;
  margin-left: auto;
  margin-right: auto;
}
h1 {
  font-size: 16px;
  color: #333;
  background-color: #DDD;
  border-bottom: 1px #999 solid;
  text-align: center;
}
h2 {
  text-align: center;
}
.secpart {
  width: 400px;
  float: left;
}
#lossgraph {
  /*border: 1px solid #F0F;*/
  width: 100%;
}
.testdiv canvas {
  float: left;
  width: 64px;
}
.testdiv {
  background-color: rgba(255,255,255,0.65);
  height: auto;
  width: auto;
  display: inline-block;
  font-size: 12px;
  box-shadow: 0px 0px 2px 2px #EEE;
  margin: 5px;
  padding: 5px;
  color: black;
}
.probsdiv {
  float: left;
  width: 100px;
  margin-left: 1px;
}
.pp {
  margin: 1px;
  padding: 1px;
}
#testset_acc {
  /* margin-bottom: 200px; */
}
#testset_vis {
  margin-bottom: 200px;
}
body {
  font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
  /* color: #333; */
  /* padding: 20px; */
}
```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
