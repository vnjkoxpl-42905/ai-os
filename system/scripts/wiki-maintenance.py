"""Maintain the wiki catalog and report structural issues without changing sources."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
WIKI = ROOT / "wiki"
START = "<!-- BEGIN GENERATED WIKI CATALOG -->"
END = "<!-- END GENERATED WIKI CATALOG -->"
RECOVERED = ROOT / "research/audit-repairs-2026-10-08/historical-links.json"


def recovery_target(source, target):
    """Resolve only explicitly recorded historical evidence with a matching hash."""
    if not RECOVERED.exists():
        return None
    entries = json.loads(RECOVERED.read_text(encoding="utf-8"))
    for entry in entries:
        if entry["page"] == source.relative_to(ROOT).as_posix() and entry["target"] == target:
            recovered = ROOT / entry["recovered"]
            if recovered.is_file() and hashlib.sha256(recovered.read_bytes()).hexdigest() == entry["sha256"]:
                return recovered.resolve()
    return None


def replace_checked(path, text, expected):
    current = path.read_bytes() if path.exists() else b""
    if hashlib.sha256(current).digest() != expected:
        raise RuntimeError(f"Concurrent change: {path.relative_to(ROOT)}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def description(path):
    text = path.read_text(encoding="utf-8")
    body = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    title = re.search(r"^# (.+)$", body, re.M)
    label = title.group(1) if title else path.stem
    lines = body.splitlines()
    summary = ""
    in_code = False
    for line in lines:
        line = line.strip()
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not line or line[0] in "#>|-*" or line.startswith("<!--"):
            continue
        line = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", lambda m: m[2] or m[1], line)
        line = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", line)
        summary = line.replace("—", ", ").replace("|", "/")[:180].strip()
        break
    return label.replace("|", "/").replace("—", ":"), summary or "See the page for its record and context."


def catalog(pages):
    path = WIKI / "index.md"
    before = path.read_bytes()
    text = before.decode("utf-8")
    groups = {}
    for page in pages:
        if page == path:
            continue
        relative = page.relative_to(WIKI)
        group = relative.parts[0] if len(relative.parts) > 1 else "Operating pages"
        label, summary = description(page)
        groups.setdefault(group, []).append(
            f"- [[wiki/{relative.with_suffix('').as_posix()}|{label}]]: {summary}"
        )
    block = [START, "", "## Complete wiki catalog", "",
             "Every Markdown page under `wiki/` is listed below; this index is the catalog itself.",
             "Regenerate this section after page changes with `py system/scripts/wiki-maintenance.py --index`.", ""]
    for group, rows in sorted(groups.items()):
        block += [f"### {group.capitalize()}", "", *rows, ""]
    block.append(END)
    block = "\n".join(block)
    if START in text or END in text:
        if text.count(START) != 1 or text.count(END) != 1:
            raise RuntimeError("Invalid catalog fences")
        first, last = text.index(START), text.index(END) + len(END)
        if last <= first:
            raise RuntimeError("Reversed catalog fences")
        text = text[:first] + block + text[last:]
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    replace_checked(path, text, hashlib.sha256(before).digest())
    print(f"Catalog updated: {len(pages)} wiki pages, including the index.")


def resolve(source, target, by_name):
    target = unquote(target.split("#", 1)[0]).strip().strip("<>")
    if not target or re.match(r"^[a-zA-Z][\w+.-]*:", target) or target.startswith("//"):
        return True, None
    candidates = [source.parent / target, ROOT / target]
    for candidate in candidates:
        for p in (candidate, candidate.with_suffix(".md") if not candidate.suffix else candidate):
            if p.exists():
                return True, p.resolve()
    matches = by_name.get(target, []) if "/" not in target and "\\" not in target else []
    if len(matches) == 1:
        return True, matches[0].resolve()
    if matches:
        return False, None
    recovered = recovery_target(source, target)
    if recovered:
        return True, recovered
    # Native automemory lives outside the Obsidian vault. Resolve actual files,
    # never invent a wiki page or accept a name solely because it says 'memory'.
    if "/" not in target and "\\" not in target:
        project_key = str(ROOT.resolve()).replace(":", "-").replace("\\", "-").replace("/", "-")
        memory = Path.home() / ".claude/projects" / project_key / "memory" / (target + ".md")
        if memory.is_file():
            return True, memory.resolve()
    return False, None


def lint(pages):
    by_name = {}
    for area in ("wiki", "corpus", "context", "references", "decisions", "students", "brainstorms", "research", "system/schema"):
        for path in (ROOT / area).rglob("*.md"):
            by_name.setdefault(path.stem, []).append(path)
    # System records such as the machine profile live directly under system/.
    # Avoid indexing dependency/runtime trees merely to recover those records.
    for path in (ROOT / "system").glob("*.md"):
        by_name.setdefault(path.stem, []).append(path)
    inbound = set()
    issues = []
    for page in pages:
        text = page.read_text(encoding="utf-8")
        if page.name.endswith(".generated.md"):
            continue
        # The index is a directory, so its links don't prove conceptual connectivity.
        content = re.sub(r"```.*?```", "", text, flags=re.S)
        content = re.sub(r"`+[^`\n]*`+", "", content)
        targets = re.findall(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]", content)
        targets += re.findall(r"(?<!!)\[[^\]\n]+\]\(([^\n)]+)\)", content)
        for target in targets:
            good, dest = resolve(page, target, by_name)
            if not good:
                issues.append(("broken-or-ambiguous-link", page.relative_to(ROOT).as_posix(), target))
            elif dest and page.name != "index.md" and dest != page.resolve():
                inbound.add(dest)
        if page.parent.name == "sources" and not re.search(r"^sources:", text, re.M):
            issues.append(("missing-source-provenance", page.relative_to(ROOT).as_posix(), "Review source metadata"))
    for page in pages:
        if page.parent.name in ("sources", "entities", "concepts", "synthesis") and page.resolve() not in inbound:
            issues.append(("possible-orphan", page.relative_to(ROOT).as_posix(), "No inbound link beyond the catalog"))
    out = ROOT / "system/generated/wiki-lint.generated.tsv"
    before = out.read_bytes() if out.exists() else b""
    text = "kind\tpage\tdetail\n" + "".join("\t".join(v.replace("\t", " ").replace("\n", " ") for v in row) + "\n" for row in issues)
    replace_checked(out, text, hashlib.sha256(before).digest())
    print(f"Structural lint: {len(pages)} wiki pages; {len(issues)} findings. Report: system/generated/wiki-lint.generated.tsv")
    print("Semantic contradictions, stale claims, and knowledge gaps still require a source-grounded review.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", action="store_true")
    parser.add_argument("--lint", action="store_true")
    args = parser.parse_args()
    if not args.index and not args.lint:
        parser.error("Choose --index, --lint, or both")
    pages = sorted(WIKI.rglob("*.md"))
    if args.index:
        catalog(pages)
    if args.lint:
        lint(pages)


if __name__ == "__main__":
    main()
