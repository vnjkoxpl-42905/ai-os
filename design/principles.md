---
type: reference
subject: Find the owning design principle before choosing a treatment
created: 2026-10-24
updated: 2026-10-27
aliases: [Design principles router]
tags: [design, llm-wiki]
sources:
  - ../raw/sources/design/2026-10-27-dashboard-material/PROVENANCE.md
  - ../references/website-design-planning.md
  - ../research/2026-10-21-lexprep-motion-teardown.md
  - ../references/intro-to-lr-design.md
---

# Use principles with their original context

This is a routing synthesis of existing documents. It does not replace their evidence, introduce a fixed aesthetic, or approve a product change. Read the owning source before applying a rule.

| Decision | Principle to investigate | Owning source |
|---|---|---|
| What deserves attention first? | Start with the user's immediate decision. Give sections distinct jobs and one clear main action. | [Website planning](../references/website-design-planning.md), [five review checks: one accent, three layers, one mover](../references/website-design-planning.md#five-review-checks-from-a-later-video-ingested-2026-11-20) |
| How can an interface have depth? | Vary visual intensity and use purposeful layers. Depth is an option, not a requirement for glass, 3D or continuous motion. | [Material and depth guidance](#material-depth-and-a-richer-layered-feel), [selected reference](../raw/sources/design/2026-10-27-dashboard-material/PROVENANCE.md), [website planning: later video methods](../references/website-design-planning.md#what-two-later-videos-add-ingested-2026-10-12) |
| How do we avoid blandness without changing everything? | Compare actual reference regions, identify hierarchy, scale, surface and spacing causes, then inspect a focused rendered revision. A style name or score alone is insufficient. | [Current methods and critique route](methods.md) |
| Which transition should run? | Separate page entrance, scroll reveal and panel movement. A filter update should not replay an entire page or remount working state. | [LexPrep motion teardown](../research/2026-10-21-lexprep-motion-teardown.md) |
| Is motion verified? | Inspect natural playback and reduced-motion behavior separately. Settled screenshots do not establish timing quality. Keep reading and controls immediately available. | [Motion evidence and constraints](../research/2026-10-21-lexprep-motion-teardown.md) |
| Which colours or typography are authoritative? | Inspect actual imports, scoped styles and the rendered host. Legacy token files can conflict with current source. Current user direction takes precedence over historical palettes. | [Imported styling comparison](../references/intro-to-lr-design.md) |
| How should question controls behave? | Combine question discovery coherently while distinguishing opening one question from selecting questions into a set. Preserve explicit focus, loading, shortage and error feedback. | [LR drill setup brief](../brainstorms/2026-09-26-lr-drill-setup-design.md) |
| Which dashboard additions are useful? | Connect question access, recent work and session preparation to actual student decisions. More installed effects are not themselves useful widgets. | [All 25 tips applied to the student home](../research/2026-10-24-student-widgets/clip-findings.md) |
| How do we judge quality? | Separate aesthetic judgment, usability, factual accuracy and integration. Declare a rubric; preserve limitations rather than claiming a perfect score. | [Methods](methods.md), [historical measured audit](../wiki/DRILL-HUB-IMPECCABLE-AUDIT-2026-09-08-RUN3.md) |
| How should activity answers and feedback teach the task? | Use consistent question wording, preserve condition direction and modality, present accepted quotations as alternatives, and distinguish local recognition from an AI judgment. Keep historical keys intact. | [Spot question audit and confirmed corrections](../research/2026-10-25-spot-all-questions-claude-review.md); app-owned `.impeccable/surfaces/src-features-activity-centre.md` remains the implementation brief. |

## Historical work is useful evidence, not a new mandate

- [The 2026-09-23 Home discovery](../brainstorms/2026-09-23-classroom-home-visual-upgrade.md) preserves historical decisions, not the current brief. For the current dashboard appearance, use the user-selected warm-paper/charcoal reference below. Earlier near-white or top-rail directions do not override this selection; it does not authorize unrelated product changes or restore a countdown.
- [The 2026-09-28 student experience](../brainstorms/2026-09-28-lsatu-student-experience-design.md) explains navigation grouping and distinguishes an illustrative prototype from production behavior.
- [The 2026-10-22 role-home specification](../brainstorms/2026-10-22-role-home.build-spec.md) owns its role-specific product scope. A teacher's teaching tasks and a student's assigned work are different views.

Use the [document routing audit](document-routing-audit.md) and [catalogue](catalog.generated.md) to find additional critiques, project authorities and prototype notes. Skills and libraries supply techniques; they do not silently replace Joshua's current product decisions or the [teaching voice](../references/lsat-teaching-voice-standard.md).

## Material, depth and a richer layered feel

### The selected dashboard reference

Joshua selected a user-supplied screenshot of the classroom dashboard (supplied 2026-10-26; exact capture time unknown) over the cooler neutral prototype, saying "this version and oclur scheme is better". On 2026-10-27 he explicitly asked to retain these lessons and route future design work here. See the [preserved screenshot and provenance](../raw/sources/design/2026-10-27-dashboard-material/PROVENANCE.md) and [reference image](../raw/sources/design/2026-10-27-dashboard-material/dashboard.png).

The evidence is a user-supplied still image of https://lsatprep.study/classroom, not an independently exercised production session. The following explanations are visual interpretations of that image and Joshua's preference, not measured usability findings. Exact CSS values cannot be recovered reliably from a scaled screenshot.

Superseded in part 2026-11-18: the base is near-white, not beige paper. Warm beige may appear as an occasional streak or accent, never the whole surface. Status shows in one ink tone through shape and weight, not hue. For LSAT U, preserve soft charcoal, restrained shadows, compact composition and the existing destination structure as the visual baseline. Do not default to cool gray, navy or gold. Other projects inherit the principles below, not a mandatory palette. A later explicit brief can supersede this selection.

The reference is a starting point, not approval of every detail: its coloured dots appear to track the row type (Bootcamp/Activity), which is already shown in text; if a dot conveys status instead, pair it with a label or symbol. The diffuse haze above the header is not a feature to preserve; retain controlled contact and ambient shadows while keeping text and edges crisp. The screenshot came from a user-supplied clipboard attachment in a Codex design session; its transcript is not archived with this evidence.

### Give each surface a physical job

Here, material design means treating surfaces as coherent materials with light, edges and relative elevation. It does not mean adopting Google's Material Design system or adding a component library.

| Visible treatment in the still | Likely effect (interpretation) | Suggested application, not observed behavior |
|---|---|---|
| Near-white ground (beige only as an accent), lighter assignment rows and soft charcoal | Related tones feel like parts of one environment while still separating content. | Define a small surface scale: page ground, section plane, interactive row, focal dark surface. Compare them together in the rendered host. |
| Broad header and main panels with shadows concentrated beneath their edges | A restrained contact shadow makes a panel feel supported above the ground. | Combine a fine edge/contact shadow with a soft lower ambient shadow. Keep light direction consistent and use stronger elevation only for a higher layer. |
| Large rounded section planes, smaller rounded rows and controls | Shape distinguishes containers from things users can operate. | Use a deliberate radius hierarchy and aligned inner padding. Do not give every object the same radius, border and shadow. |
| Compact charcoal next-assignment panel beside the greeting | Contrast appears to emphasize the next action without dominating the workspace; ease of finding it needs runtime testing. | Size the focal element around its task. Keep surrounding assignments, messages and schedule legible together. A large atmospheric image is not a substitute for depth. |
| Raised action pills and quieter content planes | Small local elevation suggests something can be pressed. | Not visible in the still: define distinct resting, hover, pressed and keyboard-focus states. Pressed controls can reduce shadow; focus needs a visible boundary independent of shadow. |
| Small row accents within a near-white/charcoal scheme | Limited accents supply life without fragmenting the page. | Show status through shape and weight in one ink tone, never hue (2026-11-18). |

### Compose layers rather than piling on cards

- Establish a clear ground, a few section planes and local interactive elements. Group related content within a shared plane; separate it with spacing or rules when another card adds no meaning.
- Preserve compact balance as a priority order: make the next action easy to find, keep assignments and messages readable, and keep the schedule secondary. Adapt placement and sequence to the task and viewport; the screenshot's horizontal calendar and desktop grouping are examples, not required phone geometry. Density should support scanning without shrinking text to unreadable sizes.
- Use tonal separation, edge definition and shadow together. A broad gray blur around every panel creates haze; removing every shadow and tint creates flatness. Check the silhouette and the contact edge at actual display size.
- Let typography reinforce the layers: expressive display type for the greeting, readable working type for tasks and controls, restrained metadata. Maintain clear size/weight differences and aligned baselines. Do not spread tiny tracked labels or decorative italics across all content.
- Keep texture and gradients subtle enough that text remains crisp. They should suggest illumination or material, not decorate empty space or imitate metallic gold.
- Separate hierarchy from depth: clearer grouping can still look flat. Judge both the reading order and whether the surfaces convincingly relate to one another.

### Verify the result against the selected reference

Before a revision, name the specific cause being improved: surface contrast, contact shadow, proportion, spacing, type or state. Compare matched, readable desktop and phone renders using equivalent content and viewport sizes. Check the main action, secondary content, focus/pressed states and text contrast on each actual surface; inspect motion separately when changed. Preserve a before/after image and state what was actually inspected. Passing layout tests or receiving an agent's approval does not establish visual superiority or user acceptance.

Retrieval check: "How do we add depth without more cards?" Start at [the design hub](README.md), read this section, then inspect the selected reference. The answer is a small coherent surface scale, purposeful elevation, consistent lighting, proportional emphasis and grouping within shared planes.

## Illustrations should teach the example they sit beside

For student notes, pair each illustration with an example from the same concrete situation. Arrange the image, evidence, conclusion, and reasoning in reading order. On phones, stack them in that order. Compare lookalike flaws using the same objects whenever possible. For causal alternatives, show the actual direction and name what each cause would explain. Use motion when revealing a comparison makes the reasoning easier to follow, and make it optional with reduced motion.

Source: Joshua's Famous Flaws preview feedback, 2026-11-15.
