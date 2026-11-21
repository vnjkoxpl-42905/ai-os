"""Generate a bounded local ARMS inventory; never reads credential values or prompts."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import shutil
import subprocess
import tomllib

ROOT = Path(__file__).resolve().parents[2]
HOME = Path.home()
OUTPUT = ROOT / "system/generated/brain-inventory.generated.json"


def snapshot():
    def presence(path):
        return {"path": str(path), "present": path.exists()}
    registries = ["connections.md", "skills/INDEX.md", "skills/PARITY.md", "wiki/index.md",
                  "wiki/tasks.md", "system/schema/llm-wiki.md", "references/automation-backlog.md"]
    data = {"schema": 1, "observed_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "scope": "Bounded local filesystem/configuration snapshot; live authentication, granted scopes, usage and delivery UNKNOWN",
            "registries": [presence(ROOT / x) for x in registries], "skills": [], "routines": [],
            "memory": [], "applications": [], "unknowns": []}
    for name, path in [("Claude project", ROOT / ".claude/skills"), ("Codex project", ROOT / ".agents/skills"),
                       ("Gemini project", ROOT / ".gemini/skills"), ("Claude home", HOME / ".claude/skills"),
                       ("Agents home", HOME / ".agents/skills"), ("Codex home", HOME / ".codex/skills")]:
        entries = sorted(p.parent.name for p in path.glob("*/SKILL.md")) if path.exists() else []
        data["skills"].append({"owner": name, **presence(path), "entrypoint_count": len(entries),
                               "names": entries, "usage": "UNKNOWN", "discovery": "filesystem presence only"})
    for name, path in [("Claude project memory", HOME / ".claude/projects/C--Users-Joshu-dev-ai-os/memory"),
                       ("Codex memory", HOME / ".codex/memories"), ("Compiled wiki", ROOT / "wiki"),
                       ("Teaching corpus", ROOT / "corpus"), ("Student records", ROOT / "students")]:
        data["memory"].append({"owner": name, **presence(path), "access": "local filesystem; content not inventoried"})
    for tool in ["gws", "gh", "firecrawl", "codex", "claude", "obsidian"]:
        found = shutil.which(tool) or shutil.which(tool + ".exe") or shutil.which(tool + ".ps1")
        data["applications"].append({"name": tool, "mechanism": "CLI", "path_on_process_PATH": found,
                                      "auth": "UNKNOWN: no provider call", "usage": "UNKNOWN"})
    # Only explicitly selected metadata. Do not serialize prompts, environment or credentials.
    for slug in ["monitor-payments-calendar-and-session-notes", "update-claudex-skills"]:
        path = HOME / ".codex/automations" / slug / "automation.toml"
        entry = {"owner": "Codex automation", "id": slug, **presence(path), "execution_success": "UNKNOWN"}
        if path.is_file():
            with path.open("rb") as stream:
                config = tomllib.load(stream)
            for key in ["name", "status", "rrule"]:
                if key in config:
                    entry[key] = config[key]
        data["routines"].append(entry)
    if shutil.which("powershell.exe"):
        command = "Get-ScheduledTask -TaskName 'AI OS - Matt Pocock Skills Sync' -ErrorAction Stop | Select-Object TaskName,TaskPath,State | ConvertTo-Json -Compress"
        result = subprocess.run(["powershell.exe", "-NoProfile", "-Command", command], capture_output=True, text=True, timeout=25)
        if result.returncode == 0:
            selected = json.loads(result.stdout)
            data["routines"].append({"owner": "Windows Task Scheduler", "metadata": selected, "execution_success": "UNKNOWN: state does not prove execution"})
        else:
            data["unknowns"].append("Named Windows task metadata could not be read")
    data["unknowns"].extend(["No full task scheduler or automation inventory", "No provider scopes, last-use or authentication recheck", "No connection or routine retired"])
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write generated inventory using compare-and-swap")
    args = parser.parse_args()
    before = OUTPUT.read_bytes() if OUTPUT.exists() else None
    data = snapshot()
    payload = (json.dumps(data, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    if args.write:
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        current = OUTPUT.read_bytes() if OUTPUT.exists() else None
        if current != before:
            raise SystemExit("Inventory changed during collection; rerun rather than overwrite")
        OUTPUT.write_bytes(payload)
        print(json.dumps({"output": str(OUTPUT), "sha256": hashlib.sha256(payload).hexdigest(),
                          "skills": {r["owner"]: r["entrypoint_count"] for r in data["skills"]},
                          "routines": len(data["routines"]), "live_auth": "UNKNOWN"}, indent=2))
    else:
        print(payload.decode("utf-8"), end="")


if __name__ == "__main__":
    main()
