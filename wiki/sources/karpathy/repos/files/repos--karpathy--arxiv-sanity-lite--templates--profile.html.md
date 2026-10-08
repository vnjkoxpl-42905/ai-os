---
type: source
subject: "GitHub source repos/karpathy/arxiv-sanity-lite/templates/profile.html"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/templates/profile.html]
semantic-status: complete-named-text-read
---

# repos/karpathy/arxiv-sanity-lite/templates/profile.html

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/templates/profile.html), SHA-256 `aeace710b81c7e690bcf28374ab43ffdd20c3a062f1be3ee84fd270661bb42af`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

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
<div id="profilewrap">

    {% if user %}
    <div>
        <div>
            <div><b>Current session</b></div>
            <div>Logged in user: {{ user }}</div>
        </div>
        <br>
        <div>
            <div><b>Email recommendations</b></div>
            <div>
                Users can receive regular new paper recommendations via email based on their tags.
                (This is still being developed, may not be running or may be unreliable.)
                Register your email address below to receive these recommendations.
                To stop the recommendations simply delete your email address.
            </div>
            <div>
                <form id="email-form" action="{{ url_for('register_email') }}" method="post">
                    <div class="form-group">
                        <input type="text" class="form-control" name="email" placeholder="Email address" value="{{ email }}">
                    </div>
                    <input type="submit" class="btn" value="Set">
                </form>
            </div>
        </div>
        <br>
        <div>
            <a href="{{ url_for('logout') }}">Log out</a>
        </div>
    </div>
    {% else %}
    <div>

        <div id="profile-warning">
            <p>
            Okay, arxiv-sanity-lite uses a super lite version of
            "user accounts" where there are no passwords. Basically, you can "log in"
            with any arbitrary username. If you want to share your library with a
            friend, you can just tell them the username. And if you'd like to keep your
            account private, just make your username be something unique
            and write it down somewhere safe.
            </p>
            <b>TLDR: there are no passwords!</b>
        </div>

        <form id="profile-login-form" action="/login" method="POST">
            <div class="form-group">
              <label>Username:</label>
              <input class="form-control" type="text" name="username">
            </div>
            <button type="submit" class="btn">Log in</button>
        </form>
    </div>
    {% endif %}

</div>
{% endblock %}

{% block elements %}
{% endblock %}

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
