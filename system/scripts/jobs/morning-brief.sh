#!/bin/zsh
# Daily morning brief. Runs the `morning-brief` skill unattended and leaves a
# ranked queue of Gmail DRAFTS for Joshua to review and send himself.
#
# Backlog item A. The plan's finding was that the drafting skills already
# existed but were pull-only, so nothing ran them and the backlog kept forming
# (19% of authored email is an apology for replying late). This closes that: the
# brief runs whether or not anyone remembers to ask for it.
#
# Auth note: `claude` reads its credentials from the login keychain, so this
# only works while Joshua is logged in. A locked or logged-out Mac fails the
# run; launchd retries on the next schedule. That is the accepted trade-off —
# the alternative is a long-lived API key on disk.
#
# Sending: impossible by construction. The skill drafts through
# gmail-draft.sh, which hardcodes --draft. There is no auto-send path.
set -euo pipefail
ROOT="${BRAIN_ROOT:-${0:A:h:h:h:h}}"
cd "$ROOT"

out="$ROOT/system/logs/morning-brief.$(/bin/date '+%Y-%m-%d').log"

# --permission-mode default keeps the settings.json allow/deny lists in force;
# anything not allow-listed is denied rather than prompted, since no one is here
# to answer. The deny list (git push, rm -rf, sudo) still applies.
claude -p 'Run the morning-brief skill now. This is an unattended scheduled run: complete the full sweep, classify, rank, draft, and log pipeline without asking questions. Create every draft with system/scripts/gmail-draft.sh. Never send. End with the ranked queue exactly as the skill specifies.' \
  --permission-mode default \
  >"$out" 2>&1

# Surface the queue in the job output so the launchd log is useful on its own.
/usr/bin/tail -n 40 "$out"
print "morning-brief: PASS (full output: $out)"
