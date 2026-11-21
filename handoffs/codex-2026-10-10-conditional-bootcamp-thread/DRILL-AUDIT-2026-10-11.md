# Conditional bootcamp drill audit (2026-10-11)

Scope: all 13 drills on the opening course path, plus the lessons that come before each one. Three read-only reviewers covered the drills in parallel; Claude re-checked the High findings against the source. Branch `claude/conditional-bootcamp-drills-2026-10-11` (PR vnjkoxpl-42905/lsatu-684d89db#204).

Already fixed during the audit: Drill 7 item 07 read "exceeding the groups" because Claude's word sweep had changed "targets". Restored, and that was the only damaged item.

## Across many drills

| # | Sev | Problem | Fix |
|---|---|---|---|
| X1 | High | **Wrong answers reveal the answer** in Spot the condition (correct option ticked + "The correct answer is marked above"), worksheet Drills 2 to 8 ("Indicators: …" key, full diagram), and mixed practice (diagram direction, full readback). | On a wrong answer, show a hint only. Reveal after a correct answer, or after a second miss. |
| X2 | High | **when, whenever, where and each are tested but never taught on the path.** The Group 1 word lesson (`IndicatorNote group-1`, reference section 3) exists but is not routed. | Show the Group 1 word lesson inside "Find the complete condition". |
| X3 | High | **"only after"** is tested (Drill 2 #07, Drill 5 #07, Revisit 5 #07) and never taught. | Add it to "Necessary-condition words", or rewrite the items with "only if". |
| X4 | High | **The contrapositive drills give no feedback until the end** (Revisit 5, Revisit 6, Drill 7, Drill 8: up to 7 unchecked steps per sentence). | Show the comparison after the diagram step and after the contrapositive step. |
| X5 | High | **"who" is graded inconsistently.** Required on its own in Drill 2 #08 ("Members who"), marked wrong in #05 and #13 and in Drill 3. The lessons teach "people who". | Accept "who"/"[group] who" wherever it introduces the condition. |
| X6 | Medium | **Internal editing notes are shown to students** under "Source adaptation" ("The source key conflicts…", "needs clarification before grading", "Reviewed derivative…"). | Hide them, or rewrite them for students. |
| X7 | Medium | **51 contrapositives start "If that …"** with nothing for "that" to point to ("If that person is not required…"). | Lead with "a/no": "If a person is not required…, then that person is not a manager." |
| X8 | Medium | **Exact-phrase indicator matching**: "Only those" (Drill 6 #03, #08, #16) fails a student who selects "Only", the word that was taught. | Key the item as "Only", or accept either. |
| X9 | Medium | **Words already on the banned list are still in the worksheet copy**: "the model"/"a model" (Drill 7 and Drill 8 instructions, engine line 131), "Preserve…", "classify each expression", "statements" (Revisit 5 instructions). | Apply the list. Claude skipped this file earlier to protect source text, so only the student-facing fields need changing. |

## Order and flow on the path

| # | Sev | Problem | Fix |
|---|---|---|---|
| P1 | High | **Drill 3 (find the indicators) is Drill 2's first step on its own**, and comes after Drill 2. Easier follows harder. | Move Drill 3 before Drill 2, or fold it in. Renumbers the drills. |
| P2 | Medium | **Drill 4 reuses Drill 3's sentences.** Placement is a two-button choice showing the key's wording, so there is little challenge. | Use fresh sentences, or have students place their own wording. |
| P3 | Medium | **Drill 5 repeats Drill 2's 15 sentences and redoes the conditions step.** Nothing is auto-checked. | Carry over the Drill 2 conditions, and add one checked direction step. |
| P4 | Medium | **Revisit drills redo conditions and symbols**; Drill 8 is 35 sentences × 8 steps (280 steps). | Prefill from the first pass; split Drill 8 into three sets. |
| P5 | Medium | **"Check your contrapositive" (multiple choice) comes after the harder free-writing Revisits.** | Move it right after the contrapositive lesson. |
| P6 | Medium | **Spot the condition goes backwards in difficulty.** It ends with 7 easy "rule vs fact" questions after "only if"/"requires". | Put the rule-vs-fact questions right after the concept questions. |
| P7 | Medium | **"Build the sufficient side" is 24 sentences × 4 steps**, the indicator step always offers "only if"/"requires" as distractors (students learn to eliminate), and 5 sentences are copied from the lesson (the report sentence appears twice). | Cut to about 10 fresh sentences, one per indicator, and vary the distractors. |
| P8 | Medium | **Drill 6 has the student write the if/then before finding the indicator.** | Indicator, then rewrite, then diagram. |

## Individual items

| Drill | Item | Sev | Problem → fix |
|---|---|---|---|
| Spot the condition | concept Qs | Medium | "trigger" and "required outcome" are only defined inside the questions → use sufficient/necessary. |
| Spot the condition | entry page | Medium | Still titled "Drill 1" (`DrillOneExperience.tsx:28`) → "Spot the condition". |
| Spot the condition | raffle Q | Low | Options use "I" when the question says "you" → "Yes, it says you win." |
| Drill 2/5/Rev 5 | #02 | Medium | "you are instructed to expect thunder" → "you should expect thunder to follow." |
| Drill 2/5 | #14 | Low | "this fictional election", "not election-law advice" → "the club election". |
| Drill 3 / Drill 4 | #11 / #10 | Medium | "Errors are always documented" states a fact, but the note calls it an instruction → "must always be documented" (add "must"). |
| Drill 6 | #07 | Medium | "The reviewed statement makes teamwork…" → "The rule makes teamwork necessary for success." |
| Drill 6 | #11 | Medium | "Every" keyed Group 1, but the sufficient side is "legally binding" → key only "must". |
| Drill 6 | #14 | Low | "artists are not inspired" → "those artists were not inspired". |
| Revisit 6 | #24 | Medium | "then that complaint … is not filed" → "then no complaint … has been filed". |
| Revisit 6 | #20 | Low | "must" inside the condition, then "is not required" → "is required to be recalibrated" in both. |
| Drill 8 | #02 | Medium | "Each and every" not taught → key "every", accept either. |
| Drill 8 | #20 | Medium | "always" keyed Group 2, but the explanation says it is not a condition; unreadable sufficient side → replace the item. |
| Drill 8 | #26 | Medium | "that system has a good legal system" is circular → "a place has independent judges → that place has a good legal system". |
| Drill 8 | #31 | Medium | The source result was replaced, and the note says "do not grade it" → remove or rewrite. |
| Check contrapositive | items 1, 7, 8, 9 | Medium | "Write it in English" shows the original sentence word for word → skip that step when the sentence is already if/then. |
| Mixed | write-your-own #6 | Medium | Asks "what must be true of a stall" but the answer is "stalls with a permit" → reword the prompt. |
| Mixed | transfer-1 C | Medium | Uses negation before the contrapositive lesson → replace the distractor. |
| Mixed | diagram stage | Medium | One-word labels ("dancer", "map") cut against "keep the complete condition" → use full labels. |
| Mixed | correct template | Medium | "Your diagram keeps dancer as sufficient for stretch." → use the readback. |
| Mixed | confirm-direction C | Low | "Registration accepted → Registration accepted" is not a plausible distractor. |
| Mixed | write-your-own | Medium | "under this statement" → "under this rule". |

## What checked out
- Every answer key in Drills 2 to 5 is correct, and every indicator in them can be selected.
- All 24 Spot the condition keys are correct; both contrapositive lessons come before any drill that asks for a contrapositive.
- The staged drills now give hints only (fixed earlier today); Check your contrapositive keys and hints are correct.
- Drill 7 and 8 double negatives and compound negations (#13, #15, #16, #21, #23–25, #27, #35) are handled correctly.

## Not verified
- No reviewer clicked through every drill in a browser; flow findings come from reading the code.
- Screen-reader behaviour.
