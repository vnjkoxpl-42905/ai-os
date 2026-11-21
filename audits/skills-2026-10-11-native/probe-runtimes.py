"""Fresh native CLI probes whose prompts prohibit writes and external actions.

Claude built-ins are restricted to read/search/skill loading; configured MCP
tools can still be exposed. Codex matches this
chat's authorized profile; its read-only boundary is task instructions, not a
tool-level sandbox. These probes verify loading, not production workflows.
"""
from pathlib import Path
import argparse
import json
import shutil
import subprocess
import time

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('runtime',choices=['codex','claude'])
parser.add_argument('case')
parser.add_argument('prompt_file')
args=parser.parse_args()
prompt=Path(args.prompt_file).read_text(encoding='utf-8')
if args.runtime=='codex':
    # Use the node launcher directly; PowerShell shims cannot be subprocess executables.
    launcher=Path.home()/'AppData/Roaming/npm/node_modules/@openai/codex/bin/codex.js'
    # Match this chat's authorized runtime profile. Windows read-only helper
    # refresh conflicts with the desktop's active node_repl executable lock.
    # The probe prompt itself limits this run to read-only inspection.
    cmd=[shutil.which('node'),str(launcher),'exec','--json','--color','never','-s','danger-full-access','-C',str(ROOT),'-']
else:
    cmd=[shutil.which('claude'),'--print','--output-format','stream-json','--verbose',
         '--permission-mode','dontAsk','--tools','Read,Glob,Grep,Skill',
         '--allowedTools','Read,Glob,Grep,Skill']
start=time.time()
result=subprocess.run(cmd,input=prompt,cwd=ROOT,
                      capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=300)
prefix=OUT/(args.runtime+'-'+args.case)
prefix.with_suffix('.jsonl').write_text(result.stdout,encoding='utf-8')
prefix.with_suffix('.stderr.txt').write_text(result.stderr,encoding='utf-8')
receipt=dict(runtime=args.runtime,case=args.case,exit_code=result.returncode,seconds=round(time.time()-start,2),
             stdout_file=str(prefix.with_suffix('.jsonl')),stderr_file=str(prefix.with_suffix('.stderr.txt')))
prefix.with_suffix('.receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt))
for line in result.stdout.splitlines():
    try:
        event=json.loads(line)
    except ValueError:
        continue
    if event.get('type') in ('result','error'):
        print(json.dumps({k:v for k,v in event.items() if k in ('type','subtype','result','is_error','errors')}))
    if event.get('type')=='item.completed' and event.get('item',{}).get('type')=='agent_message':
        print(event['item'].get('text','')[:5000])
raise SystemExit(result.returncode)
