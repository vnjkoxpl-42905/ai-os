---
type: source
subject: "GitHub source repos/karpathy/find-birds/fetch.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/find-birds/fetch.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/find-birds/fetch.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/find-birds/fetch.py), SHA-256 `01a8fb35b361042d99cbd217e86ec14ab705f0ab8b587dc916ac9b0db3e3c5a7`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
import os import time import logging import argparse import tweepy from common import authenticate, api_iter,
```

EigenLibSVM Karpathy-authored 2012 wrappers translate dense Eigen rows into LibSVM nodes, validate data/label dimensions and parameters, expose linear weights, C and model persistence, and explicitly warn about imbalance and missing cross-validation. Test prints expected MATLAB margins and approximately 0.945 training accuracy before and after save/load, rather than claiming held-out evaluation. Prediction allocates D nodes without the required terminating sentinel; source is historical and not correctness-certified. Matrix serialization helper credits Alex Teichman and notes newline-dependent ASCII parsing, so it is third-party evidence. Find-birds separates bounded depth-one acquisition with disk pickle caching and manual Tweepy error waits from offline recommendation: mutual-follow counts discounted by logarithmic popularity, expensive formatting only after top-list selection, then a plain HTML report. Incomplete cached users are explicitly skipped; remote descriptions inserted without escaping are a rendering limitation. These scripts were read without executing credentials, network collection or pickle payloads.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
import os
import time
import logging
import argparse

import tweepy

from common import authenticate, api_iter, LOLDB

# -----------------------------------------------------------------------------
parser = argparse.ArgumentParser()
# required arguments
parser.add_argument('user', type=str, help='The user to get information about')
# options
parser.add_argument('-d', '--depth', type=int, default=0, help='Fetch just the single user, or also all of their friends recurisvely.')
parser.add_argument('-n', '--max-friends', type=int, default=1000, help='Maximum number of latest friends we fetch per any user.')
parser.add_argument('-m', '--max-tweets', type=int, default=200, help='Maximum number of latest tweets we fetch per any user.')
parser.add_argument('-x', '--cache', type=int, default=1, help='If we already have the user in database, skip? 1/0')
parser.add_argument('-i', '--db-dir', type=str, default="db", help='Folder where we store all of the information')
args = parser.parse_args()
# -----------------------------------------------------------------------------

assert args.depth in [0,1], "for now depth should be either 0 or 1. Anything else is likely to take way too long."

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

api = authenticate()
db = LOLDB(args.db_dir)

def download_user(user):
    if args.cache and user in db:
        return # nothing to be done
    # hit the Twitter API to get the information
    friends = api_iter(api.friends, user, args.max_friends)
    tweets = api_iter(api.user_timeline, user, args.max_tweets)
    blob = { 'time':time.time(), 'friends': friends, 'tweets': tweets }
    # back the information up in database for later
    db[user] = blob

logging.info("fetching user %s" % (args.user, ))
download_user(args.user)
b = db[args.user]
if args.depth == 1:
    for i,f in enumerate(b['friends']):
        logging.info("%d/%d fetching a friend %s" % (i+1, len(b['friends']), f.screen_name))
        download_user(f.screen_name)

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
