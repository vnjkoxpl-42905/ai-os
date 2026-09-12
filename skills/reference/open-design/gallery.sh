#!/usr/bin/env bash
# Open Design — visual gallery launcher
# Runs the daemon (API on :7456) + Next.js web app (:3000) using Node 24.
# Skips the broken Electron desktop shell entirely.
#
# Usage:  ./gallery.sh          start both, open the browser
#         ./gallery.sh stop     kill anything on :7456 and :3000
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PATH="/usr/local/opt/node@24/bin:$PATH"
DAEMON_LOG=/tmp/od-daemon.log
WEB_LOG=/tmp/od-web.log

kill_port() { lsof -ti tcp:"$1" 2>/dev/null | xargs kill -9 2>/dev/null || true; }

if [[ "${1:-}" == "stop" ]]; then
  kill_port 7456; kill_port 3000
  echo "stopped."
  exit 0
fi

cd "$REPO"
echo "node: $(node -v)"

# fresh start
kill_port 7456; kill_port 3000

echo "starting daemon (API :7456)…"
nohup pnpm --filter @open-design/daemon dev > "$DAEMON_LOG" 2>&1 &
# wait for the daemon to bind
for i in $(seq 1 60); do
  if curl -s -o /dev/null http://127.0.0.1:7456/api/design-systems; then break; fi
  sleep 1
done

echo "starting web app (:3000)…"
nohup pnpm --filter @open-design/web dev > "$WEB_LOG" 2>&1 &
for i in $(seq 1 60); do
  if curl -s -o /dev/null http://localhost:3000; then break; fi
  sleep 1
done

echo "gallery up → http://localhost:3000  (click the 'Design Systems' tab)"
open http://localhost:3000 || true
echo "logs: $DAEMON_LOG  /  $WEB_LOG"
echo "stop with: $REPO/gallery.sh stop"
