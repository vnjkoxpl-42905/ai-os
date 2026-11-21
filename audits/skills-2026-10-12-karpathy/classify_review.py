"""Split review-class drift: provider-swap corruption only, updater-owned packs, and the rest."""
import json, re
from pathlib import Path
HERE = Path(__file__).parent
V = HERE.parents[1]
HOME = Path.home()
ROOT = {'home-claude': (HOME/'.claude/skills','claude'), 'home-agents': (HOME/'.agents/skills','codex'), 'home-codex': (HOME/'.codex/skills','codex')}
CONTRACT = re.compile(r'^## (Local|Current AI OS) execution contract')
STALE = re.compile(r'~/ai-os\b|~/\.Codex|/Users/joshuaf|/mnt/d/|projects/lsatu/|archive/wiki-pre-rebuild')
UPDATER = set('ask-matt decision-mapping edit-article handoff claude-handoff implement implement-spec improve-codebase-architecture loop-me qa request-refactor-plan resolving-merge-conflicts retro review scaffold-exercises setup-pre-commit setup-ts-deep-modules tdd teach to-prd to-questionnaire wayfinder writing-beats writing-great-skills codebase-design design-an-interface prototype brainstorming executing-plans finishing-a-development-branch requesting-code-review systematic-debugging test-driven-development using-git-worktrees using-superpowers writing-plans writing-skills'.split())
def lines(t, swap=False):
    out, skip = [], False
    for ln in t.replace('\r\n','\n').split('\n'):
        if CONTRACT.match(ln): skip=True; continue
        if skip and ln.startswith(('## ','# ')): skip=False
        s = re.sub(r'\s+',' ',ln.strip())
        if swap: s = s.replace('Codex Code','Claude Code').replace('Codex','Claude').replace('.Codex','.claude')
        if skip or not s or s=='## Workflow' or s.startswith('description:'): continue
        out.append(s)
    return out
d = json.load(open(HERE/'drift-classes.json', encoding='utf-8'))
res = {'corruption-only': [], 'updater-owned': [], 'decide': []}
for r in d['review']:
    root, rt = ROOT[r['install']]
    a = (root/r['skill']/'SKILL.md').read_text(encoding='utf-8', errors='replace')
    b = (V/'skills'/rt/r['skill']/'SKILL.md').read_text(encoding='utf-8', errors='replace')
    cat = set(lines(b, True))
    left = [l for l in lines(a, True) if l not in cat and not STALE.search(l)]
    key = 'updater-owned' if r['skill'] in UPDATER else ('corruption-only' if not left else 'decide')
    res[key].append({**r, 'left': len(left), 'left_sample': left[:3]})
json.dump(res, open(HERE/'review-classes.json','w',encoding='utf-8'), indent=1)
for k,v in res.items(): print(k, len(v), ' '.join(sorted({x['skill'] for x in v})))
