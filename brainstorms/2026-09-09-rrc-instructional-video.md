# RRC Instructional Video: Brainstorm / Discovery Notes
Date: 2026-09-09 · Goal: Define an instructional video showing a full RRC run of 3 questions, stimulus rendered as students see it, narrated by Joshua's stored model-run recordings.
Status: in progress
Context sources: [[VIDEO-GENERATION-OPTIONS-2026-09-09]], [[RRC-DRILL-AUDIT-CRITIQUE-2026-09-09]], projects/lsatu SectionRunner.tsx, model_runs table

## Summary / key decisions
- Build target: Remotion project at `projects/video` (verified rendering 2026-09-09).
- Source audio: `model_runs` bucket, 714 MP3s, one per stimulus. Joshua doing the drill correctly.

## Q&A log

## Open flags (pending input)
### Q0 - Codebase facts established without asking (2026-09-09)
Read `SectionStage.tsx`, `section.ts`, `SectionRunner.tsx` directly.

- **Only two phases exist:** `working` and `recalling`. There is no third state.
- **During `working` the WHOLE stimulus is on screen**, all chunks rendered in
  order, "with nothing marking one out from another". The app does NOT reveal
  lines one at a time and does NOT track which line she is on
  (ADR 0013: she chunks freely and the app does not track it).
- **During `recalling` the paper stays and the text is removed entirely.**
- **Space is pressed TWICE per stimulus**, not once: "once when you have read it
  all, once when you have given The Recall."
- Footer instruction copy, verbatim:
  - working: "Read it. Tell it back and colour it in as you go."
  - recalling: "Say the whole argument back from memory."
- Key hint copy: working -> "recall full stimulus"; recalling -> "next stimulus"
- Visual contract: mirrors LawHub via `OfficialDrillFrame` - indigo field, white
  header rail, one centred white paper card, stimulus in Fraunces at 19px.
  Header carries a progress rail, a clock, and a REC indicator.
- Ready beat before the run: "Recording now / One take, all the way through, out
  loud." plus a countdown.

### Q1 - Screen fidelity vs teaching the invisible discipline
- Asked: The app shows the whole stimulus at once and never highlights a line.
  How should the video show what she is supposed to be doing internally?
- Captured: **Exact screen + a teaching overlay.** Render the real runner screen
  pixel-accurate (whole stimulus visible, nothing removed), and add a clearly
  distinct overlay layer: a soft highlight on the chunk currently being worked,
  plus a side caption naming the step.
- Decision consequence: the overlay must be *visually unmistakable as
  instruction*, not as UI, or she will expect a highlight in the real drill.
  Treat that as a hard design constraint on the overlay styling.
- Flags: none

### Q2 - Which three stimuli
- Asked: Which three stimuli should the video use?
- Captured: **PT105.S2 Q1, Q2, Q3, in order.** A genuine consecutive run, so
  "a full run" is honest. Q1 is the cave stimulus (~73s, 289 transcript words).
- Note: accepts that PT105.S2's opening is shown to anyone who watches.

### Q3 - How the overlay syncs to his audio
- Asked: Only `transcript_text` is stored, no word timings. How to sync?
- Captured: **Forced-align locally with Whisper** (WhisperX / whisper.cpp) to get
  word-level timestamps, then map spoken words onto the authored chunks.
- Rationale: accurate, automatic, and reusable across all 714 recordings later.
- Flags: local model download + setup time -> me, before build starts.

### Data integrity flag found while measuring durations
- `PT105_S2_Q13` and `PT105_S2_Q14` have **byte-identical audio (1672845B) and
  identical transcript word counts (388)**. Almost certainly a duplicate upload;
  one of the two is probably the wrong recording. -> Joshua / separate task.

### Q4 - The blank recall phase
- Asked: Paper goes blank ~30s per stimulus, ~90s total. What is on screen?
- Captured: **Blank paper (honest) + the authored details listed in the overlay,
  each ticking off the moment he says it.** Dead air becomes the clearest lesson
  on what "carrying the points" means, and it mirrors exactly what the grader
  scores.
- Build consequence: needs detail-level alignment, not just chunk-level. The
  Whisper forced-alignment step must resolve each `details[]` entry to a
  timestamp, which is a fuzzy semantic match (he rephrases), not string match.
  This is the hardest technical piece of the build.

### Q5 - Placement
- Asked: Where will it be watched?
- Captured: **In-app, on the RRC briefing page.** 16:9. Sound on (she is about to
  record herself anyway). Not public, not social, not email - for now.
- Note: the briefing page scored lowest in the 2026-09-09 audit (11/20), so the
  video lands on the surface most in need of it.

### Q6 - Narration
- Asked: Who explains the rules, given the model-run audio is him DOING the drill
  rather than teaching it?
- Captured: **On-screen text only. No new narration.** Silent titled sections
  carry the rules, then his drill audio runs uninterrupted.
- Consequence: all instructional copy is written, not spoken, so it must pass
  [[teaching-voice]] and [[COPY-CORRECTIONS]] before it is rendered.

### Q7 - Captions
- Asked: Burned-in captions on his drill audio?
- Captured: **Yes, throughout.** Word timing comes free from the Whisper
  alignment already required for the overlay.
- Rationale: the journey scored 2/5 on a11y in the 2026-09-09 audit; captions are
  the single biggest fix available on this surface.

### Q8 - Tick-off risk and bookends
- Asked: Fallback if detail-level tick-off is unreliable? And what bookends the run?
- Captured (verbatim): "make sure there is nothing wrong verify make sure and
  verify its done perfectly" / "make sure its done perfectly no mistakes verify
  make sure it's perfected"
- Read: he did NOT pick an option. He set a **standard** and delegated the choice.
  Correctness is the constraint; I choose the means and prove the result.
- Decisions taken on his behalf, in service of that standard:
  - **Tick-off:** chunk-level is the guaranteed floor. Per-detail ticking ships
    ONLY for details whose timing I have verified against the Whisper word
    stream. Any detail that does not verify degrades to its chunk. Nothing
    unverified reaches the screen.
  - **Bookends:** title card with the rules -> the real ready beat (REC +
    countdown) -> Q1, Q2, Q3 -> the Report Card ending. Everything except the
    cold open, because each bookend removes a documented confusion.

## Verification plan (the deliverable is not done until all pass)
1. Stimulus text on screen is string-identical to `model_runs` / content JSON.
2. Chunk splits identical to the authored `chunks[]`; no re-wrapping.
3. Every caption line matches `transcript_text`.
4. Every tick timestamp falls inside the window where the matching words are
   actually spoken, checked against the Whisper word stream. Failures degrade.
5. Rendered duration equals audio duration per stimulus (no drift).
6. Colours/fonts sampled from the real `section.css`, not eyeballed.
7. Watch the rendered MP4 back and confirm frame by frame before he sees it.

## BLOCKER FOUND DURING BUILD (2026-09-09) - The Recall phase is not in the audio

Verified three independent ways: Whisper word-level transcripts of all three
MP3s, the stored Deepgram `transcript_text`, and `walkthrough_md`.

**The model runs contain the WORKING phase only.** The pattern in every one:
read a sentence verbatim -> rephrase it -> colour it in (analysis, analogies,
objections) -> next sentence -> a closing analytical takeaway.

There is **no** "say the whole argument back from memory" restatement anywhere
in any of the three. That is the `recalling` phase, and it does not exist in
this audio.

Evidence, Q1 ends: "So from this we can infer that it wasn't always totally
filled with water because the drops had to form." -> analysis, not recall.
Q3 ends: "sort of an assumed universal goal there." -> analysis, not recall.

This directly blocks the **Q4 decision** (blank paper + details ticking off as he
carries them during the recall). There is no recall audio to tick against.

### Second finding, this one helpful
`walkthrough_md` is already the run segmented exactly as he performed it:
blockquoted verbatim chunk reads, each followed by his rephrase paragraph. It
also shows he **groups chunks** - Q2 quotes chunks 1 and 2 back to back then
gives one rephrase; Q3 the same. This is ADR 0013 (she chunks freely) visible in
his own run. The overlay should follow HIS grouping, not the authored chunk
boundaries, and `walkthrough_md` is the authoritative source for it.
Supersedes the fuzzy audio anchoring I built first.

### Q9 - Resolution of the missing Recall
- Asked: how to handle the missing recall phase?
- Captured (verbatim): "make one wih t hte vice nd make sureti follows what we
  want accoridng ot our criteria"
- Read as: **generate the missing Recall audio in his voice** (clone from his own
  real recordings via seed_audio), scripted to carry the authored Details, and
  hold it to the criteria already agreed.
- Decision I am taking unasked, per his own "say what's actually true" rule: the
  generated Recall carries a **visible on-screen label** marking it a
  demonstration rather than his recording. Students must not believe it is the
  standard he recorded when it is not.

### Vocabulary corrected against the real glossary
`src/features/activity-centre/CONTEXT.md` defines the four steps. My earlier
description was imprecise. Correctly:
1. **Read** - silent reading of a Chunk. 2. **Retelling**, student label
**"Tell it back"**. 3. **Colouring In** - the spoken reaction. 4. **The Recall** -
whole argument from memory, text gone, graded on Coverage.
Separately, **The Read** is NOT a step: it is the analytical takeaway and the
second graded number (`read_given`, `read_matches`, ADR 0025).

**Therefore the precise finding:** his recordings contain steps 1, 2, 3 AND The
Read (the closing analytical takeaway). Only **step 4, The Recall**, is absent.

Banned words for on-screen copy: Line, segment, piece, part (say **Chunk**);
"Say it back" (say **Tell it back**); takeaway/gist/analysis (say **The Read**);
point/fact/bullet (say **Detail**); no em dashes, ever.

