"""Portable application paths, outside the Obsidian vault when relocated."""
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parents[2]
_sibling = VAULT_ROOT.parent / "ai-os-projects"
PROJECTS_ROOT = _sibling if _sibling.is_dir() else VAULT_ROOT / "projects"


def project_path(*parts):
    return PROJECTS_ROOT.joinpath(*parts)
