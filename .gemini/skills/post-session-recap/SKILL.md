---
name: post-session-recap
description: Create the complete LSAT post-session note set from a tutoring session or transcript, built in Joshua's Session Manual look. Activate for "session write up", "session write-up", "make a post-session recap", "write up the session", "recap my last session", "make session notes", "[student] session", or similar requests to turn a completed tutoring session into student notes. In an established tutoring-session context, "write up", "recap", and "make notes" also activate it. Owns transcript grounding, the student record, the three-note set (recap, drill primer, method reference), preview, verification, and filing. Explicit transcript lookup or inspection stays narrow; posting and assignment require authorization.
---

# Post Session Recap

Turn one tutoring session into the notes the student reads afterwards. Every note is built from Joshua's own posted notes, never from a newly invented design. The model is **Reading Flaw Answer Choices** (Lexi, 2026-08-05, "Session Manual"), approved 2026-10-25.

## Finish the note process

On continuation, read the existing session record and latest decisions before asking anything. Do not restart the design interview or repeat an unanswered homework questionnaire on every turn. Separate preparation from authorized student-facing actions: unresolved homework does not prevent completing the teaching, syncing the records, checking the files, or showing the notes.

1. Resolve the session and read the complete transcript.
2. Extract the teaching and every commitment using the private source map below.
3. Choose the recap's focus, the matching drill primer and the existing or new method reference. Explain what each contributes; do not repeat the same lesson three times.
4. Build from the Session Manual and inventory, then check reasoning, interaction and reading order.
5. Sync the primary Markdown to the exact current HTML wording, including hidden practice answers. Preserve private material and prior versions.
6. Present the three notes together with one concise homework proposal and any decision genuinely needed. Propose a specific matching drill for approval instead of handing Joshua an empty selection task. Distinguish an unverified candidate from a validated assignment.
7. After explicit posting/assignment approval, execute only the authorized actions, read them back and log them. Report preparation, approval, assignment and posting as separate states.

When the request is to develop this workflow, finish the reusable extraction, writing, building and verification rules as well as the sample notes. Homework selection alone is not completion of that request.

## Run as the recap agent

The `recap-agent` runs this skill for one student and one job (note, homework, or both). `recap-reviewer` then checks the result in a separate session. The agent's tool list withholds posting, assigning, messaging and email, so do not look for another route; if a step needs one, list it for Joshua and stop.

End every agent run with a report that counts what was checked, never "looks good":

- Transcript read in full, with word count and session date.
- Commitments: N of N from the transcript are in the assignment table, each with its real certainty.
- Emphasis map: N of N points have a timestamp and a student-facing passage.
- Student-facing text: builder lint result, and the rejected phrases from `wiki/COPY-CORRECTIONS.md` checked across N of N pages, revealed answers included.
- Previews: which of the three pages were opened at desktop and phone width; list the rest as unverified.
- States, each yes or no: prepared, approved, assigned, posted.

The reviewer returns PASS or a fix list. Apply the fix list once, then present the set and the reviewer's report to Joshua. A correction he makes goes into [recap calibration](references/recap-calibration.md); a problem seen twice becomes a rule here or a builder lint.

## When to activate

Recognize the intent to turn an LSAT tutoring session into student notes. Natural wording counts; no magic phrase is required.

- "Session write up", "make a post-session recap", "write up the session", "recap my last session", "make session notes", "turn the session into a lesson", "[student] session", "write up this transcript".
- Short requests ("write up", "recap", "make notes", "today's session") activate it when the conversation is clearly about a tutoring session. In an empty or unrelated context, ask one short question.

**Resolve the session.** Honor an explicit student, date or supplied transcript first. Otherwise use the session already identified in the conversation, or the student's most recent completed session, verified through Calendar and the intake procedure (America/Toronto for relative dates). Confirm student and absolute date before writing. Never substitute an easier-to-find session, and never pick a future or ongoing one.

**Route by the result asked for.** This skill owns session write-ups and student-facing post-session notes. `transcript-intake` finds, files and privately distils transcripts when no notes are requested. `second-brain-ingest` handles general knowledge sources. `guided-drill-assignment` chooses drills. `lsat-u-platform-actions` posts or assigns after approval.

