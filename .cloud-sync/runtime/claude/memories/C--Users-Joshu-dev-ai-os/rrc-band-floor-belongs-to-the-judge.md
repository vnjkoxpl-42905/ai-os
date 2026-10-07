---
name: rrc-band-floor-belongs-to-the-judge
description: RRC Coverage bands are calibrated to the judge model; re-run scripts/rrc-census.ts (admin census route inside grade-rrc-section) whenever the model changes
metadata: 
  node_type: memory
  type: project
  originSessionId: 88f3772c-2682-413b-be8e-1f23f7ae7b85
  modified: 2026-09-08T08:07:18.156Z
---

The Read, Recall, Colour band floor (`BAND_FLOOR` in `supabase/functions/_shared/rrcGrading.ts`) is the 10th percentile of Joshua's 71 model runs judged by the LIVE model. On 2026-09-08 it moved 86 → 82 when the judge went from gemini-2.5-flash to gemini-3.8-flash (ADR 0035). The census inputs from ADR 0018 exist only on the Mac and there is no Gemini key on the Windows box, so the census runs inside the edge function: admin-only `{ census: { sourceSection, items } }` on `grade-rrc-section`, driven by `npx vite-node scripts/rrc-census.ts` (~100 s, 71 judge calls, writes nothing).

**Why:** a floor measured on one model and applied by another under-banded every student by four points; Joshua wants one consistent judge and a fair scale.

**How to apply:** if anyone (Lovable included) changes the judge model, re-run the census before any new grade is shown, move `BAND_FLOOR` with an ADR, and re-grade the existing student rows with `force: true`. Lovable's deploy message races a fresh push: send it after the push lands and name the commit it will actually see. Related: [[lovable-edge-functions-do-not-deploy-from-push]].
