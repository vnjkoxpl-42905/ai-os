from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
HUB=ROOT/'design/README.md'
marker='<!-- SHARED DESIGN BRAIN -->'
block=f'\n\n{marker}\nFor design, UI/UX, visual principles, components, typography, colour, motion or design research, first read `{HUB.as_posix()}`. This shared Claude Code/Codex hub routes to existing skills, repositories, preserved sources and project evidence. Follow the current project/user brief and use only relevant links; do not load the entire library or relocate executable repositories.\n<!-- END SHARED DESIGN BRAIN -->\n'
receipts=[]
for p in [Path.home()/'.claude/CLAUDE.md',Path.home()/'.codex/AGENTS.md',Path.home()/'AGENTS.md']:
 if not p.is_file(): continue
 old=p.read_bytes()
 if marker in old.decode('utf-8-sig'):continue
 backup=ROOT/'research/2026-10-24-design-completeness/before'/p.parent.name/(p.name+'.snapshot')
 backup.parent.mkdir(parents=True,exist_ok=True)
 if not backup.exists():backup.write_bytes(old)
 if p.read_bytes()!=old:raise RuntimeError('Concurrent edit '+str(p))
 p.write_bytes(old+block.encode('utf-8'))
 receipts.append({'path':str(p),'before':hashlib.sha256(old).hexdigest(),'after':hashlib.sha256(p.read_bytes()).hexdigest()})
(ROOT/'research/2026-10-24-design-completeness/global-routing.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
print(f'Added design routing to {len(receipts)} existing global/ancestor instruction files.')
