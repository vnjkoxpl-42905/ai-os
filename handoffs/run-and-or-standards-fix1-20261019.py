from pathlib import Path
import subprocess, json, time
root=Path(r'C:/Users/Joshu/dev/ai-os-projects/lsatu-and-or-20261019')
art=Path(r'C:/Users/Joshu/dev/ai-os/handoffs/and-or-20261019-standards-fix1')
art.mkdir(exist_ok=True)
base='2348f76584ad642104fb3af1e8543765a6a9e185'
(art/'baseline-status.txt').write_bytes(subprocess.check_output(['git','status','--short','--untracked-files=all'],cwd=root))
(art/'baseline-diff.patch').write_bytes(subprocess.check_output(['git','diff',base],cwd=root))
prompt='Continue the authorized standards alignment. Fix only these reviewed gaps, preserve unrelated work and all prior safeguards. No shell/provider/billing/publication actions.\n1. AndOrLessons 2.2 Right card: "Use the rule only when the whole left side is established" wrongly excludes contraposition. Restrict this instruction to FORWARD inference.\n2. Replace "may give you nothing under this rule" with the exact limit: project alone gives no additional conclusion about regional-round qualification.\n3. AndOrVisuals assigns amber left / teal right, recoloring original ideas when flipped. Match approved ContrapositiveVisuals idea-bound tones; color travels with the original idea through negation and switching; retain current side-role labels.\n4. Film 2.3 introduces a third tablet example beyond float/pool. Reuse float with OR explicitly marked a different rule, or existing pool, to explain OR failure. Update app narration, script.json and scene visuals together.\n5. 2.2 error cards: show the actual full OR rule for the regional-round/laptop card rather than leaving only project/inspection context.\n6. Host typecheck: AndOrLessonStandard.test.tsx47 fireEvent.toggle does not exist. Dispatch a real toggle Event with supported fireEvent API. Test transcript within its actual fallback container rather than asserting the film first sentence appears nowhere on the whole page (it also appears legitimately in lesson 2.3). Keep assertions meaningful.\nRead the .impeccable conditional surface briefs and approved contrapositive CSS plus local HyperFrames skill instructions as relevant; previous report explicitly said those were skipped. Do not replace the scoped approved palette.\nHost results: 213 tests passed, 2 new standard tests failed for above test issues. Typecheck failed only unsupported toggle. Native previous build completed successfully with no permission denials. Host owns synthesis/render/test/browser after your fixes. Keep pipeline reproducible with pinned 0.8.149 and local cached af_heart voice. Do not add paid calls. Report concrete files and commands, no claims tests/render ran.\n'
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





