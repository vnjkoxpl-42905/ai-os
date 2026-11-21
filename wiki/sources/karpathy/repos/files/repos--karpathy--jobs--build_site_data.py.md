---
type: source
subject: "GitHub source repos/karpathy/jobs/build_site_data.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/jobs/build_site_data.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/jobs/build_site_data.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/jobs/build_site_data.py), SHA-256 `7fcbe80a74ab531b053d82febaf8eabe7bbe9e5cc86c2ddf0ff20d1d6041dae5`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
""" Build a compact JSON for the website by merging CSV stats with AI exposure
```

Jobs pipeline parses cached BLS Quick Facts and projections tables, reports missing HTML and explicitly imputes annual/hourly pay using 2080 hours per year. Site builder merges occupation CSV facts with separate model exposure scores by slug and retains missing values as null. Prompt builder compiles structured data and aggregate slices into a single reusable Markdown analysis input, preserving rationales and labeling Gemini Flash scores as model judgments. Scoring heuristic distinguishes digital home-office tasks from physical/human-presence barriers; anchors are calibration choices, not measured future job losses. Computed wages use jobs times median pay, an approximation rather than authoritative total wage statistics; exposure-weighted denominators exclude missing scores and fixed 342 headers can drift from actual count. This is evidence for explicit provenance and reusable compact analysis artifacts, not proof of socioeconomic forecasts. Full authored scripts read, generated datasets handled separately by payload worker.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""
Build a compact JSON for the website by merging CSV stats with AI exposure scores.

Reads occupations.csv (for stats) and scores.json (for AI exposure).
Writes site/data.json.

Usage:
    uv run python build_site_data.py
"""

import csv
import json


def main():
    # Load AI exposure scores
    with open("scores.json") as f:
        scores_list = json.load(f)
    scores = {s["slug"]: s for s in scores_list}

    # Load CSV stats
    with open("occupations.csv") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Merge
    data = []
    for row in rows:
        slug = row["slug"]
        score = scores.get(slug, {})
        data.append({
            "title": row["title"],
            "slug": slug,
            "category": row["category"],
            "pay": int(row["median_pay_annual"]) if row["median_pay_annual"] else None,
            "jobs": int(row["num_jobs_2024"]) if row["num_jobs_2024"] else None,
            "outlook": int(row["outlook_pct"]) if row["outlook_pct"] else None,
            "outlook_desc": row["outlook_desc"],
            "education": row["entry_education"],
            "exposure": score.get("exposure"),
            "exposure_rationale": score.get("rationale"),
            "url": row.get("url", ""),
        })

    import os
    os.makedirs("site", exist_ok=True)
    with open("site/data.json", "w") as f:
        json.dump(data, f)

    print(f"Wrote {len(data)} occupations to site/data.json")
    total_jobs = sum(d["jobs"] for d in data if d["jobs"])
    print(f"Total jobs represented: {total_jobs:,}")


if __name__ == "__main__":
    main()

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
