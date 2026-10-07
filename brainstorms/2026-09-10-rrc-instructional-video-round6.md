# RRC Instructional Video, Round 6: Brainstorm / Discovery Notes
Date: 2026-09-10 · Goal: Correct the instructional cut against the app's own drill spec, and settle the revision list he gave on 2026-09-10.
Status: built and delivered, awaiting his review
Context sources:
- [[2026-09-09-rrc-instructional-video]] (rounds 1-5, 1381 lines, source of truth for everything already decided)
- `projects/lsatu/src/features/activity-centre/content/read-recall-colour-section.instructions.json` (NEW ground truth this round)
- `projects/lsatu/src/features/activity-centre/recall/section.ts` (the runner's real state machine)
- `projects/video/` (the build)

## Summary / key decisions
(running synthesis, updated as we go)

- Round 6 opened because he watched `instr-q1.mp4` and returned a revision list, then stopped me mid-build to say the film teaches the wrong sequence and told me to read the real drill first.

## Open flags (pending input)
- (none yet)

## Q&A log

### R6-Q0 - His revision list, verbatim intent (2026-09-10)

Given before any question was asked. Decoded from his message:

1. **Not instructional.** Cards narrate in third person ("He reads the chunk in his head"). Should instruct in second person: "now you are expected to do X", then he demonstrates it. His words: "it snot instuctinal ... now you are expected todo x then does it ... it doens make sens form a stdnt viewr perspective this hould be instuctional".
2. **It glitches between colouring and retelling.**
3. **Edit the script.** "smoothen out and make it more fluid and cut anythign aht is t ofar off they go slightly to far oloruing".
4. **Read-along light.** "should ... light up s the read so it akes itclear wherethey re eye are as the yread".
5. **Screen is off-centre.** "the screen is offcentred igt should mroe centred".
6. **More 3D, more first person.** "should use 3d effets and su h ... should be ore first person its curretnly clsoeb ut needs tobe imrpvoed".
7. **One line per step in Q2/Q3** so The Recall is clearly defined. (Answer to the Round 5 open question about the Recall intro.)
8. **Mine the HyperFrames kit** at `projects/hyperframes-student-kit` for anything useful.

Then, mid-turn:

9. **A full restatement of the whole stimulus after the last chunk**, with the stimulus off screen. "it should do what i was meant o do whre in the orginail rr dril u can reveiwe before ucreate it" -> in the original drill you can REVIEW the whole stimulus before you recreate it.
10. **Review the original drill, then grill him** so the steps are settled and clear.

### R6-Q0b - Facts established from the codebase without asking (2026-09-10)

Read `read-recall-colour-section.instructions.json` and `recall/section.ts` rather than asking him.

**The four steps, in the app's own student-facing words** (`briefing.sections[1].steps[]`):

| # | label | short |
|---|---|---|
| 1 | `Read it.` | Read about a sentence at a time, silently. Nothing is spoken yet. |
| 2 | `Tell it back.` | Look away and tell it back in your own words, out loud. |
| 3 | `Colour it.` | React to it out loud. A doubt, a question, an example, a joke. |
| 4 | `The Recall.` | The text goes. Say the whole argument back from memory. |

- **Two of my four shipped labels are inventions.** The film says "Reading" and "Colouring In". The app says "Read it." and "Colour it.". CONFIRMED DEFECT.
- **This also settles the Round 5 open question on step 2.** The app says "Tell it back.", not "Rephrase". The shipped label was already right.
- **Structure:** "Three steps through the stimulus, then a fourth step once you have read all of it." Steps 1-3 loop per chunk; step 4 happens once. The film models this correctly.
- **Space is pressed TWICE per stimulus.** "The first press takes the text away and asks you for the whole argument from memory. The second press moves you to the next stimulus." The film presses once. CONFIRMED DEFECT (missing second press).
- **The runner has exactly two phases**, `working` and `recalling` (`section.ts:37`). `advance()` goes working -> recalling -> next item working. There is NO separate review screen.
- **THE BIG ONE - the film contradicts a stated design principle of the drill.** The briefing says, under the heading "Look away. That part is on you.":
  > "While you are working the stimulus, nothing on the screen hides. The whole thing stays readable, which means the only thing stopping you rereading a line while you tell it back is you, looking away from it."
  > "That is deliberate. Reading while you recall is a one way street with cars coming both ways."
  > "It is also the version that still works on paper, and on test day. **A screen that hides the text for you is a crutch that cannot come with you.**"

  The film's `POVStimulus` / `chunkBlur` blurs every inactive chunk to 2.6px at 0.62 opacity, and blurs ALL chunks to 3.1px while he speaks. So the film shows the app hiding the text for him. That is the exact crutch the drill was built to refuse. It is also why "review before you recreate it" has nowhere to happen: the page the student is meant to be able to re-read is blurred out.

  This makes the "review" he asked for not an addition but a **restoration** - it becomes possible the moment the blur goes.

### R6-Q1 - The blur
- Asked: The stimulus on screen: how readable should it stay while he works through it? Given that the briefing says nothing hides and that the blur is what blocks the review beat.
- **Captured: FULLY READABLE, NO BLUR.** He took the recommendation.
- Consequence: `chunkBlur()` in `src/pov/Room.tsx` is retired. Attention is carried by the camera glance alone, which already exists. The whole stimulus is legible in every working beat.
- This reverses a Round 3 decision (optical defocus as the attention device). Reason it falls: the drill's briefing explicitly refuses a screen that hides text, and the defocus was the film demonstrating exactly that crutch.
- It also unblocks the review beat at no cost: the page the student reviews is now on screen and readable.

### R6-Q2 - What the review beat actually is
- Asked: After the last chunk and before Space, what does the review beat show? Flagged first that the app never prescribes a review, it only permits one ("press space when you have got all of it" + nothing hides), and that a full re-read risks teaching students to recall from a fresh read rather than from retention.
- **Captured: SILENT CHECK. ~5s held beat, whole stimulus readable, eye sweeps all of it once at a CHECKING pace, faster than reading. Then Space.**
- His framing: "what i was meant o do" - his own recording did not do this, but the demonstration must show the intended method regardless.
- Consequence: a new `review` beat kind, inserted after the last `speak` and before the `press`. Silent, because his audio has no such stretch. Camera sweeps the full quad rather than sitting on one chunk.
- Deliberately NOT a re-read. The distinction the film has to carry: "look over the whole thing and decide you have got it" is not "read it again".

### R6-Q3 - Where Tell it back ends and Colour it begins
- First attempt used the word "retell", which he did not recognise: "what dou eman by retell". Corrected: dropped the word, re-asked using only the app's vocabulary (step 2 "Tell it back.", step 3 "Colour it."). VOCABULARY NOTE: do not invent shorthand for his step names.
- Asked: Inside one continuous stretch of him talking, what marks the end of "Tell it back" and the start of "Colour it"?
- **Captured: the first thing that was not on the page.** While he is only saying what the sentence said, that is step 2. The moment he adds a picture, a doubt, a comparison or a what-if, that is step 3.
- Method: mark all 7 boundaries against his real Whisper word timings (`align/PT105_S2_Q*.words.json`) so the split is measured, not authored. Show him the list before rendering.
- Fixes the glitch: currently `release` (0.38-0.50s) is labelled "Tell it back" and `speak` (16.5-34.0s) is labelled "Colouring In". The half-second label flash IS the glitch he saw.

### R6-Q3b - HE FLAGGED AGAIN: the step after the spacebar
- His words: "it is missing one sep after aspacebar pressed it shuld make the m reate the whole arguemnt everychunk combined at thenwithut the sitmulus insight like the drill revwi the rrc drill t omake sure u ndetand what imean"
- He raised this twice. I verified rather than assumed, and he is right, though not in the way I first read it.

**What I verified:**
1. The Recall TEXT is correct. `recall/scripts.json` for Q1 covers every chunk: divers found the cave, the underwater tunnel, the seawater interior, the stalagmites, and the definition. Every chunk combined. NOT a defect.
2. The Recall AUDIO plays (23.52s, Chatterbox clone of his voice). NOT a defect.
3. **The Recall PICTURE is the defect.** Frame grab of `out/instr-q1.mp4` at 125s shows a large blank white panel and nothing else for 23 seconds. No visual evidence that an argument is being reconstructed. The step that "gets scored" reads as dead air.
4. The film is FAITHFUL here - `SectionStage.tsx:179-188` confirms the real app shows a blank stimulus area with footer "Say the whole argument back from memory." So the defect is not accuracy. A faithful blank screen simply makes 23 seconds of dead film.

**The resolution available:** this is the Round 1 tension (screen fidelity vs teaching the invisible discipline) recurring. This film already has the established answer - annotations float in the ROOM, never on the screen. So the screen can stay honestly blank while the argument visibly rebuilds beside it in room space.

**Data available to drive it:** `recall/generated/PT105_S2_Q*.recall.timing.json` carries SENTENCE-level timings of the synthesized recall (Q1: 9 sentences across 23.52s). The assembly can be timed to his voice exactly.

**Other defects visible in the same frame grabs:**
- The monitor sits well left of centre with dead wall and window on the right. Confirms his "screen is offcentred". Root cause found: the detected screen quad in `src/pov/quad.ts` spans x 0.071-0.616 of the plate, so its centroid sits at x=0.34, not 0.5. The camera never compensates.
- The `StepLabel` at top-left is CLIPPED by the frame edge during the recall.
- The step card at 108s reads "He presses Space. The stimulus disappears. He gives the whole argument back from memory." - third person, confirming his "it snot instuctinal" complaint.

### R6-Q4 - How the argument rebuilds during The Recall
- Asked: During The Recall, what appears in the room as he speaks? Constraint stated up front: the screen stays blank because that is the drill, but the room is where this film already puts everything the screen cannot show.
- **Captured: THE ARGUMENT STACKS UP, SENTENCE BY SENTENCE.** Each sentence of his recall lands as a card in the room as he says it and STAYS. By the end the whole argument is assembled beside a blank screen.
- Driven by `recall/generated/PT105_S2_Q*.recall.timing.json` sentence timings, so the assembly is locked to his voice.
- Rejected: revealing missed details at the end (turns a demonstration into a scoring exercise), and one-card-at-a-time (nothing accumulates, so the whole argument never visibly comes back together).
- This is what makes "every chunk combined" visible rather than only audible, which is what he asked for twice.

### R6-Q5 - Which digressions get cut
- Measured two candidates against his real word timings rather than guessing:
  - **A. The YouTube aside**, 35.96-41.06 = **5.10s**: "If you all are too young for this, look up Amy Poehler Thai boys on YouTube." The Thai cave comparison immediately before it is good colouring and stays; this is the part that talks past the material to an audience.
  - **B. The stalagmite working-out**, 73.32-86.72 = **13.40s**, which splits into two different things:
    - 77.5-80.2 (2.7s) the stalactite tangent: "I guess stalactites are the ones that form on the ceiling. These are the ones that form on the floor." Stalactites are not in the stimulus.
    - 80.2-86.7 (6.5s) him telling back the stimulus's OWN definition. Legitimate step 2/3 work, not a digression.
- The payoff at 86.72, "So from this we can infer that it wasn't always totally filled with water", is protected in every option.
- He asked what the stalactite tangent was, so I quoted it back verbatim with context rather than describing it. His concern: "it needs to be more relatabale".
- **Captured: CUT THE STALACTITE LINE.** 2.7s out. Reasoning I gave and he accepted: it is outside knowledge he hedges on ("I guess"), so on tape it reads as the teacher being unsure rather than as a memory hook, and that is what costs him, not the tangent.
- Rejected: keeping it with a ceiling-vs-floor graphic (adds a graphic to a film that has deliberately kept them scarce).
- STILL OPEN at this point: the YouTube aside (A). He answered the sub-question about stalactites without ruling on A.

### R6-Q6 - The YouTube aside, and the second-person card copy
- Asked (a): cut the YouTube aside? (b) where does the card copy come from?
- **Captured (a): DO NOT CUT - REPLACE.** His words: "rpelace it with omething that is moreitnuive to the a ntaualr peros more ituive epersoable and mroe itnuvi to gernela masses but ver y human". So the weak line is replaced with better colouring, not removed.
- **Captured (b):** "should have a recall part done first hten colour it usingap eornable rlateble applygin the pricneples ofthe dirll but u caninovate andmake slightyl difernte exmaple" - read as: telling it back comes first, then colouring (confirms the R6-Q3 order), and he authorises me to author replacement examples that apply the drill's principles.
- **On the card copy specifically, a fact found rather than asked:** the app's briefing ALREADY contains second-person imperative `short` lines for all four steps. Using them verbatim fixes the third-person problem, fixes the two invented labels, and guarantees the film and app teach one vocabulary. Adopted.

### R6-Q7 - Scope and register of synthesised colouring
- FLAGGED TO HIM BEFORE ASKING: this reverses the Round 5 decision "only The Recall is synthesized; his real recordings carry steps 1 to 3". Part of step 3 becomes words he never said, in his cloned voice, under his name. He owns the brand and the drill so it is his to authorise, but it was not slid past him.
- Asked (a): which replacement line? (b) does the authorisation extend past this one line?
- **Captured (a): a CONSTRAINT rather than one of the drafts.** "shoud be ntual or ai sounign an ormal person woul undetand andotn go to otuhtere" = should be natural, NOT AI sounding; a normal person would understand it; do not go too out there.
  - Production consequence: every synthesised line is spot-checked against his real audio. If it reads as synthetic it does not ship.
  - Content consequence: replacements stay grounded and universal. Nothing clever, nothing niche, nothing that dates.
- **Captured (b): ANY COLOURING THAT LANDS BADLY**, across all three stimuli. Every replacement line comes back to him for approval BEFORE synthesis. That gate was in the option he chose and is now binding.

### R6-Q8 - The replacement colouring lines themselves
- Went through all 7 colouring passages across the three stimuli. Most are strong and stay untouched, specifically: the aspirin-vs-flu-shot line (Q2), the million-dollars-per-vaccine objection (Q2, the real LSAT objection and the best colouring in the film), and the overtime-vs-lost-day passage (Q3).
- Four moments land badly. All measured against his real word timings. Only TWO need synthesis, which keeps the departure from his real run small.

| # | slug | span | secs | action |
|---|---|---|---|---|
| 1 | Q1 | 18.24-21.12 | 2.88 | CUT "or maybe it's like a volcano situation" |
| 2 | Q1 | 76.50-80.18 | 3.68 | CUT the stalactite line (agreed R6-Q5) |
| 3 | Q1 | 35.96-41.06 | 5.10 | REPLACE the YouTube aside |
| 4 | Q3 | 72.84-78.40 | 5.56 | REPLACE the reversed assumption line |

**Seams verified by reading the word stream either side:**
- Cut 1 leaves "...maybe it used to be above water, now it's filled in. Who knows?" - good colouring on its own, and it quietly sets up the chunk-3 inference.
- Cut 2 joins "which is what happens when like drops of water," directly to "where it's like the drops keep falling over time, then the deposits layer up," - reads clean.
- NOT verified by ear. Nobody has auditioned these seams.

**#4 was found by me, not raised by him, and is the most serious.** As recorded he says: "Or what if just because saving money is important, that doesn't mean it's the most important thing. **It's the overriding concern, and that should be the sole basis on which we make this decision.** Sort of an assumed universal goal there." Taken straight, the middle sentence asserts the opposite of his point - that saving money IS the overriding concern and SHOULD be the sole basis. He means the argument assumes that. In a film teaching how to find an assumption, stating the assumption as fact is the worst available error.

- **Captured: ALL FOUR APPROVED.**
  - Both cuts approved (6.56s out, nothing synthesised).
  - Replace 1 approved: "There is no walking in. You would have to swim through a tunnel in the dark to get there. That sounds like a nightmare." Runs on from his Thai soccer team line, which stays.
  - Replace 2 approved: "or the overriding concern, or the only thing we should be deciding this on." Runs on from "that doesn't mean it's the most important thing" and into "sort of an assumed universal goal there".

### R6-Q9 - The read-along light
- FLAGGED FIRST: this bumps the Round 1 rule "nothing marks the text", which exists because anything drawn on the page can be mistaken for an app feature the student will not have. That rule is why blur was chosen originally.
- Why it is now compatible: blur worked by REMOVING legibility, which the briefing refuses. A light works by ADDING emphasis while everything stays fully readable. It just has to read as light falling on a page, not as a highlighter.
- **Captured: A SOFT WARM POOL TRAVELLING THE LINE.** Gentle unfocused glow moving word to word. Every word stays fully readable, lit or not.
- Pace is free and measured: his real read duration divided across the chunk's words, so the light moves at the speed he actually read.
- Rejected: karaoke highlight (looks exactly like a software feature, the Round 1 failure), line brightening (edges back toward de-emphasising text).

## Round 6 - settled

1. **No blur.** Whole stimulus fully readable in every working beat. `chunkBlur()` retired.
2. **Review beat.** ~5s silent held beat after the last chunk, eye sweeps the whole page at a checking pace, then Space. Not a re-read.
3. **Tell/colour split at "the first thing that was not on the page."** 7 boundaries marked against real word timings. Fixes the half-second label flicker.
4. **The Recall assembles.** Each sentence of the recall lands as a card in the room as he says it and STAYS, so the whole argument is visibly rebuilt beside a blank screen. Driven by the existing sentence timings.
5. **App's own copy, verbatim.** Read it. / Tell it back. / Colour it. / The Recall., with the briefing's second-person `short` lines. Two invented labels retired.
6. **Second Space press** added after the recall. The app presses twice per stimulus; the film pressed once.
7. **Four edits to his audio.** Two cuts (volcano 2.88s, stalactite 3.68s), two synthesised replacements (YouTube aside, Q3 reversed assumption line). Approved verbatim.
8. **Synthesised colouring is authorised generally**, subject to: natural not AI-sounding, understandable to a normal person, not too out there, and every line approved before synthesis.
9. **Reading light**: soft warm pool travelling the line at his real reading pace.
10. **Screen centring, more 3D, stronger first person**: taken as technical work, not asked.

## Open flags (pending input)
- Screen centring has a geometry limit not yet put to him. The monitor occupies plate x 0.071-0.616 so its centroid sits at x=0.34. Fully centring it requires zoom >= 1.45, at which the monitor fills 994 of 1080 frame px and the room mostly disappears. Options are partial centring, or a new Kling plate with the monitor centred (19 credits of 641). To be shown a still rather than asked in the abstract.
- Seam quality on the two cuts is unverified by ear.

## Build log (2026-09-10, Round 6)

**Voice patches generated.** `recall/generate_patches.py`, same Chatterbox path as the recall passages, spec in `recall/patches.json`.
- `Q1_TUNNEL.patch.wav` 6.28s (replaces 5.10s, +1.18s)
- `Q3_ASSUMPTION.patch.wav` 6.52s (replaces 7.72s, -1.20s)
- Two departures from the approved wording, both to serve his own "natural, not AI sounding" constraint, both flagged to him: contractions ("There's" / "You'd") because he does not speak in full forms; and Q3 synthesised as one whole sentence rather than the bare fragment "or the overriding concern...", because a fragment beginning "or" gets unnatural prosody in isolation. Same words, same meaning, cleaner seams.
- Both sent to him as mp3 for the natural-not-AI judgment, which is his to make and not one I can make by ear.

**Boundaries resolved.** `align/boundaries.json`. Six of seven matched first time; Q2 gi=1 failed because walkthroughs.json says "Like, you have an infection" and the Whisper stream says "Like if you have an infection". Boundary phrases must match WHISPER, not the markdown. All seven now resolve:

| slug | gi | step 2 | step 3 |
|---|---|---|---|
| Q1 | 0 | 4.84s | 11.68s |
| Q1 | 1 | 3.62s | 15.30s |
| Q1 | 2 | 9.42s | 24.56s |
| Q2 | 0 | 25.22s | 6.30s |
| Q2 | 1 | 18.94s | 25.02s |
| Q3 | 0 | 20.16s | 15.96s |
| Q3 | 1 | 5.60s | 22.68s |

Step 2 was 0.38-0.50s in the shipped cut. The flicker is structurally gone.

**Audio rebuilt.** All three OK, 0.02s drift.
- Q1 18 beats, 139.86s (was 138.42s). Step 2 19.3s, step 3 46.3s, 11.7s cut, 6.3s patched in.
- Q2 11 beats, 141.55s (was 134.91s). Step 2 45.1s, step 3 31.4s.
- Q3 11 beats, 109.53s (was 104.04s). Step 2 26.6s, step 3 37.5s, 7.7s cut, 6.5s patched in.

**A drift bug found and fixed.** First rebuild put Q1 0.22s out. Cause: an ffmpeg `-ss/-to` slice lands on a frame boundary, so an emitted piece is never exactly `b-a`, and Q1 splices most (three edits). `slice_src` now MEASURES every piece instead of assuming its nominal length.

**Captions preserved across edits.** A single `srcStart` offset is wrong by the length of the cut for every word after it, and would caption words he no longer says. Beats containing an edit now carry a piecewise `map`, and a patch stretch carries its own text.

**Defects found by check render, not by reasoning:**
1. `stackOn` called `stackLeave(2)` where the beat's `k` belonged. It clamps to 0, so the recall stack was invisible for the ENTIRE recall - the one element that exists to fix his complaint. Fixed, and the stack now holds through the second press and only lets go on the settle.
2. The step label at x=318,y=92 landed in the monitor BEZEL, inches from the app's own "PT105 Section 2 · 1 of 23" header at much the same size. That is the Round 1 rule broken exactly. Moved onto the empty lower half of the page, where the drill draws nothing, so it can only read as floating in front. `place="top"` for The Recall, where the rebuilt argument owns the middle.
3. The stack's fit was a fudge factor assuming 46 characters per line in a 1180px container. Q1's third recall sentence is 291 characters and broke it. Now solved by trying sizes 30 down to 17 and taking the first that fits.

**Confirmed good in the check render:** screen much more centred (monitor centre 654 -> 825 of 1920), stimulus fully readable with no blur, reading light reads as light rather than as a highlighter, "STEP 1 Read it." carries the app's own words in the second person.

**Two more defects found by check render (second pass):**
4. The review beat ran with NO LABEL. `labelOn` required the step's card to have played, and the review deliberately never gets a card, so it could never satisfy the gate. It now shows "Got all of it?" with the cue "Look it over. Nothing is hidden. When you have got all of it, press space." - which states the drill's own principle on screen.
5. The caption bubble at room x=1120 ran off the right of the frame and clipped the text. Moved to x=890: it is 560 wide in room space and the camera sits as far right as +251, so its far edge must stay under room x 1490.

**Caption correctness across the cuts.** A cue is a caption line written against his UNEDITED run, so a cue straddling a cut still contains removed words. Q1 cue 7 is "like a volcano situation. Who knows?" and "like a volcano situation" is exactly what came out. Showing it would caption words nobody says. `build_script` now rewrites any cue overlapping a cut from the word stream and drops cues left empty, emitting `<slug>.cues.instr.json`. Q1: 30 cues -> 29, 4 rebuilt. Q2 and Q3: 0 rebuilt (Q3's edit is a replacement, so its caption comes from the patch text through the beat map, which is correct).

**Framing, measured.** `centringShift` in `quad.ts`. Monitor centre moves from x=654 to x=825 of 1920 at BASE_ZOOM 1.26. NOT fully centred: that needs zoom >= 1.45, where the monitor stands 994px tall in a 1080 frame and the room disappears. The clamp reports its own `shortfall` rather than silently under-delivering.

## Still open after Round 6

- **Full centring needs a new plate.** The monitor sits at plate x 0.34 and no camera move fixes that without eating the room. A new Kling still with the monitor centred costs 19 of his 641 credits. Not done, not asked yet - better shown a frame than described.
- **Seam quality on the two cuts is unverified by ear.** Nobody has listened to the joins at Q1 18.24 and 76.50.
- **The two synthesised lines are unverified by him.** Sent as mp3; his test is "natural, not AI sounding" and it is his call, not mine.
- **His broader authorisation to replace any colouring that lands badly is only partly used.** Four moments were fixed. A full pass over all seven colouring passages against that standard has not been done.
- Deferred from Round 5, unchanged: Kling video plates, stitching the three cuts into one film with bookends, the byte-identical audio on `PT105_S2_Q13`/`Q14` in model_runs, and the RRC grader judging "the spirit of the exercise".


## Shipped (2026-09-10 02:13)

| file | runtime | was |
|---|---|---|
| `projects/video/out/instr-q1.mp4` | 139.93s | 138.50s |
| `projects/video/out/instr-q2.mp4` | 141.59s | 134.91s |
| `projects/video/out/instr-q3.mp4` | 109.59s | 104.04s |

1920x1080 / 30fps, plus `-720.mp4` copies. Durations match their beat scripts to
0.06s. Audio verified present and at level (Q1 mean -29.3 dB / max -5.2 dB;
Q3 mean -28.9 dB / max -4.8 dB).

Also written this round:
- `projects/video/README.md` - Round 6 section: the app-is-the-source rule, the
  nothing-hides rule, the boundary method and its Whisper-vs-markdown trap, the
  centring maths and its zoom cap, the measure-every-piece drift trap, the
  caption-across-cuts trap, and the two defects that type-checked clean and were
  still wrong.
- Memory: `rrc-step-names-live-in-the-app.md`.

Sent to him for the judgments that are his and not mine:
- `Q1_TUNNEL.mp3` and `Q3_ASSUMPTION.mp3` - is the cloned voice natural, not AI.
- `seam1-volcano-cut.mp3`, `seam2-tunnel-patch.mp3`, `seam3-stalactite-cut.mp3`,
  `seam4-q3-assumption.mp3` - are any of the four joins audible.
- All three cuts at 720p.
