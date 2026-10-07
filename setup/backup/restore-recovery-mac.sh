#!/bin/bash
# macOS portable-data restore. Defaults to verification and extraction only.
set -eo pipefail
if [[ $# -lt 1 ]]; then echo 'Usage: bash restore-recovery-mac.sh BACKUP_FOLDER [--apply]'; exit 2; fi
backup=$(cd "$1" && pwd)
apply=false
if [[ ${2:-} == --apply ]]; then apply=true; elif [[ $# -gt 1 ]]; then echo 'Unknown option'; exit 2; fi
seven=$(command -v 7zz || command -v 7z || true)
[[ -n "$seven" ]] || { echo 'Install 7-Zip for macOS (7zz), then rerun. No software was installed.'; exit 1; }
manifest="$backup/CLOUD-VERIFIED-SHA256SUMS.txt"
[[ -f "$manifest" ]] || { echo 'Missing cloud-verified SHA256 manifest'; exit 1; }
names=()
while IFS= read -r line || [[ -n "$line" ]]; do
  line=${line%$'\r'}
  [[ -z "$line" || "$line" == \#* ]] && continue
  if [[ "$line" =~ ^([a-fA-F0-9]{64})[[:space:]]+\*?([^/\\]+)$ ]]; then
    expected=${BASH_REMATCH[1]}; name=${BASH_REMATCH[2]}
  else echo 'Invalid manifest line'; exit 1; fi
  [[ "$name" != . && "$name" != .. && "$name" != *:* ]] || { echo 'Unsafe manifest name'; exit 1; }
  for known in "${names[@]}"; do [[ "$known" != "$name" ]] || { echo 'Duplicate manifest filename'; exit 1; }; done
  [[ -f "$backup/$name" ]] || { echo "Missing verified file: $name"; exit 1; }
  actual=$(shasum -a 256 "$backup/$name"); actual=${actual%% *}
  [[ $(printf '%s' "$actual" | tr 'A-F' 'a-f') == $(printf '%s' "$expected" | tr 'A-F' 'a-f') ]] || { echo "SHA256 mismatch: $name"; exit 1; }
  names+=("$name")
done < "$manifest"
[[ ${#names[@]} -gt 0 ]] || { echo 'Empty manifest'; exit 1; }
verified() { local n; for n in "${names[@]}"; do [[ "$n" == "$1" ]] && return 0; done; return 1; }
categories=(runtime-final second-brain development app-data sqlite-live-raw personal-files extra-settings additional-profile codex-final-delta)
active=()
for category in "${categories[@]}"; do
  if verified "$category.7z.001"; then first="$backup/$category.7z.001"; elif verified "$category.7z"; then first="$backup/$category.7z"; else continue; fi
  for volume in "$backup/$category.7z" "$backup/$category.7z."[0-9]*; do
    [[ -f "$volume" ]] || continue
    verified "${volume##*/}" || { echo 'Unverified archive volume'; exit 1; }
  done
  "$seven" t "$first" -bsp0 >/dev/null
  active+=("$category")
done
verified runtime-final.7z.001 || verified runtime-final.7z || { echo 'Missing runtime-final archive'; exit 1; }
verified second-brain.7z.001 || verified second-brain.7z || { echo 'Missing second-brain archive'; exit 1; }
stage=$(mktemp -d "$backup/restored-mac-XXXXXX")
for category in "${active[@]}"; do
  if verified "$category.7z.001"; then first="$backup/$category.7z.001"; else first="$backup/$category.7z"; fi
  "$seven" x "$first" "-o$stage/$category" -y -bsp0 >/dev/null
done
echo "Verified archives extracted to: $stage"
if ! $apply; then echo 'Stage only. No profile files changed.'; exit 0; fi
if pgrep -if '(^|/)(Codex|Claude)( |$|/|\.app)' >/dev/null; then echo 'Close Codex and Claude, including terminal agents, then rerun from Terminal.'; exit 1; fi
old=$(mktemp -d "$HOME/preexisting-before-restore-XXXXXX")
copy_safe() {
  local source=$1 target=$2 item name relative saved
  [[ -e "$source" && ! -L "$source" ]] || return 0
  name=${source##*/}
  case "$name" in node_modules|.venv|venv|__pycache__|.sandbox|.sandbox-bin|.sandbox-secrets|mcp-oauth-locks|project-metadata-locks|thread-writer-locks|rollout-migrations|.tmp|tmp) return 0;; esac
  case "$name" in yarn.lock|uv.lock|poetry.lock|Cargo.lock|Pipfile.lock|bun.lock) ;; *) case "$source" in */runtime/*|*/.git/*) case "$name" in *.lock|lockfile) return 0;; esac;; esac;; esac
  case "$source" in */runtime/*) case "$name" in *-wal|*-shm|*.sqlite|*.sqlite3|*.db) return 0;; esac;; esac
  [[ ! -L "$target" ]] || { echo "Target symlink needs manual restore: $target"; exit 1; }
  if [[ -d "$source" ]]; then
    [[ ! -e "$target" || -d "$target" ]] || { echo "File blocks directory: $target"; exit 1; }
    mkdir -p "$target"
    shopt -s dotglob nullglob
    for item in "$source"/*; do copy_safe "$item" "$target/${item##*/}"; done
  else
    [[ ! -d "$target" ]] || { echo "Directory blocks file: $target"; exit 1; }
    mkdir -p "${target%/*}"
    relative=${target#"$HOME"/}; saved="$old/$relative"
    if [[ -e "$target" && ! -e "$saved" ]]; then mkdir -p "${saved%/*}"; cp -p "$target" "$saved"; fi
    cp -p "$source" "$target"
  fi
}
root_for() { if [[ -d "$stage/$1/$2" ]]; then printf '%s' "$stage/$1/$2"; else printf '%s' "$stage/$1"; fi; }
runtime=$(root_for runtime-final runtime)
# Copy portable history/assets only. Windows configs, databases, credentials and binaries stay staged.
for name in .agents; do copy_safe "$runtime/$name" "$HOME/$name"; done
for name in projects sessions file-history skills hooks scheduled-tasks; do copy_safe "$runtime/.claude/$name" "$HOME/.claude/$name"; done
for name in sessions archived_sessions attachments automations skills pets plans visualizations generated_images dictation-history; do copy_safe "$runtime/.codex/$name" "$HOME/.codex/$name"; done
for category in second-brain development; do root=$(root_for "$category" "$category"); copy_safe "$root/dev" "$HOME/dev"; done
personal=$(root_for personal-files personal-files)
for name in Documents Desktop Downloads Pictures Music Videos Favorites; do copy_safe "$personal/$name" "$HOME/$name"; done
for category in "${active[@]}"; do
  [[ "$category" == codex-final-delta ]] || continue
  delta=$(root_for codex-final-delta codex-final-delta)
  copy_safe "$delta/second-brain/dev" "$HOME/dev"
  [[ ! -d "$delta/runtime" ]] || delta="$delta/runtime"
  [[ -d "$delta/.codex" ]] || { echo 'Unexpected final delta layout; inspect staged evidence manually.'; exit 1; }
  for name in sessions archived_sessions attachments automations skills pets plans visualizations generated_images dictation-history; do copy_safe "$delta/.codex/$name" "$HOME/.codex/$name"; done
done
echo "Portable data restored. Preexisting conflicts preserved: $old"
echo 'Codex SQLite databases, Windows configs, AppData, credentials and forensic raw SQLite remain staged.'
echo 'Install apps/tools, sign in, and repair Windows absolute paths manually. Restored transcripts do not guarantee chat-sidebar import on macOS.'
