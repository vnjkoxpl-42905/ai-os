---
type: teaching-notes
subject: Handoff prompt paste this verbatim into Claude Code
updated: 2026-07-17
aliases: []
---

# Handoff prompt — paste this verbatim into Claude Code

Below is the full copy-paste block. Open Claude Code in your project directory, paste the entire fenced block (the lines between the triple backticks) as one message, and Claude Code will read the spec, ask the few questions it needs answered, and start the build.

---

## ⬇ Copy this entire block ⬇

````
You are building Main Conclusion v1.0 — a Logical Reasoning learning app for the LSAT, focused entirely on the Main Conclusion question type. The build is production-grade, voice-led, top-tier modern UI.

=== READ FIRST (in this order) ===

1. /Users/joshuaf/Documents/Claude/02_PROJECTS/lsat-u/Curriculum/Main Conclusion/_export_2026-04-29/README.md
2. /Users/joshuaf/Documents/Claude/02_PROJECTS/lsat-u/Curriculum/Main Conclusion/_export_2026-04-29/rules/voice_calibration.md     (INVIOLABLE — voice + content preservation)
3. /Users/joshuaf/Documents/Claude/02_PROJECTS/lsat-u/Curriculum/Main Conclusion/_export_2026-04-29/rules/pedagogical_flow.md     (INVIOLABLE — teach first, never cold-test)
4. /Users/joshuaf/Documents/Claude/02_PROJECTS/lsat-u/Curriculum/Main Conclusion/_export_2026-04-29/rules/named_tools_lexicon.md  (15 named tools — preserve verbatim)
5. /Users/joshuaf/Documents/Claude/02_PROJECTS/lsat-u/Curriculum/Main Conclusion/_export_2026-04-29/spec.html                     (the full spec — content, components, design tokens, premium polish bar)

The spec at #5 is the source of truth. §M1-M6 is the content layer (port verbatim, do not paraphrase). §3.1-§3.8 is the design system. The Feature Strategist appendix has the v1.0 / v1.0.5 release plan tile near the top — that locks scope.

=== V1.0 SCOPE (locked) ===

1. The 6 modules from spec §M1-M6:
   - M1 Lessons (12 sequenced lessons + capstone calibration drill at 1.13)
   - M2 Reference (10 sections including the 6-category Indicator Vault + Quick Reference Card)
   - M3 Drills (9 stratified drills with the recommended drill-order roadmap)
   - M4 Question Simulator + Trap Master (8 sections including all 7 traits with PT examples)
   - M5 Reading Hard Sentences (7 sections + capstone at 5.8)
   - M6 Diagnostics + AI Tutor + Progress (10 sections; AI Tutor is STUB MODE in v1.0)

2. Stage-Gate Tracker as the universal drill wrapper. Architectural template: the local prototype source at /Users/joshuaf/Documents/Claude/02_PROJECTS/lsat-u/Curriculum/Netlify/index (4).html (this scored S/100% on the audit — read it as the codebase reference).

3. End-of-module calibration drills at Lessons 1.13 and §5.8. Pull questions from the user's existing PT bank (see #4). Show Coach's Note + trait tag on every wrong answer.

4. External PT-question-bank integration. The user has an existing PT question bank already set up. Ask the user for: endpoint URL, auth method (API key / bearer token / etc.), sample request, question schema (stimulus + 5 answer choices + correct answer + metadata), trait-tagging convention, rate limits, CORS status. Do NOT proceed with calibration drill construction until those answers come in.

5. Concept search — unified knowledge index across all modules. Use lunr.js or fuse.js (~10KB, client-side). Index lesson titles, named tools, indicator words, trait names. Persistent search input in the top bar.

6. Re-do mode with hindsight. On every wrong-answer Coach's Note, a "Re-attempt with explanation visible" button. Re-attempt scores don't count toward accuracy but DO count toward mastery (correct re-do tags the trait as "recovered").

7. R&R Drill — DESKTOP with live mic via MediaRecorder API, ONE CONTINUOUS recording across the full LR section, audio stored in IndexedDB, Web Speech API transcription, TEMPLATED diff highlighting only (Left Out and Added flagged via word-overlap; Mischaracterized NOT auto-flagged in v1.0; student reviews manually). NO LLM call in v1.0.

8. AI Tutor (§6.8) in STUB MODE — templated responses anchored to existing spec content. Routing layer over the app's own corpus:
   - "Why is B the answer?" → pull the question's Coach's Note inline
   - "What does FABS mean?" → jump to Reference §2.C
   - "What's a Trojan Horse?" → jump to Lesson 1.8 + Reference §2.I
   - "What should I work on next?" → templated recommendation from §6.4 decision tree
   - "Did I replace the pronoun right?" → run §6.5 templated rules
   Suggested-question chips in the drawer. Free-text input falls back to "Try one of these instead" when no template matches. NO LLM call in v1.0.

