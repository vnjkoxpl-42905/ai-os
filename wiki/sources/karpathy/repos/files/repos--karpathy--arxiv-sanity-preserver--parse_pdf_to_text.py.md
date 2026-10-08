---
type: source
subject: "GitHub source repos/karpathy/arxiv-sanity-preserver/parse_pdf_to_text.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-preserver/parse_pdf_to_text.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/arxiv-sanity-preserver/parse_pdf_to_text.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-preserver/parse_pdf_to_text.py), SHA-256 `73f1b08d2bd3b29247fdda2384e81e71b68555ef6a02046ce5e11e9630fe6159`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "\"\"\" Very simple script that simply iterates over all files data/pdf/f.pdf and create a file".

The preserver pipeline fetches versioned arXiv records incrementally with an explicit gentle wait and a stated early-stop assumption. PDFs are cached with timeouts; failed PDF conversion creates an empty marker, so attempted acquisition is not successful extraction. Analyze filters suspicious text lengths, fits TF-IDF on a seeded subset for memory efficiency, transforms the complete retained corpus and precomputes nearest neighbors. Buildsvm balances positive libraries against other papers. Make_cache precomputes dates, popularity and weighted lexical search to speed startup; its comments acknowledge missing bigram search. SQL defines user and library tables and contains destructive initialization statements that were read but never executed. Historical cache correctness, platform portability and completeness were not verified.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""
Very simple script that simply iterates over all files data/pdf/f.pdf
and create a file data/txt/f.pdf.txt that contains the raw text, extracted
using the "pdftotext" command. If a pdf cannot be converted, this
script will not produce the output file.
"""

import os
import sys
import time
import shutil
import pickle

from utils import Config

# make sure pdftotext is installed
if not shutil.which('pdftotext'): # needs Python 3.3+
  print('ERROR: you don\'t have pdftotext installed. Install it first before calling this script')
  sys.exit()

if not os.path.exists(Config.txt_dir):
  print('creating ', Config.txt_dir)
  os.makedirs(Config.txt_dir)

have = set(os.listdir(Config.txt_dir))
files = os.listdir(Config.pdf_dir)
for i,f in enumerate(files): # there was a ,start=1 here that I removed, can't remember why it would be there. shouldn't be, i think.

  txt_basename = f + '.txt'
  if txt_basename in have:
    print('%d/%d skipping %s, already exists.' % (i, len(files), txt_basename, ))
    continue

  pdf_path = os.path.join(Config.pdf_dir, f)
  txt_path = os.path.join(Config.txt_dir, txt_basename)
  cmd = "pdftotext %s %s" % (pdf_path, txt_path)
  os.system(cmd)

  print('%d/%d %s' % (i, len(files), cmd))

  # check output was made
  if not os.path.isfile(txt_path):
    # there was an error with converting the pdf
    print('there was a problem with parsing %s to text, creating an empty text file.' % (pdf_path, ))
    os.system('touch ' + txt_path) # create empty file, but it's a record of having tried to convert

  time.sleep(0.01) # silly way for allowing for ctrl+c termination


```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
