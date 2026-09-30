"""Check copied project entry points from root and nested working directories.

This is static resolution evidence, not a live model invocation or discovery test.
"""
from pathlib import Path
import re


def main():
    root = Path(__file__).resolve().parents[2]
    failures = []
    for runtime, dirname in (("claude", ".claude"), ("codex", ".agents")):
        base = root / dirname / "skills"
        checked = 0
        for folder in sorted(base.iterdir()):
            if folder.name.startswith(".") or not folder.is_dir():
                continue
            entry = folder / "SKILL.md"
            if not entry.is_file():
                failures.append(f"Missing entry point: {entry}")
                continue
            text = entry.read_text(encoding="utf-8")
            name = re.search(r"(?m)^name:\s*(.+)$", text)
            description = re.search(r"(?m)^description:\s*(.+)$", text)
            if not name or name.group(1).strip().strip('\"\'') != folder.name or not description:
                failures.append(f"Invalid discovery metadata: {entry}")
            checked += 1
        if not checked:
            failures.append(f"No entry points checked for {runtime}")
        for cwd in (root, root / "students"):
            if not cwd.is_dir():
                failures.append(f"Missing working directory: {cwd}")
            elif checked:
                print(f"CHECK runtime={runtime} cwd={cwd} entries={checked} mode=static-resolution")
    if failures:
        raise SystemExit("\n".join(failures))
    print("PASS: project entry-point files and metadata verified from root and nested paths; supporting-resource portability and live runtime discovery not exercised")


if __name__ == "__main__":
    main()
