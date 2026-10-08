---
type: source
subject: "GitHub source repos/karpathy/arxiv-sanity-lite/compute.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/compute.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/arxiv-sanity-lite/compute.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/compute.py), SHA-256 `57feea13e06e6047527a5aa24ce3d198c820636667c28ec6f34d34e135961471`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "\"\"\" Extracts tfidf features from all paper abstracts and saves them to disk. \"\"\" import".

Arxiv-sanity-lite intake batches 100 papers, preserves newest versions by timestamp, stops after unchanged batches to spare the API, and signals whether feature recomputation is needed. Inspection finds the retry counter advances on exceptions but not on short successful pages, so a short page can loop indefinitely; this was not reproduced. API parsing normalizes feed records and version IDs but assumes expected fields. Database helpers centralize paths and distinguish read-only/write-open modes; a StackOverflow-credited temporary-write/rename pattern protects pickle readers, with historical platform portability not certified. Compressed pickle storage assumes trusted local data. Feature computation fits TF-IDF on a possible subset then transforms all title/abstract/author text, stores float32 vectors and ID mappings. The Makefile is a convenience launcher, not an independently verified production scheduler.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""
Extracts tfidf features from all paper abstracts and saves them to disk.
"""

import argparse
from random import shuffle

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

from aslite.db import get_papers_db, save_features

# -----------------------------------------------------------------------------

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Arxiv Computor')
    parser.add_argument('-n', '--num', type=int, default=20000, help='number of tfidf features')
    parser.add_argument('--min_df', type=int, default=5, help='min df')
    parser.add_argument('--max_df', type=float, default=0.1, help='max df')
    parser.add_argument('--max_docs', type=int, default=-1, help='maximum number of documents to use when training tfidf, or -1 to disable')
    args = parser.parse_args()
    print(args)

    v = TfidfVectorizer(input='content',
                        encoding='utf-8', decode_error='replace', strip_accents='unicode',
                        lowercase=True, analyzer='word', stop_words='english',
                        token_pattern=r'(?u)\b[a-zA-Z_][a-zA-Z0-9_]+\b',
                        ngram_range=(1, 2), max_features=args.num,
                        norm='l2', use_idf=True, smooth_idf=True, sublinear_tf=True,
                        max_df=args.max_df, min_df=args.min_df)

    pdb = get_papers_db(flag='r')

    def make_corpus(training: bool):
        assert isinstance(training, bool)

        # determine which papers we will use to build tfidf
        if training and args.max_docs > 0 and args.max_docs < len(pdb):
            # crop to a random subset of papers
            keys = list(pdb.keys())
            shuffle(keys)
            keys = keys[:args.max_docs]
        else:
            keys = pdb.keys()

        # yield the abstracts of the papers
        for p in keys:
            d = pdb[p]
            author_str = ' '.join([a['name'] for a in d['authors']])
            yield ' '.join([d['title'], d['summary'], author_str])

    print("training tfidf vectors...")
    v.fit(make_corpus(training=True))

    print("running inference...")
    x = v.transform(make_corpus(training=False)).astype(np.float32)
    print(x.shape)

    print("saving to features to disk...")
    features = {
        'pids': list(pdb.keys()),
        'x': x,
        'vocab': v.vocabulary_,
        'idf': v._tfidf.idf_,
    }
    save_features(features)

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
