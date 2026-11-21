---
type: research
subject: What Joshua sent back in the last 30 days, grouped by skill, with one-line fixes (AQ-012)
created: 2026-10-14
window: 2026-09-14 to 2026-10-14
queue_item: AQ-012
status: proposals only; no skill edited
---

# Send-backs, 2026-09-14 to 2026-10-14: four repeat patterns worth a one-line fix

## How this was read

- **Sources:** 133 Claude Code sessions in `~/.claude/projects/C--Users-Joshu-dev-ai-os/` and 263 Codex sessions in `~/.codex/sessions/`, all modified on or after 2026-09-14. Only Joshua's own turns were read. Pasted handoffs, system text, sub-agent turns and this session were skipped.
- **Two passes.** The first was a keyword pass ("no", "I said", "wrong", "try again", "you didn't", "still not", "instead of", and similar). The second was a pass over short turns (under 220 characters) that start with a correction verb, read next to the assistant message they answered.
- **Hand check.** The passes flagged 215 turns. I read each one and kept only real send-backs, meaning rejected or redone output. New feature requests that used "should" were dropped, along with grill answers, Joshua's own dictation slips, and usage-limit retries.
- **Duplicates.** Many Codex threads are forks or imports that replay the same user turns (the Fernande email session appears in both runtimes, for example). Each send-back is counted once.
- **Skill attribution.** Each turn was tagged with the last skill invoked in that session. That tag is sticky, so a long `grill-me` session tags later lesson edits too. I corrected the group by reading the context. Treat the skill named in each group as the owner of the behavior, not always the skill that was running.
- No credentials, tokens or student email addresses are copied here. Quotes are shortened and paraphrased from dictation.

Result: **36 real send-backs**. Six groups have two or more; four of those are candidates for a one-line fix.

## Groups seen twice or more

### 1. Dictated logistics emails come back with lines he did not say: 8 send-backs, no skill running

| Date | Session | What he sent back |
|---|---|---|
| 2026-10-12 | Claude `a1b94b7a` (also replayed in Codex `01a13430`) | "don't say that's on me" and "make it more human" |
| 2026-10-12 | `a1b94b7a` | "slightly longer, apologize for the slight delay, I believe I had this weekend off" |
| 2026-10-12 | `a1b94b7a` | three rewrites in a row of one sentence, ending at "say I'm not sure when you scheduled this day" |
| 2026-10-12 | `a1b94b7a` | Celia reschedule: "'work best for me' is awkward, try again", then "say more warmly", then "not 'hope you're doing well'" |

**Pattern:** each draft added lines he never dictated ("That's on me", "I know a delay like that is frustrating", "I'll make it right", "I hope you're doing well") or paraphrased the reason he gave. Each fix was to restore his wording.

**Proposed fix,** for the logistics register of `wiki/teaching-voice.md`, the voice source that `inbound-tutoring-replies`, `morning-brief` and the consultation skills route through:

```
When Joshua dictates an email, keep his stated reason in his own words and add nothing he did not say beyond the greeting, one apology line and the sign-off: no empathy lines, no "I hope you're doing well", no promises such as "I'll make it right".
```

Note: the apology move in `wiki/teaching-voice.md` (step 1) currently models "The error was on my end, not yours." On 2026-10-12 he struck "That's on me" from a draft. Joshua should confirm whether ownership lines stay in the template.

### 2. Lesson and bootcamp copy: 12 send-backs across `post-session-recap`, `lsat-u-voice` and bootcamp work

| Date | Session | What he sent back |
|---|---|---|
| 2026-09-28 | Codex `01a0e942` (session-recap) | "it should be my voice", awkward wording, an inaccurate characterization |
| 2026-09-29 | Codex `01a0e942` | practice questions reused "the same example that we had in the image above"; "should be another example" |
| 2026-10-11 | Claude `d1b2fc2f` | "'has to be true for it.' Has to be true for what?" |
| 2026-10-11 | `d1b2fc2f` | words blocked out separately; "I shouldn't say 'signal rule'" |
| 2026-10-12 | Claude `6f1c3429` | "don't mention logic games"; "don't use the air example, but use the same idea", a parallel to the coffee example |
| 2026-10-12 | `6f1c3429` | "don't have the flashcards in the lesson, detach them" |
| 2026-10-12 | Claude `1438185e` | "use one example; the second should be a random, simple, intuitive idea"; "not just letters, condensed versions of the statements" |
| 2026-10-12 | Claude `a4c18d6b` (twice) | "it's not defining what sufficient condition is enough to a point where it's very clear" |
| 2026-10-13 | Claude `68735b21` | "not make the acronym ... make this clear" |
| 2026-10-13 | Claude `e73e83bf` | note and drill "structure doesn't really make sense" |

**Already captured:** "has to be true for it" and "signal the rule" are in `wiki/COPY-CORRECTIONS.md` (2026-10-11). The Logic Games ban, original examples, and the contrapositive gold standard are saved as memories.

**Two repeats still not covered by a skill line:**

