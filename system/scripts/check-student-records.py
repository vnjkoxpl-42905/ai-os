"""Check the local navigation contract for current student folders.

Read-only. Run from the repository root with:
    python system/scripts/check-student-records.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
STUDENTS = ROOT / "students"
WIKILINK = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def section(markdown: str, heading: str) -> str | None:
    match = re.search(rf"(?m)^## {re.escape(heading)}\s*$", markdown)
    if not match:
        return None
    end = re.search(r"(?m)^## ", markdown[match.end() :])
    return markdown[match.end() : match.end() + end.start()] if end else markdown[match.end() :]


def linked_files(markdown: str, folder: Path) -> tuple[set[Path], list[str]]:
    paths: set[Path] = set()
    broken: list[str] = []
    for target in WIKILINK.findall(markdown) + MARKDOWN_LINK.findall(markdown):
        target = target.split("#", 1)[0].strip()
        if not target or target.startswith(("http://", "https://")):
            continue
        path = (ROOT / target) if target.startswith("students/") else (folder / target)
        if not path.name.endswith(".md"):
            path = Path(f"{path}.md")
        path = path.resolve()
        paths.add(path)
        if not path.is_file():
            broken.append(target)
    return paths, broken


def main() -> int:
    errors: list[str] = []
    folders = [
        path
        for path in sorted(STUDENTS.iterdir())
        if path.is_dir() and not path.name.startswith("_") and path.name != "non-students"
    ]
    exports = packages = 0

    for folder in folders:
        profile = folder / f"{folder.name}.md"
        inventory = folder / "transcripts.md"
        if not profile.is_file() or not inventory.is_file():
            errors.append(f"{folder.name}: missing profile or transcripts.md")
            continue

        profile_section = section(profile.read_text(encoding="utf-8"), "Open this record")
        inventory_section = section(inventory.read_text(encoding="utf-8"), "Local session files")
        if profile_section is None:
            errors.append(f"{folder.name}: profile lacks 'Open this record'")
            continue
        if inventory_section is None:
            errors.append(f"{folder.name}: transcripts.md lacks 'Local session files'")
            continue

        profile_links, profile_broken = linked_files(profile_section, folder)
        inventory_links, inventory_broken = linked_files(inventory_section, folder)
        if inventory.resolve() not in profile_links:
            errors.append(f"{folder.name}: profile does not link transcripts.md")
        errors.extend(f"{folder.name}: broken profile link {link}" for link in profile_broken)
        errors.extend(f"{folder.name}: broken session link {link}" for link in inventory_broken)

        downloads = folder / "transcript-downloads"
        for raw in sorted(downloads.rglob("*.md")) if downloads.exists() else []:
            exports += 1
            if raw.resolve() not in inventory_links:
                errors.append(f"{folder.name}: unlinked full export {raw.relative_to(folder)}")

        sessions = folder / "sessions"
        for package in sorted(sessions.iterdir()) if sessions.exists() else []:
            if not package.is_dir():
                continue
            packages += 1
            for name in ("transcript.md", "summary.md", "topic-map.md"):
                file = package / name
                if not file.is_file():
                    errors.append(f"{folder.name}: incomplete package {package.name}/{name}")
                elif file.resolve() not in inventory_links:
                    errors.append(f"{folder.name}: unlinked package file {package.name}/{name}")

    print(f"Checked {len(folders)} student folders, {exports} local Markdown exports, {packages} packages.")
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1
    print("All internal routers and local session links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
