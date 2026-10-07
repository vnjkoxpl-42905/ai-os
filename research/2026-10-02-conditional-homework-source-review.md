# Conditional homework recovered from Gmail

Reviewed for the opening bootcamp through Group 2. Gmail retrieval used the authenticated `gws` CLI. No messages were sent or deleted.

## What the search actually covered

All pages of four searches were retrieved. The strict window was 2025-10-02 through 2026-10-02. A sent-message attachment search for conditional, conditionals, sufficient, or necessary returned 29 messages. A second filename/indicator search returned no additional messages. A Queen and conditional filename search returned her general weekly schedule, dated 2025-11-16.

Those matches largely contain flaw, negation, or broader LR materials mentioning conditionals. Dedicated conditional worksheets were found by a supplemental all-time sent filename search: 11 messages dated 2025-06-23 through 2025-09-19. These precede the strict one-year window. They are labeled historical reference materials, not represented as past-year sends.

41 distinct messages and 120 attachments were preserved in `raw/sources/conditional-gmail-2026-10-02/`. This includes every attachment from matching messages, so the archive also contains unrelated materials. `provenance.json` records original filenames, Gmail message IDs, dates, headers, SHA256 hashes, sizes, and exact queries. `extracted-relevance.json` records term matches; these are candidates rather than a claim that every file is a conditional lesson. PDF text extraction produced font encoding warnings for some older PDFs. Original files are intact.

Search limitation: indexed body/text/filenames can miss unnamed, image-only, or unindexed attachments. This is a complete retrieval of the search results, not proof that every conditional homework attachment in the account was found.

## The useful dedicated materials

| Sent date and student | Material | How to use it |
|---|---|---|
| 2025-09-03, Queen | `1991094de0c213db_G1 &G2 worksheet (1) (1).docx` | Three-part progression: highlight indicator and underline concepts; diagram and identify sufficient/necessary roles; original arrow, contrapositive, then English. Strong blueprint for interaction scaffolding. |
| 2025-09-03, Queen | `1991094de0c213db_G1 & G2 Answer key (1) (1).pdf` | Reference explanations to audit against the diagram; verify symbol formatting visually before reuse. |
| 2025-09-03, Queen | `1991094de0c213db_Conditional intro.pdf` | Indicator families, six-step translation method, flip-and-negate, four-case activation chart. Contains a paragraph error discussed below. |
| 2025-09-03, Queen | `1991094de0c213db_4-translation-groups-cheatsheet1 (4) (1).png` | Visual reference. Only Group 1 and Group 2 belong in current scope. |
| 2025-06-23, Kristine | `1979af3af7560da0_intro training group ½ (3).pdf` | Separate concept/indicator identification from complete diagramming using the same sentences. Suitable for progressive support fading. |
| 2025-06-23, Kristine | `1979af3af7560da0_intro answer key group 1 and 2.pdf` | Full-word diagrams and explanations. Negation slashes can disappear in extraction; rendered PDF is authority. |
| 2025-06-23, Kristine | `1979af3af7560da0_Group 1 breakdown.pdf`, `Group 2 breakdown .pdf` | One worked example each, then translation algorithm. Structure useful; older machine/computer prose is not the new student voice. |
| 2025-09-19, Queen | `19964c743716d4d2_Conditional Homework Set.docx`, `Conditional Answer Key.docx` | Applied official-question references across MBT, SA, parallel, principle and flaw. Later application stage, not introductory drill bank. Complex conjunction/chains exceed opening scope. |

Other historical matches include Dillen/Kristine conditional question practice on 2025-07-10; conditional logic practice on 2025-07-14; timed conditional questions on 2025-07-17; Kristine conditional practice on 2025-08-03 and worksheet/review on 2025-08-12; Glenn conditional review on 2025-08-24. Preserve them for later stages rather than importing their full difficulty into the opening.

Selected text extracts, with filenames mapping directly to the original Gmail archive, are in `research/conditional-homework-2026-10-02/`.

## Sandra establishes the current teaching method

The latest local Sandra conditional session is 2026-09-28: `students/sandra/sessions/2026-09-28-conditional-logic-foundations/transcript.md`.

Joshua teaches a conditional as a rule with a trigger and an outcome. One guaranteed way is not necessarily the only way. He uses California and USA, and an entry/passport requirement. He asks what must be true, then compares it to the tempting reversal. He recommends readable labels rather than unexplained A/B/X/Y labels.

The five steps at transcript line 589 are:

1. Identify the conditional indicator.
2. Label the two ideas.
3. Apply the left-side or right-side rule.
4. Find the contrapositive.
5. Say it back in English.

The older six-step PDF separates identifying concepts from labeling them; Sandra combines them. Preserve the newer five-step version. Students first need the idea and worked examples before all five steps are assessed. The full five-step process requires an explicit flip-and-negate lesson, even if the overall unit ends at Group 2. If an interaction assesses only through diagramming, label it as steps 1–3 rather than pretending the whole method stops there.

The session explicitly reserves Groups 3 and 4 for later and asks for repeated Group 1/2 left/right practice until it becomes automatic. The religious example is personalized to Sandra and should not be the default bootcamp example. Unsupported claims about how many LSAT questions use conditionals should not be repeated.

## Errors and wording to correct before reuse

- Queen's intro chart places sufficient present and necessary absent in its first two rows correctly. Its following paragraph mistakenly calls the last two rows the activating situations. Correct to the first two.
- 'Nothing happens' is shorthand for no further deduction about the paired condition. The rule still holds. Knowing the sufficient condition is false does not tell us whether the necessary condition is true or false.
- Word detection is not blind substitution. `Only` and `the only` differ; read the full sentence. An `always` imperative needs its implied context made explicit.
- Some practice statements use 'expect' or 'should' while their answer keys treat them as factual guaranteed outcomes. Rewrite original practice as explicit stipulated rules to avoid mixing obligation, expectation, and certainty.
- Some subset examples omit relevant restrictions. Keep the entire sufficient concept, such as 'applicant who passes', rather than reducing it to 'passes' without a stated applicant universe.
- Symbol extraction can drop the slash, producing an apparent illegal reversal in a correct original PDF. Do not trust extracted symbols alone.

## Recent clips to integrate carefully

`raw/inbox/Dashboard.md` is a 7Sage Lawgic lesson transcript: circles/dots show categories well but cannot carry every conditional or manipulate complex rules efficiently. The arrow is introduced as a second visual language. Use the idea to transition from nested-set interaction to a readable arrow, not to copy the prose.

`raw/inbox/Dashboard 1.md` emphasizes that sufficient and necessary are roles within a particular relationship. A middle category can be necessary in one rule and sufficient in another. Keep this as a short preview or later nuance, not a new chain lesson in the opening.

`raw/inbox/Dashboard 2.md` is Group 1 translation: if, when, where, all, every, any, the only. It notes real grammar/context work in identifying the indicator and the complete concepts. Good justification for a concept-selection interaction before diagram placement.

## Design opportunities grounded in these sources

Start with an example students can inspect: a California marker inside USA, or a complete hypothetical entry rule. Let them move between 'rule' and 'known fact' and reveal exactly what follows. Do not require a smaller inner set; containment, including equal boundaries, is the logical requirement.

Use one sentence across three drill passes: mark its language, select both complete concepts, then place those concepts around the arrow. Later remove the highlights and slots. Feedback should identify the particular misunderstanding rather than only showing a correct arrow.

Contrast the same content under 'if' and 'only if'; have students predict which idea switches sides. Finish by reading the arrow aloud in English. Include both legal deductions and cases where no further conclusion is warranted. Bring the complete five-step method together only after each part has been taught.
