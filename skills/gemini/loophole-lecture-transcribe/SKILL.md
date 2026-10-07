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
