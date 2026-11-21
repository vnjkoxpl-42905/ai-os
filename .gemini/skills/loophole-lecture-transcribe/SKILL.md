---
name: loophole-lecture-transcribe
description: Automatically transcribe, screenshot, and adapt Loophole Online video lessons into verbatim transcripts, teleprompter scripts, and structured concept routers in the Loophole Lecture archive.
---

# Loophole Lecture Transcribe

Automate the full intake and educational adaptation of Loophole Online training videos into the `Loophole Lecture/` archive. This skill coordinates Edge browser automation, transcript harvesting, visual whiteboard capture, broadcast teleprompter drafting, and two-tier router indexing.

## When to Use

Activate this skill when Joshua says:
- "Transcribe this Loophole video" / "Transcribe the whole video"
- "Create a Loophole lecture for [topic]"
- "Turn this video into a teleprompter script"
- "Take screenshots of the whiteboard and attach timestamps"
- "Add this lesson to the Loophole Lecture archive"

## Standard Directory Architecture

Every ingested video follows the structured schema:
```text
Loophole Lecture/
├── README.md                            <- Master Router (all topics)
└── <Topic Name>/                        <- Concept Subfolder (e.g. Sufficient Assumption)
    ├── README.md                        <- Subfolder Router
    ├── <slug>-transcript.md             <- Verbatim transcript with embedded images
    ├── <slug>-teleprompter.md           <- Read-aloud teleprompter script with visual cues
    └── images/                          <- Timestamped frame captures
        ├── 00-00-player-overview.png
        └── 00-05-whiteboard-prompt.png
```

## Step-by-Step Execution Protocol

### Step 1: Connect to Active Edge Tab
Locate the open lesson tab in Microsoft Edge over CDP:
```powershell
node .gemini/skills/edge-live-control/scripts/edge-control.mjs tabs
```
Ensure the target lesson URL is active on the tab.

### Step 2: Harvest Video Timeline and Transcripts
Extract video duration, current playback position, closed captions, and the on-page transcript element:
```powershell
node .gemini/skills/edge-live-control/scripts/edge-control.mjs video --match "loophole"
node .gemini/skills/edge-live-control/scripts/edge-control.mjs inspect --match "loophole" --selector "[data-testid='transcript'], .transcript-container, main"
```

### Step 3: Capture Key Visual Milestones
Seek the video to core visual inflection points and capture screenshots into `Loophole Lecture/<Topic>/images/`:
```powershell
node .gemini/skills/edge-live-control/scripts/edge-control.mjs screenshot --match "loophole" --out "Loophole Lecture/<Topic>/images/00-00-player.png"
```

### Step 4: Generate Verbatim Transcript Markdown
Create `<slug>-transcript.md`:
- Frontmatter containing title, runtime, instructor, platform, source URL, and linked practice drills.
- Chunked chronological sections with exact timestamp ranges (`[MM:SS - MM:SS]`).
- Inline links to corresponding whiteboard frame captures (`![Label](images/filename.png)`).
- Visual margin commentary describing what is written on the digital whiteboard.

### Step 5: Draft Spoken Teleprompter Script
Create `<slug>-teleprompter.md`:
- Written in Joshua's authoritative, conversational teaching voice (from `wiki/teaching-voice.md`).
- Formatted in natural breath-length paragraphs for live reading.
- Explicit visual production cues:
  - `[PRODUCTION CUE: INSERT WHITEBOARD IMAGE -> images/... / SHOW EQUATION]`
  - `[PAUSE]`
  - `[EMPHASIZE: KEY RULE]`
- Strictly adheres to voice guardrails: zero em-dashes and no AI-slop vocabulary.

### Step 6: Maintain Two-Tier Router Indexing
1. Write `Loophole Lecture/<Topic>/README.md`:
   - Summarize the topic's logical rules and formal mechanisms.
   - Catalog all transcript, teleprompter, and image files in the subfolder.
2. Update `Loophole Lecture/README.md`:
   - Register the topic in the master navigation table.
   - Verify all markdown links resolve accurately.


## Codex browser and efficient native-caption capture (2026-10-14)

