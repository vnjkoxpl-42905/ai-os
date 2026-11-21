---
type: source
subject: "GitHub source repos/karpathy/jobs/process.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/jobs/process.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/jobs/process.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/jobs/process.py), SHA-256 `e38a210fc4305288a1c9c755f3e74b421fdc7bfc14ebdb160781ac465e64010e`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
""" Process scraped HTML files into Markdown. Reads from html/<slug>.html, writes to pages/<slug>.md. Reuses parse_detail.parse_ooh_page()
```

Jobs scraping treats cached raw HTML as source of truth and derived Markdown as a separate processing stage, with bounded start/end ranges, cache skips, polite delay and visible HTTP/error reporting. Occupation index parser resolves see-aliases to canonical URLs and deduplicates; its initial output lacks later-required slug/category fields, an explicit pipeline-generation boundary. Detail parser preserves canonical URL, quick facts, chart data and selected descriptive/projection tabs but intentionally excludes summary, regional links, similar occupations and contacts, so derived Markdown is not a lossless full-page transcript. Process reports cached/missing inputs. Scorer uses a stated calibration rubric and low-temperature model JSON, saves after each occupation for resumability, reports errors and exposes missing Markdown. It does not validate exposure range/type or cache model identity, and force can rebuild only selected subset. No paid model call, browser scrape or secret loading performed; authored scripts read fully.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""
Process scraped HTML files into Markdown.

Reads from html/<slug>.html, writes to pages/<slug>.md.
Reuses parse_detail.parse_ooh_page() which is already tested.

Usage:
    uv run python process.py              # process all HTML files
    uv run python process.py --force      # re-process even if .md exists
"""

import argparse
import json
import os
from parse_detail import parse_ooh_page


def main():
    parser = argparse.ArgumentParser(description="Convert HTML to Markdown")
    parser.add_argument("--force", action="store_true", help="Re-process even if .md exists")
    args = parser.parse_args()

    os.makedirs("pages", exist_ok=True)

    # Load master list for ordering/metadata
    with open("occupations.json") as f:
        occupations = json.load(f)

    processed = 0
    skipped = 0
    missing = 0

    for occ in occupations:
        slug = occ["slug"]
        html_path = f"html/{slug}.html"
        md_path = f"pages/{slug}.md"

        if not os.path.exists(html_path):
            missing += 1
            continue

        if not args.force and os.path.exists(md_path):
            skipped += 1
            continue

        md = parse_ooh_page(html_path)
        with open(md_path, "w") as f:
            f.write(md)
        processed += 1

    total_html = len([f for f in os.listdir("html") if f.endswith(".html")])
    total_md = len([f for f in os.listdir("pages") if f.endswith(".md")])
    print(f"Processed: {processed}, Skipped (cached): {skipped}, Missing HTML: {missing}")
    print(f"Total: {total_html} HTML files, {total_md} Markdown files")


if __name__ == "__main__":
    main()

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
