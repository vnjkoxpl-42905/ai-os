---
type: source
subject: "GitHub source repos/karpathy/jobs/scrape.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/jobs/scrape.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/jobs/scrape.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/jobs/scrape.py), SHA-256 `8ed95717e7cd79358146b9f20863adcb0b5ac727a54943ecc02a52ccd881ebd2`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
""" Scrape BLS Occupational Outlook Handbook detail pages (raw HTML). Saves raw HTML to html/<slug>.html
```

Jobs scraping treats cached raw HTML as source of truth and derived Markdown as a separate processing stage, with bounded start/end ranges, cache skips, polite delay and visible HTTP/error reporting. Occupation index parser resolves see-aliases to canonical URLs and deduplicates; its initial output lacks later-required slug/category fields, an explicit pipeline-generation boundary. Detail parser preserves canonical URL, quick facts, chart data and selected descriptive/projection tabs but intentionally excludes summary, regional links, similar occupations and contacts, so derived Markdown is not a lossless full-page transcript. Process reports cached/missing inputs. Scorer uses a stated calibration rubric and low-temperature model JSON, saves after each occupation for resumability, reports errors and exposes missing Markdown. It does not validate exposure range/type or cache model identity, and force can rebuild only selected subset. No paid model call, browser scrape or secret loading performed; authored scripts read fully.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""
Scrape BLS Occupational Outlook Handbook detail pages (raw HTML).

Saves raw HTML to html/<slug>.html as the source of truth.
Run process.py afterwards to derive data/<slug>.json and pages/<slug>.md.

Usage:
    uv run python scrape.py                      # scrape all (0 to 342)
    uv run python scrape.py --start 0 --end 5    # scrape first 5
    uv run python scrape.py --start 10 --end 20  # scrape indices 10-19
    uv run python scrape.py --force               # re-scrape ignoring cache

Caching: skips any occupation where html/<slug>.html already exists.
"""

import argparse
import json
import os
import time
from playwright.sync_api import sync_playwright

# ---------------------------------------------------------------------------
# Main scraper
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Scrape BLS OOH pages")
    parser.add_argument("--start", type=int, default=0, help="Start index (inclusive)")
    parser.add_argument("--end", type=int, default=None, help="End index (exclusive)")
    parser.add_argument("--force", action="store_true", help="Re-scrape even if cached")
    parser.add_argument("--delay", type=float, default=1.0, help="Seconds between requests")
    args = parser.parse_args()

    # Load master list
    with open("occupations.json") as f:
        occupations = json.load(f)

    end = args.end if args.end is not None else len(occupations)
    subset = occupations[args.start:end]

    # Create output dirs
    os.makedirs("html", exist_ok=True)
    os.makedirs("data", exist_ok=True)
    os.makedirs("pages", exist_ok=True)

    # Figure out what needs scraping (cache based on html/ existence)
    to_scrape = []
    for i, occ in enumerate(subset, start=args.start):
        html_path = f"html/{occ['slug']}.html"
        if not args.force and os.path.exists(html_path):
            print(f"  [{i}] CACHED {occ['title']}")
            continue
        to_scrape.append((i, occ))

    if not to_scrape:
        print("Nothing to scrape — all cached.")
        return

    print(f"\nScraping {len(to_scrape)} occupations (non-headless Chromium)...\n")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        for idx, (i, occ) in enumerate(to_scrape):
            slug = occ["slug"]
            url = occ["url"]
            html_path = f"html/{slug}.html"

            print(f"  [{i}] {occ['title']}...", end=" ", flush=True)

            try:
                resp = page.goto(url, wait_until="domcontentloaded", timeout=15000)
                if resp.status != 200:
                    print(f"HTTP {resp.status} — SKIPPED")
                    continue

                # Save raw HTML — this is the source of truth
                html = page.content()
                with open(html_path, "w") as f:
                    f.write(html)

                print(f"OK ({len(html):,} bytes)")

            except Exception as e:
                print(f"ERROR: {e}")

            # Be polite
            if idx < len(to_scrape) - 1:
                time.sleep(args.delay)

        browser.close()

    # Summary
    cached = len([f for f in os.listdir("html") if f.endswith(".html")])
    print(f"\nDone. {cached}/{len(occupations)} HTML files cached in html/")


if __name__ == "__main__":
    main()

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
