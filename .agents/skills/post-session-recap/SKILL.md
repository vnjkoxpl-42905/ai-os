---
name: post-session-recap
description: Create the LSAT post-session note and homework proposal from a tutoring session or transcript, built in the approved Session Desk design (3D hero, tactile cards, switches, stamped tap-to-check rows). Activate for "session write up", "session write-up", "make a post-session recap", "write up the session", "recap my last session", "make session notes", "[student] session", or similar requests to turn a completed tutoring session into student notes. In an established tutoring-session context, "write up", "recap", and "make notes" also activate it. Owns transcript grounding, the student record, the post-session note (with a drill note only when a drill needs one), preview, verification, and filing. Explicit transcript lookup or inspection stays narrow; posting and assignment require authorization.
---

# Post Session Recap

Turn one tutoring session into the notes the student reads afterwards. Every note is built in the **Session Desk** design, never a newly invented one. The model is **Finding the Conclusion by Asking Why** (Lanae, 2026-10-29), which Joshua approved on 2026-11-13 as the gold standard for the look, the interactions, the exercises, the note structure and the writing quality. The full specification is [references/session-desk/SPEC.md](references/session-desk/SPEC.md). Read it in full before every build and follow it literally; where it is silent, do not improvise, and list the gap for Joshua.

## Finish the note process

On continuation, read the existing session record and latest decisions before asking anything. Do not restart the design interview or repeat an unanswered homework questionnaire on every turn. Separate preparation from authorized student-facing actions: unresolved homework does not prevent completing the teaching, syncing the records, checking the files, or showing the notes.

1. Resolve the session and read the complete transcript.
2. Extract the teaching and every commitment using the private source map below.
3. Choose the one idea the post-session note teaches. Add a short note beside a drill only when the drill has no intro of its own or the note teaches the idea the drill practises.
4. Build with the Session Desk procedure (SPEC.md section 2), then check reasoning, interaction and reading order.
5. Sync the primary Markdown to the exact current HTML wording, including hidden practice answers. Preserve private material and prior versions.
6. Present the post-session note together with one concise homework proposal and any decision genuinely needed. Propose a specific matching drill for approval instead of handing Joshua an empty selection task. Distinguish an unverified candidate from a validated assignment.
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

## The post-session note

Every session produces one post-session note: a teaching note that carries the session recap. Decided by Joshua 2026-11-14; this replaces the three-note set (recap, drill primer, method reference) he chose on 2026-10-25. Vocabulary is in `CONTEXT.md`.

| Part | Job | Shape |
|---|---|---|
| **Post-session note** | What the session taught, in his voice, so the student can return to it, with the session recap inside | Full Session Desk page: hero with 3D stage, five to nine sections, practice checks, tick-off work list |

- **A drill note is an exception.** A guided drill already carries its own intro. Add a short note beside a drill only when the drill has none, or when the note teaches the idea the drill practises. It must match the real drill instructions, not an assumed task inferred from the title. Pick the matching drill and have Joshua approve it before anything is assigned.
- **Adapted note.** If an earlier teaching note on LSAT U already covers the topic, reuse its teaching and write a fresh recap for this student and session. Never copy a recap between students. Check posted notes first (`classroom_items`, type note). Write a new teaching note only when none exists, grounded in `corpus/Curriculum/<type>/Notes/` and the session.
- **Warm-Up** notes are standing sets, not post-session notes. They carry no session recap.

Keep the quality bar the same for every note: Joshua's voice, no banned words, the model note's visual standard, and real platform questions where a question appears. For a revision, preserve the intended student's existing lesson marker and item identity where supported; inspect any older note before posting a second copy. An approved appearance does not authorize a duplicate note or an unrelated student's update.

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

The transcript supplies session teaching. Corpus material can ground the teaching. Inventory and posted notes supply the design and reusable teaching for an adapted note. Narrow live reads can check identity, existing assignments, note duplication and delivery status; they do not replace the transcript or require a broad student-performance data pull. If an operational check fails, complete the independent note preparation and report the specific unresolved check.

