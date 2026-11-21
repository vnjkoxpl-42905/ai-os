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
  python sync.py --modes-only --left-alt --restart
                           preserve live word lists, apply custom modes and Alt toggle
  python sync.py --modes-only --left-alt --silence-removal off --restart
                           disable silence removal, preserving other preferences
  python sync.py --modes-only --word-lists-file PATH --restart
                           apply exact lists from an empty profile or saved backup JSON

The app reads these files at launch. After a sync, quit Superwhisper from the
tray icon and reopen it. Never launch it from this shell.
"""
import argparse, hashlib, json, os, re, shutil, sys, uuid, datetime, glob

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--check", action="store_true")
parser.add_argument("--modes-only", action="store_true")
parser.add_argument("--left-alt", action="store_true")
parser.add_argument("--plain-recorder", action="store_true")
parser.add_argument("--restart", action="store_true")
parser.add_argument("--preserve-extra-modes", action="store_true",
                    help="keep additional loaded mode keys with existing app JSON files; do not rewrite them")
parser.add_argument("--active-mode", metavar="KEY",
                    help="activate a canonical or explicitly preserved extra mode after restart; omitted preserves the current mode")
parser.add_argument("--expected-active-mode", metavar="KEY",
                    help="refuse writes if the current active mode differs before or after stopping")
parser.add_argument("--silence-removal", choices=("off", "on"),
                    help="set silence removal; omitted preserves the current preference")
parser.add_argument("--word-lists-file", metavar="PATH",
                    help="JSON containing exact vocabulary and replacements arrays; overrides --modes-only preservation")
parser.add_argument("--expected-word-lists-sha256", metavar="SHA256",
                    help="refuse writes unless current canonical vocabulary/replacements JSON matches this hash")
ARGS = parser.parse_args()
if ARGS.expected_word_lists_sha256 is not None:
    if not re.fullmatch(r"[0-9a-fA-F]{64}", ARGS.expected_word_lists_sha256):
        parser.error("--expected-word-lists-sha256 must contain exactly 64 hexadecimal characters")
    ARGS.expected_word_lists_sha256 = ARGS.expected_word_lists_sha256.lower()


class WordListConflict(Exception):
    pass


class ActiveModeConflict(Exception):
    pass


def check_active_mode(keys):
    if ARGS.active_mode is not None and ARGS.active_mode not in keys:
        raise ActiveModeConflict(f"active-mode conflict: {ARGS.active_mode!r} is not a canonical or preserved mode key")


def check_expected_active_mode():
    if ARGS.expected_active_mode is not None:
        preferences = json.load(open(os.path.join(TARGET, "preferences.json"), encoding="utf-8"))
        actual = preferences.get("activeMode")
        if actual != ARGS.expected_active_mode:
            raise ActiveModeConflict(f"active-mode conflict: current mode {actual!r} differs from expected {ARGS.expected_active_mode!r}")


def word_lists_sha256(settings):
    value = {key: settings.get(key, []) for key in ("vocabulary", "replacements")}
    payload = json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def check_word_lists_hash(settings):
    if ARGS.expected_word_lists_sha256 is not None:
        actual = word_lists_sha256(settings)
        if actual != ARGS.expected_word_lists_sha256:
            raise WordListConflict(f"word-list conflict: current SHA256 {actual} differs from the expected value")


def load_word_lists(path):
    try:
        with open(path, encoding="utf-8-sig") as handle:
            value = json.load(handle)
    except (OSError, ValueError) as exc:
        raise ValueError(f"cannot read word-lists file: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError("word-lists file must contain a JSON object")
    vocabulary, replacements = value.get("vocabulary"), value.get("replacements")
    if not isinstance(vocabulary, list) or any(not isinstance(term, str) for term in vocabulary):
        raise ValueError("vocabulary must be an array of strings")
    if not isinstance(replacements, list) or any(
        not isinstance(row, dict) or any(not isinstance(row.get(key), str) for key in ("id", "original", "with"))
        for row in replacements
    ):
        raise ValueError("replacements must be an array of objects with string id, original, and with fields")
    return {"vocabulary": vocabulary, "replacements": replacements}


WORD_LISTS = None
if ARGS.word_lists_file is not None:
    try:
        WORD_LISTS = load_word_lists(ARGS.word_lists_file)
    except ValueError as exc:
        parser.error(str(exc))

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = r"\\localhost\C$\Users\Joshu\AppData\Local\com.superwhisper.app"
CHECK = ARGS.check
MODES_ONLY = ARGS.modes_only


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
    """Exactly the "- term" lines of vocabulary.md. Replacement targets are NOT added:
    that rule (2026-09-11, morning) pushed the list to 654 and transcription got worse
    within the hour, so Joshua reversed it the same evening. Keep the list short."""
    text = open(os.path.join(HERE, "vocabulary.md"), encoding="utf-8").read()
    terms = []
    for t in [l[2:].strip() for l in text.splitlines() if l.startswith("- ")]:
        if t and t.lower() not in {x.lower() for x in terms}:
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


def read_shared():
    """Two blocks from shared.md. `first` is prepended to every mode prompt: the silence-artefact
    strip has to be the model's first instruction, not a footnote (measured 2026-09-26: appended
    at the bottom it cleaned 5% of them). `rest` is the house rules and glossary, appended."""
    text = open(os.path.join(HERE, "shared.md"), encoding="utf-8").read()
    first = "<step_zero>" + text.split("<step_zero>", 1)[1].split("</step_zero>", 1)[0] + "</step_zero>"
    rest = "<house_rules>" + text.split("<house_rules>", 1)[1].rsplit("</glossary>", 1)[0] + "</glossary>"
    return first.strip(), rest.strip()

def read_modes(existing_dir):
    shared_first, shared = read_shared()
    modes = []
    for path in sorted(glob.glob(os.path.join(HERE, "modes", "*.md"))):
        meta, body = frontmatter(open(path, encoding="utf-8").read())
        key = meta["key"]
        # prompt = body up to "## Examples"; examples = "### Input" / "### Output" pairs
        parts = re.split(r"^## Examples\s*$", body, flags=re.M)
        prompt = parts[0].strip()
        if meta.get("type") == "voice":
            prompt = ""
        else:
            if shared_first not in prompt:
                prompt = shared_first + "\n\n" + prompt.lstrip()
            if shared not in prompt:
                prompt = prompt.rstrip() + "\n\n" + shared
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
            "type": meta.get("type", "custom"),
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


def mode_keys(settings, modes_dir, canonical_keys):
    keys = list(canonical_keys)
    if ARGS.preserve_extra_modes:
        for key in settings.get("modeKeys", []):
            if key not in keys and os.path.isfile(os.path.join(modes_dir, key + ".json")):
                keys.append(key)
    return keys


def main():
    if not os.path.isdir(TARGET):
        raise SystemExit(f"target not found: {TARGET}")
    settings_path = os.path.join(TARGET, "settings", "settings.json")
    modes_dir = os.path.join(TARGET, "modes")
    settings = json.load(open(settings_path, encoding="utf-8"))
    try:
        check_word_lists_hash(settings)
        check_expected_active_mode()
    except (WordListConflict, ActiveModeConflict) as exc:
        raise SystemExit(f"{exc}; no sync writes performed and app was not stopped") from exc

    if WORD_LISTS is not None:
        reps, vocab = WORD_LISTS["replacements"], WORD_LISTS["vocabulary"]
    else:
        reps = settings.get("replacements", []) if MODES_ONLY else read_replacements(settings.get("replacements", []))
        vocab = settings.get("vocabulary", []) if MODES_ONLY else read_vocabulary(reps)
    modes = read_modes(modes_dir)
    canonical_keys = [m["key"] for m in modes]
    keys = mode_keys(settings, modes_dir, canonical_keys)
    try:
        check_active_mode(keys)
    except ActiveModeConflict as exc:
        raise SystemExit(f"{exc}; no sync writes performed and app was not stopped") from exc

    new_settings = dict(settings)
    new_settings["vocabulary"] = vocab
    new_settings["replacements"] = reps
    new_settings["modeKeys"] = keys

    # report
    old_v, old_r = set(settings.get("vocabulary", [])), {(r["original"].lower(), r["with"]) for r in settings.get("replacements", [])}
    new_v, new_r = set(vocab), {(r["original"].lower(), r["with"]) for r in reps}
    print(f"vocabulary: {len(vocab)} (+{len(new_v - old_v)} / -{len(old_v - new_v)})")
    print(f"replacements: {len(reps)} (+{len(new_r - old_r)} / -{len(old_r - new_r)})")
    if WORD_LISTS is not None:
        print(f"word lists: exact override from {os.path.abspath(ARGS.word_lists_file)}")
    for m in modes:
        cur = os.path.join(modes_dir, m["key"] + ".json")
        state = "new" if not os.path.exists(cur) else ("changed" if json.load(open(cur, encoding="utf-8")) != m else "same")
        print(f"mode {m['key']:15s} {m['name']:16s} lm={m['languageModelID'] or '-':22s} {state}")
    stale = [k for k in settings.get("modeKeys", []) if k not in keys]
    if stale:
        print("modeKeys dropped from the app list (files left in place):", stale)
    extra_keys = [key for key in keys if key not in canonical_keys]
    if extra_keys:
        print("extra app modes preserved without rewriting their files:", extra_keys)
    if ARGS.silence_removal is not None or ARGS.active_mode is not None:
        preferences = json.load(open(os.path.join(TARGET, "preferences.json"), encoding="utf-8"))
        if ARGS.silence_removal is not None:
            print(f"silence removal: {preferences.get('enableSilenceRemoval', 'unset')} -> {ARGS.silence_removal == 'on'}")
        if ARGS.active_mode is not None:
            print(f"active mode: {preferences.get('activeMode', 'unset')} -> {ARGS.active_mode}")

    if CHECK:
        print("check only, nothing written")
        return

    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
    bak = os.path.join(TARGET, "settings", "bak")
    if "--restart" in sys.argv:
        # Stop before writing: a running app can flush its old state over new files.
        import subprocess
        subprocess.run(["powershell", "-NoProfile", "-Command", "Get-Process Superwhisper -EA SilentlyContinue | Stop-Process -Force"], check=True, capture_output=True)
        settings = json.load(open(settings_path, encoding="utf-8"))
        try:
            check_word_lists_hash(settings)
            check_expected_active_mode()
            keys = mode_keys(settings, modes_dir, canonical_keys)
            check_active_mode(keys)
        except (WordListConflict, ActiveModeConflict) as exc:
            try:
                processes = launch_app()
            except (Exception, SystemExit) as recovery_error:
                raise SystemExit(f"{exc}; no sync writes performed; automatic unchanged-app relaunch failed: {recovery_error}") from exc
            raise SystemExit(f"{exc}; no sync writes performed; app relaunched unchanged ({processes} process(es)); requested settings were not applied or verified") from exc
        new_settings = dict(settings)
        new_settings.update(vocabulary=vocab, replacements=reps, modeKeys=keys)
    os.makedirs(bak, exist_ok=True)
    shutil.copy(settings_path, os.path.join(bak, f"settings.json.{stamp}"))
    mode_bak = os.path.join(bak, f"modes.{stamp}")
    shutil.copytree(modes_dir, mode_bak)
    preferences_path = os.path.join(TARGET, "preferences.json")
    shutil.copy(preferences_path, os.path.join(bak, f"preferences.json.{stamp}"))
    if "--left-alt" in sys.argv or "--plain-recorder" in sys.argv or ARGS.silence_removal is not None or ARGS.active_mode is not None:
        preferences = json.load(open(preferences_path, encoding="utf-8"))
        if "--left-alt" in sys.argv:
            preferences.update(toggleRecordingShortcut="AltLeft", p2t=False)
        if "--plain-recorder" in sys.argv:
            preferences.update(enableWindowEffects=False, alwaysShowMiniRecorder=False)
        if ARGS.silence_removal is not None:
            preferences["enableSilenceRemoval"] = ARGS.silence_removal == "on"
        if ARGS.active_mode is not None:
            preferences["activeMode"] = ARGS.active_mode
        json.dump(preferences, open(preferences_path, "w", encoding="utf-8"), indent=2)
    json.dump(new_settings, open(settings_path, "w", encoding="utf-8"), indent=2)
    for m in modes:
        json.dump(m, open(os.path.join(modes_dir, m["key"] + ".json"), "w", encoding="utf-8"), indent=2)
    print(f"written. backup: settings/bak/settings.json.{stamp}")
    if "--restart" in sys.argv:
        restart(expected_mode_keys=keys)
    else:
        print("now quit Superwhisper from the tray and reopen it (or rerun with --restart).")


def launch_app():
    """Relaunch outside the agent process and return the confirmed process count."""
    import subprocess
    ps = r'''
$a = New-ScheduledTaskAction -Execute 'C:\Users\Joshu\AppData\Local\superwhisper\Superwhisper.exe'
Register-ScheduledTask -TaskName SWRun -Action $a -Force | Out-Null; Start-ScheduledTask -TaskName SWRun; Start-Sleep 10; Unregister-ScheduledTask -TaskName SWRun -Confirm:$false
(Get-Process Superwhisper -EA SilentlyContinue | Measure-Object).Count
'''
    result = subprocess.run(["powershell", "-NoProfile", "-Command", ps], capture_output=True, text=True, check=True)
    out = result.stdout.strip()
    if not out or not out.splitlines()[-1].isdigit() or int(out.splitlines()[-1]) < 1:
        raise SystemExit("restart failed: no Superwhisper process confirmed")
    return int(out.splitlines()[-1])


def restart(expected_mode_keys=None):
    """Relaunch in the background, then verify the requested configuration."""
    processes = launch_app()
    d = json.load(open(os.path.join(TARGET, "settings", "settings.json"), encoding="utf-8"))
    preferences = json.load(open(os.path.join(TARGET, "preferences.json"), encoding="utf-8"))
    shortcut_key = "pushToTalkShortcut" if preferences.get("p2t", False) else "toggleRecordingShortcut"
    shortcut = preferences.get(shortcut_key, "unset")
    behavior = "hold to record" if preferences.get("p2t", False) else "press to start/stop"
    print(f"restarted in the background ({processes} process(es)); recording: {shortcut} ({behavior})")
    print(f"loaded: {len(d['replacements'])} replacements, {len(d['vocabulary'])} vocabulary, {len(d['modeKeys'])} modes: {d['modeKeys']}")
    expected = read_modes(os.path.join(TARGET, "modes"))
    expected_keys = set(expected_mode_keys) if expected_mode_keys is not None else {m['key'] for m in expected}
    if set(d['modeKeys']) != expected_keys:
        raise SystemExit("verification failed: loaded mode keys differ from source")
    for mode in expected:
        loaded = json.load(open(os.path.join(TARGET, "modes", mode['key'] + '.json'), encoding="utf-8"))
        for field in ('type', 'prompt', 'languageModelID', 'contextFromActiveApplication', 'contextFromClipboard', 'contextFromSelection'):
            if loaded.get(field) != mode.get(field):
                raise SystemExit(f"verification failed: {mode['key']} {field} differs")
    if "--left-alt" in sys.argv and (shortcut != "AltLeft" or preferences.get("p2t", False)):
        raise SystemExit("verification failed: Left Alt toggle did not persist")
    if "--plain-recorder" in sys.argv:
        if preferences.get("enableWindowEffects") or preferences.get("alwaysShowMiniRecorder"):
            raise SystemExit("verification failed: recorder display settings did not persist")
        print("verified: window effects and always-visible mini recorder disabled")
    if ARGS.silence_removal is not None:
        expected_silence_removal = ARGS.silence_removal == "on"
        if preferences.get("enableSilenceRemoval") is not expected_silence_removal:
            raise SystemExit("verification failed: silence removal preference did not persist")
        print(f"verified: silence removal {'enabled' if expected_silence_removal else 'disabled'}")
    if ARGS.active_mode is not None:
        if preferences.get("activeMode") != ARGS.active_mode:
            raise SystemExit("verification failed: active mode did not persist")
        print(f"verified: active mode {ARGS.active_mode}")
    if WORD_LISTS is not None:
        for field in ("vocabulary", "replacements"):
            if d.get(field) != WORD_LISTS[field]:
                raise SystemExit(f"verification failed: loaded {field} differs from word-lists file")
        print("verified: loaded vocabulary and replacements exactly match word-lists file")
    print("verified: loaded mode files match source types, prompts, models, and context flags")


if __name__ == "__main__":
    main()
