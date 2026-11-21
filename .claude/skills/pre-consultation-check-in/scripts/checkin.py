#!/usr/bin/env python3
"""
Pre-consultation check-in: find Cal.com consultations on Joshua's Google
Calendar, register a one-shot Windows scheduled task 30 minutes before each
one, and (when that task fires) re-verify the event and send the check-in
email through the gws CLI.

Subcommands
  find      list consultations in a window and whether each is already covered
  schedule  register the T-30 tasks (or send now if T-30 already passed)
  send      what the scheduled task runs; verifies the event, then sends
  status    what is scheduled, what fired, what failed
  cancel    remove a scheduled task and mark the row so it is not re-created

Everything the agent needs is in the JSON these print (--json) and in the
vault log at wiki/PRE-CONSULT-LOG.md. No LLM runs at send time.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import traceback
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

# --------------------------------------------------------------------------
# Machine facts. Hard-coded on purpose: this runs from Task Scheduler with no
# environment, so nothing may depend on PATH, cwd, or a shell profile.
# --------------------------------------------------------------------------
VAULT = Path(os.environ.get("AI_OS_VAULT", r"C:\Users\Joshu\dev\ai-os"))
LOG_MD = VAULT / "wiki" / "PRE-CONSULT-LOG.md"
LEDGER_MD = VAULT / "wiki" / "send-ledger.md"
NODE = Path(r"C:\Users\Joshu\dev\tools\node\node.exe")
GWS_RUNJS = Path(r"C:\Users\Joshu\dev\tools\node\node_modules\@googleworkspace\cli\run.js")
SKILL_DIR = Path(__file__).resolve().parent.parent
RUNLOG = SKILL_DIR / "logs" / "checkin.log"

try:
    TZ = ZoneInfo("America/Toronto")  # every consultation is booked in this zone
except Exception:  # Windows Python has no tz database unless `pip install tzdata`
    TZ = datetime.now().astimezone().tzinfo  # this laptop lives in Eastern time; same clock
LEAD = timedelta(minutes=30)          # send this long before the consultation
TASK_PATH = "\\LSATU\\PreConsult\\"   # Task Scheduler folder (trailing backslash required)
CALENDAR_ID = "primary"

# The one rule that identifies a consultation. Verified 2026-09-11 against 241
# calendar events: 70/70 consultations match, 0/171 other events match. See
# references/identification.md before loosening this.
CONSULT_RE = re.compile(r"^Consultation\s+between\s+Joshua\s+and\s+(.+)$")

SUBJECT = "Consultation check-in"
BODY = """Hi {first},

Just checking in before our consultation today. Looking forward to speaking with you. I just wanted to make sure everything is still good for our meeting.

If anything has come up or you need to reschedule, just let me know.

Best,

