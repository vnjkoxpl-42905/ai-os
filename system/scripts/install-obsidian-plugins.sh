#!/bin/zsh
# Install pinned plugin release assets from repositories in Obsidian's official registry.
set -euo pipefail

ROOT="${0:A:h:h:h}"
STAGING="$ROOT/system/logs/staging/obsidian-install"
PLUGIN_ROOT="$ROOT/.obsidian/plugins"
LOCK="$ROOT/system/generated/obsidian-plugins.lock.tsv"
mkdir -p "$STAGING" "$PLUGIN_ROOT"
print $'id\trepository\tversion\ttag\tstatus\treview' > "$LOCK"

while IFS=$'\t' read -r id repo; do
  [[ -n "$id" && -n "$repo" ]] || continue
  json="$STAGING/$id.release.json"
  /usr/bin/curl -fsSL "https://api.github.com/repos/$repo/releases/latest" -o "$json"
  tag="$(/usr/bin/ruby -rjson -e 'puts JSON.parse(File.read(ARGV[0]))["tag_name"]' "$json")"
  [[ -n "$tag" ]] || { print -u2 "obsidian-plugin: no release tag for $id"; exit 1; }
  target="$PLUGIN_ROOT/$id"
  mkdir -p "$target"

  for asset in manifest.json main.js styles.css; do
    url="$(/usr/bin/ruby -rjson -e 'j=JSON.parse(File.read(ARGV[0])); a=j.fetch("assets",[]).find{|x| x["name"]==ARGV[1]}; puts(a ? a["browser_download_url"] : "")' "$json" "$asset")"
    if [[ -n "$url" ]]; then
      /usr/bin/curl -fsSL "$url" -o "$target/$asset"
    elif [[ "$asset" != styles.css ]]; then
      /usr/bin/curl -fsSL "https://raw.githubusercontent.com/$repo/$tag/$asset" -o "$target/$asset"
    fi
  done

  [[ -s "$target/manifest.json" && -s "$target/main.js" ]] || {
    print -u2 "obsidian-plugin: incomplete release for $id"
    exit 1
  }
  manifest_id="$(/usr/bin/ruby -rjson -e 'puts JSON.parse(File.read(ARGV[0]))["id"]' "$target/manifest.json")"
  version="$(/usr/bin/ruby -rjson -e 'puts JSON.parse(File.read(ARGV[0]))["version"]' "$target/manifest.json")"
  id_matches=0
  [[ "$manifest_id" == "$id" ]] && id_matches=1
  [[ "$id" == calendar && "$manifest_id" == calendar-beta ]] && id_matches=1
  (( id_matches == 1 )) || { print -u2 "obsidian-plugin: id mismatch $id != $manifest_id"; exit 1; }
  review='pending-disabled'
  [[ "$id" == karpathywiki ]] && review='static-review-recorded-disabled'
  [[ "$id" == calendar ]] && review='historical-manifest-id-calendar-beta-disabled'
  print "$id\t$repo\t$version\t$tag\tinstalled-disabled\t$review" >> "$LOCK"
  print "obsidian-plugin: installed $id@$version (disabled)"
done <<'PLUGINS'
tag-wrangler	pjeby/tag-wrangler
periodic-notes	liamcain/obsidian-periodic-notes
obsidian-icon-folder	florianwoelki/obsidian-iconize
obsidian-tasks-plugin	obsidian-tasks-group/obsidian-tasks
calendar	liamcain/obsidian-calendar-plugin
homepage	mirnovov/obsidian-homepage
obsidian-linter	platers/obsidian-linter
dataview	blacksmithgu/obsidian-dataview
terminal	polyipseity/obsidian-terminal
table-editor-obsidian	tgrosinger/advanced-tables-obsidian
obsidian-style-settings	obsidian-community/obsidian-style-settings
obsidian-excalidraw-plugin	zsviczian/obsidian-excalidraw-plugin
quickadd	chhoumann/quickadd
karpathywiki	green-dalii/obsidian-llm-wiki
claude-sidebar	derek-larson14/obsidian-claude-sidebar
obsidian-outliner	vslinko/obsidian-outliner
pdf-plus	ryotaushio/obsidian-pdf-plus
templater-obsidian	silentvoid13/Templater
PLUGINS

print $'nldates-obsidian\tremoved-from-official-registry\t-\t-\tomitted\tlegacy plugin not reinstalled' >> "$LOCK"
chmod -R u+rwX,go-rwx "$PLUGIN_ROOT"
print 'obsidian-plugin: PASS all installed plugins remain disabled'