## Build log (2026-09-09)

**Alignment.** faster-whisper `small.en`, word timestamps, on all three MP3s.
Whisper vs stored Deepgram agreement: Q1 96.8%, Q2 97.2%, Q3 98.0%. Timings
trustworthy; captions derived from the Whisper word stream.

**Timeline.** First attempt used greedy fuzzy anchoring and drifted (Q1 group 3
matched at 61%, Q2 lost a whole group). Replaced with **global Needleman-Wunsch
alignment** of `walkthrough_md` tokens against the spoken word stream. Result:
Q1 91.7%, Q2 97.1%, Q3 92.0% aligned. Every read span then matched what I had
read manually in the raw transcripts.

His actual grouping, recovered from the audio:
- Q1: chunk 1 alone, chunk 2 alone, chunks 3+4 together
- Q2: chunks 1+2 together, chunks 3+4 together
- Q3: chunks 1+2 together, chunk 3 alone

**Layout law.** First render clipped the app's header rail because the floating
step panel and badge sat on top of it. Fixed by giving the teaching layer its own
96px band across the top; it never overlaps the replicated app now. `Stage.tsx`
carries the rule as a comment.

**Verification run: 18 of 18 passed.**
Per stimulus: chunk text and numbering identical to authored content; chunks
concatenate back to the exact prompt; all Details preserved (24/19/11); timeline
monotonic, non-overlapping and inside the audio; every chunk covered exactly
once; caption cues inside audio bounds.
Copy: **zero em dashes** across `src/`. Only banned-term hit is the string
"Say it back" inside a code comment that exists to forbid it.

**Blocked:** the generated Recall audio. Higgsfield is at 0 credits on a free
plan and there is no ElevenLabs, Azure, Google or OpenAI TTS key anywhere in
the .env files. Voice reference was prepared and uploaded successfully
(21.9s of clean natural speech from Q1, media_id 9016f3b6), and the three Recall
scripts are written and verified to carry 52 of 54 Details lexically (the other
two are structural Details carried by "whereas" and "since"). Everything is
staged; only the generation call failed.

---

# Round 2 (2026-09-09, after first cut reviewed)

## What he said is wrong with v1
1. **The Read is silent and internal.** v1 reads as "read out loud, then react",
   which is not the drill. Step 1 is reading in your head. Then you **look away**
   (the text may stay on screen) and rephrase in your own words, then react.
2. Wants an explicit **step indicator on the side** that fades.
3. Wants **The Recall demonstrated**, not just taught: Space pressed, a spacebar
   shown on screen, the screen clears, then the whole stimulus repeated back
   from memory out loud. Wants a script written and audio made to fit.
4. Wants **pauses**, with the instruction shown bold, then the demonstration.
5. Naming: the react step is **Colouring In**.

## The central conflict I have to resolve with him
His model-run recordings have him **reading each chunk aloud, verbatim**, before
rephrasing. That is how the audio is structured and it is what makes the
alignment possible. But the drill's step 1 is silent. So the source audio
demonstrates the exact behaviour he now says the video must not teach.

---

# Round 3 (2026-09-09) - POV cinematic treatment

## What he asked for, verbatim intent
- Use **Kling** (CLI `@klingai/cli-global@0.2.0`, installed, NOT logged in) for generated video.
- "Maximum capabilities" / "top tier" / "really cool and really realistic".
- **4K**.
- Voice must be "really clear, non-AI sounding".
- **Visually interactive**, not static.
- **POV**: he is looking at the screen like he did; when he looks away, he *had* to
  look away, so it reads as real, not staged.
- An audio/visual effect conveying **"reading in my head"** - you can tell he is
  thinking as he reads.
- **High-end 4K-looking on-screen pop-ups** that tell you what is going on.
- Constraint he stated: free plan, "something like six credits a day".

## Why this resolves the Round 2 central conflict
Round 2 deadlocked: his model-run audio has him reading each chunk ALOUD, but drill
step 1 (The Read) is silent and internal. Treating that audio as **interior
monologue** (POV + "in my head" processing) makes the same audio teach the correct
behaviour. No re-recording needed for steps 1-3.

## Hard constraints found before asking anything
- `kling who_am_i` -> "No login state found (.credentials is missing ACCESS_TOKEN)".
  Cannot read his real model list, resolution ceiling, or credit balance until he
  runs `kling login`. Flagged to him; auth is his to perform.
- Higgsfield remains at 0 credits (Round 2 finding). The "non-AI sounding voice"
  for The Recall is still blocked unless another route is found.
- 4K claim is UNVERIFIED against his actual Kling tier. Free tiers are typically
  720p/1080p. Do not promise 4K until who_am_i confirms it.

## Q&A log (Round 3)

### R3-Q1 - POV framing
- Asked: whose eyes is the camera, and do we ever see him?
- Captured: **True first-person. We never see his face.** Camera IS his eyes:
  monitor in frame, hands/desk edge possible. The look-away is a literal camera
  move - pan off the screen to ceiling or window, then drift back.
- Consequences:
  - No character consistency problem, so free-tier Kling credits go much further.
    No reference-image locking, no retry burn on matching a face across shots.
  - "Thinking" must be carried entirely by camera behaviour, sound design, and
    the popups. There is no face to do that work.
- Constraint stated to him before asking (not a question, a finding):
  **Kling cannot render the stimulus text.** Generative video hallucinates written
  text and it shifts frame to frame. Verification check #1 requires the on-screen
  stimulus be string-identical to the content JSON. Therefore the screen stays
  Remotion and is composited into the Kling plate. Kling supplies room, light,
  body, camera. Remotion supplies every pixel that must be correct.

### R3-Q2 - The "reading in my head" audio treatment
- Asked: what does reading in his head sound like, and how does it differ from
  him talking aloud?
- Captured: **Two-layer, plus a thinking bed.**
  - Verbatim chunk reads -> processed as **interior monologue**: closer, drier,
    quieter, slight low-pass, no room reverb, sitting inside the skull.
  - Rephrase and Colouring In -> **natural, present, in the room.**
  - Under the interior passages only, a **sustained low texture** (bed) that
    **drops out the instant he speaks aloud.**
- Why this works: the switch between the two IS the lesson. The ear hears the
  exact moment reading stops and Telling Back begins. Uses only existing audio,
  zero credits, and resolves the Round 2 conflict with no re-recording.
- Enabled by: the Needleman-Wunsch alignment already built knows, span by span,
  which words are verbatim reads and which are rephrase. That span map drives
  the audio processing automatically.
- Risk I raised and he accepted by choosing this: a pulse/heartbeat bed under a
  timed drill can read as anxiety, which is off-brand for a drill about calm
  processing. **Mitigation to hold myself to: the bed must be a held tone or
  room tone, NOT a heartbeat and NOT a rising pulse.** No tension scoring.

### R3-Q3 - Credit spend and quality bar
- Asked: where do the scarce Kling seconds get spent?
- Captured (verbatim): "I have a lot more credits now. So I want you to use the
  maximum, not maximum but be comfortable and make sure it's very clean and very
  sharp. It's very effective for understanding the exact immersing yourself and
  being able to immerse them to understand what they have to do for each step.
  And very clear. Make sure the voice is not very AI sounding, very natural. The
  internal thoughts, internal mental thoughts. And making clear when they're
  speaking out loud and colouring in."
- Read as: he did NOT pick from the four options. He raised the budget and set a
  STANDARD again (same pattern as R2-Q8). The standard, in priority order:
  1. Clean and sharp.
  2. Immersive, so the student understands exactly what to do at each step.
  3. Very clear.
  4. Voice natural, never AI-sounding.
  5. Unmistakable distinction between internal thought and speaking aloud /
     Colouring In.
- Spend guidance: "be comfortable", not maximum. Generous, not reckless.
- **He asked me to check the credits.**

### Credit check performed 2026-09-09
- **Higgsfield: 0 credits, plan "free".** UNCHANGED from the Round 2 blocker.
  Whatever he topped up, it was not this account.
- **Kling: unknown.** `.credentials` still has no ACCESS_TOKEN, so `who_am_i`
  cannot run. Requires `kling login` (browser OAuth) - his to perform.
- The `KLING_API_KEY` he supplied was added to `.env` but the installed CLI reads
  no API-key env var (verified: only KLING_HOME, KLING_NONINTERACTIVE, DISPLAY,
  WAYLAND_DISPLAY), so it does not substitute for login.

### KEY REALISATION about the "non-AI voice" requirement
Most of this film needs **no synthesis at all**. The interior monologue and the
Colouring In are his OWN recorded voice from `model_runs`. It cannot sound AI
because it is not AI. The requirement is already met for steps 1-3.
**Only The Recall** (step 4, absent from every recording) needs generated voice.
So the Higgsfield 0-credit blocker is narrow: it blocks one scripted passage per
stimulus, not the film.

### Correction from him mid-session (2026-09-09)
"I'm using kling, not Higgsfield." The topped-up credits are on **Kling**.
Higgsfield stays at 0 and is out of scope.
**Consequence:** Kling's tool set is text_to_image / image_to_image /
text_to_video / image_to_video / Elements / motion control. **No TTS.** Kling
credits buy the POV world and nothing for the voice.

### Assets already staged on disk (verified 2026-09-09)
- `projects/video/public/audio/PT105_S2_Q{1,2,3}.mp3` - his real drill audio.
- `projects/video/recall/scripts.json` - the three Recall passages, written,
  verified to carry 52 of 54 Details.
- `projects/video/recall/voice-ref.mp3` - 21.9s clean reference of his speech.

### R3-Q4 - How to get The Recall voice
- Asked: the Recall is the only audio in the film we do not already have. How do
  we get it?
