---
type: operating-layer
subject: Log
updated: 2026-09-30
aliases: []
---

# Log

Entries before 2026-11 live in `wiki/log-archive-YYYY-MM.md` (moved unchanged 2026-11-20): [[wiki/log-archive-2026-07|2026-07]], [[wiki/log-archive-2026-09|2026-09]], [[wiki/log-archive-2026-10|2026-10]].

## [2026-11-20] system | Log split: July to October entries archived

- `wiki/log.md` went from 931,921 to about 44 KB. The 736 entries dated 2026-07, 2026-09 and 2026-10 moved unchanged into `wiki/log-archive-2026-07.md`, `-09` and `-10` (54 November entries stay). Lint exempts the archives from old-link checks like the log. Pre-split copy was in the session scratchpad. Not yet committed.

## [2026-11-20] synthesis | Second brain setup playbook

- Wrote `wiki/second-brain-setup-playbook.md` from the second-brain source pages: library analogy, ten ranked practices not yet adopted, recommended direction. Nothing decided. One curated line added to `wiki/index.md`.

## [2026-11-20] system | Index shrunk, Karpathy mirrors hidden from Obsidian, own pages committed locally

- Backups: Google Drive is still not mounted (no G: drive); it needs a sign-in in the Drive desktop app, which only Joshua can do. Committed only my nine new pages locally as `b4b639cb` (not pushed). Safety copies of `wiki/index.md`, `wiki/log.md`, `.obsidian/app.json` and `system/scripts/wiki-maintenance.py` taken beforehand to the session scratchpad (temporary folder).
- Index: `system/scripts/wiki-maintenance.py --index` now lists pages under `wiki/sources/karpathy/<folder>/` only through each folder's `catalog.generated` page (counts checked complete: x 2,521, repos 799, github-payload 416, blog 78, lectures 17). `wiki/index.md` went from 1,164,654 bytes to 58,558 bytes (298 lines). Curated hub lines outside the fence were preserved (spot-checked).
- Obsidian: added `wiki/sources/karpathy/` to `userIgnoreFilters` in `.obsidian/app.json`. Nothing deleted or moved; agents can still read the folder. Takes effect when Obsidian is next opened (it was not running).
- Supersedes the 2026-11-20 ingest entry's "catalog NOT regenerated" and its open item on catalog regeneration.
- Verification: structural lint reports 0 findings over 4,007 pages; catalog fences intact; app.json parses.
- Open: index, log, script and app.json changes are uncommitted and mixed with other sessions' changes; Drive sign-in; Obsidian speed not re-measured; `skills/INDEX.md` (about 85,000 tokens) not split; AI-setup hub, AI-setup inbox folder and the index-versus-disk audit script not started.

## [2026-11-20] ingest | Second-brain sources clipped 2026-11-20 (14 clips) and the one-vault-versus-many synthesis

- Scope: 14 clips in `raw/inbox/` modified in the hour before 15:01, read in full by four read-only passes, plus a baseline pass over the 16 earlier second-brain source pages, `references/`, `decisions/log.md` and `Second_Brain_Prompt.pdf`. Line references come from those passes and were not re-checked line by line.
- Archived (6, new evidence, hash verified against the inbox originals): `self-improving-claude-knowledge-base-one-prompt-robonuggets`, `new-way-build-second-brain-claude-nick-saraev`, `new-agentic-os-standard-claude-5-robonuggets`, `grill-me-skill-10x-claude-code-nate-herk`, `steal-my-ai-os-setup-5-tips-nate-herk` (a new generation beside the old-vault copy), `complete-guide-ai-second-brain-claude-comments` (comments plus a machine summary, no transcript; archived only, no wiki page).
- Not archived again (7 re-clips): Every Level of a Claude Second Brain, I Turned Claude Into the Ultimate Second Brain, Build your Ultimate Second Brain with Fable 5 (" 1" copy), Obsidian in 24 Minutes, Stop Prompting Claude (Karpathy method), The Agentic OS Setup That Will 10x Claude Code, and I Turned GPT-6 Astra (byte-identical to its archive). Transcripts match the archived copies; only the frontmatter header or description links differ. Originals stay in `raw/inbox/`.
- Not ingested: Code Mode (RoboNuggets, `Qf0EzOEall8`): about Claude Code token use, not second brains; left in the inbox.
- Created: [one vault versus many](second-brain-one-vault-vs-many.md) and seven source pages: five for newly archived clips (`sources/self-improving-claude-knowledge-base-one-prompt-robonuggets.md`, `sources/new-way-build-second-brain-claude-nick-saraev.md`, `sources/new-agentic-os-standard-claude-5-robonuggets.md`, `sources/grill-me-skill-10x-claude-code-nate-herk.md`, `sources/steal-my-ai-os-setup-5-tips-nate-herk.md`) and first pages for two already-archived clips (`sources/agentic-os-setup-10x-claude-code-chase-ai.md`, `sources/every-level-of-a-claude-second-brain-nate-herk.md`).
- Changed: `wiki/index.md` (one curated hub line only). The generated catalog was NOT regenerated.
- Finding: the committed `wiki/index.md` is 13,203 bytes (121 lines, no Karpathy rows); the working copy is 1,159,899 bytes, regenerated 2026-11-20 07:26, uncommitted, with 3,842 rows for `wiki/sources/karpathy/`. The committed `wiki-maintenance.py --index` lists every page, so running it rebuilds the large index. Not fixed here.
- Also found: Google Drive mirror not running (no G: drive), 6,262 changed or untracked paths in git, `wiki/log.md` at 926,889 bytes, evidence-lock hook script present but not registered in `.claude/settings.json`.
- Conflicts left open: Chase AI's `claude -p` billing claim (2026-06 video) versus the 2026-05 claim in `references/obsidian-command-center.md`; RoboNuggets "file names do not matter" versus Nate Herk's explorer test.
- Verification: SHA-256 of each archived `clip.md` matches its inbox original; originals untouched.
- Open: the one-vault-versus-several decision (not locked); catalog regeneration.

