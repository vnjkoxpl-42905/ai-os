---
type: source
subject: "GitHub source repos/karpathy/arxiv-sanity-preserver/buildsvm.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-preserver/buildsvm.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/arxiv-sanity-preserver/buildsvm.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-preserver/buildsvm.py), SHA-256 `9d9b101fcf3863f267785578829d846cd52890b2fa5c7bed88f5287243a132c1`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "# standard imports import os import sys import pickle # non-standard imports import numpy as".

The preserver pipeline fetches versioned arXiv records incrementally with an explicit gentle wait and a stated early-stop assumption. PDFs are cached with timeouts; failed PDF conversion creates an empty marker, so attempted acquisition is not successful extraction. Analyze filters suspicious text lengths, fits TF-IDF on a seeded subset for memory efficiency, transforms the complete retained corpus and precomputes nearest neighbors. Buildsvm balances positive libraries against other papers. Make_cache precomputes dates, popularity and weighted lexical search to speed startup; its comments acknowledge missing bigram search. SQL defines user and library tables and contains destructive initialization statements that were read but never executed. Historical cache correctness, platform portability and completeness were not verified.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
# standard imports
import os
import sys
import pickle
# non-standard imports
import numpy as np
from sklearn import svm
from sqlite3 import dbapi2 as sqlite3
# local imports
from utils import safe_pickle_dump, strip_version, Config

num_recommendations = 1000 # papers to recommend per user
# -----------------------------------------------------------------------------

if not os.path.isfile(Config.database_path):
  print("the database file as.db should exist. You can create an empty database with sqlite3 as.db < schema.sql")
  sys.exit()

sqldb = sqlite3.connect(Config.database_path)
sqldb.row_factory = sqlite3.Row # to return dicts rather than tuples

def query_db(query, args=(), one=False):
  """Queries the database and returns a list of dictionaries."""
  cur = sqldb.execute(query, args)
  rv = cur.fetchall()
  return (rv[0] if rv else None) if one else rv

# -----------------------------------------------------------------------------

# fetch all users
users = query_db('''select * from user''')
print('number of users: ', len(users))

# load the tfidf matrix and meta
meta = pickle.load(open(Config.meta_path, 'rb'))
out = pickle.load(open(Config.tfidf_path, 'rb'))
X = out['X']
X = X.todense().astype(np.float32)

xtoi = { strip_version(x):i for x,i in meta['ptoi'].items() }

user_sim = {}
for ii,u in enumerate(users):
  print("%d/%d building an SVM for %s" % (ii, len(users), u['username'].encode('utf-8')))
  uid = u['user_id']
  lib = query_db('''select * from library where user_id = ?''', [uid])
  pids = [x['paper_id'] for x in lib] # raw pids without version
  posix = [xtoi[p] for p in pids if p in xtoi]
  
  if not posix:
    continue # empty library for this user maybe?

  print(pids)
  y = np.zeros(X.shape[0])
  for ix in posix: y[ix] = 1

  clf = svm.LinearSVC(class_weight='balanced', verbose=False, max_iter=10000, tol=1e-6, C=0.1)
  clf.fit(X,y)
  s = clf.decision_function(X)

  sortix = np.argsort(-s)
  sortix = sortix[:min(num_recommendations, len(sortix))] # crop paper recommendations to save space
  user_sim[uid] = [strip_version(meta['pids'][ix]) for ix in list(sortix)]

print('writing', Config.user_sim_path)
safe_pickle_dump(user_sim, Config.user_sim_path)

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
