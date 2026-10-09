# Native Codex agent handoff and tokenizer lesson verified

Verified 2026-10-09 against the video's unchanged Prompt 4 and Prompt 6. Joshua authorized replacing Claude with Codex. The saved original commands remain unchanged.

## The original slash spelling is not a Codex command

In a fresh Codex 0.162.0-alpha.2 interactive runtime (`codex --no-daemon --no-alt-screen`), submitting `/karpathy-teach build me a tiny byte-pair tokenizer from scratch and teach me what it does` returned `Unrecognized command '/karpathy-teach'. Type "/" for a list of supported commands.` No lesson ran from that submission. The authorized Codex spelling is `$karpathy-teach` followed by the same task. This is a runtime adaptation, not identical parser behavior.

## A genuine registered agent performed the task

The native parent session is `01a12043-561e-7570-a820-839c60cc3c73`. It called `spawn_agent` with `agent_type="karpathy"`, task `tokenizer_lesson`. Child `01a12044-a1f1-7d92-867d-3054b9adde81` records `agent_role="karpathy"` and native `source.subagent.thread_spawn`. No generic worker substitution occurred. The child first read `wiki/karpathy/hot.md`, then `wiki/karpathy/rules.md`, and read only those two wiki pages. It cited source pages, applied all seven rules and ended with What I ran, What came out, What I changed.

The fresh physical [implementation](C:/Users/Joshu/dev/ai-os-projects/karpathy-method-tools/examples/native-codex-tokenizer-20261009/tokenizer.py) and [lesson](C:/Users/Joshu/dev/ai-os-projects/karpathy-method-tools/examples/native-codex-tokenizer-20261009/README.md) preserve existing examples. The code uses only Python's standard library.

## Actual execution matched the teaching predictions

Native command-completion events establish these runs, retained in [extracted evidence](NATIVE-CODEX-LESSON-EVIDENCE.json):

| Run | Actual result | Receipt |
|---|---|---|
| Initial trace-helper invocation with `python -B tokenizer.py --broken` | Exit 1 before tokenizer execution: helper did not support that argument shape. No executed-file entry. | `b17644224bd64d6da132ddc0f47857de` |
| Supported broken decoder invocation | Exit 1, `UnicodeDecodeError`, decoding the first byte of `é` independently | `961dbbeef9fc4a709824b9f12904c9a3` |
| Correct join-first decoder and BPE demo | Exit 0; eight byte IDs become `[257,257]`; unseen `abXab` becomes `[256,88,256]`; `é` restores exactly | `58fe289f1b66428e8d006c1ef2ce9c7d` |
| Behavioral checks | Exit 0; exact merges, non-overlap, nine round trips, byte preservation and boundary assertions pass | `ac477d32172f4db8b6da089ab4349315` |

[REDACTED CREDENTIAL]

## The skill needed a stricter handoff and independent review

The previous skill allowed generic/self fallback and did not explicitly require independent parent review. Its first native presentation copied the child's grades. That was weaker than Prompt 4, so it was not accepted as the final grading proof.

Activated and catalog Codex copies now require the actual registered `karpathy` agent, report registration errors rather than substituting a generic worker, inspect execution evidence, independently grade all seven rules and send applicable failures back to that same agent. Both copies have SHA-256 `07f8ac4e4b606101215665249137c956b0002908fcbeb7a2174699040d0ebf4d`.

In the same retained native session, a second review turn reread the tightened skill, inspected the implementation, lesson, all four receipts and current hash, then presented an independently graded answer. All seven rules passed with concrete evidence. The initial weaker presentation and corrected review are both preserved in the extracted evidence. No second lesson or second generic agent was used. Native runtime ended normally after both completed turns.

## Limits remain explicit

This proves native custom-agent discovery, real task handoff, the Codex skill invocation, runnable tokenizer behavior and independent parent grading. It does not prove that every future model response obeys instructions, that Joshua has answered the reconstruction exercise, or production tokenizer performance. This lesson did not deliberately trigger native child SubagentStop blocking. The separately verified main Stop acceptance remains in [hook acceptance](CODEX-STOP-ACCEPTANCE.md); child blocking remains configured and unit-tested only.
