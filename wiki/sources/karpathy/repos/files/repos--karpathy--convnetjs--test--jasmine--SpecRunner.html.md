---
type: source
subject: "GitHub source repos/karpathy/convnetjs/test/jasmine/SpecRunner.html"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/test/jasmine/SpecRunner.html]
semantic-status: complete-named-text-read
---

# repos/karpathy/convnetjs/test/jasmine/SpecRunner.html

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/test/jasmine/SpecRunner.html), SHA-256 `d1d22aa95382aba837134f811ffa9feb956616538fb376d9decd36a0f231d69d`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
<!DOCTYPE HTML> <html> <head> <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"> <title>Jasmine Spec Runner v2.0.0</title> <link rel="shortcut icon"
```

Convnet neural-net specs verify desugared layer count, normalized probabilities, increased ground-truth probability after a small unregularized update and finite-difference input gradients; comments explicitly qualify step size and coverage. Specs were read, not run; analytic gradients are taken before an update and numeric losses afterward, a comparison limitation. Jasmine license/runner preserve third-party dependency provenance. Covid-sanity updater fetches BioRxiv collection, uses title-plus-abstract unigram TF-IDF, balanced exemplar SVM similarities and a weighted inverted search dictionary prioritizing title and authors. Flask loads local generated JSON, adapts changed author API schema to a legacy string, ranks optional tweets by follower count and returns at most forty search or latest papers with a small recency boost. React shows abstracts, PDF/similarity links and expandable tweets. Fixed-width styling and CDN/Babel template are historical implementation choices. Banned list excludes automated preprint accounts. No current API availability or deployed behavior verified.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
<!DOCTYPE HTML>
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <title>Jasmine Spec Runner v2.0.0</title>

  <link rel="shortcut icon" type="image/png" href="lib/jasmine-2.0.0/jasmine_favicon.png">
  <link rel="stylesheet" type="text/css" href="lib/jasmine-2.0.0/jasmine.css">

  <script type="text/javascript" src="lib/jasmine-2.0.0/jasmine.js"></script>
  <script type="text/javascript" src="lib/jasmine-2.0.0/jasmine-html.js"></script>
  <script type="text/javascript" src="lib/jasmine-2.0.0/boot.js"></script>

  <!-- include source files here... -->
  <script type="text/javascript" src="../../build/convnet.js"></script>

  <!-- include spec files here... -->
  <script type="text/javascript" src="spec/NeuralNetSpec.js"></script>

</head>

<body>
</body>
</html>

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
