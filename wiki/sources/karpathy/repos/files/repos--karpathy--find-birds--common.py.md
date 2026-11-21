---
type: source
subject: "GitHub source repos/karpathy/find-birds/common.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/find-birds/common.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/find-birds/common.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/find-birds/common.py), SHA-256 `2850b180d76a5da328a5bd0b6c29a251d38f51018a6e4a7dedaa82bdcc1724da`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
import os import time import tweepy import pickle def authenticate(): """ Reads keys from a
```

EigenLibSVM Karpathy-authored 2012 wrappers translate dense Eigen rows into LibSVM nodes, validate data/label dimensions and parameters, expose linear weights, C and model persistence, and explicitly warn about imbalance and missing cross-validation. Test prints expected MATLAB margins and approximately 0.945 training accuracy before and after save/load, rather than claiming held-out evaluation. Prediction allocates D nodes without the required terminating sentinel; source is historical and not correctness-certified. Matrix serialization helper credits Alex Teichman and notes newline-dependent ASCII parsing, so it is third-party evidence. Find-birds separates bounded depth-one acquisition with disk pickle caching and manual Tweepy error waits from offline recommendation: mutual-follow counts discounted by logarithmic popularity, expensive formatting only after top-list selection, then a plain HTML report. Incomplete cached users are explicitly skipped; remote descriptions inserted without escaping are a rendering limitation. These scripts were read without executing credentials, network collection or pickle payloads.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
import os
import time
import tweepy
import pickle

def authenticate():
    """
    Reads keys from a file, it's glorious.
    """
    # extract keys
    with open('twitter.txt', 'r') as f:
        keys = f.read().split()
    assert len(keys) == 4, "sorry to interupt, but there should be 4 lines in this file."
    # authenticate
    auth = tweepy.OAuthHandler(keys[0], keys[1])
    auth.set_access_token(keys[2], keys[3])
    api = tweepy.API(auth, wait_on_rate_limit=False, wait_on_rate_limit_notify=False)
    return api

def api_iter(api_func, user, limit):
    """
    Iterates API while error fetching correct. can't believe I have to do this manually and that
    it is not supported by tweepy. It claims to have it, but when I tried it crashed with an error.
    """
    if limit == 0: 
        return [] # fast escape when applicable
    
    it = tweepy.Cursor(api_func, id=user).items(limit)
    elements = []
    while True:
        try:
            f = it.next()
            elements.append(f)
        except tweepy.TweepError:
            print("got a tweepy error. collected %d/%d so far. waiting 15 minutes..." % (len(elements), limit))
            time.sleep(60 * 15 + 10)
            continue
        except StopIteration:
            break

    return elements

class LOLDB:
    """
    This class is a "database". haha
    """
    def __init__(self, dbpath):
        self.dbpath = dbpath
        if not os.path.isdir(dbpath):
            print("creating directory", dbpath)
            os.makedirs(dbpath)
    
    def _key_to_path(self, key):
        return os.path.join(self.dbpath, key+'.p')
    
    def __setitem__(self, key, item):
        with open(self._key_to_path(key), 'wb') as fp:
            pickle.dump(item, fp)

    def __getitem__(self, key):
        with open(self._key_to_path(key), 'rb') as fp:
            item = pickle.load(fp)
        return item
    
    def __contains__(self, key):
        pp = self._key_to_path(key)
        return os.path.isfile(pp)
    
```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
