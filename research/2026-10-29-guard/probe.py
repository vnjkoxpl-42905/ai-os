import json
import subprocess
from pathlib import Path

binary = Path(__file__).parent / 'release' / 'dcg.exe'
cases = [
    ('claude-safe', {'session_id':'probe','hook_event_name':'PreToolUse','tool_name':'Bash','tool_input':{'command':'git status --short'}}),
    ('claude-reset', {'session_id':'probe','hook_event_name':'PreToolUse','tool_name':'Bash','tool_input':{'command':'git reset --hard HEAD~1'}}),
    ('claude-powershell', {'session_id':'probe','hook_event_name':'PreToolUse','tool_name':'PowerShell','tool_input':{'command':'Remove-Item -LiteralPath C:\\test -Recurse -Force'}}),
    ('codex-safe', {'session_id':'probe','turn_id':'turn-1','hook_event_name':'PreToolUse','tool_name':'Bash','tool_input':{'command':'git status --short'},'tool_use_id':'call-1'}),
    ('codex-reset', {'session_id':'probe','turn_id':'turn-1','hook_event_name':'PreToolUse','tool_name':'Bash','tool_input':{'command':'git reset --hard HEAD~1'},'tool_use_id':'call-1'}),
    ('codex-powershell', {'session_id':'probe','turn_id':'turn-1','hook_event_name':'PreToolUse','tool_name':'Bash','tool_input':{'command':'Remove-Item -LiteralPath C:\\test -Recurse -Force'},'tool_use_id':'call-1'}),
]
for name, data in cases:
    result = subprocess.run([str(binary)], input=json.dumps(data), text=True, capture_output=True, timeout=15)
    print(json.dumps({'case':name, 'exit':result.returncode, 'stdout':result.stdout, 'stderr':result.stderr}, ensure_ascii=False))
