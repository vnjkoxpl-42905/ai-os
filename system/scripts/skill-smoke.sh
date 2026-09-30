#!/bin/sh
# Portable static check for the copy-based project activation model.
set -eu
script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
exec python3 "$script_dir/skill-smoke.py"
