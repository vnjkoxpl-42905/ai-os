# Missing catalogue and activation repair

Date: 2026-10-24

The existing project Codex activations were the complete authoritative local trees for this repair. Read both SKILL.md entry points in full, inspected tree structure and reference routes, and verified that counterpart destinations did not already exist before copying. No previous generation was overwritten.

Copied each complete tree into skills/codex/, skills/claude/ and .claude/skills/. The existing .agents/skills/ copy remains unchanged. All six copied trees match their source byte-for-byte by SHA-256, include supporting files and the generated shared design hub route, and are ordinary directories/files rather than symlinks. No global activation was added, and no global counterparts existed in the inspected user .agents/skills or .claude/skills roots.

- **chrome-extensions**: 24 files per tree; 23 explicit local reference paths checked; no missing references.
- **modern-web-guidance**: 193 files per tree; 0 explicit local reference paths checked; no missing references.

Evidence: [File hash verification](catalog-hashes.json).

Added a dated parity repair note to skills/PARITY.md. INDEX.md is generated, so the parent agent should run `py system/scripts/gen-skill-index.py` after all parallel catalogue repairs finish. No validator or other skill was changed by this worker.
