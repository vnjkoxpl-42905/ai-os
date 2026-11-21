# Refined studio

Local preview: http://127.0.0.1:5192/06-refined-studio/

Built from04 and the user's saved HTML attachment.04,05 and the attachment are preserved. Neutral near-white/charcoal, Newsreader and Manrope remain the visual foundation. Slate accents are confined to controls and small reference marks.

## What changed

- Original layered paper sculpture, rendered with CSS3D and a brief GSAP settling motion. Pointer parallax only on hover-capable devices. Responsive scale belongs to its outer wrapper, so resizing remains correct.
- Raised progress folio within the charcoal resumed-work card, stronger type hierarchy and aligned assignment rows.
- Inset reference console with LR/RC segmented controls, readable numbered fields, indexed original sample slips and saved/recent browsing.
- Exact practice counts and answer strips, plus an actionable sample revisit rather than an invented trend.
- Three visual passes: initial material/layout treatment; structural console/sculpture revision; legibility and alignment. Final pass applies independent Claude Opus5.5 findings.

## Verification

Playwright with installed Microsoft Edge. Actual screenshots were opened and inspected for desktop, tablet and phone, including question console and natural motion start/settled frames.

- Final1440,768,390: zero page errors and zero horizontal overflow (`artifacts/pass-final-report.json`).320 and1024 also zero overflow after a narrow-card fix.
- `artifacts/verify.cjs`: filters, type cascade, unsupported-reference honesty, answer selection/hint/correct feedback, bookmark persistence, keyboard calendar, session-note persistence, mobile menu, natural GSAP motion and reduced-motion zero tweens.
- `artifacts/edge.cjs`: Ctrl+K, empty search, focus restoration, failed storage write notice and bookmark rollback. Native search Escape clears an entered query before a subsequent Escape closes the dialog, so focus restoration is tested with an empty query.
- `artifacts/regression.cjs`: selecting an assignment no longer mutates the resumed task; Friday agenda consistently returns to Negation Station. Responsive sculpture wrapper verified after resizing the existing page.

Final evidence: `artifacts/final-desktop.png`, `final-hero.png`, `final-tablet-hero.png`, `pass-final-390.png`, `question-phone.png`.

## Independent review dispositions

Claude Opus5.5 review lives in ai-os/research/2026-10-24-neutral-studio-review/round1. Addressed high-severity resumed-task corruption; GSAP/CSS transform conflict; tablet sculpture overlap; incorrect navigation targets; inconsistent assignment date; variable-font range declarations; row arrow alignment; small labels and mobile score alignment. The brief original sculpture entrance is intentionally retained for the user's motion request, with a static reduced-motion equivalent. Decorative reference watermark is retained but remains secondary. No claim of unconditional Claude approval.

## Limits

Local interactive visual prototype, not production. Questions are three original demonstration examples, never official PrepTest material. Unsupported references show an honest unavailable state. Recent results and dates are sample content. Continue/assignment/practice panels preview workflows; full live drills are not connected. No external or production writes.

No ReactBits implementation was copied. Its skill/pattern guidance was considered; the sculpture and interaction code are original vanilla CSS/JS suited to this existing prototype. GSAP is the existing local runtime. Existing font licenses remain in fonts/.
