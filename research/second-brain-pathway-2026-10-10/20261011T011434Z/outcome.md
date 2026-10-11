# Clip-to-knowledge pathway verification: 2026-10-10

## Result and scope

Claude and Codex project workflows agree. Student/session intake is separate from general knowledge compilation. Existing user-level knowledge entrypoints dispatch to the selected vault workflow rather than retaining a second pipeline. No new global activation, clipper automation, source intake, student-record edit, deployment, or outbound message was performed.

The route is: saved clip -> immutable archive with provenance/hashes -> attributed source summary -> existing owning topic page -> index/domain hub -> evidence-backed answer. If no topic change is warranted, explain the source-only result rather than creating duplicate pages.

## Changes

- Clarified public video captions versus student transcript intake; removed reliance on unavailable watch.
- Pending/latest-new clip selection skips operating README and retained completed sources, and resumes incomplete compilation.
- Compilation, query and lint use bounded index navigation rather than loading the 1.1 MB master catalog wholesale.
- Ingest completion includes one natural retrieval question through saved navigation to evidence-backed knowledge.
- Lint clarifies separate anchor/alias/index/semantic checks beyond the helper.
- Eleven existing user-level skill entrypoints repaired as current-vault dispatchers. Original bytes are preserved in previous-user-skills with hashes in user-entrypoint-changes.json. Two global ingest files later received concurrent execution-contract prefixes; preserved them and reverified dispatcher routing in final-user-entrypoint-state.json. No claim of exclusive control over other active processes.

## Observed verification

- Full project check-skills.py: PASS, Claude224/Codex209 catalog skills, activation routes resolve, index complete.
- Claude/Codex active/catalog byte equality: ingest entrypoint, compilation reference, query, lint and transcript-intake all pass.
- Native fresh Claude read-only acceptance: success, no permission denials. Session used Skill(ingest), Read, Glob and Grep. No writes or live API tools exposed. Actual tool names retained in claude-tool-checks.json and result in claude-acceptance2.json. First launch had invalid empty MCP JSON/argument separation; corrected to mcpServers:{} plus end-of-options separator before retry. Only the successful run supports native acceptance.
- Native Claude routing: AI article -> ingest; public video missing captions -> knowledge acquisition with coverage limits; student transcript lookup -> narrow transcript-intake. No missing skill/read reported.
- Native Claude retrieval: found saved JavaScript-video source through bounded index search, read compiled source and owning topic, returned useful advice while preserving source claims and untested qualifications.
- Parent independently verified both archived clip and provenance hashes against SHA256SUMS. Inbox/archive bytes differ only CRLF/LF; archive remains unchanged. Normalized equality is not a replacement for exact hash identity, and no source was rewritten or silently re-ingested.
- Structural lint:3892 wiki pages,2 broken historical log references: ../raw/README.md and ../references/ai-workspace/expert-teaching-workflow.md. Report remains system/generated/wiki-lint.generated.tsv. These were already observed before this pathway work and are not fixed here.
- Independent Karpathy and skill-writing reviews found corrected routes sound. One existing source/topic example proves bounded retrieval, not whole-vault completeness.

## A real usability example

Question: What did the saved Claude JavaScript video suggest I could reuse in my video workflow?

Saved answer: Preview storyboard frames before coding; specify duration, aspect ratio and audio; review a contact sheet, fix frames and render again. The creator describes a time-to-picture JavaScript function rendered in a browser and assembled with FFmpeg. These are saved creator claims, not a locally tested video pipeline. The clip omits the distributed skill's identity and leaves comparative quality/tool installation unverified.

Route: references/ai-workspace/index.md -> wiki/VIDEO-GENERATION-OPTIONS-2026-09-09.md Added2026-10-10 -> wiki/sources/claude-now-does-video-free-javascript.md -> archived provenance/hashes.

## Independent parent grading of seven method rules

| Rule | Grade | Observed evidence |
|---|---|---|
| Mechanism reconstruction | Pass | Traced capture, archive, compilation, navigation and cited answer |
| Small baseline | Pass | One already-saved source and owning topic, not a bulk intake |
| Prediction/run/comparison | Pass | Predicted saved evidence-backed retrieval; native Claude returned it |
| Counterexample/fix | Pass | Missing watch/public-video ambiguity and completed-newest selection corrected; independent readback passed |
| Relevant execution | Pass | Native Skill(ingest) and bounded compiled-page retrieval, file hashes and structural checks |
| Explicit assumptions | Pass | Exact-byte difference, source claims, limited scope and acquisition/runtime limits recorded |
| Justified simplicity | Pass | Existing vault/schema/index/topic homes; existing global entrypoints dispatch, no second pipeline |

## Limits and remaining checks

Browser Web Clipper's currently selected vault/template was not inspected. Existing files demonstrate captures in raw/inbox; they do not certify every browser template. Saving a clip does not automatically run ingestion. Ask to ingest it, then ask later questions through query. No fresh-source mutation test, actual public caption acquisition, or live Calendar/Drive reconciliation occurred. Standalone quick_validate.py could not run because available Python runtimes lacked PyYAML; project validation and native Claude skill parsing/activation passed instead. No installations were made for that auxiliary checker. Cloud publication and other devices are not certified by local checks.

## What I ran

Registered Karpathy review, independent skill review, project validator, structural lint, exact source/hash checks, current-vault dispatcher checks, and a native Claude read-only skill/retrieval run.

## What came out

Verified paired project configuration, corrected fallback routes, and one concrete reusable saved answer. Two pre-existing historical links remain unresolved.

## What I changed

Knowledge skills and matching project/catalog resources; eleven existing user-level dispatchers with preserved snapshots; operating schema and parity notes; the existing architecture reference and system log; generated structural lint. Source bytes and student records unchanged.
