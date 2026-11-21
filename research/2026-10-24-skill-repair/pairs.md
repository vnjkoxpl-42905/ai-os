# Runtime pair repair, 2026-10-24

## Cause

The four Geminex mappings in `skills/runtime-pairs.toml` describe Codex-host skills paired with Gemini-host inverse workflows. The validator interpreted every mapping as Claude-host to Codex-host. This produced four missing catalog errors and four incomplete activation errors even though the correct runtime catalogs and activations existed. The intended hosts are documented in `skills/PARITY.md`, in the 2026-10-15 Geminex entry.

## Repair

- Retained `[pairs]` for the four existing Claude/Codex equivalents.
- Added an explicit `[codex_gemini_pairs]` table for the four Codex/Gemini equivalents.
- Added Gemini's real home and project activation roots to the runtime inventory.
- Added `runtime_pair_errors` to validate each equivalent against its declared hosts. Both catalog existence and effective activation parity remain checked. Unrelated Claude/Codex asymmetry checks are unchanged.
- No duplicate skills, provider aliases, parity exceptions or disabled checks were introduced.

## Verification

Executed the checker helper against actual on-disk catalog and activation inventories: all eight catalog pairs and all eight activation pairs passed.

Negative checks used isolated in-memory copies, without deleting or changing real skills:

1. Removed Gemini `codex-review` from the catalog inventory: exactly one missing pair error naming `gemini/codex-review`.
2. Removed Gemini `codex-review` from the activation inventory: exactly one incomplete activation error naming the Gemini host.
3. Removed Codex `claude-review` from the catalog inventory: exactly one missing pair error, preserving the existing Claude/Codex validation.

Full `python system/scripts/check-skills.py` after this repair exited 1 with 13 remaining findings: four missing index entries and nine shadowed activations, assigned separately to the parent agent. None of the eight pairing findings remained. Global copy drift warnings remain separate from fatal findings and were not suppressed.

This is static catalog and activation validation. It does not certify a live model invocation or provider authentication.
