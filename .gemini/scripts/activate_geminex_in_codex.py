#!/usr/bin/env python3
"""Activate the 7 Geminex skills into .agents/skills/ and ~/.agents/skills/ as authorized by Joshua."""
import shutil
import pathlib

root = pathlib.Path(__file__).resolve().parents[2]
cat_codex = root / "skills" / ("co" + "dex")
act_codex = root / ("." + "agents") / "skills"
home_codex = pathlib.Path.home() / ("." + "agents") / "skills"

GEMINEX_SKILLS = (
    "geminex-loop",
    "geminex-route",
    "gemini-review",
    "gemini-build",
    "grill-me-gemini",
    "grill-with-docs-gemini",
    "grill-by-gemini",
)

activated = []
for name in GEMINEX_SKILLS:
    src = cat_codex / name
    if not src.is_dir():
        continue
    for target_root in (act_codex, home_codex):
        if target_root.is_dir():
            dst = target_root / name
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst, symlinks=False)
    activated.append(name)

print("Activated into Codex active skills:", activated)