## [2026-11-18] lint | Structural pass on the whole wiki, plus component-library routing and backup

- Scope: `py system/scripts/wiki-maintenance.py --lint` over 3,997 wiki pages (structural only). `--evidence` is not a flag in this script, so raw-archive hashes were NOT re-checked. No semantic or contradiction review was done.
- Findings: 613 total. 607 broken-or-ambiguous links, 553 of them under `wiki/` (the Karpathy repo-file mirrors `wiki/sources/karpathy/repos/files/` account for most; 13 in `wiki/hot-archive/`), and 6 `missing-source-provenance` pages (five `loophole-rc-day-*` summaries and `mcat-cars-three-passages`). None touch `wiki/component-library.md`.
- Fixes applied: none to existing findings (check-only; mass link edits not authorized). New page linked from `wiki/index.md`, `CLAUDE.md`, `AGENTS.md`, `design/README.md`.
- Backup finding: Google Drive desktop was installed but not running, so G: was missing and the "Claude Code Backup" task was exiting 1 (last run 2026-11-18 2:09 AM). Started `GoogleDriveFS.exe`; G: still not mounted after ~2 minutes (likely needs sign-in). Added `component-library` to `setup/backup/backup.ps1` (syntax parses) and made a local git commit in the library folder.
- Unresolved: Drive sign-in; the 607 links; the 6 provenance pages.

## [2026-11-18] system | Saved UI component library made findable

- Joshua could not find his saved 21st.dev components. Found them in `C:\Users\Joshu\dev\component-library` (4 components, added 2026-11-11, created in the "21st MCP HTTP transport setup" session), plus 4 more adapted into the LSAT U checkout.
- Added `wiki/component-library.md` (catalog, how to view, how to add, limits). Routed from `CLAUDE.md` and `AGENTS.md` (same new row in both), `design/README.md`, and the curated Hubs list in `wiki/index.md`.
- Not done: the library folder is still outside version control and has no backup. Generated catalog section of `wiki/index.md` not regenerated by hand.

## [2026-11-14] system | Ore's reference replaced by the full Famous Flaws note

- Source: Joshua's canonical Famous Flaws catalog (15 flaws, 3 groups, 68 answer-choice phrasings), already built as `brainstorms/2026-11-11-ore-post-session/famous-flaws-full/`; found only after Joshua asked for a full search of earlier flaw notes (assignment export query found 18 flaw-related notes across students).
- Changed on LSAT U: "Famous Flaws" posted to Ore; "The Four Flaws to Know First" hidden; recap re-posted with its next-step line updated. Local: one line in `brainstorms/2026-11-11-ore-post-session/build.py`, `students/ore/assignment-log.md`.
- Verification: dry-run before posting; `verify_existing` returned both notes already_current with matching SHA-256; admin item list shows the old reference archived.
- Not checked: the note's content against the canonical file by Claude (relied on its own 44/44 verifier, run in `C:/Users/Joshu/dev/famous-flaws-build`); the final slot-filling step and last fixes were never re-reviewed by Codex (usage limit); phone use by a real student; admin list shows due dates one day later than the readback (likely time zone, unconfirmed).
- Open: Codex candidate recap and reference (`codex-candidate/`) unused; their new visual pieces were never approved.

## [2026-11-14] system | Ore flaw notes rebuilt by Codex through claudex-loop (candidate, not posted)

- Process: Codex reviewed the work order over four rounds (REVISE, REVISE, APPROVED, APPROVED after a `py` to `python` edit), built it, and Claude inspected. Two fix rounds followed Claude's rendered-page inspection (wrong sentence in flaw 1, reference numbering and spacing, diagram symbol, hero label overlap, then reference sheet padding).
- Candidate files: `brainstorms/2026-11-11-ore-post-session/codex-candidate/` (recap.html, reference-four-flaws.html, NEW-PIECES.md, REPORT.md, build.py). The build also lives in the isolated checkout `C:/Users/Joshu/dev/ai-os-codex-ore` (uncommitted, with two stashes of aborted runs).
- Verified by Claude: byte-identical rebuild, primer unchanged (SHA-256 2b001ccd...), headless Chrome renders at 640, 1000 and 1400 px, a 375 px frame, script test of five tap-to-check rows and all four switch states, no script errors, no sideways scroll, LSAT U dry-run reports both notes would update in place.
- Not verified: keyboard activation (inconclusive test), a real phone, print layout. Codex changed the recap's CSS in the last round although only the reference was requested; the recap was re-checked at phone width and by script, not re-compared pixel for pixel at 1000 px.
- Open: Joshua's approval of the new visual pieces and of re-posting; the vault's Taste skill is the older High-Agency version, not v2.

## [2026-11-14] system | Codex sandbox can run Python (mxc mode enabled)

- Changed: `prefer_mxc = true` in `~/.codex/config.toml` (backup kept); fixed an argument bug in `system/scripts/run-codex-build.ps1`; recorded the result in `references/claude-plus-codex.md`.
- Verification: `python -V` inside the mxc sandbox printed 3.12.10; a throwaway runner build created the file and ran a Python proof inside Codex; Claude checked the file and removed it.
- Open: network access and `py` remain unavailable inside the sandbox; the Ore flaw-notes build still has not been completed (an orphaned Codex process kept running after the Terminal tab was stopped and had to be killed; its partial work is in `git stash` in `C:/Users/Joshu/dev/ai-os-codex-ore`).

