# Session Handoff: Andrej Karpathy Source Collection (Antigravity -> Codex)

**Date:** 2026-10-08  
**Source Workflow:** Nate Herk "Karpathy Brain" Reproduction (Prompt 1: Source Collection Only)  
**Handing Off From:** Jay 2 / Antigravity  
**Handing Off To:** Codex (ai-os primary runtime)  
**Collection Root:** `C:\Users\Joshu\dev\ai-os\raw\sources\karpathy-brain\raw\`  

---

## 1. Executive Summary

Antigravity has completed the source-collection stage. All public source materials for Andrej Karpathy across Blogs/Writing, GitHub, YouTube, and X (Twitter) have been collected into physical local files under the collection root. 

As strictly instructed:
* Zero summaries, rule derivations, or wiki pages were generated.
* Zero agents, skills, hooks, or AI OS configurations were altered.
* No cookies, auth tokens, passwords, or browser sessions were exported.
* Temporary environments (`karpathy-venv`, `karpathy-gh-clones`) were maintained outside the Obsidian vault in `C:\Users\Joshu\Tools\`.

The collection is ready for Codex to begin the synthesis, wiki compiling, and agent stages.

---

## 2. Quantitative Inventory

| Source Domain | Status | Files / Items | Word Count | Payload Size |
| :--- | :--- | :--- | :--- | :--- |
| **1. Blog & Writings** | Complete | 79 articles (Markdown + HTML) | 202,396 words | 1.33 MB |
| **2. GitHub** | Complete | 1,209 source & doc files (54 repos, 13 gists) | 4,892,153 words | 64.58 MB |
| **3. YouTube** | Complete (Channel) | 15 lecture transcripts | 325,686 words | 1.94 MB |
| **4. X (Twitter)** | Complete | 1,975 items (1,706 posts + 269 replies) | 212,399 words | 1.62 MB |
| **TOTAL** | **100% Collected** | **3,278 items** | **5,632,634 words** | **~69.47 MB** |

---

## 3. Directory Layout and Deliverables

All data resides under `C:\Users\Joshu\dev\ai-os\raw\sources\karpathy-brain\raw\`:

```text
raw\sources\karpathy-brain\raw\
├── COLLECTION-REPORT.md          # Master executive summary across all domains
├── COLLECTION_INSTRUCTIONS.md    # Authoritative extraction standard and agent rules
├── blog\
│   ├── md\                       # 79 clean Markdown articles
│   ├── html\                     # 79 original source HTML files
│   ├── scripts\                  # Reusable Python scripts (collect_blog.py, make_manifest.py)
│   ├── MANIFEST.json             # SHA-256 hashes, word counts, metadata per item
│   ├── MANIFEST.md
│   ├── COVERAGE.md
│   └── FAILURES.md
├── github\
│   ├── repos\karpathy\<name>\    # 54 public non-fork repos (source code, READMEs, docs, notebooks)
│   ├── gists\<id>\               # 13 public gists
│   ├── scripts\                  # collect_github.py
│   ├── MANIFEST.json             # Commit SHAs, licenses, hashes per file
│   ├── MANIFEST.md
│   ├── COVERAGE.md
│   └── FAILURES.md
├── youtube\
│   ├── captions\                 # Raw JSON captions from YouTube
│   ├── transcripts\              # 15 timestamped Markdown lecture transcripts
│   ├── scripts\                  # collect.py, generate_manifests.py
│   ├── enumeration.json          # Complete discovery enumeration
│   ├── MANIFEST.json
│   ├── MANIFEST.md
│   ├── COVERAGE.md
│   └── FAILURES.md
└── x\
    ├── archive\<Year>\<YM>.md    # 1,706 posts organized into 40 monthly Markdown files (2023-01 to 2026-10)
    ├── replies\archive\          # 269 replies organized into monthly Markdown files with in-reply-to context
    ├── posts.jsonl               # Complete append-only JSONL ledger for all main posts
    ├── replies\replies.jsonl     # Complete append-only JSONL ledger for dedicated replies
    ├── scripts\                  # collect_shard.mjs, scroll_profile.mjs, collect_replies_dedicated.mjs, fill_gaps.mjs
    ├── MANIFEST.json
    ├── MANIFEST.md
    ├── COVERAGE.md
    └── FAILURES.md
