---
type: research
subject: Whole-sentence no-op cut candidates in five heavily used skills (AQ-013)
created: 2026-10-14
queue_item: AQ-013
status: proposals only; no skill edited
---

# No-op cuts: about 4.3 KB of sentences that change nothing, mostly in post-session-recap and assign-lsatu-work

A sentence is a candidate when removing it would not change what Claude does. That covers four kinds: it restates something said elsewhere in the same skill, it restates a root rule from `CLAUDE.md`, it is an activation phrase written in the body (the body only loads after the skill has already activated), or it is history or implementation trivia with no instruction in it.

**Never candidates,** and left out on purpose: anything about sending, posting, deleting or unsending, credentials, Lovable credits, student work or student records, and duplicate guards. Where a guardrail is duplicated, both copies stay.

Byte counts are UTF-8, measured 2026-10-14. File sizes are on disk. Sentence sizes are measured with wrapped lines joined, plus one separator byte, so totals are close but not exact.

## second-brain-ingest (`.claude/skills/`, 11,555 bytes)

| # | Sentence | Bytes | Why it does nothing |
|---|---|---|---|
| 1 | "It is the one ingest workflow; no separate alias exists." | 57 | History of the `ingest` rename; no instruction. |
| 2 | "Student/session transcript intake is owned by `transcript-intake`." | 67 | Same as the routing-table row and the "Session transcripts use a separate workflow" section. |
| 3 | "Knowledge-source compilation is this skill's internal reference." | 65 | Already said in the opening paragraph. |
| 4 | "`post-session-recap` owns the complete student-facing session write-up workflow." | 81 | Repeated in the transcripts section. |
| 5 | "A request only to retrieve or file a transcript stays narrow; a recap request goes directly to that skill without asking for a second activation." | 146 | Repeated in the transcripts section ("Do not ask the user to invoke a second skill"). |
| 6 | "He has answered "where is it" too many times." | 46 | Reason only; the instruction before it ("Ask only if that comes up empty") does the work. |
| 7 | "One source at a time unless Joshua explicitly asks for batch work." | 67 | Same as Clips step 1 and the hard rule "Process one source at a time unless batch work is explicitly requested." |
| 8 | "Public lecture transcripts and research interviews supplied as reusable knowledge remain knowledge sources for `second-brain-ingest`." | 134 | Covered by the routing table (public video row) and Clips step 3. |
| 9 | "Purpose determines the route." | 30 | Follows from 8; no new instruction. |
| 10 | "Dedupe before ingesting." | 25 | Hard-rule repeat of "Always" step 2. |
| 11 | "Distinguish archived from successfully compiled." | 49 | Hard-rule repeat of "Always" step 2 and Clips step 4. |
| 12 | "Use the current machine's tools and paths, resolved from the vault root." | 73 | Repeat of "Do not assume a saved Windows or Mac path" in the first section, and of the root rule. |
| 13 | "Ingest adds queue items; only `second-brain-task` approves, builds and clears them." | 84 | Repeat of Clips step 6 ("Ingest never builds an item and never changes another item's status"). |

Candidate total: about 924 bytes (8.0%). Kept although duplicated: "Never move, delete, or modify original sources" (a deletion guardrail).

## post-session-recap (`.claude/skills/`, 17,509 bytes)

| # | Sentence | Bytes | Why it does nothing |
|---|---|---|---|
| 1 | "New transcript retrieval routes to transcript-intake, not knowledge ingest." | 76 | Repeated in "Route overlapping requests". |
| 2 | "Recognize the intent to turn an LSAT tutoring session into a finished post-session lesson." | 91 | Activation guidance in the body; the description already does this. |
| 3 | "The examples below are natural language, not required commands." | 64 | Activation guidance. |
| 4 | "Accept capitalization, punctuation, hyphenation, and ordinary wording variations." | 82 | Default behavior. |
| 5 | "Do not require the exact skill name or a second instruction to create the lesson after intake." | 95 | Repeated at the end of "Route overlapping requests". |
| 6 to 14 | The heading "**Clear activation phrases:**" and its eight bullet lines ("Session write up" through "Make a review note for the student...") | 30 + 44 + 80 + 97 + 95 + 95 + 92 + 148 + 120 = 801 | Trigger phrases are read only to decide whether to load the skill, and that decision comes from the description. Once the body is loaded the list does nothing. The description already holds the main phrases. |
| 15 | "Mentioning a session in scheduling, payment, cancellation, or consultation correspondence does not activate this skill." | 120 | Activation guidance read after activation. Move it into the description if it matters. |
| 16 | "A skill does not monitor the calendar or schedule itself." | 58 | Self-evident; no instruction. |
| 17 | "Use the shared teaching standard when drafting the note." | 57 | Repeat of step "Find and ground the lesson" (read the standard first). |
| 18 | "Keep examples independent of the original test question unless that question is needed to understand the method." | 113 | Repeat of "Teach the concept rather than retelling the question". |
| 19 | "The archived `session-recap` is an internal reference, not an active alternative." | 82 | History; the archived skill is not loadable. |

Candidate total: about 1,639 bytes (9.4%). **Keep:** "Short requests use context" and "Resolve the session" (both change behavior after load). Also keep the whole last paragraph (posting authorization, a guardrail).

One sentence for Joshua to judge: "Draft in Joshua's **teaching-content** register: direct, calm, precise, with short sentences and no em dashes." It overlaps the standard but restates the em-dash ban. Low confidence; not counted.

## transcript-intake (`.claude/skills/`, 6,579 bytes)

