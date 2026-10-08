---
type: source
subject: "GitHub source repos/karpathy/covid-sanity/templates/index.html"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/covid-sanity/templates/index.html]
semantic-status: complete-named-text-read
---

# repos/karpathy/covid-sanity/templates/index.html

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/covid-sanity/templates/index.html), SHA-256 `47535410ef755f83eb90043ebef264c09d998a01e5daa903ba733eefd4a7ec6b`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "<!DOCTYPE HTML> <html> <head> <!-- meta info --> <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\"> <title>biomed-sanity</title> <!-- CSS".

Convnet neural-net specs verify desugared layer count, normalized probabilities, increased ground-truth probability after a small unregularized update and finite-difference input gradients; comments explicitly qualify step size and coverage. Specs were read, not run; analytic gradients are taken before an update and numeric losses afterward, a comparison limitation. Jasmine license/runner preserve third-party dependency provenance. Covid-sanity updater fetches BioRxiv collection, uses title-plus-abstract unigram TF-IDF, balanced exemplar SVM similarities and a weighted inverted search dictionary prioritizing title and authors. Flask loads local generated JSON, adapts changed author API schema to a legacy string, ranks optional tweets by follower count and returns at most forty search or latest papers with a small recency boost. React shows abstracts, PDF/similarity links and expandable tweets. Fixed-width styling and CDN/Babel template are historical implementation choices. Banned list excludes automated preprint accounts. No current API availability or deployed behavior verified.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
<!DOCTYPE HTML>
<html>

<head>
<!-- meta info -->
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>biomed-sanity</title>
<!-- CSS -->
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
<!-- Favicon -->
<link rel="shortcut icon" type="image/png" href="{{ url_for('static', filename='favicon.png') }}" />

<script>
var papers = {{ papers | tojson }};
var gvars = {{ gvars | tojson }};
</script>
</head>

<body>

<a href="https://github.com/karpathy/covid-sanity"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://camo.githubusercontent.com/38ef81f8aca64bb9a64448d0d70f1308ef5341ab/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6769746875622f726962626f6e732f666f726b6d655f72696768745f6461726b626c75655f3132313632312e706e67" alt="Fork me on GitHub" data-canonical-src="https://s3.amazonaws.com/github/ribbons/forkme_right_darkblue_121621.png"></a>

<!-- title / description -->
<div id="titdiv">
    <a href="/"><h1>BioMed Sanity</h1></a>
    Built in spare time by </a><a href="https://twitter.com/karpathy">@karpathy</a> following <a href="https://connect.biorxiv.org/relate/content/181">biorxiv</a> and my older project <a href="https://www.arxiv-sanity.com/">arxiv-sanity</a> to help with influx of papers on COVID-19, currently indexing {{ gvars.num_papers }} papers.<br>
    </div>
</div>

<!-- search box -->
<div id="sbox">
    <form action="/search" method="get">
        <input name="q" type="text" id="qfield" value="{{ gvars.search_query }}">
    </form>
</div>

<!-- paper list renders here -->
<div id="wrap">
</div>

<!-- React -->
<script src="https://unpkg.com/react@16/umd/react.production.min.js" crossorigin></script>
<script src="https://unpkg.com/react-dom@16/umd/react-dom.production.min.js" crossorigin></script>
<!-- Babel for displaying JSX -->
<script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
<!-- Load our React component -->
<script src="{{ url_for('static', filename='paper_list.js') }}" type="text/babel"></script>

</body>
</html>
```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
