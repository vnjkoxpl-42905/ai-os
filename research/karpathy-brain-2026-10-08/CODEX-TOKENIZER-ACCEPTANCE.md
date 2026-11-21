# Codex tokenizer lesson executed with current-file receipts

Date: 2026-10-08. Task: `build me a tiny byte-pair tokenizer from scratch and teach me what it does`.

Joshua authorized adapting the video's Claude workflow to Codex. A dispatched Codex worker followed the saved `karpathy-teach` skill and `agents/codex/karpathy.toml` instructions directly. This did not exercise native custom-agent registration, a native skill slash-command parser, or native stop-hook blocking. The first tool action read `wiki/karpathy/hot.md` then `wiki/karpathy/rules.md`, before any code. Only those two wiki pages were read, below the five-page limit. Source links in the lesson were obtained from the rules page.

## Actual chronological execution

1. Created a fresh standard-library tokenizer, tests and written predictions in [codex-tokenizer](C:/Users/Joshu/dev/ai-os-projects/karpathy-method-tools/examples/codex-tokenizer/LESSON.md), without modifying the previous demonstration. The initial decoder deliberately decoded each token independently.
2. Ran the seven tests through the execution receipt helper. Receipt **`8e2c799cd2e94411bc2e703370e1dc23`**, exit **1**. Observed one baseline assertion failure and three Unicode errors. The Unicode errors were expected; the baseline assertion revealed a real mistaken hand prediction about the lexicographic tie rule.
3. Preserved the original prediction and appended the cause and corrected prediction before rerunning. Corrected the test expectation to the declared tie rule, rather than altering the algorithm to fit a wrong prediction. Repaired the decoder to join bytes before UTF-8 decoding.
4. Reran the identical seven test methods, with the corrected baseline expectation. Receipt **`71cc7c27c8b64f31a6832f14b03aa31a`**, exit **0**, **7/7 passed**. This receipt covers the current `bpe.py` and `test_bpe.py` hashes.
5. Ran the fresh demonstration. Receipt **`cc4f17be32804aa39683cdde5ae794f5`**, exit **0**. It covers the current `bpe.py` and `demo.py` hashes. The demo completed while the corrected test receipt was still being collected; both are successful post-fix executions.

Successful receipt hashes were compared with the physical current files after all code edits and matched. The failed receipt deliberately retains the previous file hashes. Copied receipts, current-hash comparisons and exact command arrays are in [RUN-RECEIPTS.json](C:/Users/Joshu/dev/ai-os-projects/karpathy-method-tools/examples/codex-tokenizer/RUN-RECEIPTS.json).

## Observed output

```text
Text: aaabdaaabac
Byte baseline: [97, 97, 97, 98, 100, 97, 97, 97, 98, 97, 99]
Merge: (97, 97) -> 256 = b'aa'
Merge: (97, 98) -> 257 = b'ab'
Merge: (256, 257) -> 258 = b'aaab'
Tokens: [258, 100, 258, 97, 99]
Round trip: aaabdaaabac
Token counts: 11 -> 5
Unicode round trip: hello 🌍
```

The tests check exact learned merges and tokens; unmerged `é`; unseen ASCII, emoji, combining accent, null/newline and empty text; nonoverlapping replacement; reset and early stop; invalid merge counts; and invalid token IDs. Seven test methods include multiple round-trip subcases. This is local behavioral acceptance of a teaching toy, not production performance, arbitrary adversarial input, model training or live application acceptance.

## Reproduce the corrected run

Run from `C:/Users/Joshu/dev/ai-os-projects/karpathy-method-tools/examples/codex-tokenizer`:

```powershell
& 'C:/Users/Joshu/AppData/Local/Programs/Python/Python312/python.exe' ../../run_gate.py --run --file bpe.py --file test_bpe.py --cwd . -- 'C:/Users/Joshu/AppData/Local/Programs/Python/Python312/python.exe' test_bpe.py
& 'C:/Users/Joshu/AppData/Local/Programs/Python/Python312/python.exe' ../../run_gate.py --run --file bpe.py --file demo.py --cwd . -- 'C:/Users/Joshu/AppData/Local/Programs/Python/Python312/python.exe' demo.py
```

The helper traces executed Python files rather than counting an unrelated successful shell command. It supplies receipts; this worker did not verify a Codex native stop hook. The root's separately prepared hook adapter requires its own native acceptance evidence.

## Grade against all seven rules

| Rule | Grade | Evidence |
|---|---|---|
| Reconstruct the mechanism | Pass | Byte baseline, merge table, decode explanation and learner expansion question |
| Small correct baseline | Pass | One short training string and exact five-token expectation |
| Predict, run, compare | Pass | Initial predictions retained, actual unexpected tie failure investigated, corrected prediction before rerun |
| Counterexample and cause repair | Pass | UTF-8 split-character errors reproduced, join-then-decode repair rerun |
| Relevant verification | Pass | Seven behavioral test methods and traced hashes for every current Python file |
| Explicit assumptions | Pass | UTF-8, deterministic ties, no special tokens/normalization, teaching and native-runtime limits disclosed |
| Justified simplicity | Pass | Standard library only, 49-line core, no services or packages |

Source support and historical exceptions remain in [seven rules](../../wiki/karpathy/rules.md); the full [lesson](C:/Users/Joshu/dev/ai-os-projects/karpathy-method-tools/examples/codex-tokenizer/LESSON.md) cites the underlying evidence pages and ends in the required order.

## What I ran

The broken test suite, corrected test suite and demonstration through `run_gate.py`. Actual failed and successful receipts retained.

## What came out

Initial exit 1 exposed Unicode decoding failure and a mistaken tie prediction. After cause repair and corrected expectation, 7/7 test methods pass, 11 bytes become five tokens, and ASCII and Unicode round trips restore exactly.

## What I changed

Created a fresh external `examples/codex-tokenizer/` teaching artifact and this acceptance record. No raw sources, current root configuration, existing tokenizer demonstration or status files were edited by this worker.
