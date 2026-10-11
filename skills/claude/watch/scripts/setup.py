#!/usr/bin/env python3
"""Read-only watch preflight. Native captions need no paid provider key."""
from __future__ import annotations
import argparse
import json
import os
import shutil
from pathlib import Path

REQUIRED_BINARIES = ("ffmpeg", "ffprobe", "yt-dlp")

def central_root():
    """Resolve the workspace root from its paired operating instructions."""
    for candidate in (Path.cwd(), *Path.cwd().parents):
        if (candidate / "AGENTS.md").is_file() and (candidate / "CLAUDE.md").is_file():
            return candidate
    return None

def credential_present(provider):
    name = {"groq": "GROQ_API_KEY", "openai": "OPENAI_API_KEY"}[provider]
    if os.environ.get(name, "").strip():
        return True
    root = central_root()
    if root is None:
        return False
    try:
        lines = (root / ".env").read_text(encoding="utf-8").splitlines()
    except OSError:
        return False
    for line in lines:
        key, separator, value = line.strip().partition("=")
        if separator and key.strip() == name:
            return bool(value.strip().strip("\"'"))
    return False

def _status(paid_provider=None):
    missing = [name for name in REQUIRED_BINARIES if shutil.which(name) is None]
    result = {"status": "needs_tools" if missing else "ready", "mode": "native_captions",
              "missing_binaries": missing, "paid_provider": paid_provider}
    if paid_provider:
        result["credential_present"] = credential_present(paid_provider)
        result["mode"] = "explicit_paid_provider_preflight"
        if not missing and not result["credential_present"]:
            result["status"] = "needs_selected_provider_key"
    return result

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    output = parser.add_mutually_exclusive_group()
    output.add_argument("--check", action="store_true")
    output.add_argument("--json", action="store_true")
    output.add_argument("--hook", action="store_true")
    parser.add_argument("--paid-provider", choices=("groq", "openai"),
                        help="Check selected credential presence only; does not authorize or call an API")
    args = parser.parse_args(argv)
    status = _status(args.paid_provider)
    if args.json:
        print(json.dumps(status, sort_keys=True))
    elif status["missing_binaries"]:
        print("/watch: missing tools on PATH: " + ", ".join(status["missing_binaries"]) +
              ". Check existing installs and refresh PATH; this preflight installs nothing.")
    elif status["status"] == "needs_selected_provider_key":
        print("/watch: selected provider credential absent. Use the AI OS root .env or process environment only. Native captions remain free; no provider was called.")
    elif not args.hook:
        print("/watch: ready for native captions and local frames. No API key required; no files changed.")
    return 2 if status["missing_binaries"] else (3 if status["status"] == "needs_selected_provider_key" else 0)

if __name__ == "__main__":
    raise SystemExit(main())