**Keep narrow requests narrow.** "Find the transcript", "read the transcript", or a question about a session is not a request for notes. Scheduling, payment or consultation mail that mentions a session does not activate this skill.

## The three-note set

Every session produces three notes. Decided by Joshua 2026-10-25.

| Note | Job | One per | Shape |
|---|---|---|---|
| **Session recap** | What the session taught, in his voice, so the student can return to it | Session | Full Session Manual page (below) |
| **Drill primer** | Sets up one assigned drill: the rule from the session, the trap the drill catches, one habit | Assigned drill | Short Session Manual page, kicker "Before you start · [drill]" |
| **Method reference** | The whole method for a question type, kept open while drilling | Question type | Session Manual page, kicker "Reference · Keep it open while you drill" |

- **Method reference:** if one already exists on LSAT U for that question type, revise it lightly and do not write a new one. Check posted notes first (`classroom_items`, type note). Write a new one only when none exists, grounded in `corpus/Curriculum/<type>/Notes/` and the session.
- **Drill primer:** if no drill was assigned, pick one matching drill and have Joshua approve it before anything is assigned.

Keep these purposes distinct. The recap teaches what this session established and what to practise next. The primer is a short read immediately before the actual drill: its task, the relevant rule, the trap and one habit. The method reference covers the full method, including its limits, for repeated use while drilling. A primer must match the real drill instructions, not an assumed task inferred from its title.

Reuse a reference's content across students without altering other students' records. For a revision, preserve the intended student's existing lesson marker and item identity where supported; inspect any older note before posting a second copy. An approved appearance does not authorize a duplicate reference or an unrelated student's update.

## Ground everything in the session

1. Read the **full transcript**, not Gemini's summary. Look in `students/<slug>/sessions/` first, then follow the [intake procedure](references/transcript-intake-and-record.md). Never create a student folder without approval. If no transcript exists, report where you looked and stop.
2. Read `wiki/COPY-CORRECTIONS.md` (especially the "Words never to use" table), `wiki/teaching-voice.md`, `references/lsat-teaching-voice-standard.md`, and [recap calibration](references/recap-calibration.md).
3. Make a source map in the private section: Joshua's governing explanations with timestamps, the student's sticking points, what the student did well, examples used, and uncertainties.
4. **Capture every assignment and promise.** Scan the end of the session and anything Joshua said he would send, assign or do: drills, bootcamps, notes, question sets, recalls, account fixes, next-session topics. Every item goes in the private assignment table with who, item, timestamp and status. Student work and student-relevant promises also go in the recap's "Your work this week," preserving their actual certainty. Mark items genuinely requiring Joshua's choice as **Joshua to approve/select** and propose a matching existing resource where possible; never claim a proposed set has been assigned.

Use this private extraction checklist before writing:

| Extract | Preserve |
|---|---|
| Joshua’s emphasis | The points he stressed, his own useful analogies, their timestamps, and the student-facing passage that teaches each point |
| Central teaching | The reasoning the student should be able to explain after the session; Joshua's explanation and timestamp |
| Traps and distinctions | What fails, why it fails, and a small counterexample; complete conditions, modality, timing and scope |
| Student evidence | Sticking points to teach as general traps; specific successful reasoning to credit accurately |
| Examples | Which session examples teach well; which test details to omit; any new illustrative example clearly identified privately |
| Transfer | The next task on which the student should use the method and the two or three practice checks that test it |
| Commitments | Every drill, question set, note, recall, account fix, promised follow-up and next-session topic; owner, timestamp, exact wording and status |
| Limits | Unclear transcript text, tentative offers, missing resources and source-backed teaching that needs Joshua's judgment |

Distinguish **assigned**, **promised**, **offered/tentative**, **proposed by the assistant**, and **verified available**. "Probably assign" is not a confirmed assignment. Keep every offer in the private table, but preserve its tentativeness in student copy rather than upgrading it to a promise. Student homework contains what the student should do; teacher-only account fixes and delivery tasks remain private unless the student needs to know the outcome.

