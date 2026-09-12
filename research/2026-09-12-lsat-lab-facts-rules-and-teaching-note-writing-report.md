---
title: LSAT Lab facts, rules, conditionals, and a teaching-note writing skill
date: 2026-09-12
status: researched
sources:
  - .firecrawl/lsat-lab-facts-rules-agent.json
  - .firecrawl/teaching-note-writing-skill-agent.json
---

# What the research changed

The session note should not teach “apply a rule to a fact” as if every conditional Must Be True stimulus contains both. LSAT Lab's explanations make the cleaner distinction:

- A **fact** is an asserted true condition or case supplied by the stimulus.
- A **rule** is a general conditional relationship. It says what must follow if its trigger is present; it does not establish that the trigger occurred.
- Some stimuli contain rules and no facts. In those, chain the rules. Do not invent a fact.
- When a fact is supplied, test whether it matches a rule's sufficient condition. If the result is known false, use the contrapositive. Do not reverse or negate a conditional.

That is the correction applied to [Sofia's 2026-09-11 recap](../students/sofia/recaps/2026-09-11-recap.md).

## LSAT Lab method

1. Identify a Must Be True stem: “must be true,” “could be logically inferred,” or equivalent.
2. Find related statements. Repeated terms are possible bridges, not automatic links.
3. Label each statement as a fact or a rule. Check whether the repeated term is in the position needed for a valid chain.
4. Chain valid conditionals: `A → B` and `B → C` yield `A → C`.
5. If a supplied fact matches a trigger, apply the rule forward. If a known result is false, use the contrapositive: `A → B` becomes `not-B → not-A`.
6. Prephrase the inference, then test answers. Reject reversals, same-direction negations, unsupported quantities, and answers that assume a trigger the stimulus never established.

The most useful source checks are LSAT Lab's [Must Be True video](https://www.youtube.com/watch?v=uywHnsMelJg), [Conditional Logic video](https://www.youtube.com/watch?v=jeDnykOrswY), the [standards-committee explanation](https://www.lsatlab.com/lsat-explanations/PT149-S1-Q18/if-the-standards-committee-has-a-quorum), and the [conditional-logic cram sheet](https://assets.lsatlab.com/uploads/2024/07/2024-Updated-LR-cram-sheet.pdf). The standards-committee explanation is especially useful because it explicitly notes that a stimulus can contain no facts.

## Ranked research for a reusable post-session-note skill

The Firecrawl agent scored each candidate from 1 to 5. Weights were pedagogical usefulness (25%), transfer to student notes (25%), clarity/scannability (15%), fit with Joshua's voice (10%), evidence/authority (15%), and implementation cost (10%, where 5 means easy to implement).

| Rank | Candidate | Type | Weighted score | Best use |
|---|---|---:|---:|---|
| 1 | [Retrieval Practice Guide](https://pdf.retrievalpractice.org/RetrievalPracticeGuide.pdf) | Guide | 4.75 | Make the note lead to recall and transfer, not passive rereading |
| 2 | [Retrieval Practice for Improved Learning](https://www.cmu.edu/teaching/resources/instructionalstrategies/activelearningstrategies/retrievalpractice/index.html) | CMU framework | 4.55 | Add a short explain-from-memory diagnostic |
| 3 | [Cognitive Load Theory in Practice](https://education.nsw.gov.au/content/dam/main-education/about-us/educational-data/cese/2017-cognitive-load-theory-practice-guide.pdf) | Government guide | 4.50 | Use one worked example, then fade the scaffold |
| 4 | [Backward Design](https://teaching.uic.edu/cate-teaching-guides/syllabus-course-design/backward-design/) | UIC framework | 4.50 | Tie takeaway, evidence, and next practice to one capability |
| 5 | [Business Writing](https://writingcenter.unc.edu/tips-and-tools/business-letters/) | UNC guide | 4.45 | Keep prose plain, active, concise, and scannable |
| 6 | [Audience](https://writingcenter.unc.edu/tips-and-tools/audience/) | UNC guide | 4.25 | Write for a capable student who does not share the tutor's context |
| 7 | [Anthropic public skills repository](https://github.com/anthropics/skills) | Repository | 3.45 | Packaging reference for a `SKILL.md`, not the teaching method |

### Recommendation

Build a custom `lsat-post-session-note` skill. Use retrieval practice as the learning loop, worked examples and cognitive-load principles for explanations, backward design for next steps, and UNC's audience/plain-language rules for the prose. Use the Anthropic repository only as a packaging reference.

The proposed note shape is:

1. **Main takeaway:** one transferable LSAT concept or decision rule.
2. **How to use it:** cue, reasoning move, and common trap.
3. **What the work showed:** evidence-based diagnostic, with fact separated from interpretation.
4. **Practice next:** one retrieval prompt and one concrete transfer task with a success criterion.
5. **Watch-for:** only if the session left a real uncertainty.

The skill should explicitly forbid chronological play-by-play, praise for merely choosing a correct answer, answer-key dumping, unsupported claims about improvement, generic motivational filler, and invented student beliefs. It should require a scan test: the student can find the main concept and next action in under two minutes.

### Backups

- **Cognitive Load Theory in Practice** is the best backup when the difficulty is explaining a complex LSAT reasoning process without overwhelming the student. Keep the worked example short and fade the scaffold.
- **UNC Business Writing** is the best backup when the difficulty is tone, organization, or concision. It cannot replace a learning-science diagnostic.

## Source-backed principles to carry into the skill

- Retrieval is a learning strategy, not only an assessment. [Retrieval Practice Guide](https://pdf.retrievalpractice.org/RetrievalPracticeGuide.pdf), “What is retrieval practice?”
- Worked examples should make every important reasoning step visible, then guidance should fade. [Cognitive Load Theory in Practice](https://education.nsw.gov.au/content/dam/main-education/about-us/educational-data/cese/2017-cognitive-load-theory-practice-guide.pdf), “Strategy 2: Use worked examples.”
- Start with the capability the student should demonstrate, then choose evidence and practice that match it. [UIC Backward Design](https://teaching.uic.edu/cate-teaching-guides/syllabus-course-design/backward-design/).
- Write for the actual reader. The student is capable but does not share the tutor's context, so the note must define the needed term and carry the reasoning. [UNC Audience](https://writingcenter.unc.edu/tips-and-tools/audience/).

## Caveats

This is a research synthesis and design proposal, not proof that one public source already contains the exact skill we need. The retrieval guide and NSW PDF had no clearly established reuse license in the fetched material. UNC and CMU pages state Creative Commons terms; adapt principles rather than copying their prose. Anthropic's repository has mixed licensing by subdirectory. Human review remains necessary for LSAT logic, student diagnosis, privacy, and any claim about progress.