- Captured: **Find another TTS route.** He declined to record it himself.
- Consequence: the Recall stays **synthetic**, so the Round 2 Q9 decision stands
  in full - the generated Recall carries a **visible on-screen label** marking it
  a demonstration, not his recording. Students must not believe it is the
  standard he recorded when it is not.
- Requirement it must still meet: "not very AI sounding, very natural", and it
  must match the voice in the surrounding real audio or the cut will expose it.

### Machine facts probed 2026-09-09 (before offering TTS options)
- Python 3.12.10 present at AppData/Local/Programs/Python/Python312.
- **No NVIDIA GPU** (`nvidia-smi` not found). CPU-only. Fine for ~90s of audio.
- **No TTS key of any kind** in `.env` or `projects/lsatu/.env`.
- Licence flag raised: **Coqui XTTS-v2 is non-commercial (CPML)**. This video
  ships inside a paid product, so XTTS is excluded on licence grounds no matter
  how it sounds. Permissive alternative identified: Chatterbox (MIT).

### R3-Q5 - Which TTS route
- Asked: which TTS route for the three Recall passages?
- Captured: **"Kling first, voice last."** Park the voice entirely. Build the POV
  film with Kling and Remotion, leave silence where the Recall goes, solve the
  voice once we can see how much of the film depends on it.
- Consequence: The Recall is a **known, deliberate hole** in the first cut. Not a
  bug, not to be quietly filled. Every cut before the voice lands must be
  described to him as incomplete at that beat.
- Deferred, still open: ElevenLabs Starter (~$5/mo, best quality, commercial
  licence, needs him to sign up) vs Chatterbox local (MIT, free, CPU, quality a
  step down). -> revisit after first cut.

### R3-Q6 - Where the popups live (resolving a Round 1 vs Round 3 contradiction)
- Contradiction surfaced to him: Round 1 set a HARD constraint that the overlay
  must be unmistakable as instruction and never read as UI (or she expects a
  highlight in the real drill, which does not exist). Round 3 asked for popups
  that are "very real looking, high-end" - which is precisely what triggers the
  Round 1 failure.
- Asked: where do the popups physically live so they look premium without reading
  as app features?
- Captured: **Floating in the room, not on the screen.**
  - Real depth, parallax as the head moves, soft shadows falling on the desk,
    slight defocus when the eye is on the screen.
  - Spatially impossible to mistake for app UI: nothing in the real drill floats
    in your bedroom.
  - Bonus the POV framing unlocks: a popup can hang in space while the camera
    pans off the monitor during a look-away.
- This satisfies both rounds. Round 1's constraint is met by GEOMETRY rather than
  by styling, which is far more robust - it cannot erode as the design gets
  prettier.
- Build consequence: popups are Remotion, composited into the Kling plate with
  matched perspective, shadow direction and depth of field. Camera move data must
  be known so popups track the room correctly. That likely means Kling camera
  moves are chosen to be simple and predictable (a controlled pan), not
  free-roaming, so the overlay can be matched to them.

### R3-Q7 - Whose head are we inside (answered by changing the premise)
- Asked: are we behind Joshua's eyes doing the drill, or the student's about to?
- Captured (verbatim): "need. I don't have- it doesn't have to be my voice, just
  has to be a real human sounding voice you can use the same recording we have
  for the actual RRC drill like the golden template with the voice, we can use
  it. We want to use the script regardless but i just don't wanna make my own
  voice and it should be modified where it fits into the The other thing is I
  want to be able to make sure... ...that it all is very much in sync. The inner
  voice doesn't matter. You can modify her voice if you like slightly but I don't
  need that. It just ultimately has to be something that is very interactive or
  real. My voice is not going to be used. It doesn't matter if you're just
  pretending. We're just pretendin' here. The students will know it's not my
  voice; it's no big deal."
- He did not pick a POV option. He removed a constraint I had been protecting.
- **What is now settled:**
  - His voice is NOT required. Voice identity does not matter.
  - It MUST sound like a real human, not AI.
  - The **script** is used regardless.
  - Authenticity of "this is really Joshua's run" is EXPLICITLY not needed.
    "We're just pretending here." Students knowing it is not his voice is fine.
  - Everything must be **very much in sync** (he stressed this).
  - He referred to a "golden template" recording for the actual RRC drill and
    said we can use it.
  - He said "her voice", which may indicate a female voice / student POV.
- **Consequence for the Round 2 honesty label:** the Round 2 Q9 decision required
  a visible label on generated Recall audio so students would not mistake it for
  his recorded standard. If NO voice in the film is his, that specific confusion
  cannot arise and the label's purpose changes. Do not silently drop it - re-ask.
- **Ambiguity that blocks the build, to resolve next:** does the new voice replace
  the WHOLE film (all four steps, discarding the real model-run audio), or only
  The Recall? These are very different builds.

### "Golden template" - assumption flagged
Searched `projects/lsatu` for a named golden template recording. No such asset
exists; every "golden" hit is unrelated (colour tokens, drill content).
**Assumption: he means the existing `model_runs` audio already staged.** Told him
so rather than acting on it silently. -> correct if wrong.

### R3-Q8 - Re-voice scope
- Asked: how much of the film gets the new voice?
- Captured: **Everything, keeping his exact words.** Re-voice the whole film using
  the transcripts of his real run as the script, verbatim.
- What is kept: his chunking, his rephrasing, his Colouring In, his actual way of
  thinking through a stimulus. Only the vocal identity changes.
- What this buys:
  - **Exact sync.** Generating from known text removes the alignment guess.
    Overlays, popups and tick-offs land on the word, not within 91-97%.
  - One consistent voice across all four steps; the Recall stops being a graft.
  - The existing Needleman-Wunsch alignment is not wasted - it becomes the
    timing map / structural source (his real grouping of chunks).
- Still true: the Recall script is authored (52 of 54 Details) since it never
  existed in the audio.

### R3-Q9 - Who we are behind, and how much body is visible
- Technical fact given to him first: generated video mangles hands. Hands on a
  keyboard mid-frame in 4K is the most reliable failure mode in the medium.
- Asked: who is the person, and how much of them do we see?
- Captured: **Male voice. No hands in frame.**
- Consequences:
  - POV stays closer to the original recording's speaker; his words are not put
    in a woman's mouth.
  - **No body is ever generated.** Eyes move, camera moves, the screen is the
    subject. This removes Kling's worst failure mode entirely and cuts retry
    cost to near zero.
  - The Space press (pressed TWICE per stimulus) cannot be shown physically.
    It must be conveyed by sound plus the screen state change, or by a floating
    popup. -> open design item.
  - Popup copy stays third person / neutral imperative; it is not "her" head.

## HyperFrames Student Kit - review (2026-09-09, at his request)
Location: `projects/hyperframes-student-kit`. 14 skills in `.claude/skills/` and
`.agents/skills/` (not a top-level `skills/`). Installed, tests pass, `.env` empty.

### The one finding that unblocks the voice
`npx hyperframes tts` is **Kokoro-82M**, run locally. Verified `--list` works.
- **Apache-2.0**, so commercial use inside a paid product is fine (unlike XTTS).
- Free, local, no account, no credits, nothing leaves the machine.
- Male voices available: **am_adam, am_michael, bm_george** (54 total upstream).
- Requires `pip install kokoro-onnx soundfile`; installing into a project venv.
- This closes R3-Q5 without ElevenLabs and without him recording anything.
  Voice identity no longer matters (R3-Q7), so cloning is not needed at all.

### Directly relevant skills
- **video-storytelling** - "one persistent world the camera moves through,
  instead of a sequence of separate graphics". This IS the POV concept from
  R3-Q1 and R3-Q6, already written down as a method: camera grammar, the
  spotlight rule, spatial open loops, transcript timing, verification gates.
  Highest-value skill in the kit for this build.
- **hyperframes-video-beats** - plan, time, style and VALIDATE motion beats.
- **style-templates/left-glass-popout** - matches the floating-popup decision.
- **gsap** - easing/stagger/timeline reference for the popup motion.
- **cut-silences / cut-mistakes** - useful later if we ever cut real footage.

### MOTION_PHILOSOPHY.md - adopt the craft, REJECT the pacing
It deconstructs a 30-second payments ad. Its craft vocabulary is excellent and
worth stealing: liquid-glass cards (4-stop gradient + backdrop-filter blur +
inset highlight), grain overlay, vignette, "camera never sleeps", light as the
brand rather than colour, type as a character.
**But its pacing laws are wrong for this film and must not be applied:**
- "One idea per beat, cut fast, avg scene 1.5s" - this film is one sustained
  read of a dense LSAT stimulus. Fast cutting destroys comprehension.
- "Black is the canvas, ~90% near-black" - our hero object is a white paper card
  of body text that must be read. It cannot live in 90% black.
- "Motion blur on every transition" - blurs text.
Adopting those laws would produce a beautiful advert that teaches nothing.
Craft yes, grammar no.

### Kokoro TTS - VERIFIED WORKING 2026-09-09
- `pip install kokoro-onnx soundfile` into
  `projects/hyperframes-student-kit/.venv` (venv, not global Python). Imports OK.
- Invoke with `HYPERFRAMES_PYTHON` pointed at that venv python:
  `HYPERFRAMES_PYTHON=<venv>/Scripts/python.exe npx hyperframes tts "<text>" --voice am_michael --output out.wav`
- First run downloads ~27MB of voice data, then generation is ~10s of speech in
  roughly real time on CPU. No GPU needed.
- Three male samples generated from the real Q1 Recall script and sent to him:
  `projects/video/recall/voice-tests/{am_michael,am_adam,bm_george}.wav`
