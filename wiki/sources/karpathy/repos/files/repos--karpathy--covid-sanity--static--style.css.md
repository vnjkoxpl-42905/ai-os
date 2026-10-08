---
type: source
subject: "GitHub source repos/karpathy/covid-sanity/static/style.css"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/covid-sanity/static/style.css]
semantic-status: complete-named-text-read
---

# repos/karpathy/covid-sanity/static/style.css

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/covid-sanity/static/style.css), SHA-256 `064b85fed465c4e03f75805cc7293afb32c8c78b34c62ce14a47cf74fb0429d2`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "body { margin: 0; padding: 0; font-family: \"Gill Sans\", \"Gill Sans MT\", Helvetica, Arial, sans-serif;".

Convnet neural-net specs verify desugared layer count, normalized probabilities, increased ground-truth probability after a small unregularized update and finite-difference input gradients; comments explicitly qualify step size and coverage. Specs were read, not run; analytic gradients are taken before an update and numeric losses afterward, a comparison limitation. Jasmine license/runner preserve third-party dependency provenance. Covid-sanity updater fetches BioRxiv collection, uses title-plus-abstract unigram TF-IDF, balanced exemplar SVM similarities and a weighted inverted search dictionary prioritizing title and authors. Flask loads local generated JSON, adapts changed author API schema to a legacy string, ranks optional tweets by follower count and returns at most forty search or latest papers with a small recency boost. React shows abstracts, PDF/similarity links and expandable tweets. Fixed-width styling and CDN/Babel template are historical implementation choices. Banned list excludes automated preprint accounts. No current API availability or deployed behavior verified.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
body {
    margin: 0;
    padding: 0;
    font-family: "Gill Sans", "Gill Sans MT", Helvetica, Arial, sans-serif;
    font-weight: 400;
    background-color: #F6F3E5;
}

#titdiv {
	height: 50px;
	background-color: #840000;
	color: white;
	padding-top: 10px;
	padding-left: 20px;
	border-bottom: 1px solid #540000;
}
h1 {
    font-size: 24px;
    padding: 0;
    margin: 0;
    font-weight: 400;
}
#titdiv a {
    font-weight: 300;
}
#titdiv a:visited {
    color: white;
}
#titdiv a:link {
    color: white;
}

#wrap {
    width: 970px;
    margin-left: auto;
    margin-right: auto;
}

.rel_paper {
    margin: 10px;
    padding: 6px;
    color: #333;
    font-size: 16px;
    border: 1px solid #333;
    background-color: white;
}

.rel_paper a {
    font-weight: normal;
    text-decoration: none;
}

.rel_authors {
    font-weight: 300;
    font-size: 14px;
}

.dllinks {
    border-radius: 5px;
    float: right;
    text-align: right;
}

.metadata {
    font-size: 16px;
    padding: 5px;
    display: inline-block;
}
.action {
    cursor: pointer;
    text-decoration: underline;
}

.rel_date {
    color: #900;
}

.rel_title {
    font-size: 18px;
}

.medrxiv .rel_title a {
    color: #0e4c92;
}

.biorxiv .rel_title a {
    color: #bc2635;
}

.rel_abs {
    font-family: Arial, Helvetica, sans-serif;
    font-weight: 300;
    background-color: #EFE;
    padding: 10px;
    margin-top: 10px;
    border-radius: 5px 5px 0px 0px;
}

.rel_tweets_summary {
    background-color: #EEF;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 16px;
    border-radius: 5px;
    padding: 5px;
    margin-top: 5px;
    cursor: pointer;
    text-align: center;
}

.tweet {
    background-color: #EEF;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 14px;
    border-radius: 5px;
    padding: 5px;
    margin-top: 5px;
    min-height: 48px;
}

.tweet img {
    float: left;
    margin-right: 5px;
    border-radius: 5px;
}

.tweet .meta {
    margin-top: 3px;
}

.tweet .following {
    background-color: #0e4c92;
    padding: 3px 5px 3px 5px;
    border-radius: 3px 0px 0px 3px;
    color: white;
}

.tweet .uname {
    padding: 3px 5px 3px 5px;
    background-color: #6a99d4;
    color: white;
    border-radius: 0px 3px 3px 0px;
    margin-right: 5px;
}

.tweet .uname a {
    color: white;
}

.tweet .text {
    line-height: 18px;
}


#info {
    background-color: #EEF;
    padding: 10px;
    margin: 10px;
    border: 1px solid #CCD;
    color: #005;
    font-weight: 300;
}

#sbox {
    margin-top: 10px;
    text-align: center;
}

#qfield {
    border: 5px solid white;
    width: 920px;
    border: solid 1px #999;

    height: 40px;
    font-size: 22px;
    color: "#333";

    padding-left: 50px;

    background-image:url('/static/search.png');
    background-repeat:no-repeat;
    background-position:left center;
    outline:0;
  }
```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
