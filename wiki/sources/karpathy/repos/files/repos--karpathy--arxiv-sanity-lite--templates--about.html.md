---
type: source
subject: "GitHub source repos/karpathy/arxiv-sanity-lite/templates/about.html"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/templates/about.html]
semantic-status: complete-named-text-read
---

# repos/karpathy/arxiv-sanity-lite/templates/about.html

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/templates/about.html), SHA-256 `4714577c07cdea45c786606b1894d9b94a9a5581cf5817e4dce763d99ab06469`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "{% extends \"base.html\" %} {% block variables %} {% endblock %} {% block content %}".

The arxiv-sanity-lite frontend exposes explicit ranking filters, tag shortcuts, paper feature weights, date-window statistics and responsive presentation. Its profile is deliberately username-only and warns email delivery may fail; this is a historical prototype rather than hardened authentication. The thumbnail daemon skips cached outputs and limits download and converter time, logging failures and terminating stuck conversion. Templates load external React and Babel, and some UI handling logs errors rather than displaying them. These files describe interface and reliability choices, not personal beliefs; no network or subprocess behavior was executed.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
{% extends "base.html" %}

{% block variables %}
{% endblock %}

{% block content %}
<div id="aboutwrap">
    <div>
        A much lighter-weight arxiv-sanity from-scratch re-write. Periodically polls arxiv API for new papers. Then allows users to tag papers of interest, and recommends new papers for each tag based on SVMs over tfidf features of paper abstracts. Allows one to search, rank, sort, slice and dice these results in a pretty web UI. Lastly, arxiv-sanity-lite can send you daily emails with recommendations of new papers based on your tags. Curate your tags, track recent papers in your area, and don't miss out!
    </div>

    <br>
    <div>
        This particular instance indexes papers from cs.CV, cs.LG, cs.CL, cs.AI, cs.NE, cs.RO,
        and only since early-ish 2021.
    </div>

    <br>
    <div>The code for this website is open source at Github under <a href="https://github.com/karpathy/arxiv-sanity-lite">arxiv-sanity-lite</a>.</div>

    <br>
    <div>Developed in spare time as a labor of love by <a href="https://twitter.com/karpathy">@karpathy</a>.</div>
</div>
{% endblock %}

{% block elements %}
{% endblock %}

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
