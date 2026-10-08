---
type: source
subject: "GitHub source repos/karpathy/arxiv-sanity-lite/aslite/db.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/aslite/db.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/arxiv-sanity-lite/aslite/db.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/aslite/db.py), SHA-256 `d349ea7181063fef466797a5105eec4b70659de91eee91d5759869f1cb6dbd54`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "\"\"\" Database support functions. The idea is that none of the individual scripts deal directly".

Arxiv-sanity-lite intake batches 100 papers, preserves newest versions by timestamp, stops after unchanged batches to spare the API, and signals whether feature recomputation is needed. Inspection finds the retry counter advances on exceptions but not on short successful pages, so a short page can loop indefinitely; this was not reproduced. API parsing normalizes feed records and version IDs but assumes expected fields. Database helpers centralize paths and distinguish read-only/write-open modes; a StackOverflow-credited temporary-write/rename pattern protects pickle readers, with historical platform portability not certified. Compressed pickle storage assumes trusted local data. Feature computation fits TF-IDF on a possible subset then transforms all title/abstract/author text, stores float32 vectors and ID mappings. The Makefile is a convenience launcher, not an independently verified production scheduler.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""
Database support functions.
The idea is that none of the individual scripts deal directly with the file system.
Any of the file system I/O and the associated settings are in this single file.
"""

import os
import sqlite3, zlib, pickle, tempfile
from sqlitedict import SqliteDict
from contextlib import contextmanager

# -----------------------------------------------------------------------------
# global configuration

DATA_DIR = 'data'

# -----------------------------------------------------------------------------
# utilities for safe writing of a pickle file

# Context managers for atomic writes courtesy of
# http://stackoverflow.com/questions/2333872/atomic-writing-to-file-with-python
@contextmanager
def _tempfile(*args, **kws):
    """ Context for temporary file.
    Will find a free temporary filename upon entering
    and will try to delete the file on leaving
    Parameters
    ----------
    suffix : string
        optional file suffix
    """

    fd, name = tempfile.mkstemp(*args, **kws)
    os.close(fd)
    try:
        yield name
    finally:
        try:
            os.remove(name)
        except OSError as e:
            if e.errno == 2:
                pass
            else:
                raise e


@contextmanager
def open_atomic(filepath, *args, **kwargs):
    """ Open temporary file object that atomically moves to destination upon
    exiting.
    Allows reading and writing to and from the same filename.
    Parameters
    ----------
    filepath : string
        the file path to be opened
    fsync : bool
        whether to force write the file to disk
    kwargs : mixed
        Any valid keyword arguments for :code:`open`
    """
    fsync = kwargs.pop('fsync', False)

    with _tempfile(dir=os.path.dirname(filepath)) as tmppath:
        with open(tmppath, *args, **kwargs) as f:
            yield f
            if fsync:
                f.flush()
                os.fsync(f.fileno())
        os.rename(tmppath, filepath)

def safe_pickle_dump(obj, fname):
    """
    prevents a case where one process could be writing a pickle file
    while another process is reading it, causing a crash. the solution
    is to write the pickle file to a temporary file and then move it.
    """
    with open_atomic(fname, 'wb') as f:
        pickle.dump(obj, f, -1) # -1 specifies highest binary protocol

# -----------------------------------------------------------------------------

class CompressedSqliteDict(SqliteDict):
    """ overrides the encode/decode methods to use zlib, so we get compressed storage """

    def __init__(self, *args, **kwargs):

        def encode(obj):
            return sqlite3.Binary(zlib.compress(pickle.dumps(obj, pickle.HIGHEST_PROTOCOL)))

        def decode(obj):
            return pickle.loads(zlib.decompress(bytes(obj)))

        super().__init__(*args, **kwargs, encode=encode, decode=decode)

# -----------------------------------------------------------------------------
"""
some docs to self:
flag='c': default mode, open for read/write, and creating the db/table if necessary
flag='r': open for read-only
"""

# stores info about papers, and also their lighter-weight metadata
PAPERS_DB_FILE = os.path.join(DATA_DIR, 'papers.db')
# stores account-relevant info, like which tags exist for which papers
DICT_DB_FILE = os.path.join(DATA_DIR, 'dict.db')

def get_papers_db(flag='r', autocommit=True):
    assert flag in ['r', 'c']
    pdb = CompressedSqliteDict(PAPERS_DB_FILE, tablename='papers', flag=flag, autocommit=autocommit)
    return pdb

def get_metas_db(flag='r', autocommit=True):
    assert flag in ['r', 'c']
    mdb = SqliteDict(PAPERS_DB_FILE, tablename='metas', flag=flag, autocommit=autocommit)
    return mdb

def get_tags_db(flag='r', autocommit=True):
    assert flag in ['r', 'c']
    tdb = CompressedSqliteDict(DICT_DB_FILE, tablename='tags', flag=flag, autocommit=autocommit)
    return tdb

def get_last_active_db(flag='r', autocommit=True):
    assert flag in ['r', 'c']
    ladb = SqliteDict(DICT_DB_FILE, tablename='last_active', flag=flag, autocommit=autocommit)
    return ladb

def get_email_db(flag='r', autocommit=True):
    assert flag in ['r', 'c']
    edb = SqliteDict(DICT_DB_FILE, tablename='email', flag=flag, autocommit=autocommit)
    return edb

# -----------------------------------------------------------------------------
"""
our "feature store" is currently just a pickle file, may want to consider hdf5 in the future
"""

# stores tfidf features a bunch of other metadata
FEATURES_FILE = os.path.join(DATA_DIR, 'features.p')

def save_features(features):
    """ takes the features dict and save it to disk in a simple pickle file """
    safe_pickle_dump(features, FEATURES_FILE)

def load_features():
    """ loads the features dict from disk """
    with open(FEATURES_FILE, 'rb') as f:
        features = pickle.load(f)
    return features

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