When the user specifies Codex browser, bind that exact tab using cua_repl, rather than the Edge CDP helpers. Enumerate the rendered sidebar video links, preserve their order and titles, and read only the video source and track attributes from the DOM. Open Toggle transcript and preserve all rendered segments in source.json. Never scan unrelated iframes or authentication state.

For a batch, make a user-named folder with one sanitized exact-title subfolder per video. The Python helper system/scripts/loophole-day-one-capture.py consumes browser-observed source.json files, downloads native VTT and media with three concurrent workers, extracts original audio and sampled frames, and records provenance and SHA-256. Its Day One path is currently fixed; change ROOT for another batch. Signed media URLs are temporary and should not be copied into chat or published.

Prefer unchanged native captions over retranscription. Label automatic captions accurately, check final cue times against media duration, and keep correction notes separate until checked against audio. Download success does not establish word accuracy. Preserve the original instructor voice. Only produce a Joshua teleprompter adaptation when requested.


### Capture written notes separately

For every video, inspect the full Ellen's Notes section below the player. Save its exact innerText in ellens-notes.txt and HTML in ellens-notes.html, including nested lists, emphasis, and links. Include it in source.json and the per-lesson index. When absent, record notes-status.txt. Written notes and spoken captions are different sources; never use one as a substitute for the other. Capture the whole notes container, including content below the initial viewport. The Python helper now accepts an archive directory argument, e.g. python system/scripts/loophole-day-one-capture.py "Loophole Lecture/Day Two".

### Written interactive Bootcamps

For a requested Bootcamp capture, follow `system/scripts/loophole-bootcamp-browser-capture.md` and use its CUA helper. Preserve each question, choices, diagrams, confirmed correct answer, and original response commentary. Save transient hints immediately; revisiting an answered question may hide them. Keep earlier evidence as a supplement. Use small resumable batches, preserve diagram image bytes, and record gated external stimuli explicitly. The helper changes attempt scores and progress, so use it only within the user's authorization to work through the drills. Package the source with `system/scripts/package-loophole-bootcamps.py`; do not produce a Joshua adaptation unless requested.

### Compare and complete a conditional source collection

Compare only the saved Loophole source library with the live Concept Review, relevant Prep Map objectives across all five stages, and the directly linked homework. Do not compare with Joshua's curriculum unless requested. Preserve the before-state and distinguish substantive transcripts, notes-only captures, and navigation links. A link to a lesson is not the lesson body.

Use `system/scripts/loophole-lecture-browser-capture.mjs` through the selected CUA tab for native media/track attributes, the full rendered transcript, exact written notes and any book-excerpt panel. Lecture-attached **Video Bootcamp** quizzes are separate from Book Extras Bootcamps. Capture them with `system/scripts/loophole-inline-bootcamp-capture.mjs`, including confirmed responses and transient commentary. Wait for the selected answer marker to match the submitted choice before attributing feedback; label historical mismatches unverified.

Process observed source records with `system/scripts/loophole-conditional-capture.py`. Verify original video/audio, native captions, sampled diagram frames and supplement coverage separately. Native captions and rendered transcript groups can have different counts and wording; counts alone do not establish missing speech. Use actual media duration and caption endings to check cutoff. Never claim word-level listening verification without performing it.

### Named RC activity demonstrations

For Decaf, Cappuccino, Caffeinated and related activity demos, first inventory the named training blocks and compare actual local video/audio/caption bytes with saved SHA-256 manifests. Do not infer a missing ignored media file from `rg --files`; check its exact path. Reuse complete existing packages, preserve a fresh verification snapshot separately, and capture missing sources with the CUA lecture helper. Keep generic RC theory separate from demonstrations; include related named review activities only when within the requested scope.

The earlier native-media packager supports a new batch: `py system/scripts/loophole-conditional-capture.py "Loophole Lecture/<batch>" --inventory "raw/sources/<batch>/target-lectures.json" --title "<batch title>" --allow-missing-supplements`. This option verifies the downloaded demonstration media while leaving uncaptured inline quizzes explicitly incomplete; never call those quizzes captured or absent. Inspect actual downloaded frames, compare caption tails with measured media duration, and preserve original captions without claiming word-level listening verification.