Joshua
"""

COLUMNS = ["Consultation (Toronto)", "Student", "Email", "Status", "Fires at",
           "Task", "Note", "Event ID", "iCalUID"]
COVERED = {"scheduled", "sent", "sent-late", "sent-now"}   # do not touch again
OPTED_OUT = {"cancelled-by-joshua"}                    # Joshua said no; skip unless --force


# --------------------------------------------------------------------------
# Small utilities
# --------------------------------------------------------------------------
def now() -> datetime:
    return datetime.now(timezone.utc).astimezone(TZ)


def runlog(msg: str) -> None:
    RUNLOG.parent.mkdir(parents=True, exist_ok=True)
    with RUNLOG.open("a", encoding="utf-8") as f:
        f.write(f"{now():%Y-%m-%d %H:%M:%S} {msg}\n")


def fmt(dt: datetime) -> str:
    return dt.astimezone(TZ).strftime("%Y-%m-%d %H:%M")


def parse_iso(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone(TZ)


class GwsError(RuntimeError):
    def __init__(self, code: int, message: str):
        super().__init__(f"gws error {code}: {message}")
        self.code = code


def gws(*args: str) -> dict:
    """Call the gws CLI through node directly (no cmd.exe, so newlines in
    --body survive), capture stdout only (stderr carries the keyring banner),
    and turn API errors into GwsError."""
    if NODE.exists() and GWS_RUNJS.exists():
        cmd = [str(NODE), str(GWS_RUNJS), *args]
    else:  # fall back to whatever gws is on PATH (e.g. the Mac)
        cmd = ["gws", *args]
    p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    out = p.stdout.strip()
    data: dict = {}
    if out:
        try:
            data = json.loads(out)
        except json.JSONDecodeError:
            data = {"_raw": out}
    if isinstance(data, dict) and "error" in data:
        err = data["error"]
        if isinstance(err, dict):
            raise GwsError(int(err.get("code", 0) or 0), str(err.get("message", err)))
        raise GwsError(0, str(err))
    if p.returncode != 0 and not data:
        raise GwsError(p.returncode, (p.stderr or "")[-800:])
    return data


def student_email(event: dict) -> str | None:
    others = [a.get("email") for a in event.get("attendees", []) if not a.get("self")]
    return others[0] if len(others) == 1 else (others[0] if others else None)


def student_name(event: dict) -> str:
    m = CONSULT_RE.match(event.get("summary", ""))
    return (m.group(1) if m else event.get("summary", "")).strip()


def first_name(full: str) -> str:
    tok = full.split()[0] if full.split() else full
    return tok[:1].upper() + tok[1:] if tok.islower() else tok


def slug(full: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", full.lower()).strip("-") or "unknown"


def task_name(start: datetime, full: str) -> str:
    return f"PreConsult_{start:%Y-%m-%d_%H%M}_{re.sub(r'[^A-Za-z0-9]+', '-', full).strip('-')}"


# --------------------------------------------------------------------------
# Calendar
# --------------------------------------------------------------------------
@dataclass
class Consult:
    event_id: str
    ical_uid: str
    name: str
    email: str | None
    start: str          # ISO with offset
    end: str
    hangout: str | None

    @property
    def start_dt(self) -> datetime:
        return parse_iso(self.start)

    @property
    def fire_dt(self) -> datetime:
        return self.start_dt - LEAD


def to_consult(e: dict) -> Consult:
    return Consult(
        event_id=e["id"], ical_uid=e.get("iCalUID", ""), name=student_name(e),
        email=student_email(e), start=e["start"]["dateTime"], end=e["end"]["dateTime"],
        hangout=e.get("hangoutLink"),
    )


def list_consultations(t_from: datetime, t_to: datetime, include_flagged: bool = False) -> tuple[list[Consult], list[dict]]:
    """Every confirmed consultation in the window, plus title-matched events
    that are NOT from Cal.com (flag those; never happened in 241 events)."""
    params = {
        "calendarId": CALENDAR_ID,
        "timeMin": t_from.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "timeMax": t_to.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "singleEvents": True, "orderBy": "startTime", "maxResults": 250,
    }
    data = gws("calendar", "events", "list", "--params", json.dumps(params), "--format", "json")
    found, flagged = [], []
    others: list[str] = []          # titles that did not match, so a "0" answer can show its work
    for e in data.get("items", []):
        if not CONSULT_RE.match(e.get("summary", "")):
            others.append(e.get("summary", "") or "(untitled)")
            continue
        if e.get("status") != "confirmed" or "dateTime" not in e.get("start", {}):
            continue
        if not e.get("iCalUID", "").lower().endswith("@cal.com") and not include_flagged:
            flagged.append({"summary": e.get("summary"), "start": e["start"].get("dateTime"),
                            "iCalUID": e.get("iCalUID"), "why": "title matches but not a Cal.com booking; pass --include-flagged to schedule it"})
            continue
        found.append(to_consult(e))
    list_consultations.last_others = others   # type: ignore[attr-defined]
    return found, flagged


def get_event(event_id: str) -> dict | None:
    """None when the event is gone or cancelled."""
    try:
        e = gws("calendar", "events", "get", "--params",
                json.dumps({"calendarId": CALENDAR_ID, "eventId": event_id}), "--format", "json")
    except GwsError as ex:
        if ex.code in (404, 410):
            return None
        raise
    if e.get("status") == "cancelled":
        return None
    return e


# --------------------------------------------------------------------------
# Vault log (wiki/PRE-CONSULT-LOG.md): one row per consultation, keyed by
# iCalUID, updated in place. The send ledger is append-only and separate.
# --------------------------------------------------------------------------
LOG_HEADER = """---
title: Pre-consultation check-in log
type: operating-layer
record_kind: primary
tags: [operating-layer, correspondence, consultations]
created: 2026-09-11
status: active
subject: Pre-consultation check-in log
aliases: [PRE-CONSULT-LOG]
---

