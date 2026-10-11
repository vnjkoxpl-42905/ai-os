---
name: watch
description: "Inspect sampled video frames alongside captions when the user requests visual video analysis. Transcript-only YouTube requests use the existing free transcript collector."
argument-hint: "<video-url-or-path> [question]"
allowed-tools: Bash, Read, AskUserQuestion
homepage: https://github.com/bradautomates/claude-video
repository: https://github.com/bradautomates/claude-video
author: bradautomates
license: MIT
user-invocable: true
---

## Current AI OS execution contract

For transcript-only YouTube requests use the existing free get_youtube_transcript.py collector first. For visual frame inspection check binaries without requiring an API key, then run watch.py with --no-whisper. Credentials stay in the central .env; do not create ~/.config/watch/.env. Optional external audio transcription requires explicit bounded provider/cost authorization and an approved loader. Preserve output until deletion is expressly authorized.

# /watch — Claude watches a video

You don't have a video input; this skill gives you one. A Python script downloads the video, extracts frames as JPEGs, gets a timestamped transcript (native captions first, then Whisper API as fallback), and prints frame paths. You then `Read` each frame path to see the images and combine them with the transcript to answer the user.

## Step 0: Free local preflight

Resolve this skill's actual directory in the host; use `python` on Windows. Check existing yt-dlp/ffmpeg/ffprobe discovery and the shared Windows toolchain reference before reinstalling. Use the existing free caption collector `system/scripts/get_youtube_transcript.py` for transcript-only requests; inspect its help and reuse saved outputs.

For visual questions, inspect the bundled watch script and run it with `--no-whisper` by default. A missing API key is not a blocker to free captions or frames, and does not authorize an installer or a second credential home. Do not run setup.py's credential scaffold. API fallback is optional only after explicit upload/spend authorization, through privately entered central `.env` credentials loaded without printing values. If the installed script cannot use that loader, report the integration gap; do not put keys in chat, arguments or `~/.config/watch/.env`.

## When to use

- User pastes a video URL (YouTube, Vimeo, X, TikTok, Twitch clip, most yt-dlp-supported sites) and asks about it.
- User points at a local video file (`.mp4`, `.mov`, `.mkv`, `.webm`, etc.) and asks about it.
- User types `/watch <url-or-path> [question]`.

## Recommended limits

- **Best accuracy: videos under 10 minutes.** Frame coverage scales inversely with duration.
- **Hard caps: 100 frames total and 2 fps.** Token cost grows with frame count, so the script targets a frame budget by duration (and never exceeds 2 fps even when the budget would imply more):
  - ≤30s → ~1-2 fps (up to 30 frames)
  - 30s-1min → ~40 frames
  - 1-3min → ~60 frames
  - 3-10min → ~80 frames
  - \>10min → 100 frames, sparsely spaced (warning printed)
- If the user hands you a long video, consider asking whether they want a specific section before burning tokens on a sparse scan.

## How to invoke

**Step 1 — parse the user input.** Separate the video source (URL or path) from any question the user asked. Example: `/watch https://youtu.be/abc what language is this in?` → source = `https://youtu.be/abc`, question = `what language is this in?`.

**Step 2 — run the watch script.** Pass the source verbatim. Do not shell-escape it yourself beyond normal quoting:

```bash
python3 "<verified-skill-directory>/scripts/watch.py" "<source>" --no-whisper
```

Optional flags:
- `--start T` / `--end T` — focus on a section. Accepts `SS`, `MM:SS`, or `HH:MM:SS`. When either is set, fps auto-scales denser (see "Focusing on a section" below).
- `--max-frames N` — lower the cap for tighter token budget (e.g. `--max-frames 40`)
- `--resolution W` — change frame width in px (default 512; bump to 1024 only if the user needs to read on-screen text)
- `--fps F` — override auto-fps (clamped to 2 fps max)
- `--out-dir DIR` — keep working files somewhere specific (default: an auto-generated tmp dir)
- `--whisper groq|openai` — force a specific Whisper backend (default: prefer Groq if both keys exist)
- `--no-whisper` — disable the Whisper fallback entirely (frames-only if no captions)

### Focusing on a section (higher frame rate)

When the user asks about a specific moment — "what happens at the 2 minute mark?", "zoom into 0:45 to 1:00", "the first 10 seconds" — pass `--start` and/or `--end`. The script switches to focused-mode budgets, which are denser than full-video budgets (still capped at 2 fps):

- ≤5s → 2 fps (up to 10 frames)
- 5-15s → 2 fps (up to 30 frames)
- 15-30s → ~2 fps (up to 60 frames)
- 30-60s → ~1.3 fps (up to 80 frames)
- 60-180s → ~0.6 fps (100 frames, capped)

Focused mode is the right call for:
- Any moment/range the user names explicitly ("around 2:30", "the intro", "the last 30 seconds").
- Any video longer than ~10 minutes where the user's question is about a specific part — running focused on the relevant section is far more useful than a sparse scan of the whole thing.
- Re-runs after a full scan didn't have enough detail in some region.

Transcript is auto-filtered to the same range. Frame timestamps are absolute (real video timeline, not offset-from-start).

