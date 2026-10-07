---
name: rrc-step-names-live-in-the-app
description: "The RRC drill's four step names and their student-facing copy are in the app, not in anyone's head — read them before writing about the drill."
metadata: 
  node_type: memory
  type: project
  originSessionId: 0fab1330-1a2f-4eb3-a78c-b3d24958df4e
  modified: 2026-09-10T06:11:47.961Z
---

The Read-Recall-Colour drill's canonical vocabulary lives at
`projects/lsatu/src/features/activity-centre/content/read-recall-colour-section.instructions.json`,
under `briefing.sections[1].steps[]`. The four steps are **Read it. / Tell it back. /
Colour it. / The Recall.**, each with a `short` line already written in second-person
imperative in Joshua's voice, plus a longer `body`.

Also in that file, and easy to get wrong:
- Space is pressed **twice** per stimulus. First press takes the text away and asks for
  the recall; second press loads the next stimulus.
- **Nothing on the screen ever hides during `working`.** The whole stimulus stays
  readable and looking away is the student's own discipline: "a screen that hides the
  text for you is a crutch that cannot come with you." Anything that dims, blurs or
  hides text is teaching the opposite of the drill.
- The runner has exactly two phases, `working` and `recalling` (`recall/section.ts:37`).
  There is no separate review screen — reviewing before the recall is possible only
  because nothing hides.

**Why:** on 2026-09-10 the RRC instructional video shipped with two invented step labels
("Reading", "Colouring In") and a blur that demonstrated the exact crutch the briefing
refuses. Both came from paraphrasing instead of reading the file.

**How to apply:** before writing any student-facing copy about RRC — video, email,
lesson, course page — open that JSON and lift the wording. Never paraphrase a
student-facing string that already exists in the app; a student who meets the film and
then the drill should meet one vocabulary, not two. See also [[lsatu-copy-corrections-log]]
and [[lsatu-content-lives-in-postgres]].
