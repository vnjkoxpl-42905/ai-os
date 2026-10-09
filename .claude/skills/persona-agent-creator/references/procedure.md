# Preserve the method while adapting the person

The video `https://www.youtube.com/watch?v=bvGptCLDhyo` explicitly names sales teachers, authors and coaches at 02:15–02:24. It describes four conceptual steps and demonstrates five numbered prompt cards plus a sixth teaching command. Original prompt cards and complete timestamped captions live in `research/karpathy-video-2026-10-08/`. Use these local sources; verify the live video when a source discrepancy matters. Captions are automatic and narration is not biographical authority.

## Stage 1: bounded collection

Use `raw/sources/<slug>-brain/raw/<source-family>/` unless an existing registered subject home owns the sources. Read scoped instructions. Define a source inventory before collection: first-party writing, lectures/interviews, public posts, repositories or user-provided documents relevant to the intended job. An author need not have GitHub repositories. Label interviewer, guest, quoted third party and uncertain authorship separately. A repository belonging to a person does not prove every line is theirs.

Preserve publication/capture dates, original URL or file identity, author/speaker, timestamps or section anchors, SHA-256, caption/manual-transcript status, truncation and media/attachment limits. Manifest each physical file with size/word count and acquisition result; record unavailable, private, deleted, blocked and deliberately excluded sources. Stop repeated rate-limited acquisition and report the gap instead of presenting retries as completeness. Do not require paid providers, evasive access or expanded browser permissions. Use available authorized routes and state coverage honestly.

Verify delivered manifests against disk, attribution and sampled content. For batch collection keep sources separate and immutable; retain failures. Collection may be complete for a specified inventory without being exhaustive public history.

## Stage 2: compiled knowledge

Use the existing `ingest` workflow; an explicit requested corpus build permits batch intake. Search existing source pages before creating another truth. Reuse an existing person's home, otherwise normally create `wiki/<slug>/` with index, log, principles, methods and hot, and source summaries under `wiki/sources/<slug>/`. Domain knowledge may belong in existing corpus/references pages with links back.

Track every manifested file as text-reviewed, payload/non-prose, duplicate, excluded or failed, with a justification. Machine-readable payload presence is not semantic understanding. Source summaries link raw evidence and hashes. Claims, interpretation and uncertainty stay distinct. Compile relationships both ways: sources support rules; rules link sources. Keep the hot page under 500 words, focused on the intended job and links to current rules. Maintain the master fenced catalog and append-only history through schema tools.

## Stage 3: evidence into behavior

For each retained rule record: stable ID, plain-language behavior, two exact attributable quotations with original artifact identities and locators, limits/counterexamples, and a practical grading criterion. Prefer evidence from different contexts; do not count syndicated copies or a transcript repeated in a blog as corroboration. Preserve dates if advice changes. A single-source candidate remains provisional.

The video targets seven rules. If fewer qualify, say how many qualified and use that honest smaller set; do not manufacture evidence. If a task needs a rule outside the person's demonstrated expertise, label our adaptation. Do not transplant Karpathy's tokenizer or debugging checklist into an unrelated person's habits.

## Stage 4: agent and entry skill

Keep a canonical agent definition in `agents/` under its existing conventions and register it for each requested runtime. Codex configuration uses `.codex/agents/<slug>.toml` with `name`, `description` and `developer_instructions`; verify the current installed discovery mechanism before claiming registration. Claude uses `.claude/agents/<slug>.md` and its own metadata. Verify the matching catalog location from existing agent examples. Do not rename Claude fields mechanically into Codex fields.

The agent needs identity limits, intended jobs, hot/rules paths, source support, task loop, applicable rules and the required endings. It should perform delegated work directly, without recursively invoking itself. Do not select or hardcode a model unless requested or required by active instructions.

The person-specific entry skill is separate from this factory. Choose `<slug>-teach`, `<slug>-review` or another precise job name rather than implying universal expertise. Save in requested runtime catalogs and activate copies, never symlinks. The entry skill must delegate to the actual registered type, wait, inspect sources/artifacts, grade each rule independently and return failures to the same agent. Non-applicable rules are explicit N/A. Preserve Joshua's own voice and instructions.

## Stage 5: relevant verification and hook scope

Inspect the existing Karpathy implementation only as a tested example. Its current `codex_stop.py` and hook matchers name `karpathy`/`karpathy-teach`; changing the agent name does not extend protection. Decide whether to add a separate adapter or a maintained person registry without disrupting the original gate. Keep scripts and dependencies outside the vault, configure only project hooks, and record supported event/tool paths. Consult current runtime documentation/local CLI guidance when changing hook APIs.

For a coding person, require current-file execution after edit, not a random successful command. A failed run is failure; subsequent edits invalidate old receipts. Require native evidence of edit-without-run blocked, genuine execution allowed, later edit invalidation and unrelated-task pass before claiming enforcement. Test child completion separately if promising a child gate. New hook definitions require the host's normal review/trust; never bypass it. Unsupported native paths remain explicitly workflow-enforced until proved.

For an author or sales teacher, code execution may be N/A. Use appropriate checks such as verifying cited examples against the archive, applying a sourced rubric to a draft, or comparing a revision with the brief. Workflow review is not a native hook. Do not install a contrived run gate just to imitate the coding demo.

## Stage 6: acceptance

State the expected behavior before the acceptance probe. Choose one representative job with an explicit success criterion, such as a cited explanation and learner reconstruction, a draft meeting a sourced author rubric, or a sales-conversation critique tied to the supplied buyer brief. Compare the observed output against that criterion; a fluent imitation alone is not a pass. For an unsupported attribution, predict that the agent will disclose the gap instead of inventing a quotation, then check what it actually returns.

Run the actual new entry skill in a fresh supported session. Retain a trace proving native agent discovery, hot-first retrieval, <=5 wiki pages, relevant evidence and independent parent grading. Test a realistic useful task plus an unsupported-claim or domain-relevant failure case. If coding, include predicted/observed output, isolated failure, repair and rerun. If reviewing, supply the actual draft and brief; never claim an unavailable client example was reproduced.

If a probe fails, isolate the cause, repair only the owning configuration/rule/skill, and repeat the failed probe plus relevant scope checks. Do not award the agent's own grades as independent proof. For non-code jobs, distinguish rubric compliance from real-world effectiveness: a reviewed sales question does not establish conversion improvement, and a draft review does not establish client acceptance.

Record test command/request, runtime/version, output and receipts, artifact paths/current hashes, rule grades, changed files and missing proof. Use an isolated test area for new application artifacts and preserve unrelated work. A partial setup is a valid reported result, not a finished agent.

Updates: `ingest` new sources, revisit corroboration and contradictions, refresh hot and configured instructions when justified, validate copies and rerun affected acceptance tests. No automatic learning, automatic source watching or recurring schedule is implied.
