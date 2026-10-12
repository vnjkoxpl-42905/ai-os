# Most skills were invisible to the model, and many loaded copies were stale

Run 2026-10-12 with the Karpathy method (mechanism first, predict then measure, verify what the runtime actually loads). Earlier audits ([2026-10-10](../skills-2026-10-10-repairs/SUMMARY.md), [2026-10-11](../skills-2026-10-11-native/SUMMARY.md)) repaired skill *content*. This pass checked what Claude and Codex actually *load* and *see*, which those audits did not measure.

## Why unpopular skills stayed unpopular

Claude Code shows the model each skill's name, and its description only while a budget lasts. Reconstructed from the installed binary and confirmed by a live debug run:

- Budget = 1% of the context window (30,000 characters here). Measured: **403 skills wanted 126,322 characters.**
- Descriptions are handed out by recent use (count × weekly half-life), then in listing order: home skills A to Z, then vault skills.
- A never-used skill gets no description, so it cannot trigger on its own, so it stays never-used.

The result was backwards. `academy-guide`, `algorithmic-art` and `brand-guidelines` got full descriptions because they sort early. `transcript-intake`, `post-session-recap`, `pickup`, `level-up`, `guided-drill-assignment`, `lsat-u-platform-actions`, `tutorocean-profile-fill`, `prompt-architect-refiner`, `lsat-lab-sync` and `morning-brief` were names only.

Usage across 669 local sessions (491 Claude, 178 Codex) confirms the picture: 88 skills were ever deliberately used. The top ten: session-handoff 63, grill-me 28, impeccable 22, ingest 22, assign-lsatu-work 21, wait-what 19, grilling 13, karpathy-teach 13, second-brain-query 10, watch 10. Data: [usage_all.json](analysis/usage_all.json).

**Fix (vault `.claude/settings.json`, reversible):** `skillListingBudgetFraction` 0.015; 69 never-used vendor skills hidden from the model but still runnable as `/name` (Workspace recipes and personas, team/enterprise Workspace admin, Anthropic brand, Slack GIF); 183 never-used generic skills listed by name only. That includes the 23 Expo/EAS sub-skills, which are routed through `expo-overview`, the router Expo designed to be loaded first. Generator: [listing_overrides.py](listing_overrides.py).

| Live check (headless `claude -p`, debug log) | Before | After |
|---|---|---|
| Skills listed / demand / budget | 403 / 126,322 / 30,000 | 372 / 72,691 / 45,000 |
| 10 sampled core skills with a description | 0 of 10 | 10 of 10 (quotes match the files word for word) |
| `academy-guide`, `brainstorming` | described | name only |
| `recipe-find-free-time` | name only | not listed (still `/recipe-find-free-time`) |

Cost: the listing can grow from 30,000 to 45,000 characters, roughly 3,750 more tokens per message in AI OS sessions only.

## Claude loads the home copy, not the vault copy

When a skill exists in both `~/.claude/skills` and the vault's `.claude/skills`, Claude Code loads the home copy. Proof: this session listed the home `bootcamp-builder` description; no other copy contains that text. The validator compared the catalog only with vault copies, so it reported PASS while the copies that actually run had drifted. 142 home Claude copies differed from the catalog.

Synced 16 skills where the loaded copy had verified wrong facts or unsafe instructions (43 file writes across 39 installs; every overwritten file backed up in [backups/](backups/); [receipts](sync-receipts.json)):

