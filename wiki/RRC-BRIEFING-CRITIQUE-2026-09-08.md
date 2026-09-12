# Read, Recall, Colour section briefing page: design critique

Date: 2026-09-08. Method: `$impeccable critique` on
`src/features/activity-centre/components/SectionBriefingPage.tsx`, two isolated
passes (a design review with live desktop inspection, and the deterministic
detector) woven into one report. Related: [[COPY-CORRECTIONS]], [[ASSIGN-AN-ACTIVITY]].

## Design health score

| # | Heuristic | Score | Key issue |
|---|---|---|---|
| 1 | Visibility of system status | 2 | "One take, no pause" and "about 25 minutes" are not on the page |
| 2 | Match system / real world | 3 | "The Recall." reads as a typo beside three imperatives |
| 3 | User control and freedom | 3 | Back is 44x44 and works; nothing else needed |
| 4 | Consistency and standards | 2 | Three micro-label styles; the two H2s render at different weights |
| 5 | Error prevention | 3 | No warning that the browser will ask for the microphone |
| 6 | Recognition rather than recall | 3 | A " +" text glyph is the only disclosure affordance |
| 7 | Flexibility and efficiency | 2 | Space is the runner's only key but does nothing here |
| 8 | Aesthetic and minimalist | 3 | Chip and H1 both say the product name; foot restates the notice |
| 9 | Error recovery | 2 | Mic-denied case has no hint on this page |
| 10 | Help and documentation | 4 | The collapsed long version is exactly right |
| **Total** | | **27/40** | **Acceptable, upper end** |

## Anti-patterns verdict

Does it look AI-made? No. Single column, four numbered steps, one primary
action, Fraunces title on cream, no hero metric, no icon grid, no gradient text,
no side stripes, no em dashes in the rendered DOM. The one drift toward generic
is the Start button: a landing-page pill with a hover lift and drop shadow,
written for the dark hero and inherited by this cream task page.

Deterministic scan: `npx impeccable --json` on the page returned zero findings.
The directory scan of `components/` returned 53 advisory findings, none touching
this page or `section-launch.css` (47 are in `activity-scenes.css`). No false
positives to triage. Browser overlay could not run: impeccable 4.0.4 ships no
`detect.js`, and the page has no CSP, so this is a tooling gap and not a page
problem. Cognitive load: 1 of 8 checks failed (working memory), which is low.

## Overall impression

The structure is right and the copy is the best on the platform. The misses are
content gaps and vocabulary drift, not layout. One of them matters: the page was
edited on 2026-09-07 on the belief that the one-take fact survived in Step 4.
It did not. It lives in `instructions.rules[0]`, which this page never renders.

## What's working

- A page, not a modal, with all four steps open and numbered. "Laughing is
  fine." and "It does not have to be clever, it has to be yours." earn their place.
- The hero classes are honestly re-grounded for paper, and the comments say why.
- Accessibility basics hold, measured live: H1 H2 H2 H3, Back 44x44, 2px focus
  rings, no live-region noise.

## Priority issues

**[P1] The two facts she most needs before Start are not on the page.**
Verified live with the long version open: zero hits for "one take"; "minute"
only inside the collapsed essay's sixth heading. The code comment at
`SectionBriefingPage.tsx:63` claims Step 4 carries it. Step 4 does not.
Fix: one plain sentence beside the foot Start: "It runs in one take, about
twenty-five minutes, and it does not pause." Or render `briefing.closer`,
which the type describes as "the last beat before the Start action" and which
nothing renders. Correct the comment. Command: `$impeccable clarify`.

**[P1] The calming notice is styled as a fifth step card.**
`.sl-notice` and `.sl-bp-list li` share fill, hairline, and radius. The one
sentence written to lower her shoulders reads as procedure.
Fix: take the box off it. A plain ink line under the CTA. Command: `$impeccable layout`.

**[P2] Step body lines run about 105 characters.** The essay caps at 68ch; the
step list has no measure. Fix: `max-width: 62ch` on `.sl-bp-list li p` and
`.sl-notice`. Command: `$impeccable typeset`.

**[P2] Three micro-label styles on one page, and mismatched H2s.** Mono chip,
Inter-uppercase h2, Inter-uppercase step number, while `.sl-label` is declared
the one style and goes unused. The summary's h2 inherits body weight, so the
only help on the page looks like a stray sentence. Fix: put step numbers and
h2s on `.sl-label`; give the summary the same h2 treatment and a real chevron.
Command: `$impeccable typeset`.

**[P2] The lede is silently overridden.** `.sl-essay p` outranks `.rd-lede`, so
the 20px italic lede renders at 16.5px. Fix: `.sl-essay p.rd-lede`.
Command: `$impeccable polish`.

**[P3] Landing-page button on a task page.** Drop the transform and outer
shadow on `.sl-briefing-page .sl-start`; keep the fill darkening.
Command: `$impeccable quieter`.

## Persona red flags

- **Jordan (first-timer):** reads "Press space" in Step 4 and looks for a Space
  button; presses Start and meets a microphone permission dialog with no warning.
- **Sam (screen reader):** an `h2` nested inside `summary` is exposed
  inconsistently; some readers drop it from the headings list, the very outline
  the h2 was added to fix.
- **Casey (mobile):** the reassurance sits at the top and the Start she presses
  is 1,000px below it. Same fix as the first P1. Mobile was reasoned from the
  CSS, not seen: the viewport resize did not take.
- **A coaching client at 9pm:** wants "how long is this and can I stop if my
  roommate walks in." The page answers neither, and nothing on it is addressed
  from her coach.

## Minor observations

- Chip and H1 both say "Read, Recall, Colour"; the chip is redundant here.
- The head's side-by-side layout never fits at 840px, so the CTA always wraps
  under the tagline. What ships is accidental.
- Empty tagline still renders an empty `p` with top margin.
- Foot copy repeats "begins" and restates the notice's fact.
- Summary focus ring is `--rd-ink-2`, buttons are `--rd-ink`.
- `.sl-bp-meta` is defined and unused.

## Questions to consider

1. Why is the one sentence written to calm her styled identically to the four things she has to do?
2. If the runner's only key is Space, what would happen if Space started the section from here?
3. What would be missing if the page were only the notice, the four steps, and one Start at the foot?

## Recommended order

1. `$impeccable clarify`: the one-take and 25-minute sentence at the foot, render `closer`, fix the comment.
2. `$impeccable layout`: un-box the notice.
3. `$impeccable typeset`: 62ch measure, one label style, matching H2s, lede fix.
4. `$impeccable quieter`: the Start button's lift and shadow.
5. `$impeccable polish` last.
