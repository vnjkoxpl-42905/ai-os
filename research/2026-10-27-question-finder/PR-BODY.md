Question lookup previously occupied the side rail and sent LR selections into drill setup instead of showing the requested question. Remove that rail item, keep lookup in Home and Practice, and open a complete read-only LR preview with correctness hidden until Reveal answer. RC results validate identity before opening their existing preview.

Preserves builders and legacy routes, gates lookup on permissions/account state, and handles URL launch, dismissal and preview history without writing attempts or progress.

Validation: 298 focused tests across 14 files passed, typecheck and production build passed, and local rendered checks covered desktop, tablet, phone and docked widths. Independent Claude inspection approved the final diff. Two low-severity follow-ups remain around restored-tab history and focus when a trigger is hidden. Local fixture checks do not certify signed-in production student acceptance.