## [2026-11-14] system | Codex build path set up and tested on Windows

- Source: [ClaudeX Loop clip summary](sources/claudex-loop-chase-ai.md) and the upstream `chaseai-yt/claudex-loop` README and VALIDATION notes (both CLIs installed and authenticated; Codex's Windows sandbox has known limits that must not be bypassed).
- Changed: installed `@openai/codex` 0.169.0 in the real PowerShell; moved the unreadable `~/.codex/.sandbox-secrets/sandbox_users.json` aside (kept as `.bak-2026-11-14`, new file recreated); added `system/scripts/run-codex-build.ps1`; rewrote the 2026-11-14 section of `references/claude-plus-codex.md`, correcting the earlier wrong explanation.
- Verification: a throwaway build through the runner with Codex as builder wrote the expected file (checked byte for byte by Claude, then removed). Not tested: `run-codex-build.ps1` itself, a build with a real work order, the `inspect` step.
- Open: Codex's sandbox cannot run `python`, so the host runs the proof. The Ore flaw-notes build has not been launched.

## [2026-11-14] ingest | Chase AI's ClaudeX Loop walkthrough

- Source: [source summary](sources/claudex-loop-chase-ai.md). Clip `This Open Source Repo Solve Claude's 1 Problem.md`, 15,673 bytes, SHA-256 `f281fc7536a196bd82726cf7c7b288644639dce3287fec31f007618cc0b8d7f7`, archived byte for byte in `raw/sources/clips/claudex-loop-chase-ai/` with provenance and hash manifest. Inbox original kept.
- Revision check: the old vault holds a different capture of the same video (hash `1d1b46ac...`, adds frontmatter, body identical). Not a duplicate by hash, so a new source page; the older capture stays as evidence for the recovered-methods page.
- Changed: new source summary; `references/claude-plus-codex.md` (link and the 2026-11-14 Codex-from-Claude-app finding); `references/ai-workspace/action-queue.md` (AQ-048).
- Already here: ClaudeX Loop is installed (2026-09-30) with matching round limits, an assumptions ledger and fresh inspection.
- Pages considered: `references/ai-workspace/migrated-source-methods.md` (complementary, no edit), `wiki/sources/meet-new-codex-cli.md` (skip).
- Verification: archive hash re-checked; source quotes checked by the wiki lint; index refreshed.
- Open: whether the round-limit extension is wanted (AQ-048). The video and demo were not inspected. The Codex run from the Codex desktop app is untested.

## [2026-11-14] system | Ore's recap and reference re-posted in the upgraded design

- Source: local rebuild in `brainstorms/2026-11-11-ore-post-session/build.py`, using Yahunathan's 2026-08-19 Famous Flaws notes, the raffle and bicycle anchor (2026-10-03) and the corpus Flaw model picks. Approved by Joshua in chat.
- Changed: two notes revised on LSAT U (older versions archived), `students/ore/assignment-log.md`.
- Verification: `assign_student_work` posted both and `verify_existing` returned already_current, with SHA-256 matching the local files.
- Open: the platform notified Ore again for each revised note; the shared note shell still has the narrow-width hero overlap; the drill note still mentions "all fifteen" Famous Flaws.

## [2026-11-14] system | Ore assigned after the 2026-11-11 session

- Source: `students/ore/homework/2026-11-11-homework-proposal.md`, approved by Joshua in chat on 2026-11-14. Plan `students/ore/assignments/2026-11-11-session-work.json`.
- Changed: three notes and three guided drills assigned to Ore on LSAT U; created `students/ore/assignment-log.md`; proposal status updated.
- Verification: `assign_student_work` with `verify_existing` returned all six items verified (exact note HTML, dates, 7/12/10 questions, difficulty 1-3, 1-3, 2-4).
- Open: each drill's run stopped on "New bell count differs" and needed a re-run, so notification counts per item are unchecked. RC passages not assigned (Joshua's call). Charles's note and homework not built; Sabrina Egal's drafts not checked.

## [2026-11-14] system | Correction: active post-session-recap copies were the newer ones

- Corrects the entry above. The active copies (`.claude/skills/post-session-recap`, `.agents/skills/post-session-recap`, identical, last changed 2026-11-13) are newer than the catalog copy and hold the Session Desk work (`references/session-desk/`). They were not overwritten.
- Changed: both active `SKILL.md` files now say one post-session note per session, with a drill note only when a drill has no intro; the "three-note set" (decided 2026-10-25) is replaced.
- Open: lines about building a primer and method reference (build-output list, whole-set preview, corpus-grounding line) still mention them in the active copies. `skills/claude/post-session-recap` (edited earlier today) and `skills/codex/post-session-recap` are not synced to the active copies and still differ. Not run against a real session.

## [2026-11-14] system | Assignment vocabulary settled in CONTEXT.md and applied