Examples:
```bash
# Last 10 seconds of a 1 minute video
python3 "${CLAUDE_SKILL_DIR}/scripts/watch.py" video.mp4 --start 50 --end 60 --no-whisper

# Zoom into 2:15 → 2:45 at the 2 fps cap (60 frames)
python3 "${CLAUDE_SKILL_DIR}/scripts/watch.py" "$URL" --start 2:15 --end 2:45 --fps 2 --no-whisper

# From 1h12m to the end of the video
python3 "${CLAUDE_SKILL_DIR}/scripts/watch.py" "$URL" --start 1:12:00 --no-whisper
```

**Step 3 — Read every frame path the script lists.** The Read tool renders JPEGs directly as images for you. Read all frames in a single message (parallel tool calls) so you see them together. The frames are in chronological order with a `t=MM:SS` timestamp so you can align them to the transcript.

**Step 4 — answer the user.** You now have two streams of evidence:
- **Frames** — what's on screen at each timestamp
- **Transcript** — what's said at each timestamp. The report's header shows the source (`captions` = yt-dlp pulled native subs; `whisper (groq)` or `whisper (openai)` = transcribed by API).

If the user asked a specific question, answer it directly citing timestamps. If they didn't ask anything, summarize what happens in the video — structure, key moments, notable visuals, spoken content.

**Step 5 — retain captures.** Preserve the working directory for verification and follow-ups. Delete only after explicit authorization.

## Transcription

The script gets a timestamped transcript in one of two ways:

1. **Native captions (free, preferred).** yt-dlp pulls manual or auto-generated subtitles from the source platform if available.
2. **Whisper API fallback.** If no captions came back (or the source is a local file), the script extracts audio (`ffmpeg -vn -ac 1 -ar 16000 -b:a 64k`, ~0.5 MB/min) and uploads it to whichever Whisper API has a key configured:
   - **Groq** — `whisper-large-v3`. Preferred default: cheaper, faster. Get a key at console.groq.com/keys.
   - **OpenAI** — `whisper-1`. Fallback. Get a key at platform.openai.com/api-keys.

Approved keys live in the central private `.env`; no alternate credential home. Default `--no-whisper` disables paid/upload fallback. Configured keys do not authorize spending or upload; verify the central loader and explicit task/provider limits before an optional fallback.

## Failure modes and handling

- **Missing tool**: verify saved tool paths first; install only a genuinely missing dependency within authorized scope. No credential scaffold or chat key request.
- **No transcript available** → captions missing AND (no Whisper key OR Whisper API failed). Script prints a hint pointing to setup. Proceed frames-only and tell the user.
- **Long video warning printed** → acknowledge it in your answer. Offer to re-run focused on a specific section via `--start`/`--end` rather than a sparse full-video scan.
- **Download fails** → yt-dlp's error goes to stderr. If it's a login-required or region-locked video, tell the user plainly; do not keep retrying.
- **Whisper request fails** → the error is printed to stderr (likely: invalid key, rate limit, or 25 MB upload limit on a very long video). The report will say "none available" for transcript. Retry/switch providers only within explicit upload/spend authorization; otherwise report the failure and keep free outputs.

## Token efficiency

This skill burns tokens primarily on frames. Order of magnitude:
- 80 frames at 512px wide is roughly 50-80k image tokens depending on aspect ratio.
- The transcript is cheap (a few thousand tokens at most for a 10-minute video).
- Bumping `--resolution` to 1024 roughly quadruples the image tokens per frame. Only do it when necessary.

If you already watched a video this session and the user asks a follow-up, do **not** re-run the script — you already have the frames and transcript in context. Just answer from what you have.

## Security & Permissions

**What this skill does:**
- Runs `yt-dlp` locally to download the video and pull native captions when the source supports them (public data; the request goes directly to whatever host the URL points at)
- Runs `ffmpeg` / `ffprobe` locally to extract frames as JPEGs and, when Whisper is needed, a mono 16 kHz audio clip
- Sends the extracted audio clip to Groq's Whisper API (`api.groq.com/openai/v1/audio/transcriptions`) when `GROQ_API_KEY` is set (preferred — cheaper, faster)
- Sends the extracted audio clip to OpenAI's audio transcription API (`api.openai.com/v1/audio/transcriptions`) when `OPENAI_API_KEY` is set and Groq is not, or when `--whisper openai` is forced
- Writes the downloaded video, frames, audio, and an intermediate transcript to a working directory under the system temp dir (or `--out-dir` if specified) so Claude can `Read` them
- Bundled setup has a legacy plugin-local credential scaffold; this AI OS workflow must not run it. Verify central loader compatibility before an authorized API fallback.

**What this skill does NOT do:**
- Does not upload the video itself to any API — only the extracted audio goes out, and only when native captions are missing AND Whisper is not disabled with `--no-whisper`
- Does not access any platform account (no login, no session cookies, no posting)
- Does not share API keys between providers (Groq key only goes to `api.groq.com`, OpenAI key only goes to `api.openai.com`)
- Does not log, cache, or write API keys to stdout, stderr, or output files
- Preserve the task output directory until explicit removal authorization (Step 5); create no duplicate credential store.

**Bundled scripts:** `scripts/watch.py` (entry point), `scripts/download.py` (yt-dlp wrapper), `scripts/frames.py` (ffmpeg frame extraction), `scripts/transcribe.py` (caption selection + Whisper orchestration), `scripts/whisper.py` (Groq / OpenAI clients), `scripts/setup.py` (preflight + installer)

Review scripts before first use to verify behavior.
