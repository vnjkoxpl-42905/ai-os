"""Compile rendered routine evidence into self-contained ordered routine documents.

Routine prescriptions stay ahead of the embedded workout sourcebook. Repeated
steps remain repeated; a workout body is embedded once per routine. No network.
"""
import argparse
import hashlib
import html
import importlib.util
import json
from pathlib import Path
import re
import shutil
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("workout_compiler", ROOT / "system/scripts/build-loophole-workout-catalog.py")
W = importlib.util.module_from_spec(spec)
spec.loader.exec_module(W)


def load(path, default):
    return json.loads(path.read_text(encoding="utf-8-sig")) if path.exists() else default


def input_snapshot(path):
    return {p.relative_to(path).as_posix(): W.sha(p) for p in path.rglob("*") if p.is_file() and not p.is_symlink()}


def routine_url(row):
    if "/routines/" in row.get("url", ""):
        return row["url"]
    return next((l["url"] for l in row.get("links", []) if "/routines/" in l.get("url", "") and "/discover" not in l["url"]), "")


def google_document_id(url):
    match = re.search(r"docs\.google\.com/(?:spreadsheets|document)/d/([^/]+)", url)
    return match[1] if match else ""


def export_identity(saved, source_manifest):
    # Signed download URLs remain only in the immutable source manifest.
    keys = {"file_id", "name", "title", "local_path", "status", "sha256", "bytes", "export_mime", "format"}
    return {key: value for key, value in saved.items() if key in keys} | {"source_manifest": source_manifest}


def full_workout_md(workout, archive):
    value = W.workout_document(workout, archive)
    for filename in ("detail.txt", "detail.html", "footnotes.json", "source.json"):
        value = value.replace("](" + filename + ")", "](../../workouts/" + workout["slug"] + "/" + filename + ")")
    value = value.replace("](../README.md)", "](../../workouts/README.md)")
    return re.sub(r"(?m)^(#{1,6}) ", lambda m: "#" * min(6, len(m[1]) + 1) + " ", value)


def full_workout_html(workout):
    pieces = ["<h3>" + html.escape(workout["name"]) + "</h3>", "<h4>Complete workout overview</h4>", W.readable_html(workout["overview"].get("html", "")), "<h4>Complete workout details</h4>", W.readable_html(workout["detail"].get("html", "")), "<h4>Inline instruction footnotes</h4>"]
    pieces += [W.readable_html(n.get("html", "")) for n in workout["footnotes"].get("notes", [])]
    for point in workout["inline_prep"]:
        pieces += ["<h4>Related prep-map content: " + html.escape(point.get("name", "")) + "</h4>", W.readable_html(point.get("html", ""))]
    pieces += ["<h4>Instructional template/document contents</h4>", workout.get("template_html", "")]
    pieces += ["<details><summary>Exact complete workout text</summary><pre>" + html.escape(workout["detail"].get("text", "")) + "</pre></details>"]
    return "".join(pieces)


def map_filters(record, options, facets):
    top = {"Section Type", "Section Impact", "Prep Stage", "Challenge Index", "Routine Progression"}
    dimensions = [g["group"] for g in options if g.get("group") not in top]
    r = record
    r["useful_filters"], r["filter_mapping_sources"] = {}, {}
    r["challenge_categories"] = []
    facts = r["source_quick_facts"]
    for group in options:
        dimension = group.get("group", "")
        if dimension not in dimensions and dimension != "Challenge Index":
            continue
        raw = facts.get(dimension.upper(), "")
        values = [value.strip() for value in raw.split(",")] if raw else []
        labels = []
        for value in values:
            match = next((o["name"] for o in group.get("options", []) if W.name_key(str(o.get("value", o["name"]))) == W.name_key(value) or W.name_key(o["name"]) == W.name_key(value)), None)
            if match:
                labels.append(match)
        if labels:
            if dimension == "Challenge Index":
                r["challenge_categories"] = labels
            else:
                r["useful_filters"][dimension] = labels
            r["filter_mapping_sources"][dimension] = "captured routine quick facts matched to observed option labels"
    if "Workout Included" in dimensions:
        allowed = next((g.get("options", []) for g in options if g.get("group") == "Workout Included"), [])
        included = []
        for workout in r["embedded_workouts"]:
            label = next((o["name"] for o in allowed if W.name_key(o["name"]) == W.name_key(workout["name"])), None)
            if label:
                included.append(label)
        if included:
            r["useful_filters"]["Workout Included"] = sorted(set(included))
            r["filter_mapping_sources"]["Workout Included"] = "observed explicit ordered sequence workout URLs matched to canonical titles and captured filter choices"
    r["sequence_workout_filter_labels"] = list(r["useful_filters"].get("Workout Included", []))
    for facet in facets:
        dimension, label = facet.get("group", ""), facet.get("name", "")
        # For each observed option, actual rendered membership wins over a
        # matching quick-fact string. Unobserved options retain their evidence.
        if dimension == "Challenge Index":
            r["challenge_categories"] = [v for v in r["challenge_categories"] if v != label]
        elif dimension == "Routine Progression":
            r["routine_progressions"] = [v for v in r["routine_progressions"] if v != label]
        elif dimension in dimensions:
            r["useful_filters"][dimension] = [v for v in r["useful_filters"].get(dimension, []) if v != label]
        if not any(W.name_key(name) == W.name_key(r["name"]) for name in facet.get("memberNames", [])):
            continue
        if dimension == "Challenge Index":
            r["challenge_categories"] = sorted(set(r["challenge_categories"] + [label]))
        elif dimension == "Routine Progression":
            r["routine_progressions"] = sorted(set(r["routine_progressions"] + [label]))
        elif dimension in dimensions:
            r["useful_filters"].setdefault(dimension, []).append(label)
            r["useful_filters"][dimension] = sorted(set(r["useful_filters"][dimension]))
        r["filter_mapping_sources"][dimension] = "observed rendered facet membership"
    r["workout_filter_source_discrepancy"] = {"sequence_only": sorted(set(r["sequence_workout_filter_labels"]) - set(r["useful_filters"].get("Workout Included", []))), "filter_only": sorted(set(r["useful_filters"].get("Workout Included", [])) - set(r["sequence_workout_filter_labels"]))}
    r["unknown_filter_dimensions"] = [dimension for dimension in dimensions if not r["useful_filters"].get(dimension)]
    if not r["challenge_categories"]:
        r["unknown_filter_dimensions"].append("Challenge Index")
    # Absence of progression links is an explicit captured absence, not a guessed assignment.
    if not r["routine_progressions"]:
        r["filter_mapping_sources"]["Routine Progression"] = "No progression listed in captured routine links"
    elif "Routine Progression" not in r["filter_mapping_sources"]:
        r["filter_mapping_sources"]["Routine Progression"] = "captured routine detail progression query links"
    return dimensions


