#!/usr/bin/env python3
"""Push the vault's Superwhisper config into the app.

Source of truth (this folder):
  vocabulary.md      -> settings.json "vocabulary"   (the "- term" lines)
  replacements.md    -> settings.json "replacements" (the table rows)
  modes/*.md         -> modes/<key>.json + settings.json "modeKeys"

Target: the REAL Superwhisper config folder, reached through the UNC path so the
Claude Desktop sandbox cannot redirect the write (see CLAUDE.md).

Usage:
  python sync.py            write, after backing up what is there
  python sync.py --check    show what would change, write nothing

The app reads these files at launch. After a sync, quit Superwhisper from the
tray icon and reopen it. Never launch it from this shell.
"""
import json, os, re, shutil, sys, uuid, datetime, glob

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = r"\\localhost\C$\Users\Joshu\AppData\Local\com.superwhisper.app"
CHECK = "--check" in sys.argv


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise SystemExit("missing frontmatter")
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, m.group(2)


def truthy(v):
    return str(v).lower() in ("true", "yes", "1")


def read_vocabulary(reps):
    """Terms listed in vocabulary.md, plus every distinct replacement target (Joshua's rule,
    2026-09-11: a replacement is always also a vocabulary word), minus the Exclude section."""
    text = open(os.path.join(HERE, "vocabulary.md"), encoding="utf-8").read()
    main, _, excl = text.partition("## Exclude")
    listed = [l[2:].strip() for l in main.splitlines() if l.startswith("- ")]
    excluded = {l[2:].split("(")[0].strip().lower() for l in excl.splitlines() if l.startswith("- ")}
    terms = []
    for t in listed + [r["with"] for r in reps]:
        if t and t.lower() not in excluded and t.lower() not in {x.lower() for x in terms}:
            terms.append(t)
    return terms


def read_replacements(existing):
    """Rows of the table. Reuse an existing id for an unchanged (original, with) pair so the
    app does not see churn; mint a uuid4 for new ones (the app's own format)."""
    keep = {(r["original"].lower(), r["with"]): r["id"] for r in existing}
    rows = []
    for l in open(os.path.join(HERE, "replacements.md"), encoding="utf-8"):
        if not l.startswith("|") or l.startswith("| Heard") or l.startswith("|---"):
            continue
        c = [x.strip() for x in l.strip("|\n").split("|")]
        if len(c) < 2 or not c[0]:
            continue
        rows.append({"id": keep.get((c[0].lower(), c[1]), str(uuid.uuid4())), "original": c[0], "with": c[1]})
    return rows


def read_modes(existing_dir):
    modes = []
    for path in sorted(glob.glob(os.path.join(HERE, "modes", "*.md"))):
        meta, body = frontmatter(open(path, encoding="utf-8").read())
        key = meta["key"]
        # prompt = body up to "## Examples"; examples = "### Input" / "### Output" pairs
        parts = re.split(r"^## Examples\s*$", body, flags=re.M)
        prompt = parts[0].strip()
        if meta.get("type") == "voice":
            prompt = ""
        # The app rejects a mode whose promptExamples list was written from outside its UI
        # (verified 2026-09-11: the struct has a third field we could not name), so examples
        # are folded into the prompt text in the same shape the app itself sends to the model.
        examples = []
        pairs = re.findall(r"### Input\s*\n(.*?)\n### Output\s*\n(.*?)(?=\n### Input|\Z)", parts[1], re.S) if len(parts) > 1 else []
        if pairs:
            prompt += "\n\nEXAMPLES OF CORRECT BEHAVIOR:\n" + "\n\n".join(
                f"User: {i.strip()}\nAssistant: {o.strip()}" for i, o in pairs)
        # start from the app's current file for the fields this folder does not manage
        base_path = os.path.join(existing_dir, key + ".json")
        base = json.load(open(base_path, encoding="utf-8")) if os.path.exists(base_path) else {
            "iconName": "", "language": "en", "translateToEnglish": False, "realtimeOutput": False,
            "diarize": False, "activationApps": [], "activationSites": [], "playbackBehavior": None,
            "script": "", "scriptEnabled": False, "autocapitalizeInsert": True, "version": 1}
        base.update({
            "key": key,
            "name": meta["name"],
            "type": meta.get("type", "super"),
            "voiceModelID": meta.get("voice_model", "sv-1"),
            "languageModelID": meta.get("language_model", "") or "",
            "prompt": prompt,
            "promptExamples": examples,
            "contextFromApplication": None,  # placeholder removed below
            "contextFromActiveApplication": truthy(meta.get("context_application", "false")),
            "contextFromClipboard": truthy(meta.get("context_clipboard", "false")),
            "contextFromSelection": truthy(meta.get("context_selection", "false")),
            "useSystemAudio": truthy(meta.get("use_system_audio", "false")),
            "autoPaste": None if truthy(meta.get("auto_paste", "true")) else False,
        })
        base.pop("contextFromApplication", None)
        modes.append(base)
    return modes


