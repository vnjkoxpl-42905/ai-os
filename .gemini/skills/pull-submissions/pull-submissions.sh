#!/usr/bin/env bash
# Pull booking-time student submissions (files + notes) from the LSAT U backend
# into students/<name>/submissions/. Idempotent: a per-student manifest records
# what has already been pulled, so re-running only fetches new submissions.
#
# Auth: logs in with the admin creds in ~/ai-os/.env against GoTrue (password
# grant), then calls the booking-pass-admin edge function exactly as the admin
# UI does. Files come back as short-lived signed URLs from the private bucket.
#
# Usage: pull-submissions.sh            (pull everything new)
#        pull-submissions.sh --dry-run  (list what would be pulled, write nothing)
set -euo pipefail

AIOS="${AIOS_ROOT:-$HOME/ai-os}"
DRY_RUN=0
[[ "${1:-}" == "--dry-run" ]] && DRY_RUN=1

# --- env: admin creds (root .env) + supabase url/anon (lsatu .env) ------------
set -a
# shellcheck disable=SC1090
source "$AIOS/.env"
# shellcheck disable=SC1091
source "$AIOS/projects/lsatu/.env"
set +a

SUPABASE_URL="${VITE_SUPABASE_URL:?missing VITE_SUPABASE_URL}"
ANON="${VITE_SUPABASE_PUBLISHABLE_KEY:?missing VITE_SUPABASE_PUBLISHABLE_KEY}"
EMAIL="${LSATPREP_ADMIN_EMAIL:?missing LSATPREP_ADMIN_EMAIL}"
PASS="${LSATPREP_ADMIN_PASSWORD:?missing LSATPREP_ADMIN_PASSWORD}"

need() { command -v "$1" >/dev/null || { echo "need $1 installed" >&2; exit 1; }; }
need jq; need curl

# --- 1) login -> access token -------------------------------------------------
TOKEN=$(curl -s "$SUPABASE_URL/auth/v1/token?grant_type=password" \
  -H "apikey: $ANON" -H "Content-Type: application/json" \
  -d "{\"email\":\"$EMAIL\",\"password\":\"$PASS\"}" | jq -r '.access_token // empty')
[[ -n "$TOKEN" ]] || { echo "login failed" >&2; exit 1; }

admin() { # action json -> response
  curl -s "$SUPABASE_URL/functions/v1/booking-pass-admin" \
    -H "Authorization: Bearer $TOKEN" -H "apikey: $ANON" -H "Content-Type: application/json" \
    -d "$1"
}

slugify() { echo "$1" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$//g'; }

# --- 2) list bookings, keep those with a note or files ------------------------
BOOKINGS=$(admin '{"action":"list_bookings"}' | jq -c '[.bookings[] | select((.upload_count // 0) > 0 or (.student_note // "" | length > 0))]')
COUNT=$(echo "$BOOKINGS" | jq 'length')
echo "Found $COUNT booking(s) with a submission."

pulled_new=0
for row in $(echo "$BOOKINGS" | jq -c '.[]'); do
  RID=$(echo "$row" | jq -r '.id')
  NOTE=$(echo "$row" | jq -r '.student_note // ""')
  NUP=$(echo "$row" | jq -r '.upload_count // 0')
  START=$(echo "$row" | jq -r '.start_at')
  NAME=$(echo "$row" | jq -r '.booking_passes.student_name // .student_name_snapshot // .booking_passes.student_email // .student_email_snapshot // "unknown-student"')
  DATE=$(echo "$START" | cut -c1-10)
  SLUG=$(slugify "$NAME")

  DEST="$AIOS/students/$SLUG/submissions"
  MANIFEST="$DEST/.pulled.json"
  # already pulled this redemption?
  if [[ -f "$MANIFEST" ]] && jq -e --arg r "$RID" 'index($r)' "$MANIFEST" >/dev/null 2>&1; then
    continue
  fi

  echo "  • $NAME ($DATE): note=$([[ -n "$NOTE" ]] && echo yes || echo no) files=$NUP"
  [[ $DRY_RUN -eq 1 ]] && continue

  mkdir -p "$DEST"
  BASE="$DEST/${DATE}_${RID:0:8}"

  # note file
  if [[ -n "$NOTE" ]]; then
    { echo "# Booking submission note — $NAME"; echo; echo "- Session: $START"; echo "- Redemption: $RID"; echo; echo "$NOTE"; } > "${BASE}_note.md"
  fi

  # files via signed urls
  if [[ "$NUP" -gt 0 ]]; then
    UPLOADS=$(admin "{\"action\":\"get_booking_uploads\",\"redemption_id\":\"$RID\"}")
    for u in $(echo "$UPLOADS" | jq -c '.uploads[]'); do
      FNAME=$(echo "$u" | jq -r '.file_name')
      URL=$(echo "$u" | jq -r '.url // empty')
      [[ -n "$URL" ]] || { echo "    (no url for $FNAME)"; continue; }
      curl -s -L -o "${BASE}_${FNAME}" "$URL" && echo "    ↓ ${DATE}_${RID:0:8}_${FNAME}"
    done
  fi

  # record in manifest
  if [[ -f "$MANIFEST" ]]; then
    jq --arg r "$RID" '. + [$r] | unique' "$MANIFEST" > "$MANIFEST.tmp" && mv "$MANIFEST.tmp" "$MANIFEST"
  else
    echo "[\"$RID\"]" > "$MANIFEST"
  fi
  pulled_new=$((pulled_new+1))
done

echo "Done. Pulled $pulled_new new submission(s)."
