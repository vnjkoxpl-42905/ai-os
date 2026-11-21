# Gemini runner repair verification

2026-10-29. Approved plan scope: Gemini trajectory post-run audit repair only. This is fresh local verification by the implementing agent, not an independent provider code-review verdict. No live provider calls, app edits, global skill edits or commits/pushes in this verification.

## Source finding and repair

The former audit checked only current step.type strings for uppercase RUN_COMMAND/WRITE/REPLACE/EDIT/CREATE/DELETE/SUBAGENT substrings. The declared forbidden set also contained send_message/schedule/ask_question, which this predicate did not cover. Nested planner/tool/function invocation names were not checked. This is a source-established naming/schema coverage gap, not proof a historical run exploited it.

The repaired audit normalizes camel/Pascal/snake/kebab names, handles namespaces and step prefixes, includes write_file/manage_task/call_mcp_tool, checks concrete step types and root execution payloads, and traverses invocation-bearing plannerResponse/toolCalls/toolCall/functionCall/function wrappers with camel/snake keys. It avoids scanning metadata/tool inventories/config/arguments/results/prose as if they were actual calls. Builds bypass the read-only rejection; resumed earlier steps remain excluded.

## Fresh checks

From C:/Users/Joshu/dev/ai-os:

```powershell
python -X utf8 -m unittest discover -s .agents/skills/geminex-loop/scripts -p test_runner_audit.py -v
```

Result:9 unittest methods PASS, exit0, fresh authoritative run. The same9-method suite previously passed independently from each of the four owning directories; those are repeated tests, not36 distinct cases. Subtests cover every forbidden category in enum/name spellings, camel/snake nested structural wrappers, direct payloads, legacy mutating enum aliases, allowed read-only calls and metadata/argument/result/prose false positives. Mocked execute_gemini_turn verifies rejection before reply.txt acceptance while stdout diagnostics are retained, prior-turn exclusion and build bypass. No network is used by this suite.

Fresh Python verification additionally ran py_compile.compile(...,doraise=True) on runner.py and test_runner_audit.py in all4 copies, and compared hashlib.sha256(path.read_bytes()) for all three files in all4 copies. All compile/parity checks PASS. Runtime/catalog roots are .agents/skills, .gemini/skills, skills/codex and skills/gemini, each under geminex-loop. No globals mirrored.

| Relative file | SHA-256 | Parity |
| --- | --- | --- |
| `scripts/runner.py` | `5939fe75a6b0561747e43a8fcdeb8e21d5affc3fc81b41c690408bd7b82e7891` | 4/4 |
| `scripts/test_runner_audit.py` | `3164b9a2c9e543e68435261a6620e94fd57076627dc88d22a591870f0a2b2dfd` | 4/4 |
| `references/runtime.md` | `c7791f9b5e2040920f61178789822d07b4970bb2b45f81d6f5b4bc7c45f68d74` | 4/4 |

## Explicit demonstration fixtures

These are clearly labeled synthetic fixtures, not recovered tool calls or an exploit claim:

- Fixture `{"type":"CORTEX_STEP_TYPE_SEND_MESSAGE"}`: former substring predicate did not reject; repaired audit rejects.
- Fixture `{"type":"CORTEX_STEP_TYPE_PLANNER_RESPONSE","plannerResponse":{"toolCalls":[{"functionCall":{"name":"askQuestion"}}]}}`: former substring predicate did not reject; repaired audit rejects.

The unittest suite separately confirms a metadata tool inventory containing these names does not cause rejection.

## Historical evidence boundary

No verified historical offending camelCase invocation was available. A bounded read of recent saved trajectories and the known2026-10-27 recovered trajectory did not establish one. Metadata did contain forbidden tool definitions, reinforcing why generic recursive name matching would be wrong. No historical approval was relabeled or overwritten.

Historical approved-plan record read without modification: `C:/Users/Joshu/AppData/Local/Temp/geminex-gnqvlnb1/result.json`.

Original record status `completed`, verdict `APPROVED`; SHA-256 before/after `7a0c615e3a1725f704dabd9af3c15970bfa0a72097b6c1107fc7689495c074e5` unchanged.


## Limits

This is POST-RUN DETECTION AND RESULT REJECTION, NOT PREVENTIVE SANDBOXING. A forbidden effect can occur before the runner retrieves the trajectory and rejects the reply. Unknown future execution schemas need explicit audit support. The audit does not prevent side effects inside a tool falsely presented as a read-only name. Offline fixtures verify recorded-shape handling; they do not establish live Antigravity transport behavior or full system confinement. Parent should bind final independent Gemini inspection to the exact file hashes above and preserve that review's own coverage/limitations.