9. Diagnostic dashboard (§6.3-6.4) — accuracy by mechanic + by trait. Recommendation engine fed by post-instruction calibration data only.

10. WCAG 2.1 AA compliance per §3.7 audit (color contrast, keyboard nav, screen reader semantics, reduced-motion, color-never-only-signal).

11. Persistence abstraction layer — REQUIRED. App code talks to a `Persistence` interface (TypeScript signature defined in spec §6.9). NEVER call localStorage / IndexedDB directly anywhere in the codebase. Ship `LocalStoragePersistence` implementation in v1.0. R&R audio blobs go to IndexedDB (localStorage quota too small). Schema uses UUIDs + ISO 8601 + typed records (tables: users, module_progress, simulator_attempts, sr_queue, annotations, recordings) — designed for clean migration later.

12. PDF export — Stage-Gate session reports + the Quick Reference Card (§2.J). Lift the PDF generator pattern from the local prototype source at /Users/joshuaf/Documents/Claude/02_PROJECTS/lsat-u/Curriculum/Netlify/index (4).html.

=== V1.0.5 — SPEC AS COMMENTED HOOKS IN V1.0 (do not build now) ===

- AI Tutor live LLM mode
- R&R Drill LLM-driven semantic comparison (Left Out / Added / Mischaracterized auto-flagging via AI)
- Spaced repetition (SM-2 scheduling, seeded from end-of-module calibration drill misses)
- Live AI co-pilot during R&R

Add commented-out hooks or feature-flag-gated stubs in the v1.0 codebase so v1.0.5 work is a swap-in, not a refactor.

=== INVIOLABLE RULES ===

VOICE: preserve all 15 named tools verbatim — FABS, 2-Part Conclusion Check, Upside Down Argument, Trojan Horse Concession, Pre-Phrase Goal, Skeptic's Ear Check, Stegosaurus Interrogation, X-Ray Scan, Trap Master, Stage-Gate Tracker, R&R Drill, Indicator Vault, Pronoun & Reference Library, Concession Decoder, Coach's Note. Preserve all worked examples (cake-on-blocks, William/Harry, gun-laws, EV chain, tomato/fruit, Monica/dinosaurs, all-nighter, tornado, Alex/Jordan, Microphones-drink-coffee + the other whimsical premises). Preserve voicy passages verbatim ("monsters called cluster sentences", "(aghhhhhhhhh)", "HARK", "TATTOO IT IF YOU HAVE TO", "beautiful starships", masterclass intro paragraph). Register 2 (whimsical, metaphor-led) for Lessons + drill setup. Register 1 (decisive, procedural) for Reference + Question Simulator + drill instructions.

PEDAGOGY: per-module flow is Lesson → Guided examples during the lesson → Checkpoint questions after key concepts → End-of-module calibration drill → Post-drill weakness profile → Spaced repetition (v1.0.5). The diagnostic engine NEVER runs before instruction. No cold pre-test. Calibration is post-instruction only.

=== DESIGN BAR — TOP-TIER MODERN UI ===

Read spec §3.8 (PREMIUM DESIGN DIRECTION) before generating any visual code. Reference quality: Linear, Vercel, Stripe, Arc Browser, Notion (current), Apple HIG modern. The app should look at home next to a Linear or Vercel UI screenshot.

Specific commitments from §3.8 (do not skip any):

TYPOGRAPHY: Inter Variable for body (or Söhne if licensed). Newsreader (Google Fonts, free, editorial-grade serif by David Jonathan Ross) for display + Lessons module long-read prose (17-19px). JetBrains Mono Variable for mono. Voice-to-typography pairing: Register 2 prose in serif, Register 1 callouts in mono, headers in display serif, body UI in sans.

COLOR: deepen background to #08090E. Surface gradients on cards (linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02))). Aspiring Gold #E8D08B used SPARINGLY — primary CTAs only, logo, Stage-Gate "passed" state, focus rings. Default UI chrome uses warm-grey neutrals. Add #FAF8F2 warm-white for the Lessons module's long-read pages.

FOCUS RINGS: 2px gold outline + 4px gold-at-15%-alpha glow ring outside it. Replace browser default globally.

SHADOW STACK (Linear-style three-layer on cards): 0 0 0 1px rgba(255,255,255,0.06), 0 1px 1px rgba(0,0,0,0.4), 0 8px 24px rgba(0,0,0,0.3).

GLASS LAYER: AI Tutor drawer + modals use backdrop-filter: blur(20px) saturate(180%). Sticky top bar uses backdrop-filter: blur(10px) + 80% surface alpha.

MOTION — NAMED CUSTOM EASINGS ONLY:
   --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);     (entrances)
   --ease-in-out-quart: cubic-bezier(0.77, 0, 0.175, 1); (transitions)
   --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);    (Stage-Gate unlock overshoot)
   --ease-out-quint: cubic-bezier(0.22, 1, 0.36, 1);    (default for hover/focus)