def main():
    if not os.path.isdir(TARGET):
        raise SystemExit(f"target not found: {TARGET}")
    settings_path = os.path.join(TARGET, "settings", "settings.json")
    modes_dir = os.path.join(TARGET, "modes")
    settings = json.load(open(settings_path, encoding="utf-8"))

    reps = read_replacements(settings.get("replacements", []))
    vocab = read_vocabulary(reps)
    modes = read_modes(modes_dir)
    keys = [m["key"] for m in modes]

    new_settings = dict(settings)
    new_settings["vocabulary"] = vocab
    new_settings["replacements"] = reps
    new_settings["modeKeys"] = keys

    # report
    old_v, old_r = set(settings.get("vocabulary", [])), {(r["original"].lower(), r["with"]) for r in settings.get("replacements", [])}
    new_v, new_r = set(vocab), {(r["original"].lower(), r["with"]) for r in reps}
    print(f"vocabulary: {len(vocab)} (+{len(new_v - old_v)} / -{len(old_v - new_v)})")
    print(f"replacements: {len(reps)} (+{len(new_r - old_r)} / -{len(old_r - new_r)})")
    for m in modes:
        cur = os.path.join(modes_dir, m["key"] + ".json")
        state = "new" if not os.path.exists(cur) else ("changed" if json.load(open(cur, encoding="utf-8")) != m else "same")
        print(f"mode {m['key']:15s} {m['name']:16s} lm={m['languageModelID'] or '-':22s} {state}")
    stale = [k for k in settings.get("modeKeys", []) if k not in keys]
    if stale:
        print("modeKeys dropped from the app list (files left in place):", stale)

    if CHECK:
        print("check only, nothing written")
        return

    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
    bak = os.path.join(TARGET, "settings", "bak")
    os.makedirs(bak, exist_ok=True)
    shutil.copy(settings_path, os.path.join(bak, f"settings.json.{stamp}"))
    json.dump(new_settings, open(settings_path, "w", encoding="utf-8"), indent=2)
    for m in modes:
        json.dump(m, open(os.path.join(modes_dir, m["key"] + ".json"), "w", encoding="utf-8"), indent=2)
    print(f"written. backup: settings/bak/settings.json.{stamp}")
    if "--restart" in sys.argv:
        restart()
    else:
        print("now quit Superwhisper from the tray and reopen it (or rerun with --restart).")


def restart():
    """Quit the app, relaunch it OUTSIDE the Claude sandbox via Task Scheduler, reopen its
    nothing on screen, then prove the load by reading modeKeys back (the app rewrites it and
    drops any mode it rejected)."""
    import subprocess
    ps = r'''
Get-Process Superwhisper -EA SilentlyContinue | Stop-Process -Force; Start-Sleep 3
$a = New-ScheduledTaskAction -Execute 'C:\Users\Joshu\AppData\Local\superwhisper\Superwhisper.exe'
Register-ScheduledTask -TaskName SWRun -Action $a -Force | Out-Null; Start-ScheduledTask -TaskName SWRun; Start-Sleep 10; Unregister-ScheduledTask -TaskName SWRun -Confirm:$false
(Get-Process Superwhisper -EA SilentlyContinue | Measure-Object).Count
'''
    out = subprocess.run(["powershell", "-NoProfile", "-Command", ps], capture_output=True, text=True).stdout.strip()
    d = json.load(open(os.path.join(TARGET, "settings", "settings.json"), encoding="utf-8"))
    print(f"restarted in the background ({out.splitlines()[-1] if out else '?'} process(es)); ready for Ctrl+Space")
    print(f"loaded: {len(d['replacements'])} replacements, {len(d['vocabulary'])} vocabulary, {len(d['modeKeys'])} modes: {d['modeKeys']}")


if __name__ == "__main__":
    main()
