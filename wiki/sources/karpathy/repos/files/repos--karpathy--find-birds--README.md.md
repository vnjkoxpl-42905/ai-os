---
type: source
subject: "GitHub source repos/karpathy/find-birds/README.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/find-birds/README.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/find-birds/README.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/find-birds/README.md), SHA-256 `fcd01cdf6db5ca9f57807588d0ad63496c72531fb7a876a58487c5532878b2d7`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "# find-birds !\[user interface\](https://raw.github.com/karpathy/find-birds/master/ui.png) The goal is to find people on Twitter (\"birds\", haha) who".

Cryptos presents a zero-dependency educational Bitcoin implementation and compares SHA-256 with a reference tool; it explicitly restricts use to education and distinguishes partial transaction/header verification from a complete full node. Demonstration keys are source examples, not private workspace credentials. Deep-vector-quantization separates attempted VQVAE reproduction, data-driven initialization needed to avoid index collapse, finicky Gumbel tuning and unfinished DALL-E work; reconstruction loss alone is qualified evidence. EigenLibSVM documents a dense linear-kernel wrapper with a tiny installation demo. Find-birds separates resumable rate-limited social-graph acquisition from reports that can use partial results, while historical Twitter credentials/API instructions are not current recommendations. ForestJS makes weak learners pluggable and advises cross-validation of depth/tries; its universal tree-count and dimensionality statements remain historical source opinions. Gitstats is a small generated-repository-activity visualization. HN Time Capsule stages historical retrieval, prompts, paid analysis, parsing and HTML rendering; it is explicitly 99-percent vibe-coded and unsupported, so hindsight grades are model judgments rather than verified prediction accuracy.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
# find-birds

![user interface](https://raw.github.com/karpathy/find-birds/master/ui.png)

The goal is to find people on Twitter ("birds", haha) who you should follow.

The source of signal is that the people you follow follow other people you probably should follow but so far do not.

## installation

The code base uses tweepy library to interact with the Twitter API:

`pip install -r requirements.txt`

You will have to set up oauth access to Twitter API. Follow [this great tutorial](https://www.digitalocean.com/community/tutorials/how-to-authenticate-a-python-application-with-twitter-using-tweepy-on-ubuntu-14-04) to set that up. You'll then want to enter your consumer key, consumer secret, access token, access token secret as 4 lines in a file `twitter.txt` in the root directory of this project.


## usage

The typical usage for me (username "karpathy") looks as follows:

1. Run `fetch.py karpathy --depth 1`, which fetches information about who I follow, and who everyone I follow follows. Everything is saved to a super lightweight "database" as pickle files. This part can take many days because the Twitter API access is heavily rate limited. For example, I follow about 400 people and it took about 2 weeks to download all of the information. Therefore, I'd run this script in a screen session and come back later.
2. Run `report.py --from-user karpathy`, which finds the most commonly occurring people and then renders the results into an `html` page (by default `report.html`), for pretty consumption. You'll be able to use this script before the `fetch.py` script above fully finishes to see preliminary results if you like.

These two scripts have some more bells and whistles - don't be afraid to read & modify the code, it's relatively short.

## ugh, so much work

If we are very good friends I'd be happy to run all of this code for you on a first-come-first-serve basis, get in touch.


# license
MIT

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