# Pre-consultation check-in log

One row per Cal.com consultation the `pre-consultation-check-in` skill has
handled. Written by `scripts/checkin.py`; safe to read, do not hand-edit rows
(the script rewrites the table). To stop a scheduled send, run
`checkin.py cancel --event-id <id>` rather than deleting the row.

**Status meanings**

- `scheduled` — a one-shot Windows task exists and will send 30 minutes before the consultation
- `sent` / `sent-late` — the email went out (late = fired after T-30 but still before the start, e.g. the laptop was asleep)
- `sent-now` — T-30 had already passed when the skill ran, so it sent immediately
- `cancelled` — the booking disappeared or was cancelled before the send; nothing sent
- `moved` — the start time changed; the old task was replaced (a new `scheduled` row follows)
- `missed` — the task could not run before the consultation started; nothing sent
- `failed` — the send errored; see Note and logs/checkin.log
- `cancelled-by-joshua` — Joshua opted this one out; the skill will not re-create it

Related: [[send-ledger]] gets one row when a send is scheduled and one when it goes out.

## Log

"""


def load_log() -> dict[str, dict]:
    if not LOG_MD.exists():
        return {}
    rows: dict[str, dict] = {}
    for line in LOG_MD.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or line.startswith("| Consultation") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != len(COLUMNS) or not cells[-1]:
            continue
        rows[cells[-1]] = dict(zip(COLUMNS, cells))
    return rows


def save_log(rows: dict[str, dict]) -> None:
    LOG_MD.parent.mkdir(parents=True, exist_ok=True)
    head = LOG_HEADER
    if LOG_MD.exists():
        text = LOG_MD.read_text(encoding="utf-8")
        if "## Log" in text:
            head = text.split("## Log")[0] + "## Log\n\n"
    lines = ["| " + " | ".join(COLUMNS) + " |", "|" + "---|" * len(COLUMNS)]
    for r in sorted(rows.values(), key=lambda r: r["Consultation (Toronto)"]):
        lines.append("| " + " | ".join(str(r.get(c, "")).replace("|", "/") for c in COLUMNS) + " |")
    LOG_MD.write_text(head + "\n".join(lines) + "\n", encoding="utf-8")


def upsert(rows: dict[str, dict], c: Consult, status: str, fires: str = "", task: str = "", note: str = "") -> None:
    rows[c.ical_uid] = {
        "Consultation (Toronto)": fmt(c.start_dt), "Student": c.name, "Email": c.email or "",
        "Status": status, "Fires at": fires, "Task": task, "Note": note,
        "Event ID": c.event_id, "iCalUID": c.ical_uid,
    }


def ledger(recipient: str, what: str, status: str, note: str) -> None:
    """Append one row to wiki/send-ledger.md (append-only by rule)."""
    if not LEDGER_MD.exists():
        runlog(f"ledger missing at {LEDGER_MD}; skipped row: {recipient} {what} {status}")
        return
    row = f"| {now():%Y-%m-%d %H:%M} | {recipient} | {what} | {status} | {note} |\n"
    with LEDGER_MD.open("a", encoding="utf-8") as f:
        f.write(row)


# --------------------------------------------------------------------------
# Windows Task Scheduler
# --------------------------------------------------------------------------
def powershell(script: str) -> str:
    """-EncodedCommand: multi-line scripts via stdin silently produce nothing
    on Windows PowerShell 5, so the script goes in as base64 UTF-16LE."""
    import base64
    enc = base64.b64encode(script.encode("utf-16-le")).decode("ascii")
    p = subprocess.run(["powershell", "-NoProfile", "-NonInteractive", "-EncodedCommand", enc],
                       capture_output=True, text=True, encoding="utf-8")
    if p.returncode != 0:
        raise RuntimeError((p.stderr or p.stdout)[-1500:])
    return p.stdout


def pythonw() -> str:
    exe = Path(sys.executable)
    cand = exe.with_name("pythonw.exe")
    return str(cand if cand.exists() else exe)


def register_task(c: Consult, fire: datetime) -> str:
    """One-shot task at `fire` (local time). Runs as the logged-on user so gws
    can reach the keyring. If the laptop is asleep at T-30 it wakes or catches
    up when available; the task expires at the consultation start, because a
    check-in after the meeting began is worse than none."""
    name = task_name(c.start_dt, c.name)
    fire_local = fire.astimezone()          # machine-local for Task Scheduler
    end_local = c.start_dt.astimezone()
    args = f'"{Path(__file__).resolve()}" send --event-id {c.event_id}'
    ps = f"""
