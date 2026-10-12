---
type: source
subject: Jack video, 10 new GitHub repos for Claude and ChatGPT
created: 2026-10-12
updated: 2026-10-12
aliases: [10 New Github Repos to Make Money in 19 mins, ten repos clip]
tags: [ai-workspace, claude, github, tools, skills]
sources: [../../raw/sources/clips/10-new-github-repos-make-money-19-mins/PROVENANCE.md]
---

# Ten repos worth a look: mostly a launch-week hype list, two overlap with what we already have

"10 New Github Repos to Make Money in 19 mins" is a YouTube video by a creator who calls himself Jack ([YouTube](https://www.youtube.com/watch?v=zwQmodmp1To), publication date unknown). The full clip (description plus transcript, about 20 minutes) was read on 2026-10-12. The transcript is ASR-grade and mis-hears several names; the repo links in the description are the authority.

Evidence: [archived clip, provenance and hashes](../../raw/sources/clips/10-new-github-repos-make-money-19-mins/PROVENANCE.md). Archived clip SHA-256 `83905a7fce8fc1d7b19653dd16d5b3ad9ee9643c78acd8eb641880a67494ea42`, verified against the inbox original.

## What the video claims

All of this is the narrator's account. No repository was opened or tested during this ingest.

| # | Tool (description link) | Claim |
|---|---|---|
| 1 | PhotoCraft, Artcraft suite (`storytold/photocraft`, getartcraft.com) | Open-source Photoshop-style editor, part of a "Craft" suite of about 12 apps (Lightcraft for Lightroom, Filmcraft for Premiere, Vectorcraft built in Rust, PDF Craft, Wordcraft). Claude can edit inside it with computer control. Said to have 39,000 stars in 10 days. |
| 2 | Compositor (`robbietilton/Compositor`) | A second open-source Photoshop rebuild with Claude working in the layers. Narrator prefers its UI slightly. |
| 3 | Ego Lite (short link only) | A browser for AI agents that works in the background without taking over the screen, uses the user's logged-in sessions, runs one tab per agent task, and accepts any model. Free from `lite.ego.app` (as heard in captions). |
| 4 | Rea (`morluto/rea`) | Ask how any app does something, see the evidence, and have the same feature built into your project. One-command setup. Said to have 65,000 stars and to be the fastest-growing repo that week. |
| 5 | 21st.dev and its MCP (short link) | A UI component library. The MCP lets Claude pull footers, navbars, pricing sections and so on without browsing. Narrator used it for his own product UI. |
| 6 | Find Skills (`vercel-labs/skills`) | A skill that finds the best skill for a task. Said to be the top skill on Skills.sh. The narrator warns never to install a skill without having Claude or ChatGPT review the repo first. |
| 7 | Orca (`stablyai/orca`) | Run many agents side by side on separate tasks and review each one's work. Said to have about 89,000 stars, mostly gained that month. |
| Bonus | Zapier MCP (short link) | One shared set of app connections with per-action permissions (for example, read Gmail but not send), reused across agents. |
| 8 | Arena Skill (`Jakeschincariol/arena-skill`) | Runs 100 answers to one question through bracket-style pairwise comparisons until one wins, then explains why. |
| 9 | Universal Modder (`rehan-remade/universal-modder`) | Give it a game and it builds a mod. Narrator calls it early and fun. |
| 10 | Cloudflare Security Audit Skill (`cloudflare/security-audit-skill`) | Turns an agent into a security auditor: reconnaissance, coverage hunting, candidate validation, structured output, independent record verification, target-neutral reporting. Narrator suggests running it before shipping a client app. |
| Bonus | SlopMonster (`ItsssssJack/SlopMonster`) | Rewrites text to sound human and, he says, to follow marketing and sales practices that convert. The narrator's own repo. |

The description and closing also promote the narrator's paid "Agentic OS" course and community, a Zapier link and a Glaido speech product. The title's "make money" is not supported by anything in the transcript.

## What it means here (interpretation, not source fact)

- **Already covered.** We already have a `find-skills` skill in the catalog ([skill catalog](../../skills/INDEX.md)), and the Claude Code `security-review` skill covers part of the audit job. Neither needs a new install on the strength of this clip.
- **Closest to current work.** The Cloudflare audit skill is the only item with a plain fit: LSAT U ships to students, and a pre-release security pass is a real gap. Orca overlaps the multi-agent terminal work we already settled on with Herdr ([Herdr summary](herdr-claude-codex-headache.md), [Claude plus Codex](../../references/claude-plus-codex.md)).
- **Weak fit.** The Adobe-style editors, Universal Modder, SlopMonster and Arena do not match any open item. SlopMonster's goal also conflicts with Joshua's writing rules: his voice standard lives in [teaching voice](../teaching-voice.md), and an automated "sound human" rewriter is not a substitute.
- **Safety note from the source itself.** Zapier MCP and any agent-browser that reuses logged-in sessions widen what an agent can reach. The Google Workspace grant is already broad, so any such connection needs the restraint at the tool-permission layer, not in wording.
- **Hype signal.** The star counts (39,000 in 10 days, 65,000, 89,000) are the narrator's figures and are unverified. Repo names and ownership are also unchecked; several look like very new, unvetted projects.

## Status of each idea

All twelve items are **captured** only. None is evaluated, tested, installed or activated. Before relying on any of them, inspect the actual repository (the schema's rule for repos and skills) and check overlap with the catalog.

## Which ones are of value (checked 2026-10-12)

GitHub API check on 2026-10-12. Contents of the repositories were not opened or run.

| Tool | GitHub state | Value to you |
|---|---|---|
| Cloudflare security-audit skill | 28k stars, MIT, pushed 2026-09-14 | **High.** Pre-release security pass for LSAT U. Evaluate with Anthropic's Claude Security from the [Nate Herk clip](100-github-repos-for-claude-nate-herk.md) and pick one. |
| Orca | 90k stars, MIT, pushed today. "ADE for working with a fleet of parallel agents," your own subscription, desktop, mobile and remote runtime | **Medium, kept alongside Herdr.** It overlaps Herdr's job, but the repo advertises mobile and remote runtime. Herdr is installed; Orca is not. Compare only if Herdr falls short. |
| Find Skills (`vercel-labs/skills`) | 34k stars, MIT, v1.7.2 released 2026-10-09 | **Already have it; now updated.** See below. |
| 21st.dev | Magic MCP repo: 6k stars, ISC, pushed 2026-09-09 | **Medium for UI work.** Resolved below. Not installed. |
| Rea | 113k stars, MIT, pushed today | **Medium-low.** "Reverse engineer anything with agents." Interesting for studying how other prep platforms work; no open task needs it. |
| Zapier MCP | not a GitHub repo | **Low, with a caution.** One more connection layer on top of `gws`. |
| PhotoCraft | 49k stars, Apache-2.0 | Low. No design-editing task is open. |
| Compositor | 16k stars, MIT, "Photoshop alternative for Mac" | Low. Mac only. |
| Ego Lite | `lite.ego.app` (resolved from short link) | Low. Your Chrome extension and the in-app browser already cover this. |
| Universal Modder | 6.7k stars, MIT | None for LSAT U. |
| Arena Skill | 460 stars, MIT | Low. Hundred-way sampling is costly; 460 stars means little vetting. |
| SlopMonster | 895 stars, MIT | Low, and the "sound human" goal conflicts with your own voice standard. |

## 21st.dev, resolved

- The `bit.ly` link in the description points to `https://21st.dev/`, a library of "12,000+ crafted React components, templates, and shadcn themes."
- The Magic MCP repo (`21st-dev/magic-mcp`) now says Magic MCP **has been replaced by the 21st MCP**. Install is `npx @21st-dev/cli@latest init --client claude`, or add the HTTP server `https://21st.dev/api/mcp` with an `x-api-key` header.
- It needs a free API key from `21st.dev/mcp`. Old Magic keys were reset. A Claude Code plugin route exists (`claude plugin marketplace add 21st-dev/magic-mcp`, then `/plugin install 21st`, key in `API_KEY_21ST`).
- Without the paid AI tier, only `search` and `get_component` work; `generate` needs AI access enabled.
- Fit: LSAT U is React, Tailwind and shadcn, which matches the library. Per your global rule, the key would go in the root `.env`, never in chat.
- **Not installed.** Installing needs your key and a configuration change.

## Find Skills, updated

Compared the catalog copy with upstream `vercel-labs/skills` (`skills/find-skills/SKILL.md`, 2026-10-12). The only upstream differences were the new `--owner <owner>` option for `npx skills find` and the broader trigger wording. I added `--owner` to both catalog copies (`skills/claude/find-skills`, `skills/codex/find-skills`) and kept your narrower local trigger ("only when asked to find or install a skill"). The upstream file no longer lists `npx skills check`; I left that line in the local copy because I did not verify the CLI dropped the command.

## Second clip generation

Joshua re-clipped the same video on 2026-10-12. The second file (SHA-256 `dfa4f73a1449c81988e1f0c15b0fd786b226a64a1450c902a4be8819e5f0cdec`) differs only in line endings and is archived beside the first.

## Limits and open questions

- Publication date and channel name are unknown.
- Zapier's short link was not opened.
- Open: evaluate the Cloudflare audit skill and Claude Security together against LSAT U? Proposed, not agreed.

Related: [AI workspace hub](../../references/ai-workspace/index.md).
