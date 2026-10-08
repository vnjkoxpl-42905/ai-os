"""Run the GitHub snapshot publisher and verified Google Drive mirror."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone

from drive_sync import mirror_from_state
from sync import process_lock


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
        result = subprocess.run([sys.executable, str(config.parent / 'sync.py'), '--once', '--config', str(config)],
                                capture_output=True, text=True,
                                creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
        receipt = {'last_attempt': datetime.now(timezone.utc).isoformat(), 'github_exit_code': result.returncode}
        try:
            receipt['drive'] = mirror_from_state(config)
        except Exception as error:
            receipt['drive_error'] = str(error)
        (state / 'runner-status.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
        print(json.dumps(receipt, indent=2))
        if result.returncode or 'drive_error' in receipt:
            raise SystemExit(1)


if __name__ == '__main__':
    main()
