# Making videos from Claude Code: the options, priced

Date: 2026-09-09. Method: five Firecrawl `agent` jobs (spark-1-pro) plus two
developer-index searches. All figures are from official pricing/licence pages
retrieved on this date and are cited below. Related: [[tasks]], [[hot]].

## The recommendation

**Remotion, driven by Claude Code through Remotion's own agent skills.** For a
solo operator it is free, including commercial use and automated local
rendering, so it costs nothing beyond the Claude Code membership. That was the
constraint, and it is the only serious option that meets it.

Install path:

```bash
npx create-video@latest
npx remotion skills add
```

There is also an official Claude Code plugin: `remotion-dev/claude-code-plugin`.
The older official Remotion MCP is **deprecated** — the docs say not to use it
for new installs. Skills/plugin is the current path.

## Why Remotion and not the alternatives

| Option | Licence | Cost for a solo operator | LLM fit |
|---|---|---|---|
| **Remotion** 4.0.523 | Source-available, proprietary | **Free** (orgs ≤3 people, all features, unlimited commercial use) | Excellent — official Claude Code skills + plugin |
| Revideo 0.11.0 | MIT | Free | Good, plain TypeScript, but no narration layer |
| Manim / ManimGL | MIT | Free | Good for math/diagram animation only |

The Remotion licence has a trap worth knowing even though it does not bite you:
organizations of **4 or more people** need a Company License, and the
"Automators" tier ($0.01/render, **$100/month minimum**) covers batch rendering,
prompt-to-video apps, and automated video products. At your size the Free
License covers all of it. If Aspiring Attorneys ever passes three people, that
changes — it is a headcount trigger, not a usage trigger. Verify the terms
yourself before relying on it commercially; this is a licence, not a spec.

## Working pipelines other people have built

- **`runesleo/claude-video-kit`** (MIT, 119 stars) — closest to your use case. A
  JSON script becomes a 1080x1920 explainer MP4 via one `render.sh`: TTS,
  Whisper-aligned captions, Remotion slides.
- **`Bhonar/docs-to-video`** — MCP extracts a page, a Claude Code skill writes the
  scenes, ElevenLabs narrates with real word timestamps, Remotion renders.
  Strongest repository evidence of the four.
- **`Agents365-ai/video-podcast-maker`** (MIT, 1.6k stars) — script-driven 4K
  narrated video, local Edge/Azure TTS, CI smoke-render.
- **`itsjwill/vanta`** (MIT) — voice cloning + WhisperX word-accurate captions.
- **`Yusuke710/manim-skill`** — Claude Code skill: plan, write Manim, render,
  watch it, iterate.

## The narration question

You do not need a TTS vendor. `model_runs` already holds **714 recordings of you
doing the drill**, 713 transcribed with word timings. For RRC videos the
narration is already recorded, in your own voice, and Remotion can lay
transcript-timed captions against it.

You also already have an ElevenLabs-family MCP connected in this session
(`generate_audio`, `create_voice`, `generate_video`, `shorts_studio`) if you want
synthetic narration for scripts you have not recorded.

## If you ever want generated footage instead of rendered graphics

Cheapest per finished minute, API rates as of 2026-09-09:

| Model | Rate | Per finished minute | Audio | Max clip |
|---|---|---|---|---|
| **Veo 3.1 Lite** 720p | $0.05/sec | **$3.00** | Yes | 8s |
| Veo 3.1 Fast 720p | $0.10/sec | $6.00 | Yes | 8s |
| Sora 2 Standard 720p | $0.10/sec | $6.00 | Yes | 20s |
| Veo 3.1 Standard | $0.40/sec | $24.00 | Yes | 8s |

**Sora 2's API is deprecated and scheduled to shut down 2026-09-24.** Do not
build on it.

Avatar/talking-head, if you ever want a synthetic you on camera:

| Vendor | Price/min | Custom avatar of yourself |
|---|---|---|
| HeyGen Avatar III | $1.00 | Yes on web plans; **API digital twin is Enterprise only** |
| Synthesia Starter | ~$1.90 | Yes, 3 personal avatars |
| Argil Classic | ~$4.16 | Yes |
| Captions.ai Mirage | $9.00 | Yes |

For teaching content none of this beats screen-rendered graphics plus your real
voice. Generated footage is for atmosphere, not instruction.

## Added 2026-10-10: a second free route, plain JavaScript with no framework

Source claim, not tested here. Chase AI's video ([summary](sources/claude-now-does-video-free-javascript.md))
says Claude Code can skip Remotion entirely. Claude writes one function that
turns a time `t` into a picture, Playwright's headless browser draws each frame,
and FFmpeg stitches 60 frames per second into an MP4. Claude then reviews an
FFmpeg contact sheet of frames and fixes the function until it looks right.
Sound is code or a supplied narration file.

How it compares with the recommendation above:

| | Remotion route (above) | Plain JavaScript route (2026-10-10 source) |
|---|---|---|
| Framework | Remotion 4.x, official skills and plugin | None; headless browser plus FFmpeg |
| Cost claim | Free for organizations of three or fewer, per the pricing page checked 2026-09-09 | "Essentially free"; Claude usage only, per the narrator |
| Licence question | Headcount trigger at four people | None stated in the source; not checked |
| Evidence | Official docs, pricing page, several repositories | One creator's demonstration; no repository or skill URL in the clip |
| Overlap | | The narrator made his own reference video with Remotion and used it as a style reference, so he treats the two as compatible |

Workflow ideas in the source that apply to either route and cost nothing to
adopt: ask for a storyboard of scene frames before any code runs; state length,
aspect ratio and audio route in the prompt; end the prompt with "pull a contact
sheet, look at it, fix, re-render, repeat"; supply narration first and time the
visuals to it. The narrator reports one 15-second showreel took about 20 minutes
at low effort, 30 at high, and 8 hours at the highest setting, with little
quality difference between low and high. Those timings are his, unverified.

Open and untested: whether Playwright is installed here (only FFmpeg is recorded
in the [toolchain note](../references/ai-workspace/windows-cli-toolchain.md)),
whether the plain route beats Remotion on a real RRC or conditional lesson, and
the name and source of the skill he distributes. Nothing was installed or
changed by ingesting the clip.

## Sources

remotion.dev/docs/license/pricing · remotion.dev/docs/ai/coding-agents ·
github.com/remotion-dev/claude-code-plugin · ai.google.dev/gemini-api/docs/pricing
· developers.openai.com/api/docs/pricing · heygen.com/api-pricing ·
synthesia.io/pricing · docs.argil.ai/resources/api-pricings