| # | Sentence | Bytes | Why it does nothing |
|---|---|---|---|
| 1 | "Resolve the current vault from its instructions." | 49 | Root rule. |
| 2 | "It does not compile session records into the general wiki or create a student-facing lesson." | 93 | Repeated by the routing bullets right below it. |
| 3 | "Report any existing unrelated validator failures separately." | 61 | Default reporting behavior. Low confidence. |

Candidate total: about 203 bytes (3.1%). This skill is already lean. **Kept:** "Never create a student folder without approval" and its repeat in "Archival local transcripts" (student records), and the closing "No lesson drafting ... posting, assignment, email, or source deletion follows from intake" (guardrail).

## assign-lsatu-work (loaded home copy `~/.claude/skills/`, 17,594 bytes)

There is no `.claude/skills/assign-lsatu-work`. Claude loads `~/.claude/skills/assign-lsatu-work/SKILL.md`, byte-identical to `~/.agents/skills/assign-lsatu-work/SKILL.md`. The catalog copies in `skills/claude/` and `.agents/skills/` are 2,507-byte pointers to it, so cuts here apply to the two home copies only.

| # | Sentence | Bytes | Why it does nothing |
|---|---|---|---|
| 1 | "AI OS is a Git repository." | 27 | Root fact. |
| 2 | "On 2026-09-23 it had no `--section`, `--due` or `--set`." | 57 | Incident detail; the "Never `cd projects/lsatu`" rule carries the instruction. |
| 3 | "On 2026-09-10 (a Thursday) Saturday was 2026-09-12; a handoff once carried 09-13, which is the Sunday." | 103 | Anecdote; "Dates are absolute" and its lookup rule carry it. |
| 4 | "There is no RPC and no edge function for it; it is client-side code." | 69 | Implementation trivia; "never hand-write these rows" is the rule. |
| 5 | The section heading "## Checking what a student already has" and its sentence "`system/scripts/lsatu status "Celia"` lists every open classroom item..." | 39 + 147 = 186 | Repeats the `status` line in the Reads block and the "run `status` before assigning" paragraph. |
| 6 | "**Why the timer is real:** `src/lib/drillRunSpec.ts` `singleSectionOf()` sees ... (a stopwatch)." | 202 | App internals; no operator action. |
| 7 | "Shipped with `--section` in PR #113, merged 2026-09-11." | 56 | History. |
| 8 | "Verified live on 2026-09-23: it returns 401 without a token and serves OAuth discovery." | 88 | Hosted connector, marked "not used" on this laptop. |
| 9 | "The source is `src/lib/mcp/` in the app repo, deployed as the `mcp` edge function." | 83 | Same. |
| 10 | "- **Connect:** claude.ai → Settings → Connectors → add a custom connector with that URL, then sign in with an LSAT U account." | 132 | Setup for a connector this skill says not to use. |
| 11 | "There is no key to paste." | 26 | Same. |
| 12 | "- **Who gets the admin tools:** any account with the `admin` role in `user_roles`." | 83 | Same. |
| 13 | "To grant someone access, give their account that role; remove the role to revoke it." | 85 | Same. |
| 14 | "Students who connect see only their own data." | 46 | Same. |
| 15 | "- **Tools today:** `find_students`, ... `list_my_classroom_items`." | 276 | Same. |

Candidate total: about 1,519 bytes (8.6%). **Kept:** the authorization block and its "deliberate, narrow exception" lines (sending), the multi-line refusal and its 2026-09-23 incident (it explains a send guard), "Adding them means app code plus a Lovable deploy, which needs Joshua's credit confirmation first" (Lovable credits), every confirm-first and unsend rule, the credentials section, and the `vite-node` warning (it prevents a bad commit).

**Contradiction, not a cut:** the "Local execution contract (2026-10-10)" says "Respect actual current user authorization, not a historical person-count approval rule". The Authorization section still says to confirm for "3 or more students at once". These disagree. Joshua should say which one stands.

## lsat-u-voice (`.claude/skills/`, 2,250 bytes)

| # | Sentence | Bytes | Why it does nothing |
|---|---|---|---|
| 1 | "The detailed standard is maintained in one place." | 50 | A note for editors; the next sentence ("Do not copy it into this skill...") carries the instruction. |
| 2 | "Resolve the canonical ai-os vault from the workspace instructions." | 67 | Root rule; the relative links resolve without it. Low confidence. |

Candidate total: about 117 bytes (5.2%). Kept: the precedence sentence over vendor `lsat-u-voice` copies (it settles a real name clash) and the last line (posting, assigning, paid media).

## Totals

| Skill | Bytes before | Candidates | Share |
|---|---|---|---|
| second-brain-ingest | 11,555 | ~924 | 8.0% |
| post-session-recap | 17,509 | ~1,639 | 9.4% |
| transcript-intake | 6,579 | ~203 | 3.1% |
| assign-lsatu-work (home copy) | 17,594 | ~1,519 | 8.6% |
| lsat-u-voice | 2,250 | ~117 | 5.2% |
| **All five** | **55,487** | **~4,402** | **7.9%** |

## What Joshua decides

1. Approve, strike or keep each numbered row, skill by skill.
2. For `post-session-recap`: cut the activation-phrase list outright, or move any phrase he cares about into the description first.
3. For `assign-lsatu-work`: whether the hosted-connector section shrinks to one line ("A hosted LSAT U MCP exists; on this laptop use the CLI"), and which authorization rule stands (3+ students confirm, or current authorization only).

When cuts are approved, apply them to every copy and record before/after byte counts in `wiki/log.md`. The copies are `skills/claude/`, `skills/codex/`, `.claude/skills/` and `.agents/skills/`; for `assign-lsatu-work`, the two home copies. Then run `python audits/skills-2026-10-12-karpathy/sync_loaded_copies.py <name>` and `sh system/scripts/check-skills.sh`.
