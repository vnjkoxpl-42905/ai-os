from pathlib import Path
import subprocess, json, time
root=Path(r'C:/Users/Joshu/dev/ai-os-projects/lsatu-and-or-20261019')
art=Path(r'C:/Users/Joshu/dev/ai-os/handoffs/and-or-20261019-standards-copyfix')
art.mkdir(exist_ok=True)
base='2348f76584ad642104fb3af1e8543765a6a9e185'
(art/'baseline-status.txt').write_bytes(subprocess.check_output(['git','status','--short','--untracked-files=all'],cwd=root))
(art/'baseline-diff.patch').write_bytes(subprocess.check_output(['git','diff',base],cwd=root))
prompt='Narrow follow-up prompted by a new defect found after fix1; extend bounded corrections only for this concrete issue. In AndOrLessons.tsx around line80, "A fact that reaches one member of a group on the left does not establish the group" is false for OR. Qualify precisely: "A fact that reaches only one member of an AND group on the left does not establish the group." Preserve the following regional-round explanation. Change only that sentence (and a focused assertion if needed); do not touch narration/media scripts since host synthesis is running. Host typecheck and all217 focused tests passed before this new wording correction. No shell/provider/publication/billing. Report exact change, no further work.'
(art/'prompt.txt').write_text(prompt,encoding='utf-8')
args=[r'C:/Users/Joshu/.local/bin/claude.exe','--resume','aab5c2f4-cfea-4a46-a59d-06f64320e88b','--add-dir','C:/Users/Joshu/dev/ai-os-projects/conditional-and-or-video-20261019','--print','--output-format','json','--permission-mode','acceptEdits','--tools','Read,Edit,Write,Glob,Grep','--strict-mcp-config','--mcp-config','{"mcpServers":{}}']
(art/'command.json').write_text(json.dumps(args),encoding='utf-8')
started=time.time()
with (art/'stdout.json').open('wb') as out,(art/'stderr.txt').open('wb') as err:
    p=subprocess.Popen(args,cwd=root,stdin=subprocess.PIPE,stdout=out,stderr=err)
    try:
        p.communicate(prompt.encode(),timeout=1200)
        status={'status':'completed' if p.returncode==0 else 'failed','exit_code':p.returncode}
    except subprocess.TimeoutExpired:
        subprocess.run(['taskkill','/PID',str(p.pid),'/T','/F'],capture_output=True)
        p.communicate()
        status={'status':'failed','error':'Recovery timed out'}
status.update(elapsed_seconds=time.time()-started,workflow='native Claude standards alignment; not runner resume',base=base)
(art/'host-status.json').write_text(json.dumps(status,indent=2),encoding='utf-8')
print(json.dumps(status))





