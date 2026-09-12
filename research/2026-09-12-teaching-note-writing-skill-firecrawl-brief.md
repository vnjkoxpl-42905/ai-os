---
title: Firecrawl brief: research a high-quality teaching-note writing skill
date: 2026-09-12
status: research-brief
---

# Research brief

Find and rank the best publicly documented writing methods, teaching-note frameworks, or open-source skill repositories that could be adapted into a reusable skill for Joshua's LSAT post-session notes.

## What the skill must support

- Notes are written for a student after a tutoring session.
- The note should be concept-first, concrete, and easy to scan.
- It should explain the reasoning that transfers to new LSAT questions, not retell the conversation or praise correct answers.
- It should include a compact explanation, a diagnostic of the student's practice, and tangible next steps.
- It should sound plain, direct, confident, and human. Avoid cliches, motivational filler, play-by-play narration, and unsupported claims.
- It should distinguish what the source session actually established from interpretation or future practice.
- It should work for a range of students and topics, not only one recap.

## Research scope

Use Firecrawl search/scrape/agent capabilities. Prefer authoritative primary sources and maintained public repositories: university writing centers, established instructional-design or learning-science organizations, respected style guides, and GitHub repositories with clear licenses, recent activity, and usable documentation. Search for methods such as explanatory writing, feedback, retrieval practice, worked examples, backward design, cognitive load, and meeting/session notes, but do not assume a method fits; evaluate it.

Include any especially strong repository or skill template that could be adapted, while separating an actual reusable skill from a general article or course. Do not recommend installing unknown code or copying copyrighted text. Do not use Joshua's private notes as public evidence.

## Deliverable

Return a research report in structured JSON with:

1. A ranked shortlist of 5-8 candidates. For each: name, type (skill/repository/framework/guide), exact URL, maintainer or institution, evidence of quality/maintenance, license if applicable, core method, and fit for post-session LSAT notes.
2. A scoring table using explicit 1-5 scores for pedagogical usefulness, transfer to student notes, clarity/scannability, adaptability to Joshua's voice, evidence/authority, and implementation cost. Explain the weighting.
3. The top recommendation and two backup choices, with reasons and cautions.
4. A proposed skill specification for this use case: trigger/description, workflow, note structure, style rules, failure modes, and a small quality checklist. This is a design proposal, not a claim that a source already provides it.
5. At least three source-backed examples of principles that should appear in the skill. Keep quotations short, give exact URLs, and include section headings or timestamps when available.
6. Uncertainties, copyright/license caveats, and anything requiring human review.

Do not invent sources, repositories, licenses, quotations, or maintenance signals. If a candidate cannot be verified, mark it as unverified and exclude it from the ranking.
