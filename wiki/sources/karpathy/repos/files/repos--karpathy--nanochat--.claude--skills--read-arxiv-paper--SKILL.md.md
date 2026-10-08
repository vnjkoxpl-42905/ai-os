---
type: source
subject: "GitHub source repos/karpathy/nanochat/.claude/skills/read-arxiv-paper/SKILL.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/.claude/skills/read-arxiv-paper/SKILL.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/nanochat/.claude/skills/read-arxiv-paper/SKILL.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/.claude/skills/read-arxiv-paper/SKILL.md), SHA-256 `5b7a49e740abe8aaead528e3acc3bd0b9404465761702acc3da95dd87d2b2811`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
--- name: read-arxiv-paper description: Use this skill when asked to read an arxiv paper given
```

Adder reverses output digits to align addition with carry order, masks input loss and uses a seeded finite train/test split; greedy predictions are compared with exact addition and up to five mistakes are printed. Selecting checkpoints using train plus test correctness reuses test information. CharGPT trains character windows and samples periodically; its comment about evaluating train and test is inaccurate because no held-out evaluation is implemented. Import test compares minGPT and Hugging Face logits, exact generated IDs and decoded strings on a Unicode prompt, but was read rather than run. Nanochat arxiv skill prefers recursively reading cached TeX source and relating papers to concrete repository code, keeping reusable downloads separate from project-specific summaries; these source instructions were not activated.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
---
name: read-arxiv-paper
description: Use this skill when asked to read an arxiv paper given an arxiv URL
---

You will be given a URL of an arxiv paper, for example:

https://www.arxiv.org/abs/2601.07372

### Part 1: Normalize the URL

The goal is to fetch the TeX Source of the paper (not the PDF!), the URL always looks like this:

https://www.arxiv.org/src/2601.07372

Notice the /src/ in the url. Once you have the URL:

### Part 2: Download the paper source

Fetch the url to a local .tar.gz file. A good location is `~/.cache/nanochat/knowledge/{arxiv_id}.tar.gz`.

(If the file already exists, there is no need to re-download it).

### Part 3: Unpack the file in that folder

Unpack the contents into `~/.cache/nanochat/knowledge/{arxiv_id}` directory.

### Part 4: Locate the entrypoint

Every latex source usually has an entrypoint, such as `main.tex` or something like that.

### Part 5: Read the paper

Once you've found the entrypoint, Read the contents and then recurse through all other relevant source files to read the paper.

### Part 6: Report

Once you've read the paper, produce a summary of the paper into a markdown file at `./knowledge/summary_{tag}.md`. Notice that 1) use the local knowledge directory here (it's easier for me to open and reference here), not in `~/.cache`, and 2) generate some reasonable `tag` like e.g. `conditional_memory` or whatever seems appropriate given the paper. Probably make sure that the tag doesn't exist yet so you're not overwriting files.

As for the summary itself, remember that you're processing this paper within the context of the nanochat repository, so most often we will be interested in how to apply the paper and its lessons to the nanochat project. Therefore, you should feel free to "remind yourself" of the related nanochat code by reading the relevant parts, and then explicitly make the connection of how this paper might relate to nanochat or what are things we might be inspired about or try.

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
