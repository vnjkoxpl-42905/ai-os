---
type: source
subject: "GitHub source repos/karpathy/gitstats/run.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/gitstats/run.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/gitstats/run.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/gitstats/run.py), SHA-256 `a63348efd46f02ee068db222867936e6b531c4f825edff67f7edb912ea6897ae`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "import re import sys import time import json from git import Repo # ------------------------------------------------------------------------------ def".

Forest MIT license records 2012 authorship and reuse terms, without new reasoning. Gitstats separates local GitPython extraction from a static JSON-fed viewer. It sorts recently active refs, deduplicates commits by SHA across branches, excludes automatic merges, retains author/commit dates and file statistics and explicitly leaves unreliable automatic pulling disabled. Example config is a fictional path/link fixture, not actual personal infrastructure. Viewer provides author/email filtering, contributor-by-day cells, colored file types and capped detailed commit rendering. Contributions exclude tiny changes; timezone offset is explicitly uncertain and equal timestamps can break day normalization. HTML insertion of commit metadata is a historical rendering risk, not a recommended safe implementation. Full source read, no repo fetch or browser execution.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
import re
import sys
import time
import json
from git import Repo

# ------------------------------------------------------------------------------

def encode_commit(info, c, branch):

    # in-place create ahref tags for JIRA
    txt = c.message
    if info['jira_link']:
        txt = re.sub(r'(SW-\d+)', r'<a href=' + info['jira_link'] + r'\1>\1</a>', txt)

    j = {
        'id': c.hexsha,
        'message': txt,
        'name': c.author.name,
        'email': c.author.email,
        'authored_date': c.authored_date,
        'committed_date': c.committed_date,
        'total': c.stats.total,
        'files': c.stats.files,
        'idlink': info['cid_link'] + c.hexsha,
        'branch': branch,
    }
    return j

def process_repo(info):

    tnow = time.time()

    print("processing repo", info['local_path'])
    repo = Repo(info['local_path'])
    assert not repo.bare, "trouble loading " + info['local_path']

    # update the repo. NOTE: does not seem to work sometimes? doing manually for now. debug later
    # print("pulling the latest...")
    # o = repo.remotes.origin
    # o.pull()

    # fetch active branches and extract the time of latest commit to each branch
    print("fetching active branches...")
    refs = sorted(repo.refs, key=lambda r: r.commit.authored_date, reverse=True)
    refs = [r for r in refs if (tnow - r.commit.authored_date)/60/60/24 < info['dtmax']]
    print("found %d branches with new commits" % (len(refs), ))

    # get all commits on branches
    print("extracting all commits...")
    have = set()
    commits = []
    for r in refs:
        n = 0
        for c in repo.iter_commits(r.name):
            if (tnow - c.authored_date)/60/60/24 > info['dtmax']:
                continue # skip very old commits
            h = c.hexsha
            if not h in have:
                n += 1
                have.add(h)
                encoded = encode_commit(info, c, r.name)
                if not 'Automatic merge from' in encoded['message']:
                    commits.append(encoded)
        if n > 0:
            print(r.name, n)
    commits.sort(key=lambda r: r['authored_date'], reverse=True)

    out = {
        'commits': commits,
        'dtmax': info['dtmax']
    }
    return out

# ------------------------------------------------------------------------------
if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--repos-config', help='configuration json file of repos to use')
    args = parser.parse_args()

    with open(args.repos_config, 'r') as f:
        config = json.load(f)
        infos = config['infos']

    # process each one in turn
    for info in infos:
        jout = process_repo(info)
        # write JSON output
        out_path = 'deploy/%s.json' % (info['name'], )
        with open(out_path, 'w') as f:
            json.dump(jout, f)
        print("wrote", 'deploy/%s.json' % (info['name'], ))

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
