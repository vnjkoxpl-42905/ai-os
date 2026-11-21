import json
import os
from pathlib import Path

path = Path.home() / '.claude' / 'settings.json'
original = path.read_bytes()
text = original.decode('utf-8')
needle = '''      {
        "matcher": "Bash|PowerShell|Monitor",
        "hooks": [
          {
            "type": "command",
            "command": "& 'C:\\\\Users\\\\Joshu\\\\dev\\\\ai-os\\\\research\\\\2026-10-29-guard\\\\release\\\\dcg.exe'",
            "shell": "powershell"
          }
        ]
      },
'''
if text.count(needle) != 1:
    raise SystemExit('Expected exact probe hook once; no change made')
changed = text.replace(needle, '', 1)
before, after = json.loads(text), json.loads(changed)
before['hooks']['PreToolUse'].pop(0)
if before != after or path.read_bytes() != original:
    raise SystemExit('Configuration changed concurrently or unexpected difference; no change made')
tmp = path.with_name('settings.dcg-probe-undo.tmp')
tmp.write_bytes(changed.encode('utf-8'))
os.replace(tmp, path)
print('Removed only probe-added DCG hook; all other parsed settings preserved')
