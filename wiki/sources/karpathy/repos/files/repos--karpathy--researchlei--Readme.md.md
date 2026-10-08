---
type: source
subject: "GitHub source repos/karpathy/researchlei/Readme.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/researchlei/Readme.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/researchlei/Readme.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/researchlei/Readme.md), SHA-256 `d8fcc3e060a5d8d8013237655dfafa0f9f31057f07cca67e8f0fe8bf9b95ffc2`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
# Research Lei This page contains code for Research Lei: http://cs.stanford.edu/people/karpathy/researchlei/ Google Group: https://groups.google.com/forum/?fromgroups#!forum/research-lei Feel
```

PyTorch MADE reimplements a paper with masked autoregressive dependencies, contrasts cheap likelihood with sequential sampling and admits failure to reproduce claimed single-pass multi-mask gains; averaged multiple passes improve reported loss at added cost. Normalizing-flows README lists GPU/high-dimensional/image support and stable-update work as TODO, not implemented capability. Matlab Random Forest explicitly restricts itself to learning and recommends mature alternatives for serious use. Randomfun Rust notes are learning notes and broad claims about language safety need qualifications before practical reuse. Reader3 is a chapter-oriented EPUB-to-local-library/LLM co-reading illustration, explicitly mostly vibe-coded and unsupported. RecurrentJS exposes values/derivatives, expression graphs and optimizers but warns beta users must understand backprop; its example variable inconsistencies are not certified executable code. ReinforceJS marks continuous policy/actor-critic work very alpha and reuses RecurrentJS, so these are not independent implementation evidence. Researchlei separates citation acquisition and visual library while admitting sparse indexes and aggressive external throttling. RustBPE aims at a small fast training component interoperating with tiktoken inference; it explicitly discloses LLM-assisted Rust and compares equality against an author-understood Python reference rather than treating passing tests as proof of idiomatic Rust design.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text

# Research Lei

This page contains code for Research Lei: 
http://cs.stanford.edu/people/karpathy/researchlei/

Google Group: https://groups.google.com/forum/?fromgroups#!forum/research-lei

Feel free to contact me for questions, suggestions on Twitter: https://twitter.com/karpathy or via email: karpathy@cs.stanford.edu


#### Installation

0. Clone this repository `git clone https://github.com/karpathy/researchlei.git`

1. (Optional) Make sure you have [ImageMagick](http://www.imagemagick.org/script/binary-releases.php) installed on your system if you'd like to extract image thumbnails from downloaded papers. In Ubuntu, this is available as `sudo apt-get install imagemagick`

2. (Optional) Install pdftotext. This is included by default in many Linux distributions. This tool is used to extract all the words from a paper and find the top 100. Later, this can be used for other fancy processing, such as topic models, tfidf similarity rankings, etc.

3. You will need [Python](http://www.python.org/), preferrably Python 2.7.

4. Obtain Microsoft Academic Search API APP ID key and place it into a file `appid.txt`. Since App ID's are rate limited to 200 queries per minute, I would strongly encourage you to [obtain your own key](http://cs.stanford.edu/people/karpathy/researchlei/myrequest.html) from Microsoft (the request involves a single email and they reply fast). However, if you'd only like to check it out first for a bit, fill out this [form](https://docs.google.com/forms/d/1AZTJrQKOBro_4t6AGCcrAURvNUYPWXhnVzfy_sn3nTw).

#### Usage

0. You start with an empty database in the beginning. To add a paper, run, for example: `python addpaper.py name building rome in a day`. This gets the `addpaper.py` script to search Microsoft Academic Search by name for a paper with a title that contains the query words building, rome, in, a, day. The script will then guide you through downloading its citations, reference, and the actual .pdf of the paper. (Sadly, you may find that Microsoft's Academic Search is sparser than Google Scholar, especially with more recent work :( I contacted them about this and they said they are working on an update to their index. Unfortunately, Google Scholar does not provide convenient API, makes scraping difficult, and does not provide information that is as complete.)

1. The main Python script `addpaper.py` creates a JSON file that the `client/index.html` renders for the UI. Open it to see your library (remember to refresh it too every time you run `addpaper.py`)! Some browsers like Safari and Chrome will not (by default) allow you to do an AJAX call to read the local JSON file. This can be fixed by starting Chrome with a special flag (--allow-file-access-from-files). In Ubuntu, you can drag the Chrome icon to desktop, right click -> properties and append it to Command. Alternatively, just *use Firefox*!

#### Usage Example TLDR

0. add a paper to library: `python addpaper.py name building rome in a day`
1. view library: open `client/index.html`
2. follow instructions in interface to download any specific paper of interest, or goto 0. to add a custom new paper

#### FAQ
Q: Microsoft Academic Search is sparser than Google Scholar, especially on very recent work. Could you use Scholar instead?
A: No. Google Scholar does not provide API that allows you to easily download their structured data. It is possible to scrape the HTML manually, but they aggressively throttle your requests. Even if you could, they don't provide as much data. For example, they don't provide references, abstracts, etc. Or if there are more than a few authors on a paper, they simply write "..." and refer you to a publisher's page for the paper. I wish Google Scholar was as cool as Microsoft Academic Search. However, I've written MAS about this issue and they told me that they are actively working to index more papers and that we should all stay tuned. Lets hope for the best.

#### Licence

BSD licence

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
