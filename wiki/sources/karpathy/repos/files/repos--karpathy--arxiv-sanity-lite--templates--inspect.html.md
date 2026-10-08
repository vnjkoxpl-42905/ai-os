---
type: source
subject: "GitHub source repos/karpathy/arxiv-sanity-lite/templates/inspect.html"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/templates/inspect.html]
semantic-status: complete-named-text-read
---

# repos/karpathy/arxiv-sanity-lite/templates/inspect.html

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/templates/inspect.html), SHA-256 `3ab09536e5be257aa4d94a10529c2845277661091c68bcfc7e36b337f9a0d77d`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "{% extends \"base.html\" %} {% block variables %} <script> var paper = {{ paper |".

The arxiv-sanity-lite frontend exposes explicit ranking filters, tag shortcuts, paper feature weights, date-window statistics and responsive presentation. Its profile is deliberately username-only and warns email delivery may fail; this is a historical prototype rather than hardened authentication. The thumbnail daemon skips cached outputs and limits download and converter time, logging failures and terminating stuck conversion. Templates load external React and Babel, and some UI handling logs errors rather than displaying them. These files describe interface and reliability choices, not personal beliefs; no network or subprocess behavior was executed.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
{% extends "base.html" %}

{% block variables %}
<script>
var paper = {{ paper | tojson }};
var words = {{ words | tojson }};
var words_desc = {{ words_desc | tojson }};
</script>
{% endblock %}

{% block content %}
<div id="wrap">
</div>
<div id="wordwrap">
</div>
{% endblock %}

{% block elements %}
<script src="{{ url_for('static', filename='paper_detail.js') }}" type="text/babel"></script>
<script src="{{ url_for('static', filename='word_list.js') }}" type="text/babel"></script>
{% endblock %}

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
