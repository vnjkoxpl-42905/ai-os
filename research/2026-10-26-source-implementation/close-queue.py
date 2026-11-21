"""Record the human-authorized implementation pass without deleting its history."""
from pathlib import Path
from urllib.parse import unquote
import json
import re

ROOT = Path(__file__).resolve().parents[2]
DATE = '2026-10-26'
REPORT = 'research/2026-10-26-source-implementation/REPORT.md'

# Closing an optional proposal as declined is separate from calling it implemented.
DONE = {
 'AQ-003': 'Identical verification-plan guardrail implemented in both runtime manuals and compared. Local implementation checked; next native-session behavior remains a future observation.',
 'AQ-008': 'Reconciled six existing shared home utility installations through explicit parity declarations; no duplicate activation. Presence is not repaired functionality.',
 'AQ-010': 'Settled operational role under delegated judgment: Smart Connections remains an optional Obsidian aid, with catalog/alias retrieval and the bounded helper serving agents. No claim of semantic-search quality comparison.',
 'AQ-025': 'Kept the existing source-linked reference route, verified a concrete lookup and added reusable capture fields; no second media index adopted.',
 'AQ-033': 'Implemented and ran a generated local ARMS inventory with owner links, selected routine metadata and explicit unknown authentication/usage. No connections or schedules changed; full provider health is not certified.',
 'AQ-037': 'Completed official 44-skill inventory comparison and chose no wholesale plugin/Clay adoption because no missing repeated workflow was demonstrated.',
 'AQ-039': 'Reconciled six existing prompt/test entries to physical implementation. Fresh 82 regression tests and tokenizer checks passed. Native hook trust/enforcement was not newly certified.',
 'AQ-040': 'Verified installed version and official Mods eligibility, then chose no additional mod because existing owners cover the examples; no trial or new customization was needed.',
 'LQ-006': 'Completed all 12 question adjudications. Ten have defensible best answers, two are quarantined; rights remain unverified for every item. Declined question-bank reuse rather than importing it.',
}
DECLINED = {
 'AQ-004': 'Keep existing models: the saved benchmark does not establish cheaper-model equivalence. No unsupported model switch or new benchmark claim.',
 'AQ-005': 'Keep the current humanizer/voice route. The limited saved comparison does not justify a duplicate editor; no SlopMonster superiority claim.',
 'AQ-015': 'No demonstrated tool gap justifies the affiliate stack. Retain existing agent/research/dictation/media tools; reopen only for a concrete unmet task.',
 'AQ-017': 'The unnamed transition upstream remains unverified, while existing GSAP/React Bits cover current motion needs. Decline chasing/installing an unidentified extra skill.',
 'AQ-019': 'No selected teaching or promotional media need justifies a new generation demonstrator. Keep the existing preview-first method; no output/generation/quality claim.',
 'AQ-020': 'No useful 3D task selected; keep still-first planning and avoid an unrelated Blender dependency/prototype.',
 'AQ-024': 'Existing artifact annotations and preserved prototypes meet the current review need; no additional sharing/review system selected.',
 'AQ-026': 'Keep optional narrow tweaks and reload/export checks in the owning design method; no generic tweak framework without recurring need.',
 'AQ-027': 'No unique editable-brand need justifies a Linearity trial; account/licence/product superiority unverified.',
 'AQ-030': 'No recurring authoring gap justifies bespoke content/asset/metadata controls. Existing app/editor ownership remains.',
 'AQ-031': 'No provider-wrapper task or budget selected. Do not run a paid unit-cost experiment merely because a source promotes one.',
 'AQ-032': 'No useful wrapper task or verified upstream starter exists in the evidence; decline speculative starter search/installation.',
 'AQ-035': 'The useful deterministic retrieval method is implemented locally and existing research tools cover discovery. No concrete remaining gap justifies comparing replacement systems or commercial guides now; last30days identity is recorded without installing it.',
 'AQ-036': 'Keep an evidence-linked operating inventory rather than build another graph UI without a demonstrated navigation problem. Existing Graphify remains available; no graph load/performance trial claimed.',
}
REMAINING = {
 'AQ-001': 'Actual LSAT U security scan, tool comparison and finding adjudication remain unperformed; tool presence is not a scan.',
 'AQ-009': 'Draft-only rule reconciled and local standard/higher checker positive/negative tests pass; Cal.com GET returned HTTP200. Remaining: verify the unusual $60 Stripe link identity and amount with Stripe authority. No sends/payments.',
 'AQ-012': 'Three source-grounded teaching/interview corrections implemented and installed copies synced. Remaining: refreshed 30-day correction scan and remaining groups; no blanket adoption of every old suggestion.',
 'AQ-013': 'One clearly redundant 50-byte sentence removed; guardrails retained. Remaining: complete five-skill audit and real-run behavior checks.',
 'AQ-014': 'Rulebook now has proposal-only defaults and refreshed metadata (194 files,5305489837bytes). Remaining: actual original/new-name/destination filing batch and row approval. Nothing moved or deleted.',
 'AQ-018': 'Capture fields and selected-family route exist. Remaining: an actually approved permanent brand direction and extraction of its tokens, states and motion.',
 'AQ-021': 'Reusable teacher content tables exist. Remaining: selected branded document/template and its reusable rendered example.',
 'AQ-022': 'Remaining: authentication backend variable mapping and actual email-client previews before any template change.',
 'AQ-023': 'Finite visitor-decision/reference worksheet implemented. Remaining: selected acquisition task, actual comparator evidence and scoped funnel/copy pilot.',
 'AQ-028': 'Region/flow lookup map and evidence/licence fields implemented. Remaining: inspect chosen gallery examples and their actual access/licence constraints.',
 'AQ-029': 'Bounded critique recipe implemented with observable findings and finite revisions. Remaining: use it on a selected rendered feature and preserve before/after evidence.',
 'AQ-034': 'Compiled-page helper implemented and integrated into existing query skill copies;10 regression tests and8/8 local top-three/miss cases pass. Remaining: fair end-to-end agent comparison with actual model-token cost; local character/timing results are not that comparison.',
 'AQ-038': 'Concrete wording/teaching fixes landed and utility/orchestrator overlap is documented. Remaining: representative request-routing and actual briefing-output collision audit.',
 'AQ-041': 'Installed version, official latest release and command help checked. Remaining: bounded interactive voice/task/worktree/rendering acceptance if useful; no upgrade/remote enablement.',
 'LQ-001': 'Teacher-only recall observation/checking form implemented; source versions/timing differences preserved and mandatory vendor targets not adopted. Remaining: observed learner task evidence.',
 'LQ-002': 'Contextual vocabulary template implemented. Remaining: selected external resources/roots/tutor verification before recommendation or assignment.',
 'LQ-003': 'Exact-question/whole-choice method and original demonstration implemented; no fixed return/skip quotas adopted. Remaining: adjudicate complete source exceptions and caption/notes differences.',
 'LQ-004': 'Separate-author comparative evidence sheet and original worked example implemented. Remaining: observed learner task and selected-passage validation.',
 'LQ-005': 'Preview-first local checklist implemented. Remaining: accessible editing-pack/source review and a useful synthetic preview trial; no install/tool adoption.',
}