- **R3-Q5 is now unblocked with a free, local, commercially-licensed route.**
  ElevenLabs is no longer required. Pending: his ear on which voice, or a verdict
  that none of them clear the "not AI sounding" bar.

### DECISION TAKEN (not asked) - renderer and what to borrow from HyperFrames
He delegated "work out which of these skills are worth pulling into the task at
hand", so this is decided, not asked.
- **Remotion stays the renderer.** The existing build is verified 18/18 with
  pixel-accurate app replication. Swapping to HyperFrames' HTML+GSAP engine
  discards that to gain only things we can borrow without switching.
- **Borrowed from the kit:** Kokoro TTS (voice), `video-storytelling` method
  (persistent world / camera grammar / spotlight rule), GSAP easing for popup
  motion, `left-glass-popout` visual language for the floating cards.
- **Rejected:** HyperFrames as renderer; MOTION_PHILOSOPHY pacing laws.

### R3-Q10 - The room
- Asked: what room are we in, and what does he look away to?
- Captured: **Daylight desk beside a window.** Soft natural light, bright window
  just off to the side, monitor as the only screen. The look-away is a pan to the
  window with the outside thrown out of focus.
- Why it also serves the build: soft daylight is what generative video renders
  most convincingly; bright frames survive web compression where dark ones turn
  blocky; "clean and calm" is his first stated standard; and the window gives the
  floating popups real depth to sit in front of.

### R3-Q11 - Look-away choreography
- Framing given to him: during `working` the text STAYS on screen. The app never
  removes it. So looking away is a discipline the student imposes on herself,
  because Telling Back while the words are still in front of you is reading, not
  recall. This is the hardest thing about the drill to teach and POV is the only
  way found so far to show it.
- His real run gives SEVEN such moments (Q1 three chunk groups, Q2 two, Q3 two)
  plus three Recalls where the screen genuinely clears.
- Asked: how many do we film, and at what length?
- Captured: **Full first, compressed after.** The first look-away is the complete
  beat - slow pan to the window, text still visible at the edge of frame as he
  refuses it, a popup naming what he is doing and why. Every later one is a
  shorter drift with no popup.
- Build consequence: only a handful of distinct Kling plates needed. One hero
  look-away plate, one short drift plate, one return plate, reused with different
  timing and grade.

### R3-Q12 - Scope across the three stimuli
- Asked: same treatment for all three, or does the teaching fade?
- Captured: **All three, with the scaffolding fading.**
  - Q1: full POV teaching. Every popup, complete look-away, every step named.
  - Q2: noticeably less.
  - Q3: popups almost gone. A clean run with nothing explaining it.
- Why it is right: the fading scaffold is itself the lesson, since that is how the
  skill has to end up in her hands. It matches the look-away grammar from R3-Q11,
  and front-loads the expensive production into Q1.

### R3-Q13 - Disclosure
- Asked: what does the film disclose about the synthetic voice and the authored
  Recall, and where?
- Captured (verbatim): "never ever disclose anything because they already know
  this. These are my students I talk to them every day they have no need to
  describe or disclose all this. They'll have context. They know me so don't
  complicate it there's nothing needs to be disclosed just keep going"
- **DECIDED: no disclosure anywhere.** No opening line, no Recall marker, no
  persistent badge. This SUPERSEDES the Round 2 Q9 decision, which required a
  visible label on generated Recall audio. That requirement is withdrawn.
- Rationale he gave: the audience is his own students, who he speaks with daily
  and who already have the context.
- Also mentioned: he has "two competitions running for the same task" - i.e. two
  parallel agent sessions on this same video. Noted; not acted on.

## Round 3 - state at end of interview
### Settled
- True first-person POV, never see his face, no hands in frame (R3-Q1, R3-Q9).
- Kling supplies room/light/camera. Remotion supplies every pixel that must be
  correct, because generative video cannot render the stimulus text (R3-Q1).
- Two-layer audio: verbatim reads = interior monologue, rephrase/Colouring In =
  natural in-room, plus a held-tone bed under interior passages only, dropping
  out the instant he speaks aloud. No heartbeat, no rising pulse (R3-Q2).
- Popups float in the room, not on the screen. Round 1's "never read as UI"
  constraint is met by GEOMETRY, not styling (R3-Q6).
- Whole film re-voiced with his exact words from the transcripts. Voice identity
  irrelevant; male voice; sync becomes exact because we generate from known text
  (R3-Q7, R3-Q8, R3-Q9).
- Daylight desk beside a window; look-away is a pan to a defocused window (R3-Q10).
- First look-away in full with a popup, all later ones compressed (R3-Q11).
- All three stimuli, scaffolding fading Q1 -> Q3 (R3-Q12).
- No disclosure of anything (R3-Q13).
- Renderer stays Remotion; borrow Kokoro TTS, video-storytelling method, GSAP
  easing, left-glass-popout look; reject MOTION_PHILOSOPHY pacing (decision).

### Open flags
- **`kling login` -> Joshua.** Hard blocker on all POV footage. Browser OAuth,
  cannot be done from here. Until then his real credit balance, model list and
  the 4K claim are all unverified.
- **Voice pick -> Joshua.** Three samples sent. Default if he does not choose:
  am_michael.
- 4K feasibility unverified, and 4K on an in-app briefing page is heavy for web
  delivery. Revisit once who_am_i is readable.
- How the Space press is conveyed with no hands in frame -> me to design.
- Duplicate audio: PT105_S2_Q13 and Q14 byte-identical -> Joshua, separate task.

## KLING - LOGGED IN AND CAPABILITIES VERIFIED (2026-09-09)
`kling login` completed via browser OAuth. Tokens at `C:\Users\Joshu\.kling\.credentials`.
Persistent - does not need repeating.

### Account
- userId 105315947, membership **VIP / Standard**, **660 credits available**.
- His "six credits a day" estimate was wrong. Budget is real.

### Resolution - 4K IS AVAILABLE (my earlier hedge was wrong, in his favour)
- `kling-video-v3_0` and `kling-video-v3_0_omni`: resolution **['720p','1080p','4k']**,
  and **4k is the DEFAULT**. Both text_to_video and image_to_video.
- `v3_0_turbo`, `v2_5`, `v2_6`, `o1`: 1080p ceiling.
- motion_control: 720p/1080p only.

### Duration
- v3_0 / v3_0_omni / v3_0_turbo: **3-15 seconds** (not the 5s I assumed).
- v2_5 / v2_6: 5 or 10 only. o1 image_to_video: 3-10.

### Aspect
- 16:9 supported natively on text_to_video across the v3 family. Matches the
  in-app 16:9 placement from R2-Q5.

### Image models available for seed stills
kling-image-v3_0 / v3_0_omni / o1 / v2_1, plus gemini-3-pro-image,
gemini-3.1-flash-image, gpt-image-2. 16:9 available on all.

### Chosen generation pipeline (decision)
1. `text_to_image` at 16:9 to author each POV still - cheap, controllable,
   and it fixes composition before any video credit is spent.
2. `image_to_video` with **kling-video-v3_0 at 4k**, duration chosen per plate,
   to add the camera move. Seeding from a locked still is what keeps the room
   identical across plates, which matters because plates are reused (R3-Q11).
3. `query_tasks` to poll, then pull `works[].url`.

### Other CLI facts
- `kling account` gives membership + credits. `kling element_*` creates reusable
  subjects. `motion_control` drives a subject image with a motion video.
- Global `--omni` flag selects the omni family. `--quiet` gives single-line JSON.

## Cross-session handoff received 2026-09-09
A parallel Claude session relayed its state (Joshua confirmed he had two sessions
running on this same task). Everything it reported matches what is already in
this file and on disk. Genuinely NEW facts worth keeping:

### Three machine traps (documented in projects/video/README.md)
1. `Config.setRspack(true)` emits ZERO JavaScript on this machine while exiting 0.
   The resulting "ENOENT ... bundle.js" is a DECOY from the source-map reader, not
   the real fault. It is commented out. Do not re-enable without a real render test.
2. npm blocks install scripts here, so esbuild's binary never installs.
   Fix: `npm approve-scripts esbuild`.
3. Render from a BUILT BUNDLE, not the default temp path:
   `npx remotion bundle` then `npx remotion render build RRCWalkthrough out/x.mp4`.
   The default temp-path render hits ENOENT on this box.

### Existing first cut
`out/rrc-walkthrough.mp4` - 5:24, 1920x1080, 30fps, 21.5 MB. Composition
`RRCWalkthrough`: rules card, real ready beat, Q1-Q3 with his real audio, amber
teaching band, burned-in captions, Report Card outro.
Rendered duration 324.245s vs predicted 324.20s. Audio peaks -6.6 / -3.1 / -5.2 dB.

### Also produced by that session
`wiki/VIDEO-GENERATION-OPTIONS-2026-09-09.md`. Notes Remotion is free for teams up
to 3; the official Remotion MCP is deprecated in favour of the skills/plugin path;
Sora 2's API shuts down 2026-09-24.

### Where it differs from Round 3
That session listed blocker A (read-aloud vs silent step 1) and blocker B (no TTS)
as unresolved. **Both are resolved in Round 3 above:**
- A is resolved by the interior-monologue treatment (R3-Q2) plus the full re-voice
  (R3-Q8). The audio no longer teaches reading aloud; it plays as thought.
- B is resolved by Kokoro TTS, verified working locally (Apache-2.0, free).
Its suggestion that Joshua record the Recall himself was PUT TO HIM and DECLINED
(R3-Q4). Do not re-propose it.

## Hunt for the "golden template" mp4s (2026-09-09)
He said: "stick to the female voice that I have ... with original recording ...
look at the golden template like the mp4s that we have for doing it."