| Skill | What the loaded copy got wrong |
|---|---|
| superwhisper | Recording key was Ctrl+Space. `superwhisper/CLAUDE.md` says Left Alt. |
| wrapup | Wrote log entries at the TOP in an old format under `~/ai-os/`. Schema: append at the bottom as `## [date] op \| Title`. |
| pickup | Vault root `~/ai-os/`, which does not exist on Windows. |
| bootcamp-builder | "After clean diff + green build, commit and push without asking"; dead archive paths; missing `teaching-preferences.md`. The Codex copy lacked 49 lines of your 2026-10-11 corrections. |
| lsat-u-platform-actions | Chrome-only; said there is no backend path. Current route is the headless `lsat-u-lessons` MCP and Node CLI. |
| guided-drill-assignment | Old in-vault app path; no inspect / recommend / assign split. |
| lsatu-cc-handoff | Ten `~/ai-os/` paths. |
| lsat-lab-mega-set | Deleted wrong practice sets automatically; dead log path. |
| session-handoff | Corrupted `~/.Codex/` paths in Codex copies. |
| grilling, grill-with-docs, chief-of-staff | Home copies shadowed newer vault copies. |
| booking-link, lsat-u-architecture, pull-submissions, resume | Catalog itself had dead paths; fixed there first, then synced. |

Before syncing, every line unique to a loaded copy was reviewed ([loss_check.py](analysis/loss_check.py)). One real loss was caught: the catalog had dropped the React controlled-input rule (learned 2026-07-16). Restored to both catalogs. The Claude catalog also lacked the Codex copy's Paid session credits section (Stripe crediting rules from 2026-10-02); added.

## Other repairs

- **pull-submissions was broken on Windows.** Reproduced first with a stub `curl` so nothing reached the backend: `/c/Users/Joshu/ai-os/.env: No such file or directory`. The script now finds the vault itself. It still stops at `need jq installed`: `jq` is not on this machine.
- **assign-lsatu-work** said credentials live in `~/ai-os/.env`, "which is not a git repo". Both claims are false here. Corrected. Its description was 1,086 characters (spec limit 1,024); now 851 with every category and nearly every trigger phrase kept.
- **kling-cli** was missing for Claude. The 2026-10-07 `npx skills add` install wrote only to `.agents/skills`. Restored from the catalog (0.2.0).
- **Gemini/Antigravity `audit`** pointed at a rubric, history, compatibility checks and a report template that were not in its folder. Added.
- **Validator:** `check-skills.sh` now skips the Windows Store `python3` stub (open since 2026-10-10). New check (k) fails when a home copy silently shadows a different vault copy (negative-tested: a fixture with one stale shadow, one dispatcher and one identical copy flagged exactly the stale one). New (l) warns with a count of home copies that differ from the catalog. A paragraph in `PARITY.md` had exempted 26 skills from drift checks just by mentioning them in backticks; `kling-cli` slipped through that way. Fixed.

## Wiki scan

- Structural lint: 3,896 pages, 2 findings. Both are links in `wiki/log.md` to files that no longer exist: `raw/README.md` and `references/ai-workspace/expert-teaching-workflow.md`. The log is append-only, so they were left as they are.
- Four web clips sit in `raw/` instead of `raw/inbox/` and were never ingested: "5 GitHub Repos Kill AI Slop, Go Viral, Make Money", "7 Key UI Design Principles + How To Use Them", "Fable 5.1 FINALLY Kills AI Website Slop", "GPT-6 Astra FINALLY Kills AI Website Slop". The clipper now saves to the inbox correctly; these are older strays. `raw/` also holds a 26 MB `lsatu_260719.backup.zip` and a stray memory note.
- `wiki/tasks.md` is stale: its date says 2026-09-30, it was last edited 2026-10-08, and October work is barely in it.

## Left for Joshua

1. **Remaining drift:** 121 home Claude copies, 125 in `~/.agents` and 53 in `~/.codex` still differ from the catalog. They are mostly vendor and generic skills. The validator now shows the count on every run. Worth reviewing in batches, using the same sync tool.
2. Install `jq` for pull-submissions (`winget install jqlang.jq`).
3. Twenty claude.ai account skills duplicate local ones (`anthropic-skills:pdf`, `docx`, `skill-creator`, `grill-me` and others). Removing them is an account change.
4. Ingest the four stray clips, and update `wiki/tasks.md` at the next wrapup.
5. `level-up` exists in two designs: the generic AIS-OS version (loaded) and the AI OS adaptation (catalog). Pick one.
6. Codex has its own budget and dropped all descriptions on 2026-10-10. Not addressed in this pass.
7. Minor: `scroll-craft` links a CHANGELOG its installer did not copy; the Codex project `gws-gmail` links helper skills that live only in `~/.agents`; Gemini `codex-build`/`codex-review` reference `claudex-loop`, which is not installed for Gemini.