def write_checked(path, text, before):
    assert path.read_bytes() == before, f'Concurrent edit: {path}'
    newline = '\r\n' if b'\r\n' in before else '\n'
    path.write_bytes(text.replace('\r\n','\n').replace('\n',newline).encode('utf-8'))

def source_records(block, queue, ident, outcome, detail):
    line = next((line for line in block.splitlines() if line.startswith('- From:')), '')
    paths = []
    for value in re.findall(r'\]\(([^)]+)\)', line):
        relative = unquote(value.strip('<>').split('#')[0])
        path = (queue.parent / relative).resolve()
        if path.is_file() and path.is_relative_to((ROOT/'wiki/sources').resolve()):
            paths.append(path)
    for path in set(paths):
        before = path.read_bytes()
        text = before.decode('utf-8-sig')
        marker = f'{outcome} {DATE}: {ident}.'
        if marker in text:
            continue
        if '## Queue record' not in text:
            text += '\n\n## Queue record\n'
        report_link = Path('../../research/2026-10-26-source-implementation/REPORT.md').as_posix()
        text += f'\n{marker} {detail} [Implementation record]({report_link}).\n'
        write_checked(path, text, before)

def main():
    results = []
    for relative in ['references/ai-workspace/action-queue.md','wiki/lsatu-idea-queue.md']:
        queue=ROOT/relative
        before=queue.read_bytes()
        text=before.decode('utf-8-sig').replace('\r\n','\n')
        first=text.index('## Approved')
        header=text[:first]
        blocks=re.findall(r'^### ([AL]Q-\d+) · ([^\n]+)\n(.*?)(?=^### [AL]Q-|\Z)',text,re.M|re.S)
        approved=[];new=[]
        for ident,title,body in blocks:
            # Drop the old section separator captured after its final approved item.
            body=re.sub(r'\n## New\s*\n','\n',body)
            block=f'### {ident} · {title}\n{body}'.rstrip()+'\n'
            if ident in DONE:
                state='Done';detail=DONE[ident]
            elif ident in DECLINED:
                state='Declined';detail=DECLINED[ident]
            else:
                state='Partial';detail=REMAINING[ident]
                note=f'- Progress {DATE}: {detail}\n'
                if note not in block:
                    block=block.rstrip()+'\n'+note
                (approved if 'Status: approved' in block else new).append(block)
            source_records(block,queue,ident,state,detail)
            results.append({'id':ident,'title':title,'outcome':state,'detail':detail})
        assert len(blocks)==(36 if 'action-queue' in relative else 6)
        output=header+'## Approved\n\n'+ ('\n'.join(approved) if approved else 'None.\n')
        output+='\n## New\n\n'+ ('\n'.join(new) if new else 'None.\n')
        write_checked(queue,output,before)
    target=ROOT/'research/2026-10-26-source-implementation/queue-dispositions.json'
    target.write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
    counts={name:sum(r['outcome']==name for r in results) for name in ['Done','Declined','Partial']}
    print(json.dumps(counts));print('Remaining:',','.join(r['id'] for r in results if r['outcome']=='Partial'))

if __name__=='__main__':main()
