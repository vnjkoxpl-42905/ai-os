#!/bin/zsh

set -u

marker="/Users/joshuaf/ai-os/system/runtime/c-alexander-booking-email-2026-07-20.sent"
log="/Users/joshuaf/ai-os/system/runtime/c-alexander-booking-email-2026-07-20.log"

mkdir -p /Users/joshuaf/ai-os/system/runtime

if [[ -f "$marker" ]]; then
  exit 0
fi

if [[ "$(/bin/date +%Y-%m-%d)" != "2026-07-20" ]]; then
  exit 0
fi

if /usr/local/bin/gws gmail users drafts send --params '{"userId":"me"}' --json '{"id":"r617116306889391452"}' >> "$log" 2>&1; then
  /usr/bin/touch "$marker"
fi
