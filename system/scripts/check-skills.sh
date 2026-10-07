#!/bin/sh
# Validate the skills DB model (claude/ + codex/ subtrees, activations, INDEX).
# Logic lives in check-skills.py; this wrapper keeps the historic entrypoint.
# POSIX sh on purpose: must behave identically under `sh`, `bash`, and `zsh`.
set -eu
SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/../.." && pwd -P)
exec /usr/bin/env python3 "$ROOT/system/scripts/check-skills.py" "$@"
