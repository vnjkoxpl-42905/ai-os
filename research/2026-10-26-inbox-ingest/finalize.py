from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parents[2]

def update(path, transform):
    file = ROOT / path
    before = file.read_bytes()
    text = before.decode('utf-8-sig')
    newline = '\r\n' if '\r\n' in text else '\n'
    result = transform(text.replace('\r\n', '\n'))
    assert file.read_bytes() == before, f'Concurrent change: {path}'
    file.write_bytes(result.replace('\n', newline).encode('utf-8'))

def item(ident, title, source, value, existing, steps, kind='workflow change', effort='medium'):
    return f'### {ident} · {title}\n- Type: {kind}\n- From: [{source}](../../wiki/sources/{source}.md), captured transcript; see source coverage limits.\n- Value: {value}\n- Already here: {existing}\n- Steps:\n' + ''.join(f'  {i}. {step}\n' for i,step in enumerate(steps,1)) + f'- Effort: {effort} · Status: new (2026-10-26)\n'

def main():
    proposed = [
      item('AQ-037', 'Compare the small-business plugin with existing workflows', 'anthropic-small-business-13-skills-austin-marchese', 'Finds useful gaps without importing duplicate skills.', 'Both catalogs, prospect draft skills, brand/voice rules and AI visibility/SEO skills exist; the advertised plugin tables and current capabilities have not been checked.', ['Inspect the official plugin source and recover its current utility/orchestrator table before any installation.', 'Map lead discovery/enrichment, lead ranking, speed-to-lead drafts, customer-feedback inputs, content strategy/posts, SEO, proposal/contract preparation and finance preparation to existing skills. Include Clay only if a concrete uncovered enrichment need exists.', 'Pilot one genuinely missing repeated task on saved inputs, preserving draft-only sends and human decisions; do not add every named tool.', 'Check: save a source-backed gap/overlap table and one pilot result or an explicit no-adoption verdict.'], 'skill'),
      item('AQ-038', 'Audit skill routing collisions and briefing overlap', 'anthropic-small-business-13-skills-austin-marchese', 'Makes each request reach one clear owner and reduces competing reports.', 'The catalogs and root routers already define workflow owners; this capture does not establish a local routing defect.', ['Compare utility and orchestrator boundaries on actual local skill descriptions, including inbox routing, content strategy/posts and marketing review.', 'Compare Monday, Friday and quarterly briefing purposes with existing morning/level-up routines, using real outputs before proposing consolidation.', 'Propose only evidence-backed trigger or handoff changes; preserve current authorization boundaries.', 'Check: representative requests select one owner, specialist handoffs are explicit and each retained briefing has a distinct decision.'], 'workflow change'),
      item('AQ-039', 'Recover and compare the six Karpathy demonstration prompts', 'karpathy-expert-agent-nate-herk', 'Closes the explicitly unresolved visual evidence gap without rebuilding the expert system.', 'The Karpathy corpus, method, agent and teaching skill already exist; the six displayed prompts were not inspected in this ingest.', ['Obtain and inspect the actual video frames containing all six prompts; preserve readable frame evidence and exact transcription with timestamps.', 'Compare acquisition, compilation, rules, agent/skill, execution gate and acceptance criteria against the existing implementation and coverage audit.', 'Include a Windows-safe execution check if an actual gap is demonstrated; record unsupported claims separately.', 'Check: all six prompts have readable evidence and a disposition, with missing evidence still marked incomplete.'], 'workflow change'),
    ]
    for filename in ['brain-queue-proposals.md', 'runtime-queue-proposals.md']:
        text = (ROOT / 'research/2026-10-26-inbox-ingest' / filename).read_text(encoding='utf-8-sig')
        for block in re.split(r'(?=^### AQ-)', text, flags=re.M)[1:]:
            proposed.append(re.split(r'^## ', block, maxsplit=1, flags=re.M)[0].strip()+'\n')
    def ai(text):
        text = text.replace('updated: 2026-10-14', 'updated: 2026-10-26').replace('Next ID: AQ-033', 'Next ID: AQ-042')
        additions = [b for b in proposed if re.search(r'^### (AQ-\d+)',b).group(1) not in text]
        additions.sort(key=lambda b: int(re.search(r'AQ-(\d+)',b).group(1)), reverse=True)
        text = text.replace('## New\n', '## New\n\n'+'\n'.join(additions), 1)
        if text.rstrip().endswith('\nNone.'):
            text = text.rstrip()[:-5].rstrip()+'\n'
        return text
    update('references/ai-workspace/action-queue.md', ai)
    def lsat(text):
        if '### LQ-006' in text: return text
        block = '''### LQ-006 · Evaluate the expanded MCAT CARS question capture before reuse
- Type: outside tool
- From: [MCAT CARS expanded capture](sources/mcat-cars-three-passages-2026-10-15.md#expanded-question-and-explanation-capture-2026-10-26), three passages and supplied answer explanations.
- Value: determines whether the 12 saved questions add useful outside-reading practice.
- Already here: three passage bodies are filed in the Reading Center bundle; the new capture supplies 12 questions and explanations, not an adjudicated LSAT bank.
- Steps:
  1. Check each supplied key and explanation against its passage, starting with Passage 1 question 1; preserve original source answers separately from adjudications.
  2. Check provenance, reuse rights and whether a suitable existing reading/practice mode needs these questions.
  3. Propose adoption, adaptation or decline; no publication or assignment is implied.
  4. Check: all 12 questions have a support/rights disposition and any chosen pilot preserves the source and explicit limitations.
- Effort: medium · Status: new (2026-10-26)
'''
        return text.replace('updated: 2026-10-21','updated: 2026-10-26').replace('Next ID: LQ-006','Next ID: LQ-007').replace('## New\n','## New\n\n'+block,1)
    update('wiki/lsatu-idea-queue.md', lsat)
    def hub(text):
        marker = '## Inbox batch processed 2026-10-26'
        if marker in text: return text
        return text+'\n\n'+marker+'\n\n[Batch report](../../research/2026-10-26-inbox-ingest/REPORT.md) records duplicate checks, preserved revisions, new summaries and coverage limits. New sources include [ARMS and retrieval](../../wiki/sources/ultimate-second-brain-arms-robonuggets.md), [small-business skills](../../wiki/sources/anthropic-small-business-13-skills-austin-marchese.md), and [Karpathy expert-agent commentary](../../wiki/sources/karpathy-expert-agent-nate-herk.md). Source claims are captured, not current product verification. The Karpathy visual-prompt requirement remains incomplete. Follow-up is in AQ-033 through AQ-041; existing items retain their statuses.\n'
    update('references/ai-workspace/index.md', hub)
    for filename,title in [('anthropic-small-business-13-skills-austin-marchese.md','Anthropic Just Released 13 New Skills To Level Up Your Claude Setup'),('karpathy-expert-agent-nate-herk.md','I Built Another Andrej Karpathy Using Claude')]:
        update('wiki/sources/'+filename, lambda text,title=title: re.sub(r'^aliases: \[(.*?)\]$', lambda m:'aliases: ["'+title+'", '+m.group(1)+']',text,count=1,flags=re.M) if title not in text.split('tags:')[0] else text)
    print('Queue additions integrated, metadata and AI hub updated.')

if __name__ == '__main__': main()
