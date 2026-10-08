---
type: source
subject: "GitHub source repos/karpathy/arxiv-sanity-preserver/thumb_pdf.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-preserver/thumb_pdf.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/arxiv-sanity-preserver/thumb_pdf.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-preserver/thumb_pdf.py), SHA-256 `588984d3137c69567b183afc8618fd2142a26372a9596f69830d50f5f7bcc1c5`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
""" Use imagemagick to convert all pfds to a sequence of thumbnail images requires: sudo
```

The main template combines infinite scrolling with an explicit Load more fallback and time/version filters. Its hosting-cost prompt is optional and dismissible. Thumbnail extraction uses an inelegant intermediate-file approach because it was observed to succeed more often, limits a stuck converter to 20 seconds and substitutes a missing-image marker. Twitter daemon deduplicates IDs, filters recognized papers and banned accounts, explicitly labels popularity as hype, and favors meaningful commentary while capping displayed records. Its old authenticated API and unlimited retry loop were not executed or assumed usable now. Popularity weighting and fallback markers are operational heuristics, not correctness or completeness evidence.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""
Use imagemagick to convert all pfds to a sequence of thumbnail images
requires: sudo apt-get install imagemagick
"""

import os
import time
import shutil
from subprocess import Popen

from utils import Config

# make sure imagemagick is installed
if not shutil.which('convert'): # shutil.which needs Python 3.3+
  print("ERROR: you don\'t have imagemagick installed. Install it first before calling this script")
  sys.exit()

# create if necessary the directories we're using for processing and output
pdf_dir = os.path.join('data', 'pdf')
if not os.path.exists(Config.thumbs_dir): os.makedirs(Config.thumbs_dir)
if not os.path.exists(Config.tmp_dir): os.makedirs(Config.tmp_dir)

# fetch all pdf filenames in the pdf directory
files_in_pdf_dir = os.listdir(pdf_dir)
pdf_files = [x for x in files_in_pdf_dir if x.endswith('.pdf')] # filter to just pdfs, just in case

# iterate over all pdf files and create the thumbnails
for i,p in enumerate(pdf_files):
  pdf_path = os.path.join(pdf_dir, p)
  thumb_path = os.path.join(Config.thumbs_dir, p + '.jpg')

  if os.path.isfile(thumb_path): 
    print("skipping %s, thumbnail already exists." % (pdf_path, ))
    continue

  print("%d/%d processing %s" % (i, len(pdf_files), p))

  # take first 8 pages of the pdf ([0-7]), since 9th page are references
  # tile them horizontally, use JPEG compression 80, trim the borders for each image
  #cmd = "montage %s[0-7] -mode Concatenate -tile x1 -quality 80 -resize x230 -trim %s" % (pdf_path, "thumbs/" + f + ".jpg")
  #print "EXEC: " + cmd
  
  # nvm, below using a roundabout alternative that is worse and requires temporary files, yuck!
  # but i found that it succeeds more often. I can't remember wha thappened anymore but I remember
  # that the version above, while more elegant, had some problem with it on some pdfs. I think.

  # erase previous intermediate files thumb-*.png in the tmp directory
  if os.path.isfile(os.path.join(Config.tmp_dir, 'thumb-0.png')):
    for i in range(8):
      f = os.path.join(Config.tmp_dir, 'thumb-%d.png' % (i,))
      f2= os.path.join(Config.tmp_dir, 'thumbbuf-%d.png' % (i,))
      if os.path.isfile(f):
        cmd = 'mv %s %s' % (f, f2)
        os.system(cmd)
        # okay originally I was going to issue an rm call, but I am too terrified of
        # running scripted rm queries, so what we will do is instead issue a "mv" call
        # to rename the files. That's a bit safer, right? We have to do this because if
        # some papers are shorter than 8 pages, then results from previous paper will
        # "leek" over to this result, through the intermediate files.

  # spawn async. convert can unfortunately enter an infinite loop, have to handle this.
  # this command will generate 8 independent images thumb-0.png ... thumb-7.png of the thumbnails
  pp = Popen(['convert', '%s[0-7]' % (pdf_path, ), '-thumbnail', 'x156', os.path.join(Config.tmp_dir, 'thumb.png')])
  t0 = time.time()
  while time.time() - t0 < 20: # give it 15 seconds deadline
    ret = pp.poll()
    if not (ret is None):
      # process terminated
      break
    time.sleep(0.1)
  ret = pp.poll()
  if ret is None:
    print("convert command did not terminate in 20 seconds, terminating.")
    pp.terminate() # give up

  if not os.path.isfile(os.path.join(Config.tmp_dir, 'thumb-0.png')):
    # failed to render pdf, replace with missing image
    missing_thumb_path = os.path.join('static', 'missing.jpg')
    os.system('cp %s %s' % (missing_thumb_path, thumb_path))
    print("could not render pdf, creating a missing image placeholder")
  else:
    cmd = "montage -mode concatenate -quality 80 -tile x1 %s %s" % (os.path.join(Config.tmp_dir, 'thumb-*.png'), thumb_path)
    print(cmd)
    os.system(cmd)

  time.sleep(0.01) # silly way for allowing for ctrl+c termination

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
