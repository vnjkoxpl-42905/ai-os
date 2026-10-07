"""Joshua runs this himself. Installs the accommodations-email skill everywhere and adds send permissions.

Safe to re-run: every step checks before it changes anything.
"""
import json, os, shutil

home = os.path.expanduser("~")
root = os.path.join(home, "dev", "ai-os")
master = os.path.join(root, "skills", "claude", "accommodations-email")

# 1. Install identical copies: project (Claude + Codex) and global (Claude + Codex), so it works from any folder.
for dest in [
    os.path.join(root, ".claude", "skills", "accommodations-email"),
    os.path.join(root, ".agents", "skills", "accommodations-email"),
    os.path.join(home, ".claude", "skills", "accommodations-email"),
    os.path.join(home, ".agents", "skills", "accommodations-email"),
]:
    shutil.copytree(master, dest, dirs_exist_ok=True)
    print("installed", dest)

# 2. Permissions: Gmail send/reply/forward/drafts + the skill script from any location. Deletes stay blocked.
settings = os.path.join(home, ".claude", "settings.json")
shutil.copy(settings, settings + ".bak-2026-09-23")
d = json.load(open(settings, encoding="utf-8"))
allow = d.setdefault("permissions", {}).setdefault("allow", [])
rules = [
    "Bash(gws gmail +send:*)",
    "Bash(gws gmail +reply:*)",
    "Bash(gws gmail +reply-all:*)",
    "Bash(gws gmail +forward:*)",
    "Bash(gws gmail users messages send:*)",
    "Bash(gws gmail users drafts create:*)",
    "Bash(gws gmail users drafts send:*)",
    "Bash(python *accommodations-email/scripts/send.py*)",
    "Bash(python \"*accommodations-email/scripts/send.py\"*)",
]
added = [r for r in rules if r not in allow]
allow.extend(added)
json.dump(d, open(settings, "w", encoding="utf-8"), indent=2)
print(f"settings: added {len(added)} rules (backup: {settings}.bak-2026-09-23)")