The transcript supplies session teaching. Corpus material can ground the full method reference. Inventory and posted notes supply the design and reusable reference content. Narrow live reads can check identity, existing assignments, reference duplication and delivery status; they do not replace the transcript or require a broad student-performance data pull. If an operational check fails, complete the independent note preparation and report the specific unresolved check.

**Student-facing names (2026-10-25)**: Never show **manual**, **Recognition drill**, **Step zero**, or **The finalist** to students, including browser titles and hidden answers. These are private planning labels. Name the actual task or omit the redundant label. The historical design name stays private. Use **Session recap**, **Before you start**, or **Reference**. Keep the existing design and teach in plain language. The generated-page lint rejects this wording.

## Build from the Session Manual

All assets live in [references/session-manual/](references/session-manual/):

- `model-reading-flaw-answer-choices.html` is the model. Open it before every build.
- `session-manual.css` is its stylesheet, extended only with small additions (rule line, tables, extra kind colours). Reuse it unchanged.
- `build_session_manual.py` builds the recap from `recap.src.html` and turns primers and references from Markdown into Session Manual pages.
- `INVENTORY.md` catalogs every note Joshua has posted (2026-07-28 to 2026-09-30), with section orders, components, real HTML snippets and voice lines. Reuse a component from it before creating anything.
- `examples/` preserves historical 2026-10-25 builds (Amanda, Yahunatan). They contain superseded wording and are not current copy or label authorities. Use the model and current voice guidance; never copy historical kickers or absolute answer rules. A later approved example must carry its revision status.

### Recap structure

Follow this order, taking what fits the session:

1. **Hero.** Kicker `Session recap · <Month day>`. Serif title naming the reasoning, broken over two lines. A lede that reframes the problem and says why students stall, in two or three sentences.
2. **The first thing to do.** Use a heading that explains the task. Private component names are never visible labels.
3. **The taxonomy.** Two or three `.kind` cards (bar, name, what, "Sounds like" or "Looks like", "Test" or "Use it"), then an `.opposite` panel contrasting them.
4. **One section per taught idea.** Use `ol.steps` for procedures, `.callout` with a tag for the key rule and for "The trap that costs the most", `.flags` for warning words, and `.rule` for a single conditional written as a sentence with an arrow.
5. **Credit lines.** One or two `.quote` lines in second person naming something the student actually did in the session ("You caught this on the tax question before I pointed it out"). Session particulars may also clarify the concept where useful, but never frame an error as "your mistake" or reproduce the original test stimulus.
6. **Practice checks.** Two or three tap-to-check `.chip` checks. The visible heading names the task, such as Negate it.
7. **A short method checklist.** Give concrete instructions for this question type. Omit redundant labels.
8. **Before next session / Your work this week.** Every assignment and promise, as numbered steps.
9. Footer mark `LSAT U`.

Borrow the model's look, structure and useful components without inventing a taxonomy that the topic does not have or padding a primer into a full recap. Keep the five-minute reading target for the recap, not a minimum length for all three notes. Practice checks belong in the recap as implemented in the accepted examples. Joshua requested highly visual, interactive, readable notes; the accepted sample primers and references are static pages. That sample acceptance is not an explicit rule that future primers and references must be static. Use relevant existing inventory interactions when they teach something; do not invent extra controls merely to claim interactivity.

### Writing

Authority: Joshua’s current instruction and dated corrections take priority. Use the teaching register in `wiki/teaching-voice.md` and `references/lsat-teaching-voice-standard.md` next; host-written synthesis and historical examples cannot override them.

1. **Draft from Joshua’s emphasis map.** Teach what he actually stressed, including useful examples and his level of emphasis. Keep each note’s job distinct. A short reminder may repeat; do not reteach the whole lesson in all three notes. The recap is about a five-minute read, not a word quota for every note.
2. **Check the reasoning.** Try a counterexample. Narrow an overstated claim while preserving its accurate teaching point. Never silently remove an emphasized point to solve an accuracy concern. If it cannot be stated accurately without changing his method, flag the conflict and ask Joshua. Do not reproduce false claims or invented percentages.
3. **Read beside the source.** Compare the draft with the relevant transcript lines and his selected voice example. Keep terms he teaches, then explain them plainly: “Negate the answer. That means treating it as not true.” Use ordinary language, natural contractions and examples that explain why. No em dashes, stock encouragement or generic slogans. Teach traps without blaming the student; credit only source-backed reasoning.
4. **Inspect all student copy.** Read visible headings, instructions, examples, revealed answers and browser titles. Apply the current scoped exclusions in `wiki/COPY-CORRECTIONS.md`. Private editorial terms never become student labels. Check drill instructions against the actual drill rather than inferring the task or count from its name.

