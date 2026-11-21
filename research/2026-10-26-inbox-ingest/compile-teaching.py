from pathlib import Path
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[2]
DATE = '2026-10-26'

def preserve(name, slug):
    original = ROOT / 'raw/inbox' / name
    data = original.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    folder = ROOT / 'raw/sources/clips' / slug
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / 'source.md'
    if target.exists():
        assert target.read_bytes() == data
    else:
        shutil.copyfile(original, target)
    assert hashlib.sha256(target.read_bytes()).hexdigest() == digest
    provenance = folder / 'PROVENANCE.md'
    if not provenance.exists():
        provenance.write_text(f'# Preserved inbox source\n\nOriginal: raw/inbox/{name}\n\nArchived: {DATE}. Capture mechanism and publication date unknown.\n\nOriginal filename: {name}\n\nSize: {len(data)} bytes. SHA-256: {digest}.\n\nCopied byte-for-byte; original retained. No transformation.\n', encoding='utf-8')
        (folder / 'SHA256SUMS').write_text(f'{digest}  source.md\n', encoding='utf-8')
    return digest

def append(path, marker, body):
    file = ROOT / path
    before = file.read_bytes()
    text = before.decode('utf-8-sig')
    if marker in text:
        return
    assert file.read_bytes() == before
    with file.open('a', encoding='utf-8', newline='') as out:
        out.write('\n\n' + marker + '\n\n' + body + '\n')

