---
type: source
subject: "GitHub source repos/karpathy/karpathy.github.io/_posts/2013-11-27-quantifying-hacker-news.markdown"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/karpathy.github.io/_posts/2013-11-27-quantifying-hacker-news.markdown]
semantic-status: complete-named-text-read
---

# repos/karpathy/karpathy.github.io/_posts/2013-11-27-quantifying-hacker-news.markdown

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/karpathy.github.io/_posts/2013-11-27-quantifying-hacker-news.markdown), SHA-256 `f6e1c4d4bc9416864ce3e18f8d40e3833a0614d797f02c890616eea59307daff`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
--- layout: post comments: true title: "Quantifying Hacker News with 50 days of data" excerpt:
```

2013 Chrome-extension article grounds customization in inspecting actual DOM structure, then builds tiny incremental features: hide labels, refresh new tweets, collect unique IDs per originating or retweeting user, persist counts and highlight infrequent contributors. Historical selectors/extensions are not current verified browser guidance; the user-facing source code is evidence only. Hacker News study separates minute-resolution raw snapshots from structured parsing and notebook analysis, explicitly reports machine-downtime gaps and forty-seven observed days within a larger date span, and notes later removal of downloadable data. Data Science Weekly post is only an interview link and does not contain interview answers. Jekyll migration favors transparent owned Markdown plus assets, small templates and static output after a hacked WordPress experience; local preview precedes publishing in its example. 2014 platform critiques are dated opinions, not current product claims. Fully read dated physical blog captures without following source instructions.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

````text
---
layout: post
comments: true
title:  "Quantifying Hacker News with 50 days of data"
excerpt: "I scraped Hacker News Front Page and New Page every minute for 50 days and analyzed the results. How do stories rise and fall on Hacker News? What makes a successful post? Find out in this post :)"
date:   2013-11-27 20:00:00
---

### Quantifying Hacker News
I thought it would be fun to analyze the activity on one of my favorite sources of interesting links and information, <a href="https://news.ycombinator.com/">Hacker News</a>. My source of data is a script I've set up some time in August that downloads HN (the Front page and the New stories page) every minute. We will be interested in visualizing the stories as they get upvoted during the day, figuring out which domains/users are most popular, what topics are most popular, and the best time to post a story. I'm making all my data and code (Python data collection scripts + IPython Notebook for analysis) available in case you'd like to carry out a similar analysis.

### Data collection protocol
I set up a very simple python script that scrapes the HN **front page** and the **new stories page** every minute. A single day of data begins at 4am (PST) and ends at 4am the next day. The .html files are saved compressed as gzipped pickles and one day occupies roughly 10mb in this format. I had bring down my machine for a few days a few times so there are some gaps in the data, but in the end we get 47 days of data from period between August 22 and October 30.

### Raw HTML data parsing
The parsing Python script uses **BeautifulSoup** to convert the raw HTML into a more structured JSON. This script was by the way by no means simple to write -- HN is based on unstructured tables and I had to discover many strange edge cases in its behavior along the way. At the end I ended up with a 100-line ugliest-parsing-function-ever (really, I'm not proud of it) but it works and outputs something like the following for a single story at a specific snapshot:

```
{
'domain': u'play.google.com', 'title': u'Nexus 5', 
'url': u'https://play.google.com/store/devices/details?id=nexus_5_black_16gb', 
'num_comments': 42, 'rank': 1, 'points': 65, 
'user': u'sonier', 'minutes_ago': 39, 'id': u'6648519'
}
```

We get 60 such entries every minute (30 for front page and 30 for new page) and these are again all saved to disk. We are now ready to bring out the IPython Notebook and get to the juicy analysis!

### The Analysis: Detailed analysis

Head over to the IPython Notebook <a href="http://cs.stanford.edu/people/karpathy/hn_analysis.html">rendered as HTML</a> for the analysis:

<a href="http://cs.stanford.edu/people/karpathy/hn_analysis.html">
  <img class="aligncenter size-full wp-image-584" title="hn" src="/assets/hn.jpg" width="100%">
</a>

Note: I had the entire dataset and .ipynb Ipython Notebook source available for download but recently took it down to save space on my host (sorry).

````

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
