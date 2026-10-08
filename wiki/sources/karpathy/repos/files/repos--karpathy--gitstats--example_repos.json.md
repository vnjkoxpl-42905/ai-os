---
type: source
subject: "GitHub source repos/karpathy/gitstats/example_repos.json"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/gitstats/example_repos.json]
semantic-status: complete-named-text-read
---

# repos/karpathy/gitstats/example_repos.json

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/gitstats/example_repos.json), SHA-256 `5cc95b58351fa8efd8062e0acbbef0d91bb2e1d6cda876d024db1444fce51afa`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "{ \"infos\" : \\[ { \"name\": \"arbitrary_name\", \"local_path\": \"/Users/example_user/cool_code\", \"cid_link\": \"https://stash.somedomain.com/projects/cool_project/repos/repo/commits/\", \"jira_link\": \"https://issues.somedomain.com/browse/\", \"dtmax\": 7".

Forest MIT license records 2012 authorship and reuse terms, without new reasoning. Gitstats separates local GitPython extraction from a static JSON-fed viewer. It sorts recently active refs, deduplicates commits by SHA across branches, excludes automatic merges, retains author/commit dates and file statistics and explicitly leaves unreliable automatic pulling disabled. Example config is a fictional path/link fixture, not actual personal infrastructure. Viewer provides author/email filtering, contributor-by-day cells, colored file types and capped detailed commit rendering. Contributions exclude tiny changes; timezone offset is explicitly uncertain and equal timestamps can break day normalization. HTML insertion of commit metadata is a historical rendering risk, not a recommended safe implementation. Full source read, no repo fetch or browser execution.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
{
    "infos" : [
        {
            "name": "arbitrary_name",
            "local_path": "/Users/example_user/cool_code",
            "cid_link": "https://stash.somedomain.com/projects/cool_project/repos/repo/commits/",
            "jira_link": "https://issues.somedomain.com/browse/",
            "dtmax": 7
        }
    ]
}
```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
