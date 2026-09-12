# RRC Instructional Video, Round 8: text written in the air
Date: 2026-09-11 · Goal: replace the dark slabs (intro card, speech bubbles, recall stack, placard) with text that is written in the air, lifelike, at the 4K effect budget; add blinks where they are natural.
Status: shipped 2026-09-11 (Round 7 one PR away)
Context: [[2026-09-10-rrc-instructional-video-round7]] (the shipped version, tagged `r7-shipped` in `projects/video`)

## His brief (2026-09-11, voice, decoded)

Verbatim: "change the bezel to be more realistic, with a 4k sleek hyper use of maximum effects. Use the Hyperframe skill and blinking where it's natural. The exposure lift is good, and the blink is cool. Show me the best you can do. It should be very lifelike and real, rather than just a block. It should be almost written in the air, with some cool effects, but don't mess up. We've got a perfect version and might stick with it."

Answers to the carried open items:
- 175 Kling credits: spent, accepted. Further generation allowed if needed. (None needed this round; everything here is DOM and CSS.)
- Exposure lift: keep. Blink: keep, and add more where natural.
- 40 deg turn: not mentioned; kept.
- Audio seams / synthesised lines: still unanswered.

## What "the bezel" means (my reading, stated so it can be corrected)
The frames at 3 s, 17 s and 128 s of the Q1 cut show dark rounded slabs with a lit rim: the Step 1 intro card looks like a tablet with a bezel, the bubbles and recall lines are black blocks. "Rather than just a block ... almost written in the air" points at those. The monitor's own bezel sliver at the left edge when turned is real plate pixels and is left alone.

## Decisions (my call under the Round 7 Q4 licence)
- **No boxes anywhere.** Every room card becomes light-written type: crisp warm-white face, dark diffuse ink halo for legibility over the window, a soft cast glow on the room behind it, and a faint local shade that has no edges. Nothing that reads as a panel.
- **Written as spoken.** Bubble text appears word by word across the cue's real duration (the cue files carry phrase start/end; words are spread evenly inside a phrase). A small point of light travels each word as it forms: the pen. The previous phrase lifts and dissolves as the next writes in.
- **Recall lines** are the same material, stacked; older lines recede (dimmer, slightly smaller, softer). Counter is small tracked caps with a hairline, not a badge.
- **Intro cards** (Q1): "STEP n" in tracked caps with a hairline that draws in, the step name in Fraunces at display size written in the air, the cue line under it in Helvetica. Same anchor, same half-turn.
- **Placard** on the desk: same type, no glass.
- **"Look Away"** keeps its chrome face and gets the pen light and a once-only shimmer so the material matches.
- **Effects, each tied to something real:** pen light (writing), focus pull on entry (blur 10px to 0, letters settle), shimmer sweep once after a line lands (light moving on a surface), motes drifting in the window light near the type (dust in a sunbeam, seeded PRNG, deterministic), a slow float on holds (the type hangs, it is not pinned).
- **Blinks:** gaze-shift blink on the turn-away (existing) AND on the turn-back; periodic natural blinks on holds, first at ~3.5 s into a hold then every 4.5 to 7 s (seeded jitter), fast (2 frames down, 4 up), never inside the last 1.5 s before a move and never during the Space presses.
- No Kling spend. No plate change. Head turn untouched.

## Build log
(appended as it happens)

**2026-09-11 ~03:10 Round 7 checkpointed.** `projects/video` committed as `8283e29`, tag `r7-shipped` (build/ and the 408 MB of plate frames now ignored; the first attempt swept them in and was redone). `git checkout r7-shipped` brings the shipped films' source back exactly.

**03:15-03:50 Built.**
- `src/pov/Air.tsx` (new): `AirLine` / `AirWord` / `AirLabel` / `Pen` / `Motes`. Two-layer letters (under-copy carries the ink halo and a 3-step body; face is a light gradient clipped to the glyphs, since Chrome paints text-shadow over a clipped fill). Word progress is a pure function of seconds-since-start, so a phrase writes across its real cue duration.
- `Cards.tsx` rewritten: Bubble / Placard / IntroCard on Air, no glass. `RecallRoom.tsx` rewritten: lines on Air, older lines recede. `LookAway.tsx`: pen light per word, focus pull, one sweep of light after landing.
- `headState.ts`: `blinkTimes` / `naturalBlink` (schedule from the move list). `HeadRoom.tsx`: `blinkExtra` prop; gaze blink now on the turn-back too.
- `POVInstructional.tsx`: bubble driven by `since`/`write` from the cue's real start and length; previous phrase rendered with `leave` for 0.5 s; blink schedule wired; presses quiet.
- Placement corrected from the camera model (probe: monitor right edge x 1631 facing, 1318 half-turned): `PLACARD` theta 23.6 / 0.14 m, `CARD` theta 27.2 / 0.36 m, `RECALL` phi 7.5. Lesson: at 0.98 m one plane px is ~1.9 frame px, so placard type is set at 25 px, not 36.
- Q1 blink schedule (verified by script): 15 natural blinks, none within 1.5 s of a move, none in a press beat, plus 8 gaze-shift blinks.
- Stills at 3 / 17 / 62 / 101.5 / 128 s checked: nothing over the screen, nothing clipped, legible over the lit window.

