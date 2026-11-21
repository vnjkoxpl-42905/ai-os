---
type: source
subject: Jeff Su video on giving an AI agent a file-management rulebook, then a daily reviewed filing task
created: 2026-10-14
updated: 2026-10-14
aliases: [Stop Organizing Files Yourself, Jeff Su file rulebook, AI file management rulebook]
tags: [ai-workspace, automation, file-management, google-drive]
evidence: "../../raw/sources/clips/stop-organizing-files-yourself-jeff-su/Stop Organizing Files Yourself.md"
sha256: 1f7f58517a363f2f25cd8c507860597f7b9f51286623d52b625d4b5463d42b5f
sources: [../../raw/sources/clips/stop-organizing-files-yourself-jeff-su/PROVENANCE.md]
contradictions: []
---

# Jeff Su's file rulebook: the agent proposes, you approve, and the rulebook learns

"Stop Organizing Files Yourself" is a YouTube video by Jeff Su ([YouTube](https://www.youtube.com/watch?v=peP_o66u-vM)), inferred from the jeffsu.org links. Sponsor: Dropbox. The publication date is unknown; the inbox file was last modified 2026-10-14. The description and the auto-caption transcript (to 14:22) were read in full on 2026-10-14. His starter rulebook and prompts sit behind a link and were not fetched.

Evidence: [archived clip, provenance and hashes](../../raw/sources/clips/stop-organizing-files-yourself-jeff-su/PROVENANCE.md). SHA-256 `1f7f58517a363f2f25cd8c507860597f7b9f51286623d52b625d4b5463d42b5f`.

## What he says

- **The problem (0:50).** People know how they want files organized; the tedious part is doing it every time a file arrives.
- **A rulebook with three parts (1:35 to 3:41).** An organization framework (his "area first" variant of Tiago Forte's PARA: each life or work area holds resources, projects and archive), naming conventions (short descriptive names for documents, year and quarter first for project folders, full date for receipts and invoices), and a filing workflow that says when to ask and how to save new preferences.
- **Small example (3:56 to 5:54).** A root folder with `00 inbox` and `01 reference`; the rulebook is a Markdown file in reference. The agent reads it, proposes a new name and location for each inbox file, moves nothing yet, and asks when it cannot tell (personal or business card). He answers once, says "remember the card rule", and the agent writes the rule into the rulebook. Desktop agents only; web chat cannot touch local files.
- **Existing cloud files (7:51 to 12:19).** Mount Google Drive for desktop rather than using a connector. Ask for two read-only snapshots: the current folder tree and a proposed future tree under the rulebook. The agent flags structural problems and asks clarifying questions. Exceptions you want (his root-level quick-share folder) go into the rulebook. He recommends doing the first reorganization by hand with the agent guiding, moving whole folders and skipping renames. Pro tip: a `legacy` folder to start the root fresh.
- **Automation (12:34 to 14:22).** A daily scheduled task, run in the folder that holds the rulebook, reports proposed changes; he replies "approved". Expect more feedback in the first days; he claims about 95% accuracy after two weeks.

## Mentions in source

> "this will not work in a normal web chat." (4:20)

> "the AI saved our card rule" (5:30)

> "Ignore file name changes for now so it doesn't become a huge renaming project." (11:21)

> "But after two weeks, the reports should be around 95% accurate with minimal input from you." (13:52)

## How it compares with ai-os (interpretation)

Checked on disk 2026-10-14.

- **The pattern is already how the vault files knowledge.** `raw/inbox/` is an inbox folder, the [schema](../../system/schema/llm-wiki.md) is the rulebook, `second-brain-ingest` proposes and files, and corrections become rules. His "the agent writes the preference into the rulebook" matches how memory and skills are updated here.
- **Personal files have no rulebook.** `~/Downloads` held 182 entries on 2026-10-14 and `second-brain-ingest` already searches it for sources, but nothing names or files the rest. Queued as AQ-014 in the [AI action queue](../../references/ai-workspace/action-queue.md): proposal only, moves on Joshua's approval.
- **His safety shape fits the vault rules.** Read-only snapshots first, a plan before any move, approval per batch. The vault's no-delete rule and the Drive delete denial stay in force; nothing in his method needs deletion.
- **His Drive advice conflicts with nothing here but differs in route.** He prefers a mounted Drive folder over a connector; Google access here is the `gws` CLI by rule. Which route a rulebook run would use is a step in AQ-014.

Related: [Jeff Su on personal agents](personal-agents-clearly-explained-jeff-su.md), [Austin Marchese's automation steps](automate-99-percent-work-claude-austin-marchese.md), [AI workspace hub](../../references/ai-workspace/index.md).

## Limits

- Auto-captions: "Taj, Claw" and "Chachi PT", "Kashibb" are ChatGPT and Claude; "PAR framework" and "parap" are PARA; "Thiago" is Tiago Forte. "Gemini Spark" and "ChatGPT Work" are product names as captioned and were not checked.
- The 95% accuracy figure and five months of daily runs are his claims.
- The starter rulebook was not read.


## Queue record

Partial 2026-10-26: AQ-014. Rulebook now has proposal-only defaults and refreshed metadata (194 files,5305489837bytes). Remaining: actual original/new-name/destination filing batch and row approval. Nothing moved or deleted. [Implementation record](../../research/2026-10-26-source-implementation/REPORT.md).
