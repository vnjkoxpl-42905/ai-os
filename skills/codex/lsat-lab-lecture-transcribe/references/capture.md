# Efficient authorized lecture capture

Joshua explicitly authorized a reusable script to retrieve the selected lecture efficiently. The shared project helper is `system/scripts/lsatlab-lecture-capture.py`. Inspect its `--help` before using it; it requires local `yt-dlp` and `ffmpeg`.

```powershell
python system/scripts/lsatlab-lecture-capture.py --video-id 33013 --player-url <OBSERVED-EMBED-URL> --video --normalize-to <lecture-folder>/source-transcript.txt
```

Use only the embedded player URL actually observed in the selected LSAT Lab page. The helper uses the LSAT Lab page as referrer. It does not extract cookies or credentials. It retrieves native English automatic subtitles (`en-x-autogen`), then video-only up to 1080p with 16 concurrent fragments. This language is a tested selection for video 33013, not a promise that every lecture provides it. If unavailable, inspect the supported native captions and adapt the documented helper or use the native transcript UI. Do not invent a transcript or call automatic subtitles audio-verified. Video-only has no audio and is sufficient for board frames; audio verification needs a separately authorized audio route.

Preserved capture lives at `raw/sources/lsat-lab-lectures/<video-id>/`. Existing source captures are reused rather than overwritten. Once the transcript identifies visual milestones, supply a JSON frame plan containing filename/time pairs and run the helper's frame mode:

```powershell
python system/scripts/lsatlab-lecture-capture.py --video-id 33013 --frames <frame-plan.json> --screenshots <lecture-folder>/screenshots
```

The frame plan is a JSON array such as `[{"path":"01-concept-board.png","at_seconds":365}]`. Use a basename and seconds, no remote screenshot URLs. Capture one clear initial board plus complete question text/choices and important board states. Verify frames visually. `frame-times.json` records frame source times and rejects a filename reused for a different timestamp. This is meaningful capture at selected times, not an arbitrary frame sampler.

If authenticated retrieval fails, use the approved browser/native transcript route and report the actual blocker. Do not bypass access or switch to guessed internal media endpoints. Preserve caption confidence and source errors in `coverage.md`.
