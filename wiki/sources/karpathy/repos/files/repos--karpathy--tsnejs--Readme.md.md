---
type: source
subject: "GitHub source repos/karpathy/tsnejs/Readme.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/tsnejs/Readme.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/tsnejs/Readme.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/tsnejs/Readme.md), SHA-256 `df8fddca95f5eb39494f596182280c07632f407633617ba9e3f1b3582562ba91`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "# tSNEJS tSNEJS is an implementation of t-SNE visualization algorithm in Javascript. t-SNE is a".

ScholarOctopus describes a curated paper-pointer visualization using TF-IDF and t-SNE while its collection scripts are explicitly private and absent. SVMJS starts with a linear baseline before nonlinear kernels, exposes speed/accuracy tolerances and references Matlab correctness tests; universal memory-efficiency language remains qualified historical documentation. TF-agent README merely labels Gym RL code. TSNEJS attributes the original algorithm to van der Maaten and Hinton and supplies raw-distance and CSV interfaces; illustrative clusters are not proof of causal structure. Twoolpy contains historical authenticated stream, social-graph recommendation and follower-diff examples with a preflight auth test; obsolete plain-text credential conventions are not adopted. Ulogme separates local timestamped acquisition, processing and browser visualization, keeps data local, documents malformed-log and permission/port troubleshooting, and explicitly supports historical Ubuntu/macOS rather than Windows; current browser incompatibility claims are stale.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

````text

# tSNEJS

tSNEJS is an implementation of t-SNE visualization algorithm in Javascript. 

t-SNE is a visualization algorithm that embeds things in 2 or 3 dimensions. If you have some data and you can measure their pairwise differences, t-SNE visualization can help you identify clusters in your data. See example below.

## Online demo
The main project website has a [live example](http://cs.stanford.edu/people/karpathy/tsnejs/) and more description.

There is also the [t-SNE CSV demo](http://cs.stanford.edu/people/karpathy/tsnejs/csvdemo.html) that allows you to simply paste CSV data into a textbox and tSNEJS computes and visualizes the embedding on the fly (no coding needed).

## Research Paper
The algorithm was originally described in this paper:

    L.J.P. van der Maaten and G.E. Hinton.
    Visualizing High-Dimensional Data Using t-SNE. Journal of Machine Learning Research
    9(Nov):2579-2605, 2008.

You can find the PDF [here](http://jmlr.csail.mit.edu/papers/volume9/vandermaaten08a/vandermaaten08a.pdf).

## Example code
Import tsne.js into your document: `<script src="tsne.js"></script>`
And then here is some example code:

```javascript

var opt = {}
opt.epsilon = 10; // epsilon is learning rate (10 = default)
opt.perplexity = 30; // roughly how many neighbors each point influences (30 = default)
opt.dim = 2; // dimensionality of the embedding (2 = default)

var tsne = new tsnejs.tSNE(opt); // create a tSNE instance

// initialize data. Here we have 3 points and some example pairwise dissimilarities
var dists = [[1.0, 0.1, 0.2], [0.1, 1.0, 0.3], [0.2, 0.1, 1.0]];
tsne.initDataDist(dists);

for(var k = 0; k < 500; k++) {
  tsne.step(); // every time you call this, solution gets better
}

var Y = tsne.getSolution(); // Y is an array of 2-D points that you can plot
```

The data can be passed to tSNEJS as a set of high-dimensional points using the `tsne.initDataRaw(X)` function, where X is an array of arrays (high-dimensional points that need to be embedded). The algorithm computes the Gaussian kernel over these points and then finds the appropriate embedding.

## Web Demos
There are two web interfaces to this library that we are aware of:

- By Andrej, [here](http://cs.stanford.edu/people/karpathy/tsnejs/csvdemo.html).
- By Laurens, [here](http://homepage.tudelft.nl/19j49/tsnejs/), which takes data in different format and can also use Google Spreadsheet input.

## About
Send questions to [@karpathy](https://twitter.com/karpathy).

## License

MIT


````

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