- Source: grill-with-docs session with Joshua, 2026-11-14 (nine questions). Terms are in `CONTEXT.md`.
- Changed: `CONTEXT.md` (post-session note, post-session homework, teaching note, Warm-Up, adapted note, proposal, draft, assign, assignment, assigned work, status, model note, quality bar, assigned-work archive; "post-session package" retired). Applied to `wiki/homework-assigning/note-formula.md` (two kinds of note), `rules.md`, and the catalog copy of `skills/claude/post-session-recap` (`SKILL.md`, `references/notes-and-homework-package.md`).
- Finding: Joshua retired Before you start, Reference and Follow-up as kinds of note, because a guided drill already carries its own intro. The old rule "every guided drill is paired with a note" is now "only when the drill has none".
- Verification: wording edits only; the skill's behaviour change (one teaching note per topic instead of three) was not run against a session.
- Open: the active skill copies `.claude/skills/post-session-recap`, `.agents/skills/post-session-recap` and `skills/codex/post-session-recap` already differed from the catalog copy and lack `notes-and-homework-package.md`; they were not touched and still carry the old wording. Generated pages (`playbook`, `by-topic`, `taxonomy`, `assignment-log`) keep real note titles such as "Before you start: ..." because those are records.

## [2026-11-14] system | Sofia and Celia assigned-work packages filed

- Source: read-only LSAT U export re-run 2026-11-14 12:38 UTC (`wiki/homework-assigning/data/assignments.generated.json`); Sofia 47 rows (20 notes, 21 drills, 5 activities, 1 bootcamp module), Celia 28 rows (7 notes, 8 drills, 11 activities, 2 bootcamp modules).
- Changed: new `students/sofia/assigned-work/` (19 note folders) and `students/celia-cutler/assigned-work/` (7 note folders), each with a README index, `note.html` and a per-note `CLAUDE.md` linking the session transcripts in `transcript-downloads/` (not duplicated). Linked from `sofia.md`, `celia-cutler.md`, `students/README.md`, `wiki/homework-assigning/README.md` and `wiki/index.md`. Desktop copies exist at `Desktop/Sofia - Assigned Work` and `Desktop/Celia - Assigned Work`.
- Finding: Parallel Reasoning (both students) exists only as Markdown in the archive, so its HTML is rebuilt. Welcome to your classroom is a one-line stub. Sofia's Famous Flaws notes (2026-08-19) are tied to no session. Drills, activities and bootcamp modules are indexed, not attached.
- Verification: export re-run 2026-11-14 matched both packages (47 and 28 rows; 19 and 7 note folders; every note.html byte-identical to the refreshed archive where an original page exists); all local links in the new files resolve; `wiki-maintenance.py --index` refreshed the catalog (3,995 pages, now listing `homework-assigning/`); `check-student-records.py` reports no error naming `assigned-work` (its 70 existing errors are older unlinked exports and packages, 23 of them for Sofia and Celia).
- Open: the 2026-10-25 post-session pages (recap, drill primer, method reference) for both students do not appear as assigned items and were not included.

## [YYYY-MM-DD] type | Title` so `grep "^## \[" log.md | tail -5` gives the last 5 events. The pre-rebuild log was removed from disk 2026-07-17 (recoverable from git history).

## [2026-11-01] change | Celia Cutler recap set restyled (version E)
Joshua chose version E "studio" as the main build for the 2026-10-29 set: dark hero, interactive graphics, question list. Originals kept in brainstorms/2026-10-29-celia-cutler-post-session/versions/original-gold/. Unapproved, unassigned, unposted. Student record Markdown not yet resynced to the new wording.

## [2026-11-01] change | LSAT U single-question page published (PR 258, PR 259)

PR 258 added /question/lr/:pt/:section/:qnum. PR 259 rebuilt it on the drill question pane (tinted stimulus column) and added a Show session notes toggle for PT151 Section 4 Questions 10 and 16 (marked sentences, answer verdicts, lesson labels; off by default, nothing saved). Both merged to main (merge commit 6876432) and published with deploy_project; live bundle index-AjrjT6jK; Q16 opened signed in and the notes toggle worked. Celia Cutler recap cards link to Q10 and Q16; her set is still unapproved, unassigned and unposted, and Joshua has not read the new sentence notes and verdict lines.

## [2026-11-01] change | Celia Cutler Q16 lesson wording corrected against the transcript

Joshua flagged "Stay inside the author's world" as meaningless: it was only the focus when going through the answer choices. Transcript check (about 01:11 to 01:13): the conclusion predicts a new world, each answer must be about that world, A describes the current one. Heading and lesson label are now "Ask which world the answer is about" in the recap set (main build, E build, original-gold base, recap.src.html) and the student record; A and E verdict lines reworded. LSAT U page text fixed in PR 260 (open, not merged). Older theme versions A to D still carry the old heading as history.

## [2026-11-01] publish | LSAT U Q16 lesson wording corrected, live
PR 260 (merge c8a7d37) merged and published with free deploy_project after latest_commit_sha matched. Live bundle index-AjrjT6jK -> index-D1mC5dI2. Checked signed in on /question/lr/151/4/16 with notes on: lesson "Ask which world the answer is about", A tag "About today's world" with the new text, E reworded; old "author's world" wording absent. Celia's set remains unapproved, unassigned, unposted.

## [2026-11-01] publish | LSAT U question page: plain passage, notes beside it, live
PR 261 (merge 12a97a3) merged and published with free deploy_project after latest_commit_sha matched. Live bundle index-D1mC5dI2 -> index-Deg_Cbk4. Checked signed in on /question/lr/151/4/16: no highlight marks on the passage, notes quote each sentence with its note, "Take this with you" list present, no horizontal scroll at phone width. Celia's set still unapproved, unassigned, unposted.

