# 07: Make failed annotation and flag saves recoverable

**Blocked by:**06 reviewed. **Scope:** RC10,11.

Own annotation/flag persistence acknowledgement, pending recovery and relevant player status. Extend existing persistence adapters; do not introduce a second save system. Show Saving, Saved only after acknowledgement, and Not saved with Retry on failure. Keep newer intent when an older acknowledgement arrives. Annotation recovery is actor+passage across sessions; flag recovery is actor+session+question. Preserve ticket06's owner and hydration contract, and retry without duplicate effect.

Existing seams: rcProgress.test.ts, useRcHighlights.test.ts, RcPlayer.saveSafety.test.tsx, rcAnswerBackup.test.ts. Keep answer/timer/completion protection independent from annotation/flag statuses.

- [ ] Rejected saves retain intent and expose retry.
- [ ] Late/duplicate/lost replies cannot mark newer unsaved edits as Saved.
- [ ] Reload recovers the correct actor's pending changes, with visible recovery state.
- [ ] Flag failure is visible; the displayed state never falsely claims persisted success.
- [ ] Account switches cannot replay another actor's pending work.
- [ ] Protected source flags remain immutable.

Fault-inject at existing adapter boundaries and verify actual read-after-write on dedicated test records. Do not claim durable behavior from optimistic DOM state alone.
