---
type: source
subject: "GitHub source repos/karpathy/hn-time-capsule/README.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/hn-time-capsule/README.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/hn-time-capsule/README.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/hn-time-capsule/README.md), SHA-256 `77d9e715cc0fd3d20794cab5a83d81c32ac0f9c00f5bd5de87cd13ae109e5f4b`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "# HN Time Capsule !\[hero\](hnhero.png) A Hacker News time capsule project that pulls the HN".

Cryptos presents a zero-dependency educational Bitcoin implementation and compares SHA-256 with a reference tool; it explicitly restricts use to education and distinguishes partial transaction/header verification from a complete full node. Demonstration keys are source examples, not private workspace credentials. Deep-vector-quantization separates attempted VQVAE reproduction, data-driven initialization needed to avoid index collapse, finicky Gumbel tuning and unfinished DALL-E work; reconstruction loss alone is qualified evidence. EigenLibSVM documents a dense linear-kernel wrapper with a tiny installation demo. Find-birds separates resumable rate-limited social-graph acquisition from reports that can use partial results, while historical Twitter credentials/API instructions are not current recommendations. ForestJS makes weak learners pluggable and advises cross-validation of depth/tries; its universal tree-count and dimensionality statements remain historical source opinions. Gitstats is a small generated-repository-activity visualization. HN Time Capsule stages historical retrieval, prompts, paid analysis, parsing and HTML rendering; it is explicitly 99-percent vibe-coded and unsupported, so hindsight grades are model judgments rather than verified prediction accuracy.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

````text
# HN Time Capsule

![hero](hnhero.png)

A Hacker News time capsule project that pulls the HN frontpage from exactly 10 years ago, analyzes articles and discussions using an LLM to evaluate prescience with the benefit of hindsight, and generates an HTML report. Also see [my short blog post about this repo](https://karpathy.bearblog.dev/auto-grade-hn/) for more context.

## What it does

1. Fetches the HN frontpage from 10 years ago (e.g., `https://news.ycombinator.com/front?day=2015-12-09`)
2. For each article, fetches the original article content and all HN comments
3. Generates prompts asking an LLM to analyze what happened with hindsight
4. Parses LLM responses to extract grades for each commenter
5. Renders an HTML summary with all analyses and grades

The goal is to find which HN commenters were most prescient or most wrong over time, and surface interesting predictions from a decade ago. The more general and interesting idea is that of LLMs automatically scouring human artifacts from the past and synthesizing them into knowledge and insights.

## Vibe code alert

99% of this repo was vibe coded in a few hours with Opus 4.5. Code is provided as is and I don't intend to support it.

## Setup

```bash
# Install dependencies
uv sync

# Set up OpenAI API key into a .env file
echo "OPENAI_API_KEY=your-key-here" > .env
```

## Usage

The main entry point is `pipeline.py` with 5 stages that can be run individually or all at once:

```bash
# Run all stages for today minus 10 years
uv run python pipeline.py all

# Run with a limit (for testing)
uv run python pipeline.py all --limit 5

# Run for a specific date
uv run python pipeline.py all --date 2015-06-15

# Run individual stages
uv run python pipeline.py fetch              # fetch frontpage + articles + comments
uv run python pipeline.py prompt             # generate LLM prompts
uv run python pipeline.py analyze            # run LLM analysis (costs money!)
uv run python pipeline.py parse              # extract grades from responses
uv run python pipeline.py render             # generate HTML summary

# Use a cheaper model for testing
uv run python pipeline.py analyze --model gpt-5-mini
```

## Data Directory Structure

```
data/
  2015-12-09/
    frontpage.json              # list of all articles from that day
    all_grades.json             # aggregated grades across all articles
    summary.html                # rendered HTML report
    10699846/                   # directory per article (by item_id)
      meta.json                 # article metadata
      article.txt               # fetched article content
      article_error.txt         # or error if fetch failed
      comments.json             # HN comment tree
      prompt.md                 # full LLM prompt
      response.md               # LLM analysis output
      grades.json               # parsed grades from response
```

## Files

- `pipeline.py` - Main pipeline with all stages (clean, fetch, prompt, analyze, parse, render)

## Example Output

The LLM analyzes each article and its discussion, then:
1. Summarizes what actually happened to the topic over 10 years
2. Awards "Most prescient" and "Most wrong" to commenters
3. Notes fun/notable aspects of the discussion
4. Grades each commenter (A+ to F) based on how their comments aged

Grades are parsed and aggregated in the Hall of Fame so we can track which HN accounts have the best prediction track records over time.

## License

MIT
````

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
