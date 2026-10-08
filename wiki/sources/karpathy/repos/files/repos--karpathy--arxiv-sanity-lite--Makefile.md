---
type: source
subject: "GitHub source repos/karpathy/arxiv-sanity-lite/Makefile"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/Makefile]
semantic-status: complete-named-text-read
---

# repos/karpathy/arxiv-sanity-lite/Makefile

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/Makefile), SHA-256 `1184d5ca43ce7424d1a04b8074facc13a6a6acaf211d52e2bf336e6cf5a33932`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
# I run this to update the database with newest papers every day or so
```

Arxiv-sanity-lite intake batches 100 papers, preserves newest versions by timestamp, stops after unchanged batches to spare the API, and signals whether feature recomputation is needed. Inspection finds the retry counter advances on exceptions but not on short successful pages, so a short page can loop indefinitely; this was not reproduced. API parsing normalizes feed records and version IDs but assumes expected fields. Database helpers centralize paths and distinguish read-only/write-open modes; a StackOverflow-credited temporary-write/rename pattern protects pickle readers, with historical platform portability not certified. Compressed pickle storage assumes trusted local data. Feature computation fits TF-IDF on a possible subset then transforms all title/abstract/author text, stores float32 vectors and ID mappings. The Makefile is a convenience launcher, not an independently verified production scheduler.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text

# I run this to update the database with newest papers every day or so or etc.
up:
	python arxiv_daemon.py --num 2000
	python compute.py

# I use this to run the server
fun:
	export FLASK_APP=serve.py; flask run

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
