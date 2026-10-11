---
name: every-drill-gets-its-own-walkthrough
description: "Each LSAT U drill's instructions page needs its own animated walkthrough of that drill's real steps, with a fresh example, never a shared demo"
metadata:
  node_type: memory
  type: feedback
  originSessionId: d1b2fc2f-0290-4d30-9b30-a10b8a062516
  modified: 2026-10-11T21:23:48.753Z
---

Every drill's instructions page shows a walkthrough built for that drill: one animated frame per step the drill actually asks for, in drill order, using an example that is not one of the drill's questions. Never reuse one demo across drills, and never put the demo on the practice page itself.

**Why:** Joshua (2026-10-11): the visual should make clear what this particular drill will have the student do; a repeated image across drills is not accurate.
**How to apply:** in the conditional bootcamp this lives in `src/bootcamps/conditionals/content/drillDemos.ts` + `components/DrillDemo.tsx`, guarded by `drillDemos.test.ts` (every drill on the path has one; worksheet step counts match). Any new drill or bootcamp gets its own entry. Motion is built in code (CSS/JS), not Kling, unless he asks; see [[conditional-videos-use-kling]].
