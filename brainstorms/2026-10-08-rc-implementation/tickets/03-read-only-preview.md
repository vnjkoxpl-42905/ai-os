# 03: Open a question without creating a drill

**Blocked by:**02 reviewed. **Scope:** RC-19,25; lookup/preview/start boundary.

Own finder navigation, RC preview/player entry and validated return destinations. Reuse the builder's preview/start boundary where suitable. The current player passage entry creates a saved session; it is unsuitable as a lookup preview. Add an explicit preview contract rather than trusting review=1 on an in-progress drill.

Deliver Open question → read-only passage/question preview, with the official selected question focused. Show no answer or summary. A separate Start passage drill action displays complete passage/question counts and deliberately creates one session. Preserve validated internal returnTo through preview, start and exit.

Use RcHubSurface.test.tsx for preview/start precedent, RcPlayer.saveSafety.test.tsx and rcSessionDestination.test.ts for persistence/routing. Prefer a dedicated preview surface sharing content rendering over partially guarding the live player. Mock backend and device-storage boundaries; assert zero create/answer/clock/annotation/flag, cross-out/bookmark and answer-backup writes from preview, including direct load, refresh and close. Marking controls are disabled or explicitly ephemeral; ephemeral state never hydrates into or persists over a saved actor's marks.

- [ ] Open/close/reload preview creates zero sessions/attempts and saves zero personal marks.
- [ ] Backend and local-storage write spies both remain untouched; existing annotations, cross-outs, bookmarks and answer backups stay identical.
- [ ] Chosen official address stays visible and identifies the focused question.
- [ ] Explicit start creates exactly one intended passage session, including duplicate-click/failed-response handling.
- [ ] Exit returns to the originating internal page; external or invalid return targets use a safe fallback.
- [ ] Reveals remain unavailable until the selected scored-drill policy permits them.
- [ ] Dedicated test account browser evidence confirms preview and deliberate start separately.

Use a dedicated test session for start verification; preserve Joshua's existing drills and protected answers.
