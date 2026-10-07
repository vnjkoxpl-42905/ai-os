#!/bin/zsh
# Conservative secret/Tier-A scanner for staged content, worktree, or outer history.
set -euo pipefail

mode="${1:-staged}"
root="$(git rev-parse --show-toplevel)"
cd "$root"

forbidden_name_re='(^|/)(\.env($|\.)|\.npmrc$|bankcard\.(jpe?g|png)$|id[[:space:]]*\.(jpe?g|png)$|.*(oauth|credential|service-account).*\.json$|.*\.(pem|p12|pfx)$)'
secret_re='(-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{30,}|gh[pousr]_[0-9A-Za-z]{30,}|(^|[^0-9A-Za-z])sk-(proj-)?[0-9A-Za-z_-]{20,}|xox[baprs]-[0-9A-Za-z-]{10,}|client_secret["'"'"'[:space:]]*[:=]["'"'"'[:space:]]*[0-9A-Za-z_-]{12,}|(api[_-]?key|access[_-]?token|auth[_-]?token|password)["'"'"'[:space:]]*[:=]["'"'"'[:space:]]*[0-9A-Za-z_./+=:-]{16,})'

scan_names() {
  local name
  while IFS= read -r name; do
    [[ -z "$name" ]] && continue
    # Explicitly-safe template names (mirror .gitignore's !.env.example / !.env.template).
    # Content scanning still runs on them, so a real key pasted in is still caught.
    case "${name:t}" in
      .env.example|.env.template) continue ;;
    esac
    if print -r -- "$name" | /usr/bin/grep -Eiq "$forbidden_name_re"; then
      print -u2 "Tier-A filename rejected: $name"
      return 1
    fi
  done
}

# Adjudicated content false positives (Joshua, 2026-07-16). Exact paths only;
# the patterns stay full-strength and any new path still fails.
content_allowlist=(
  # "don't do this" documentation examples, not live credentials
  'skills/claude/higgsfield-websites/references/security.md'
  'skills/codex/higgsfield-websites/references/security.md'
)

scan_blob() {
  local label="$1"
  local plain="${label#history:}"
  if (( ${content_allowlist[(Ie)$plain]} )); then
    cat >/dev/null
    return 0
  fi
  if LC_ALL=C /usr/bin/grep -EIna "$secret_re" 2>/dev/null; then
    print -u2 "Potential secret rejected in: $label"
    return 1
  fi
}

case "$mode" in
  staged)
    git diff --cached --name-only --diff-filter=ACMR | scan_names
    while IFS= read -r filepath; do
      [[ -z "$filepath" ]] && continue
      git show ":$filepath" 2>/dev/null | scan_blob "$filepath"
    done < <(git diff --cached --name-only --diff-filter=ACMR)
    ;;
  worktree)
    git ls-files | scan_names
    while IFS= read -r filepath; do
      [[ -f "$filepath" ]] || continue
      /usr/bin/file -b --mime "$filepath" | /usr/bin/grep -q 'charset=binary' && continue
      scan_blob "$filepath" < "$filepath"
    done < <(git ls-files)
    ;;
  history)
    git rev-list --objects --all | git cat-file --batch-check='%(objecttype) %(objectname) %(rest)' |
      while IFS=' ' read -r type oid filepath; do
        [[ "$type" == blob ]] || continue
        # Same template exemption scan_names applies to staged/worktree; history
        # mode predates it and was the one place .env.example still failed.
        case "${filepath:t}" in
          .env.example|.env.template) ;;
          *)
        if print -r -- "$filepath" | /usr/bin/grep -Eiq "$forbidden_name_re"; then
          print -u2 "Tier-A filename in history: $filepath"
          exit 1
        fi
          ;;
        esac
        size="$(git cat-file -s "$oid")"
        (( size <= 5242880 )) || continue
        git cat-file blob "$oid" | scan_blob "history:$filepath"
      done
    ;;
  *) print -u2 "usage: $0 {staged|worktree|history}"; exit 2 ;;
esac

print "secret-scan: PASS ($mode)"
