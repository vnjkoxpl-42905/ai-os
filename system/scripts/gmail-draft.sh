#!/bin/zsh
# Create a Gmail DRAFT. This wrapper cannot send.
#
# Why this exists: `gws gmail +send` sends by default and only becomes safe with
# a trailing `--draft`. Any permission rule broad enough to allow the draft form
# is also broad enough to allow a real send, so the guarantee cannot live in the
# allow-list. It lives here instead: this script builds the gws invocation from
# three named arguments and appends --draft itself. No caller-supplied flag is
# ever forwarded, so there is no argument that turns this into a send.
#
# Used by the morning-brief job, which drafts unattended. Nothing in this repo
# has an approved auto-send path.
#
#   gmail-draft.sh --to a@b.com --subject "Re: pacing" --body "..."
set -euo pipefail

to='' subject='' body=''
while (( $# )); do
  case "$1" in
    --to)      to="${2:?--to requires a value}"; shift 2 ;;
    --subject) subject="${2:?--subject requires a value}"; shift 2 ;;
    --body)    body="${2:?--body requires a value}"; shift 2 ;;
    *) print -u2 "gmail-draft: unsupported argument: $1"
       print -u2 "only --to, --subject, --body are accepted (drafts only, never sends)"
       exit 2 ;;
  esac
done

[[ -n "$to" && -n "$subject" && -n "$body" ]] || {
  print -u2 'usage: gmail-draft.sh --to <email> --subject <text> --body <text>'
  exit 2
}

# --draft is appended here, by the script, always. It is not a caller decision.
exec gws gmail +send --to "$to" --subject "$subject" --body "$body" --draft
