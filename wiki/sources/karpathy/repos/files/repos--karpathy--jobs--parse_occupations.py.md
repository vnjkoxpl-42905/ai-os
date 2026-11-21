---
type: source
subject: "GitHub source repos/karpathy/jobs/parse_occupations.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/jobs/parse_occupations.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/jobs/parse_occupations.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/jobs/parse_occupations.py), SHA-256 `b679ee4ce67257603082fcede55d06e7b7c296bab741b46a8232d41ae82f2193`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
"""Parse BLS Occupational Outlook Handbook A-Z index to extract all occupations.""" from bs4 import BeautifulSoup
```

Jobs scraping treats cached raw HTML as source of truth and derived Markdown as a separate processing stage, with bounded start/end ranges, cache skips, polite delay and visible HTTP/error reporting. Occupation index parser resolves see-aliases to canonical URLs and deduplicates; its initial output lacks later-required slug/category fields, an explicit pipeline-generation boundary. Detail parser preserves canonical URL, quick facts, chart data and selected descriptive/projection tabs but intentionally excludes summary, regional links, similar occupations and contacts, so derived Markdown is not a lossless full-page transcript. Process reports cached/missing inputs. Scorer uses a stated calibration rubric and low-temperature model JSON, saves after each occupation for resumability, reports errors and exposes missing Markdown. It does not validate exposure range/type or cache model identity, and force can rebuild only selected subset. No paid model call, browser scrape or secret loading performed; authored scripts read fully.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""Parse BLS Occupational Outlook Handbook A-Z index to extract all occupations."""

from bs4 import BeautifulSoup
import json

with open("occupational_outlook_handbook.html", "r") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

# The occupation listings are inside <div class="a-z-list">
az_list = soup.find("div", class_="a-z-list")

# Each <li> contains either:
# 1. A direct link: <a href="url">Occupation Name</a>
# 2. An alias: <a href="url">Alias</a>, see: <a href="url">Canonical Name</a>
#
# We want the unique canonical occupations (deduplicated by URL).

occupations = {}  # url -> canonical name
aliases = []  # list of (alias_name, canonical_name, url)

for li in az_list.find_all("li"):
    links = li.find_all("a")
    text = li.get_text()

    if ", see:" in text or ", see " in text:
        # This is an alias entry — the second link is the canonical one
        if len(links) >= 2:
            alias_name = links[0].get_text(strip=True)
            canonical_name = links[1].get_text(strip=True)
            url = links[1]["href"]
            aliases.append((alias_name, canonical_name, url))
            # Still register the canonical occupation
            if url not in occupations:
                occupations[url] = canonical_name
    else:
        # Direct entry
        if links:
            name = links[0].get_text(strip=True)
            url = links[0]["href"]
            if url not in occupations:
                occupations[url] = name

# Sort by name
sorted_occupations = sorted(occupations.items(), key=lambda x: x[1].lower())

print(f"Total unique occupations: {len(sorted_occupations)}")
print(f"Total aliases (redirects): {len(aliases)}")
print()
print("--- First 20 occupations ---")
for url, name in sorted_occupations[:20]:
    print(f"  {name}")
    print(f"    {url}")
print("...")
print()
print("--- Last 10 occupations ---")
for url, name in sorted_occupations[-10:]:
    print(f"  {name}")
    print(f"    {url}")

# Save to JSON for further analysis
output = []
for url, name in sorted_occupations:
    output.append({"title": name, "url": url})

with open("occupations.json", "w") as f:
    json.dump(output, f, indent=2)

print(f"\nSaved {len(output)} occupations to occupations.json")

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