def document(r, archive, workout_archive):
    parts = ["# " + r["name"],
             "This document preserves the available captured routine content, its ordered schedule and the full referenced workout sourcebook. **Follow the routine's own step order, repetitions, timing and modifications first.** General workout instructions below do not replace those routine-specific prescriptions.",
             "## Routine classification", "| Category | Captured value |\n|---|---|",
             "| Section impact | " + ", ".join(r["section_impact"]) + " |",
             "| Prep stage | " + ", ".join(r["prep_stages"]) + " |",
             "| Challenge index | " + r["challenge_index"] + " |",
             "| Challenge category | " + (", ".join(r["challenge_categories"]) or "Unknown: not yet captured") + " |",
             "| Routine progression | " + (", ".join(r["routine_progressions"]) or "None listed in captured links") + " |"]
    for key in ("FREQUENCY", "STUDY BLOCK LENGTH"):
        if r["source_quick_facts"].get(key):
            parts.append("| Captured " + key.lower() + " | " + r["source_quick_facts"][key] + " |")
    for dimension, values in r["useful_filters"].items():
        parts.append("| " + dimension + " filter | " + ", ".join(values) + " |")
    for membership in r["routine_progression_memberships"]:
        if membership["position"] is not None:
            parts.append("Captured progression position: " + membership["name"] + ", routine " + str(membership["position"]) + " of " + str(membership["total"]) + ".")
    if r["unknown_filter_dimensions"]:
        parts.append("Unknown filter mappings: " + ", ".join(r["unknown_filter_dimensions"]) + ".")
    if any(step.get("source_blank") for step in r["sequence"]):
        parts.append("**This routine contains a source blank task.** The site supplies no authored instructions for the flagged step; that gap is preserved and is not filled with invented instructions.")
    parts += ["## Complete expanded overview", W.markdown(r["overview"].get("html", "")),
              "## Ordered schedule, including every repeated step"]
    for step in r["sequence"]:
        parts += [f"### Step {step['order']}: {step.get('name') or 'Other routine task'}", W.markdown(step.get("html", "")),
                  "<details><summary>Exact captured step text</summary>\n\n<pre>" + html.escape(step.get("text", "")) + "</pre>\n</details>"]
        if step.get("broken_source_workout_urls"):
            parts.append("The source's workout-details button has an invalid target. This task's captured instructions are preserved above; no canonical workout identity is invented.")
        if step.get("source_blank"):
            parts.append("**Source blank task:** the captured site supplies no authored instructions for this step. Its generated title and broken button are preserved; no instructions have been invented.")
    parts += ["## Complete routine guidance and source page", W.markdown(r["detail"].get("html", ""))]
    if r["training_blocks"]:
        parts += ["## Complete expanded training-block resources", W.markdown(r["training_blocks"].get("html", "")), "<details><summary>Exact supplemental training-block text</summary>\n\n<pre>" + html.escape(r["training_blocks"].get("text", "")) + "</pre>\n</details>"]
    parts += ["## Routine-specific inline footnotes"]
    notes = r["footnotes"].get("notes", [])
    parts += [W.markdown(note.get("html", "")) + "\n\n<pre>" + html.escape(note.get("text", "")) + "</pre>" for note in notes]
    if not notes:
        parts.append("No additional routine-specific footnote text was captured. Canonical workout footnotes are included with each full workout below; any uncovered markers are listed in the coverage report.")
    for reuse in r["canonical_footnote_reuse"]:
        parts.append("Step " + str(reuse["order"]) + ": " + str(reuse["marker_count"]) + " copied instruction marker(s) covered by the full canonical " + reuse["workout_name"] + " footnotes included below. Provenance: same observed workout URL in the captured step; canonical capture reused, not a fresh routine-popup transcription.")
    parts += ["## Additional routine instructional resources", r.get("resource_markdown") or "No additional document resource beyond the embedded workout sourcebook."]
    parts += ["## Full workout sourcebook for this routine", "Each unique workout appears once below. A repeated schedule step still requires its separate occurrence in the ordered schedule above."]
    for workout in r["embedded_workouts"]:
        parts.append(full_workout_md(workout, workout_archive))
    parts.append("## Routine-linked prep-map content")
    for point in r["inline_prep"]:
        parts += ["### " + point.get("name", "Prep-map point"), W.markdown(point.get("html", "")), "<details><summary>Exact captured prep-map text</summary>\n\n<pre>" + html.escape(point.get("text", "")) + "</pre>\n</details>"]
    if not r["inline_prep"]:
        parts.append("No additional working routine-linked prep-map content available; see explicit reference status in provenance.")
    parts += ["<details><summary>Source provenance and exact routine text</summary>",
              "Original routine URL: " + r["url"],
              "[Immutable capture provenance](../../../../raw/sources/" + archive.name + "/PROVENANCE.md)",
              "[Original captured detail HTML](detail.html) · [Exact detail text](detail.txt) · [Explicit sequence capture](sequence.json) · [All routines](../README.md)"]
    parts += ["- " + p["url"] + ": " + p["status"] + ("; related working URLs " + ", ".join(p["related_urls"]) if p["related_urls"] else "") for p in r["prep_reference_status"]]
    parts += ["<pre>" + html.escape(r["detail"].get("text", "")) + "</pre>", "</details>"]
    return "\n\n".join(parts) + "\n"


