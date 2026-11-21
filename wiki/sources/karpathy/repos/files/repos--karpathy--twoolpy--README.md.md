---
type: source
subject: "GitHub source repos/karpathy/twoolpy/README.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/twoolpy/README.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/twoolpy/README.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/twoolpy/README.md), SHA-256 `82cda2b319aa9de464f2a470a6cc51b438181eb2088bc35622c00cd1e2ad44ab`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
# Twoolpy Twitter API fun scripts using Tweepy in Python. I'm hoping people can use
```

ScholarOctopus describes a curated paper-pointer visualization using TF-IDF and t-SNE while its collection scripts are explicitly private and absent. SVMJS starts with a linear baseline before nonlinear kernels, exposes speed/accuracy tolerances and references Matlab correctness tests; universal memory-efficiency language remains qualified historical documentation. TF-agent README merely labels Gym RL code. TSNEJS attributes the original algorithm to van der Maaten and Hinton and supplies raw-distance and CSV interfaces; illustrative clusters are not proof of causal structure. Twoolpy contains historical authenticated stream, social-graph recommendation and follower-diff examples with a preflight auth test; obsolete plain-text credential conventions are not adopted. Ulogme separates local timestamped acquisition, processing and browser visualization, keeps data local, documents malformed-log and permission/port troubleshooting, and explicitly supports historical Ubuntu/macOS rather than Windows; current browser incompatibility claims are stale.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text

# Twoolpy

Twitter API fun scripts using Tweepy in Python. I'm hoping people can use these 
examples as repository to draw on when they develop their own scripts.

#### Scripts

1. `$ python recommend.py blahblah`: gives recommendations to user 'blahblah' on who to follow, based on their social graph on twitter. It looks for people who are very often followed by blahblah's followers, but who 'blahblah' doesn't follow. 

2. `$ python userstream.py`: prints authenticated user's timeline, live

3. `$ python followersdiff.py`: finds all your followers and saves them to local file. Re-running the script
will do a diff with that file so you can see who followed or unfollowed you 
since last time you ran the script.

#### Installation

1. Install tweepy:
`$ easy_install tweepy`
(requires: `$ sudo apt-get install python-setuptools`)

2. Follow [this excellent tutorial](http://talkfast.org/2010/05/31/twitter-from-the-command-line-in-python-using-oauth) to set up oauth access.

3. Once you register an app on Twitter they will give you 4 strings: consumer key, consumer secret, access key, and access secret. Create a new file called `tconf` in the folder where you keep twoolpy and enter the 4 strings one per line, in order listed above (consumer key, consumer secret, access key, and access secret).

4. run `$ python authest.py` to make sure everything is setup right. If yes, some people's names will be printed, or error will result.

#### Licence

WTFPL licence


```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
