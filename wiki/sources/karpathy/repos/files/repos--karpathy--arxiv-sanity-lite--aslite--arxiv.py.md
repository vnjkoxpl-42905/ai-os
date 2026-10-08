---
type: source
subject: "GitHub source repos/karpathy/arxiv-sanity-lite/aslite/arxiv.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/aslite/arxiv.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/arxiv-sanity-lite/aslite/arxiv.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/aslite/arxiv.py), SHA-256 `2269cee057c524a2d5d2593bd7a39f25694ccda4d11e5d85b3ae9d10804a248d`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "\"\"\" Utils for dealing with arxiv API and related processing \"\"\" import time import logging".

Arxiv-sanity-lite intake batches 100 papers, preserves newest versions by timestamp, stops after unchanged batches to spare the API, and signals whether feature recomputation is needed. Inspection finds the retry counter advances on exceptions but not on short successful pages, so a short page can loop indefinitely; this was not reproduced. API parsing normalizes feed records and version IDs but assumes expected fields. Database helpers centralize paths and distinguish read-only/write-open modes; a StackOverflow-credited temporary-write/rename pattern protects pickle readers, with historical platform portability not certified. Compressed pickle storage assumes trusted local data. Feature computation fits TF-IDF on a possible subset then transforms all title/abstract/author text, stores float32 vectors and ID mappings. The Makefile is a convenience launcher, not an independently verified production scheduler.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""
Utils for dealing with arxiv API and related processing
"""

import time
import logging
import urllib.request
import feedparser
from collections import OrderedDict

logger = logging.getLogger(__name__)

def get_response(search_query, start_index=0):
    """ pings arxiv.org API to fetch a batch of 100 papers """
    # fetch raw response
    base_url = 'http://export.arxiv.org/api/query?'
    add_url = 'search_query=%s&sortBy=lastUpdatedDate&start=%d&max_results=100' % (search_query, start_index)
    #add_url = 'search_query=%s&sortBy=submittedDate&start=%d&max_results=100' % (search_query, start_index)
    search_query = base_url + add_url
    logger.debug(f"Searching arxiv for {search_query}")
    with urllib.request.urlopen(search_query) as url:
        response = url.read()

    if url.status != 200:
        logger.error(f"arxiv did not return status 200 response")

    return response

def encode_feedparser_dict(d):
    """ helper function to strip feedparser objects using a deep copy """
    if isinstance(d, feedparser.FeedParserDict) or isinstance(d, dict):
        return {k: encode_feedparser_dict(d[k]) for k in d.keys()}
    elif isinstance(d, list):
        return [encode_feedparser_dict(k) for k in d]
    else:
        return d

def parse_arxiv_url(url):
    """
    examples is http://arxiv.org/abs/1512.08756v2
    we want to extract the raw id (1512.08756) and the version (2)
    """
    ix = url.rfind('/')
    assert ix >= 0, 'bad url: ' + url
    idv = url[ix+1:] # extract just the id (and the version)
    parts = idv.split('v')
    assert len(parts) == 2, 'error splitting id and version in idv string: ' + idv
    return idv, parts[0], int(parts[1])

def parse_response(response):

    out = []
    parse = feedparser.parse(response)
    for e in parse.entries:
        j = encode_feedparser_dict(e)
        # extract / parse id information
        idv, rawid, version = parse_arxiv_url(j['id'])
        j['_idv']= idv
        j['_id'] = rawid
        j['_version'] = version
        j['_time'] = time.mktime(j['updated_parsed'])
        j['_time_str'] = time.strftime('%b %d %Y', j['updated_parsed'])
        # delete apparently spurious and redundant information
        del j['summary_detail']
        del j['title_detail']
        out.append(j)

    return out

def filter_latest_version(idvs):
    """
    for each idv filter the list down to only the most recent version
    """

    pid_to_v = OrderedDict()
    for idv in idvs:
        pid, v = idv.split('v')
        pid_to_v[pid] = max(int(v), pid_to_v.get(pid, 0))

    filt = [f"{pid}v{v}" for pid, v in pid_to_v.items()]
    return filt
```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
