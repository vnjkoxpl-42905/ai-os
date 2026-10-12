# Contrapositive video from the most recent clip: Brainstorm / Discovery Notes
Date: 2026-10-12 · Goal: decide what video to make for the Conditional Bootcamp contrapositive lesson, using the most recent thing Joshua clipped. Nothing is generated until Joshua confirms.
Status: in progress (round 1 answered 2026-10-12; length/format and content still open)
Context sources: [wiki/sources/claude-now-does-video-free-javascript.md](../wiki/sources/claude-now-does-video-free-javascript.md), [wiki/VIDEO-GENERATION-OPTIONS-2026-09-09.md](../wiki/VIDEO-GENERATION-OPTIONS-2026-09-09.md), memory `conditional-videos-use-kling`, memory `remotion-rspack-emits-no-js`, `lsatu-conditional-bootcamp/docs/agent/conditional-recovery-20261007/media/necessary-film-20261010.md`

## Facts found (not asked)
- Newest folder in `raw/sources/clips/` is `lsat-lab-conditional-logic-2026-10-11` (LSAT Lab, "Conditional Logic", a competitor's lesson). Next is `herdr-claude-codex-headache`, then `claude-now-does-video-free-javascript` (Chase AI, the JavaScript video method).
- FFmpeg is installed. Playwright is not installed. No ElevenLabs key in `.env`. faster-whisper was used locally on 2026-10-10 for caption checks.
- The lesson already has Kling films (two sufficient-condition clips, one necessary-condition clip). The necessary clip cost 99 of 106 Kling credits on 2026-10-10. Joshua chose Kling over NotebookLM for student-facing conditional videos on 2026-10-02.
- Remotion was recommended on 2026-09-09; it has a known rspack gotcha on this machine.
- The contrapositive page now has a light bulb stage, a flip-and-negate demo and a four-rule drill, all interactive.

## Summary / key decisions
- Placement: a brief lecture video inside the lesson, explaining what a contrapositive is, with dynamic real-time, visually engaging graphics.
- Route: code-rendered (no Kling credits).
- Narration: AI voice.
- Source: not Chase AI by default. Joshua clipped a Nate Herk video (HyperFrames, a HeyGen tool) and wants the two compared before choosing.

## Q&A log
- Q1 (clip): "I recently clipped a Nate Herk source... HyperFrame or something. Compare his version versus Chase AI Methods' version and see which one's better." Clip is `raw/inbox/I Tried 100+ Github Repos for Claude. These 6 Are the Best.md`; HyperFrames segment is 0:24 to 1:28.
- Q2 (purpose): in a lecture, a brief lecture video of what a contrapositive is, dynamic real-time visuals, very visually engaging.
- Q3 (route): code-rendered.
- Q4 (narration): AI voice.

## Open flags (pending input)
- Whether Playwright and a Chromium download may be installed (ask after the route is chosen).
