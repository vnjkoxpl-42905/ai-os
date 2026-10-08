---
type: source
subject: "GitHub source repos/karpathy/nipspreview/Readme.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nipspreview/Readme.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/nipspreview/Readme.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nipspreview/Readme.md), SHA-256 `bb9d643884dbeaf218ecea12f4fb8046f9100d10567f0db0dcf2fc99d1f18bb8`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "# NIPS papers pretty html This is a set of scripts for creating nice preview".

Neuraltalk2 documents captioning, pretrained evaluation, data preprocessing, staged CNN finetuning and visualization, with explicit beam-search speed/quality tradeoffs and a known corrupt input-image failure. Its 2016 update recommends Google im2txt and preserves this as educational Torch code; projected leaderboard placement and speed are dated reports. Ng-video-lecture keeps lecture-identical code while acknowledging missing initialization treatment and slower convergence, and warns a differently named successor implementation cannot simply be pasted in. Nipspreview breaks PDF and metadata acquisition into thumbnail, word-cloud, topic-model and abstract stages and admits malformed-paper extraction needs human intervention; its LDA implementation is credited externally. Zero-to-Hero sequences scalar autograd, bigrams, MLP, activation/gradient diagnostics, manual backpropagation, hierarchical CNNs, GPT and tokenization; the backprop lesson asks learners to work the exercise and unpause only when stuck, rather than merely watch. Notpygamejs abstracts game/event boilerplate while admitting globals; paper-notes README is an informal placeholder.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text

# NIPS papers pretty html

This is a set of scripts for creating nice preview page (see here: http://cs.stanford.edu/~karpathy/nipspreview/ ) for all papers published at NIPS. I hope these scripts can be useful to others to create similar pages for other conferences. They show how one can manipulate PDFs, extract image thumbnails, analyze word frequencies, do AJAX requests to load abstracts, etc.

#### Installation

0. Clone this repository `git clone https://github.com/karpathy/nipspreview.git`

1. Download nips25offline from `http://books.nips.cc/nips25.html` and move it into the folder created in step 0

2. Make sure you have ImageMagick: `sudo apt-get install imagemagick`

3. Run `pdftowordcloud.py` (to generate top words for each paper. Output saved in topwords.p as pickle)

4. Run `pdftothumbs.py` (to generate tiny thumbnails for all papers. Outputs saved in thumbs/ folder)

5. Run `scrape.py` (to generate paperid, title, authors list by scraping NIPS .html page)

6. Run `makecorpus.py` (to create allpapers.txt file that has all papers one per row)

7. Run `python lda.py -f allpapers.txt -k 7 --alpha=0.5 --beta=0.5 -i 100` . This will generate a pickle file called `ldaphi.p` that contains the LDA word distribution matrix. Thanks to this [nice LDA code](https://github.com/shuyo/iir/blob/master/lda/lda.py) by shuyo! It requires nltk library and numpy. In this example we are using 7 categories. You would need to change the `nipsnice_template.html` file a bit if you wanted to try different number of categories.

8. Generate the abstract files inside abstracts/ folder using `getabstracts.py`. Some user interaction may be necessary because of poorly formatted papers that make abstract extraction a pain. See script.

9. Finally, run `generatenicelda.py` (to create the nipsnice.html page)

#### Licence

WTFPL licence

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