**Student-facing names (2026-10-25)**: Never show **manual**, **Recognition drill**, **Step zero**, or **The finalist** to students, including browser titles and hidden answers. These are private planning labels. Name the actual task or omit the redundant label. The historical design name stays private. Use **Session recap** for the post-session note. A drill note, when one is needed, may use **Before you start**. Keep the existing design and teach in plain language. The generated-page lint rejects this wording.

## Build in the Session Desk design

Everything needed is in [references/session-desk/](references/session-desk/):

- `SPEC.md` is the specification: build steps, page order, every piece with its markup and limits, what the script adds, fixed wording, each visual effect and its job, the writing and practice-check standards, and the verification commands.
- `model-finding-the-conclusion.html` is the approved page. Open it before every build and keep it beside the draft.
- `model-finding-the-conclusion.src.html` is the starting file for every recap. Copy it to `recap.src.html` and replace the content piece by piece.
- `session-desk.css` and `session-desk.js` hold all styling and behaviour. Reuse them unchanged.
- `build_session_desk.py` builds the three pages and checks them. It writes nothing if a check fails.

The older [references/session-manual/](references/session-manual/) folder is retired as the look. Its `INVENTORY.md` is still useful for finding Joshua's earlier posted notes and reusable reference content, and its `student-copy-exclusions.json` still feeds the builder's wording check. Do not build new notes with `build_session_manual.py`.

### Why the procedure is this strict

Joshua asked that the next note match the approved one without anyone having to guess. So the rule is: copy, then replace. Start from the model source, change content only, and let the stylesheet, script and builder supply everything else. A new colour, effect, piece or label is a change to the standard, and it needs his approval before it goes into the CSS, the spec and the builder checks together.

### Recap structure

Follow SPEC.md section 3 for the order and section 4 for each piece. In short:

1. **Hero.** Kicker `Session recap · <Month day>`, a title naming the reasoning on two lines, a lede that names what most students do and what works instead, and the 3D stage: two cards for what the student does or asks, resting on the result.
2. **The first thing to do**, as numbered steps with a key-rule callout.
3. **The distinction the session turned on**, as two or three kind cards when the session taught real categories.
4. **The rule or test itself**, with the two-switch gate only when the rule has exactly two conditions.
5. **A shortcut and its limit**, with warning-word tags, the one red trap callout and the credit line.
6. **Practice checks.** Two or three, at least five rows, one row being the trap.
7. **The method as a short checklist**, with the left-then-right screen only when it applies.
8. **The student's work**, last, as tick-off steps holding every assignment and promise.

Optional pieces are omitted when the session does not call for them. Never invent a taxonomy, a second condition or a credit line to fill a piece. Keep the five-minute reading target for the recap.

### Writing

Authority: Joshua’s current instruction and dated corrections take priority. Use the teaching register in `wiki/teaching-voice.md` and `references/lsat-teaching-voice-standard.md` next; host-written synthesis and historical examples cannot override them.

1. **Draft from Joshua’s emphasis map.** Teach what he actually stressed, including useful examples and his level of emphasis. Keep each note’s job distinct. A short reminder may repeat; do not reteach the whole lesson in a paired drill note. The recap is about a five-minute read, not a word quota for every note.
2. **Check the reasoning.** Try a counterexample. Narrow an overstated claim while preserving its accurate teaching point. Never silently remove an emphasized point to solve an accuracy concern. If it cannot be stated accurately without changing his method, flag the conflict and ask Joshua. Do not reproduce false claims or invented percentages.
3. **Read beside the source.** Compare the draft with the relevant transcript lines and his selected voice example. Keep terms he teaches, then explain them plainly: “Negate the answer. That means treating it as not true.” Use ordinary language, natural contractions and examples that explain why. No em dashes, stock encouragement or generic slogans. Teach traps without blaming the student; credit only source-backed reasoning.
4. **Inspect all student copy.** Read visible headings, instructions, examples, revealed answers and browser titles. Apply the current scoped exclusions in `wiki/COPY-CORRECTIONS.md`. Private editorial terms never become student labels. Check drill instructions against the actual drill rather than inferring the task or count from its name.

Before handoff, show the private emphasis map with a timestamp and the exact passage teaching each important point. An omitted point needs a recorded reason. Do not claim a browser or phrase check proves Joshua’s voice. After one complete revision addressing his corrections, present the result and wait for his response rather than continuing unrequested rewrites. Existing explicit implementation and delivery approval still apply; do not re-ask settled questions.

