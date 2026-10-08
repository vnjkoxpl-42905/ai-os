"""Run the GitHub snapshot publisher and verified Google Drive mirror."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone

from drive_sync import atomic_json, mirror_from_state
from sync import process_lock
from uuid import uuid4

HISTORY_LIMIT = 200


def record_event(state, run_id, event, **details):
    """Keep bounded safe metadata under the existing runner lock.

    Status remains the latest completed attempt. History also records interrupted
    attempts; absence of a completed event is evidence, not a success receipt.
    """
    path = state / 'runner-history.json'
    history = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {'format': 1, 'events': []}
    history['events'].append({'run_id': run_id, 'event': event,
                             'utc': datetime.now(timezone.utc).isoformat(), **details})
    history['events'] = history['events'][-HISTORY_LIMIT:]
    atomic_json(path, history)


def run_once(config, state):
    run_id = uuid4().hex
    record_event(state, run_id, 'started')
    receipt = {'last_attempt': datetime.now(timezone.utc).isoformat(), 'run_id': run_id}
    try:
        result = subprocess.run([sys.executable, str(config.parent / 'sync.py'), '--once', '--config', str(config)],
                                capture_output=True, text=True,
                                creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
        receipt['github_exit_code'] = result.returncode
    except Exception as error:
        # Exception messages and child output may contain credentials.
        receipt['github_exit_code'] = 1
        receipt['github_error'] = type(error).__name__
    try:
        receipt['drive'] = mirror_from_state(config)
    except Exception as error:
        receipt['drive_error'] = type(error).__name__
    failed = bool(receipt['github_exit_code'] or 'drive_error' in receipt)
    busy = receipt.get('drive', {}).get('status') == 'busy'
    outcome = 'failed' if failed else 'deferred' if busy else 'succeeded'
    receipt['outcome'] = outcome
    receipt['completed_utc'] = datetime.now(timezone.utc).isoformat()
    atomic_json(state / 'runner-status.json', receipt)
    record_event(state, run_id, outcome, github_exit_code=receipt['github_exit_code'],
                 drive_error_type=receipt.get('drive_error'),
                 drive_results=[{key: item[key] for key in ('commit', 'status', 'updated_utc') if key in item}
                                for item in receipt.get('drive', {}).get('results', [])])
    return receipt, failed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', required=True)
    parser.add_argument('--once', action='store_true')
    args = parser.parse_args()
    config = Path(args.config).resolve()
    state = config.parent / 'state'
    state.mkdir(parents=True, exist_ok=True)
    with process_lock(state / 'runner.lock') as acquired:
        if not acquired:
            return
        receipt, failed = run_once(config, state)
        print(json.dumps(receipt, indent=2))
        if failed:
            raise SystemExit(1)


if __name__ == '__main__':
    main()