### What I actually found
- **No RRC golden-template mp4 exists anywhere on disk.** Searched the whole user
  profile for mp4/mov/webm named rrc / recall / golden. The ONLY hit is
  `projects/video/out/rrc-walkthrough.mp4`, which is the cut WE rendered (his own
  male voice). 43 mp4s total in the vault; the rest are HyperFrames kit samples
  and LSAT U auth-screen loops.
- **The one real LSAT U instructional video with a female narrator:**
  `projects/lsatu/public/fallacy-flaw/bootcamp-video.mp4`
  5:10.66, 1280x720, h264 + aac, 40.6 MB. Alongside it sits
  `public/fallacy-flaw/bootcamp-audio.mp3` (39 MB), same content.
  Referenced from `src/bootcamps/fallacy-flaw-v2/data/videoAssets.ts:21`.
- **Verified female by measurement**, not by guessing: autocorrelation pitch over
  a 45s sample gives median F0 **190.5 Hz** (10th-90th pct 136.8-290.9 Hz).
  Male speech sits near 85-155 Hz. This is a female voice.
- **Verified it is teaching content**, by transcribing the sample with
  faster-whisper: "...We call these the famous flaws, and they include structural
  errors like causal, necessary versus sufficient, part versus whole, ad hominem,
  and sampling..."
- **No record anywhere of how that narration was produced.** No voice id, no
  service name, no source script, in the repo, the wiki, or the decisions log.
  `wiki/VIDEO-GENERATION-OPTIONS-2026-09-09.md` discusses narration options but
  never says what the fallacy-flaw video used.

### Supabase storage, checked directly (signed in as admin)
- `model-runs`: 714 rows, **every audio_path is .mp3**. No mp4. All his voice.
- `drill-recordings`: 21 files, all `.webm` with mimetype **audio/webm**. These
  are STUDENT recordings of the drill, not templates. Using one would put a real
  student's voice in a published video, which is a consent question, not a
  technical one. Not proposed.
- `external-work-uploads`: 0 files. `message-attachments`: 50 files, no video.

### The blocking unknown
Kokoro CANNOT clone a voice. It has fixed preset voices (including female:
af_heart, af_nova, af_sky, bf_emma, bf_isabella). So "use the female voice I
have" resolves one of three completely different ways:
  1. He means a Kokoro female preset -> free, trivial, do it today.
  2. He means the fallacy-flaw narrator -> need to know what produced her. If it
     was a cloning service we need that account; if it was a person she must
     record; if NotebookLM it cannot be directed to a script.
  3. He means clone her from the existing mp4 -> possible, but needs a paid
     cloning service (ElevenLabs). Kokoro cannot do it.
-> ASKED HIM. Do not guess: option 2 and 3 have real cost and consent shapes.

