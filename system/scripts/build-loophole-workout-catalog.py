"""Compile captured, user-authorized Loophole workout pages without network access.

Run after browser capture finishes. --archive copies and verifies immutable source
bytes, refusing to replace any existing evidence with different bytes.
"""
import argparse
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import tempfile
import posixpath
import zipfile
import xml.etree.ElementTree as ET
import unicodedata
from urllib.parse import urlsplit, parse_qs

ROOT = Path(__file__).resolve().parents[2]
BASE = "https://new.theloophole.com"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class SemanticHTML(HTMLParser):
    """Keep authored structure; discard executable markup and app chrome styling."""
    allowed = {"p", "div", "span", "section", "article", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "li", "strong", "b", "em", "i", "u", "br", "blockquote", "table", "thead", "tbody", "tr", "th", "td", "a", "sup", "sub", "hr"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.hidden = 0
        self.stack = []

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style", "svg", "iframe"}:
            self.hidden += 1
        if self.hidden or tag not in self.allowed:
            if not self.hidden and tag == "button":
                self.parts.append(" ")
            return
        attr = dict(attrs)
        safe = ""
        if tag == "a":
            href = attr.get("href", "")
            if href.startswith("/"):
                href = BASE + href
            if href.startswith(("https://", "http://", "#")):
                safe = ' href="' + html.escape(href, quote=True) + '" rel="noreferrer"'
        if tag == "ol" and attr.get("start", "").isdigit():
            safe = ' start="' + attr["start"] + '"'
        self.parts.append("<" + tag + safe + ">")
        if tag not in {"br", "hr"}:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in {"script", "style", "svg", "iframe"}:
            self.hidden = max(0, self.hidden - 1)
            return
        if not self.hidden and tag in self.stack:
            while self.stack:
                closing = self.stack.pop()
                self.parts.append("</" + closing + ">")
                if closing == tag:
                    break

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(html.escape(data))


class FootnoteCounter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.count = 0

    def handle_starttag(self, tag, attrs):
        if "cursor-help" in dict(attrs).get("class", "").split():
            self.count += 1


def semantic(value):
    parser = SemanticHTML()
    parser.feed(value)
    while parser.stack:
        parser.parts.append("</" + parser.stack.pop() + ">")
    return "".join(parser.parts)


def readable_html(value):
    # Source navigation is provenance, not a substitute for the inline content.
    return re.sub(r"<a\b[^>]*>", "<span>", semantic(value)).replace("</a>", "</span>")


class MarkdownTree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = ["root", {}, []]
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = [tag, dict(attrs), []]
        self.stack[-1][2].append(node)
        if tag not in {"br", "hr"}:
            self.stack.append(node)

    def handle_endtag(self, tag):
        if len(self.stack) > 1 and self.stack[-1][0] == tag:
            self.stack.pop()

    def handle_data(self, value):
        self.stack[-1][2].append(value)


def markdown(value):
    tree = MarkdownTree()
    tree.feed(semantic(value))

    def render(node):
        if isinstance(node, str):
            return re.sub(r"\s+", " ", node)
        tag, attrs, children = node
        if tag in {"ol", "ul"}:
            lines = []
            number = int(attrs.get("start", "1"))
            for child in children:
                if isinstance(child, str) or child[0] != "li":
                    continue
                body = render(child).strip()
                prefix = f"{number}. " if tag == "ol" else "- "
                parts = body.splitlines() or [""]
                lines.append(prefix + parts[0] + "\n" + "\n".join(" " * len(prefix) + line if line else "" for line in parts[1:]))
                number += 1
            return "\n\n" + "\n".join(lines) + "\n\n"
        inner = "".join(render(child) for child in children)
        if tag.startswith("h") and len(tag) == 2 and tag[1].isdigit():
            return "\n\n" + "#" * min(6, int(tag[1]) + 1) + " " + inner.strip() + "\n\n"
        if tag in {"strong", "b"}:
            return "**" + inner.strip() + "**" if inner.strip() else ""
        if tag in {"em", "i"}:
            return "*" + inner.strip() + "*" if inner.strip() else ""
        if tag == "a":
            return inner.strip() + ("\n\n" if "\n" in inner.strip() else " ")
        if tag == "span":
            return inner + " " if inner.strip() else inner
        if tag == "br":
            return "\n"
        if tag == "hr":
            return "\n\n---\n\n"
        if tag in {"div", "p", "section", "article", "blockquote", "tr", "table"}:
            return "\n\n" + inner.strip() + "\n\n" if inner.strip() else ""
        if tag in {"td", "th"}:
            return inner.strip() + " | "
        return inner

    return re.sub(r"\n[ \t]*\n(?:[ \t]*\n)+", "\n\n", render(tree.root)).strip()


def instructional_export(path):
    """Return every authored nonempty workbook cell or complete document text."""
    if path.suffix.lower() == ".txt":
        text = path.read_text(encoding="utf-8-sig")
        return text, "<pre class=\"exact\">" + html.escape(text) + "</pre>"
    if path.suffix.lower() != ".xlsx":
        return "", ""
    ns = {"s": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    relns = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
    md, fragments = [], []
    with zipfile.ZipFile(path) as package:
        shared = []
        if "xl/sharedStrings.xml" in package.namelist():
            root = ET.fromstring(package.read("xl/sharedStrings.xml"))
            shared = ["".join(item.itertext()) for item in root.findall("s:si", ns)]
        rels = {r.attrib["Id"]: r.attrib["Target"] for r in ET.fromstring(package.read("xl/_rels/workbook.xml.rels"))}
        workbook = ET.fromstring(package.read("xl/workbook.xml"))
        for sheet in workbook.findall("s:sheets/s:sheet", ns):
            name = sheet.attrib["name"]
            target = rels[sheet.attrib["{" + relns + "}id"]]
            sheet_path = target.lstrip("/") if target.startswith("/") else posixpath.normpath("xl/" + target)
            root = ET.fromstring(package.read(sheet_path))
            dimension = root.find("s:dimension", ns)
            area = dimension.attrib.get("ref", "unknown") if dimension is not None else "unknown"
            cells = []
            for cell in root.findall("s:sheetData/s:row/s:c", ns):
                value = cell.find("s:v", ns)
                formula = cell.find("s:f", ns)
                inline = cell.find("s:is", ns)
                text = value.text or "" if value is not None else ""
                if cell.attrib.get("t") == "s" and text:
                    text = shared[int(text)]
                elif inline is not None:
                    text = "".join(inline.itertext())
                if formula is not None:
                    text = "=" + (formula.text or "") + (" (cached value: " + text + ")" if text else "")
                if text.strip():
                    cells.append((cell.attrib.get("r", ""), text))
            merges = [m.attrib.get("ref", "") for m in root.findall("s:mergeCells/s:mergeCell", ns)]
            md.append(f"### Worksheet: {name}\n\nUsed range: `{area}`. Every nonempty authored value/formula follows; blank formatted cells are represented by the used range." + (" Merged ranges: " + ", ".join(merges) + "." if merges else ""))
            md.append("| Cell | Complete value or formula |\n|---|---|\n" + "\n".join("| " + coordinate + " | " + text.replace("|", "\\|").replace("\n", "<br>") + " |" for coordinate, text in cells))
            fragments.append("<h3>Worksheet: " + html.escape(name) + "</h3><p>Used range: " + html.escape(area) + ". All nonempty authored values/formulas; blank formatted cells omitted.</p><table><thead><tr><th>Cell</th><th>Complete value or formula</th></tr></thead><tbody>" + "".join("<tr><td>" + html.escape(c) + "</td><td>" + html.escape(t).replace("\n", "<br>") + "</td></tr>" for c, t in cells) + "</tbody></table>")
    return "\n\n".join(md), "".join(fragments)


def workout_document(record, archive):
    r = record
    parts = [f"# {r['name']}",
             "| Section type | Prep stage | Challenge index |\n|---|---|---|\n| " + ", ".join(r["section_types"]) + " | " + ", ".join(r["prep_stages"]) + " | " + r["challenge_index"] + " |",
             "This file contains the complete captured workout, its inline instruction footnotes, related working prep-map content and readable instructional template contents. Original source wording remains attributed to Loophole Online / Ellen Cassidy.",
             "## Complete expanded overview", markdown(r["overview"].get("html", "")),
             "## Complete workout details", markdown(r["detail"].get("html", "")),
             "## Inline instruction footnotes"]
    classification = ["## Filter classification", "| Filter | Captured classification |\n|---|---|",
                      "| Challenge Index category | " + (", ".join(r["challenge_filters"]) or "Unknown: observed facet membership not available") + " |",
                      "| Workout Pack | " + (", ".join(r["workout_packs"]) or "Unknown: no pack captured") + " |"]
    for dimension in ("Level", "Sections to Use", "Timing Compatible", "How to Time", "Volume", "Intensity"):
        classification.append("| " + dimension + " | " + (", ".join(r["useful_filters"].get(dimension, [])) or "Unknown: observed facet membership not available") + " |")
    classification.append("Membership source: " + "; ".join(k + ": " + v for k, v in r["filter_mapping_status"].items()) + ". Full original workout wording below is unchanged.")
    parts.insert(3, "\n\n".join(classification))
    notes = r["footnotes"].get("notes", [])
    if not notes:
        parts.append("No inline instruction footnotes were present in this workout's captured page.")
    for index, note in enumerate(notes, 1):
        parts.extend([f"### Footnote {index}", markdown(note.get("html", "")),
                      "<details><summary>Exact captured footnote text</summary>\n\n<pre>" + html.escape(note.get("text", "")) + "</pre>\n</details>"])
    parts.append("## Related prep-map content, included in full")
    if not r["inline_prep"]:
        parts.append("No working related prep-map page was captured for this workout. Original references and their status are retained in provenance below.")
    elif any(p["availability"] != "captured" for p in r["prep_map_points"]):
        parts.append("Some original stage-specific links returned a source error. The observed working same-topic pages are included below; this does not assert that an unavailable stage variant had identical content.")
    for point in r["inline_prep"]:
        parts.extend(["### " + point.get("name", "Prep-map point"), markdown(point.get("html", "")),
                      "<details><summary>Exact captured prep-map text</summary>\n\n<pre>" + html.escape(point.get("text", "")) + "</pre>\n</details>"])
    parts.append("## Instructional templates and documents, included here")
    parts.append(r["template_markdown"] or "This workout has no saved instructional document/template content.")
    provenance = ["<details><summary>Source files, original URLs and verification</summary>",
                  f"Original workout URL: {r['url']}",
                  f"[Immutable provenance and hashes](../../../../raw/sources/{archive.name}/PROVENANCE.md)",
                  "[Exact detail text](detail.txt) · [Original detail HTML](detail.html) · [Footnotes](footnotes.json) · [Structured source](source.json) · [All workouts](../README.md)"]
    for point in r["prep_map_points"]:
        provenance.append("- " + point["name"] + ": " + point["availability"] + "; original URL " + point["url"] + ("; related captured URLs " + ", ".join(point["related_captured_urls"]) if point["related_captured_urls"] else ""))
    for attachment in r["attachments"]:
        provenance.append("- Saved export: [" + attachment["export_mime"] + "](../" + attachment["archive_href"] + "); SHA-256 `" + attachment.get("sha256", "") + "`.")
    provenance.append("</details>")
    parts.append("\n\n".join(provenance))
    parts.append("<details><summary>Exact complete captured workout text</summary>\n\n<pre>" + html.escape(r["detail"].get("text", "")) + "</pre>\n</details>")
    return "\n\n".join(parts) + "\n"


def slug(url):
    return re.sub(r"[^a-z0-9-]+", "-", urlsplit(url).path.rstrip("/").split("/")[-1].lower()).strip("-")


def point_key(url):
    return re.sub(r"[^a-z0-9-]+", "-", urlsplit(url).path.strip("/").lower()).strip("-")


def workout_url(row):
    value = row.get("url", "")
    if "/workouts/" in value:
        return value
    return next((link.get("url", "") for link in row.get("links", []) if "/workouts/" in link.get("url", "")), "")


def field(text, start, end):
    return text.split(start, 1)[1].split(end, 1)[0].strip() if start in text and end in text.split(start, 1)[1] else ""


def name_key(value):
    return "".join(c for c in unicodedata.normalize("NFKC", value).casefold() if c.isalnum())


def facet_dimension(option):
    group = option.get("group", "")
    dimension = option.get("dimension", option.get("category", option.get("subcategory", "")))
    return dimension or group


def apply_facets(records, options, useful_options):
    """Observed membership, not heuristic interpretation of workout prose."""
    dimensions = {"Level", "Sections to Use", "Timing Compatible", "Timing Compatible With", "How to Time", "Volume", "Intensity"}
    for r in records:
        r["challenge_filters"] = []
        r["useful_filters"] = {}
        observed_packs = []
        r["filter_mapping_status"] = {"section_type": "captured overview", "prep_stage": "captured overview", "challenge_index": "unknown: facet membership not captured", "workout_pack": "captured detail workoutPack URL", "useful_filters": "unknown: facet membership not captured"}
        r["useful_filter_sources"] = {}
        for dimension, fact in (("Level", "LEVEL"), ("Sections to Use", "SECTIONS TO USE"), ("Timing Compatible", "TIMING COMPATIBLE WITH"), ("How to Time", "HOW TO TIME")):
            raw = r["source_quick_facts"].get(fact, "")
            values = [v.strip() for v in raw.split(",")] if raw else []
            values = [{"35m": "35 Minutes", "53m": "53 Minutes", "70m": "70 Minutes"}.get(value, value) for value in values]
            allowed = {o["name"] for group in useful_options if group.get("group") == dimension for o in group.get("options", [])}
            if values and all(v in allowed for v in values):
                r["useful_filters"][dimension] = values
                r["useful_filter_sources"][dimension] = "captured workout quick facts; labels matched to observed filter options"
            else:
                r["useful_filter_sources"][dimension] = "unknown: source fact or matching observed option unavailable"
        for option in options:
            names = option.get("memberNames", option.get("member_names", []))
            if not any(name_key(str(name)) == name_key(r["name"]) for name in names):
                continue
            group = option.get("group", "")
            dimension = facet_dimension(option)
            dimension = next((d for d in dimensions if name_key(d) == name_key(dimension)), dimension)
            label = option.get("name", option.get("label", ""))
            if "challenge" in group.casefold():
                r["challenge_filters"].append(label)
                r["filter_mapping_status"]["challenge_index"] = "observed facet membership"
            elif "pack" in group.casefold():
                observed_packs.append(label)
                r["filter_mapping_status"]["workout_pack"] = "observed facet membership"
            elif dimension in dimensions or "useful" in group.casefold():
                if dimension == "Timing Compatible With":
                    dimension = "Timing Compatible"
                r["useful_filters"].setdefault(dimension, []).append(label)
                r["useful_filters"][dimension] = sorted(set(r["useful_filters"][dimension]))
                r["useful_filter_sources"][dimension] = "observed live facet membership"
                r["filter_mapping_status"]["useful_filters"] = "observed facet membership"
        if observed_packs:
            r["workout_packs"] = sorted(set(observed_packs))
        if r["useful_filter_sources"]:
            r["filter_mapping_status"]["useful_filters"] = "per-dimension source recorded in useful_filter_sources"


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    previous = path.read_bytes() if path.exists() else None
    content = value.encode("utf-8")
    if previous == content:
        return
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as handle:
        temporary = Path(handle.name)
        handle.write(content)
    current = path.read_bytes() if path.exists() else None
    if current != previous:
        raise RuntimeError(f"Concurrent edit detected; new bytes preserved at {temporary}")
    temporary.replace(path)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", type=Path, default=ROOT / "raw/inbox/loophole-workouts-2026-10-14")
    ap.add_argument("--output", type=Path, default=ROOT / "corpus/loophole-online/workouts")
    ap.add_argument("--archive", action="store_true")
    ap.add_argument("--archive-dir", type=Path, help="New immutable source generation; never overwrites an earlier archive")
    ap.add_argument("--capture-start", default="2026-10-14")
    ap.add_argument("--capture-end", default="2026-10-15")
    ap.add_argument("--facets", type=Path, default=ROOT / "raw/sources/loophole-workout-filters-2026-10-15/facets.json")
    args = ap.parse_args()
    facet_options = []
    useful_options = []
    useful_path = args.facets.parent / "options.json"
    if useful_path.exists():
        useful_options = json.loads(useful_path.read_text(encoding="utf-8-sig"))
    if args.facets.exists():
        facet_payload = json.loads(args.facets.read_text(encoding="utf-8-sig"))
        facet_options = facet_payload.get("options", []) if isinstance(facet_payload, dict) else facet_payload
        if not isinstance(facet_options, list):
            raise ValueError("Facet options must be an array of observed memberships")
    archive = args.archive_dir or ROOT / "raw/sources" / args.input.name
    archive = archive.resolve()
    if not archive.is_relative_to((ROOT / "raw/sources").resolve()):
        raise ValueError("Archive generation must be under raw/sources")
    captures = {}
    for name in ("overviews", "details", "prep-points", "footnotes", "attachments"):
        path = args.input / (name + ".json")
        captures[name] = json.loads(path.read_text(encoding="utf-8-sig")) if path.exists() else []
        if not isinstance(captures[name], list):
            raise ValueError(f"{path}: expected array")
    overviews, details, points = (captures[n] for n in ("overviews", "details", "prep-points"))
    footnote_lookup = {row.get("url"): row for row in captures["footnotes"]}
    issues = []
    for group, rows in captures.items():
        if group in {"attachments", "footnotes"}:
            continue
        for row in rows:
            for key in ("text", "html"):
                if "[Truncated]" in row.get(key, ""):
                    issues.append(f"Truncated {group} {key}: " + row.get("url", row.get("name", "")))
    by_url = {}
    for detail in details:
        url = detail.get("url", "")
        if not url or url in by_url:
            issues.append("Missing or duplicate detail URL: " + url)
        by_url[url] = detail
    seen = set()
    records = []
    referenced = set()
    for overview in overviews:
        url = workout_url(overview)
        if not url or url in seen:
            issues.append("Missing or duplicate overview URL: " + url)
            continue
        seen.add(url)
        detail = by_url.get(url, {})
        if not detail.get("text", "").strip() or not detail.get("html", "").strip():
            issues.append("Missing full detail text/HTML: " + url)
        if detail.get("status") == "source-error":
            issues.append("Workout detail source error: " + url)
        if detail.get("remainingExpanders", detail.get("remaining_expanders", 0)):
            issues.append("Workout detail has unexpanded controls: " + url)
        text = overview.get("text", "")
        section = field(text, "Section Type", "Prep Stage").split()
        stage = field(text, "Prep Stage", "Challenge Index").split()
        challenge = field(text, "Challenge Index", "Prep Map Points")
        if not section or not stage or not challenge:
            issues.append("Missing overview section/prep-stage/challenge metadata: " + url)
        links = overview.get("links", []) + detail.get("links", [])
        prep = {link["url"]: link.get("text", "") for link in links if "/prep-map/" in link.get("url", "")}
        referenced.update(prep)
        record = {"name": overview.get("name", detail.get("name", slug(url))), "slug": slug(url), "url": url, "section_types": section, "prep_stages": stage, "challenge_index": challenge, "prep_map_points": [{"url": u, "name": n, "key": point_key(u)} for u, n in prep.items()], "overview": overview, "detail": detail}
        record["workout_packs"] = sorted({value for link in detail.get("links", []) for value in parse_qs(urlsplit(link.get("url", "")).query).get("workoutPack", [])})
        record["source_quick_facts"] = {}
        fact_labels = ["LEVEL", "MINIMUM TIME", "TIMING COMPATIBLE WITH", "SECTIONS TO USE", "HOW TO TIME", "VOLUME", "INTENSITY"]
        for label in fact_labels:
            match = re.search(r"(?im)^" + re.escape(label) + r"\s*\n([^\n]+)", detail.get("text", ""))
            if match:
                record["source_quick_facts"][label] = match.group(1).strip()
        counter = FootnoteCounter()
        counter.feed(detail.get("html", ""))
        footnotes = footnote_lookup.get(url, {"url": url, "count": 0, "notes": []})
        actual = len(footnotes.get("notes", []))
        if actual != counter.count or footnotes.get("count", actual) != actual:
            issues.append(f"Footnote count mismatch ({actual} captured / {counter.count} expected): {url}")
        if any(not n.get("text", "").strip() or not n.get("html", "").strip() for n in footnotes.get("notes", [])):
            issues.append("Empty footnote capture: " + url)
        record["footnotes"] = footnotes
        record["expected_footnote_count"] = counter.count
        record["attachments"] = [{**a, "archive_href": "../../../raw/sources/" + archive.name + "/" + a.get("local_path", "")} for a in captures["attachments"] if a.get("workout") == record["name"]]
        for attachment in record["attachments"]:
            if attachment.get("status") == "captured":
                path = args.input / attachment["local_path"]
                if not path.is_file() or sha(path) != attachment.get("sha256"):
                    issues.append("Attachment missing or hash mismatch: " + attachment.get("url", ""))
        records.append(record)
    apply_facets(records, facet_options, useful_options)
    filter_mapping_counts = {"section_type": sum(bool(r["section_types"]) for r in records), "prep_stage": sum(bool(r["prep_stages"]) for r in records), "challenge_index": sum(bool(r["challenge_filters"]) for r in records), "workout_pack": sum(bool(r["workout_packs"]) for r in records)}
    for dimension in ("Level", "Sections to Use", "Timing Compatible", "How to Time", "Volume", "Intensity"):
        filter_mapping_counts[dimension] = sum(bool(r["useful_filters"].get(dimension)) for r in records)
    unknown_filter_mappings = [{"workout": r["name"], "dimensions": [dimension for dimension in ("Level", "Sections to Use", "Timing Compatible", "How to Time", "Volume", "Intensity") if not r["useful_filters"].get(dimension)] + (["Challenge Index"] if not r["challenge_filters"] else []) + (["Workout Pack"] if not r["workout_packs"] else [])} for r in records]
    unknown_filter_mappings = [entry for entry in unknown_filter_mappings if entry["dimensions"]]
    facet_membership_checks = []
    for option in facet_options:
        group, label = option.get("group", ""), option.get("name", "")
        expected = {name_key(name) for name in option.get("memberNames", [])}
        if group == "Section Type":
            actual = {name_key(r["name"]) for r in records if (all(value in r["section_types"] for value in ("LR", "RC")) if label == "LR & RC" else label in r["section_types"])}
        elif group == "Challenge Index":
            actual = {name_key(r["name"]) for r in records if label in r["challenge_filters"]}
        elif group in {"Volume", "Intensity"}:
            actual = {name_key(r["name"]) for r in records if label in r["useful_filters"].get(group, [])}
        else:
            continue
        check = {"group": group, "name": label, "observed_count": len(expected), "compiled_count": len(actual), "matches": actual == expected}
        facet_membership_checks.append(check)
        if not check["matches"]:
            issues.append("Observed facet membership mismatch: " + group + " / " + label)
    point_urls = {p.get("url") for p in points if p.get("status") != "source-error" and p.get("text", "").strip() and p.get("html", "").strip()}
    source_errors = [p.get("url") for p in points if p.get("status") == "source-error"]
    point_lookup = {p.get("url"): p for p in points}
    resolutions = []
    for url in sorted(referenced):
        alternatives = sorted(u for u in point_urls if slug(u) == slug(url) and u != url)
        state = "captured" if url in point_urls else "source-error-with-related-capture" if url in source_errors and alternatives else "source-error" if url in source_errors else "missing"
        resolutions.append({"url": url, "availability": state, "related_captured_urls": alternatives})
        if state in {"missing", "source-error"}:
            issues.append(f"Unresolved prep-map reference ({state}): {url}")
    if len(point_lookup) != len(points):
        issues.append("Duplicate prep-map URL capture")
    for r in records:
        for point in r["prep_map_points"]:
            resolution = next(x for x in resolutions if x["url"] == point["url"])
            point.update(resolution)
        included = set()
        r["inline_prep"] = []
        for point in r["prep_map_points"]:
            urls = [point["url"]] if point["availability"] == "captured" else point["related_captured_urls"]
            for url in urls:
                if url not in included:
                    included.add(url)
                    r["inline_prep"].append({"name": point["name"], **point_lookup[url]})
        template_md, template_html = [], []
        seen_templates = set()
        for attachment in r["attachments"]:
            if attachment.get("status") != "captured" or attachment["local_path"].endswith(".pdf"):
                continue
            if attachment["file_id"] in seen_templates:
                continue
            seen_templates.add(attachment["file_id"])
            content_md, content_html = instructional_export(args.input / attachment["local_path"])
            template_md.append(content_md)
            template_html.append(content_html)
        r["template_markdown"] = "\n\n".join(template_md)
        r["template_html"] = "".join(template_html)
    for p in points:
        if p.get("remainingExpanders", p.get("remaining_expanders", 0)):
            issues.append("Prep-map page has unexpanded controls: " + p.get("url", ""))
    extras = sorted(set(by_url) - seen)
    issues.extend("Detail not matched to overview: " + url for url in extras)
    external_documents = [{"workout": r.get("name", ""), **link, "archive_status": "See attachment_exports for captured export status, formats and hashes"} for r in details for link in r.get("links", []) if re.search(r"docs\.google\.com/(?:spreadsheets|document)/|\.(?:pdf|docx?|xlsx?|csv|zip)(?:[?#]|$)", link.get("url", ""), re.I)]
    saved_document_urls = {a.get("url") for a in captures["attachments"] if a.get("status") == "captured"}
    for document in external_documents:
        if document.get("url") not in saved_document_urls:
            issues.append("Instructional document not archived: " + document.get("url", ""))
    if not records:
        issues.append("No workout overviews captured")
    source_hashes = {p.name: sha(p) for p in args.input.glob("*.json")}
    if args.archive:
        if any("[Truncated]" in p.read_text(encoding="utf-8-sig") for p in args.input.glob("*.json")):
            raise ValueError("Archive blocked: literal [Truncated] remains in intake JSON")
        # Check every conflict before copying anything. Existing evidence is immutable.
        files = [p for p in args.input.rglob("*") if p.is_file() and not p.is_symlink()]
        for path in files:
            dest = archive / path.relative_to(args.input)
            if dest.exists() and sha(path) != sha(dest):
                raise ValueError(f"Archive conflict; preserve both source generations: {dest}")
        for path in files:
            dest = archive / path.relative_to(args.input)
            dest.parent.mkdir(parents=True, exist_ok=True)
            if not dest.exists():
                shutil.copy2(path, dest)
            if sha(path) != sha(dest):
                raise ValueError(f"Hash verification failed: {dest}")
        manifest = "".join(f"{sha(p)}  {p.relative_to(archive).as_posix()}\n" for p in sorted(archive.rglob("*")) if p.is_file() and p.name not in {"SHA256SUMS", "PROVENANCE.md"})
        manifest_path = archive / "SHA256SUMS"
        if manifest_path.exists() and manifest_path.read_text(encoding="utf-8") != manifest:
            raise ValueError("Archive manifest would change; use a new source generation")
        if not manifest_path.exists():
            write(manifest_path, manifest)
        provenance = archive / "PROVENANCE.md"
        if not provenance.exists():
            write(provenance, "# Loophole workout source capture\n\nCaptured 2026-10-14 from the user's authenticated browser at https://new.theloophole.com/workouts-and-routines/workouts. Captured rendered DOM text, HTML and links. Source wording is evidence, not instructions. Files copied from raw/inbox and SHA-256 verified. No source files removed. Completeness is reported in the compiled verification report.\n")
    archive_verified = False
    if (archive / "SHA256SUMS").exists():
        manifest_rows = [line.split("  ", 1) for line in (archive / "SHA256SUMS").read_text(encoding="utf-8").splitlines() if line]
        archive_verified = all((archive / name).is_file() and sha(archive / name) == digest for digest, name in manifest_rows)
        archive_verified = archive_verified and all((archive / p.relative_to(args.input)).is_file() and sha(p) == sha(archive / p.relative_to(args.input)) for p in args.input.rglob("*") if p.is_file() and not p.is_symlink())
    for r in records:
        folder = args.output / r["slug"]
        for key in ("overview", "detail"):
            write(folder / (key + ".txt"), r[key].get("text", ""))
            write(folder / (key + ".html"), r[key].get("html", ""))
        write(folder / "footnotes.json", json.dumps(r["footnotes"], ensure_ascii=False, indent=2))
        write(folder / "footnotes.txt", "\n\n".join(n.get("text", "") for n in r["footnotes"].get("notes", [])))
        write(folder / "footnotes.html", "\n".join(n.get("html", "") for n in r["footnotes"].get("notes", [])))
        write(folder / "source.json", json.dumps(r, ensure_ascii=False, indent=2))
        write(folder / "README.md", workout_document(r, archive))
    for point in points:
        key = point_key(point.get("url", ""))
        if key:
            write(args.output / "prep-map-points" / key / "source.json", json.dumps(point, ensure_ascii=False, indent=2))
            write(args.output / "prep-map-points" / key / "text.txt", point.get("text", ""))
            write(args.output / "prep-map-points" / key / "original.html", point.get("html", ""))
    report = {"overview_count": len(overviews), "workout_count": len(records), "detail_count": len(details), "prep_point_count": len(points), "expected_footnote_count": sum(r["expected_footnote_count"] for r in records), "captured_footnote_count": sum(len(r["footnotes"].get("notes", [])) for r in records), "all_footnotes_captured": all(len(r["footnotes"].get("notes", [])) == r["expected_footnote_count"] for r in records), "referenced_prep_point_count": len(referenced), "complete_within_captured_inventory": not issues and not source_errors, "all_workout_details_captured": bool(records) and len(records) == len(details) and all(r["detail"].get("text", "").strip() and r["detail"].get("html", "").strip() and r["detail"].get("status") != "source-error" and "[Truncated]" not in r["detail"].get("html", "") and "[Truncated]" not in r["detail"].get("text", "") and not r["detail"].get("remainingExpanders", r["detail"].get("remaining_expanders", 0)) for r in records), "captured_prep_point_count": len(point_urls), "source_error_urls": source_errors, "prep_reference_resolution": resolutions, "issues": issues, "archive_hash_verified": archive_verified, "filter_facet_source": str(args.facets.relative_to(ROOT)) if args.facets.is_relative_to(ROOT) else str(args.facets), "filter_facet_sha256": sha(args.facets) if args.facets.exists() else None, "filter_facet_option_count": len(facet_options), "filter_mapping_counts": filter_mapping_counts, "unknown_filter_mappings": unknown_filter_mappings, "facet_membership_checks": facet_membership_checks, "useful_filter_options_sha256": sha(useful_path) if useful_path.exists() else None, "source_archive": archive.relative_to(ROOT).as_posix(), "source_sha256": source_hashes, "linked_instructional_documents": external_documents, "attachment_exports": captures["attachments"], "captured_attachment_export_count": sum(a.get("status") == "captured" for a in captures["attachments"]), "limits": ["Counts prove coverage of captured inventory; compare inventory against rendered pagination separately.", "Verbatim means captured rendered text and HTML; not independent audio transcription.", "Image URLs and alt text remain source metadata. Image bytes, embedded files, linked videos and audio are not downloaded by this compiler. Instructional Google document exports are preserved separately when listed as captured in attachment_exports."]}
    write(args.output / "verification.generated.json", json.dumps(report, ensure_ascii=False, indent=2))
    write(args.output / "catalog.generated.json", json.dumps({"verification": report, "facet_options": facet_options, "useful_options": useful_options, "workouts": records, "prep_map_points": points}, ensure_ascii=False, indent=2))
    rows = "\n".join(f"| [{r['name']}]({r['slug']}/README.md) | {', '.join(r['section_types'])} | {', '.join(r['prep_stages'])} | {r['challenge_index']} |" for r in records)
    write(args.output / "README.md", f"# Loophole workouts\n\n[Loophole home](../README.md) | [LR](../logical-reasoning/README.md) | [RC](../reading-comprehension/README.md) | [Shared](../shared/README.md) | [Prep-map captures](../workouts/prep-map-points/README.md)\n\n[Search and expand every captured workout](catalog.html) · [Structured catalog](catalog.generated.json) · [Coverage report](verification.generated.json)\n\nCapture started {args.capture_start}, completed {args.capture_end}. **{len(records)} workouts and {len(details)} full detail pages**, plus **{report['captured_footnote_count']} inline instruction footnotes**. All {len(points)} linked prep-map URLs were checked: **{len(point_urls)} working pages captured and {len(source_errors)} source error pages preserved**, each with related observed working-topic links where available. Eight instructional templates/documents are preserved as {report['captured_attachment_export_count']} exports (XLSX, text and PDF). The [source summary](../../../wiki/sources/loophole-workouts-2026-10-14.md) explains the corrected `-complete` archive generation; the earlier incomplete archive remains preserved and is superseded for current retrieval. Verification issues: {len(issues)}; original source errors remain explicit and are not counted as recovered content. Exact source text and original HTML are kept inside each workout folder. LR and RC are filterable views over one source record, so shared workouts are not duplicated.\n\n| Workout | Section type | Prep stage | Challenge index |\n|---|---|---|---|\n{rows}\n")
    point_titles = {p["url"]: p["name"] for r in records for p in r["prep_map_points"]}
    payload = json.dumps({"facet_options": facet_options, "useful_options": useful_options, "workouts": [{**{k: r[k] for k in ("name", "slug", "url", "section_types", "prep_stages", "challenge_index", "prep_map_points", "attachments", "expected_footnote_count", "template_html", "workout_packs", "useful_filters", "challenge_filters", "filter_mapping_status")}, "detail": {"text": r["detail"].get("text", "")}, "footnotes": {"notes": [{"text": n.get("text", "")} for n in r["footnotes"].get("notes", [])]}, "overview_html": readable_html(r["overview"].get("html", "")), "detail_html": readable_html(r["detail"].get("html", "")), "footnotes_html": "".join(readable_html(n.get("html", "")) for n in r["footnotes"].get("notes", [])), "inline_prep_html": "".join("<h3>" + html.escape(p.get("name", "Prep-map point")) + "</h3>" + readable_html(p.get("html", "")) + "<details><summary>Exact captured prep-map text</summary><pre class=\"exact\">" + html.escape(p.get("text", "")) + "</pre></details>" for p in r["inline_prep"])} for r in records], "points": [{**{k: p.get(k) for k in ("name", "url", "status", "text")}, "display_name": point_titles.get(p.get("url"), slug(p.get("url", "")).replace("-", " ")) if p.get("status") == "source-error" else p.get("name", p.get("url")), "key": point_key(p.get("url", "")), "safe_html": readable_html(p.get("html", ""))} for p in points]}, ensure_ascii=False).replace("<", "\\u003c")
    template = r'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Loophole workouts</title><style>body{font:16px/1.6 system-ui;margin:0;background:#f5faf8;color:#171712}main{max-width:1100px;margin:auto;padding:24px}header{position:sticky;top:0;background:#f5faf8;padding:12px 0;z-index:2}input,select{font:inherit;padding:8px;border:1px solid;border-radius:8px;max-width:100%}details.workout{border:2px solid;border-radius:12px;background:white;margin:12px 0}summary{cursor:pointer;padding:16px;font-weight:700}.content{padding:0 24px 24px}.tags{font-size:14px;color:#36594d}.source{border-top:1px solid #ccc;padding-top:12px}.exact{white-space:pre-wrap;font:14px/1.6 ui-monospace,monospace}a{color:#006b70}p,li{max-width:85ch}table{border-collapse:collapse}td,th{border:1px solid #ccc;padding:6px}button{font:inherit}#count{margin:8px 0}ol,ul{padding-left:28px}.filter-menu{display:inline-block;position:relative;border:1px solid;border-radius:8px;background:white;vertical-align:top}.filter-menu>summary{padding:8px 12px;font-weight:400}.filter-menu[open]{z-index:3}#useful-controls{display:grid;gap:8px;padding:12px;min-width:240px}#useful-controls label{display:grid;gap:4px;font-size:14px}#clear-useful{margin:0 12px 12px;padding:6px 10px}</style><main><nav><a href="../README.md">Loophole home</a> | <a href="../logical-reasoning/README.md">LR</a> | <a href="../reading-comprehension/README.md">RC</a> | <a href="../shared/README.md">Shared</a> | <a href="../workouts/prep-map-points/README.md">Prep-map captures</a></nav><header><h1>Loophole workouts</h1><input id="search" placeholder="Search all captured wording" aria-label="Search workouts"> <select id="section" aria-label="Section type"><option value="">Every section</option></select> <select id="stage" aria-label="Prep stage"><option value="">Every prep stage</option></select> <select id="challenge" aria-label="Challenge Index"><option value="">Every challenge index</option></select> <select id="pack" aria-label="Workout Pack"><option value="">Every workout pack</option></select> <details class="filter-menu"><summary>Useful Filters</summary><div id="useful-controls"></div><button id="clear-useful" type="button">Clear useful filters</button></details><p id="count"></p></header><p>Local reference capture, CAPTURE_DATES. <a href="verification.generated.json">Coverage and limitations</a>. Original source wording is preserved; this viewer does not run source scripts or recreate interactive exercises. Image URLs and alt text are retained in each source.json. Saved instructional document exports are linked below their workout; other media bytes are not downloaded by this compiler.</p><div id="list"></div><h2>Linked prep-map points</h2><div id="points"></div></main><script type="application/json" id="data">PAYLOAD</script><script>const data=JSON.parse(document.getElementById('data').textContent),$=id=>document.getElementById(id),esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));for(const [id,key] of [['section','section_types'],['stage','prep_stages'],['challenge','challenge_filters'],['pack','workout_packs']])for(const value of [...new Set([...data.workouts.flatMap(r=>r[key]),...(id==='section'?['LR & RC']:[])])].sort()){const o=document.createElement('option');o.value=o.textContent=value;$(id).append(o)}const usefulDimensions=['Level','Sections to Use','Timing Compatible','How to Time','Volume','Intensity'];for(const dimension of usefulDimensions){const label=document.createElement('label');label.textContent=dimension;const select=document.createElement('select');select.dataset.dimension=dimension;select.setAttribute('aria-label',dimension);const empty=document.createElement('option');empty.value='';empty.textContent='Any '+dimension.toLowerCase();select.append(empty);const observed=data.useful_options.find(g=>g.group===dimension);const values=observed?observed.options.map(o=>o.name):[...new Set(data.workouts.flatMap(r=>r.useful_filters[dimension]||[]))].sort();for(const value of values){const option=document.createElement('option');option.value=option.textContent=value;select.append(option)}select.addEventListener('input',render);label.append(select);$('useful-controls').append(label)}$('clear-useful').addEventListener('click',()=>{for(const select of document.querySelectorAll('#useful-controls select'))select.value='';render()});function render(){const q=$('search').value.toLowerCase(),s=$('section').value,t=$('stage').value,c=$('challenge').value,p=$('pack').value;const selectedUseful=[...document.querySelectorAll('#useful-controls select')].filter(el=>el.value);const rows=data.workouts.filter(r=>(!s||(s==='LR & RC'?r.section_types.includes('LR')&&r.section_types.includes('RC'):r.section_types.includes(s)))&&(!t||r.prep_stages.includes(t))&&(!c||r.challenge_filters.includes(c))&&(!p||r.workout_packs.includes(p))&&selectedUseful.every(el=>(r.useful_filters[el.dataset.dimension]||[]).includes(el.value))&&JSON.stringify(r).toLowerCase().includes(q));$('count').textContent=rows.length+' of '+data.workouts.length+' workouts';$('list').innerHTML=rows.map(r=>`<details class="workout"><summary>${esc(r.name)}<div class="tags">${esc(r.section_types.join(' / '))} · ${esc(r.prep_stages.join(' / '))} · Challenge ${esc(r.challenge_index)}</div></summary><div class="content"><p><a href="${esc(r.slug)}/README.md">Open complete workout document</a></p><h2>Overview</h2>${r.overview_html}<h2>Full workout details</h2><div class="source">${r.detail_html||'<p>Capture missing. See coverage report.</p>'}</div><h3>Instructional template/document contents</h3>${r.template_html}<details><summary>Saved original exports</summary><ul>${r.attachments.map(a=>`<li>${esc(a.export_mime)}: ${a.status==='captured'?`<a href="${esc(a.archive_href)}">Saved export</a>`:esc(a.status)} · <a href="${esc(a.url)}">Original source</a></li>`).join('')}</ul></details><h3>Instruction footnotes (${esc(r.footnotes.notes.length)} / ${esc(r.expected_footnote_count)})</h3>${r.footnotes_html}<details><summary>Exact footnote text</summary><pre class="exact">${esc(r.footnotes.notes.map(n=>n.text).join("\n\n"))}</pre></details><details><summary>Exact captured text</summary><pre class="exact">${esc(r.detail.text||'')}</pre></details><h3>Complete related prep-map content</h3>${r.inline_prep_html}<details><summary>Original source URLs and prep-map availability</summary><p><a href="${esc(r.url)}">Original workout URL</a></p><ul>${r.prep_map_points.map(p=>`<li><a href="#point-${esc(p.key)}">${esc(p.name)}</a> (${esc(p.availability)}) ${p.related_captured_urls.map(u=>`<a href="#point-${esc(u.replace(/^https?:\/\/[^/]+\//,'').replace(/[^a-z0-9-]+/g,'-'))}">Related captured page</a>`).join(' ')} · <a href="${esc(p.url)}">Original</a></li>`).join('')}</ul></details></div></details>`).join('')}for(const id of ['search','section','stage','challenge','pack'])$(id).addEventListener('input',render);$('points').innerHTML=data.points.map(p=>`<details class="workout" id="point-${esc(p.key)}"><summary>${esc(p.display_name||p.name||p.url)} (${esc(p.status||'captured')})</summary><div class="content"><a href="${esc(p.url)}">Original prep-map point</a>${p.safe_html}<details><summary>Exact captured text</summary><pre class="exact">${esc(p.text)}</pre></details></div></details>`).join('');render();document.addEventListener('click',e=>{const a=e.target.closest('a[href^="#point-"]');if(a){const target=$(a.getAttribute('href').slice(1));if(target)target.open=true}});</script></html>'''
    write(args.output / "catalog.html", template.replace("PAYLOAD", payload).replace("CAPTURE_DATES", html.escape(args.capture_start + " to " + args.capture_end)))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not issues else 2


if __name__ == "__main__":
    raise SystemExit(main())