$ErrorActionPreference = 'Stop'
$action  = New-ScheduledTaskAction -Execute '{pythonw()}' -Argument '{args}' -WorkingDirectory '{SKILL_DIR}'
$trigger = New-ScheduledTaskTrigger -Once -At ([datetime]'{fire_local:%Y-%m-%dT%H:%M:%S}')
$trigger.EndBoundary = '{end_local:%Y-%m-%dT%H:%M:%S}'
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -WakeToRun -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Minutes 10) -DeleteExpiredTaskAfter (New-TimeSpan -Hours 2)
$principal = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\\$env:USERNAME" -LogonType Interactive -RunLevel Limited
Register-ScheduledTask -TaskName '{name}' -TaskPath '{TASK_PATH}' -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Description 'LSAT U pre-consultation check-in for {c.name} ({fmt(c.start_dt)}). Created by pre-consultation-check-in skill.' -Force | Out-Null
(Get-ScheduledTask -TaskName '{name}' -TaskPath '{TASK_PATH}').State
"""
    state = powershell(ps).strip()
    runlog(f"registered task {name} fire={fmt(fire)} state={state}")
    return name


def unregister_task(name: str) -> bool:
    if not name:
        return False
    try:
        powershell(f"Unregister-ScheduledTask -TaskName '{name}' -TaskPath '{TASK_PATH}' -Confirm:$false -ErrorAction Stop")
        runlog(f"unregistered task {name}")
        return True
    except RuntimeError as ex:
        runlog(f"unregister {name} failed: {ex}")
        return False


def list_tasks() -> list[dict]:
    # An empty (or missing) task folder makes Get-ScheduledTask throw; that is
    # the normal state after every send, so swallow it and return [].
    ps = f"""
