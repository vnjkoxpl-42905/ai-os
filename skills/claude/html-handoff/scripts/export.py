"""Run the existing LSAT U HTML exporter and package its named outputs."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zipfile


def local_file(root: Path, name: str) -> Path:
    if not name or Path(name).name != name or "/" in name or "\\" in name:
        raise ValueError(f"Expected a plain output filename: {name!r}")
    result = root / name
    if result.is_symlink() or not result.is_file():
        raise ValueError(f"Missing or linked output: {result}")
    return result


def package(root: Path) -> Path:
    report_file = local_file(root, "auto-checks.json")
    report = json.loads(report_file.read_text(encoding="utf-8"))
    outputs = report.get("outputs")
    if not isinstance(outputs, dict) or not outputs:
        raise ValueError("auto-checks.json has no named outputs")
    selected = {report_file, local_file(root, "README.md")}
    skipped = []
    for role, item in outputs.items():
        if not isinstance(item, dict):
            raise ValueError("Invalid output report")
        html = local_file(root, item.get("file", ""))
        if html.suffix.lower() != ".html":
            raise ValueError(f"Not an HTML output: {html.name}")
        digest = hashlib.sha256(html.read_bytes()).hexdigest()
        if digest != item.get("sha256"):
            raise ValueError(f"HTML changed after export checks: {html.name}")
        checks = item.get("checks")
        if not isinstance(checks, dict) or not checks or not all(v is True for v in checks.values()):
            raise ValueError(f"Export checks did not pass: {html.name}")
        selected.add(html)
        selected.add(local_file(root, f"{role}-handoff.md"))
        image = root / f"{html.stem}.png"
        if image.exists():
            local_file(root, image.name)
            if image.stat().st_mtime_ns >= html.stat().st_mtime_ns:
                selected.add(image)
            else:
                skipped.append(image.name)
    prompt_file = root / "START-HERE-PROMPT.md"
    if prompt_file.is_symlink():
        raise ValueError("Refusing to overwrite a linked prompt")
    descriptions = {
        ".html": "Self-contained interactive design preview using sample data; open and render it.",
        ".png": "Screenshot reference for visual review.",
    }
    lines = [
        "Review the exported interface designs.", "",
        f"All files are on this computer in: {root}", "",
        "Read README.md first, then each role-specific handoff Markdown before rendering its HTML.",
        "Current files and purposes:",
    ]
    for file in sorted(selected):
        purpose = ("Review requirements, context, and limitations." if file.name.endswith("-handoff.md")
                   else "Opening instructions and package overview." if file.name == "README.md"
                   else "Automated export checks; not proof of backend or visual correctness." if file.name == "auto-checks.json"
                   else descriptions.get(file.suffix.lower(), "Supporting handoff file."))
        lines.append(f"- {file}: {purpose}")
    lines.extend([
        f"- {prompt_file}: Ready-to-paste routing prompt with local paths and file purposes.",
        f"- {root / 'html-handoff.zip'}: Complete package of the current named files and this prompt.",
        "", "Other files in this folder may be older. Use only the filenames listed above.",
        "Follow the role handoffs for the authorized creative task. Current visuals are reference material, not mandatory design requirements.",
        "For an authorized redesign, use your strongest creative judgment, implement locally, and visually verify and refine it. For review-only handoffs, report findings without editing.",
        "Sample interactions do not establish production backend persistence. Do not publish, deploy, or change live records unless asked.",
        "If you cannot access this computer's filesystem, ask me to upload html-handoff.zip. Never claim to review files you cannot open.",
    ])
    prompt_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    selected.add(prompt_file)
    target = root / "html-handoff.zip"
    if target.is_symlink():
        raise ValueError("Refusing to overwrite a linked archive")
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
        for file in sorted(selected):
            archive.write(file, file.name)
    print(f"Packaged {len(selected)} files: {target}")
    if skipped:
        print("Skipped screenshots older than their HTML: " + ", ".join(skipped))
    print("Screenshot freshness is a timestamp check, not a claim of visual review.")
    return target


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, help="Active LSAT U application checkout")
    parser.add_argument("--out", required=True, type=Path, help="Export output directory")
    parser.add_argument("--package-only", action="store_true", help="Verify/package current files without rebuilding")
    args = parser.parse_args()
    output = args.out.resolve()
    if not args.package_only:
        if args.repo is None:
            parser.error("--repo is required unless --package-only is used")
        repo = args.repo.resolve()
        exporter = repo / "scripts/verification/export-role-home.mjs"
        if not exporter.is_file():
            parser.error(f"No LSAT U exporter at {exporter}; use the correct active checkout")
        subprocess.run(["node", str(exporter), "--out", str(output)], cwd=repo, check=True)
    package(output)


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, subprocess.CalledProcessError, zipfile.BadZipFile) as exc:
        print(f"html-handoff: {exc}", file=sys.stderr)
        raise SystemExit(1)
