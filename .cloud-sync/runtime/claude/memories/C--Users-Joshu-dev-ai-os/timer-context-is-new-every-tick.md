---
name: timer-context-is-new-every-tick
description: "In LSAT U, the timer context object is recreated on every 250ms tick, so any effect or useCallback that lists `timer` as a dependency re-runs four times a second"
metadata: 
  node_type: memory
  type: project
  originSessionId: e6445ce4-1415-4754-915e-cb42437a0b45
  modified: 2026-09-11T19:16:46.342Z
---

`useTimer` (src/hooks/useTimer.ts) returns a fresh object on every render and `TimerProvider` memoises on it, so `useTimerContextSafe()` in Drill.tsx yields a new `timer` every 250ms while the clock runs.

**Why:** On 2026-09-11 this turned the "snapshot on every answer" effect into a 4Hz `in_progress` writer and made the 20s heartbeat `setInterval` get torn down before it ever fired. It is how a spent 35:00 clock ended up in a `bootcamp_kv` resume row (PR #124).

**How to apply:** Read the clock through a ref (`timerRef.current`) inside callbacks and effects; depend on `hasTimer`/`!!timer` or on the timer *config*, never on the `timer` object itself. See [[section-resume-row-is-per-section-not-per-assignment]] (now keyed per assignment for homework).
