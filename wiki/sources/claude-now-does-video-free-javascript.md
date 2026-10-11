---
type: source
subject: Chase AI video, Claude makes videos with JavaScript
created: 2026-10-10
updated: 2026-10-10
aliases: [Claude Now Does Video, JavaScript video pipeline]
tags: [ai-workspace, claude, video, playwright, ffmpeg]
sources: [../../raw/sources/clips/claude-now-does-video-free-javascript/PROVENANCE.md]
---

# Claude writes the video as a function of time, then checks its own frames

Chase AI's video "Claude Now Does Video (FOR FREE) Thanks To JavaScript" ([YouTube](https://www.youtube.com/watch?v=rscb1DgJtNg)) argues that Claude Code can produce finished MP4s with plain JavaScript, with no Remotion, no After Effects and no AI video generator. The full clip transcript was read on 2026-10-10 (13:56 of video, 2,902 words). Publication date is unknown.

Evidence: [archived clip, provenance and hashes](../../raw/sources/clips/claude-now-does-video-free-javascript/PROVENANCE.md). Archived clip SHA-256 `8772757fc82f20e0ef92126026444ac6d2bc115821e61ad6c8805998d85d075a`. A second, rougher caption generation of the same video (`d5bb8d0e…`) remains in `raw/inbox/` and was deliberately not archived or compiled; the provenance file records both.

## What the video claims

All of this is the narrator's account, not verified here.

**The mechanism (0:23 to 2:55).** Claude writes a function that takes a time `t` and returns one picture. The same `t` always gives the same picture, so any frame can be redrawn or checked alone. A headless browser draws 60 frames per second, FFmpeg stitches them into an MP4, and sound is also a function of `t`. The narrator says Claude cannot watch a video but can look at the frames, spot what is wrong, and fix the function. His demonstration video was a one-shot attempt in the style of a Three Blue One Brown explainer, with ElevenLabs narration.

**Level 1, prompting (4:10 to 7:11).** He gave Opus 5.5 one prompt for a 15-second motion-graphics showreel with no skills, at low, high and "ultra code" effort. He reports roughly 20 minutes, 30 minutes and 8 hours, with all three "pretty solid" and ultra best. His conclusion is that weak results are usually a prompt problem, not an effort problem. The one change he recommends is asking for a storyboard first: the scenes are shown as frames before any code runs, which avoids long regenerate loops.

**Level 2, tools and looping (7:11 to 9:35).** The prompt should state length, aspect ratio (full screen or vertical), JavaScript, the soundtrack route, and "render to MP4 with Playwright and FFmpeg". It should end with a check instruction: before calling it done, pull a contact sheet with FFmpeg, look at it, fix what is wrong, re-render, repeat. Audio can come first (supply a narration MP3 and have visuals timed to it) or visuals first. He says Opus 5.5 and Fable 5.1 often do the check unprompted. He prefers ElevenLabs for narration (about five dollars a month, not sponsored) and says open-source narration also exists.

**Level 3, references (9:35 to 11:35).** Give an image to copy a style, or a video to borrow composition. His example fed Claude an Opus 5.5 plus Remotion video about currency and got a JavaScript recreation about the history of electricity, "from the same family of design". Inspiration sources named: skillery.dev (an AI-video category; paid, partly free) and a Twitter creator he calls Kevin.

**Level 4, a skill (11:43 to 13:26).** He packaged the process as a Claude Code skill with seven preloaded styles (cut paper, crosshatch, Rizzoli sketchbook, isometric, and others he does not name in the captions) and custom styles from a reference. Stages: intake questions (subject, format, audio, optional hero character), story, storyboard, then code and delivery, with the Playwright and FFmpeg loop automatic. It installs as a plugin or by handing Claude Code a URL, and it checks prerequisites including Playwright, FFmpeg and faster-whisper, and offers the ElevenLabs connector. He calls it a work in progress and invites pull requests.

**Cost claim.** "It's all code. It's essentially free." The only cost is Claude usage, plus ElevenLabs if used. The video's closing sponsor segment is for his own paid community.

## Limitations of this source

- **Captions, not script.** Names and numbers are heard text. "Ultra code", "Fable 5.1", "skillery.dev" and the effort timings should be checked against the video before anyone quotes them.
- **No skill identity.** The URL for the skill is not in the clip, so its name, repository, licence and contents are unknown. Nothing here lets us assess or install it.
- **Description mismatch.** The clipped blurb belongs to a different Chase AI video; only its timestamps match. See the provenance file.
- **Promotional frame.** The video has a sponsor segment (about 3:24 to 4:10) and a closing plug for the narrator's paid course and "AI OS". "Biggest upgrade" style framing is the channel's, not an independent finding.
- **No evidence shown for the cost and speed claims** beyond his own runs. Eight hours for the best result is a stated cost, not a free one in time.

## How it fits this workspace

This is a dated source claim, captured and read, not yet evaluated or tested here. Status: **captured**.

It does not conflict with the earlier recommendation in [video generation options](../VIDEO-GENERATION-OPTIONS-2026-09-09.md); it adds a second route. That page recommends Remotion driven by Claude Code skills, free for organizations of three or fewer. This video's route drops the framework and renders from plain JavaScript through a headless browser and FFmpeg, and the narrator's own reference video was made with Remotion, so the two are complementary rather than rival. See the dated section added to that page for the comparison and the open tests.

Local prerequisites checked on 2026-10-10 from existing records: FFmpeg is installed ([toolchain](../../references/ai-workspace/windows-cli-toolchain.md)). Playwright and faster-whisper were not checked and are not recorded as installed.

Related: [AI workspace hub](../../references/ai-workspace/index.md), [video generation options](../VIDEO-GENERATION-OPTIONS-2026-09-09.md).