$ProgressPreference = 'SilentlyContinue'
$tasks = @(Get-ScheduledTask -TaskPath '{TASK_PATH}' -ErrorAction SilentlyContinue)
$rows = foreach ($t in $tasks) {{
  $i = $t | Get-ScheduledTaskInfo -ErrorAction SilentlyContinue
  [pscustomobject]@{{ name=$t.TaskName; state=[string]$t.State; next=[string]$i.NextRunTime; last=[string]$i.LastRunTime; result=$i.LastTaskResult }}
}}
if ($rows) {{ @($rows) | ConvertTo-Json -Compress }}
exit 0
"""
    out = powershell(ps).strip()
    if not out:
        return []
    data = json.loads(out)
    return data if isinstance(data, list) else [data]


# --------------------------------------------------------------------------
# The send itself (what the scheduled task runs)
# --------------------------------------------------------------------------
def compose(c: Consult) -> tuple[str, str]:
    return SUBJECT, BODY.format(first=first_name(c.name))


def send_email(c: Consult, dry_run: bool) -> dict:
    subject, body = compose(c)
    args = ["gmail", "+send", "--to", c.email, "--subject", subject, "--body", body, "--format", "json"]
    if dry_run:
        args.append("--dry-run")
    return gws(*args)


def do_send(event_id: str, dry_run: bool = False, force: bool = False, mode: str = "task") -> dict:
    """Verify, then send. Returns a result dict; never raises on a
    'do not send' outcome (those are logged as statuses)."""
    rows = load_log()
    e = get_event(event_id)
    if e is None:
        r = next((r for r in rows.values() if r["Event ID"] == event_id), None)
        if r and not dry_run:
            unregister_task(r["Task"])
            r["Status"], r["Task"], r["Note"] = "cancelled", "", f"booking gone at {fmt(now())}; nothing sent"
            save_log(rows)
        runlog(f"send {event_id}: event gone/cancelled; nothing sent")
        return {"status": "cancelled", "event_id": event_id}

    if not CONSULT_RE.match(e.get("summary", "")):
        runlog(f"send {event_id}: title no longer a consultation: {e.get('summary')!r}")
        return {"status": "not-a-consultation", "summary": e.get("summary")}

    c = to_consult(e)
    prev = rows.get(c.ical_uid, {})
    t = now()

    if not c.email:
        upsert(rows, c, "failed", note="no student attendee on the event")
        save_log(rows)
        return {"status": "failed", "reason": "no attendee email"}

    if prev.get("Status") in {"sent", "sent-late", "sent-now"} and not force:
        runlog(f"send {event_id}: already {prev['Status']}; refusing to double-send")
        return {"status": "already-sent", "student": c.name}

    # Rescheduled since we registered? Compare to the logged start.
    logged_start = prev.get("Consultation (Toronto)")
    if logged_start and logged_start != fmt(c.start_dt):
        new_fire = c.fire_dt
        if new_fire > t + timedelta(minutes=1):
            unregister_task(prev.get("Task", ""))
            name = register_task(c, new_fire)
            upsert(rows, c, "scheduled", fires=fmt(new_fire), task=name, note=f"moved from {logged_start}; re-scheduled")
            save_log(rows)
            runlog(f"send {event_id}: moved {logged_start} -> {fmt(c.start_dt)}; re-registered {name}")
            return {"status": "moved", "student": c.name, "new_start": fmt(c.start_dt), "fires": fmt(new_fire)}
        # otherwise the new time is within 30 min (send now) or past (missed) - fall through

    if t >= c.start_dt:
        if not dry_run:
            upsert(rows, c, "missed", note=f"task ran at {fmt(t)}, after the start; nothing sent")
            unregister_task(prev.get("Task", ""))
            save_log(rows)
        runlog(f"send {event_id}: too late ({fmt(t)} >= {fmt(c.start_dt)}); nothing sent")
        return {"status": "missed", "student": c.name}

    late = t > c.fire_dt + timedelta(minutes=5)
    status = "sent-now" if mode == "now" else ("sent-late" if late else "sent")
    subject, body = compose(c)
    if dry_run:
        out = SKILL_DIR / "logs" / f"dryrun-{c.event_id}.txt"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(f"To: {c.email}\nSubject: {subject}\nWould-be status: {status}\nAt: {fmt(t)}\n\n{body}", encoding="utf-8")
        runlog(f"send {event_id}: DRY RUN ok -> {out.name}")
        return {"status": "dry-run", "student": c.name, "to": c.email, "subject": subject, "body": body, "file": str(out)}

    try:
        resp = send_email(c, dry_run=False)
    except Exception as ex:  # noqa: BLE001 - we want every failure in the log
        upsert(rows, c, "failed", task=prev.get("Task", ""), note=f"{type(ex).__name__}: {str(ex)[:160]}")
        save_log(rows)
        ledger(slug(c.name), f"pre-consult check-in (consult {fmt(c.start_dt)})", "failed", str(ex)[:120])
        runlog(f"send {event_id}: FAILED {ex}")
        return {"status": "failed", "student": c.name, "error": str(ex)}

    msg_id = resp.get("id") or resp.get("messageId") or resp.get("_raw", "")[:40]
    upsert(rows, c, status, fires=prev.get("Fires at", ""), task="", note=f"sent {fmt(t)} to {c.email}; msg {msg_id}")
    save_log(rows)
    ledger(slug(c.name), f"pre-consult check-in (consult {fmt(c.start_dt)})", f"sent {t:%Y-%m-%d}",
           f"auto-send at T-30 via pre-consultation-check-in; Msg {msg_id}")
    unregister_task(prev.get("Task", ""))
    runlog(f"send {event_id}: SENT to {c.email} msg={msg_id} status={status}")
    return {"status": status, "student": c.name, "to": c.email, "message_id": msg_id}


# --------------------------------------------------------------------------
# Commands
# --------------------------------------------------------------------------
def window(args) -> tuple[datetime, datetime]:
    t0 = now()
    if getattr(args, "until", None):
        d = datetime.strptime(args.until, "%Y-%m-%d").replace(tzinfo=TZ)
        return t0, d + timedelta(days=1)
    return t0, t0 + timedelta(days=args.days)


def coverage(c: Consult, rows: dict[str, dict]) -> str:
    r = rows.get(c.ical_uid)
    if not r:
        return "new"
    if r["Status"] in COVERED and r["Consultation (Toronto)"] == fmt(c.start_dt):
        return f"covered ({r['Status']})"
    if r["Status"] in COVERED:
        return f"moved (was {r['Consultation (Toronto)']})"
    if r["Status"] in OPTED_OUT:
        return "opted out"
    return f"retry ({r['Status']})"


def cmd_find(args) -> int:
    t0, t1 = window(args)
    found, flagged = list_consultations(t0, t1)
    rows = load_log()
    items = []
    for c in found:
        cov = coverage(c, rows)
        fire = c.fire_dt
        timing = "send now" if fire <= t0 < c.start_dt else ("past" if t0 >= c.start_dt else f"fires {fmt(fire)}")
        items.append({**asdict(c), "start_local": fmt(c.start_dt), "coverage": cov, "timing": timing})
    others = getattr(list_consultations, "last_others", [])
    result = {"window": [fmt(t0), fmt(t1)], "consultations": items, "flagged": flagged,
              "other_events_in_window": others}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Window {fmt(t0)} -> {fmt(t1)} (America/Toronto). {len(items)} consultation(s) "
              f"among {len(items) + len(flagged) + len(others)} events scanned.")
        if not items and others:
            print("  not consultations: " + ", ".join(sorted(set(others))))
        for i in items:
            print(f"  {i['start_local']}  {i['name']:<28} {i['email'] or '(no email)':<34} {i['coverage']:<22} {i['timing']}")
        for f in flagged:
            print(f"  FLAG {f['start']} {f['summary']!r}: {f['why']}")
    return 0


def cmd_schedule(args) -> int:
    t0, t1 = window(args)
    found, flagged = list_consultations(t0, t1, include_flagged=args.include_flagged)
    rows = load_log()
    only = {s.lower() for s in (args.only or [])}
    report = []
    for c in found:
        if only and not any(s in (c.name.lower(), c.ical_uid.lower(), c.event_id.lower(), (c.email or "").lower()) for s in only):
            continue
        cov = coverage(c, rows)
        prev = rows.get(c.ical_uid, {})
        what = f"pre-consult check-in (consult {fmt(c.start_dt)})"
        if cov.startswith("covered"):
            report.append({"student": c.name, "start": fmt(c.start_dt), "action": "skip", "why": cov}); continue
        if cov == "opted out" and not args.force:
            report.append({"student": c.name, "start": fmt(c.start_dt), "action": "skip", "why": "cancelled-by-joshua"}); continue
        if not c.email:
            upsert(rows, c, "failed", note="no student attendee on the event")
            report.append({"student": c.name, "start": fmt(c.start_dt), "action": "failed", "why": "no attendee email"}); continue
        if cov.startswith("moved"):
            unregister_task(prev.get("Task", ""))
        if t0 >= c.start_dt:
            report.append({"student": c.name, "start": fmt(c.start_dt), "action": "skip", "why": "already started"}); continue
        if c.fire_dt <= t0:
            if args.dry_run:
                report.append({"student": c.name, "start": fmt(c.start_dt), "action": "would send now", "to": c.email}); continue
            save_log(rows)
            res = do_send(c.event_id, mode="now")
            rows = load_log()
            report.append({"student": c.name, "start": fmt(c.start_dt), "action": "sent now", **{k: v for k, v in res.items() if k != "student"}})
            continue
        if args.dry_run:
            report.append({"student": c.name, "start": fmt(c.start_dt), "action": "would schedule", "fires": fmt(c.fire_dt), "to": c.email}); continue
        try:
            name = register_task(c, c.fire_dt)
        except Exception as ex:  # noqa: BLE001
            upsert(rows, c, "failed", note=f"task registration failed: {str(ex)[:160]}")
            report.append({"student": c.name, "start": fmt(c.start_dt), "action": "failed", "why": str(ex)[:200]}); continue
        note = f"moved from {prev['Consultation (Toronto)']}" if cov.startswith("moved") else ""
        upsert(rows, c, "scheduled", fires=fmt(c.fire_dt), task=name, note=note)
        ledger(slug(c.name), what, "scheduled", f"fires {fmt(c.fire_dt)} via Task Scheduler {TASK_PATH.rstrip(chr(92))}\\{name}; to {c.email}")
        report.append({"student": c.name, "start": fmt(c.start_dt), "action": "scheduled", "fires": fmt(c.fire_dt), "to": c.email, "task": name})
    if not args.dry_run:
        save_log(rows)
    # Reconcile: anything we scheduled inside this window that vanished from the calendar was cancelled.
    seen = {c.ical_uid for c in found}
    for uid, r in list(rows.items()):
        if r["Status"] != "scheduled" or uid in seen:
            continue
        try:
            st = datetime.strptime(r["Consultation (Toronto)"], "%Y-%m-%d %H:%M").replace(tzinfo=TZ)
        except ValueError:
            continue
        if t0 <= st <= t1 and not args.dry_run and get_event(r["Event ID"]) is None:
            unregister_task(r["Task"])
            r["Status"], r["Task"], r["Note"] = "cancelled", "", f"booking gone by {fmt(t0)}; task removed"
            report.append({"student": r["Student"], "start": r["Consultation (Toronto)"], "action": "cancelled", "why": "booking no longer on the calendar"})
    if not args.dry_run:
        save_log(rows)
    result = {"window": [fmt(t0), fmt(t1)], "dry_run": args.dry_run, "actions": report, "flagged": flagged}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Window {fmt(t0)} -> {fmt(t1)}{' (dry run)' if args.dry_run else ''}. {len(report)} action(s).")
        for a in report:
            extra = {k: v for k, v in a.items() if k not in ('student', 'start', 'action')}
            print(f"  {a['start']}  {a['student']:<28} {a['action']:<16} {json.dumps(extra) if extra else ''}")
        for f in flagged:
            print(f"  FLAG {f['start']} {f['summary']!r}: {f['why']}")
    return 0


def cmd_send(args) -> int:
    res = do_send(args.event_id, dry_run=args.dry_run, force=args.force)
    print(json.dumps(res, indent=2))
    return 0 if res.get("status") not in {"failed"} else 1


def cmd_status(args) -> int:
    rows = load_log()
    tasks = {t["name"]: t for t in list_tasks()}
    t0 = now()
    out = []
    for r in sorted(rows.values(), key=lambda r: r["Consultation (Toronto)"]):
        try:
            st = datetime.strptime(r["Consultation (Toronto)"], "%Y-%m-%d %H:%M").replace(tzinfo=TZ)
        except ValueError:
            continue
        if st < t0 - timedelta(days=args.past) :
            continue
        t = tasks.get(r["Task"]) if r["Task"] else None
        out.append({**r, "task_state": (t or {}).get("state", "absent" if r["Status"] == "scheduled" else ""),
                    "task_next": (t or {}).get("next", "")})
    orphans = [t for n, t in tasks.items() if not any(r["Task"] == n for r in rows.values())]
    if args.json:
        print(json.dumps({"rows": out, "orphan_tasks": orphans}, indent=2))
    else:
        for r in out:
            print(f"  {r['Consultation (Toronto)']}  {r['Student']:<28} {r['Status']:<14} fires {r['Fires at'] or '-':<17} task:{r['task_state'] or '-':<8} {r['Note']}")
        for t in orphans:
            print(f"  ORPHAN task {t['name']} state={t['state']} (no log row)")
    return 0


def cmd_cancel(args) -> int:
    rows = load_log()
    r = next((r for r in rows.values() if r["Event ID"] == args.event_id or r["iCalUID"] == args.event_id), None)
    if not r:
        print(json.dumps({"status": "not-found", "event_id": args.event_id})); return 1
    unregister_task(r["Task"])
    r["Status"], r["Task"], r["Note"] = "cancelled-by-joshua", "", f"cancelled {fmt(now())}: {args.reason or 'no reason given'}"
    save_log(rows)
    ledger(slug(r["Student"]), f"pre-consult check-in (consult {r['Consultation (Toronto)']})", "cancelled", args.reason or "Joshua cancelled the scheduled send")
    print(json.dumps({"status": "cancelled-by-joshua", "student": r["Student"]}, indent=2))
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    def add_window(sp):
        sp.add_argument("--days", type=float, default=5, help="window length from now (default 5)")
        sp.add_argument("--until", help="instead of --days: through the end of this date, YYYY-MM-DD (Toronto)")
        sp.add_argument("--json", action="store_true")

    sp = sub.add_parser("find", help="list consultations and their coverage"); add_window(sp); sp.set_defaults(fn=cmd_find)
    sp = sub.add_parser("schedule", help="register T-30 tasks"); add_window(sp)
    sp.add_argument("--dry-run", action="store_true", help="report what would happen, change nothing")
    sp.add_argument("--only", nargs="*", help="restrict to these names / emails / ids")
    sp.add_argument("--force", action="store_true", help="re-create even if Joshua cancelled it before")
    sp.add_argument("--include-flagged", action="store_true", help="also schedule title-matched events that are not Cal.com bookings (hand-made consultations)")
    sp.set_defaults(fn=cmd_schedule)
    sp = sub.add_parser("send", help="verify and send one check-in (what the task runs)")
    sp.add_argument("--event-id", required=True); sp.add_argument("--dry-run", action="store_true")
    sp.add_argument("--force", action="store_true", help="send even if the log says it already went")
    sp.set_defaults(fn=cmd_send)
    sp = sub.add_parser("status", help="scheduled / sent / failed, with Task Scheduler state")
    sp.add_argument("--past", type=int, default=7, help="include consultations up to N days back (default 7)")
    sp.add_argument("--json", action="store_true"); sp.set_defaults(fn=cmd_status)
    sp = sub.add_parser("cancel", help="remove a scheduled send and mark it opted out")
    sp.add_argument("--event-id", required=True, help="event id or iCalUID"); sp.add_argument("--reason", default="")
    sp.set_defaults(fn=cmd_cancel)

    args = p.parse_args(argv)
    try:
        return args.fn(args)
    except Exception:  # noqa: BLE001 - a scheduled task has no console; the log is the only witness
        runlog(f"{args.cmd} crashed:\n{traceback.format_exc()}")
        raise


if __name__ == "__main__":
    sys.exit(main())
