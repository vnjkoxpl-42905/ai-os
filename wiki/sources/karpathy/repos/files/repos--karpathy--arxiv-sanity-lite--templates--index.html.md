---
type: source
subject: "GitHub source repos/karpathy/arxiv-sanity-lite/templates/index.html"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/templates/index.html]
semantic-status: complete-named-text-read
---

# repos/karpathy/arxiv-sanity-lite/templates/index.html

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/templates/index.html), SHA-256 `61f1a2750f6cd4e09a5d514b959a695557ab6df9d43201dc0a40fb62c82ba177`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
{% extends "base.html" %} {% block variables %} <script> var papers = {{ papers |
```

The arxiv-sanity-lite frontend exposes explicit ranking filters, tag shortcuts, paper feature weights, date-window statistics and responsive presentation. Its profile is deliberately username-only and warns email delivery may fail; this is a historical prototype rather than hardened authentication. The thumbnail daemon skips cached outputs and limits download and converter time, logging failures and terminating stuck conversion. Templates load external React and Babel, and some UI handling logs errors rather than displaying them. These files describe interface and reliability choices, not personal beliefs; no network or subprocess behavior was executed.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
{% extends "base.html" %}

{% block variables %}
<script>
var papers = {{ papers | tojson }};
var tags = {{ tags | tojson }};
var words = {{ words | tojson }};
var words_desc = {{ words_desc | tojson }};
var gvars = {{ gvars | tojson }};

/*
JS code here handles pagination. I really don't super love this approach,
if anyone can think of a cleaner / shorter way please let me know.
*/
var move_page = function(int_offset) {
    var queryParams = new URLSearchParams(window.location.search);
    queryParams.set("page_number", Math.max(1, parseInt(gvars.page_number) + int_offset));
    window.location.href = '/?' + queryParams.toString();
}
</script>
{% endblock %}

{% block content %}

{% if not user %}
<div id="log-fun-warn">(hi! just btw you have to be logged in to be able to add/delete/curate tags for papers and get recommendations)</div>
{% endif %}

<div id="controls">
    <div>

        <!-- the choice box, allowing us to sort, rank, slice and dice papers -->
        <div id="cbox">
            <form action="/" method="get">

                <!-- the search box, allowing us to search by keywords -->
                <input name="q" type="text" id="qfield" value="{{ gvars.search_query }}">

                <!-- rank type: one of tags, pid, time, or random -->
                <label for="rank_type">Rank by:</label>
                <select name="rank" id="rank_select">
                    <option value="search" {{ gvars.rank == 'search' and 'selected' }}>search</option>
                    <option value="tags" {{ gvars.rank == 'tags' and 'selected' }}>tags</option>
                    <option value="pid" {{ gvars.rank == 'pid' and 'selected' }}>pid</option>
                    <option value="time" {{ gvars.rank == 'time' and 'selected' }}>time</option>
                    <option value="random" {{ gvars.rank == 'random' and 'selected' }}>random</option>
                </select>

                <!-- current tags, simply in a text field -->
                <label for="tags">tags: </label>
                <input name="tags" type="text" id="tags_field" value="{{ gvars.tags }}">

                <!-- current pid, simply in a text field -->
                <label for="pid">pid: </label>
                <input name="pid" type="text" id="pid_field" value="{{ gvars.pid }}">

                <!-- current time_filter, in a text field -->
                <label for="time_filter">time_filter (days): </label>
                <input name="time_filter" type="text" id="time_filter_field" value="{{ gvars.time_filter }}">

                <!-- current svm_c, in a text field -->
                <label for="svm_c">svm_c: </label>
                <input name="svm_c" type="text" id="svm_c_field" value="{{ gvars.svm_c }}">

                <!-- current skip_have: one of yes or no -->
                <label for="skip_have">skip_have: </label>
                <select name="skip_have" id="skip_have_select">
                    <option value="yes" {{ gvars.skip_have == 'yes' and 'selected' }}>yes</option>
                    <option value="no" {{ gvars.skip_have == 'no' and 'selected' }}>no</option>
                </select>

                <input type="submit" value="Submit">
            </form>
        </div>
        <!-- some hand-coded common choices for faster and more convenient operation -->
        <div id="cbox_fast">
            Shortcuts:
            <a href="/?rank=tags&tags=all&time_filter=7&skip_have=yes">recommend over last week</a>
            <a href="/?rank=tags&tags=all&time_filter=3&skip_have=yes">recommend over last 3 days</a>
            <a href="/?rank=time">recent</a>
            <a href="/?rank=random&time_filter=7">random last week</a>
        </div>
    </div>
    <div>

    </div>
</div>

{% if user and tags %}
<div id="tagwrap">
</div>
{% endif %}

{% if user and words %}
<div id="wordwrap" style="display:none;">
</div>
{% endif %}

<!-- main content showing all the papers as a list -->
<div id="wrap">
</div>

<!-- links to previous and next pages -->
<div id="pagination">
    <span id="link-prev-page" onclick='move_page(-1);'>prev</span>
    <span>current page: {{ gvars.page_number }} </span>
    <span id="link-next-page" onclick='move_page(1);'>next</span>
</div>
{% endblock %}

{% block elements %}
<script src="{{ url_for('static', filename='paper_list.js') }}" type="text/babel"></script>
<script src="{{ url_for('static', filename='word_list.js') }}" type="text/babel"></script>
{% endblock %}

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
