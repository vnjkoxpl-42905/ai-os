# Handoff: RRC instructional video

Joshua here. I accidentally ran this in a different chat than I meant to. We are
picking it up in this one. Below is everything that session did, so you have the
full picture without re-deriving it.

Date: 2026-09-09. Source session: `ai-os-9f`.

---

## What the task is

Build an instructional video showing a full Read, Recall, Colour run of 3
questions, with the stimulus rendered exactly as students see it in the runner,
narrated by Joshua's stored model-run recordings, so students understand each
step before they sit the drill.

Full requirements interview is captured at
`brainstorms/2026-09-09-rrc-instructional-video.md`. **Read that first.** It has
every decision, its reasoning, and the flags.

---

## What exists and works

**Remotion project at `projects/video`.** Verified rendering. A 5:24 video was
produced at `out/rrc-walkthrough.mp4` (21.5 MB, 1920x1080, 30fps).

Composition `RRCWalkthrough`: rules card, the real ready beat, PT105.S2 Q1-Q3
with Joshua's real audio, an amber teaching band naming the current step, burned
in captions, and a Report Card outro.

**Setup already done, do not redo:**
- Remotion 4.0.523, Tailwind v4, agent skills in `skills-lock.json`
- `remotion@remotion` Claude Code plugin installed (user scope)
- faster-whisper in `.venv`, word-level alignment for all three MP3s
- The three model-run MP3s downloaded byte-exact to `public/audio/`

**Two machine traps already solved (see `projects/video/README.md`):**
1. `Config.setRspack(true)` emits ZERO JavaScript on this box while exiting 0.
   The resulting `ENOENT ... bundle.js` is a decoy from the source-map reader,
   not the real fault. It is commented out. Do not re-enable.
2. npm blocks install scripts, so esbuild's binary never installed.
   `npm approve-scripts esbuild` fixes it.
3. Render from a built bundle: `npx remotion bundle` then
   `npx remotion render build RRCWalkthrough out/x.mp4`. The default temp-path
   render hits an ENOENT here.

---

## Key findings that took work to establish

**1. The model runs contain steps 1 to 3 plus The Read. They contain NO Recall.**
Verified three independent ways: Whisper transcripts, the stored Deepgram
`transcript_text`, and `walkthrough_md`. Nowhere in any of the three does he say
the whole argument back from memory. Step 4 currently ships as a card that
teaches The Recall rather than demonstrating it.

**2. He groups chunks when he works them.** Recovered from the audio:
- Q1: chunk 1 alone, chunk 2 alone, chunks 3+4 together
- Q2: chunks 1+2 together, chunks 3+4 together
- Q3: chunks 1+2 together, chunk 3 alone
This is ADR 0013 (she chunks freely) visible in his own run. The overlay follows
his grouping, not the authored chunk boundaries.

**3. `walkthrough_md` is the authoritative segmentation.** Blockquoted verbatim
chunk reads, each followed by his rephrase paragraph. Aligning it to the Whisper
word stream with global Needleman-Wunsch gives exact step timings
(Q1 91.7%, Q2 97.1%, Q3 92.0% aligned). An earlier greedy fuzzy anchor drifted
badly. Do not go back to it.

**4. Vocabulary is strict.** From `activity-centre/CONTEXT.md`:
Read (step 1, silent) / Retelling, student label **"Tell it back"** (step 2) /
**Colouring In** (step 3) / **The Recall** (step 4, text gone, graded on
Coverage). **The Read** is NOT a step: it is the analytical takeaway and the
second graded number. Banned in student copy: line, segment, piece, part,
"say it back", takeaway, gist, bullet, beat. **No em dashes, ever.**

**5. Data integrity flag:** `PT105_S2_Q13` and `PT105_S2_Q14` have byte-identical
audio (1672845B) and identical word counts. Almost certainly a duplicate upload.
Not investigated. Separate task.

---

## Verification already passed (18/18)

Per stimulus: chunk text and numbering identical to authored content; chunks
concatenate back to the exact prompt; all Details preserved (24/19/11); timeline
monotonic, non-overlapping, inside audio; every chunk covered exactly once;
caption cues in bounds. Zero em dashes in `src/`. Rendered duration 324.245s vs
predicted 324.20s. Audio confirmed audible in all three questions
(-6.6, -3.1, -5.2 dB peak); cards confirmed silent.

---

## Where it stopped: round 2, unresolved

Joshua reviewed the first cut and asked for five changes:

1. **Step 1 is silent and internal.** v1 reads as "read out loud then react",
   which is not the drill. Reading happens in your head. Then you look away (text
   may stay on screen), rephrase in your own words, then react.
2. A **step indicator on the side** that fades.
3. **The Recall demonstrated, not just taught:** show a spacebar being pressed,
   the screen clearing, then the whole stimulus repeated back from memory out
   loud. He wants a script written and audio made to fit.
4. **Pauses**, with the instruction shown bold before each demonstration.
5. The react step is named **Colouring In**.

### Two things block round 2

**A. The central contradiction, NOT yet resolved.**
His recordings have him reading each chunk **aloud, verbatim**, before
rephrasing. That is what makes the alignment possible. But step 1 is silent. So
the source audio demonstrates the exact behaviour the video must not teach.
Playing his voice reading the text while a caption says "read this in your head"
contradicts itself. Options put to him (he has not answered):
mute the reading and compress to a silent beat; mute but keep real duration;
keep audio and label it a recording artefact; or duck it to a murmur.
**He dismissed the question set. Nothing was changed. Ask him again.**

**B. The Recall audio cannot be produced on this machine.**
Higgsfield is at **0 credits on a free plan**, and there is no ElevenLabs, Azure,
Google or OpenAI TTS key in any `.env`. Already staged and waiting:
- Voice reference cut and uploaded successfully: `recall/voice-ref.mp3`,
  21.9s of clean natural speech from Q1, media_id `9016f3b6-65e5-482e-8efe-6ce518888c68`
- Three Recall scripts written and verified in `recall/scripts.json`, carrying
  52 of 54 Details lexically (the other two are structural, carried by "whereas"
  and "since")
Unblock by topping up credits, adding a TTS key, or Joshua recording the three
himself (about 90 seconds; arguably the best answer for a teaching brand).

---

## Also worth knowing

Separate research this session produced
`wiki/VIDEO-GENERATION-OPTIONS-2026-09-09.md`: Remotion is free for teams of up
to 3, so it costs nothing beyond the Claude Code membership; the official
Remotion MCP is **deprecated** (skills/plugin is the current path); Sora 2's API
shuts down 2026-09-24. Firecrawl research for it cost 4 credits total.