## Assumptions and limits

- "Never used" means on this Windows laptop. MacBook sessions are not in these logs. Name-only is reversible: edit [name-only.json](name-only.json) and rerun the generator.
- The precedence rule was observed for Claude. Codex precedence was not tested; making every copy identical removes the question for the 16 synced skills.
- The budget model matched the observed listing to within one 36-character description. The live checks sampled 13 skills, not all of them.
- The listing settings apply only to sessions opened in AI OS. LSAT U app sessions are unchanged. Plugin skills cannot be overridden.
- Another session installed 37 skills into the vault at 01:17 during this run and mirrored them into the catalog. Their files were not touched. The Expo router rule was added because the measurement showed they would push three core skills back to names only.
- Not run: pull-submissions against the backend, any Kling generation, any send. The karpathy subagent was not used. This was a repair of the skill system that depended on this session's evidence, so the method was applied directly and graded here.

## Seven-rule grades

1. **Reconstruct the mechanism: pass.** Budget formula, ranking and precedence read from the installed binary, then confirmed in live runs.
2. **Small baseline: pass.** Before-measurement (403 / 126,322 / 30,000); single-case repros of shadowing (`bootcamp-builder`) and pull-submissions before any general fix.
3. **Predict, run, compare: pass.** Predicted 334 skills, a 45,000 budget, 10 of 10 core described, NONE and ABSENT; observed the same. One prediction failed: I expected YAML errors and found none.
4. **Counterexample and repair: pass.** The pull-submissions failure was reproduced, then fixed. The shadow check flagged the planted stale copy. Two of my own bugs were caught and fixed: a regex the shell had stripped of backslashes, and a hide rule that would have hidden your `persona-agent-creator`.
5. **Verify relevant behavior: pass for Claude.** Proof is what the runtime loaded (hot-reloaded descriptions, headless listing), not file equality. Codex runtime loading was not exercised.
6. **Explicit assumptions: pass.** See above.
7. **Earned complexity: pass.** Used Claude Code's own settings instead of a new mechanism; two small scripts; about 40 validator lines; the router rule was added only after a measurement showed it was needed.

## What I ran

Inventory and YAML parse of 1,910 skill copies across 10 roots; usage scan of 669 session logs counting only real tool calls; stale-path scan; the reconstructed budget model and its calibration; three headless `claude -p --debug-file` runs; a stubbed pull-submissions run before and after the fix; the validator through `check-skills.sh`, plus a negative fixture; a sync dry run, then the real sync, then an idempotence rerun; `wiki-maintenance.py --lint`.

## What came out

Validator PASS (Claude 311, Codex 299, Gemini 222) with drift warnings. Sync rerun: 0 writes. Live listing: 372 skills; all sampled core skills described. pull-submissions now stops at the missing `jq`, not a path error. Wiki lint: 2 findings.

## What I changed

Vault: `.claude/settings.json` (listing keys only), `system/scripts/check-skills.py` and `check-skills.sh`, `skills/PARITY.md` (one paragraph), `skills/README.md` (two sections), catalog skills `booking-link`, `lsat-lab-mega-set`, `lsat-u-architecture`, `lsat-u-platform-actions`, `pull-submissions`, `resume`; `.claude/skills/kling-cli` restored; Gemini `audit` support files added. Home: the 16 synced skills across `~/.claude`, `~/.agents` and `~/.codex`, plus `assign-lsatu-work` in both home roots. Nothing deleted, sent, published or committed.
