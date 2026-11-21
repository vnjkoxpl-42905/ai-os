from pathlib import Path
import subprocess, json, time
root=Path(r'C:/Users/Joshu/dev/ai-os-projects/lsatu-and-or-20261019')
art=Path(r'C:/Users/Joshu/dev/ai-os/handoffs/and-or-20261019-standards-fix2')
art.mkdir(exist_ok=True)
base='2348f76584ad642104fb3af1e8543765a6a9e185'
(art/'baseline-status.txt').write_bytes(subprocess.check_output(['git','status','--short','--untracked-files=all'],cwd=root))
(art/'baseline-diff.patch').write_bytes(subprocess.check_output(['git','diff',base],cwd=root))
prompt='Final bounded media correction before host runs synthesis/render. Independent media reviewer found:\n1. prepare.py check_against_app only checks sentence membership globally and silently passes missing source. Require exact perlesson slug/title/scenes ordered sentence equality, with no missing/extra/reordered sentences; missing app source must fail. Use robust extraction (or explicit exported JSON source) rather than global substring membership. Host must be able to prove wronglesson/reordered/extra/missing source fails without editing real source.\n2. whole-group-negation.scenes.js double scene starts Pool open -> (Lifeguard OR NOT crowded), then strikes lifeguard/cancels crowded and adds NOT to Pool open WITHOUT FLIPPING SIDES. Final screen depicts inverse NOT open -> (NOT lifeguard AND crowded). Fix to final (NOT lifeguard AND crowded) -> NOT open, actual negation plus switch. Preserve idea colors and match narration. Review other two films for analogous direction/color errors.\nPreserve fix1 and all earlier safeguards. No shell/provider/billing/publication actions; host runs commands. You are not alone; do not revert unrelated edits. Report final concrete edits and commands. Scope app narration and new separate media project as already authorized. No new features or unrelated rewrites. This is fix round2, focus narrowly.\n'
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





