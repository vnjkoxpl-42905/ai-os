"""Resume the explicitly approved ten-payload cleanup after live fresh-backup proof.

Nothing runs on import. Launch only after the human approval recorded by the owner.
"""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import sys
import time

import new_machine_discard_failed_history as discard

CONFIRMED_SHA = 'b0b0908f68c950c4d17e03d8048047de103a40907ab7b8363a7fcc65b39ad9c5'
CORE = '20261024-211629'
CORE_BASE = '20261023-174504'
PERSONAL = '20261024-213612'
EXPECTED_PROCESSES = {14252: CORE, 27808: '20261014-200506'}
HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent.parent
PLAN = PROJECT / 'research/2026-10-24/backup-failed-history-discard-bound-plan.json'
STATE = discard.STAGE / 'APPROVED-TEN-HISTORY-CLEANUP.json'
LOG = discard.STAGE / 'APPROVED-TEN-HISTORY-CLEANUP.log'


def process_inventory():
    command = ("Get-CimInstance Win32_Process | Where-Object { $_.ProcessId -in @(14252,27808) } | "
               "ForEach-Object { [pscustomobject]@{ pid=$_.ProcessId; name=$_.Name; command=$_.CommandLine; "
               "created=$_.CreationDate.ToUniversalTime().ToString('o') } } | ConvertTo-Json -Compress")
    result = subprocess.run(['powershell.exe', '-NoProfile', '-Command', command],
                            capture_output=True, text=True, check=True, timeout=30,
                            creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))
    rows = json.loads(result.stdout) if result.stdout.strip() else []
    if isinstance(rows, dict):
        rows = [rows]
    return {int(row['pid']): row for row in rows}


def bind_processes(inventory):
    result = {}
    for pid, generation in EXPECTED_PROCESSES.items():
        actual = inventory.get(pid)
        if actual is None:
            result[str(pid)] = {'finished_before_worker': True, 'generation': generation}
            continue
        command = actual.get('command') or ''
        if (actual.get('name', '').lower() not in {'python.exe', 'pythonw.exe'}
                or 'new-machine-cloud.py' not in command or generation not in command):
            raise ValueError('Expected uploader PID identity differs: ' + str(pid))
        result[str(pid)] = {'generation': generation, 'created': actual['created']}
    return result


def still_running(bound, inventory):
    active = []
    for text_pid, identity in bound.items():
        if identity.get('finished_before_worker'):
            continue
        actual = inventory.get(int(text_pid))
        if actual is None or actual.get('created') != identity['created']:
            continue  # Original process ended; a reused PID is not the same uploader.
        command = actual.get('command') or ''
        if ('new-machine-cloud.py' not in command or identity['generation'] not in command
                or actual.get('name', '').lower() not in {'python.exe', 'pythonw.exe'}):
            raise ValueError('Bound uploader command identity changed')
        active.append(int(text_pid))
    return active


def append_event(stream, event, **fields):
    record = {'utc': datetime.now(timezone.utc).isoformat(), 'event': event, **fields}
    stream.write(json.dumps(record) + '\n')
    stream.flush()
    print(json.dumps(record), flush=True)


def transient_log_failure(text):
    return '"retryable": true' in text or '"retryable":true' in text


def require_bound_restore_sample(directory):
    """Require the offloader's actual cloud download, bound to current metadata."""
    from new_machine_offload import METADATA
    evidence = discard.read_json(directory / 'OFFLOADED.json')
    manifest = discard.read_json(directory / 'manifest.json')
    parts = discard.read_json(directory / 'parts-manifest.json')
    receipt = discard.read_json(directory / 'CLOUD-VERIFIED.json')
    first = parts['parts'][0]
    remote = next((record for record in receipt['files'] if record.get('name') == first['name']), {})
    expected_sample = {'cloud_id': remote.get('id'), 'sha256': first['sha256'],
                       'md5': first['md5'], 'bytes': first['bytes'], 'verified': True}
    metadata = {name: discard.file_sha256(directory / name) for name in METADATA}
    if (evidence.get('status') != 'evicted' or evidence.get('generation') != directory.name
            or evidence.get('archive_sha256') != manifest['archive_sha256']
            or evidence.get('archive_bytes') != sum(part['bytes'] for part in parts['parts'])
            or evidence.get('metadata_sha256') != metadata
            or not remote.get('id') or evidence.get('restore_sample') != expected_sample):
        raise ValueError('Fresh core lacks bound downloaded restore-sample proof')
    return expected_sample


