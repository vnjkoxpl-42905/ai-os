from pathlib import Path
import subprocess, json, time
root=Path(r'C:/Users/Joshu/dev/ai-os-projects/lsatu-and-or-20261019')
art=Path(r'C:/Users/Joshu/dev/ai-os/handoffs/and-or-20261019-standards-durationfix')
art.mkdir(exist_ok=True)
base='2348f76584ad642104fb3af1e8543765a6a9e185'
(art/'baseline-status.txt').write_bytes(subprocess.check_output(['git','status','--short','--untracked-files=all'],cwd=root))
(art/'baseline-diff.patch').write_bytes(subprocess.check_output(['git','diff',base],cwd=root))
prompt='Actual host synthesis completed: film2.1 58.6s,2.2 58.4s,2.3 63.3s. Firsttwo fail required60-90sec. Narrow correction based actual measurement: add a useful short clarification to an EXISTING sentence in firsttwo films (aim+5sec). Keep exact app and script.json equality, same sentence/scene counts so timingindexes remainvalid. No padding silence/speedchanges/newexamples. Film2.1 can clarify unknown vs denied; film2.2 whole-side forward vs backward. Do not touch film2.3. Also HyperFrames firstfilm checkpassed0errors but3contrastwarnings2.85:1need3 at t16.282,42.334 (elementsandscene child5,orscene child6/10); inspect text colors/sharedCSS and make labelsmeetcontrast genuinely, no suppressing checks. Info overlaps may be intended coloredcardbackground+text: inspect before changing; do not mark unreadable text acceptable. Host will regenerate cachedaudio/check/render. No shell/providercalls/publication. Report exact edits. Preserve framefix and priorcopyfix. This measured failure justifies narrow additionalcorrection, no scopeexpansion.'
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





