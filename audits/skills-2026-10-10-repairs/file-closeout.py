"""File authorized system repair outcome without changing task statuses."""
from pathlib import Path
import os
import tempfile

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).parent

def save(p, before, after):
    backup=OUT/'backups/closeout'/p.relative_to(ROOT)
    backup.parent.mkdir(parents=True,exist_ok=True)
    backup.write_bytes(before)
    with tempfile.NamedTemporaryFile(dir=p.parent,prefix='.closeout-',delete=False) as f:
        f.write(after.encode('utf-8'))
        stage=Path(f.name)
    try:
        if p.read_bytes()!=before:
            raise RuntimeError('Concurrent edit: '+str(p))
        os.replace(stage,p)
    finally:
        if stage.exists():
            stage.unlink()

p=ROOT/'skills/PARITY.md'
before=p.read_bytes()
text=before.decode('utf-8')
title='## 2026-10-10: reviewed skill adaptations and preserved compatibility'
if title not in text:
    text+='\n\n'+title+'\n\n'
    text+='The full-catalog repair preserves provider identities and runtime-specific host calls. Current Codex `codex-build` and `codex-review` activations are explicit compatibility wrappers to `claude-build` and `claude-review`; their inert Codex catalog copies preserve this route. Current primary triggers remain the provider named by the caller. No additional global activations were created.\n\n'
    text+='Existing catalog/activation drift was reconciled, including Gemini copies. Three previously uncatalogued Gemini browser-operation skills remain Gemini-only; they are not automatically ported or activated for Claude/Codex. The validator skips inactive/snapshot/fork container directories and checks Gemini entrypoints against their owning catalog without imposing feature parity.\n\n'
    text+='Targeted local adaptations supersede old verbatim-upstream invocation claims where the actual host lacks a literal Skill/Task tool. Matt Pocock compare-and-swap maintenance preserves these edits for review. Claude-host Codex build/review corrections persist under `system/skill-overrides/claudex/claude/`; Claudex offline dry run is a clean no-op. Never use adoption/reset to discard these changes. Native skill discovery and duplicate-name precedence are distinct from static catalog validation.\n\n'
    text+='[Repair report, tests and remaining dependencies](../audits/skills-2026-10-10-repairs/SUMMARY.md). Historical `_snapshots` and `_project-forks` remain preserved.\n'
    save(p,before,text)

p=ROOT/'wiki/hot.md'
before=p.read_bytes()
text=before.decode('utf-8')
title='## Most recent (2026-10-10): Skill catalog repaired and verified locally'
if title not in text:
    pos=text.index('## Most recent')
    older=text[pos:].replace('## Most recent','## Previous',1)
    entry=title+'\n\n'
    entry+='- Implemented the approved full skill-audit repairs, highest risk first, through the installed Karpathy agent and independent review. [Complete result](../audits/skills-2026-10-10-repairs/SUMMARY.md); [hashes, backups and validation](../audits/skills-2026-10-10-repairs/FINAL-VERIFICATION.json).\n'
    entry+='- Narrowed overlapping provider/export/video/persona triggers; fixed WIP review scope, dirty-worktree staging/deletion assumptions, runtime calls, stale paths and activation drift. Useful workflows and extra payloads retained; no new global activation.\n'
    entry+='- Video helpers preserve existing frames/audio and require an explicit paid provider; missing Codex-global watch payload restored. MCP examples now use text nodes and resolved-root containment. Tracer resolves each filename once.\n'
    entry+='- Catalog validator passes (Claude 224, Codex 211, Gemini 222). YAML check covers 1,732 current entrypoints; 900 repaired/added physical files reconcile; all 74 historical snapshot hashes preserved. Nine video, four validator/generator, two MCP fixtures and 82 hook/gate regression tests pass.\n'
    entry+='- Claudex offline dry run has zero changes/conflicts; reviewed Claude overrides persist. Matt Pocock dry run preserves intentional local edits. No source/student/live data write, paid provider call, deletion, commit, push or publication. Task statuses unchanged.\n'
    entry+='- Missing bootcamp benchmark documents and the research JSON validator remain explicit legacy input gaps. Native selectors, every vendor pipeline and fresh native child-hook acceptance are not certified; a separate terminal check recorded Codex skill-context omissions. Existing sessions may require a fresh session to load changed skills.\n\n'
    save(p,before,text[:pos]+entry+older)

p=ROOT/'wiki/log.md'
before=p.read_bytes()
text=before.decode('utf-8')
title='## [2026-10-10] system | Full skill audit repairs verified locally'
if title not in text:
    text+='\n\n'+title+'\n\n'
    text+='- Joshua authorized fixing the completed catalog audit, highest priority first, retaining useful workflows and narrowing redundant triggers. [Report](../audits/skills-2026-10-10-repairs/SUMMARY.md) and [current-file verification](../audits/skills-2026-10-10-repairs/FINAL-VERIFICATION.json). All 649 original catalog dispositions are reconciled; physical repair count is 900, not 900 distinct skills.\n'
    text+='- Fixed provider corruption/model mandates, handoff/export boundaries, review WIP omissions, scoped staging/write/delete behavior, host calls/paths, graph collision/rebuild rules, video automatic uploads/overwrites, unsafe MCP renderer/path examples and stale activations. Four malformed global YAML descriptions repaired. Original backups and 74 snapshot hashes preserved.\n'
    text+='- Validation: catalog/activation/index checks pass (224 Claude, 211 Codex, 222 Gemini); 1,732 entrypoints parse; 84 direct and 30 literal regressions pass; nine video, four validator/generator, two MCP and 82 existing hook/gate tests pass. Final independent review confirms targeted fixes. Earlier tracer timeouts and verifier path/optional-runtime launch failures are failed attempts, corrected before final verification.\n'
    text+='- Persisted existing Claude-host Claudex repairs in updater overrides; offline dry run is zero changes/conflicts. Matt Pocock dry run skips intentional locally edited copies. [Runtime distinctions](../skills/PARITY.md) and generated skill index updated. No upstream reset/adoption or new global activation.\n'
    text+='- Open limits: original three bootcamp benchmark documents and research JSON validator remain absent; no invented replacements or validated-completion claim. Native selector visibility, all vendor integrations and fresh child-hook acceptance remain outside this local proof. Existing terminal skill-context warning is not fixed by file validation.\n'
    text+='- No deletion, source mutation, student-record change, paid provider call, email/message, commit, push or publication. Existing unrelated edits and task statuses preserved.\n'
    save(p,before,text)

print('Filed PARITY, hot cache and append-only log; task statuses unchanged.')
