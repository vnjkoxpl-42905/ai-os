"""Export only instructional Google documents observed in captured workout links.

Read-only gws Drive exports; never changes/shares source documents. Existing files
are preserved. Each attempted export, including failure, is recorded with status.
"""
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[2]
INTAKE = ROOT / "raw/inbox/loophole-workouts-2026-10-14"


def main():
    gws = shutil.which("gws")
    if not gws:
        raise RuntimeError("gws is not on PATH; inspect shared Windows toolchain before installing")
    details = json.loads((INTAKE / "details.json").read_text(encoding="utf-8-sig"))
    output = INTAKE / "attachments"
    output.mkdir(exist_ok=True)
    records = []
    for detail in details:
        for link in detail.get("links", []):
            match = re.search(r"docs\.google\.com/(spreadsheets|document)/d/([^/]+)", link.get("url", ""))
            if not match:
                continue
            kind, file_id = match.groups()
            formats = [("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "xlsx")] if kind == "spreadsheets" else [("text/plain", "txt"), ("application/pdf", "pdf")]
            for mime, suffix in formats:
                path = output / f"{file_id}.{suffix}"
                record = {"workout": detail["name"], "url": link["url"], "link_text": link.get("text", ""), "file_id": file_id, "export_mime": mime, "local_path": path.relative_to(INTAKE).as_posix()}
                if path.exists():
                    record.update(status="captured", sha256=hashlib.sha256(path.read_bytes()).hexdigest(), bytes=path.stat().st_size)
                else:
                    temporary = output / (file_id + ".partial-" + suffix)
                    command = [gws, "drive", "files", "export", "--params", json.dumps({"fileId": file_id, "mimeType": mime}), "--output", str(temporary)]
                    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
                    if result.returncode == 0 and temporary.exists() and temporary.stat().st_size:
                        if suffix == "xlsx" and temporary.read_bytes()[:2] != b"PK":
                            record.update(status="failed", error="Export did not return XLSX ZIP bytes")
                        elif suffix == "pdf" and not temporary.read_bytes().startswith(b"%PDF"):
                            record.update(status="failed", error="Export did not return PDF bytes")
                        else:
                            temporary.replace(path)
                            record.update(status="captured", sha256=hashlib.sha256(path.read_bytes()).hexdigest(), bytes=path.stat().st_size)
                    else:
                        # gws errors contain request diagnostics, never auth material.
                        record.update(status="failed", error=(result.stderr or result.stdout)[-1600:], returncode=result.returncode)
                records.append(record)
                manifest = INTAKE / "attachments.json"
                prior = manifest.read_bytes() if manifest.exists() else None
                content = json.dumps(records, ensure_ascii=False, indent=2).encode("utf-8")
                with tempfile.NamedTemporaryFile(dir=INTAKE, delete=False) as handle:
                    pending = Path(handle.name)
                    handle.write(content)
                if (manifest.read_bytes() if manifest.exists() else None) != prior:
                    raise RuntimeError(f"Concurrent attachment manifest edit; new bytes retained at {pending}")
                pending.replace(manifest)
                print(detail["name"], suffix, record["status"], record.get("bytes", ""))
    print("Exports:", len(records), "Captured:", sum(r["status"] == "captured" for r in records))


if __name__ == "__main__":
    main()
