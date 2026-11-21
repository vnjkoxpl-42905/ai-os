"""Save an explicitly observed PDF and its entire extracted text. No browser state."""
import hashlib
import json
from pathlib import Path
import urllib.request

from pypdf import PdfReader

intake = Path(__file__).resolve().parents[2] / "raw/inbox/loophole-routines-2026-10-15"
source = json.loads((intake / "pdf-source.json").read_text(encoding="utf-8-sig"))
folder = intake / "attachments"
folder.mkdir(exist_ok=True)
pdf = folder / "uncut-method-vocab-list.pdf"
data = urllib.request.urlopen(source["url"], timeout=90).read()
if not data.startswith(b"%PDF-"):
    raise ValueError("Observed source did not return PDF bytes")
if pdf.exists() and pdf.read_bytes() != data:
    raise ValueError("Existing PDF differs; preserve it and use a new capture generation")
pdf.write_bytes(data)
reader = PdfReader(pdf)
texts = [page.extract_text() or "" for page in reader.pages]
txt = folder / "uncut-method-vocab-list.txt"
txt.write_text("\n\n".join(texts), encoding="utf-8")
diagnostics = {"pages": len(texts), "characters_per_page": [len(t) for t in texts],
               "blank_pages": [i+1 for i, t in enumerate(texts) if not t.strip()],
               "images_per_page": [len(page.images) for page in reader.pages],
               "page_text": texts}
(folder / "uncut-method-vocab-list-extraction.json").write_text(json.dumps(diagnostics, indent=2, ensure_ascii=False), encoding="utf-8")
manifest_path = intake / "attachments.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig")) if manifest_path.exists() else []
for path, fmt in [(pdf, "pdf"), (txt, "txt")]:
    record = {"file_id": "uncut-method-vocab-list", "title": source["title"],
              "url": source["url"], "routine_urls": source["routine_urls"],
              "local_path": str(path.relative_to(intake)).replace("\\", "/"),
              "format": fmt, "status": "captured", "bytes": path.stat().st_size,
              "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
    manifest = [r for r in manifest if r.get("local_path") != record["local_path"]]
    manifest.append(record)
manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps({"pages": len(texts), "characters_per_page": diagnostics["characters_per_page"],
                  "blank_pages": diagnostics["blank_pages"], "images_per_page": diagnostics["images_per_page"],
                  "pdf_bytes": len(data), "manifest_records": len(manifest)}))