## [2026-11-10] system | Skills activation repaired on fresh GitHub clone
- Cloned `vnjkoxpl-42905/ai-os` to `C:\Users\Joshu\dev\ai-os` (core.longpaths on). Activated the 12 skills CLAUDE.md lists as active but that were missing from `.claude/skills/`: pickup, wrapup, session-handoff, audit, level-up, consultation-inquiry-drafts, consultation-followup-drafts, inbound-tutoring-replies, guided-drill-assignment, lsat-u-platform-actions, tutorocean-profile-fill, prompt-architect-refiner.
- Closed the undeclared Claude/Codex drift both ways: 10 skills copied into `.agents/skills/` (from `skills/codex/`), 7 into `.claude/skills/` (assign-lsatu-work, gws-gmail, gws-gmail-read, gws-gmail-triage, gws-shared, pre-consultation-check-in, superwhisper).
- `check-skills.py` now reports only the 12 dead-path items for `raw/` and `../ai-os-projects/`, which GitHub excludes by design. Restore those from the private backup when needed.
- Machine: installed gh, uv, firecrawl-cli; registered the 10-minute "Claude Code Backup" task. `python3` in Git Bash resolves to a Windows Store stub, so run `check-skills.py` with the real Python 3.13.

## [2026-11-10] system | Full skill catalog activated in both runtimes
- Joshua asked for every skill he previously had to be live, overriding the "catalog is inert" default for this machine. Copied all catalog skills not already active: 182 into `.claude/skills/` (now 220) and 165 into `.agents/skills/` (now 206, including 4 Codex-only entry points that have no catalog copy).
- Nothing was overwritten. Two active copies differ from the catalog and were left as they are: `.claude/skills/lsat-lab-lecture-transcribe` and `.agents/skills/gws-gmail`. Not adjudicated.
- Skipped on purpose: `skills/claude/_inactive/` (13 retired skills), `_snapshots/`, `_project-forks/`.
- `check-skills.py` still reports only the same 12 dead-path items for `raw/` and `../ai-os-projects/`. Not committed.

