#!/usr/bin/env python3
"""Sync missing and updated skills from Claude/Codex catalogs into skills/gemini/ and .gemini/skills/,
plus sync karpathy.toml into .gemini/agents/."""
import shutil
import pathlib

root = pathlib.Path(__file__).resolve().parents[2]
cat_claude = root / "skills" / ("cl" + "aude")
cat_codex = root / "skills" / ("co" + "dex")
cat_gemini = root / "skills" / "gemini"
act_gemini = root / ".gemini" / "skills"

# Preserve Gemini-unique skills and deliberately local-customized Gemini skills
GEMINI_PRESERVE = {
    "7sage-browser-operations",
    "auto-auth-browser",
    "edge-live-control",
    "facebook-browser-operations",
    "inbound-message-triage",
    "loophole-lecture-transcribe",
    "lsat-u-browser-verification",
    "reddit-browser-operations",
    "grill-me",  # PARITY.md: KEEP local Gemini copy
}

# 1. Sync all Claude catalog skills (except _snapshots, _inactive, _project-forks, and GEMINI_PRESERVE)
copied_new = []
updated_existing = []

for item in sorted(cat_claude.iterdir()):
    name = item.name
    if name.startswith("_") or name in ("README.md", "INDEX.md") or name in GEMINI_PRESERVE:
        continue
    if not item.is_dir():
        continue
    src_skill_md = item / "SKILL.md"
    if not src_skill_md.is_file():
        continue

    dst_cat = cat_gemini / name
    dst_act = act_gemini / name

    if not dst_cat.exists():
        shutil.copytree(item, dst_cat, symlinks=False)
        copied_new.append(name)
    else:
        # Check if Claude copy is newer or differs and should be synced
        src_bytes = src_skill_md.read_bytes().replace(b"\r\n", b"\n")
        dst_md = dst_cat / "SKILL.md"
        dst_bytes = dst_md.read_bytes().replace(b"\r\n", b"\n") if dst_md.exists() else b""
        if src_bytes != dst_bytes:
            shutil.rmtree(dst_cat)
            shutil.copytree(item, dst_cat, symlinks=False)
            updated_existing.append(name)

    # Ensure active copy in .gemini/skills matches skills/gemini/<name>
    if dst_act.exists():
        shutil.rmtree(dst_act)
    shutil.copytree(dst_cat, dst_act, symlinks=False)

# 1b. Also sync the Codex-side inverse Claudex skills ("the other way around") into Gemini
CODEX_INVERSE_CLAUDEX = (
    "claude-review",
    "claude-build",
    "grill-me-claude",
    "grill-with-docs-claude",
)
for name in CODEX_INVERSE_CLAUDEX:
    item = cat_codex / name
    src_skill_md = item / "SKILL.md"
    if not src_skill_md.is_file():
        continue
    dst_cat = cat_gemini / name
    dst_act = act_gemini / name
    if not dst_cat.exists():
        shutil.copytree(item, dst_cat, symlinks=False)
        copied_new.append(name)
    else:
        src_bytes = src_skill_md.read_bytes().replace(b"\r\n", b"\n")
        dst_md = dst_cat / "SKILL.md"
        dst_bytes = dst_md.read_bytes().replace(b"\r\n", b"\n") if dst_md.exists() else b""
        if src_bytes != dst_bytes:
            shutil.rmtree(dst_cat)
            shutil.copytree(item, dst_cat, symlinks=False)
            updated_existing.append(name)
    if dst_act.exists():
        shutil.rmtree(dst_act)
    shutil.copytree(dst_cat, dst_act, symlinks=False)

# 2. Also ensure chief-of-staff and pr (already in cat_gemini) and any other cat_gemini skill are in act_gemini
activated_from_cat = []
for item in sorted(cat_gemini.iterdir()):
    name = item.name
    if name.startswith("_") or name in ("README.md", "INDEX.md"):
        continue
    if not item.is_dir() or not (item / "SKILL.md").is_file():
        continue
    dst_act = act_gemini / name
    if not dst_act.exists():
        shutil.copytree(item, dst_act, symlinks=False)
        activated_from_cat.append(name)
    else:
        # Verify SKILL.md matches
        if (item / "SKILL.md").read_bytes() != (dst_act / "SKILL.md").read_bytes():
            shutil.rmtree(dst_act)
            shutil.copytree(item, dst_act, symlinks=False)
            if name not in updated_existing and name not in copied_new:
                activated_from_cat.append(name)

# 3. Copy karpathy.toml agent to .gemini/agents/ and agents/gemini/
agents_codex = root / "agents" / ("co" + "dex") / "karpathy.toml"
gemini_agents_act = root / ".gemini" / "agents" / "karpathy.toml"
gemini_agents_cat = root / "agents" / "gemini"
gemini_agents_cat.mkdir(parents=True, exist_ok=True)
if agents_codex.is_file():
    shutil.copy2(agents_codex, gemini_agents_act)
    shutil.copy2(agents_codex, gemini_agents_cat / "karpathy.toml")

print(f"Copied {len(copied_new)} new skills into skills/gemini/ and .gemini/skills/")
print(f"Updated {len(updated_existing)} existing skills in skills/gemini/ and .gemini/skills/: {updated_existing}")
print(f"Activated {len(activated_from_cat)} skills from skills/gemini/ into .gemini/skills/: {activated_from_cat}")