## Peer session handed over asset paths (2026-09-09) - ALL VERIFIED ON DISK
Every path checked, byte counts and durations match what was claimed:
  out/rrc-walkthrough.mp4      21,557,884 B   324.245s (5:24, 1920x1080, 30fps)
  public/audio/PT105_S2_Q1.mp3  1,171,581 B    94.933s
  public/audio/PT105_S2_Q2.mp3  1,348,101 B   105.067s
  public/audio/PT105_S2_Q3.mp3  1,017,693 B    80.853s
  recall/voice-ref.mp3            351,643 B    21.900s
  recall/scripts.json / align/walkthroughs.json / public/content/{timeline,stimuli}.json
  align/PT105_S2_Q{1,2,3}.words.json + public/content/*.cues.json  all present.

### Clarification worth keeping
`recall/voice-ref.mp3` is NOT generated audio. It is a clip cut from Joshua's own
PT105_S2_Q1.mp3 between 58.0s and 79.9s (21.9s exactly, which matches), chosen
because it is natural speech rather than him reading the stimulus aloud. It was
uploaded to Higgsfield as media_id 9016f3b6-65e5-482e-8efe-6ce518888c68 and the
generation then failed on credits. **No synthetic audio has ever been produced
for this project by any session other than the Kokoro test samples I made today.**

### The peer's two "still unresolved" items are STALE - do not re-ask Joshua
(a) "recordings read chunks ALOUD but step 1 is silent" -> RESOLVED, R3-Q2 and
    R3-Q8. Interior-monologue treatment plus full re-voice. He answered it.
(b) "Recall audio needs Higgsfield credits or a TTS key" -> RESOLVED. Kokoro-82M
    runs locally, free, Apache-2.0, verified working today.
The live open question is different and newer: WHICH female voice he means
(see the golden-template section above). He dismissed that question set and asked
to wait.

---

# Round 4 (2026-09-09) - voice resolved

### R4-Q0 - Which voice (resolved)
- He said: "Use the actual voice I sent you in the mp3. Use that voice. It can be
  a female voice. You can smooth out the language slightly where it's needed to
  fit into what our context is."
- Ambiguity found and put to him: no female mp3 exists anywhere. Verified by
  searching the whole vault. The only speech mp3s are his three model runs, his
  `recall/voice-ref.mp3`, and my six Kokoro test samples. `bootcamp-audio.mp3`
  referenced in COMPREHENSIVEAUDIT.md is GONE from disk; the female narrator now
  exists only inside `fallacy-flaw/bootcamp-video.mp4`.
- **ANSWER: use `projects/video/recall/voice-ref.mp3`.** That is HIS OWN voice,
  21.9s cut from PT105_S2_Q1 between 58.0s and 79.9s.
- So the film is voiced by a CLONE OF HIM. The female-voice thread is closed.
- **Also granted: light language smoothing is allowed** where his verbatim speech
  does not fit the context. This relaxes R3-Q8's "his exact words" to "his words,
  lightly smoothed". First explicit permission to edit the transcript.

### What this reopens
R3-Q8 chose to re-voice the WHOLE film. The reason a Recall-only graft was
rejected in R3-Q8 was that "a different voice appears for one passage per
stimulus, three times, and each switch draws attention". **That objection is dead
now.** If the clone is him, a graft is invisible. So the full re-voice is no
longer forced, and keeping his real recordings is back on the table.
Kokoro CANNOT clone. A cloning engine is required either way.

### R4-Q1 - Clone scope
- Asked: how much of the film gets the cloned voice, now that the clone is him?
- Captured: **Only The Recall. Keep his real recordings for steps 1-3.**
- Reasoning he accepted: his real recording IS him and a clone only approximates
  him, so the real thing wins wherever it exists. The part that genuinely needs
  exact timing is The Recall (Details tick off one by one) and that part is
  generated anyway, so it gets exact sync for free. 90s of synthesis instead of
  4.7 minutes.
- **This reverses R3-Q8.** Full re-voice is abandoned. R3-Q8's rejection of a
  Recall-only graft rested on "a different voice appears three times", which is
  void now that the clone is him.

### R4-Q2 - Recall register (he set a standard instead of answering)
- Asked: should the Recall scripts be roughened so they sound recalled rather
  than read, given his real audio rambles and the authored scripts do not?
- Captured (verbatim): "okay, so I want you to... So when it's reading, it's
  'Reading in his mind' but it should have like a cool effect where it seems like
  he can tell it is internally thinking it. And then he rephrases out loud
  looking away. And it colors it in which is just adding the opinion of the
  person. So it should be very easy to follow. Then you should use your voice to
  be able to do the full recall for the stimulus when its out of sight."
- He did not pick. He restated the flow and set a standard: **"very easy to
  follow."** Same pattern as R2-Q8 and R3-Q3.
- **What he confirmed explicitly:**
  1. Reading is IN HIS MIND, and needs "a cool effect" so you can tell it is
     internal thinking. (He has now said this twice. It is the signature device.)
  2. He then rephrases OUT LOUD, LOOKING AWAY.
  3. Colouring In is defined by him as "adding the opinion of the person".
  4. The whole thing must be VERY EASY TO FOLLOW.
  5. The synthesized voice does the FULL Recall, delivered when the stimulus is
     OUT OF SIGHT.
- **DECISION I am taking from his standard:** keep the Recall scripts CLEAN and
  composed. Do NOT roughen them. Hesitation and self-correction make a passage
  harder to follow, and "very easy to follow" is the stated constraint that
  outranks seam-hiding. The register jump is accepted as honest: The Recall IS a
  different mode, a deliberate graded performance, and sounding more composed
  than thinking-aloud is accurate to the task.

### R4-Q3 - What "reading in his mind" LOOKS like
- Context: R3-Q2 settled what internal reading SOUNDS like. The visual was never
  decided, and he has now named it twice as the signature device.
- Constraint restated to him: Round 1 forbids anything that reads as an app
  feature, because the real drill has no highlighting and she must not expect one.
  So a box or glow around the current Chunk is out.
- Asked: what does reading in his mind look like on screen?
- Captured: **Eye focus. The camera reads, the page defocuses.**
  - The camera micro-drifts along the Chunk being read, the way an eye tracks a
    line.
  - Everything outside that Chunk falls gently out of focus, the way peripheral
    vision genuinely is.
  - The text is NEVER marked, boxed or coloured.
  - When he stops reading and looks away, focus releases and the whole page
    softens at once, so the internal-to-spoken transition is visible as well as
    audible.
- Why this satisfies Round 1: optical effects are properties of the EYE, not the
  interface. Nobody mistakes their own focus for a feature. This is the same
  logic that put the popups in the room: solve it with optics and geometry, not
  with styling.
- Build consequence: the app screen composite must be rendered at enough
  resolution to survive a selective blur without mushing, and the defocus must be
  applied in Remotion to the screen layer, not baked into the Kling plate.

### R4-Q4 - What the viewer watches during Telling Back (he REVERSED R3-Q1)
- Asked: while he speaks with his eyes off the screen, what is the viewer
  watching? Problem raised: that stretch runs 20-40s, happens seven times, and by
  his own rule the screen is not being looked at, so most of the film would be a
  window with a voice over it.
- Captured (verbatim): "I should show his head kind of like looking to the table
  or looking away so it's clear then he goes back. Then he reads the next line
  and then he does this...then he internally reads it and then turns away and
  says out loud. So I should be able to do that make sure its visually very high
  quality, very clear, very real time. So looks very real I'm not sure what you
  mean by details"

- **THIS REVERSES R3-Q1.** R3-Q1 locked "true first-person POV, never see his
  face, no hands in frame". He now wants **his HEAD VISIBLE**, turning to the
  table or away and back, so the look-away is unmistakable.
- Consequences of the reversal, all real:
  1. A PERSON must now be generated and kept consistent across every shot. That
     was the exact cost R3-Q1 avoided. Kling Elements (element_create) exist for
     reusable subjects and are the mechanism for this.
  2. Hands may now appear. Generative video mangles hands. Framing must still
     keep them out.
  3. Lip movement becomes load-bearing: he is SILENT while reading and SPEAKING
     while Telling Back. A generated head whose mouth moves during silent reading
     destroys the whole lesson. This is now the single biggest technical risk in
     the film.
  4. Look-away target may be the TABLE, not only the window (revises R3-Q10).
- He also restated the loop precisely: internally reads a Chunk -> turns away ->
  says it out loud -> back to the screen -> next Chunk.
- Standard restated: "visually very high quality, very clear, very real time, so
  it looks very real."
- **He does not recognise the word "Detail"**, which is the app's own graded
  vocabulary (Coverage counts Details; 24/19/11 across the three stimuli).
  Explained it to him plainly. Watch this: the banned-word list requires "Detail"
  in student copy, but he does not use the term conversationally.

### R4-Q5 - The reversal is WITHDRAWN. True first-person stands.
- Told him the blocking fact: **Kling has no lipsync.** Its tools are
  text_to_image / image_to_image / text_to_video / image_to_video / Elements /
  motion_control. A generated mouth moves on its own schedule, not on his
  recording. And this film needs the mouth COMPLETELY STILL for ~20s of internal
  reading, then moving in time with real speech. A generated face fails both.
- Captured (verbatim): "we should be back to true first person but when
  first-person their eyesight shifts to the side to look away to be able to
  restate it out loud you should be able do that. There's no need for a face
  there should be first person"
- **R3-Q1 STANDS. R4-Q4's reversal is withdrawn.** No face, no head, no hands.
- Two hard problems removed with it: character consistency across plates, and
  lip-sync. Neither is now a risk.
- The look-away is expressed purely as **eyesight shifting to the side**, then
  returning for the next Chunk.

### R4-Q6 - Size of the look-away
- Asked: how far does the eye shift when he looks away to restate, given a full
  turn means 20-40s of empty room, seven times.
- Captured: **A glance off. The screen stays at the edge of frame.**
  - The eye moves off the text but not out of the room.
  - The monitor stays in frame at the side, thrown out of focus, while he restates.
  - Rationale accepted: this is what looking away actually is. You do not swivel
    ninety degrees to think, you unfix your eyes and drift off the words.
- Three things this buys:
  1. The page stays present, so the viewer never loses which stimulus this is.
  2. The refusal stays VISIBLE. The text is right there and going unread, which
     is the lesson.
  3. The middle of the frame is freed for what he is carrying to surface in.
- Combined with R4-Q3 (eye focus), the full grammar of the loop is now settled:
    read internally  -> camera micro-drifts along the Chunk, rest of page soft
    stop reading     -> focus releases, whole page softens
    look away        -> glance off, monitor slides to frame edge, still soft
    restate + colour -> carried content surfaces centre-frame
    return           -> eye comes back, focus re-acquires the next Chunk

### R4-Q7 - What surfaces while he restates (big creative brief)
- Asked: while he restates a Chunk out loud, what surfaces centre-frame?
- Captured (verbatim, condensed to the load-bearing parts): "the word 'detail'
  shouldn't use the word 'Details', it should be more natural. But remember when
  he's looking away, he doesn't see the stimulus so... That should be there but
  after he looks back at his screen it can be like check-check-check It could
  show verification of him hitting all the details with a visual effect ...
  Maximum creative ability to show this So I can really use the 4K ... You can
  animate this process ... And have these 3D effects ... but it should be the
  actual stimulus on the screen like as though it's normal ... the steps
  shouldn't be like oh like a cartoon looking should look like the stuff are
  written in the real world ... as though it's ingrained into video ... I don't
  want to be static images ... you should use a real stimulus in what you see
  there ... you can even have the subtitles be when he's speaking aloud ... you
  see his words coming out on the screen not just like a caption but bubbles or
  something like that ... real life, really hyper lifelike cool effects"

- **DECIDED, and it is a correction of my proposal:**
  1. **The check-off does NOT happen during the look-away.** He cannot see the
     stimulus then, so verifying against it would be dishonest. The verification
     happens **after he looks back at the screen**: check, check, check across
     what he just covered.
  2. Annotations must look **physically present in the scene**, as though written
     into the real world and ingrained in the footage. NOT cartoon. NOT flat
     graphics. NOT static images. This pushes R3-Q6 (popups float in the room)
     further toward true 3D integration with matched light and perspective.
  3. **The stimulus on screen must be the real one, rendered normally.** No
     stylised substitute. This re-confirms the Remotion-composites-the-screen
     decision.
  4. **Spoken words appear as they are said** - not a caption bar. Bubbles or
     similar, emerging in real time as he speaks aloud.
  5. Use the 4K. Maximum creative latitude granted explicitly.

- **CONFLICT TO RESOLVE:** he says do not use the word "Details". But
  `src/features/activity-centre/CONTEXT.md` REQUIRES "Detail" in student copy and
  bans point / fact / bullet. His instruction now contradicts the codified
  vocabulary. Flagged to him rather than picked silently.

### R4-Q8 - Vocabulary in the film
- Conflict put to him: the app's glossary (`activity-centre/CONTEXT.md:86`)
  defines **Detail** and defines Coverage as "How many of a stimulus's Details
  she carried". The grader counts them. His instruction contradicted it.
- Captured (verbatim): "something more natural in the film only is something I
  want you to understand ... It's understanding the spirit of the exercise more
  than anything but use more natural language in the films. Don't use words like
  'details' ... does it sound very clear as to what is expressing to a person who
  has never heard this kind of phrasing?"
- **DECIDED: natural language in the film only.** The app keeps "Detail"
  internally. The film does not say it.
- **The test he set for all film copy:** would this be clear to someone who has
  never heard this phrasing before? That is now the bar for every on-screen word.
- Consequence: this OVERRIDES the CONTEXT.md banned-word list for the FILM's copy
  specifically. His words outrank the project convention. The app is unaffected.
  Note the tension for whoever writes the copy: CONTEXT.md bans point / fact /
  bullet and requires Detail; the film must do the opposite. Do not "fix" the
  film copy back to the glossary later.

### SEPARATE PRODUCT FLAG, not part of this video -> Joshua
He also said: "we wanna make the grading so it's not just like... It counts the
amount of details on top of the fact that it also values the amount or details by
a number ... It's understanding the spirit of the exercise more than anything."
Read as: **the RRC grader should judge whether she understood the spirit of the
stimulus, not only tally Coverage.** That is a change to the grading model in the
app, not to this film. Captured here so it is not lost; NOT actioned.

## HyperFrames kit, second pass - mined for THIS film (2026-09-09, at his request)
He asked me to go through the whole kit, not just the skills, and take anything
useful. Three cards map directly onto three things he asked for by name.

### The key structural insight
Every card is plain HTML + CSS + SVG + GSAP. **Remotion renders HTML.** So we
lift the TECHNIQUES straight into the existing Remotion project and never adopt
the HyperFrames renderer. This is what makes "borrow, don't switch" actually
work, rather than being a compromise.

### 1. His "check-check-check" -> `t2-lb-checkmark.html`
SVG check mark that DRAWS ON via `stroke-dashoffset`, with an SVG glow filter,
followed by a term phrase and a detail line. Transparent overlay, paints over
live footage. Exactly the verification beat he wants when the eye returns to the
screen.

### 2. His "bubbles, words coming out as he speaks" -> `t2-lb-bubble.html`
Glass speech bubble with a pointer tail, scaling up from zero on a `back.out`
spring. This is his "not just like a caption but bubbles" note, already built.

### 3. His "3D, physically real, not cartoon, not static" -> `t2-lt-nameplate3d.html`
This is the important one. The technique:
  perspective: 900px;  perspective-origin: 30% 60%;
  transform-style: preserve-3d;
  transform: rotateX(10deg) rotateY(-7deg);
plus an extruded side-depth edge and a **localized radial bloom behind the
component** (blur(40px), accent colour, its own z-index) rather than a global
glow. The local bloom is the trick that makes an overlay look LIT BY THE SCENE
instead of pasted on top of it. Combined with matched perspective to the Kling
plate, this is how the annotations become "ingrained into the video".

### Also worth taking
- `t1-section-typed.html`, `t1-section-reveal-mask.html`,
  `t1-section-underline-grow.html`, `t1-section-highlight.html`,
  `t1-overview-checklist.html`, `t2-lb-highlightbox.html`, `t2-lb-sticky.html`.
- Two styles exist: `01-vox-explainer` (106 cards) and `02-kallaway` (300).
  Each carries DESIGN.md + style.json + tokens.css. Cards above are kallaway.
- `docs/STORYTELLING-WORKBOOK.md` and the `video-storytelling` skill's
  `reference/design-system.md` for the persistent-world method.

### Still rejected
MOTION_PHILOSOPHY's pacing laws (1.5s cuts, 90% black, motion blur over text).
Craft yes, grammar no. See the first-pass review above.

## VOICE CLONE - VERIFIED WORKING 2026-09-09
**Chatterbox (Resemble AI), MIT licence, local, CPU.** Commercial use is fine,
which is why it beat XTTS-v2 (non-commercial, excluded on licence grounds).

### Setup, reproducible
- Installed into `projects/hyperframes-student-kit/.venv`:
  `pip install chatterbox-tts resemble-perth`
- **Trap 1:** installing chatterbox downgrades numpy to 1.26.4, which BREAKS
  kokoro-onnx (needs >=2.0.2). They cannot share a venv. Kokoro is now moot
  (we clone rather than use presets) but note it before reinstalling Kokoro.
- **Trap 2:** `perth.PerthImplicitWatermarker` imports as **None** on this box,
  so `ChatterboxTTS.from_pretrained()` dies with "'NoneType' object is not
  callable". Fix is to stub it BEFORE importing chatterbox.tts:
      import perth
      if getattr(perth,"PerthImplicitWatermarker",None) is None:
          class _NoWatermark:
              def apply_watermark(self, wav, sample_rate=None, **kw): return wav
          perth.PerthImplicitWatermarker = _NoWatermark
  Skipping the watermark is fine here: his own voice, his own product.
- Reference must be wav: `ffmpeg -i voice-ref.mp3 -ac 1 -ar 24000 voice-ref.wav`
- Runner: `projects/video/recall/clone_test.py`

### Measured performance (CPU, no GPU on this machine)
- Model load: 18.3s. Generation: **171.6s of compute for 6.4s of audio**, about
  27x realtime.
- The full Recall is ~90s of audio, so roughly **40 minutes of background
  compute** for all three. Nothing blocks on it.

### Output
`projects/video/recall/clone-tests/q1_clone.wav` (6.4s, 24kHz) and .mp3.
Sent to him as an A/B against his real reference clip:
https://claude.ai/code/artifact/d0f13075-38d8-498a-a5cb-ac76b1e8228d
-> PENDING his verdict on whether the graft is invisible.
Dials available if close-but-wrong: longer reference than 21.9s, a different
reference passage, or exaggeration/pacing settings.

## Q1 POV CUT BUILT AND RENDERED 2026-09-09
`projects/video/out/pov-q1.mp4` - 92.18s, 1920x1080, 30fps, h264+aac, 30.2 MB.
Composition `POVQ1` in `src/Root.tsx`. The old `RRCWalkthrough` is untouched.

### New files
- `src/pov/quad.ts` - homography -> CSS matrix3d, plus the DETECTED screen quad.
- `src/pov/beats.ts` - the loop as data (read / release / speak / confirm).
- `src/pov/Room.tsx` - plate, camera, monitor composite, optical defocus.
- `src/pov/Float.tsx` - Plate3D / SpeechBubble / CheckLine, kit techniques.
- `src/pov/POVWorking.tsx` - one stimulus in the room.
- `align/treat_audio.py` - the two-layer audio treatment.
- `recall/generate_recall.py` - cloned Recall generation.

### The room
`public/plates/room-v3.png`, 5504x3072, from `gemini-3-pro-image` at 16:9 / 4k.
Three variants generated; v3 chosen for the largest screen area (55% of frame
width), the study context, and the window placed right for the glance-off.

### Screen quad, and the two defects found by rendering
Detected by masking the light low-saturation region:
  TL 0.0712,0.1198  TR 0.6156,0.1839  BR 0.6052,0.7266  BL 0.0752,0.7500
- **Defect 1: composite undersized.** First render showed a grey wedge of the
  original plate down the right edge, widening toward the bottom. The mask stops
  inside the bezel because the screen vignettes at its border. A second detection
  by line-fitting DISAGREED with the first on the bottom edge, so both undershoot.
  Fixed with `OVERSCAN = 1.042`, pushing the quad out from its centroid so the
  composite buries its edge under the bezel. Verified by cropping the edge at
  high magnification: wedge gone.
- **Defect 2: plate edges exposed.** BASE_ZOOM 1.075 was not enough for a 232px
  glance; black bars appeared. The wrapper scales about its centre, so the safe
  translate is (zoom-1)/2*1920. Raised to 1.30. Costs nothing: the plate is
  5504px feeding a 1920px frame.
- Residual: a very thin light line still shows at some camera positions. Minor,
  not fixed, flagged to him rather than hidden.

### Audio treatment, verified
`align/treat_audio.py` splits on the real read spans from timeline.json.
Interior: highpass 95, lowpass 2350, +3.2dB at 220Hz, -4dB at 3kHz, volume 0.72.
Aloud: light early reflection only. Bed: 98Hz + 147Hz held sines, lowpassed to
420Hz, gated ONLY over interior spans with 0.45s/0.40s fades. No pulse.
Q1: 7 spans, 3 interior. Expected 92.12s, got 92.21s.
Render: mean -27.9dB, peak -6.0dB. Audio confirmed present and healthy.

### Cloned Recall audio, all three done
`recall/generated/PT105_S2_Q{1,2,3}.recall.wav` plus per-sentence timing JSON.
Q1 23.5s, Q2 29.4s, Q3 22.4s. Generated sentence by sentence so each piece stays
stable and the timing map falls out for free. NOT yet cut into the film.

### Verified this build
1. Duration 92.18s vs timeline 92.12s.  2. 1920x1080 h264 + aac.
3. Audio present, healthy levels.  4. Composite meets the bezel, no plate showing.
5. No frame edges exposed at full glance.  6. Correct chunk sharp in all three
   groups (checked group 0 at t=3 and group 2 at t=50).

## Q2 AND Q3 BUILT 2026-09-09 - all three POV cuts render
| cut | scaffold | expected | rendered | drift | peak |
|---|---|---|---|---|---|
| pov-q1.mp4 | 2 full | 92.12s | 92.18s | 0.06 | -6.0 dB |
| pov-q2.mp4 | 1 reduced | 102.96s | 103.02s | 0.06 | -5.6 dB |
| pov-q3.mp4 | 0 none | 80.10s | 80.15s | 0.05 | -5.9 dB |
4:35 total. All 1920x1080, 30fps, h264 + aac.

### How the fade is expressed (as data, not three hand-built compositions)
`Scaffold = 0 | 1 | 2` on `POVWorking`, driven from a `POV` array in Root.tsx.
- 2 (Q1): "He carried" label + up to 5 confirmations.
- 1 (Q2): confirmations only, label gone, 3 of them.
- 0 (Q3): no confirm card at all.
**The spoken-word cards do NOT fade.** They double as the captions, and R2-Q7
chose burned-in captions throughout because the journey scored 2/5 on a11y in the
2026-09-09 audit. Removing them in Q3 would regress that deliberately.

### REGRESSION I INTRODUCED AND CAUGHT
Raising BASE_ZOOM from 1.075 to 1.30 (to stop plate edges showing) also pushed
every annotation outward, because they live inside the camera wrapper - correct
behaviour for objects in a room, but I only re-verified the `speak` frame after
that change, not `confirm`. Result: the confirm card ran off the right edge in
BOTH Q1 and Q2. Q1's earlier good-looking still had been rendered at the OLD zoom.
Fix: anchors must satisfy `frameX = 960 + (roomX - 960) * 1.30 < ~1900`.
  SpeechBubble  x 1268 -> 1120, w 620 -> 560   (frame 1168..1896)
  Confirm card  x 1246 -> 1105, w 540 -> 500   (frame 1148..1798)
**Lesson for this build: after any camera change, re-verify EVERY phase, not the
one that motivated the change.**

### Kling video-plate findings, VERIFIED against the live declaration
The design workflow flagged these; I checked them against `who_am_i` rather than
trusting the agent. Both true, and both caught before any credit was spent:
- **`prefer_multi_shots` defaults to `true`** on kling-video-v3_0 image_to_video.
  Left alone the model cuts to an invented second shot mid-clip, which would
  destroy room continuity and the perspective-stable monitor. **Always pass false.**
- **`first_image` must be a URL returned by `file_upload`.** No local paths, no
  external URLs. The agent also claims seed stills must be BELOW 4K; our
  room-v3.png is 5504x3072, above it, so a downscaled seed will be needed. That
  specific claim is NOT yet verified against the live text.
- image_to_video on v3_0 has NO aspect_ratio argument; aspect comes from the seed.

### Still not built
The Recall beat. Audio exists for all three (`recall/generated/*.wav`), but the
picture needs its own design: Space pressed with no hands in frame, the page
clearing, and the whole argument given back to a blank screen.

---

# Round 5 (2026-09-09) - after the three POV cuts were reviewed

## What he said is wrong with them
Verbatim: "it needs to label the steps for reading ... its not clear this
internally going in their head it sounds like they are reading out loud we need
to make it more clear and have it be step 1: Reading step 2: Rephrase (look away)
and rephrasing step 3: Colouring In should pause and say now colouring in and
then introduces the colouring in and then i want you to have it where it has them
pressing space bar and making a concise restatement of the whole argument from
top to bottom with the stimulus disappearing after pressing space bar and show
should slow down and have them do that concisely and properly in her voice should
have moments, pauses, and being clear what is happening here but it is close this
is an instructional video"

## The six changes
1. **LABEL THE STEPS ON SCREEN.** Step 1: Reading. Step 2: Rephrase (look away).
   Step 3: Colouring In.
2. **The interior treatment is not reading as internal.** It still sounds like
   reading out loud. The single most important fix.
3. **PAUSE and introduce each step before demonstrating it.** "Now colouring in",
   then the demonstration. This is Round 2 request #4, which was never built.
4. **Build the Recall beat.** Space bar pressed, stimulus disappears, concise
   restatement of the whole argument top to bottom.
5. **Slow down.** Moments, pauses, clarity about what is happening.
6. "This is an instructional video." Teaching clarity outranks cinematic purity.

## What this reverses
**R3-Q12's scaffolding fade is now wrong, at least for labelling.** He wants the
steps named explicitly, which is the opposite of "by Q3 nothing explains it".
Surfaced to him rather than silently applied.

## Structural consequence I must design around
Inserting pauses means the film is no longer the same length as his recording.
The audio must FREEZE while an instructional beat plays, then resume. The film
stops being a continuous playback of his run and becomes a run with instruction
cut into it. That is what he is asking for and it is a real architecture change.

## Open ambiguity, NOT resolved
He said the Recall should be done "in her voice". R4-Q0 settled the voice as
`recall/voice-ref.mp3`, which is HIS voice, and the Recall audio is already
generated as a clone of him. "Her" may be a speech-to-text artifact or may mean
he wants a female voice after all. -> ASK. Do not assume.

### R5-Q1 - Pause pattern
- Asked: how often does the film stop to introduce a step, given pausing every
  time is nine stops in Q1 alone?
- Captured: **Full stop on first encounter, label thereafter.**
  - First time each step appears: picture holds, his audio pauses, a card names
    the step and says what is about to happen.
  - After all three are introduced: the loop runs without stopping, with a small
    step label in the room updating through Reading / Tell it back / Colouring In.
  - Three real teaching stops in Q1, none after. Labelling never goes away.

### R5-Q2 - What silent reading SOUNDS like
- Told him why the current cut fails: the source IS him reading at full voice, and
  filtering cannot turn projected speech into thought. The processing was too
  polite (lowpass 2350, volume 0.72).
- Captured: **Actual silence. Mute the reading completely.**
  - Step 1 is silent, so the soundtrack is silent.
  - The picture carries it: eye tracking the line, page defocused, bed alone.
  - Accepted risk: Q1 group 2 reads for 13.86s, which is a long silent hold.
- **Bonus this preserves:** the read spans keep their real duration, so the viewer
  watches the eye take exactly the time he took. The reading PACE becomes visible
  teaching content rather than dead air.
- Build consequence: the held-tone bed now carries those stretches alone, so its
  level and movement matter much more than when it sat under a voice.

### R5-Q3 - The step labels
- Conflict raised: he said "Rephrase", but the app glossary says Retelling with
  the student-facing label "Tell it back", and the app footer VISIBLE ON THE
  MONITOR IN THE SAME SHOT reads "Read it. Tell it back and colour it in as you
  go." R4-Q8 allowed natural language in the film, but that was about passing
  prose; these are labelled headings she will read three times.
- Captured: **Reading / Tell it back / Colouring In.**
- One vocabulary across the whole product. "Tell it back" is also plainer English
  than "Rephrase", so nothing is lost in clarity.
- **This narrows R4-Q8:** the film still avoids "Detail", but the STEP NAMES now
  follow the app exactly. Do not drift them back to "Rephrase".

### R5-Q4 - The Recall voice
- Asked: he said "in her voice"; which voice?
- Captured: **The clone of him, already generated.** "Her" was a speech-to-text
  slip. R4-Q0 stands. `recall/generated/PT105_S2_Q{1,2,3}.recall.wav` are used
  as-is. Nothing to redo.

### R5-Q5 - What the screen shows during The Recall
- Captured (verbatim): "it should do the exact the same thing as the drill where
  the stimulus goes away and it is the screen with the stimulus disappeared and
  they have to say full stimulus"
- **DECIDED: exact drill fidelity. Nothing added.**
  - Paper stays, text removed entirely (the app's real `recalling` state).
  - Footer: "Say the whole argument back from memory." Key hint: "next stimulus".
  - NO ghosting the text back, NO floating cards, NO coverage meter.
- He chose fidelity over decoration. My ghost-the-text-back idea is rejected.
- The step LABEL still applies (he wants steps named), and the Recall gets an
  introduction card like the other three, since it is its first encounter.

### Space press, decided by me (he delegated means)
No hands are in frame, so the press is carried by three things at once:
1. The app's OWN footer `Space` key chip depressing. It is already in the real
   screen, so this is honest rather than invented furniture.
2. A key thunk in the sound design.
3. The screen state change from working to recalling.
A brief frame-wide blink sells the eye, but the chip is the load-bearing part.

## Build architecture for Round 5
Inserting pauses means picture and audio must stay locked, so the AUDIO is
rebuilt with the instructional holds baked in as silence, and the same script
emits the picture timeline. One source of truth, no drift:
  - read spans      -> SILENCE (R5-Q2), real duration preserved
  - instruction holds -> inserted silence, picture holds
  - speak spans     -> his real audio, untouched
  - recall          -> the cloned passage appended after the Space press

## ROUND 5 BUILD - the instructional cut (2026-09-10)
New compositions `InstrQ1` / `InstrQ2` / `InstrQ3`. The Round 4 POV cuts stay
registered as POVQ1-3 for comparison.

### One script drives picture AND audio
`align/build_script.py` emits BOTH `public/audio/<slug>.instr.mp3` and
`public/content/<slug>.script.json` from the same pass, so they cannot drift.
Beat kinds: card / read / release / speak / press / recall / settle.
Each spoken beat carries `srcStart`, mapping it back onto the ORIGINAL recording
so the caption cues still resolve after teaching beats are cut into the timeline.
That mattered: in Q1 the Colouring In card sits BETWEEN release and speak, so a
single per-group offset would have been wrong.

| cut | beats | was | now | teaching added |
|---|---|---|---|---|
| Q1 | 16 (4 cards) | 92.12s | 138.42s | +46.3s |
| Q2 | 9 (0 cards) | 102.96s | 134.86s | +31.9s |
| Q3 | 9 (0 cards) | 80.10s | 104.00s | +23.9s |
Q1 audio is 0.15s longer than the script: mp3 encoder padding, landing in the
trailing `settle` silence. Picture is cut to the SCRIPT, not the mp3.

### Reading is now genuinely silent
His voice is muted across every read span and the span keeps its real duration.
The held-tone bed carries those stretches alone, so its level was raised
(0.075 / 0.030 from 0.055 / 0.022) with 0.55s/0.5s fades.

### THREE FRAMING BUGS, all the same root cause
Everything inside the camera wrapper is scaled by the zoom, so anchors are in
ROOM space, not frame space: `frameX = 960 + (roomX - 960) * zoom`.
1. Confirm card ran off the right edge after zoom went 1.075 -> 1.30. (Round 4.)
2. **The zoom itself was cropping the monitor.** At 1.30 the app's left edge sat
   at -111, cutting off its own footer instruction "Read it. Tell it back and
   colour it in as you go". In an instructional film, cropping the thing being
   read is the wrong trade.
3. Step label at x=132 mapped to frame -116 and was entirely off screen.
**Fix: BASE_ZOOM 1.30 -> 1.12, GLANCE_X 232 -> 96, GLANCE_Y 46 -> 26, drift 9 -> 6.**
Monitor now spans frame 37..1218, fully visible. Safe translate at 1.12 is 115,
clearing a 96px glance plus 6px drift. The glance is smaller and still reads,
because the monitor visibly slides out of the reading position.

### Two smaller fixes
- `Plate3D` gained a `flow` mode. Instruction cards are NOT objects in the room,
  they are the film stopping to talk, so they lay out in normal flow and let a
  flex parent centre them. Absolute positioning had pinned the first card to the
  top-left corner, half off frame.
- The step label washed out completely over the white paper card. It now carries
  a dark backing (rgba(9,11,26,0.82)) rather than relying on glass.

### The Space press, built
`Screen` gained a `pressed` prop, 0..1, that depresses the app's OWN Space chip
with an inset shadow and a 1.6px translate. No hands are needed and nothing is
invented: the chip is really in the drill's footer. The stimulus clears at
k > 0.55 of the press beat and the footer switches to "Say the whole argument
back from memory." / "next stimulus", which is the real recalling state.

## ROUND 5 DELIVERED 2026-09-10
`out/instr-q{1,2,3}.mp4` plus 720p copies for phone delivery.
| cut | script | render | drift | peak | teaching stops |
|---|---|---|---|---|---|
| Q1 | 138.42s | 138.50s | 0.08 | -5.3 dB | 4 |
| Q2 | 134.86s | 134.91s | 0.05 | -5.1 dB | 0 |
| Q3 | 104.00s | 104.04s | 0.04 | -4.8 dB | 0 |
All 1920x1080 / 30fps. 6:17 total.

### Late fix, caught by checking a crop rather than trusting the render
The Recall beat inherited the glance-RETURN camera, which left the frame panned
~33px left and cropped the first word off the app's own footer: it read "the
whole argument back from memory." with "Say" missing. During The Recall he is
facing a blank screen, not glancing off one, so the loop camera does not apply.
Fix: `Room` gained an optional `cam` override and `CAM_NEUTRAL`; the press,
recall, settle and card beats all use it. Verified by cropping the footer band
out of the finished mp4 and reading it: "Say the whole argument back from
memory." now complete.
**Method note: the first re-render LOOKED done (files present, plausible mtimes)
but was the previous pass. Checking the pixels, not the file listing, is what
caught it.**

### Open, for his review
- Step 2 is labelled "Tell it back" (the app's word), not "Rephrase" (his word).
  Flagged to him; one line to change if he disagrees.
- R3-Q12's scaffolding fade now only governs the confirm card, since labelling is
  present throughout. Q2 and Q3 carry no teaching stops at all.
- The Recall audio is the clone of him and lands with no introduction in Q2/Q3.
