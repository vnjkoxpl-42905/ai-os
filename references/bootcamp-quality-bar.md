# Bootcamp audits need source coverage and observed behavior

Reconstructed audit standard, 2026-10-11. This is a current replacement for the missing historical `bootcamp-quality-bar.md`, not a recovery of that document or proof that any bootcamp is shipped. Joshua's current instructions and the target repository's current decisions win over old build plans.

## Sources and authority

- [Main Conclusion handoff](../../ai-os-projects/lsatu/docs/main-conclusion-bootcamp/MAIN_CONCLUSION_HANDOFF.md): source completeness, learning surfaces, explicit gates and exclusions. Historical v1 plan; do not import its old Mac paths or no-auth assumption into the integrated app.
- [Canonical content inventory and map](../../ai-os-projects/lsatu/docs/main-conclusion-bootcamp/parity/README.md): every reviewed source maps to an included item or a reasoned exclusion. JSON inventory/map are canonical; their Markdown views are review aids.
- [Historical Gate 5 audit](../../ai-os-projects/lsatu/docs/main-conclusion-bootcamp/gate-5-audit.md): a checklist and dated results, not current acceptance evidence.
- [Current selected teaching standard](lsat-teaching-voice-standard.md): patient reasoning, complete predicates, fact-versus-rule distinctions and meaningful student attempts.
- [Current product surfaces](intro-to-lr-product.md) and [current design evidence](intro-to-lr-design.md): inspect the actual checkout before drawing conclusions.

## Check these before saying shipped quality

1. **Content is accounted for.** Trace lessons, questions, answers, explanations, named tools and exercises to the current corpus/inventory. Record omissions and deliberate exclusions. Do not count a dead route as preserved teaching content.
2. **Teaching comes before unsupported testing.** Explain the relevant distinction, work a small example, let the learner attempt it, then explain the reasoning and mistake. Preserve logical modality and complete conditions. Assess pedagogy, not just attractive layout.
3. **The interaction does real work.** Follow the relevant learn, drill, submit, review and next-step journey. Check useful feedback, loading, empty and error states. No fabricated progress, dead buttons or claimed persistence based only on an optimistic local display.
4. **Progress and access are verified separately.** Test authorized signed-in read/write behavior, reload, and account isolation where applicable. Live Supabase owns operational homework/progress state. Local unit tests do not prove deployment or signed-in acceptance.
5. **Navigation and accessibility are usable.** Check keyboard focus, labels, readable contrast, small screens and reduced motion. Verify only the routes and devices actually tested. Functional equivalence can be better than copying a historical layout.
6. **Visual decisions have an owner.** Use the imported current styles/components and explicit current design decisions. Keep role colors meaningful; do not revert cream surfaces to dark navy because an old token file says dark-only.
7. **Validation and release are distinct.** Run checks appropriate to the actual changes. Record the checkout/commit, commands, failures, observed behavior and untested limits. Historical test counts and build sizes are not current results.

Use verdicts `shipped-quality`, `in-progress`, or `needs-work`, qualified by the evidence actually collected. If live acceptance was not checked, say `static/source review only; live acceptance unverified`. A target can pass a source comparison without being ready to ship.
