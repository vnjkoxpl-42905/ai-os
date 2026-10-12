---
type: source
subject: Nate Herk video, best GitHub repos for Claude
created: 2026-10-12
updated: 2026-10-12
aliases: [I Tried 100+ Github Repos for Claude, Nate Herk repos clip]
tags: [ai-workspace, claude, github, skills, tools]
sources: [../../raw/sources/clips/100-github-repos-for-claude-6-best/PROVENANCE.md]
---

# Nate Herk's picks from 100+ Claude repos: most of the value is in tools LSAT U already touches

"I Tried 100+ Github Repos for Claude. These 6 Are the Best." is a YouTube video by Nate Herk ([YouTube](https://www.youtube.com/watch?v=HhZdNYI4pJs), publication date unknown). The full clip was read on 2026-10-12. The title says 6, the transcript says 10, and the description lists 12 repos; the description is the most complete list. His framing is agency work: build something a business will pay for.

Evidence: [archived clip, provenance and hashes](../../raw/sources/clips/100-github-repos-for-claude-6-best/PROVENANCE.md). Archived clip SHA-256 `6ab288c538c24f952e6607ce61afe86f6b736fbe6874e8ee166ffa7d3039d1d6`.

## His recommendations, with a check against GitHub

Star counts and push dates are from the GitHub API on 2026-10-12. The behavior descriptions are his claims; no repository was installed or run.

| Repo | His claim | GitHub check (2026-10-12) |
|---|---|---|
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | Describe a video in natural language; Claude builds it from HTML and renders a real MP4 locally, no per-render fees. Prefers it to Remotion. | 61k stars, Apache-2.0, pushed today. "Write HTML. Render video. Built for agents." |
| [googleworkspace/cli](https://github.com/googleworkspace/cli) | One CLI for Drive, Gmail, Calendar, Docs, Sheets, Slides, with 40+ skills. Works in Claude Code and Codex, unlike the desktop connectors. | 31k stars, Apache-2.0, pushed 2026-10-06. |
| [apify/apify-mcp-server](https://github.com/apify/apify-mcp-server) | Connects Claude to thousands of hosted scrapers (Instagram, TikTok, Amazon). Connector is open source; scrapers cost per result after $5 monthly free credit. | 10.6k stars, MIT. |
| [nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft) | His own skill: a scroll engine plus design rules and a screenshot checker for Apple-style scroll sites. He discloses he built it. | 3.2k stars, MIT. |
| [blader/humanizer](https://github.com/blader/humanizer) | Removes AI tells from text, based on a guide Wikipedia editors use. | 55.8k stars, MIT. |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | `/spec`, `/plan`, `/build`: puts the plan into files so a fresh session can resume. Easier than Superpowers for newcomers; mentions Matt Pocock's skills as a bonus. | 105k stars, MIT, pushed 2026-10-10. |
| [expo/skills](https://github.com/expo/skills) | Official Expo skills for mobile apps. Name them explicitly because they do not always auto-load. | 2.8k stars, MIT. |
| [supabase/agent-skills](https://github.com/supabase/agent-skills) | Supabase security rules for Claude (users see only their own data). Set the connector read-only and test as one user. | 2.8k stars, MIT. |
| [stripe/ai (stripe-best-practices)](https://github.com/stripe/ai/tree/main/skills/stripe-best-practices) | Install only the one skill, not the full plugin, which he says may route vendor decisions through Stripe. | 1.9k stars, MIT, pushed today. |
| [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) | Opens a real browser, clicks through the app, writes rerunnable tests. A CLI, so lighter on tokens than an MCP. | 14k stars, Apache-2.0. |
| [Claude Security](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-security) | Anthropic's plugin: agents hunt for holes, other agents try to disprove each finding, plain-English report, can write patches. | Lives inside Anthropic's official plugin directory (37k stars, pushed 2026-10-11). Plugin folder contents not opened. |
| [every-app/open-seo](https://github.com/every-app/open-seo) | Real keyword, ranking and backlink data inside Claude. Small free credits; data sits on their server unless self-hosted. | 23k stars, MIT. "Open source alternative to Semrush and Ahrefs." |

**Token savers (8:56, citing a JetBrains test).** He says Caveman cut about 8.5% of output tokens against an advertised 65%, RTK saved nothing and raised cost at low effort, and Ponytail saved about 10% per task but has an open Windows bug that can stall every message for several seconds. He recommends Codeburn for seeing where tokens go, and says to hold off on Claude Mem (sends usage data by default) and Context Mode (open bug that can burn usage). These are his report of a third-party test, not checked here.

**His advice on starting.** Do not install all of them; pick the one that fixes your current problem, and if unsure start with the Google CLI, Apify, Scrollcraft or Humanizer. Install skills only after having Claude review the repo.

## What is of value here (interpretation)

Ranked by fit with LSAT U and the AI OS, not by his ranking.

1. **Supabase agent skills and Stripe best practices.** LSAT U runs on Supabase and Stripe, so these match live systems. Highest value. Caveat from the vault: the backend is Lovable Cloud-managed, so the "read-only connector" advice needs checking against that setup before use.
2. **Playwright CLI.** A low-token way to click through LSAT U before release. We already have `webapp-testing` and browser tools; the gain is rerunnable tests. Worth comparing, not obviously additive.
3. **Claude Security.** Pairs with the Cloudflare audit skill from the [first clip](10-new-github-repos-make-money.md). Two candidates for one gap (a pre-release security pass); evaluate them together and pick one.
4. **Addy Osmani's agent-skills.** Overlaps the spec/plan/TDD skills we already carry (`writing-plans`, `tdd`, `grilling`). A comparison is useful; installation is probably redundant.
5. **Humanizer.** Overlaps your own voice rules in [teaching voice](../teaching-voice.md) and `no-em-dashes-no-filler`. Useful at most as a lint pass on drafts, never as the voice itself.
6. **Hyperframes.** Competes with Remotion and Kling, which the vault already uses ([video generation options](../VIDEO-GENERATION-OPTIONS-2026-09-09.md)). Worth a test if Remotion's rspack problems recur.
7. **OpenSEO.** Possibly relevant to lsatprep.study acquisition; free credits are small and data leaves your machine unless self-hosted.
8. **Already have it:** Google Workspace CLI (`gws`), Firecrawl in place of Apify, Ponytail (already in the skill list).
9. **Not a fit now:** Expo (no mobile app), Scrollcraft (a website-design skill from the narrator; we have several design skills).

Everything above is **captured** only. None is evaluated, tested or installed.

## Limits

Publication date unknown; the count in the title does not match the content; his income and agency claims are unverified; the Claude Security plugin was not opened.

Related: [ten-repos clip](10-new-github-repos-make-money.md), [Greg Isenberg's five repos, incl. NVIDIA SkillSpector](greg-isenberg-5-github-repos-ai-slop.md), [AI workspace hub](../../references/ai-workspace/index.md).
