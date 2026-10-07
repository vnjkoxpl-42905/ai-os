"""Read-only scope counts; no content reads or credential output."""
import ast, json, os
from pathlib import Path
tree=ast.parse(Path(__file__).with_name('new-machine-backup.py').read_text())
excluded=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign)
    and any(isinstance(t,ast.Name) and t.id=='excluded' for t in n.targets))
roots=['dev/ai-os','dev/ai-os-projects','.codex','.claude','.agents','.config',
    'AppData/Local/com.superwhisper.app','AppData/Roaming/Codex','AppData/Roaming/obsidian',
    'AppData/Roaming/Code/User','AppData/Roaming/gh','AppData/Roaming/gws']
counts={}; totalbytes=0; errors=[]
for rel in roots:
    count=0
    root=Path.home()/rel
    if not root.exists(): counts[rel]=0; continue
    walkroot=Path('\\\\?\\'+str(root.resolve())) if os.name=='nt' else root
    for parent,dirs,files in os.walk(walkroot,onerror=lambda e:errors.append(str(e))):
        base=Path(parent)
        dirs[:]=[d for d in dirs if d not in excluded and not (base/d).is_symlink() and not (base/d).is_junction()]
        for name in files:
            if name.endswith(('-wal','-shm','.lock','.tmp')): continue
            if rel=='.codex' and name.startswith('logs_'): continue
            count+=1
            try: totalbytes+=(base/name).stat().st_size
            except OSError as error:errors.append(str(error))
    counts[rel]=count
print(json.dumps({'counts':counts,'total_files':sum(counts.values()),'source_bytes':totalbytes,'traversal_errors':errors}))
