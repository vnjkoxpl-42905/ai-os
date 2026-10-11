# Compare visual behavior against imported current styles

Reconstructed design reference, 2026-10-11. The missing historical `intro-to-lr-design.md` is not reproduced here. Values below are observed local source tokens, not a claim of approved live rendering or a new redesign instruction.

## Current imported styling wins over abandoned defaults

[Application `src/index.css`](../../ai-os-projects/lsatu/src/index.css) imports [Main Conclusion `styles/scoped.css`](../../ai-os-projects/lsatu/src/bootcamps/main-conclusion/styles/scoped.css). The `.mc-bootcamp` wrapper scopes that implementation to the bootcamp. Check the actual current import and component overrides on every audit.

| Token family | Observed scoped values |
|---|---|
| Surfaces | `--bg: 245 242 237` cream; `--bg-2: 250 247 239`; `--surface: 255 255 255` white |
| Ink | `--ink: 26 26 26`, with softer opacity variants |
| Brand | `--accent: 232 208 139` gold; restrained selection/action emphasis |
| Argument roles | Conclusion green `16 185 129`; premise blue `96 165 250`; pivot orange `249 115 22`; opposing purple `168 85 247`; concession yellow `250 204 21`; background slate `148 163 184` |
| Main type | Inter/system sans, body `14px`, line height `1.6` |
| Lesson prose | Georgia/Times serif, `15px`, line height `1.7`, measure `64ch` |
| Spacing | `4, 8, 12, 16, 24, 32, 48, 64px` token steps |
| Corners | Current scoped `--r-2`, `--r-3`, `--r-5`, `--r-8` are `2px` |
| Motion | `150, 180, 220ms`, eased; reduced-motion rule sets these durations to `0ms` |

**Known source conflict:** [legacy `tokens.css`](../../ai-os-projects/lsatu/src/bootcamps/main-conclusion/styles/tokens.css) declares dark navy surfaces and rounded corners. Its old standalone defaults must not be used to revert the currently imported cream scoped design. Component-level CSS may further override tokens; inspect the rendered surface before declaring a mismatch.

## What to compare

- Whether role colors retain their meaning, and text remains readable without relying solely on color.
- Whether prose, feedback and controls support the learning step rather than compete with it.
- Whether focus, disabled/loading/error states, reduced motion and small-screen layouts work in the actual rendered target.
- Whether deviations are deliberate topic-specific choices or accidental inherited styles. Equivalent function and legibility can justify a difference.

Use [the teaching standard](lsat-teaching-voice-standard.md) for instructional voice. Preserve source typography as evidence; it does not override Joshua's current instructions. CSS inspection establishes source values only. Live visual/accessibility acceptance requires a browser check.
