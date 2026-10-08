---
type: source
subject: "GitHub source repos/karpathy/arxiv-sanity-lite/templates/stats.html"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/templates/stats.html]
semantic-status: complete-named-text-read
---

# repos/karpathy/arxiv-sanity-lite/templates/stats.html

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/templates/stats.html), SHA-256 `c996f094f32575547ecc7491d16615faa13fcb69820462ca3b6d2b756c6b815f`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
{% extends "base.html" %} {% block variables %} {% endblock %} {% block content %}
```

The arxiv-sanity-lite frontend exposes explicit ranking filters, tag shortcuts, paper feature weights, date-window statistics and responsive presentation. Its profile is deliberately username-only and warns email delivery may fail; this is a historical prototype rather than hardened authentication. The thumbnail daemon skips cached outputs and limits download and converter time, logging failures and terminating stuck conversion. Templates load external React and Babel, and some UI handling logs errors rather than displaying them. These files describe interface and reliability choices, not personal beliefs; no network or subprocess behavior was executed.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
{% extends "base.html" %}

{% block variables %}
{% endblock %}

{% block content %}
<div id="statswrap">

    <div><b>Current index:</b></div>
    <div>Number of papers total: {{ num_papers }}</div>
    <div>Earliest paper: {{ earliest_paper }}</div>
    <div>Latest paper: {{ latest_paper }}</div>

    <br>

    <!-- thresholds are [1, 6, 12, 24, 48, 72, 96] -->
    <div><b>New paper counts flow:</b></div>
    <div>Number of new papers in the last 01 hours: {{ thr_1 }}</div>
    <div>Number of new papers in the last 06 hours: {{ thr_6 }}</div>
    <div>Number of new papers in the last 12 hours: {{ thr_12 }}</div>
    <div>Number of new papers in the last 24 hours: {{ thr_24 }}</div>
    <div>Number of new papers in the last 48 hours: {{ thr_48 }}</div>
    <div>Number of new papers in the last 72 hours: {{ thr_72 }}</div>
    <div>Number of new papers in the last 96 hours: {{ thr_96 }}</div>

</div>
{% endblock %}

{% block elements %}
{% endblock %}

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
