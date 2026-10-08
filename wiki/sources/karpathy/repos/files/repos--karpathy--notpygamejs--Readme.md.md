---
type: source
subject: "GitHub source repos/karpathy/notpygamejs/Readme.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/notpygamejs/Readme.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/notpygamejs/Readme.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/notpygamejs/Readme.md), SHA-256 `bfd6c60e6146f5b9facd3d7db8eb0df58913d5e54648aa99a987d8581b019b94`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
# notpygamejs Game making library for Javascript with the Canvas element. Andrej Karpathy 1 May
```

Neuraltalk2 documents captioning, pretrained evaluation, data preprocessing, staged CNN finetuning and visualization, with explicit beam-search speed/quality tradeoffs and a known corrupt input-image failure. Its 2016 update recommends Google im2txt and preserves this as educational Torch code; projected leaderboard placement and speed are dated reports. Ng-video-lecture keeps lecture-identical code while acknowledging missing initialization treatment and slower convergence, and warns a differently named successor implementation cannot simply be pasted in. Nipspreview breaks PDF and metadata acquisition into thumbnail, word-cloud, topic-model and abstract stages and admits malformed-paper extraction needs human intervention; its LDA implementation is credited externally. Zero-to-Hero sequences scalar autograd, bigrams, MLP, activation/gradient diagnostics, manual backpropagation, hierarchical CNNs, GPT and tokenization; the backprop lesson asks learners to work the exercise and unpause only when stuck, rather than merely watch. Notpygamejs abstracts game/event boilerplate while admitting globals; paper-notes README is an informal placeholder.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

````text
# notpygamejs
Game making library for Javascript with the Canvas element.
Andrej Karpathy
1 May 2012

## Usage
This library abstracts away boring stuff such as game loop, mouse, keyboard API calls, etc etc etc. All that is left to do is to implement the meat of the following functions:

```javascript
//executes once in the beginning
function myinit(){ }

//executes every tick, FPS (typically around 30-50) times a second
function update(){ }

//executes every tick right after update()
function draw(){
    ctx.clearRect(0,0,WIDTH,HEIGHT);
}

//event function when a click occurs. x, y coordinates of click are given
function mouseClick(x, y){ }

//events for key up and down. key value is passed in.
function keyUp(key){ }
function keyDown(key){ }
```

The library assumes that your HTML file looks, for example as:

```html
<body onLoad="NPGinit(50);">
<canvas id="NPGcanvas" width="500" height="500">Browser not supported for Canvas. Get a real browser.</canvas>
```

In other words, call NPGinit({#FPS}) function once somewhere in your code. The function will hook its functionality
into a canvas on the page with id "NPGcanvas". Since this is not using any namespaces, a few things get added to global namespace (I know, I know...). For now, extra variables include:

```javascript
var canvas;
var ctx;
var WIDTH;
var HEIGHT; 
var FPS;
```

The variable ctx will get instantiated to the canvas context that you should use for drawing. See demos for details.

## License
BSD
````

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
