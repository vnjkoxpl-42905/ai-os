from pathlib import Path
import subprocess, json, time
root=Path(r'C:/Users/Joshu/dev/ai-os-projects/lsatu-and-or-20261019')
art=Path(r'C:/Users/Joshu/dev/ai-os/handoffs/and-or-20261019-standards-framefix')
art.mkdir(exist_ok=True)
base='2348f76584ad642104fb3af1e8543765a6a9e185'
(art/'baseline-status.txt').write_bytes(subprocess.check_output(['git','status','--short','--untracked-files=all'],cwd=root))
(art/'baseline-diff.patch').write_bytes(subprocess.check_output(['git','diff',base],cwd=root))
prompt='Independent follow-up found a remaining misleading frame in group-placement.scenes.js. Narrow fix before rendering; no new narration or script JSON changes (host synthesis active). In 2.2 right scene, the no-safety-form inference adds a back arrow but leaves forward arrow/must and full AND group after negating selected chips. Final frame still shows invalid NOT in round -> (NOT safetyform AND coach). Fade original forward arrow, must, unused coach/AND and role tags during that backward inference, with clear direction and idea-bound colors; or show separate valid contrapositive row. Also left firstscene strikes inspection for project-alone narration: unknown inspection is NOT denied. Visually label/fade it as unknown rather than striking it false. Preserve all source/earlier fixes. Do not touch app or narration. File tools only; no tests/render/provider/publication. This extra narrow round is justified by new independently found teaching defects, not scope expansion. Report exact edits.'
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





