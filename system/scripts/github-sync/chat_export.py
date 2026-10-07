"""Generated conversation mirror. Source-file removal is mirrored; UI archive is not.

Only allowlisted project sessions are read. Authentication files and .env are never read.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


def _redact_once(text: str) -> str:
    text = re.sub(r"(?i)\bBearer\s+[A-Za-z0-9._~+/=-]+", "Bearer [REDACTED]", text)
    text = re.sub(r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?-----END [A-Z ]*PRIVATE KEY-----", "[REDACTED PRIVATE KEY]", text, flags=re.S)
    text = re.sub(r"\b(?:sk-[A-Za-z0-9_-]{12,}|gh[pousr]_[A-Za-z0-9]{16,}|github_pat_[A-Za-z0-9_]{16,}|AIza[A-Za-z0-9_-]{20,}|sk_(?:live|test)_[A-Za-z0-9]{12,})\b", "[REDACTED KEY]", text)
    text = re.sub(r"\b(?:sb_secret_[A-Za-z0-9_-]+|AKIA[A-Z0-9]{16}|eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)\b", "[REDACTED KEY]", text)
    text = re.sub(r"(?i)(\b(?:api[_-]?key|access[_-]?token|refresh[_-]?token|password|passwd|client[_-]?secret|authorization)\b[\"']?\s*[:=]\s*)(?:\"[^\"]*\"|'[^']*'|[^\s,;}]+)", r"\1[REDACTED]", text)
    text = re.sub(r"(?i)([?&](?:token|key|secret|password|signature|access_token)=)[^&#\s]+", r"\1[REDACTED]", text)
    text = re.sub(r"(https?://)[^/\s:@]+:[^/\s@]+@", r"\1[REDACTED]@", text)
    return text


def redact(text: str) -> str:
    # Nested serialized tool arguments can expose an adjacent credential token
    # after the first replacement. Converge before declaring output sanitized.
    for _ in range(12):
        clean = _redact_once(text)
        if clean == text:
            return clean
        text = clean
    raise ValueError("redaction did not converge")


def secret_checks(text: str) -> bool:
    """True when an additional redaction pass would change the output."""
    return redact(text) != text


def _inside(cwd: str, roots: list[Path]) -> bool:
    try:
        path = Path(cwd).resolve()
        return any(path == root.resolve() or root.resolve() in path.parents for root in roots)
    except (OSError, ValueError):
        return False


def _content(value) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return "\n\n".join(filter(None, (_content(item) for item in value)))
    if not isinstance(value, dict):
        return ""
    kind = value.get("type", "")
    if kind in {"thinking", "reasoning", "redacted_thinking"}:
        return ""
    if kind in {"text", "input_text", "output_text"}:
        return value.get("text", "")
    if kind in {"image", "input_image", "image_url", "document"}:
        return "[Attachment: " + str(value.get("filename", value.get("name", "image/document; binary omitted"))) + "]"
    if kind == "tool_use":
        return "Tool call: " + str(value.get("name", "unknown")) + "\n" + json.dumps(value.get("input", {}), ensure_ascii=False)
    if kind == "tool_result":
        return "Tool result:\n" + _content(value.get("content", ""))
    return _content(value.get("content", ""))


def _parse(path: Path, platform: str, roots: list[Path]):
    raw = path.read_text(encoding="utf-8")
    lines = [line for line in raw.splitlines() if line.strip()]
    records, warnings = [], []
    for position, line in enumerate(lines):
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError:
            if position == len(lines) - 1 and records and not raw.endswith("\n"):
                warnings.append("Final incomplete JSONL record omitted; valid preceding records exported")
                break
            raise
    if not records:
        return None
    cwds = []
    session_id = path.stem
    for row in records:
        if row.get("cwd"):
            cwds.append(row["cwd"])
        if row.get("type") == "session_meta":
            payload = row.get("payload", {})
            session_id = payload.get("id", session_id)
            if payload.get("cwd"):
                cwds.append(payload["cwd"])
        if platform == "claude":
            session_id = row.get("sessionId", session_id)
    if not cwds or not any(_inside(cwd, roots) for cwd in cwds):
        return None
    if platform == "claude" and "subagents" in path.parts:
        session_id += "-" + path.stem
    if not re.fullmatch(r"[A-Za-z0-9_-]+", session_id):
        raise ValueError("unsafe session identifier")
    sections = []
    has_response_messages = any(row.get("type") == "response_item" and row.get("payload", {}).get("type") == "message" for row in records)
    for row in records:
        if platform == "claude":
            if row.get("type") in {"user", "assistant"}:
                message = row.get("message", {})
                body = _content(message.get("content", ""))
                role = message.get("role", row["type"])
            elif row.get("type") == "summary":
                body, role = row.get("summary", ""), "Compaction summary"
            else:
                continue
        else:
            payload = row.get("payload", {})
            if row.get("type") == "response_item" and payload.get("type") == "message":
                if payload.get("channel") == "analysis":
                    continue
                body, role = _content(payload.get("content", "")), payload.get("role", "message")
            elif row.get("type") == "event_msg" and not has_response_messages and payload.get("type") in {"user_message", "agent_message"}:
                body, role = payload.get("message", ""), payload["type"]
            elif row.get("type") == "response_item" and payload.get("type") in {"function_call", "function_call_output", "custom_tool_call", "custom_tool_call_output"}:
                body = str(payload.get("arguments", payload.get("output", payload.get("input", ""))))
                role = "Tool: " + payload.get("name", payload["type"])
            elif row.get("type") == "compacted":
                body, role = payload.get("message", ""), "Compaction summary"
            else:
                continue
        if body:
            sections.append("## " + str(role) + "\n\n" + redact(body))
    if not sections:
        raise ValueError("no supported conversation content")
    text = redact("# " + platform.title() + " conversation " + session_id + "\n\n" + "\n\n".join(sections) + "\n")
    title = next((section.split("\n\n", 1)[1].splitlines()[0][:100] for section in sections if section.startswith("## user")), session_id)
    return session_id, text, {"cwd": cwds[0], "title": title, "warnings": warnings}


def _write_if_changed(path: Path, text: str):
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def export_conversations(destination: Path, allowed_roots: list[Path]) -> dict:
    destination = destination.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    index_path = destination / "index.json"
    previous = json.loads(index_path.read_text(encoding="utf-8")) if index_path.exists() else {"sessions": []}
    old = {entry["source"]: entry for entry in previous.get("sessions", [])}
    entries, errors, warnings = [], [], []
    home = Path.home()
    sources = [("claude", home / ".claude" / "projects"), ("codex", home / ".codex" / "sessions"), ("codex", home / ".codex" / "archived_sessions")]
    discovery_failed = False
    for platform, source_root in sources:
        root_old = [entry for entry in old.values() if source_root.resolve() in Path(entry["source"]).parents]
        if not source_root.exists() and root_old:
            errors.append({"platform": platform, "error": "source directory unavailable; previous exports retained"})
            entries.extend(root_old)
            continue
        try:
            paths = sorted(source_root.rglob("*.jsonl")) if source_root.exists() else []
        except OSError as exc:
            errors.append({"platform": platform, "error": str(exc)})
            discovery_failed = True
            continue
        for path in paths:
            if source_root.resolve() not in path.resolve().parents:
                errors.append({"error": "source symlink escapes session directory"})
                continue
            # Claude subagents are useful separate transcripts, but each needs its own cwd.
            source = str(path.resolve())
            try:
                stat = path.stat()
                cached = old.get(source)
                if cached and cached.get("export_version") == 4 and cached.get("source_mtime_ns") == stat.st_mtime_ns and cached.get("source_size") == stat.st_size and cached.get("allowed_roots") == [str(root.resolve()) for root in allowed_roots] and (destination / cached["file"]).exists():
                    entries.append(cached)
                    continue
                parsed = _parse(path, platform, allowed_roots)
                if parsed is None:
                    if stat.st_size == 0:
                        warnings.append({"source": source, "warning": "Empty JSONL source has no conversation records"})
                        if source in old:
                            entries.append(old[source])
                    continue
                session_id, body, metadata = parsed
                # Multiple Codex rollout files may share a thread id. Preserve every
                # rollout with a source-derived suffix rather than overwrite history.
                if platform == "codex":
                    session_id += "-" + hashlib.sha256(source.encode()).hexdigest()[:12]
                relative = platform + "/" + session_id + ".md"
                target = destination / relative
                if secret_checks(body):
                    raise ValueError("output failed secret check")
                _write_if_changed(target, body)
                entries.append({"platform": platform, "session_id": session_id, "file": relative, "source": source, "sha256": hashlib.sha256(body.encode()).hexdigest(), "source_mtime_ns": stat.st_mtime_ns, "source_size": stat.st_size, "allowed_roots": [str(root.resolve()) for root in allowed_roots], "export_version": 4, **metadata})
            except (ValueError, OSError, TypeError, KeyError) as exc:
                errors.append({"source": source, "error": str(exc)})
                if source in old:
                    entries.append(old[source])
    if discovery_failed:
        known = {entry["source"] for entry in entries}
        entries.extend(entry for source, entry in old.items() if source not in known)
    retained = {entry["file"] for entry in entries}
    for entry in old.values():
        if entry["file"] not in retained:
            target = (destination / entry["file"]).resolve()
            if destination not in target.parents or target.suffix != ".md" or target.parent.name not in {"claude", "codex"}:
                errors.append({"error": "unsafe previous index path"})
                continue
            if target.exists():
                target.unlink()
    warnings.extend({"source": entry["source"], "warning": warning} for entry in entries for warning in entry.get("warnings", []))
    result = {"sessions": sorted(entries, key=lambda entry: entry["file"]), "errors": errors, "warnings": warnings, "deletion_semantics": "Source JSONL removal only. UI archive/deletion may leave source files intact."}
    _write_if_changed(index_path, json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    lines = ["# Local conversation archive", "", "Generated project-scoped Claude and Codex transcripts. Tool content is included with credential redaction; internal reasoning and attachment binary data are omitted.", "", "Native UI archive does not delete a conversation. Source-file deletion removes its generated export. These files provide context; importing them does not restore a native chat session.", "", "| Platform | Conversation | Project roots | Source updated (UTC) |", "| --- | --- | --- | --- |"]
    from datetime import datetime, timezone
    for entry in result["sessions"]:
        updated = datetime.fromtimestamp(entry.get("source_mtime_ns", 0) / 1e9, timezone.utc).isoformat(timespec="seconds")
        roots = entry.get("cwd", ", ".join(entry.get("allowed_roots", [])))
        title = entry.get("title", entry["session_id"]).replace("|", "\\|").replace("[", "\\[").replace("]", "\\]")
        lines.append(f"| {entry['platform']} | [{title}]({entry['file']}) | {roots.replace('|', '\\|')} | {updated} |")
    _write_if_changed(destination / "README.md", "\n".join(lines) + "\n")
    return result