Never use default `ease` or `linear`.

LOADING: shimmer skeletons, never spinners.

PREMIUM MICRO-INTERACTIONS:
- Cursor-follow gradient on Coach's Note card on hover (Stripe-style; disabled at reduced-motion)
- Magnetic primary CTA (button pulls 2-3px toward cursor on hover, 8-12px hover radius)
- Custom scrollbars: 4px thin, gold-tinted on hover, transparent at rest
- Indicator chip ripple: 300ms gold-at-30% radial ripple from tap point
- X-Ray Scan reveal stagger: role colors apply per-clause with 30ms stagger left-to-right
- Dashboard bar fill: --ease-spring + 60ms row stagger, 800ms total
- Stage-Gate unlock: spring overshoot scale (1 → 1.06 → 1) over 600ms + gold glow pulse
- Letter-by-letter type reveal on Coach's Note key sentences (~30ms per char)

ANTI-PATTERNS (per §3.8):
- No default `ease` or `linear` easings
- No browser-default focus rings
- No spinner loaders
- No Tailwind-default look — build the design system from the tokens
- No emoji as functional UI elements
- No skeuomorphic gold gradients (the gold is flat-color premium)
- No drop-shadows with offsets — center-shadow only
- No more than 2 weights of body sans on a single screen
- No hard pixel-borders without alpha (use rgba(255,255,255,0.06), not #222)

=== TECH STACK ===

Recommendation: vanilla JS + CSS variables + browser APIs (MediaRecorder, Web Speech, IndexedDB, localStorage). Matches the two flagship prototype apps (read /Users/joshuaf/Documents/Claude/02_PROJECTS/lsat-u/Curriculum/Netlify/index (3).html and index (4).html as architectural references — both scored S/S in the audit). Vanilla path keeps the persistence adapter swap clean.

If you propose React or another framework, justify the trade-off. Either way: the persistence adapter pattern (§6.9) is non-negotiable.

The build will eventually be integrated into a larger app the user has already built, so prioritize clean module boundaries and a portable component system. Do not concern yourself with deployment, hosting, or domain — the user will handle integration separately.

=== ASK BEFORE BUILDING ===

Before generating any code, confirm with the user:

1. **PT bank access** — endpoint URL, auth method, sample request, question schema, trait-tagging convention, rate limits, CORS status. (This is the unblocker for the calibration drills + Simulator.)
2. **Tech stack confirmation** — vanilla JS or React? (Recommend vanilla unless the user has a preference.)
3. **Logo** — extract from the prototype HTML at /Users/joshuaf/Documents/Claude/02_PROJECTS/lsat-u/Curriculum/Netlify/index (3).html (Aspiring Attorneys gold scales SVG inlined there) or accept a different SVG from the user.
4. **Branding/copy overrides** — anything the user wants changed from the spec defaults (and there shouldn't be much, since voice is locked).

Once those four are confirmed, build v1.0 end-to-end.

=== BUILD CHECKPOINTS ===

Pause and request review at two points during the build:

1. **Scaffold review (~midpoint)** — modules navigable, design tokens in place, identity screen working, top bar + nav structure done, one Lesson rendered as a sample. Show this to the user before filling in the full content.

2. **Premium polish gate (before "v1.0 done")** — sanity-check against §3.8 commitments. Are focus rings the gold + glow ring? Are loading states shimmer skeletons? Are easings the four named curves? Does the AI Tutor drawer have backdrop blur? Does X-Ray Scan stagger left-to-right? Does Stage-Gate unlock have the spring overshoot? If any answer is no, fix before declaring done.

=== OUTPUT ===

A complete, polished v1.0 codebase. README with the v1.0.5 follow-up backlog as a prioritized list, plus inline code comments referencing the spec sections (e.g., "// Per spec §3.2.1 — Stage-Gate Tracker" or "// Per §6.9 schema — UUIDs + ISO 8601").

The premium polish bar (§3.8) is the ship gate — the build does not ship until every component looks at home next to a Linear or Vercel UI screenshot.
````

---

## What Claude Code does

1. Reads the 5 files in order.
2. Asks the 4 questions above.
3. Builds v1.0 with the 12 scope items.
4. Adds v1.0.5 hooks as commented stubs.
5. Pauses at scaffold review + premium polish gate.
6. Produces a portable, integration-ready codebase + README with the v1.0.5 backlog.

## What you do

1. Have PT bank access details ready (endpoint, auth, schema, sample request, CORS, rate limits, trait tagging).
2. Open Claude Code in your project directory.
3. Copy the fenced block above.
4. Paste it as one message.
5. Answer the 4 questions when Claude Code asks.
6. Do the scaffold review at the midpoint.
7. Confirm the premium polish gate at completion.
