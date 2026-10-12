#!/bin/sh
# Validate the skills DB model (claude/ + codex/ subtrees, activations, INDEX).
# Logic lives in check-skills.py; this wrapper keeps the historic entrypoint.
# POSIX sh on purpose: must behave identically under `sh`, `bash`, and `zsh`.
# On Windows `python3` is often the Microsoft Store stub, which prints an install hint and
# exits non-zero, so use the first interpreter that actually runs Python 3.
set -eu
SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/../.." && pwd -P)
for candidate in python3 python py; do
  if command -v "$candidate" >/dev/null 2>&1 &&
     "$candidate" -c 'import sys; sys.exit(sys.version_info[0] != 3)' >/dev/null 2>&1; then
    exec "$candidate" "$ROOT/system/scripts/check-skills.py" "$@"
  fi
done
echo "skills: FAIL — no working Python 3 (tried python3, python, py)" >&2
exit 1