**~04:30 Comparison and the timing decision.** Side-by-side frames at 3 / 17 / 30 / 62 / 128 s (left R7, right R8) in `out/r8/compare/`. He asked for a comparison, then said decide, perfect it, push it in. Decision: a phrase writes in under a second (`writeFor` = 0.35 s + 0.045 s/word, cap 0.9 s), not across the whole cue. Writing across the cue meant the last words of a long phrase landed as the voice finished them, so the full line was never readable at once. Shade deepened to 0.56 for legibility over the window. Previous phrase still leaves over 0.5 s, including across cue gaps.

**~05:00-11:30 4K render.** `out/r8/render4k.cmd`, launched detached (PowerShell `Start-Process cmd.exe`; a Bash tool call dies at the 10-minute limit). Masters `out/r8/instr-q{1,2,3}-4k.mp4` at 139.9 / 141.6 / 109.6 s, 720p copies beside them. `tsc --noEmit` clean; eslint clean on touched files (2 pre-existing errors in untouched `POVWorking.tsx`, `RecallStack.tsx`).

**~11:40 Source on GitHub.** Private repo `vnjkoxpl-42905/lsatu-films`. `main` = Round 8 (`6357e00`) on top of Round 7 (`451a803`, tag `r7-shipped-pub`). History filtered: `*.wav`, `*.npy`, `audio/work/`, `align/_tmp/`, `build/`, `public/plates/r7/seq/` ignored. Full local history kept on branch `local-full` (tag `r7-shipped` = `8283e29`, Round 8 = `f1de718`).

**~12:00 Shipped.** App worktree `projects/lsatu-wt-rrc-demos`, branch `feat/rrc-demos-round8`, PR #122 squash-merged to main as `6836bdb` (six files under `public/rrc-demos/`, no code change). Lovable `deploy_project` deployment `d0ecbeb4`. Verified 12:06 by full GET: `https://lsatprep.study/rrc-demos/rrc-demo-pt105-s2-q{1,2,3}.mp4` return 200 with `x-deployment-id: d0ecbeb4` and 36,382,871 / 37,121,022 / 25,787,844 bytes, identical to the new encodes. (The CDN sends no content-length on HEAD; use a full GET.)

**Not verified:** the theatre playing the new films in a signed-in browser (dev pane redirected to `/auth`; the page component is unchanged since verified 02:12); mobile layout; his verdict in motion.

**Rollback:** in the lsatu repo, `git checkout 9b6b51c -- public/rrc-demos` on a fresh branch, PR, merge, `deploy_project`. Round 7 films come back exactly.

**Still open:** Q1_TUNNEL.mp3 / Q3_ASSUMPTION.mp3 naturalness and the four audio seams (never answered); Q3 720p copy not sent to him (`out/r8/instr-q3-720.mp4`).

**~12:40 Second-pass verification and audit.** Signed-in DOM check in his Chrome: the theatre on /activities/sections references the Round 8 src and poster, three chapters, nine tab stops. All three live files decode in Chrome at 1920x1080 (139.93 / 141.59 / 109.59 s) and play continuously. Frames from the shipped bytes at 17.5 / 30 / 62 / 101.5 / 128 s (Q1) and 80 s (Q3): air text, no slabs, previous phrase dissolving behind the next. NOT seen: the theatre in motion while signed in (his Chrome tab was hidden behind Pinterest; Chrome defers media in a tab never shown; his window was not brought forward).

**Finding, P0, predates Round 8:** lsatprep.study (Cloudflare in front of Lovable's origin) answers every `Range` request with `200` and the whole file, no `Accept-Ranges`, no `Cache-Control`, for the mp4s, the jpgs and the JS bundle alike. Chrome therefore reports `video.seekable [0,0]`: the theatre's scrubber and arrow keys are silent no-ops in production, and nothing is cached between visits. Apple requires byte-range support for iOS media, so iPhone playback is at risk (not tested on a device). Playback itself is fine: moov precedes mdat in all three files, 0.3 s to first byte. Fix: a public Supabase Storage bucket and a repoint of `src`/`poster` in `read-recall-colour-section.demos.ts`. His decision.

**Impeccable audit of the page: 14/20.** Findings and the recommended order live in [[tasks]] Next. Progress board: https://claude.ai/code/artifact/88636536-9e3c-40ac-bb02-1d99ec221dc4
