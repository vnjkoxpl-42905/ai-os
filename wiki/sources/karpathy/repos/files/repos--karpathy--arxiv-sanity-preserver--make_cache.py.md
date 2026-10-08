---
type: source
subject: "GitHub source repos/karpathy/arxiv-sanity-preserver/make_cache.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-preserver/make_cache.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/arxiv-sanity-preserver/make_cache.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-preserver/make_cache.py), SHA-256 `50f4c9eafa992e8f65554adb5a38eb0458ab4491e01f3733f4654611e9a9851d`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "\"\"\" computes various cache things on top of db.py so that the server (running from".

The preserver pipeline fetches versioned arXiv records incrementally with an explicit gentle wait and a stated early-stop assumption. PDFs are cached with timeouts; failed PDF conversion creates an empty marker, so attempted acquisition is not successful extraction. Analyze filters suspicious text lengths, fits TF-IDF on a seeded subset for memory efficiency, transforms the complete retained corpus and precomputes nearest neighbors. Buildsvm balances positive libraries against other papers. Make_cache precomputes dates, popularity and weighted lexical search to speed startup; its comments acknowledge missing bigram search. SQL defines user and library tables and contains destructive initialization statements that were read but never executed. Historical cache correctness, platform portability and completeness were not verified.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""
computes various cache things on top of db.py so that the server
(running from serve.py) can start up and serve faster when restarted.

this script should be run whenever db.p is updated, and 
creates db2.p, which can be read by the server.
"""

import os
import json
import time
import pickle
import dateutil.parser

from sqlite3 import dbapi2 as sqlite3
from utils import safe_pickle_dump, Config

sqldb = sqlite3.connect(Config.database_path)
sqldb.row_factory = sqlite3.Row # to return dicts rather than tuples

CACHE = {}

print('loading the paper database', Config.db_path)
db = pickle.load(open(Config.db_path, 'rb'))

print('loading tfidf_meta', Config.meta_path)
meta = pickle.load(open(Config.meta_path, "rb"))
vocab = meta['vocab']
idf = meta['idf']

print('decorating the database with additional information...')
for pid,p in db.items():
  timestruct = dateutil.parser.parse(p['updated'])
  p['time_updated'] = int(timestruct.strftime("%s")) # store in struct for future convenience
  timestruct = dateutil.parser.parse(p['published'])
  p['time_published'] = int(timestruct.strftime("%s")) # store in struct for future convenience

print('computing min/max time for all papers...')
tts = [time.mktime(dateutil.parser.parse(p['updated']).timetuple()) for pid,p in db.items()]
ttmin = min(tts)*1.0
ttmax = max(tts)*1.0
for pid,p in db.items():
  tt = time.mktime(dateutil.parser.parse(p['updated']).timetuple())
  p['tscore'] = (tt-ttmin)/(ttmax-ttmin)

print('precomputing papers date sorted...')
scores = [(p['time_updated'], pid) for pid,p in db.items()]
scores.sort(reverse=True, key=lambda x: x[0])
CACHE['date_sorted_pids'] = [sp[1] for sp in scores]

# compute top papers in peoples' libraries
print('computing top papers...')
libs = sqldb.execute('''select * from library''').fetchall()
counts = {}
for lib in libs:
  pid = lib['paper_id']
  counts[pid] = counts.get(pid, 0) + 1
top_paper_counts = sorted([(v,k) for k,v in counts.items() if v > 0], reverse=True)
CACHE['top_sorted_pids'] = [q[1] for q in top_paper_counts]

# some utilities for creating a search index for faster search
punc = "'!\"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~'" # removed hyphen from string.punctuation
trans_table = {ord(c): None for c in punc}
def makedict(s, forceidf=None, scale=1.0):
  words = set(s.lower().translate(trans_table).strip().split())
  idfd = {}
  for w in words: # todo: if we're using bigrams in vocab then this won't search over them
    if forceidf is None:
      if w in vocab:
        # we have idf for this
        idfval = idf[vocab[w]]*scale
      else:
        idfval = 1.0*scale # assume idf 1.0 (low)
    else:
      idfval = forceidf
    idfd[w] = idfval
  return idfd

def merge_dicts(dlist):
  m = {}
  for d in dlist:
    for k,v in d.items():
      m[k] = m.get(k,0) + v
  return m

print('building an index for faster search...')
search_dict = {}
for pid,p in db.items():
  dict_title = makedict(p['title'], forceidf=5, scale=3)
  dict_authors = makedict(' '.join(x['name'] for x in p['authors']), forceidf=5)
  dict_categories = {x['term'].lower():5 for x in p['tags']}
  if 'and' in dict_authors: 
    # special case for "and" handling in authors list
    del dict_authors['and']
  dict_summary = makedict(p['summary'])
  search_dict[pid] = merge_dicts([dict_title, dict_authors, dict_categories, dict_summary])
CACHE['search_dict'] = search_dict

# save the cache
print('writing', Config.serve_cache_path)
safe_pickle_dump(CACHE, Config.serve_cache_path)
print('writing', Config.db_serve_path)
safe_pickle_dump(db, Config.db_serve_path)

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