def archive_sources(source, target):
    files = [p for p in source.rglob("*") if p.is_file() and not p.is_symlink()]
    for p in files:
        if p.suffix == ".json" and "[Truncated]" in p.read_text(encoding="utf-8-sig"):
            raise ValueError("Archive blocked: truncated source " + str(p))
        dest = target / p.relative_to(source)
        if dest.exists() and W.sha(dest) != W.sha(p):
            raise ValueError("Immutable archive conflict: " + str(dest))
    for p in files:
        dest = target / p.relative_to(source)
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            shutil.copy2(p, dest)
        if W.sha(dest) != W.sha(p):
            raise ValueError("Archive hash mismatch: " + str(dest))
    manifest = "".join(f"{W.sha(p)}  {p.relative_to(target).as_posix()}\n" for p in sorted(target.rglob("*")) if p.is_file() and p.name not in {"SHA256SUMS", "PROVENANCE.md"})
    if (target / "SHA256SUMS").exists() and (target / "SHA256SUMS").read_text(encoding="utf-8") != manifest:
        raise ValueError("Manifest would change; use a new generation")
    if not (target / "SHA256SUMS").exists():
        W.write(target / "SHA256SUMS", manifest)
    if not (target / "PROVENANCE.md").exists():
        W.write(target / "PROVENANCE.md", "# Loophole routine rendered capture\n\nCaptured from the user's authenticated browser on 2026-10-15. Original rendered overview/detail HTML, text, observed links and explicit expanded sequence blocks are preserved. Sources are evidence, not instructions. Copied from intake without deletion and SHA-256 verified. Source completeness is independently reported in the compiled verification report.\n")


