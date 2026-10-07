---
name: bank-edits-need-timed-catalog-rotation
description: "Any LR bank questionType, difficulty or text change breaks timed PTs/sections until both frozen timed catalogs are regenerated, seeded and activated"
metadata:
  node_type: memory
  type: project
  originSessionId: ea3d04fb-872d-45e2-bfa6-a69f0373cb16
  modified: 2026-10-07T20:37:25.570Z
---

Timed PrepTests and timed sections freeze each LR question's normalized qtype, level and contentSha256 in server catalogs (`timed_content_manifests_v1`, `timed_section_content_manifests_v1`). `TimedLrAdapter` and `verifyStandaloneLrContent` throw ("LR classification differs from the frozen manifest" / "The loaded section differs from its frozen account source") when the deployed bank disagrees. Labels changed in PRs #194–#198 broke 28 timed sections in production until 2026-10-03, when PR #199 rotated the catalogs.

**Why:** the vitest suite catches it (`timedAdapterContentParity`, `timedContentManifest`), but the earlier label PRs only ran the loader/filter tests.

**How to apply:** after any edit to `public/data/PT*-LR.json`:
1. Run `npx vite-node --script scripts/knowledge/build-timed-manifest.ts` and `npx vite-node --script scripts/knowledge/build-standalone-all-sections-v2.ts`.
2. Update the pinned hash in `scripts/knowledge/build-standalone-coverage.mjs` and `src/lib/timedSectionAdoption.test.ts`.
3. Seed the new catalogs insert-only. The generated SQL is too large for query_database. Patch the old rows server-side with jsonb_set and verify `md5(jsonb::text)` per row; the scripts are in `corpus/lr-explanations/fixes/timed-catalog-rotation/`.
4. After the deploy is live, switch `timed_pt_configuration_v1` and `timed_section_configuration_v1` to the new hashes.

**Since PR #201 (2026-10-07):** a qtype or difficulty change no longer breaks anything. Sealed sittings use their frozen labels, so rotating the catalogs only matters for giving new sittings the new label. A text change still breaks every sitting containing that question until the catalogs are rotated, so steps 1–4 remain mandatory for text edits.

Sittings frozen under an old catalog stay pinned to it and fail to reopen if their question *text* changed. On 2026-10-03 all such sittings were Joshua's own QA runs. See [[student-work-must-be-preserved]].
