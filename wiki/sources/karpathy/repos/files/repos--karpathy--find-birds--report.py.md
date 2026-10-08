---
type: source
subject: "GitHub source repos/karpathy/find-birds/report.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/find-birds/report.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/find-birds/report.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/find-birds/report.py), SHA-256 `707d0713b1514a05d0e86dc1043112dc04d22e6b8d49a28354d5753d98a9a296`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "import os import time import math import codecs import argparse from common import LOLDB #".

EigenLibSVM Karpathy-authored 2012 wrappers translate dense Eigen rows into LibSVM nodes, validate data/label dimensions and parameters, expose linear weights, C and model persistence, and explicitly warn about imbalance and missing cross-validation. Test prints expected MATLAB margins and approximately 0.945 training accuracy before and after save/load, rather than claiming held-out evaluation. Prediction allocates D nodes without the required terminating sentinel; source is historical and not correctness-certified. Matrix serialization helper credits Alex Teichman and notes newline-dependent ASCII parsing, so it is third-party evidence. Find-birds separates bounded depth-one acquisition with disk pickle caching and manual Tweepy error waits from offline recommendation: mutual-follow counts discounted by logarithmic popularity, expensive formatting only after top-list selection, then a plain HTML report. Incomplete cached users are explicitly skipped; remote descriptions inserted without escaping are a rendering limitation. These scripts were read without executing credentials, network collection or pickle payloads.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
import os
import time
import math
import codecs
import argparse

from common import LOLDB

# -----------------------------------------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument('--from-user', type=str, default="", help='Report based on a user and their friends.')
parser.add_argument('--from-list', type=str, default="", help='Report based on an explicit list of (comma-separated) subset of users.')
parser.add_argument('-n', '--max', type=int, default=100, help='How many birds max to report on')
parser.add_argument('-i', '--db-dir', type=str, default="db", help='Folder where we store all of the information')
parser.add_argument('-o', '--out-page', type=str, default="report.html", help='Name of the html page that contains the report')
args = parser.parse_args()
# -----------------------------------------------------------------------------

db = LOLDB(args.db_dir)

# -----------------------------------------------------------------------------

# form a (seed, birds) list that we will want to analyze
if args.from_user:
    seed = args.from_user
    blob = db[args.from_user]
    seed_birds = [f.screen_name for f in blob['friends']]
elif args.from_list:
    seed = ""
    seed_birds = args.from_list.split(",")
else:
    raise ValueError("have to specify one of --from-user or --from-list")
# -----------------------------------------------------------------------------

# assemble data about each bird
counts = {}
round1_data = {}
lst = seed_birds
for i,user in enumerate(lst):
    print("%d/%d processing user %s" % (i+1, len(lst), user))
    if not user in db:
        print("skipping user %s and their friends, not in database?" % (user, ))
        continue # could be that the database is not yet fully downloaded
    blob = db[user]
    # iterate all friends of the bird and keep counts
    for f in blob['friends']:
        fuser = f.screen_name
        if fuser == seed or fuser in seed_birds:
            continue # skip, the seed user is already familiar with this bird
        # record round1 information
        counts[fuser] = counts.get(fuser, 0) + 1
        round1_data[fuser] = { # save some metadata about this user in case they make it to the top
            'description' : f.description,
            'following': f.friends_count,
            'followers': f.followers_count,
            'tweets': f.statuses_count,
            'profile_url': f.profile_image_url, # 48x48 thumbnail
        }
    
vk = [(v / (math.log(round1_data[k]['followers'] + 100, 2) + 1.0),k) for k,v in counts.items()]
vk.sort(reverse=True)
birds = [x[1] for x in vk]

if len(birds) > args.max: # crop to only the most commonly ocurring birds
    print("cropping birds from %d to %d" % (len(birds), args.max))
    birds = birds[:args.max]
# -----------------------------------------------------------------------------
# assemble data about each bird
# we do processing in 2 rounds because some processing may be pretty expensive
# so we want to avoid doing it until we know the user will be in the top list

def nice(n):
    # nicely format an integer
    if not isinstance(n, int): return n # noop
    millnames = ['','K','M','B','T']
    colors = ['green', 'orange', 'red', 'red', 'red']
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))
    raw = '%.0f%s' % (n/10**(3 * millidx), millnames[millidx])
    ren = '<span style="color:%s">%s</span>' % (colors[millidx], raw)
    return ren

round2_data = {}
for user in birds:
    d = {}
    d['user'] = '<a href="https://twitter.com/%s">%s</a>' % (user, user)
    d['count'] = counts[user]
    dd = round1_data[user]
    for k in ['following', 'followers', 'tweets']:
        d[k] = nice(dd[k]) # copy over data for this user from round1
    d['description'] = dd['description']
    d['image'] = '<img src="%s">' % (dd['profile_url'],)
    round2_data[user] = d

# -----------------------------------------------------------------------------
# create the output HTML page
headers = ["image", "user", "count", "following", "followers", "tweets", "description"]

# assemble the table in html
rows = []
rows.append("\n".join("<th>%s</th>" % (h,) for h in headers))
for user in birds:
    d = round2_data[user]
    rows.append("\n".join("<td>%s</td>" % (d[h],) for h in headers))
table = "<table>" + "\n".join("<tr>%s</tr>" % (r,) for r in rows) + "</table>"

# render the template
template = open('report_template.html', 'r').read()
out = template.replace("MEAT_GOES_HERE", table)
with codecs.open(args.out_page, "w", "utf-8") as f:
    f.write(out)

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
