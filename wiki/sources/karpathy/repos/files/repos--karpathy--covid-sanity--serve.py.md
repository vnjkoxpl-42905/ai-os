---
type: source
subject: "GitHub source repos/karpathy/covid-sanity/serve.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/covid-sanity/serve.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/covid-sanity/serve.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/covid-sanity/serve.py), SHA-256 `af8d04221aca824ab76d1e12faa012dbaee1eb61fcb228776990fe234cc14e7d`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "\"\"\" Simple flask server for the interface \"\"\" import os import json from flask import".

Convnet neural-net specs verify desugared layer count, normalized probabilities, increased ground-truth probability after a small unregularized update and finite-difference input gradients; comments explicitly qualify step size and coverage. Specs were read, not run; analytic gradients are taken before an update and numeric losses afterward, a comparison limitation. Jasmine license/runner preserve third-party dependency provenance. Covid-sanity updater fetches BioRxiv collection, uses title-plus-abstract unigram TF-IDF, balanced exemplar SVM similarities and a weighted inverted search dictionary prioritizing title and authors. Flask loads local generated JSON, adapts changed author API schema to a legacy string, ranks optional tweets by follower count and returns at most forty search or latest papers with a small recency boost. React shows abstracts, PDF/similarity links and expandable tweets. Fixed-width styling and CDN/Babel template are historical implementation choices. Banned list excludes automated preprint accounts. No current API availability or deployed behavior verified.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""
Simple flask server for the interface
"""

import os
import json

from flask import Flask, request, redirect, url_for
from flask import render_template

# -----------------------------------------------------------------------------

app = Flask(__name__)

# load raw paper data
with open('jall.json', 'r') as f:
    jall = json.load(f)
# this is crazy, I think they just recently changed this API
# for now converting to "legacy format" as just a string as a quick fix
for j in jall['rels']:
    if isinstance(j['rel_authors'], list):
        j['rel_authors'] = '; '.join(a['author_name'] for a in j['rel_authors'])

# load computed paper similarities
with open('sim_tfidf_svm.json', 'r') as f:
    sim_dict = json.load(f)

# load search dictionary for each paper
with open('search.json', 'r') as f:
    search_dict = json.load(f)

# OPTIONAL: load tweet dictionary, if twitter_daemon has run
tweets_dict = {}
if os.path.isfile('tweets.json'):
    with open('tweets.json', 'r') as f:
        tweets_dict = json.load(f)
# decorate each paper with tweets
for j in jall['rels']:
    j['tweets'] = tweets_dict.get(j['rel_doi'], [])
    j['tweets'].sort(key=lambda t: t['followers'], reverse=True)

# do some precomputation since we're going to be doing lookups of doi -> doc index
doi_to_ix = {}
for i, j in enumerate(jall['rels']):
    doi_to_ix[j['rel_doi']] = i

# -----------------------------------------------------------------------------
# few helper functions for routes

def default_context(papers, **kwargs):
    """ build a default context for the frontend """
    gvars = {'num_papers': len(jall['rels'])}
    gvars.update(kwargs) # insert anything else from kwargs into global context
    context = {'papers': papers, 'gvars': gvars}
    return context

# -----------------------------------------------------------------------------
# routes below

@app.route("/search", methods=['GET'])
def search():
    q = request.args.get('q', '') # get the search request
    if not q:
        return redirect(url_for('main')) # if someone just hits enter with empty field

    qparts = q.lower().strip().split() # split by spaces

    # accumulate scores
    n = len(jall['rels'])
    scores = []
    for i, sd in enumerate(search_dict):
        score = sum(sd.get(q, 0) for q in qparts)
        if score == 0:
            continue # no match whatsoever, dont include
        score += 1.0 * (n - i)/n # give a small boost to more recent papers (low index)
        scores.append((score, jall['rels'][i]))
    scores.sort(reverse=True, key=lambda x: x[0]) # descending
    papers = [x[1] for x in scores if x[0] > 0]
    if len(papers) > 40:
        papers = papers[:40]
    context = default_context(papers, sort_order='search', search_query=q)
    return render_template('index.html', **context)

@app.route('/sim/<doi_prefix>/<doi_suffix>')
def sim(doi_prefix=None, doi_suffix=None):
    doi = f"{doi_prefix}/{doi_suffix}" # reconstruct the full doi
    pix = doi_to_ix.get(doi)
    if pix is None:
        papers = []
    else:
        sim_ix = sim_dict[pix]
        papers = [jall['rels'][cix] for cix in sim_ix]
    context = default_context(papers, sort_order='sim')
    return render_template('index.html', **context)

@app.route('/')
def main():
    papers = jall['rels'][:40]
    context = default_context(papers, sort_order='latest')
    return render_template('index.html', **context)

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
