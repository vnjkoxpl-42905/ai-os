# Plan review 1 dispositions

F1 accepted: explicitly pin application owner UUID and Google account email at deployment. Validate primary calendar identity each run and reject second-admin calls. This is a single-owner integration.
F2 accepted: separate owner-bound ticket table/atomic service-only consume RPC; no reuse or alteration of undocumented booking RPC.
F3 accepted: explicit end-time cutoff, seven-day catch-up chunks, 24-hour overlap, advance only after complete writes, rotating old-task refresh and explicit rescheduled/source-unavailable states.
F4 accepted: exact normalized email/verified aliases only, exclude owner/resource/declined identities, hold ambiguous/shared/archived matches. No Gmail alias guessing.
F5 accepted: source-only upsert, no authenticated direct writes, server mutation RPCs with optimistic revision plus history and server timestamps.
F6 accepted: strict native Docs URL parsing and reconstructed safe links.

No implementation of these app changes has begun. Independent private Drive copy is already authorized/running and separately tested; its source lies outside app checkout and must be inspected separately before claiming its independent approval.
