from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]

def edit(path, transform):
    p=ROOT/path
    before=p.read_bytes()
    result=transform(before.decode('utf-8-sig').replace('\r\n','\n'))
    assert p.read_bytes()==before
    p.write_text(result,encoding='utf-8',newline='\n')

def main():
    canonical='wiki/sources/i-built-another-andrej-karpathy-using-claude.md'
    extra='''\n\n## Retained inbox caption generation (2026-10-26)

The [supplied inbox capture](../../raw/sources/clips/karpathy-expert-agent-nate-herk/source.md) was read in full through 10:43 and preserved with [provenance](../../raw/sources/clips/karpathy-expert-agent-nate-herk/PROVENANCE.md), SHA-256 `3c453f7be66ee3cf67cc63c4439c8bf477726c213a1aaa763f35e271e39a2d8c`. This complements the previously saved timestamped transcript and prompt inspection; it does not replace them. The initial batch search missed this canonical summary and therefore incorrectly characterized all six prompt entries as missing. The existing prompt record was read during reconciliation: it documents five numbered cards plus the actual test command, and explicitly does not establish a separate sixth numbered card.

The complete source describes acquisition, immutable raw evidence, linked compilation, corroborated rules, agent/teaching skill, scoped execution gate and a tokenizer test. Existing Karpathy implementation/coverage records remain authoritative. No fresh playback, displayed-prompt inspection or environment execution occurred in this batch. AQ-039 begins from the existing prompt artifacts and execution audit; recover additional video evidence only for an identified gap.

> "The raw files don't get touched" (4:10, supplied capture)

> "every rule has to connect with an exact quote from him and where it came from." (5:41, supplied capture)
'''
    edit(canonical,lambda t:t+extra if '## Retained inbox caption generation' not in t else t)
    p=ROOT/'wiki/sources/karpathy-expert-agent-nate-herk.md'
    p.write_text('''---
type: reference
subject: Karpathy inbox capture routing record
created: 2026-10-26
updated: 2026-10-26
aliases: [Karpathy caption routing 2026-10-26]
tags: [ai-workspace, routing]
---

# Use the existing Karpathy video summary

This batch initially missed the canonical source page. Its caption-generation evidence and corrected coverage now live on [the existing summary](i-built-another-andrej-karpathy-using-claude.md#retained-inbox-caption-generation-2026-10-26). Existing prompt artifacts document five numbered cards and an actual teaching test command; a separate numbered sixth card remains unverified. This routing record is retained to preserve links without deleting files or creating a second account of the source.
''',encoding='utf-8')
    queue='references/ai-workspace/action-queue.md'
    def fixqueue(t):
        start=t.index('### AQ-039');end=t.index('### AQ-038',start)
        replacement='''### AQ-039 · Reconcile existing Karpathy prompt evidence with implementation gaps
- Type: workflow change
- From: [canonical Karpathy video summary](../../wiki/sources/i-built-another-andrej-karpathy-using-claude.md), existing prompt artifacts and 2026-10-26 caption generation.
- Value: checks actual remaining gaps without repeating completed prompt extraction or rebuilding the expert system.
- Already here: research/karpathy-video-2026-10-08/prompts.md records five numbered cards plus an actual test command; the canonical source and execution audit already exist. A separate numbered sixth card was not verified.
- Steps:
  1. Read the saved prompt transcription, source evidence and VIDEO-PROMPT-EXECUTION record before proposing any new acquisition.
  2. Compare acquisition, compilation, corroborated rules, agent/skill, execution gate and environment-specific acceptance against current implementation; separate historical outcomes from fresh checks.
  3. Recover readable video evidence only for a consequential unresolved gap. Do not invent a separate sixth card merely because six prompts were announced.
  4. Check: each existing prompt/test entry has an evidence-backed implementation disposition, remaining gaps are explicit and no finished extraction is mislabeled missing.
- Effort: medium · Status: new (2026-10-26)

'''
        return t[:start]+replacement+t[end:]
    edit(queue,fixqueue)
    edit('references/ai-workspace/index.md',lambda t:t.replace('The Karpathy visual-prompt requirement remains incomplete.','The canonical Karpathy record already links five inspected numbered prompt cards and the actual test command; this batch did not repeat playback.'))
    def report(t):
        t=t.replace('Eight new source summaries:', 'Seven new source summaries plus one retained routing record:')
        t=t.replace('**MCAT', '**MCAT')
        t=t.replace('Two existing source summaries complemented:', 'Three existing source summaries complemented (including the canonical Karpathy source):')
        t=t.replace('- Karpathy: transcript compilation is limited. Joshua\'s earlier requirement to inspect six displayed video prompts is still unmet; AQ-039 tracks recovery and comparison. This ingest does not claim to satisfy that earlier visual requirement.', '- Karpathy correction: the existing canonical summary and prompt artifacts already record five inspected numbered cards plus the actual teaching-test command. The batch initially missed this record, then reconciled the new caption generation into it. A separate sixth numbered card is unverified; no fresh visual inspection occurred. AQ-039 checks remaining implementation/evidence gaps from these existing artifacts.')
        t=t.replace('one possible session lacks a resolved student identity and is not a completed student intake.', 'one incomplete session fragment was matched by distinctive wording to Celia Cutler\'s 2026-08-03 Gemini transcript, preserved and linked from her transcript ledger. Student-record validation passed; audio was not played.')
        t=t.replace('Recover six Karpathy prompts from actual video evidence','Reconcile existing Karpathy prompt evidence and implementation gaps')
        return t
    edit('research/2026-10-26-inbox-ingest/REPORT.md',report)
    # The wiki lint sees only wiki-to-wiki inbound links; add useful source relationships.
    related={
      'wiki/sources/7sage-lawgic-language.md':['7sage-sufficiency-relationships','7sage-group-one-indicators','lsat-lab-conditional-logic-clip'],
      'wiki/sources/7sage-sufficiency-relationships.md':['7sage-lawgic-language','7sage-group-one-indicators'],
      'wiki/sources/7sage-group-one-indicators.md':['7sage-lawgic-language','7sage-sufficiency-relationships'],
      'wiki/sources/anthropic-small-business-13-skills-austin-marchese.md':['claude-mods-chase-ai','ultimate-second-brain-arms-robonuggets'],
      'wiki/sources/claude-mods-chase-ai.md':['anthropic-small-business-13-skills-austin-marchese','ultimate-second-brain-arms-robonuggets','meet-new-codex-cli'],
      'wiki/sources/ultimate-second-brain-arms-robonuggets.md':['anthropic-small-business-13-skills-austin-marchese','claude-mods-chase-ai'],
    }
    for path,links in related.items():
        block='\n\n## Related source comparison (2026-10-26)\n\nCompare the distinct source accounts: '+', '.join(f'[{name}]({name}.md)' for name in links)+'. These links support comparing teaching functions or workflow ownership, not treating separate accounts as independent verification of product claims.\n'
        edit(path,lambda t,block=block:t+block if '## Related source comparison (2026-10-26)' not in t else t)
    log=ROOT/'wiki/log.md'
    with log.open('a',encoding='utf-8') as f:
        f.write('''\n\n## [2026-10-26] ingest | Reconcile missed Karpathy canonical source and resolve recording identity

- Correction to the immediately preceding batch entry: an existing canonical Karpathy video summary and saved prompt artifact were missed by the initial search. New caption evidence merged into wiki/sources/i-built-another-andrej-karpathy-using-claude.md. The new name remains a routing record, not a second source account. Existing evidence records five numbered on-screen cards plus a test command; no separate numbered sixth card is proven. AQ-039 revised to compare existing evidence and implementation gaps first.
- Recording identity resolved through distinctive text matching to Celia Cutler's 2026-08-03 full Gemini transcript; supplementary metadata/audio preserved with hashes and linked in students/celia-cutler/transcripts.md. Student-record check passed. The recording is incomplete, automatic and unheard; it does not replace the canonical transcript or create a recap.
- Final batch totals: seven new substantive source summaries, one retained routing record, three canonical summaries complemented. Queue counts unchanged:42 open. Originals retained.
''')
    print('Canonical-source reconciliation and recording correction saved.')

if __name__=='__main__':main()