def main():
    name = 'MCAT CARS Practice Questions and Explanations 1.md'
    slug = 'mcat-cars-questions-revision-2026-10-26'
    digest = preserve(name, slug)
    append('wiki/sources/mcat-cars-three-passages-2026-10-15.md', '## Expanded question-and-explanation capture (2026-10-26)', f'''The newly supplied [expanded capture](../../raw/sources/clips/{slug}/source.md) contains the same three passage subjects plus **12 questions, 48 options and 12 supplied explanations**. Its [provenance](../../raw/sources/clips/{slug}/PROVENANCE.md) and SHA-256 `{digest}` preserve this separate generation. The entire supplied text was read. The earlier passage-only evidence remains unchanged; its statement that questions are absent applies to that earlier capture only.

The supplied keys, in question order, are Passage 1: A/D/C/C; Passage 2: B/B/C/A; Passage 3: C/A/C/B. These are the source's keys, not independently adjudicated LSAT answers. The expanded source supplies adapted-text attributions to Plato/Jowett, Thoreau and A. C. Seward. Those are captured bibliographic claims; the underlying linked editions were not opened. The only visible commercial host clue is a Shemmassian Consulting question-bank link; the original page URL remains unknown.

The questions sample agreement/inference, rhetorical purpose, a hypothetical application, explicit detail, an analogy and a least-likely continuation. Passage 1 question 1 deserves review before reuse: the explanation treats Ion's Homer-only interest as evidence of comparative judgment, whereas the passage uses his narrow expertise to establish a problem. Preserve the supplied key and explanation while checking their support, rather than silently correcting the source.

This complements the existing [Reading Center bundle](../../corpus/reading-center/README.md). Passage reading is already filed; importing a question bank, validating its keys and checking reuse rights are separate proposed work. No app import, publication or assignment occurred. See LQ-006 in the [idea queue](../lsatu-idea-queue.md).

> "The correct answer is D." (Passage 1, answer 2)

> "Henry David Thoreau." (Passage 2 attribution)''')
    append('corpus/reading-center/README.md', '## Expanded MCAT question capture (2026-10-26)', 'The [canonical source summary](../../wiki/sources/mcat-cars-three-passages-2026-10-15.md#expanded-question-and-explanation-capture-2026-10-26) now links a separate preserved generation containing 12 questions and their supplied explanations alongside the three passages. Existing reading imports remain passage-only. Question validity, rights and a possible practice format await LQ-006; the source keys are not independently adjudicated.')

    dashboards = [('Dashboard.md', '7sage-lawgic-language', 'Lawgic: the language', 'The arrow expresses a sufficient-to-necessary relationship. Set inclusion is one application; a requirement between events need not describe tangible nested sets. The text motivates symbols for manipulation while retaining ordinary meaning. The bare store-to-milk example has no complete stated rule in the capture, so it is not safe to reconstruct its missing condition.', ['The visual language is cumbersome.', 'The → establishes a **conditional relationship**']), ('Dashboard 1.md', '7sage-sufficiency-relationships', 'Sufficiency and necessity are relationships', 'A condition has its role relative to another condition. Cats are sufficient for mammals; mammals are sufficient for animals and necessary for cats. Name the pair before assigning roles. This is complementary evidence for preserving complete conditions and not labeling a term permanently sufficient or necessary.', ['It\'s a relationship.', 'Sufficiency and necessity are relationships.']), ('Dashboard 2.md', '7sage-group-one-indicators', 'Group 1 sufficient-condition indicators', 'The source lists if, when, where, all, every, any and the only, then models identifying the indicator, selecting the complete ideas, assigning symbols and translating. Optional steps form the contrapositive and read it back. It explicitly warns that the list is both overinclusive and underinclusive: a word can occur without stating a conditional. Grammar and meaning must determine the whole attached condition. The example uses zombies attacking NYC and a crashing real-estate market. Its numerical prevalence claim is unsupported here.', ['Step 1: Identify the conditional indicator', 'the list is both over and underinclusive.'])]
    for filename, slug, title, meaning, quotes in dashboards:
        digest = preserve(filename, slug + '-2026-10-26')
        path = ROOT / 'wiki/sources' / (slug + '.md')
        evidence = f'../../raw/sources/clips/{slug}-2026-10-26/source.md'
        content = f'''---
type: source
subject: "{title}"
created: {DATE}
updated: {DATE}
aliases: [{json.dumps(title)}, {json.dumps(filename)}]
tags: [llm-wiki, lsat, conditionals, source]
evidence: {evidence}
sha256: {digest}
sources:
  - ../../raw/sources/clips/{slug}-2026-10-26/PROVENANCE.md
contradictions: []
---

# {title}

Source: supplied 7Sage lesson text, captured under the generic filename `{filename}`. Publication/capture date and exact original page URL unknown. Ingested {DATE}. Full text read; images and linked Miro boards were not inspected. Player progress fragments do not establish video coverage.

## What the text supports

{meaning}

## Application and existing coverage

Complementary preserved text for the [existing 7Sage conditional research](../../brainstorms/2026-09-30-conditional-curriculum/research-7sage-conditionals.md) and [conditional teaching reference](<../../corpus/Curriculum/Conditional Logic/Notes/_megadoc_reference_conditionals.md>). Those existing pages already discuss these teaching functions; no new curriculum direction, symbol system or course revision is adopted. Joshua's chosen examples, voice and sequence remain authoritative. Source jokes, learner ridicule and unsupported numerical claims do not belong in student copy.

## Mentions in source

> "{quotes[0]}" (lesson text)

> "{quotes[1]}" (lesson text)

## Coverage and actions

Text-only compilation is complete. Diagram content and video/audio remain unreviewed. No new queue item: the source's translation, complete-condition, relationship and meaning-check functions are already represented in the cited curriculum research and teaching reference. A linked image is evidence of an attachment, not proof of visual inspection.
'''
        if not path.exists():
            path.write_text(content, encoding='utf-8')
    append('brainstorms/2026-09-30-conditional-curriculum/research-7sage-conditionals.md', '## Preserved generic Dashboard clips (2026-10-26)', 'Three complete supplied lesson-text captures now have source summaries: [Lawgic language](../../wiki/sources/7sage-lawgic-language.md), [relational sufficiency/necessity](../../wiki/sources/7sage-sufficiency-relationships.md), and [Group 1 indicators](../../wiki/sources/7sage-group-one-indicators.md). Complementary evidence for the existing research, with no changed curriculum decision. Text was read; linked diagrams and lesson videos were not inspected in this batch.')
    print('Teaching compilation complete; MCAT expanded capture plus three Dashboard lesson sources preserved.')

if __name__ == '__main__':
    main()
