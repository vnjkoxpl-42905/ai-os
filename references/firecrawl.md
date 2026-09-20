---
type: reference
subject: Firecrawl integration, agent orchestration, and web intelligence
updated: 2026-09-19
aliases: [firecrawl, firecrawl-agent, web-intelligence]
---

# Firecrawl — Agent Orchestration and Web Intelligence Guide

Authority for all Firecrawl operations across Jay 2 (Claude Code, Codex, and Gemini / Antigravity).

Firecrawl provides clean, LLM-ready web extraction, web search, and autonomous web research agents. The system key lives strictly in the root `.env` as `FIRECRAWL_API_KEY`.

---

## 1. Quick Route & Endpoints

| Need | Method / Endpoint | Latency | Cost / Impact | Best Use |
|---|---|---|---|---|
| **Direct Search** | `POST https://api.firecrawl.dev/v1/search` | 1 to 3 sec | Low (1 credit/call) | Pinpoint fact checking, finding URLs, quick docs lookup |
| **Clean Page Scrape** | `POST https://api.firecrawl.dev/v1/scrape` | 2 to 5 sec | Low (1 credit/page) | Extracting clean Markdown from known URLs, bypassing popups/cookies |
| **Autonomous Deep Research** | `POST https://api.firecrawl.dev/v2/agent` | 30 to 90 sec | Dynamic (`spark-2` agent) | Multi-step research, cross-source synthesis, competitive analysis |
| **Agent Job Status** | `GET https://api.firecrawl.dev/v2/agent/{jobId}` | < 1 sec | Free polling | Checking status (`processing` vs `completed`) |

---

## 2. Optimal Execution Rules for Agents

Before launching any Firecrawl agent or search batch, follow these guidelines:

### A. Provide a Strict JSON Schema
Never launch an autonomous Firecrawl agent with an open-ended freeform prompt if you need structured, parseable facts. Freeform prompts cause the underlying agent (`spark-2`) to return conversational prose with inconsistent headings.
* Always supply the `schema` parameter in the `/v2/agent` payload.
* Specify exact fields: `summary`, `comparison`, `evidence`, `citations`, `strengths`, `risks`.
* See `references/firecrawl/schema-cookbook.md` for standard schemas.

### B. Frame Positive Constraints Over Negative Ones
Firecrawl web agents have an inherent bias toward conversational consensus. 
* Negative constraints like "do not use blog posts" frequently fail.
* Use positive domain routing: "Prioritize official vendor documentation, primary GitHub repositories with commit history, and verified benchmark leaderboards."
* Explicitly require source citations and quote extracts for load-bearing factual claims.

### C. Guard Against Rate Limits and Concurrency (HTTP 429)
The Firecrawl API enforces concurrent request thresholds on standard keys.
* When an autonomous agent job (`/v2/agent`) is actively running in the background, firing parallel `/v1/search` requests can trip HTTP 429 (Too Many Requests).
* Sequence operations: execute initial targeted searches first, then launch the deep agent job, or use polling intervals of 5 to 10 seconds between status checks.

### D. Budget Protection via `maxCredits`
On open-ended exploration prompts, set `"maxCredits": 10` (or appropriate threshold) in the `/v2/agent` JSON body to cap credit burn. Always log `creditsUsed` from the agent completion payload.

### E. File Organization & Provenance in ai-os
* **Raw Agent Payloads:** Persist completed agent responses to `.firecrawl/<topic>-agent.json` or `scratch/firecrawl_results/`. The `.firecrawl/` directory is git-ignored and holds raw machine output.
* **Briefs:** Save structured instructions as `research/YYYY-MM-DD-<slug>-firecrawl-brief.md`.
* **Distilled Reports:** Translate valuable findings into permanent markdown files in `research/YYYY-MM-DD-<slug>-report.md`. Append the ingest or research milestone to `wiki/log.md`.

---

## 3. Python Orchestration Pattern

Agents should execute Firecrawl jobs using the standard Python runner pattern at `references/firecrawl/runner.py`.

Key elements of the script:
1. Load `FIRECRAWL_API_KEY` directly from the root `.env` without exposing secrets.
2. Dispatch payload via `urllib.request` (zero third-party dependency overhead).
3. Asynchronously monitor job progress with exponential backoff.
4. Write structured result to `.firecrawl/` and print status summaries.

---

## 4. Subfolder Map

Detailed companion guides live in `references/firecrawl/`:

* `references/firecrawl/agent-guidelines.md`: Writing high-yield prompts, scoping search depths, and setting up adversarial evaluations.
* `references/firecrawl/schema-cookbook.md`: Reusable JSON schema templates for model comparisons, competitive teardowns, and curriculum research.
* `references/firecrawl/runner.py`: Standard executable script for launching and monitoring agent jobs.
