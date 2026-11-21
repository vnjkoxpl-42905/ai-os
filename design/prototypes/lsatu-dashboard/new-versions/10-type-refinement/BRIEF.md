# 10: Typography refinement

Authorized 2026-10-25. Joshua rejected09's small, thin, over-styled typography and selected the mixed-platform shortcut badge. He explicitly requested Impeccable and the saved25-tip font/Apple resources to improve fonts and remove generic AI styling. Preserve09 as the reference. This new local generation keeps the existing structure, palette, task identity and tested features.

Register: product. Scene: a coaching student reviewing assignments on a Windows laptop in ordinary room light, then checking a message on a phone between sessions. The selected light paper/ink family remains appropriate. This is working interface typography, not a landing-page treatment.

IMPECCABLE_PREFLIGHT: context=pass product=pass command_reference=pass shape=not_required image_gate=skipped:typography refinement of existing UI; no new artwork needed mutation=open

Context loader read PRODUCT.md and DESIGN.md in09 before copying them here. Product, typeset, distill, typography and polish references were read. Scoped current user direction overrides older type choices in copied app-wide context. Historical teaching/world instructions retain their own scope. No new art or font service is needed.

## Changes that should be visible

- Keep licensed local Manrope for operational text. Use a consistent fixed rem scale and meaningful weight, not tiny light utility text. Body1rem, controls0.875rem, secondary0.8125 to0.875rem, phone secondary at least0.875rem. Assignment titles1 to1.125rem with weight600. Good line height and real foreground contrast.
- Reserve Newsreader for the main page heading. Remove serif styling from ordinary work rows, message snippets, date numerals and button labels. Remove italic greeting/name styling and the redundant italic announcement line.
- Replace tracked uppercase mono labels with ordinary-case sans labels. Fixed-width references may keep monospace only when it helps scanning. Use fewer role-based size and weight choices across Home, Practice, Review, Messages, teacher views and dialogs.
- Replace the combined platform badge with Ctrl K on Windows or Command-K notation on Apple platforms. Hide optional shortcut chrome at cramped/touch widths; preserve the real keyboard action, focus treatment and visible finder label.
- Use consistent restrained control shapes. Remove unnecessary pill framing and decorative emphasis. Do not remove useful information, calendar semantics, named navigation, exact Review links or saved-state behavior.
- Keep compact Home section order, sidebar destinations, original restrained artwork, synthetic-data boundaries and failure handling. New local-storage namespace: lsatu-type-refinement-v1.

## Apple principles and their web adaptation

Official references verified for this task:

- https://developer.apple.com/design/human-interface-guidelines/typography
- https://developer.apple.com/design/human-interface-guidelines/accessibility
- https://developer.apple.com/design/human-interface-guidelines/keyboards

The applicable principles are legibility at small sizes, limiting typefaces, hierarchy through size/weight, accommodating larger text and familiar keyboard conventions. The rem values and platform-specific badge here are our web implementation choices. Apple native point sizes and Dynamic Type APIs are not universal web requirements. Existing OFL fonts suffice; the saved25-tip resource map is a discovery guide, not a required dependency list.

## Acceptance

Compare09 and10 at the reported1048x858 viewport and390px phone. Inspect actual rendered results at readable scale, including finder detail, assignment rows, inner destinations and dialogs. Check320,768 and1440 widths,200% enlarged text, focus, platform shortcut display and functionality, font loading, contrast and overflow. Run existing meaningful interaction/state regressions. Review improved design with Claude using actual source and final static captures; distinguish host browser tests from reviewer source/image inspection. Source or model approval is not Joshua's visual approval.

Local prototype only. No real account operations, commits, pushes or publication.