## [2026-11-11] system | New laptop restored from the 2026-11-01 backup
- Incident: the 2026-11-10 restore copied Drive `current\`, which `backup.ps1`'s `/MIR` had already overwritten from the fresh clone. The vault lost most of `wiki/`, and Claude chat history and memory were missing. The 10-minute backup then mirrored that state over Drive. The task was disabled from 2026-11-11 10:10 until the restore was complete.
- Downloaded the 38 generation folders the 2026-11-01 Restore-Index needs (144 GB) to `C:\Backups`. Google Drive for desktop dropped `G:` three times under this load, so most of it came through the Drive API (`gws`). `new-machine-restore.py` verified every SHA256: 626,525 core and 34,841 personal files.
- Merged, add-only, into the vault, `../ai-os-projects` (85 projects), `~/.claude`, `~/.codex`, `~/.agents`, `~/.gemini`, `~/.config`, Superwhisper and Desktop/Documents/Downloads/Pictures. Restored files carry today's date, so the merge overwrote local files. 4,246 files edited here after 2026-11-01 were put back from `C:\Backups\live-pre-merge-20261111`. `~/.config/gws` was put back from Drive `current\dotfiles`.
- Result: `wiki/` has 47 files again (hot, index, log, tasks present), Claude memory has 73 files, Claude chat history is 1.5 GB. Git history is identical on GitHub, local and the restore (`7e3a37c4`). gh, gws and Codex are signed in; Superwhisper runs. The backup task is enabled again.
- Open: `check-skills.py` reports 45 index and activation-drift problems after the restore. Checklist: `setup/NEW-LAPTOP-CHECKLIST-2026-11-11.md`.

## [2026-11-13] intake | 13 Gemini session transcripts filed
- Filing only, no recap, lesson, assignment or email. Exported 13 native Gemini Docs by Doc ID (gws drive files export, text/plain) and filed them unedited: Sofia 8 (2026-11-01, 11-02, 11-03, 11-05, 11-06, 11-07, 11-08, 11-09), Celia 1 (11-05), Yahunathan 1 (11-05), Zeina 1 (11-11), Ore 1 (11-11), and _other-sessions 1 (2026-11-10 Sabrina, reduced-rate booking; no student folder, none created).
- Newest-first rows with Doc ID and SHA-256 added to each student transcripts.md. No session packages, teaching notes or open loops written. Session dates are the ones Joshua supplied (EST); Doc header dates are UTC and differ by a day for four Sofia and Yahunathan files. No Calendar cross-check run for these 13.
## [2026-11-13] booking | Yahunathan credits

At Joshua's request, created an active two-credit, 70-minute booking pass for Yahunathan Zetvy (ynproemail@gmail.com). Fresh LSAT U readback confirmed 0 used and 2 remaining, with no expiry. His previous pass was exhausted at 8 of 8 used and was preserved. Pass ID: `2e91d4b9-1246-4c29-a2c4-849f06b66a94`.


## [2026-11-14] system | Workspace redesign implementation in progress

- [Plan and progress](../brainstorms/2026-11-14-claude-codex-workspace-redesign.md); [Start Here](../references/ai-workspace/Start-Here.md); [switching agents](../references/ai-workspace/switching-agents.md); [health report](../system/generated/workspace-health.md).
- Preserved hashed settings, grouped temporary projects reversibly, reconciled the two LSAT U roots, and removed only orphan Orca registrations. Existing unfinished checkouts and native histories remain.
- Focused hook checks and a synthetic round trip through the actual backup and restore scripts passed. The doctor fixture tests passed; the live skill validator reports existing failures, and current sync/production backup remains unproven.
- Claude CLI sign-in expired, so the real cross-agent handoff, fresh hook review, remaining-task rollout and seven-day trial are open. See the plan for evidence, checkout inventory and exact limitations. Task ledger unchanged.
- Follow-up: 20 doctor/checkpoint fixture tests passed; the stale-HEAD check used a retained Git fixture. The report writer uses cooperative locking and a final comparison, not a proven atomic guard against noncooperating writers.
- A sandboxed `gws` metadata attempt tried to remove two credential-cache files after keyring denial; both removals were denied and both files were confirmed present. No cloud-generation evidence was obtained. A Firecrawl credential appeared in initial chat metadata output and should be rotated; its value was not recorded here.


## [2026-11-17] intake | Lanae: 2026-11-17 transcript filed, folder brought current

- Found and exported the newest Gemini Doc (2026-11-17 session, native Doc ID 1aBn-dNa9fNX6x1lUxbdTwwg5LWJgSPva_G1qQxIahw8, SHA-256 4f583680...5ad7) to `students/lanae/transcript-downloads/`. The 2026-11-14 export, filed earlier the same day, re-verified against its recorded hash.
- Built three-file session packages with provenance for 2026-11-14 and 2026-11-17. Distilled teaching notes, open loops with owners and dates, stated preferences and the session index. Refreshed only Lanae's live-status mirror (13 credits, 4 used; it read 10 on 2026-10-31).
- Gaps: Calendar events on 2026-11-05 and 2026-11-12 have no Gemini Doc in the Drive searches run, so those sessions are unverified. No session package for 2026-10-29. Conditional boot camp promised twice is not in her LSAT U assigned list as read from the local mirror; not assigned by this run. No recap, assignment, message or send performed.

## [2026-11-17] ops | Lanae: Conditional Logic Bootcamp assigned

- At Joshua's request, assigned the Conditional Logic Bootcamp (`conditionals`, Classroom item 28314761-4616-4e81-a9e8-63e8c4d696fe) to Lanae with no due date, through the local MCP after a dry run. A readback found one active copy and no resend. Inbox, bell and email notifications accepted. It covers the promised conditional boot camp, quantity statements (Part 6) and must-be-true (Part 7). Still open: the 2026-11-14 note and recap, a separate must-be-true drill if wanted, and a next session.

## [2026-11-17] skill | post-session-recap learned from Sara Altuwaijri's note

Added `references/house-look.md` (neutral palette, equation card, color marks, ladder, "What you said" block, tooling gotchas), `references/examples/sara-2026-11-16-note-builder.py` (multi-note builder), a dated calibration section in `recap-calibration.md`, executor gotchas in `notes-and-homework-package.md`, and short edits to `SKILL.md`: fusion pass (transcript, corpus, posted notes, claims table), one scope per note with a 2,100-word strict cap, homework resolved before the note's closing list, open the render for Joshua early. Claude copy only; the Codex copy was not changed. Source: the 2026-11-17 Sara session and about twenty correction rounds.

## [2026-11-17] ops | Lanae: guided drill assigned

- At Joshua's request ("pick one"), assigned Conditional Logic (Easier) Set 4 (`w5-02-conditional-logic-easier-set-4`, 9 questions, difficulty 1-2, unlock 2026-11-17, due 2026-11-24) to Lanae through the local MCP. The tool verified it and reported inbox, bell and email accepted. Dates and drill were my choice, not specified by Joshua.

## [2026-11-17] fix | lsatu-work-plan.ts no longer requires the activity flag

`assign_student_work` refused activities for students whose `has_activity_access` was off. The 2026-10-02 profile trigger forces that flag false on every access write, so it can never be set; activities open through `ActivityAssignmentGate` (assignment-only). Removed the activity flag check (guided drills still require `has_drill_access`), matching the existing bootcamp handling. Found while assigning Negation Station to Sara Altuwaijri. Dry run and live assignment verified. Not yet viewed from a student session.

## [2026-11-17] fix | post-lesson revises in place instead of re-notifying

Joshua saw Sara's thread show "New note: Necessary Assumption" twice (22:34 and 23:01) because a revision archived the old note and posted a new, notified one. `system/scripts/lsatu-admin.mjs post-lesson` now PATCHes the single live copy's HTML in place (same item id, no new message); `--new-version` restores the old behavior. Dry run and syntax check only; not yet exercised live. The stale 22:34 message (link to the archived item) is still in Sara's thread pending Joshua's yes to unsend it.

## [2026-11-17] build | LSAT U messages sidebar mod (Claude desktop pane)

New mod `lsatu-messages` at `C:\Users\Joshu\.claude\dev-mods\131e9043-6957-4fbb-aff4-4d898459e061\lsatu-messages\` draws a "LSAT U messages" pane: students waiting on a reply first, with an in-pane reply box. Data comes from new read-only `system/scripts/lsatu-conversations.mjs` (automatic "New assignment/note" posts do not count as replies). Reply is staged, then sent only when Joshua presses Send, through `system/scripts/lsatu assign --message`, and logged in `wiki/send-ledger.md`. "Mark handled" is remembered in the mod store. Passed `claude plugin validate`; not yet seen rendering.

## [2026-11-18] query | Teacher side reorganization
Diagnosed the chaotic teacher side from the command-center spec, build review and 2026-10-28 quality review; proposed decisions D1-D7 in brainstorms/2026-11-18-teacher-side-reorganization.md. Nothing built.

## [2026-11-18] fix | Component library routing
Joshua asked for his locally saved 21st components; the agent searched paths for "21st" and missed `dev/component-library` (slugs omit the word). Added loose-reference table and content-search rule to `wiki/component-library.md`, a pointer in `design/library.md`, and automemory `saved-components-live-in-component-library`.

## [2026-11-18] lint | Full vault structural lint
Scope: 3,997 wiki pages via wiki-maintenance.py --lint, plus CLAUDE/AGENTS parity, memory index targets, hot.md size. Findings 613 -> 76 after two linter fixes in system/scripts/wiki-maintenance.py: wikilinks to name.py now resolve to name.py.md (Obsidian behaviour; 532 false index hits), and <angle-bracket> links with ")" in the path parse correctly. Remaining: 45 links inside immutable Karpathy source copies (left), 28 dead paths in history records wiki/log.md + hot-archive/2026-10.md (history keeps old names; left), 2 example-syntax links in gd4ai source, 1 wikilink to a memory slug in RRC-DRILL-AUDIT-CRITIQUE, 6 loophole-rc/mcat source pages missing provenance. hot.md is 44 KB (updated 2026-11-14), past its purpose. --evidence hash check is documented in the skill but not implemented in the script. Semantic contradiction review not run.

## [2026-11-18] lint | Fixes applied
Un-indented the frontmatter and body of loophole-rc-day-1/2/3/6/7 source pages (4-space indent hid frontmatter and rendered bodies as code); added `sources:` to mcat-cars-three-passages. RRC-DRILL-AUDIT-CRITIQUE now names the automemory note in text instead of a dead wikilink. Moved hot.md session entries 2026-10-25 to 2026-10-30 (133 lines) to hot-archive/2026-10.md with relative links rebased; hot.md 44 KB -> 12 KB. wiki-maintenance.py now writes via temp file with retry (report write was failing with Errno 22 under a file lock). Lint 76 -> 69: remaining are history-record and immutable-source links plus 2 example links in the gd4ai source.

## [2026-11-18] lint | Semantic contradiction review (report only)
Three read-only reviewers: context layer (CLAUDE/AGENTS/memory/hot/decisions), curated wiki, context+design+corpus. 11 errors, 16 warnings, 6 questions; nothing edited. Key: CLAUDE.md "Learned rules" Activities-access line contradicts activities-only-when-assigned + decisions/log.md:240; design/principles.md:48,63 still beige + colour status vs near-white/one-ink direction; lovable-cloud.md:20 says Edge Functions deploy on push; ASSIGN-AN-ACTIVITY.md flag step + browser path superseded; dashboard.md and several pages point at ../ai-os-projects/lsatu; claude-code-backup-to-drive memory says plaintext secrets on Drive vs encrypted-package rule; codex-model-roles memory path dev/tools/node missing; $45 per hour vs 70 min unresolved; Cal.com window 45 days vs 6 business days needs live check; priorities.md post-session deadline window open now. Unverified against live systems.

## [2026-11-18] lint | Contradiction fixes applied
Fixed: lovable-cloud.md (Edge Functions deploy via Lovable agent; SQL via MCP query_database), ASSIGN-AN-ACTIVITY.md (headless assign_student_work first; flag step replaced by row verification), app paths to ../lsatu/ in dashboard.md, HANDLING.md, COPY-CORRECTIONS.md, ASSIGN-AN-ACTIVITY.md, context/work.md. Memory: codex path (now AppData/Roaming/npm, codex-cli 0.167.0), assignment paths + assign_student_work, flag-scope note, edge-function route, 2026-10-17 publish rule, backup note (records .env reaching Drive; tension with cloud-transfer rule left for Joshua). hot.md: 5 superseded July/October lines moved to hot-archive/2026-10.md. Lint stays 69. Open for Joshua: Activities rule line in CLAUDE.md, $45 per hour vs 70 min, design/principles.md beige + colour status, post-session deadline, .env on Drive; live checks: Cal.com window/buffer, Supabase map.

## [2026-11-18] decisions | Activities flag never granted; single session $45/hour; design base near-white, beige accent only

## [2026-11-18] design | Teacher Home strip: three versions (A ledger, B rail, C agenda) via claudex-loop in design/prototypes/teacher-home/strip-versions/

## [2026-11-18] design | Teacher Home v2 "observatory" built via claudex-loop at design/prototypes/teacher-home/home-v2/ (strip A chosen)

## [2026-11-20] lint | Structural pass, diagnostic only
- Scope: `wiki-maintenance.py --lint` over 3,997 wiki pages (69 findings, same count as 2026-11-18); index coverage (all pages mentioned in `index.md`); SHA-256 re-check of 110 `raw/sources/**/SHA256SUMS` manifests (965 entries, 0 mismatches). `--evidence` is not a flag in the current script, so the hash check was run separately. Semantic contradictions and factual accuracy were not reviewed.
- Findings: 69 = 13 real in `hot-archive/2026-10.md` (links not rebased after the 2026-11-18 move); 21 real in 13 Karpathy source pages (linked raw files absent from `raw/sources/karpathy-brain`); 13 real in this log (historical paths to deleted `lsatu-*` worktrees, 3 missing local files, 2 non-page references); 22 false positives (RNN sample text, inline-code examples, 2 log prose examples).
- Fixes: none applied; check-only request.
- Open: hot-archive link rebase; Karpathy raw evidence gap; `main` last commit is 2026-10-01 despite auto-backup claims in CLAUDE.md and memory.

## [2026-11-20] lint | Hot-archive links rebased
- Changed: `wiki/hot-archive/2026-10.md`, 13 relative links moved one folder deeper (research, brainstorms, decisions, COPY-CORRECTIONS, log, `ai-os-projects`, `.codex`); no text changed.
- Verification: all 157 local links in the file resolve; structural lint 69 → 56 findings.
- Open: 21 Karpathy raw-file links, 13 historical log links; `main` last commit 2026-10-01.

## [2026-11-20] query | Teacher rail chat tabs

Checked LexPrep Home's add-tab, draft switching, and saved history against the saved LexPrep motion teardown and Classroom design principles. Added observed behavior and proposed LSAT U implementation guidance to [the Classroom design notes](../brainstorms/2026-11-19-classroom-navigation-and-teacher-rail.md). First send, refresh, tab close, and phone layout were outside the live reference check.

## [2026-11-20] system | Laptop first rule
- Changed: added the "Laptop first" guardrail to `CLAUDE.md` and `AGENTS.md` (Guardrails sections identical); removed the duplicate auto-saved line from CLAUDE.md "Learned rules"; updated the `ai-os-vault-location` memory.
- Rule: the laptop folder `C:\Users\Joshu\dev\ai-os` is the primary and only complete copy; Google Drive and GitHub are backups only; never work from a copy or clone.
- Evidence: 28 of the last 30 chats ran in laptop folders; none used Drive or a GitHub clone. Not compared: `dev\ai-os-codex-ore`, `dev\ai-os-github-copy`.
- Open: Drive backup not running (no G: drive); `skill-audit/` nested repo breaks `git switch`; both rule files uncommitted.

## [2026-11-20] lint | Full structural pass, linter inline-code fix

- Coverage: 3997 wiki pages, structural lint only (links, orphans, provenance flags). Factual accuracy not re-reviewed.
- Fix: `system/scripts/wiki-maintenance.py` now ignores `~~~` fences and inline code spans when collecting links, so link syntax shown as an example no longer reads as a broken link. Findings 56 to 52 (the 2 gd4ai examples and 2 others cleared).
- Remaining 52: 18 RNN sample-output false positives in the verbatim karpathy.github.io post mirror (left as is, editing would alter the mirror); 13 historical links in this append-only log (left); 21 Karpathy pages pointing at raw files never archived (`uv.lock`, `Cargo.lock`, `minGPT/projects/`). The snapshot under `raw/sources/karpathy-brain` lacks them; fetching them would change preserved evidence, so it waits for Joshua's approval.

## [2026-11-20] ingest | Missing Karpathy repo files archived

- On Joshua's approval, fetched 13 files that wiki pages cited but the original snapshot lacked (8 `uv.lock`, 1 `Cargo.lock`, 5 `minGPT/projects/` files) via `gh api` from each repo's default branch. Written only to new paths under `raw/sources/karpathy-brain/raw/github/repos/karpathy/`; no existing file changed.
- Provenance and hashes: `raw/sources/karpathy-brain/supplements/github-missing-*/PROVENANCE.json` (URL, last commit SHA, bytes) and `SHA256SUMS` (13/13 OK). These reflect GitHub on 2026-11-20, not the original snapshot date.
- Lint 52 to 31. Remaining: 18 RNN sample-text false positives, 13 historical links in this log.

## [2026-11-20] lint | Zero findings; skill-audit untracked

- Linter: `[[...]]` inside verbatim repo-file mirrors (`wiki/sources/karpathy/repos/files/`) is source text, not a vault link; broken links in this append-only log are history and no longer reported. Markdown links in mirrors are still checked. Probe page with one bad wikilink and one bad Markdown link produced 2 findings, then was removed. Lint 31 to 0.
- `skill-audit/` removed from the index (gitlink with a broken nested `.git`); files stay on disk and `/skill-audit/` is now in `.gitignore`.
- "Laptop first" rule also added to the global `~/.claude/CLAUDE.md`.

## [2026-11-20] ingest | I Studied 10,000 AI Websites (Nate Herk)

- Source: YouTube mImbbszCjCI, published 2026-11-09, full auto-caption transcript. SHA-256 `16426e37...f823`, archived byte-for-byte to `raw/sources/clips/10000-ai-websites-nate-herk/` (shortened filename recorded in PROVENANCE.md); inbox original kept.
- Created [source summary](sources/10000-ai-websites-nate-herk.md). Updated [website design planning](../references/website-design-planning.md) with five review checks, [design hub sources](../design/sources.md), and the [LSAT U idea queue](lsatu-idea-queue.md) with LQ-007 (interactive free sample on lsatprep.study).
- Considered: design/principles.md (complementary, unchanged: already covers layers and motion with a reason); Fable 5.1 source (qualification on parallax, not a contradiction). Scrollcraft already installed; no AI workspace item.
- Gaps: no visuals; quoted conversion figures and studies not verified against originals.

## [2026-11-20] ingest | New Skills! v1.2 (Matt Pocock)

- Source: YouTube gaDdrDdczO4, published 2026-08-05, matching tag v1.2.0 (`e903586b`). SHA-256 `4c8d9657...68b8`, archived to `raw/sources/clips/matt-pocock-skills-v1-2/`; inbox original kept.
- Created [source summary](sources/matt-pocock-skills-v1-2.md); Related link added to the [Austin Marchese Matt Pocock summary](sources/matt-pocock-system-claude-skills-austin-marchese.md) (complementary).
- Already here: all seven named skills active in both runtimes and kept by the 10-day Matt Pocock sync; local copies are newer and edited, not v1.2.0 bytes. No queue items.

## [2026-11-20] system | Herdr setup recheck

- Updated [Claude and Codex reference](../references/claude-plus-codex.md) with Herdr 0.9.5, refreshed integrations and shared CLI authentication checks. The prior installation was absent in the environment checked.
- Verified the release archive against GitHub SHA-256, both integration versions, and each CLI login status. Live Herdr panes and actual model turns remain unverified.

## [2026-11-20] system | Codex daemon startup issue

- Corrected the daemon state directory ACL and documented the remaining missing daemon executable and tested `codex --no-daemon` workaround in [Claude and Codex reference](../references/claude-plus-codex.md). Normal daemon startup remains unresolved.
