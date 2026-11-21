from pathlib import Path
import hashlib
ROOT=Path(__file__).resolve().parents[2]
def append(path, marker, block):
    original=path.read_bytes(); text=original.decode('utf-8-sig')
    if marker in text: return
    if path.read_bytes()!=original: raise RuntimeError('Concurrent edit: '+str(path))
    path.write_bytes(original+('\n\n'+block+'\n').encode('utf-8'))

for name in ['AGENTS.md','CLAUDE.md']:
    append(ROOT/name,'<!-- DESIGN DOMAIN ROUTER -->','<!-- DESIGN DOMAIN ROUTER -->\nDesign knowledge, skills, repositories, references and new design clips: start at `design/README.md`. Keep using `second-brain-ingest`; its design route maintains that hub for both runtimes.\n<!-- END DESIGN DOMAIN ROUTER -->')
for name in ['skills/codex/second-brain-ingest/SKILL.md','skills/claude/second-brain-ingest/SKILL.md']:
    append(ROOT/name,'## Design clips use the shared design hub','## Design clips use the shared design hub\n\nFor design, UI/UX, typography, colour, components, motion, design skills or design repository sources, read `design/README.md` from the resolved vault root. Preserve the normal inbox, source archive and canonical summary homes; connect the source and useful synthesis through this hub. Do not duplicate an existing subject or move executable skill/repository trees into the hub. Cross-domain sources also link their owning domain. Route actionable suggestions through the existing queues. After a changed design ingest, run `py system/scripts/design-catalog.py`, then refresh and verify the wiki index. Clip capture alone does not trigger automatic processing.')
for name in ['skills/codex/design-resource-library/SKILL.md','skills/claude/design-resource-library/SKILL.md']:
    append(ROOT/name,'## Shared design knowledge home','## Shared design knowledge home\n\nStart at `design/README.md` in the resolved ai-os vault for clipped sources, methods, current prototype pointers and the generated skill/repository/research catalogue. This complements the resource map; do not start a parallel library or assume dated tool status is current.')
append(ROOT/'wiki/index.md','<!-- DESIGN HUB NAVIGATION -->','<!-- DESIGN HUB NAVIGATION -->\n[Design hub](../design/README.md): shared Claude Code/Codex router for design clips, methods, skills, component repositories, research and visual work.\n<!-- END DESIGN HUB NAVIGATION -->')
append(ROOT/'references/ai-workspace/index.md','## Shared design domain','## Shared design domain\n\n[Design hub](../../design/README.md) is the dedicated design entry point for Claude Code and Codex. Design clips still use the single intake/archive/source-summary pipeline; the hub connects skills, repositories, tips, methods and research. Existing AI references and queues remain authoritative at their current paths.')
append(ROOT/'references/website-design-planning.md','## Shared design library','## Shared design library\n\n[Start at the design hub](../design/README.md) for related sources, installed skills, component repositories and current research. This page remains the owning website-planning method; the hub is navigation rather than a duplicate version.')
print('Routing added using compare-before-write; existing content preserved.')
