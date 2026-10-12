---
type: source
subject: Greg Isenberg video, five GitHub repos (No AI Slop, agent CRM, Video Use, SkillSpector, Phone Harness)
created: 2026-10-12
updated: 2026-10-12
aliases: [5 GitHub Repos Kill AI Slop Go Viral Make Money]
tags: [ai-workspace, repositories, writing, security, skills]
sources: [../../raw/sources/clips/greg-isenberg-5-github-repos-ai-slop/PROVENANCE.md]
---

# Five repos, and a habit: install one, make one small workflow work, then decide

Greg Isenberg's solo episode "5 GitHub Repos: Kill AI Slop, Go Viral, Make Money" ([YouTube](https://www.youtube.com/watch?v=9_SZFIW7tus), published 2026-09-02, clipped 2026-09-08). The full clip, description and transcript (about 24:40) were read on 2026-10-12. Evidence: [archived clip, provenance and hashes](../../raw/sources/clips/greg-isenberg-5-github-repos-ai-slop/PROVENANCE.md), SHA-256 `5ff5ecec3ac5c93da33b6016a5f61acf930a7d0aab8b1c31679d07a6fd805915`.

## What the video claims

All of this is the narrator's account. None of the five repos was installed or tested here.

| Repo | What he says it does | Setup he describes |
|---|---|---|
| [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | Editor skill that strips patterns that make writing read as AI ("it's not X, it's Y", over-symmetry, words like "quietly") while keeping the writer's voice. Workflow: human rough draft first, AI cleanup second. (1:44) | `npx skills add <repo>` |
| [trycompai/crm](https://github.com/trycompai/crm) | Open-source CRM run by an agent: researches people, enriches companies, schedules follow-ups, keeps notes current. Start with one pipeline of warm leads you cannot afford to forget. (5:20) | bun + docker; local on ports 3000/3001; Google or Microsoft OAuth for mail and calendar |
| [browser-use/video-use](https://github.com/browser-use/video-use) | Coding agents edit raw footage: cut filler and dead space, subtitles, grading, overlays, render, then check the output. Start with one repeatable format. (10:52) | Agent-run install; needs FFmpeg and a paid ElevenLabs key |
| [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | Scans agent skills and repos for prompt injection, data exfiltration, supply-chain risk, hidden instructions and MCP risks before you install them. `--no-llm` gives a static scan that sends no file contents to a model. (15:15) | `uv tool install git+<repo>`; `skillspector scan <dir or GitHub URL>`; Docker option |
| [ShawnPana/phone-harness](https://github.com/ShawnPana/phone-harness) | Lets Codex or Claude Code operate a real phone (iPhone through macOS iPhone mirroring, Android through ADB) for mobile QA and API-free automations. Early: locked phones, Face ID and camera flows are hard. (18:49) | macOS Sequoia+ for iPhone; `phone-harness --doctor` |

The closing method (22:25): install the repo, get one small workflow to add value, then decide whether to productize it or keep it as personal leverage. He suggests a monthly habit of trying new repos.

## Where it touches this workspace

- **No AI Slop overlaps existing rules.** Joshua's writing rules already ban the same patterns (CLAUDE.md voice rules, [teaching voice](../teaching-voice.md)), and a `humanizer` skill was activated on 2026-10-12. Proposed, not tested: compare no-ai-slop against `humanizer` on one real draft before adding a second editor.
- **SkillSpector is the most relevant to current risk.** Over 80 third-party skills were installed into this vault on 2026-10-12 from public repos. Proposed, not done: run `skillspector scan --no-llm` over newly installed third-party skills as an install gate. This is a recommendation, not an adopted decision.
- **Phone Harness and the CRM are not a fit now.** There is no LSAT U mobile app, and Cal.com, Gmail and Supabase already own the booking and student relationships ([connections](../../connections.md)).
- **Video Use** sits next to the existing video options ([video generation options](../VIDEO-GENERATION-OPTIONS-2026-09-09.md), HyperFrames skills). Not evaluated.

## Limits

Claims are from one creator's walkthrough. Star counts, current install commands and costs were not checked. The episode says "six repos" at 0:43 but covers five.
