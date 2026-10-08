---
type: source
subject: "GitHub source repos/karpathy/arxiv-sanity-lite/templates/base.html"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/templates/base.html]
semantic-status: complete-named-text-read
---

# repos/karpathy/arxiv-sanity-lite/templates/base.html

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/templates/base.html), SHA-256 `4f7edb01d16d0ae0effb44ba36d0e9854540fc541ea8b6407eee5a2d642408b5`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "<!DOCTYPE HTML> <html> <head> <!-- meta info --> <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\"> <meta name=\"viewport\" content=\"width=device-width,".

The arxiv-sanity-lite frontend exposes explicit ranking filters, tag shortcuts, paper feature weights, date-window statistics and responsive presentation. Its profile is deliberately username-only and warns email delivery may fail; this is a historical prototype rather than hardened authentication. The thumbnail daemon skips cached outputs and limits download and converter time, logging failures and terminating stuck conversion. Templates load external React and Babel, and some UI handling logs errors rather than displaying them. These files describe interface and reliability choices, not personal beliefs; no network or subprocess behavior was executed.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
<!DOCTYPE HTML>
<html>

<head>
<!-- meta info -->
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>arxiv-sanity</title>
<!-- CSS -->
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
<!-- Favicon -->
<link rel="shortcut icon" type="image/png" href="{{ url_for('static', filename='favicon.png') }}" />

<script>
var user = {{ user | tojson }};
</script>
{% block variables %}
{% endblock %}

</head>

<body>
<div id="header">
    <a href="/" id="home-link">arxiv-sanity</a>
    <a href="/profile" id="login-link">
        {{ 'profile' if user else 'login' }}
    </a>
    <a href="/stats" id="stats-link">stats</a>
    <a href="/about" id="stats-link">about</a>
</div>

{% block content %}
{% endblock %}

<!-- React -->
<script src="https://unpkg.com/react@16/umd/react.production.min.js" crossorigin></script>
<script src="https://unpkg.com/react-dom@16/umd/react-dom.production.min.js" crossorigin></script>
<!-- Babel for displaying JSX -->
<script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
<!-- Load our React component -->
{% block elements %}
{% endblock %}

</body>
</html>

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
