"""Targeted synthetic failure verification; preserves all test artifacts."""
import json, os, runpy, sys, time
from pathlib import Path
stage=Path.home()/'LaptopBackups'/('walk-error-test-'+str(time.time_ns()))
def denied_walk(root, followlinks=False, onerror=None):
    if onerror: onerror(PermissionError(13,'synthetic denied directory',str(root)))
    return iter(())
original=os.walk
os.walk=denied_walk
sys.argv=['new-machine-backup.py','--stage',str(stage),'--scope','core']
code=0
try:
    runpy.run_path(str(Path(__file__).with_name('new-machine-backup.py')),run_name='__main__')
except SystemExit as error: code=error.code
finally: os.walk=original
manifest=json.loads(next(stage.glob('*/manifest.json')).read_text())
assert code==1 and not manifest['complete'] and manifest['errors']
print('PASS: unreadable-directory error prevents a complete manifest')
