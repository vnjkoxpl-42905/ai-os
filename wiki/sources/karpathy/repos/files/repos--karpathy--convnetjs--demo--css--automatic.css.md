---
type: source
subject: "GitHub source repos/karpathy/convnetjs/demo/css/automatic.css"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/demo/css/automatic.css]
semantic-status: complete-named-text-read
---

# repos/karpathy/convnetjs/demo/css/automatic.css

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/demo/css/automatic.css), SHA-256 `6926a98287e5690e3dcd541ab88c54d70dafb1b2a4be9980acb6a190bd752e5d`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "#wrap { width:800px; margin-left: auto; margin-right: auto; } h2 { text-align: center; font-size: 34px; font-weight:".

Convnet demos expose architecture, optimization controls, training loss, test predictions and representations in the browser. Toy 2D classification paints generalization boundaries and cycles through internal neurons. CIFAR describes augmentation and greater difficulty; its state-of-art and pretrained accuracy numbers are historical claims, not current verified performance. Image painting maps coordinates to RGB and explicitly qualifies compression as impractical, reporting deeper models better empirically at fixed parameter budget. CSS distinguishes layer types and stats with fixed desktop layouts. User-edited architecture is eval-based; these demos are educational source evidence rather than safe arbitrary-code execution patterns.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
#wrap {
  width:800px;
  margin-left: auto;
  margin-right: auto;
}
h2 {
  text-align: center;
  font-size: 34px;
  font-weight: 300;
  margin-bottom: 50px;
}
h1 {
  font-size: 26px;
  font-weight: 400;
  border-bottom: 1px #999 solid;
}
#datamsg{
  background-color: white;
  margin-top: 2px;
  padding: 10px;
}
#prepromsg{
  margin-top: 10px;
  padding: 10px;
}
.msg{
  padding: 2px;
}
body {
  font-family: 'Lato', sans-serif;
  color: #333;
  font-size: 20px;
  font-weight: 300;
}
input[type=text] {
  border: 1px solid #999;
  padding: 3px;
  font-size: 18px;
  color: #333;
}
.clouds-flat-button {
  position: relative;
  vertical-align: top;
  width: 100%;
  height: 80px;
  padding: 0;
  color:#454545;
  text-align: center;
  font-size: 16px;
  background: #ecf0f1;
  border: 0;
  border-bottom: 2px solid #dadedf;
  cursor: pointer;
  -webkit-box-shadow: inset 0 -2px #dadedf;
  box-shadow: inset 0 -2px #dadedf;
}
.clouds-flat-button:active {
  top: 1px;
  outline: none;
  -webkit-box-shadow: none;
  box-shadow: none;
}
#bestmodel {
  font-size: 16px;
  background-color: #FAFAFA;
  padding: 10px;
}
#bestmodeloverall {
  font-size: 16px;
  background-color: #FAFAFA;
  padding: 10px;
  margin-top: 10px;
}
.syntaxhighlighter {
  font-size: 14px !important;
  overflow-y: hidden !important; 
}
.sopts {
  box-shadow: 0px 0px 2px 0px #555;
  margin-bottom: 5px;
  padding: 10px;
}
```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
