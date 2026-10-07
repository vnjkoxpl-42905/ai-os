---
type: reference
subject: Firecrawl agent brief guidelines and prompt architecture
updated: 2026-09-19
aliases: []
---

# Firecrawl Agent Guidelines — Prompt Architecture & Brief Writing

This guide establishes the prompt standards and research workflows for launching autonomous Firecrawl agents (`POST /v2/agent`).

---

## 1. Core Principles for Briefs

When writing a prompt for a Firecrawl agent, avoid conversational questions. Firecrawl agents perform best when given a structured mission brief containing five components:

1. **Objective Statement:** A clear, bounded goal describing the desired deliverable.
2. **Authority Hierarchy:** Explicit ranking of acceptable sources (e.g., vendor documentation, GitHub source trees, peer-reviewed papers vs generic secondary blogs).
3. **Extraction Criteria:** Specific facts, code snippets, numbers, or qualitative arguments required.
4. **Negative Guardrails:** Specific failure modes to reject (e.g., unverified marketing claims, hallucinated dates, forum speculation).
5. **Output Schema:** A companion JSON schema defining exact field types.

---

## 2. Prompt Template

Use this standard structure when crafting agent briefs:

```text
Objective: [State the precise technical, pedagogical, or architectural goal]

Primary Research Targets:
- Official documentation from [domain/vendor]
- Public source code repositories, issue trackers, and changelogs
- Primary benchmark reports with reproducible methodology

Required Findings:
1. [Specific question 1: e.g. concrete performance metrics on SWE-bench or WebDev Arena]
2. [Specific question 2: e.g. code maintenance, state preservation, breakpoint handling]
3. [Specific question 3: e.g. pricing, token limits, context window availability]

Guardrails:
- Ground all claims in accessible source URLs. Provide exact citations.
- Reject unsourced secondary blog aggregation where the primary test is absent.
- If data is ambiguous or sources conflict, highlight the contradiction explicitly.
- Do not invent benchmark numbers or extrapolate without stating the assumption.
```

---

## 3. Managing Agent Effort and Depth

* **Standard / Targeted Jobs:** For single-dimension lookups or specific documentation verification, keep the prompt focused and limit search breadth.
* **Deep Multi-Source Synthesis:** For architectural comparisons (like model evaluation or framework adoption), require the agent to cross-reference multiple independent reviews and state points of consensus versus dissent.
* **Credit Safeguard:** Always include a reasonable `maxCredits` cap (default: 10 to 15 credits) to prevent recursive link crawling on deep websites.

---

## 4. Ingesting Agent Results into ai-os

Once an agent job finishes:
1. Verify the JSON output in `.firecrawl/<slug>-agent.json`.
2. Inspect the sources and citations. Do not accept links blindly; ensure the citations resolve to authentic, relevant pages.
3. If the research informs an ongoing decision, record it in `decisions/log.md` or synthesize a full report in `research/YYYY-MM-DD-<slug>-report.md`.
4. Log the completion to `wiki/log.md`.
