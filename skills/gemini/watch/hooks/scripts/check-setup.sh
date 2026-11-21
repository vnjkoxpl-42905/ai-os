#!/usr/bin/env bash
# Read-only SessionStart preflight. No credentials, installs, or scaffolding.
set -euo pipefail
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
if command -v python >/dev/null 2>&1; then
  python "$SCRIPT_DIR/../../scripts/setup.py" --hook
elif command -v python3 >/dev/null 2>&1; then
  python3 "$SCRIPT_DIR/../../scripts/setup.py" --hook
else
  echo "/watch: Python is not on PATH. Check the existing install and refresh PATH; nothing was installed."
fi