def run_child(command, stream):
    stream.flush()
    start = LOG.stat().st_size
    result = subprocess.run(command, stdout=stream, stderr=subprocess.STDOUT,
                            timeout=24 * 60 * 60,
                            creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))
    stream.flush()
    if result.returncode:
        with LOG.open('rb') as source:
            source.seek(max(start, LOG.stat().st_size - 128 * 1024))
            tail = source.read().decode('utf-8', errors='replace')
        return False, transient_log_failure(tail)
    return True, False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--approved-plan-sha', required=True)
    parser.add_argument('--max-wait-hours', type=float, default=24)
    args = parser.parse_args()
    if args.approved_plan_sha != CONFIRMED_SHA or not 0 < args.max_wait_hours <= 72:
        raise ValueError('Exact approved plan SHA and bounded wait required')
    discard.checked_plan(PLAN, CONFIRMED_SHA)
    cloud = discard.load_cloud_module()
    runtime = json.loads((HERE / 'new-machine-runtime.json').read_text(encoding='utf-8-sig'))
    os.environ['GWS_EXECUTABLE'] = runtime['gws']
    python = runtime.get('python', sys.executable)
    previous = STATE.read_bytes() if STATE.exists() else None
    state = json.loads(previous) if previous else {}
    if state and state.get('plan_sha256') != CONFIRMED_SHA:
        raise ValueError('Existing worker state belongs to another plan')
    if state.get('status') == 'complete':
        print('Approved cleanup already completed; inspect ' + str(STATE))
        return
    if not state.get('bound_uploaders'):
        state['bound_uploaders'] = bind_processes(process_inventory())
    state['plan_sha256'] = CONFIRMED_SHA
    state.setdefault('offload_results', {})
    def save(status, **fields):
        nonlocal previous
        state.update(status=status, updated=datetime.now(timezone.utc).isoformat(), **fields)
        previous = discard.atomic_audit(STATE, state, previous)
    deadline = time.monotonic() + args.max_wait_hours * 3600
    with LOG.open('a', encoding='utf-8', buffering=1) as stream:
        save('waiting-original-uploaders')
        append_event(stream, 'waiting-original-uploaders', pids=list(EXPECTED_PROCESSES))
        while still_running(state['bound_uploaders'], process_inventory()):
            if time.monotonic() > deadline:
                save('blocked', reason='original uploader wait deadline exceeded')
                raise RuntimeError('Uploader wait deadline exceeded')
            time.sleep(15)
        append_event(stream, 'original-uploaders-finished')
        # If the original fresh uploader failed, only its exact generation is retried.
        core_dir = discard.STAGE / CORE
        if not (core_dir / 'CLOUD-VERIFIED.json').exists():
            save('retrying-fresh-core')
            for attempt in range(3):
                append_event(stream, 'fresh-core-retry', attempt=attempt + 1)
                success, transient = run_child([python, str(HERE / 'new-machine-cloud.py'), '--generation', str(core_dir)], stream)
                if success:
                    break
                if not transient or attempt == 2:
                    save('blocked', reason='fresh core upload failed', attempts=attempt + 1)
                    raise RuntimeError('Fresh core upload failed; no cleanup')
                time.sleep((2, 8)[attempt])
        save('verifying-cloud', generation=CORE)
        append_event(stream, 'verifying-cloud', generation=CORE)
        cloud.verify_generation_cloud(core_dir, cloud.make_gws(core_dir))
        # Prove an actual fresh-core cloud download before discarding any history.
        from new_machine_offload import offload_generation
        save('offloading-fresh-core-before-discard', generation=CORE)
        append_event(stream, 'offloading-fresh-core-before-discard', generation=CORE)
        core_offload = offload_generation(discard.STAGE, core_dir, apply=True)
        sample = require_bound_restore_sample(core_dir)
        state['offload_results'][CORE] = {'success': True, 'result': core_offload,
                                         'downloaded_restore_sample': sample}
        save('fresh-core-download-proven', generation=CORE)
        save('waiting-cleanup-locks')
        def progress(phase, **fields):
            save(phase, phase_details=fields)
            append_event(stream, phase, **fields)
        while not state.get('discard_result'):
            try:
                result = discard.run(PLAN, apply=True, confirmed_plan_sha=CONFIRMED_SHA, progress=progress)
            except OSError as error:
                if getattr(error, 'winerror', None) not in (32, 33, 36) and error.errno not in (13, 11):
                    raise
                if time.monotonic() > deadline:
                    save('blocked', reason='backup or target lock remained busy')
                    raise
                time.sleep(15)
                continue
            save('discard-complete', discard_result=result)
        # Only the original reviewed targets plus three named fresh-chain captures.
        exact_offloads = sorted(discard.TARGET_GENERATIONS | {CORE, CORE_BASE, PERSONAL})
        for generation in exact_offloads:
            if state['offload_results'].get(generation, {}).get('success'):
                continue
            directory = discard.STAGE / generation
            if not (directory / 'CLOUD-VERIFIED.json').exists():
                state['offload_results'][generation] = {'skipped': 'no cloud receipt'}
                save('offloading-exact-preserved-targets')
                continue
            try:
                save('offloading', generation=generation)
                append_event(stream, 'offloading', generation=generation)
                result = offload_generation(discard.STAGE, directory, apply=True)
                state['offload_results'][generation] = {'success': True, 'result': result}
                append_event(stream, 'preserved-target-offloaded', generation=generation, bytes=result['bytes'])
            except Exception as error:
                state['offload_results'][generation] = {'success': False, 'error_type': type(error).__name__}
                append_event(stream, 'preserved-target-offload-blocked', generation=generation, error_type=type(error).__name__)
            save('offloading-exact-preserved-targets')
        failed = [name for name, result in state['offload_results'].items() if result.get('success') is False]
        save('blocked' if failed else 'complete', remaining_offload_failures=failed)
        append_event(stream, state['status'], state_path=str(STATE))


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        # Preserve the last completed phase and fail closed; never continue to cleanup.
        if STATE.exists():
            previous = STATE.read_bytes()
            value = json.loads(previous)
            if value.get('plan_sha256') == CONFIRMED_SHA:
                value.update(last_phase=value.get('status'), status='blocked',
                             error_type=type(error).__name__,
                             updated=datetime.now(timezone.utc).isoformat())
                discard.atomic_audit(STATE, value, previous)
        raise
