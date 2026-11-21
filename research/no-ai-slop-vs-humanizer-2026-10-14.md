---
title: no-ai-slop vs humanizer on one approved email
type: research
created: 2026-10-14
status: awaiting-decision
source_queue_item: AQ-005 (references/ai-workspace/action-queue.md)
---

# no-ai-slop vs humanizer on one approved email

Run 2026-10-14 for queue item AQ-005. Nothing was sent. Nothing was cataloged or activated. The edits were made on scratch copies in `C:\Users\Joshu\AppData\Local\Temp\claude\no-ai-slop\compare\`.

## What was tested

- **no-ai-slop:** `petergyang/no-ai-slop`, fetched with `gh repo clone --depth 1` into a new empty folder, `C:\Users\Joshu\AppData\Local\Temp\claude\no-ai-slop\repo`. Commit `000650b156983f5159695b441477f4e63b25dc85` (2026-09-01). The skill is two Markdown files: `skills/no-ai-slop/SKILL.md` (10,853 bytes) and `eval.md`. It has no scripts. The repo's only script is `scripts/build_plugin.py`, a packaging helper. I did not run it.
- **SkillSpector** v2.12.0, `scan --no-llm`. The skill folder scored 0/100, LOW, SAFE, with no issues. The whole repo scored 20/100, LOW, SAFE, with three MEDIUM issues outside the skill: an unpinned `npx skills` line in the README, a skill-enumeration line in the README, and the same in `build_plugin.py`. Order of steps: `skillspector` was not on the Git Bash PATH when I first looked, so I read `SKILL.md` before scanning. It later turned up at `C:\Users\Joshu\.local\bin\skillspector.exe` and the scan ran then. Reading the file was low risk because it is plain text, but the queue's order (scan first) was not kept.
- **humanizer:** the active project copy, `.claude/skills/humanizer/SKILL.md` (v3.1.0).
- **Method:** two fresh subagents on the same model. Each read only its own skill and the draft. Neither read the voice guide. Each got the same context line, which described the email as going to a student "whose weekend session he missed". That wording was mine, and it went further than the draft does (see the scoring notes).

## The draft

The draft is a real email that Joshua approved. It is in `wiki/send-ledger.md` line 91 (fernande-charleus, "Sorry for the scheduling mix-up", sent 2026-10-12, Gmail message `1a13204c4ee9d0ae`). The text was read back from Gmail.

```
Subject: Sorry for the scheduling mix-up

Hi Fernande,

I'm sorry about this weekend. I'm not sure when you scheduled this session, and I believed I had this weekend blocked off. That's a mistake on my side, and I apologize for the confusion.

Please let me know a time that works best for you, and I'll make it right.

Joshua
```

## humanizer output

```
Subject: Sorry for the scheduling mix-up

Hi Fernande,

I'm sorry about this weekend. I thought I had it blocked off, and I'm not sure when you scheduled the session. That mistake is mine.

Let me know a time that works best for you, and I'll make it right.

Joshua
```

humanizer acted on none of its 26 numbered patterns. It cut the second apology under its general rule that every sentence must add something. It looked at "let me know" (§22, chatbot residue) and kept it under "When not to act", because letter sign-offs predate chatbots.

## no-ai-slop output

```
Subject: Sorry I missed our session this weekend

Hi Fernande,

I'm sorry I missed our session this weekend. I believed I had the weekend blocked off, and that's a mistake on my side.

Please reply with a time that works best for you, and I'll make it right.

Joshua
```

no-ai-slop's What changed section listed four edits. It made the subject say he missed the session. It cut "I'm not sure when you scheduled this session" because that line hints the student caused it. It cut "I apologize for the confusion". It changed "let me know" to "reply with". It passed every check in its own `eval.md`.

## Scores

The rules come from the `CLAUDE.md` Voice section and `wiki/teaching-voice.md`: core voice, signature phrases, and "The apology / accountability move".

| Check | Original | humanizer | no-ai-slop |
|---|---|---|---|
| Em dashes | 0 | 0 | 0 |
| Banned or slop words | 0 | 0 | 0 |
| Meaning kept, nothing added | n/a | Yes. All facts kept, two lines reordered | **No.** "Missed our session" is new. It came from my context line, not the draft. The draft only says "sorry about this weekend". The "not sure when you scheduled" fact is gone |
| Apology owned in the first line | Yes | Yes | Yes, and the most direct |
| Gentle about the person, no blame | Mild risk: "not sure when you scheduled" | Same risk, line kept | Yes. The line that hints at blame is cut |
| His signature phrase "let me know" (about 390 uses in his corpus) | Kept | Kept, but "Please" dropped | **Lost.** Became "reply with" |
| His wording kept | n/a | Mostly. "a mistake on my side" became "That mistake is mine" | Mostly. "a mistake on my side" kept. Subject rewritten |
| Proportional edit | n/a | Light: 3 small changes | Heavier: 4 changes, including the subject |
| **Overall** | Baseline | **Closest to Joshua.** Safe and light, with two small losses ("Please", "on my side") | **Better ownership, worse fidelity.** It added a claim and replaced his most characteristic phrase |

## Verdict

On this draft, no-ai-slop did not catch an AI tell that humanizer missed. Neither tool found a real AI pattern, and that fits, because Joshua wrote and approved the email. The only real difference is editorial judgment. no-ai-slop made one good call: it cut the line that half-blames the student, which fits "honest about the work, gentle about the person". It also made two calls that break the vault's rules. It added a fact that is not in the draft, and it removed his most-used phrase. humanizer's strict "add nothing" rule held even with the same leading context line.

**Recommendation: do not adopt no-ai-slop as a second editor.** It duplicates about 80 percent of humanizer's pattern list. Its "minimum effective edit" principle is good, but in practice it rewrote more than humanizer did. Two ideas are worth borrowing into humanizer or the voice guide if Joshua wants them, without adding a second skill:

1. **Detect mode.** Name each pattern, quote the line, give the fix, and do not rewrite. This is useful for reviewing a draft before Joshua approves it.
2. **The portability test.** If a sentence could move unchanged to another person or product, it is filler. This is a quick check for marketing copy.

Separately, humanizer's §22 lists "let me know" as chatbot residue. The model kept it this time, but only through the exception clause. A one-line note that "let me know" is Joshua's signature phrase would remove the risk.

## Limits of this test

- One draft, one run per editor. The draft is short (55 words) and human-written, so the test measures overreach, not detection. A fair detection test would use an AI-written draft from the `morning-brief` or `consultation-inquiry-drafts` output before Joshua edits it.
- My context line said "missed", which is stronger than the draft. That shows how easily no-ai-slop turns context into new claims, but the error started in the prompt, not the skill alone.
- Both editors ran without `wiki/teaching-voice.md`. With the voice guide loaded, both would probably keep "let me know".
