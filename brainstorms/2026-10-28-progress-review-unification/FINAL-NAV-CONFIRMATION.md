# Final targeted navigation confirmation before authorized main release

Joshua explicitly asked for main after Claude and Codex. The additional full-source review ybr8m7gq confirmed the LR destination, Analytics shortcut and RC report-binding corrections, but returned REVISE for two remaining navigation items. This final narrow confirmation inspects those corrections only; it must not be represented as a fresh whole-repository approval. The earlier bounded full inspection rounds and their REVISE results remain recorded.

- R-1: StudentDestination reviewTabTarget now strips mode from the explicit Progress tab target, including remembered targets. The original legacy Topics entry still opens Types; clicking Progress reaches Overview while preserving window/type/hash state.
- R-2: explicit To review tab targets strip selected, retaining queue filters and hash. The actual detail-return URL is unchanged and still restores its selected item/focus.

Inspect StudentDestination.tsx and its actual click regressions, with ReviewViewMemoryContext as context. You may read the presenter and queue focus consumer as needed. Report any remaining material issue in these two fixes. Do not edit or run tests. Code is frozen. The host executes checks and will record browser proof, typecheck/build and exact main/publication readback separately.
