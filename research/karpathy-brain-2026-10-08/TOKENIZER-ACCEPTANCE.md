# The tokenizer lesson ran through the installed skill and agent

Verified 2026-10-08 using authenticated Claude Pro CLI 2.1.293. The execution stream records karpathy-teach followed by the karpathy subagent. No new paid API service was configured.

[Lesson](C:/Users/Joshu/dev/ai-os-projects/karpathy-method-tools/examples/tokenizer/LESSON.md), [implementation](C:/Users/Joshu/dev/ai-os-projects/karpathy-method-tools/examples/tokenizer/bpe.py), [tests](C:/Users/Joshu/dev/ai-os-projects/karpathy-method-tools/examples/tokenizer/main.py), [broken decoder](C:/Users/Joshu/dev/ai-os-projects/karpathy-method-tools/examples/tokenizer/broken_decoder.py), and [raw execution](C:/Users/Joshu/dev/ai-os-projects/karpathy-method-tools/lesson-runtime.jsonl) remain outside the vault.

## Observed results

- Baseline aaabdaaabac: eleven bytes become five tokens [258, 100, 258, 97, 99] after three merges and decode exactly.
- Correct decoder: 8/8 round trips pass, including Unicode, joining bytes before UTF-8 decoding.
- Broken per-token decoder: 5/8 fail. Replacing invalid pieces hides errors rather than repairing them.
- Initial helper execution exposed Windows cp1252 output failure. Parent output and Python child processes now use UTF-8. A final rerun passed without an environment workaround; receipt b0a37346d29b4221b4e077cdb1e50f91.
- Twenty gate tests pass, including stale hashes, forged inline receipts, failed runs, registered-workspace shell edits and Unicode output. The live native hook state closed successfully. Live acceptance tested successful completion; blocked-stop behavior is covered by behavioral tests.

## Grade against the rules

| Rule | Evidence and limits |
|---|---|
| Reconstruct mechanism | Explicit bytes, pairs, merge ranks and decoding. |
| Start small | Standard-library toy baseline and Unicode cases. |
| Predict/run/compare | Exact expected and actual tokens. Lesson now folds the answer under a prediction prompt; no recorded learner answer. |
| Failure/repair | Broken decoder fails five cases; joined bytes pass eight. Fixed code already existed during comparison, so no chronological learner edit is claimed. |
| Relevant proof | Current-file receipts and eight round trips, not exhaustive correctness. |
| Assumptions | Educational BPE, deterministic merges, UTF-8, limited inputs. |
| Simplicity | Pure Python, no model download or dependency; production tokenizer outside scope. |

The CLI's earlier helper-fix request is superseded by the verified parent repair. Its broad untouched-files statement is not integrity proof. Full-corpus compilation remains incomplete.