Before handoff, show the private emphasis map with a timestamp and the exact passage teaching each important point. An omitted point needs a recorded reason. Do not claim a browser or phrase check proves Joshua’s voice. After one complete revision addressing his corrections, present the result and wait for his response rather than continuing unrequested rewrites. Existing explicit implementation and delivery approval still apply; do not re-ask settled questions.

## Record, preview, verify

- **Primary record:** `students/<slug>/recaps/YYYY-MM-DD-recap.md`, holding the student-facing text, then the `PRIVATE CONTINUATION` divider, then a clearly marked current source map, current assignment/status table and flags for Joshua. Dated superseded versions remain below as history; readers must not reconcile conflicting old tables to discover current state. Preserve any earlier recap; add a dated revision rather than overwriting.
- **Builds:** `brainstorms/YYYY-MM-DD-<student>-post-session/` with `recap.src.html`, `primer-<drill>.md`, `<type>-reference.md`. Run `uv run --with markdown python -I <skill>/references/session-manual/build_session_manual.py <folder> "<primer.md>|Before you start · <drill>|<marker>" "<reference.md>|Reference · Keep it open while you drill|<marker>"`. Each page keeps a unique `<meta name="lsatu-interactive-lesson">` and stays under 500 KB.
- **Verify before handoff:** the builder's lint reports ok (no em or en dashes, "~", "concept lesson" or "establish"). Open the recap beside the model. Every drill chip toggles. No console errors. No sideways scroll at phone width. Every claim and drill answer survives a counterexample attempt. The assignment list matches the transcript.
- **Editorial coverage:** identify the passages that retain each emphasized point; check the exact applicable rejected phrases in rendered text, including revealed answers. Report layout/interaction checks, phrase checks, source/logic review and Joshua’s voice approval separately. Never turn test passes into a writing-quality claim.
- **Interaction checks:** every answer reveal works with pointer, Enter and Space, has visible keyboard focus and exposes its expanded state. Hidden answers receive the same reasoning review as the visible teaching. Static or DOM-stub checks do not establish browser rendering, mobile behavior or student visibility; state the checks actually completed.
- **Whole-set preview:** open each delivered recap, primer and method reference at a readable desktop width and phone width, and exercise every interaction each actually contains. Keep the Session Manual beside the recap for comparison. A successful recap preview does not verify the other two pages. If a file cannot be opened, report that page as unverified rather than marking the set visually complete.
- **Pre-publication check:** all three documents are within the size limit, self-contained, addressed to the exact student and use stable lesson markers. Run supported publisher dry-runs without sending when useful. Present changed wording for review; the earlier approval of a visual model is not approval to publish later content.
- Show Joshua the files, and say plainly what is unposted and what he still has to pick.

## Posting

Draft by default. A request to make notes is not permission to post. When Joshua explicitly approves delivery of the identified notes ("post it", "send it", or "approved" in response to the concrete posting request), post to that student without a second confirmation using `lsat-u-platform-actions` (the local `lsat-u-lessons` MCP `publish_interactive_lesson`, or the documented Node fallback). Approval of a model, appearance, teaching direction or skill rewrite alone is not delivery approval. Homework assignment approval covers only the specified homework, not an unrelated message or note. Verify the saved HTML, student visibility and exactly one active copy. Log the post in the student's assignment log and `wiki/send-ledger.md`. Lovable is not involved.

## After a correction

Record the failure and the reusable fix in [recap calibration](references/recap-calibration.md). Update this file or the stylesheet rather than stacking duplicate rules. Add new reusable components to `INVENTORY.md` section C. Log substantive changes in `wiki/log.md`.