- *Practice reuses the worked example* (2026-09-29 and 2026-10-12). Proposed line for `lsat-u-voice`, which `post-session-recap` and bootcamp work both read:

```
A practice question never reuses the example the lesson just worked; give it a new everyday scenario so the student has to apply the idea, not recall the answer.
```

- *A core term is used before it is plainly defined* (2026-10-11 and 2026-10-12, twice). Proposed line for `lsat-u-voice`:

```
Define each core term in one plain sentence the first time it appears, before any example or label depends on it.
```

### 3. Interview questions he could not parse: 5 send-backs across `grill-me`, `grilling` and `wait-what`

| Date | Session | What he sent back |
|---|---|---|
| 2026-09-22 | Claude `34599f1f` | "What are the 13 switches?" |
| 2026-09-23 | Claude `98b8acde` | "I don't know what the main card is." |
| 2026-09-27 | Claude `d175f546` | "What do you mean by the two spelling?" |
| 2026-10-14 | Claude `8e78326c` | "I'm not sure what you mean by question 11." |
| 2026-10-14 | `8e78326c` | "Confused by why level up is something separate ... what does level up have to do with this?" |

**Proposed fix** for `grill-me` (and its sibling `grilling`, both runtimes):

```
Word each question in Joshua's terms: name the screen, file or skill he would recognize, and define in one clause any term he has not used himself.
```

### 4. LSAT U work done through a browser or Lovable instead of headlessly: 5 send-backs across `assign-lsatu-work`, `lsat-u-platform-actions` and `wrapup`

| Date | Session | What he sent back |
|---|---|---|
| 2026-09-23 | Claude `429c79e5` | "It shouldn't have to open a browser tab ... It should really do it headless." |
| 2026-09-23 | `429c79e5` | "It shouldn't cost any Lovable credits. Why is it costing Lovable credit?" |
| 2026-09-30 | Codex `01a0e942` (assign-lsatu-work) | Codex said bash was not on PATH and went to find another route. He replied: "fix it, never should be headless and automatic". |
| 2026-09-30 | `01a0e942` (lsat-u-platform-actions) | "this should also be done headless" |
| 2026-09-30 | `01a0e942` (wrapup) | "You should have posted to their page without going to Lovable." |

**Mostly fixed already:** both skills now say no browser and no Lovable, and no repeat was found after 2026-09-30. The one open gap is the missing-bash case on Codex. The catalog pointer (`skills/claude/assign-lsatu-work/SKILL.md`) says only "with bash". Proposed line for that pointer and the loaded home copy:

```
If `bash` is not on PATH, run the same command through Git Bash (`"C:\Program Files\Git\bin\bash.exe" system/scripts/lsatu ...`); never fall back to a browser or Lovable.
```

The Git Bash path exists on this laptop (checked 2026-10-14).

### 5. Codex re-planning or delegating instead of building: 2 send-backs, one session

| Date | Session | What he sent back |
|---|---|---|
| 2026-10-09 | Codex `01a11839` (code-review tag) | "Did you make the plan yet? ... you should be mindlessly executing the task" |
| 2026-10-09 | `01a11839` | "instead of assigning it to delegate another chat, I want you to actually finish the job" |

Both came from one session, so this is weaker evidence. A proposed line for the builder role in `claudex-loop` and `codex-build`: "As builder, carry the work order to completion yourself; do not re-plan it or hand it to another chat unless the order says to." **I recommend waiting for a second session before adding this.**

### 6. Usage-limit retries: 6 cases of "Try again", no fix

On 2026-10-02, 10-09, 10-11 and 10-13, "Try again" followed a session-limit message, not bad output. No skill change applies.

## Seen once (no fix proposed)

- 2026-10-12 Claude `a4c18d6b`: "no, push it to main" after the agent refused. This conflicts with the branch-per-session memory. One case only; Joshua may want an exception written into that memory for when he explicitly says "push to main".
- 2026-10-08 Codex `01a11ac2`: a tool list included things already installed. "Don't include things I already have installed."
- 2026-10-13 Codex `01a133fc`: a handoff prompt mentioned env files he did not want brought up.
- 2026-10-13 Codex `01a133fc` (superwhisper): "No, it's not open."
- Dictation slips, not agent errors: "five cards" for "flash cards" (2026-10-11), and "two is a typo" (2026-10-08). "five cards" is a Superwhisper replacement candidate.

## What Joshua decides

1. Approve, edit or reject each proposed line: group 1 (teaching voice), group 2 (two `lsat-u-voice` lines), group 3 (`grill-me`/`grilling`), group 4 (`assign-lsatu-work` bash fallback), group 5 (hold or add).
2. Confirm whether "That's on me" style ownership stays in the apology template.
3. Whether "push to main" on his explicit word overrides the branch-per-session rule.

Approved lines go into every copy (`skills/claude/`, `skills/codex/`, `.claude/skills/`, `.agents/skills/`, plus the home copy via `sync_loaded_copies.py`). Copy-related ones also get logged in `wiki/COPY-CORRECTIONS.md`. Then run `sh system/scripts/check-skills.sh`.