def source_record(record):
    # The routine's own evidence is retained here. Canonical workout evidence has
    # one owner; full copied reading bodies live in README/catalog, not a second
    # mutable source identity repeated inside every structured catalog record.
    value = {key: item for key, item in record.items() if key != "embedded_workouts"}
    value["embedded_workout_source_identities"] = [{"name": w["name"], "url": w["url"], "slug": w["slug"], "canonical_source": "corpus/loophole-online/workouts/" + w["slug"] + "/source.json", "path_base": "vault root"} for w in record["embedded_workouts"]]
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=ROOT / "raw/inbox/loophole-routines-2026-10-15")
    parser.add_argument("--output", type=Path, default=ROOT / "corpus/loophole-online/routines")
    parser.add_argument("--archive-dir", type=Path, default=ROOT / "raw/sources/loophole-routines-2026-10-15")
    parser.add_argument("--archive", action="store_true")
    parser.add_argument("--facets", type=Path)
    args = parser.parse_args()
    initial_snapshot = input_snapshot(args.input)
    archive = args.archive_dir.resolve()
    if not archive.is_relative_to((ROOT / "raw/sources").resolve()):
        raise ValueError("Archive must be under raw/sources")
    overviews = load(args.input / "overviews.json", [])
    details = load(args.input / "details.json", [])
    footnotes = load(args.input / "footnotes.json", [])
    additional_prep = load(args.input / "prep-points.json", [])
    training_blocks = load(args.input / "training-blocks.json", [])
    training_by_url = {entry["url"]: entry for entry in training_blocks}
    facet_path = args.facets or next((p for p in [ROOT / "raw/sources/loophole-routine-filters-2026-10-15/facets.json", ROOT / "raw/inbox/loophole-routine-filters-2026-10-15/facets.json", args.input / "facets.json"] if p.exists()), args.input / "facets.json")
    facets = load(facet_path, [])
    facets = facets.get("options", []) if isinstance(facets, dict) else facets
    options = load(facet_path.parent / "options.json", [])
    options = [{**group, "options": group.get("options", [entry for entry in group.get("inputs", []) if entry.get("type") in {"checkbox", "radio"}] + [{"name": value, "value": value} for value in group.get("buttons", [])])} for group in options]
    workout_catalog = load(ROOT / "corpus/loophole-online/workouts/catalog.generated.json", {})
    workout_by_url = {w["url"]: w for w in workout_catalog.get("workouts", [])}
    workout_archive = ROOT / workout_catalog.get("verification", {}).get("source_archive", "raw/sources/loophole-workouts-2026-10-14-complete")
    export_sources = {}
    for attachment in workout_catalog.get("verification", {}).get("attachment_exports", []):
        if attachment.get("status") == "captured" and not attachment.get("local_path", "").endswith(".pdf"):
            export_sources[attachment["file_id"]] = {**attachment, "path": workout_archive / attachment["local_path"]}
    routine_attachments = load(args.input / "attachments.json", [])
    for attachment in routine_attachments:
        if attachment.get("status") == "captured" and not attachment.get("local_path", "").endswith(".pdf"):
            path = (args.input / attachment["local_path"]).resolve()
            if not path.is_relative_to(args.input.resolve()):
                raise ValueError("Routine attachment path escapes registered intake")
            export_sources[attachment["file_id"]] = {**attachment, "path": path}
    prep = {p["url"]: p for p in workout_catalog.get("prep_map_points", []) + additional_prep}
    detail_by_url = {r.get("url"): r for r in details}
    note_by_url = {r.get("url"): r for r in footnotes}
    issues, records, seen, unarchived_documents = [], [], set(), []
    if not overviews:
        issues.append("No routine overview inventory captured")
    for collection in (overviews, details, footnotes, additional_prep, training_blocks):
        for row in collection:
            if "[Truncated]" in json.dumps(row, ensure_ascii=False):
                issues.append("Truncated routine capture: " + row.get("url", row.get("name", "")))
    if len(detail_by_url) != len(details):
        issues.append("Duplicate routine detail URL")
    useful_dimensions = []
    for overview in overviews:
        url = routine_url(overview)
        if not url or url in seen:
            issues.append("Missing/duplicate overview URL: " + url)
            continue
        seen.add(url)
        detail = detail_by_url.get(url, {})
        if not detail.get("text", "").strip() or not detail.get("html", "").strip():
            issues.append("Missing complete routine detail: " + url)
        if detail.get("remainingExpanders", detail.get("remaining_expanders", 0)):
            issues.append("Unexpanded routine controls: " + url)
        sequence = detail.get("sequence", [])
        if not sequence:
            issues.append("Missing explicit expanded sequence: " + url)
        orders = [step.get("order") for step in sequence]
        if orders != list(range(1, len(sequence) + 1)):
            issues.append("Sequence order is not contiguous: " + url)
        schedule = re.search(r"Schedule\s*\((\d+)\s+workouts?\)", detail.get("text", ""), re.I)
        if schedule and len(sequence) != int(schedule[1]):
            issues.append("Schedule declared count differs from captured sequence: " + url)
        embedded, embedded_seen, steps, source_reference_errors, canonical_reuse, uncovered_marker_steps = [], set(), [], [], [], []
        for step in sequence:
            if not step.get("text", "").strip() or not step.get("html", "").strip():
                issues.append("Empty routine step: " + url + " / " + str(step.get("order")))
            observed_urls = list(dict.fromkeys(l["url"] for l in step.get("links", []) if "/workouts-and-routines/workouts/" in l.get("url", "")))
            broken = [u for u in observed_urls if W.slug(u) in {"undefined", "null"}]
            source_reference_errors += [{"order": step.get("order"), "url": u, "status": "source emitted invalid workout URL; task text preserved without invented workout identity"} for u in broken]
            step_urls = [u for u in observed_urls if u not in broken]
            for workout_url in step_urls:
                if workout_url not in workout_by_url:
                    issues.append("Referenced workout not captured: " + workout_url)
                elif workout_url not in embedded_seen:
                    embedded_seen.add(workout_url)
                    embedded.append(workout_by_url[workout_url])
            marker_counter = W.FootnoteCounter()
            marker_counter.feed(step.get("html", ""))
            if marker_counter.count:
                candidates = [workout_by_url[u] for u in step_urls if u in workout_by_url and workout_by_url[u].get("footnotes", {}).get("notes")]
                if candidates:
                    canonical_reuse.append({"order": step.get("order"), "marker_count": marker_counter.count, "workout_name": candidates[0]["name"], "workout_url": candidates[0]["url"], "canonical_note_count": len(candidates[0]["footnotes"]["notes"]), "source": "canonical workout capture reused; not a fresh routine-popup capture"})
                else:
                    uncovered_marker_steps.append(step.get("order"))
            ignored_lines = {str(step.get("order", "")), (step.get("name") or "").strip(), "Instructions", "SEE FULL WORKOUT DETAILS"}
            authored_lines = [line.strip() for line in step.get("text", "").splitlines() if line.strip() and line.strip() not in ignored_lines]
            generic_title = W.name_key(step.get("name") or "") == W.name_key(overview.get("name", "") + str(step.get("order", "")))
            source_blank = step.get("source_blank", bool(broken) and not authored_lines and generic_title)
            steps.append({**step, "workout_urls": step_urls, "broken_source_workout_urls": broken, "kind": "workout" if step_urls else "other task", "source_blank": source_blank})
        text = overview.get("text", "")
        section = W.field(text, "Section Type", "Prep Stage").split()
        if not section:
            section = W.field(text, "Section Impact", "Prep Stage").split()
        stages = W.field(text, "Prep Stage", "Challenge Index").split()
        challenge = W.field(text, "Challenge Index", "Prep Map Points")
        if not section or not stages or not challenge:
            issues.append("Missing routine section/stage/challenge metadata: " + url)
        facts = {}
        fact_labels = {"LEVEL", "FREQUENCY", "STUDY BLOCK LENGTH", "CHALLENGE INDEX"} | {g.get("group", "").upper() for g in options}
        for match in re.finditer(r"(?m)^([A-Z][A-Z /+-]{2,})\s*\n([^\n]+)", detail.get("text", "")):
            if match[1].strip() in fact_labels:
                facts[match[1].strip()] = match[2].strip()
        links = overview.get("links", []) + detail.get("links", [])
        resource_md, resource_html, resources = [], [], []
        document_links = links + [link for step in steps for link in step.get("links", [])]
        embedded_documents = {a.get("file_id") for workout in embedded for a in workout.get("attachments", []) if a.get("status") == "captured"}
        resource_seen = set()
        for link in document_links:
            file_id = google_document_id(link.get("url", ""))
            if not file_id or file_id in resource_seen or file_id in embedded_documents:
                continue
            resource_seen.add(file_id)
            saved = export_sources.get(file_id)
            if not saved or not saved["path"].is_file() or W.sha(saved["path"]) != saved.get("sha256"):
                unarchived_documents.append({"routine": overview.get("name"), "url": link["url"], "file_id": file_id})
                issues.append("Routine instructional document not preserved: " + link["url"])
                continue
            md, fragment = W.instructional_export(saved["path"])
            resource_md.append(md)
            resource_html.append(fragment)
            manifest = archive / "attachments.json" if saved["path"].resolve().is_relative_to(args.input.resolve()) else workout_archive / "attachments.json"
            resources.append(export_identity(saved, manifest.relative_to(ROOT).as_posix()))
        for attachment in routine_attachments:
            applies = url in attachment.get("routine_urls", []) or url == attachment.get("routine_url") or any(W.name_key(name) == W.name_key(overview.get("name", "")) for name in attachment.get("routine_names", []))
            file_id = attachment.get("file_id", "")
            if not applies or file_id in resource_seen or attachment.get("local_path", "").endswith(".pdf"):
                continue
            saved = export_sources.get(file_id)
            if not saved or not saved["path"].is_file() or W.sha(saved["path"]) != saved.get("sha256"):
                issues.append("Explicit routine resource missing or hash mismatch: " + file_id)
                continue
            resource_seen.add(file_id)
            md, fragment = W.instructional_export(saved["path"])
            resource_md.append("### " + saved.get("name", saved.get("title", file_id)) + "\n\n" + md)
            resource_html.append("<h3>" + html.escape(saved.get("name", saved.get("title", file_id))) + "</h3>" + fragment)
            resources.append(export_identity(saved, (archive / "attachments.json").relative_to(ROOT).as_posix()))
        progression = sorted({value for l in links for value in parse_qs(urlsplit(l.get("url", "")).query).get("progression", [])})
        progression_memberships = []
        for link in links:
            values = parse_qs(urlsplit(link.get("url", "")).query).get("progression", [])
            for value in values:
                ordinal = re.search(r"Routine\s*(\d+)\s*/\s*(\d+)", link.get("text", ""), re.I)
                membership = {"name": value, "url": link["url"], "position": int(ordinal[1]) if ordinal else None, "total": int(ordinal[2]) if ordinal else None, "text": link.get("text", "")}
                if membership not in progression_memberships:
                    progression_memberships.append(membership)
        reference_urls = sorted({l["url"] for l in links if "/prep-map/" in l.get("url", "")})
        included_prep, prep_seen, reference_status = [], set(), []
        for ref in reference_urls:
            successful = [ref] if ref in prep and prep[ref].get("status") != "source-error" else [u for u, p in prep.items() if W.slug(u) == W.slug(ref) and p.get("status") != "source-error"]
            status = "captured" if ref in successful else "source-error with observed related capture" if successful else "unresolved"
            if not successful:
                issues.append("Routine prep-map reference unresolved: " + ref)
            reference_status.append({"url": ref, "status": status, "related_urls": [u for u in successful if u != ref]})
            for target in successful:
                if target not in prep_seen:
                    prep_seen.add(target)
                    included_prep.append(prep[target])
        notes = note_by_url.get(url, {"notes": []})
        markers = detail.get("footnoteMarkers", [])
        if (uncovered_marker_steps or (markers and not canonical_reuse)) and not notes.get("notes"):
            issues.append("Routine-specific footnote markers need capture/adjudication: " + url)
        supplemental_training = training_by_url.get(url, {})
        if re.search(r'aria-label=["\']Expand section["\']', detail.get("html", "")) and not supplemental_training.get("html", "").strip():
            issues.append("Collapsed training-block section needs supplemental capture: " + url)
        if supplemental_training and (not supplemental_training.get("text", "").strip() or not supplemental_training.get("html", "").strip() or re.search(r'aria-label=["\']Expand section["\']', supplemental_training.get("html", ""))):
            issues.append("Supplemental training block incomplete: " + url)
        r = {"name": overview.get("name", detail.get("name", W.slug(url))), "slug": W.slug(url), "url": url,
             "section_impact": section, "prep_stages": stages, "challenge_index": challenge,
             "routine_progressions": progression, "routine_progression_memberships": progression_memberships, "source_quick_facts": facts,
             "overview": overview, "detail": detail, "sequence": steps, "footnotes": notes,
             "embedded_workouts": embedded, "inline_prep": included_prep, "prep_reference_status": reference_status, "source_reference_errors": source_reference_errors,
             "additional_resource_exports": resources, "resource_markdown": "\n\n".join(resource_md), "resource_html": "".join(resource_html),
             "training_blocks": supplemental_training, "canonical_footnote_reuse": canonical_reuse, "uncovered_footnote_steps": uncovered_marker_steps}
        useful_dimensions = map_filters(r, options, facets)
        records.append(r)
    for url in set(detail_by_url) - seen:
        issues.append("Detail not matched to routine inventory: " + str(url))
    if input_snapshot(args.input) != initial_snapshot:
        raise RuntimeError("Intake changed during compilation. Wait for capture checkpoint completion and rerun; no archive/output updated.")
    if args.archive:
        archive_sources(args.input, archive)
    archive_verified = False
    if (archive / "SHA256SUMS").exists():
        rows = [line.split("  ", 1) for line in (archive / "SHA256SUMS").read_text(encoding="utf-8").splitlines() if line]
        archive_verified = all((archive / name).is_file() and W.sha(archive / name) == digest for digest, name in rows)
        archive_verified = archive_verified and all((archive / p.relative_to(args.input)).is_file() and W.sha(p) == W.sha(archive / p.relative_to(args.input)) for p in args.input.rglob("*") if p.is_file() and not p.is_symlink())
    checks = []
    for facet in facets:
        group, label = facet.get("group", ""), facet.get("name", "")
        expected = {W.name_key(n) for n in facet.get("memberNames", [])}
        if group in {"Section Type", "Section Impact"}:
            actual = {W.name_key(r["name"]) for r in records if (all(s in r["section_impact"] for s in ("LR", "RC")) if label == "LR & RC" else label in r["section_impact"])}
        elif group == "Challenge Index":
            actual = {W.name_key(r["name"]) for r in records if label in r["challenge_categories"]}
        elif group == "Routine Progression":
            actual = {W.name_key(r["name"]) for r in records if label in r["routine_progressions"]}
        elif group in useful_dimensions:
            actual = {W.name_key(r["name"]) for r in records if label in r["useful_filters"].get(group, [])}
        else:
            continue
        checks.append({"group": group, "name": label, "observed": len(expected), "compiled": len(actual), "matches": expected == actual})
        if expected != actual:
            issues.append("Routine facet mismatch: " + group + " / " + label)
    report = {"routine_count": len(records), "overview_count": len(overviews), "detail_count": len(details),
              "sequence_step_count": sum(len(r["sequence"]) for r in records),
              "other_task_step_count": sum(s["kind"] == "other task" for r in records for s in r["sequence"]),
              "embedded_unique_workout_bodies_per_routine": sum(len(r["embedded_workouts"]) for r in records),
              "supplemental_training_block_count": sum(bool(r["training_blocks"]) for r in records),
              "canonical_footnote_reuse_steps": sum(len(r["canonical_footnote_reuse"]) for r in records),
              "source_reference_errors": [{"routine": r["name"], **item} for r in records for item in r["source_reference_errors"]],
              "source_blank_tasks": [{"routine": r["name"], "url": r["url"], "order": step["order"], "name": step.get("name"), "status": "source supplies no authored instructions; preserved without invention"} for r in records for step in r["sequence"] if step.get("source_blank")],
              "workout_filter_source_discrepancies": [{"routine": r["name"], **r["workout_filter_source_discrepancy"]} for r in records if any(r["workout_filter_source_discrepancy"].values())],
              "unarchived_instructional_documents": unarchived_documents,
              "filter_mapping_counts": {"section_impact": sum(bool(r["section_impact"]) for r in records), "prep_stage": sum(bool(r["prep_stages"]) for r in records), "challenge_index": sum(bool(r["challenge_categories"]) for r in records), "routine_progression_listed": sum(bool(r["routine_progressions"]) for r in records)} | {dimension: sum(bool(r["useful_filters"].get(dimension)) for r in records) for dimension in useful_dimensions},
              "complete_within_captured_inventory": not issues and all(not r["unknown_filter_dimensions"] for r in records) and not any(step.get("source_blank") for r in records for step in r["sequence"]), "issues": issues,
              "all_filter_mappings_present": bool(records) and all(not r["unknown_filter_dimensions"] for r in records),
              "unknown_filter_mappings": [{"routine": r["name"], "dimensions": r["unknown_filter_dimensions"]} for r in records if r["unknown_filter_dimensions"]],
              "filter_membership_checks": checks, "facet_source": str(facet_path),
              "facet_sha256": W.sha(facet_path) if facet_path.exists() else None,
              "source_archive": archive.relative_to(ROOT).as_posix(), "archive_hash_verified": archive_verified,
              "source_sha256": {p.name: W.sha(p) for p in args.input.glob("*.json")},
              "limits": ["Completeness covers observed rendered inventory and explicit expanded step captures, not unseen server content.", "Routine-specific step prescriptions remain authoritative for that routine; embedded canonical workout instructions are a separate complete sourcebook.", "Related media URLs are retained, media bytes are not newly downloaded by this compiler."]}
    for r in records:
        folder = args.output / r["slug"]
        W.write(folder / "README.md", document(r, archive, workout_archive))
        for key in ("overview", "detail"):
            W.write(folder / (key + ".txt"), r[key].get("text", ""))
            W.write(folder / (key + ".html"), r[key].get("html", ""))
        W.write(folder / "sequence.json", json.dumps(r["sequence"], ensure_ascii=False, indent=2))
        W.write(folder / "source.json", json.dumps(source_record(r), ensure_ascii=False, indent=2))
    W.write(args.output / "verification.generated.json", json.dumps(report, ensure_ascii=False, indent=2))
    W.write(args.output / "catalog.generated.json", json.dumps({"verification": report, "routines": [source_record(r) for r in records], "filter_options": options}, ensure_ascii=False, indent=2))
    table = "\n".join(f"| [{r['name']}]({r['slug']}/README.md) | {len(r['sequence'])} | {', '.join(r['section_impact'])} | {', '.join(r['prep_stages'])} |" for r in records)
    W.write(args.output / "README.md", "# Loophole routines: ordered schedules and full source content\n\n[Loophole home](../README.md) | [LR](../logical-reasoning/README.md) | [RC](../reading-comprehension/README.md) | [Shared](../shared/README.md) | [Prep-map captures](../workouts/prep-map-points/README.md)\n\n[Searchable self-contained routine catalog](catalog.html) · [Coverage report](verification.generated.json)\n\nEach primary routine document contains its entire captured page, every ordered schedule step (including repeats and non-workout tasks), and full embedded workout instructions, advice, footnotes, templates and prep content. Routine-specific prescriptions remain separate from general workout source instructions.\n\nCaptured inventory: " + str(len(records)) + " routines; coverage issues: " + str(len(issues)) + ". Source blank tasks: " + str(len(report["source_blank_tasks"])) + "; these are preserved without invented instructions. Unknown filters remain explicit in the report.\n\n| Routine | Ordered steps | Section impact | Prep stage |\n|---|---:|---|---|\n" + table + "\n")
    viewer = []
    for r in records:
        seq_html = "".join("<section><h3>Step " + str(s["order"]) + ": " + html.escape(s.get("name") or "Other routine task") + "</h3>" + W.readable_html(s.get("html", "")) + "<details><summary>Exact step text</summary><pre>" + html.escape(s.get("text", "")) + "</pre></details>" + ("<p><strong>Source blank task:</strong> no authored instructions were supplied by the site for this generated step. Preserved without invention.</p>" if s.get("source_blank") else "") + "</section>" for s in r["sequence"])
        quick_facts = "<table><tbody>" + "".join("<tr><th>" + html.escape(k) + "</th><td>" + html.escape(v) + "</td></tr>" for k, v in r["source_quick_facts"].items()) + "</tbody></table>"
        body = "<h2>Complete routine overview</h2>" + W.readable_html(r["overview"].get("html", "")) + "<h2>Captured routine quick facts</h2>" + quick_facts + "<h2>Ordered schedule: follow these routine-specific prescriptions</h2>" + seq_html + "<h2>Complete routine guidance and source page</h2>" + W.readable_html(r["detail"].get("html", ""))
        body += "<h2>Routine-specific footnotes</h2>" + "".join(W.readable_html(n.get("html", "")) for n in r["footnotes"].get("notes", []))
        if r["training_blocks"]:
            body += "<h2>Complete expanded training-block resources</h2>" + W.readable_html(r["training_blocks"].get("html", ""))
        body += "<p>Canonical footnotes for copied workout instruction markers are reused from the same observed workout URL and included below; this is not a fresh routine-popup transcription.</p>" if r["canonical_footnote_reuse"] else ""
        body += "<h2>Additional routine instructional resources</h2>" + r.get("resource_html", "")
        body += "<h2>Full workout sourcebook</h2><p>Repeated schedule steps remain repeated above. General workout instructions do not replace routine-specific modifications.</p>" + "".join(full_workout_html(w) for w in r["embedded_workouts"])
        body += "<h2>Routine-linked prep-map content</h2>" + "".join("<h3>" + html.escape(p.get("name", "")) + "</h3>" + W.readable_html(p.get("html", "")) for p in r["inline_prep"])
        body += "<details><summary>Source provenance and exact routine text</summary><p>" + html.escape(r["url"]) + "</p><pre>" + html.escape(r["detail"].get("text", "")) + "</pre></details>"
        viewer.append({k: r[k] for k in ("name", "slug", "section_impact", "prep_stages", "challenge_categories", "routine_progressions", "useful_filters")} | {"body": body})
    payload = json.dumps({"routines": viewer, "options": options, "dimensions": useful_dimensions}, ensure_ascii=False).replace("<", "\\u003c")
    template = r'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Loophole routines</title><style>body{font:16px/1.6 system-ui;background:#f5faf8;color:#171712;margin:0}main{max-width:1100px;margin:auto;padding:24px}header{background:#f5faf8;position:sticky;top:0;z-index:2;padding:8px 0}input,select,button{font:inherit;padding:8px;border:1px solid;border-radius:8px;max-width:100%}details.routine{background:white;border:2px solid;border-radius:12px;margin:12px 0}summary{cursor:pointer;padding:14px;font-weight:700}.content{padding:0 24px 24px}pre{white-space:pre-wrap;font:14px/1.6 ui-monospace,monospace}a{color:#006b70}table{border-collapse:collapse}td,th{border:1px solid #ccc;padding:6px}.useful{display:inline-block;vertical-align:top;background:white;border:1px solid;border-radius:8px}.useful>summary{font-weight:400;padding:8px}#useful-controls{display:grid;gap:8px;padding:12px}#useful-controls label{display:grid;gap:4px}li{max-width:85ch}</style><main><nav><a href="../README.md">Loophole home</a> | <a href="../logical-reasoning/README.md">LR</a> | <a href="../reading-comprehension/README.md">RC</a> | <a href="../shared/README.md">Shared</a> | <a href="../workouts/prep-map-points/README.md">Prep-map captures</a></nav><header><h1>Loophole routines</h1><input id="search" aria-label="Search routines" placeholder="Search full routine content"> <select id="section" aria-label="Section Impact"><option value="">Every section impact</option></select> <select id="stage" aria-label="Prep Stage"><option value="">Every prep stage</option></select> <select id="challenge" aria-label="Challenge Index"><option value="">Every challenge index</option></select> <select id="progression" aria-label="Routine Progression"><option value="">Every routine progression</option></select> <details class="useful"><summary>Useful Filters</summary><div id="useful-controls"></div></details><p id="count"></p></header><p>Captured rendered source, 2026-10-15. <a href="verification.generated.json">Coverage, unknown mappings and limitations</a>. Read each routine's own schedule first; the full workout sourcebook is included inside that routine.</p><div id="list"></div></main><script type="application/json" id="data">PAYLOAD</script><script>const data=JSON.parse(document.getElementById('data').textContent),$=id=>document.getElementById(id),esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));for(const[id,key]of[['section','section_impact'],['stage','prep_stages'],['challenge','challenge_categories'],['progression','routine_progressions']])for(const value of[...new Set([...data.routines.flatMap(r=>r[key]),...(data.options.find(g=>g.group===({section:'Section Impact',stage:'Prep Stage',challenge:'Challenge Index',progression:'Routine Progression'}[id]))?.options||[]).map(o=>{const assigned=data.routines.flatMap(r=>r[key]);return assigned.find(v=>v.toLowerCase()===o.name.toLowerCase())||o.name}).filter(n=>n.toLowerCase()!=='all'),...(id==='section'?['LR & RC']:[])])].sort()){const o=document.createElement('option');o.value=o.textContent=value;$(id).append(o)}for(const dimension of data.dimensions){const label=document.createElement('label');label.textContent=dimension;const select=document.createElement('select');select.dataset.dimension=dimension;select.setAttribute('aria-label',dimension);const empty=document.createElement('option');empty.value='';empty.textContent='Any '+dimension.toLowerCase();select.append(empty);const source=data.options.find(g=>g.group===dimension);for(const value of source?source.options.map(o=>o.name):[...new Set(data.routines.flatMap(r=>r.useful_filters[dimension]||[]))].sort()){const o=document.createElement('option');o.value=o.textContent=value;select.append(o)}select.addEventListener('input',render);label.append(select);$('useful-controls').append(label)}function render(){const q=$('search').value.toLowerCase(),s=$('section').value,t=$('stage').value,c=$('challenge').value,p=$('progression').value,useful=[...document.querySelectorAll('#useful-controls select')].filter(e=>e.value);const titleMatches=q&&data.routines.some(r=>r.name.toLowerCase().includes(q));const rows=data.routines.filter(r=>(!s||(s==='LR & RC'?r.section_impact.includes('LR')&&r.section_impact.includes('RC'):r.section_impact.includes(s)))&&(!t||r.prep_stages.includes(t))&&(!c||r.challenge_categories.includes(c))&&(!p||r.routine_progressions.includes(p))&&useful.every(e=>(r.useful_filters[e.dataset.dimension]||[]).includes(e.value))&&(!q||(titleMatches?r.name.toLowerCase().includes(q):JSON.stringify(r).toLowerCase().includes(q))));$('count').textContent=rows.length+' of '+data.routines.length+' routines';$('list').innerHTML=rows.map(r=>`<details class="routine" data-slug="${esc(r.slug)}"><summary>${esc(r.name)}<small> · ${esc(r.section_impact.join(' / '))} · ${esc(r.prep_stages.join(' / '))}</small></summary><div class="content"></div></details>`).join('')}for(const id of['search','section','stage','challenge','progression'])$(id).addEventListener('input',render);document.addEventListener('toggle',event=>{const card=event.target;if(!card.matches?.('details.routine')||!card.open)return;const target=card.querySelector('.content');if(target.dataset.loaded)return;const r=data.routines.find(r=>r.slug===card.dataset.slug);target.innerHTML=`<p><a href="${esc(r.slug)}/README.md">Open complete routine document</a></p>${r.body}`;target.dataset.loaded='true'},true);render();</script></html>'''
    W.write(args.output / "catalog.html", template.replace("PAYLOAD", payload))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not issues else 2


if __name__ == "__main__":
    raise SystemExit(main())