```

---

## 4. Key Provenance and Verification Details

1. **Blog (`raw/blog/`):**
   * Covers `karpathy.github.io` (23 posts + about), `karpathy.bearblog.dev` (13 posts), `karpathy.medium.com` (8 posts), `cs231n.github.io` (30 course notes), and official homepage/book lists.
   * Both clean readable Markdown and original HTML are preserved side-by-side to protect equations, tables, and asset links.
   * Failures: 3 dead links on Stanford's archive index (`assignment1`, `assignment2`, `assignment3`).

2. **GitHub (`raw/github/`):**
   * 54 non-fork repositories and 13 gists cloned with `--depth 1`.
   * Captures full source code, READMEs, and Jupyter notebooks with relative paths preserved.
   * Captured commit SHA and license are recorded for every repository in `MANIFEST.json`.
   * Exclusions: 9 upstream forks (`cpython`, `transformers`, `nn`, `optim`, etc.), `.git` object databases, dependency folders, and binary files over 5MB (all itemized in `COVERAGE.md`).

3. **YouTube (`raw/youtube/`):**
   * 100% of spoken video lectures on Karpathy's official personal channel (`@AndrejKarpathy`) are captured as timestamped Markdown transcripts (`transcripts/*.md`).
   * 2 channel videos (`vEnetcj_728`, `Jv1ayv-04H4`) are silent AI animation loops with zero spoken audio (explicitly marked as instrumental/excluded).
   * Deferred: Stanford CS231n 2016 video captions (16 videos) and Microsoft Build 2023 were deferred due to YouTube IP 429 rate limit. Note that all 30 written lecture modules and assignment notes for CS231n are already fully captured in `raw/blog/`.

4. **X (Twitter) (`raw/x/`):**
   * Extracted using Joshua's persistent logged-in Agent Browser on port 9223 across parallel tabs.
   * Unbroken chronological coverage spanning 40 consecutive calendar months (January 1, 2023 through October 8, 2026).
   * 1,706 Main Posts + 269 Dedicated Replies = 1,975 total items.
   * 100% verbatim capture: every "Show more" button clicked, emojis and line breaks preserved, images and media links recorded, and quoted/replied-to content attributed.

---

## 5. Reusable Infrastructure Created

1. **Browser Agent Playbook:**
   * Created at `C:\Users\Joshu\dev\ai-os\references\browser-agent-playbook.md` (and mirrored in `C:\Users\Joshu\Tools\browser-agent-playbook.md`).
   * Documents lessons learned, port 9223 pre-flight checklists, virtual DOM scroll fixes, cp1252 encoding rules, and CDP scripting shortcuts.
2. **Dedicated Python Scripts:**
   * [get_youtube_transcript.py](file:///C:/Users/Joshu/dev/ai-os/system/scripts/get_youtube_transcript.py): Free, zero-cost CLI to fetch YouTube timestamped transcripts without API keys.
   * [get_x_post.py](file:///C:/Users/Joshu/dev/ai-os/system/scripts/get_x_post.py): Free CLI to pull any X post into formatted Markdown without paid APIs.

---

## 6. Recommended Next Steps for Codex

1. **Ingestion & Synthesis:**
   * Review `COLLECTION-REPORT.md` and domain manifests under `raw\sources\karpathy-brain\raw\`.
   * Compile the source knowledge into the wiki ledger structure following `system/schema/llm-wiki.md`.
2. **Rule Derivation:**
   * Extract Karpathy's core mental models, engineering practices, and writing voice from the 5.6M words of collected raw evidence.
3. **Agent & Skill Construction:**
   * Build the dedicated Karpathy persona, skills, and evaluation hooks as outlined in subsequent stages of the project.