## Record, preview, verify

- **Primary record:** `students/<slug>/recaps/YYYY-MM-DD-recap.md`, holding the student-facing text, then the `PRIVATE CONTINUATION` divider, then a clearly marked current source map, current assignment/status table and flags for Joshua. Dated superseded versions remain below as history; readers must not reconcile conflicting old tables to discover current state. Preserve any earlier recap; add a dated revision rather than overwriting.
- **Builds:** `brainstorms/YYYY-MM-DD-<student>-post-session/` with `recap.src.html` (copied from the model source) and, only when a drill needs one, `primer-<drill>.md`. For that drill note, run `uv run --with markdown python -I <skill>/references/session-desk/build_session_desk.py <folder> "<primer.md>|Before you start · <drill>|<marker>"`. Each page keeps a unique `<meta name="lsatu-interactive-lesson">` and stays under 500 KB.
- **Verify before handoff:** run all ten checks in SPEC.md section 11 and report each as done, failed or not done. The builder reports ok for wording (no em or en dashes, "~", "concept lesson" or "establish") and for structure (stage, sections, chips, stamps, gate, credit line, work list). Open the recap beside the model. Every chip, switch and tick box works. No console errors. No sideways scroll at phone width. Every claim and drill answer survives a counterexample attempt. The assignment list matches the transcript.
- **Editorial coverage:** identify the passages that retain each emphasized point; check the exact applicable rejected phrases in rendered text, including revealed answers. Report layout/interaction checks, phrase checks, source/logic review and Joshua’s voice approval separately. Never turn test passes into a writing-quality claim.
- **Interaction checks:** every answer reveal works with pointer, Enter and Space, has visible keyboard focus and exposes its expanded state. Hidden answers receive the same reasoning review as the visible teaching. Static or DOM-stub checks do not establish browser rendering, mobile behavior or student visibility; state the checks actually completed.
- **Whole-set preview:** open each delivered note at a readable desktop width and phone width, and exercise every interaction each actually contains. Keep the model beside the recap for comparison. The browser pane is too narrow for a desktop render, so use the headless Chrome command in SPEC.md section 11 for desktop and the pane's mobile preset for phone. A successful recap preview does not verify a separate drill note. If a file cannot be opened, report that page as unverified rather than marking the set visually complete.
- **Pre-publication check:** all three documents are within the size limit, self-contained, addressed to the exact student and use stable lesson markers. Run supported publisher dry-runs without sending when useful. Present changed wording for review; the earlier approval of a visual model is not approval to publish later content.
- Show Joshua the files, and say plainly what is unposted and what he still has to pick.

## Posting

Draft by default. A request to make notes is not permission to post. When Joshua explicitly approves delivery of the identified notes ("post it", "send it", or "approved" in response to the concrete posting request), post to that student without a second confirmation using `lsat-u-platform-actions` (the local `lsat-u-lessons` MCP `publish_interactive_lesson`, or the documented Node fallback). Approval of a model, appearance, teaching direction or skill rewrite alone is not delivery approval. Homework assignment approval covers only the specified homework, not an unrelated message or note. Verify the saved HTML, student visibility and exactly one active copy. Log the post in the student's assignment log and `wiki/send-ledger.md`. Lovable is not involved.

## After a correction

Record the failure and the reusable fix in [recap calibration](references/recap-calibration.md). Update this file, `SPEC.md` or the stylesheet rather than stacking duplicate rules. A new reusable piece goes into `session-desk.css`, `SPEC.md` section 4 and a builder check together, after Joshua approves it. Log substantive changes in `wiki/log.md`.

## Review illustrated teaching examples

Apply the [illustrated teaching guidance](../../../design/principles.md#illustrations-should-teach-the-example-they-sit-beside). During review, check every image against the example it accompanies. Keep the evidence, conclusion, and explanation together in reading order. Use the same situation to distinguish nearby flaws. For causal diagrams, check the proposed direction, the reverse direction, and a genuine common cause separately. Verify the reading order on desktop and phone and test any reveals. Record the user's correction in recap calibration even when the artifact is still a draft.
