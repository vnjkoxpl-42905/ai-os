#!/usr/bin/env bash
# restore.sh - put the whole Claude Code setup onto a NEW Mac.
# Prereqs: Google Drive for Desktop signed in, git, node, `npm i -g @anthropic-ai/claude-code`.
# Run:  bash "$HOME/Library/CloudStorage/GoogleDrive-contact@aspiringattorneys.com/My Drive/CLAUDE-CODE-BACKUP - START HERE/restore.sh"
# Optional: TARGET=/tmp/test bash restore.sh   (restore into a test folder)
set -euo pipefail
TARGET="${TARGET:-$HOME}"
DRIVE="$(dirname "$(realpath "$0")")"
CUR="$DRIVE/current"
[ -d "$CUR" ] || { echo "Backup not found at $CUR"; exit 1; }
OLDHOME=$(python3 -c "import json,sys;print(json.load(open(sys.argv[1]))['home'])" "$CUR/machine-info.json")
echo "Restoring into $TARGET (backup taken from $OLDHOME)"
put(){ [ -d "$1" ] || { echo "  skip: $1"; return; }; mkdir -p "$2"; rsync -a "$1/" "$2/"; echo "  restored $2"; }
put "$CUR/claude"        "$TARGET/.claude"
cp  "$CUR/claude.json"   "$TARGET/.claude.json"
put "$CUR/codex"         "$TARGET/.codex"
mkdir -p "$TARGET/dev/ai-os"
rsync -a --exclude='/projects/' "$CUR/ai-os/" "$TARGET/dev/ai-os/"
put "$CUR/ai-os/projects" "$TARGET/dev/ai-os-projects"
put "$CUR/dotfiles/config" "$TARGET/.config"
for f in .gitconfig .npmrc .bashrc .bash_profile; do [ -f "$CUR/dotfiles/$f" ] && cp "$CUR/dotfiles/$f" "$TARGET/"; done
# Superwhisper on Mac stores modes/vocabulary here; copy the modes + vocabulary we have.
mkdir -p "$TARGET/Documents/superwhisper" && rsync -a "$CUR/superwhisper/" "$TARGET/Documents/superwhisper/" 2>/dev/null || true

# Rewrite transcript folder names: C--Users-Joshu-... -> -Users-joshuaf-...
OLDP=$(echo "$OLDHOME" | sed 's#[\:/]#-#g'); NEWP=$(echo "$TARGET" | sed 's#[\:/]#-#g')
for d in "$TARGET/.claude/projects/$OLDP"*; do
  [ -d "$d" ] || continue
  mv "$d" "$TARGET/.claude/projects/$NEWP${d##*/$OLDP}"
done
# Paths in the transcripts and config that pointed at the old Windows home.
OLDWIN=$(printf '%s' "$OLDHOME" | sed 's#\#\\\\#g')   # C:\Users\Joshu as it appears inside JSON
grep -rl --include='*.jsonl' --include='*.json' "$OLDWIN" "$TARGET/.claude" "$TARGET/.claude.json" 2>/dev/null | \
  xargs -r sed -i '' -e "s#$OLDWIN#$TARGET#g" -e "s#$(printf '%s' "$OLDHOME" | sed 's#\#/#g')#$TARGET#g"
[ -d "$TARGET/dev/ai-os-projects/lsatu" ] && (cd "$TARGET/dev/ai-os-projects/lsatu" && npm install)
echo; echo "Done. cd $TARGET/dev/ai-os && claude --resume"
echo "Sign in once if gh / gws / claude ask. Set up the Mac backup with: setup/backup/README.md"
