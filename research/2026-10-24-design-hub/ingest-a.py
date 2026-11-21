from pathlib import Path
import hashlib, shutil, json, datetime

root = Path(__file__).resolve().parents[2]
out = Path(__file__).parent

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def put(p, text):
    p.parent.mkdir(parents=True, exist_ok=True)
    expected = digest(p) if p.exists() else None
    assert (digest(p) if p.exists() else None) == expected
    p.write_text(text, encoding='utf-8')

specs = [
    {
        'filename': "17 Things You Didn't Know Claude Design Could Do.md",
        'slug': '17-claude-design-use-cases-austin-marchese',
        'title': 'Austin Marchese: seventeen Claude Design use cases',
        'author': 'Austin Marchese', 'url': 'https://www.youtube.com/watch?v=7rRVwjzVQsc', 'end': '17:11',
        'sections': [
            ('Systems and iteration', 'The creator recommends extracting a reusable design system from an existing website and reusing it across technical and nontechnical outputs (0:00 to 1:22). Inline comments and drawings make feedback precise (9:10). He proposes divergent page or component variations followed by convergence on the preferred concept (10:19 to 11:15).'),
            ('Seventeen uses', 'The examples cover systems, animation, 3D assets with usage mockups, old-document rebranding, event flyers, colour/type comparisons, HTML email templates, inline feedback, funnel mapping, multiple variants, clickable wireframes, cross-team comments, templates, client-branded proposals, lead magnets, resumes and final copy cleanup. The email example adapts variables to the authentication backend (8:21 to 8:57).'),
            ('Limits and incentives', 'He distinguishes Design from general-purpose Code/Co-work/Chat, describes it as layout rather than native image generation (4:37), and recommends low-risk internal animations rather than an exact product launch video (1:32). This is an Anthropic-sponsored video with BuildPartner marketing. Productivity and tool-capability statements are the creator\'s claims, not independently tested facts.')],
        'quotes': ['create a reusable design system', 'find winning color pairings'],
        'actions': ['Reusable design system', 'Animated internal explainers', '3D asset plus usage mockups', 'Rebrand old documents', 'Event flyers', 'Palette/type comparison', 'Backend-compatible HTML emails', 'Inline comments/drawings', 'Funnel map and CTA variants', 'Divergent variants and convergence', 'Clickable wireframes', 'Shared feedback', 'Reusable templates', 'Client-brand proposals', 'Lead magnets', 'Resume', 'Human copy cleanup']
    },
    {
        'filename': '25 Tricks to Level Up Claude Design in 13 Mins.md',
        'slug': '25-claude-design-tricks-robonuggets',
        'title': 'RoboNuggets: twenty-five Claude Design tips',
        'author': 'Jay, RoboNuggets', 'url': 'https://www.youtube.com/watch?v=_SVU3oC4JX8', 'end': '13:31',
        'sections': [
            ('Reference-led systems', 'The creator recommends extracting a system from owned assets or a reference, shortlisting three systems, naming suitable fonts, studying competitor copy and mixing selected design principles (0:35 to 3:57). He says a local Code skill can hold a system when web Design lacks direct local-file access.'),
            ('Resources and polish', 'Intermediate tips cover external image/video generation, previous projects, annotated reference libraries, Impeccable, voice guidance, 21st.dev, React Bits, Canvas UI, coherent icon packs, editable SVG, Lordicon and Creators Toolbox (4:57 to 9:48). Counts, free-access descriptions and capabilities remain dated source claims; licences and accounts need separate verification.'),
            ('Advanced workflows', 'Advanced tips cover selective Apple HIG guidance, GSAP, Code Design artboards, a slider-based tweak panel, word-timestamped transcript animations through Hyperframes, and a searchable reusable design asset index (10:15 to 12:39). The captured text does not include the full prompts shown on screen. The existing PDF resource map already records decisions on all 25 tips; this transcript adds preserved, searchable evidence rather than another installation mandate.')],
        'quotes': ['Number 11 is Impeccable.', 'Number 21 is GSAP.'],
        'actions': ['Design systems', 'Refero-style gallery', 'Shortlist three systems', 'Code-owned system skill', 'Font sources/pairing', 'Competitor copy study', 'Mix system principles', 'Kie external generation', 'Previous-project reuse', 'Annotated reference library', 'Impeccable', 'Voice skill', '21st.dev', 'React Bits', 'Canvas UI', 'Coherent icon pack', 'Editable SVG', 'Lordicon', 'Creators Toolbox', 'Apple HIG reference', 'GSAP', 'Code Design canvas', 'Tweak sliders and bake values', 'Transcript-to-Hyperframes', 'Design asset operating system']
    },
    {
        'filename': 'How to Use Claude Design Better Than 99% of People.md',
        'slug': 'claude-design-fifteen-hacks-jack',
        'title': 'Jack: fifteen reference-led Claude Design hacks',
        'author': 'Jack; surname/channel identity not established by capture', 'url': 'https://www.youtube.com/watch?v=IYNAyRkUsjI', 'end': '34:28',
        'sections': [
            ('Motion with a visible target', 'The creator recommends a reference clip plus brand assets and intent, then three style options for looping animation whose first and last frames match (1:17 to 3:30). Hover lifts, soft presses and counters are suggested as small quality details. Claims that these make every design premium are judgments, not measured usability results.'),
            ('Brand and editable assets', 'He proposes one brand-guideline file informed by brandguidelines.net, deck.gallery, logosystem.co, Visual Journal and Rebrand Gallery. He describes Higgsfield generation and Linearity brand imports, editable layouts, templates and MCP integration (5:24 to 14:38). Account access, paid plans, legal reuse and current connector behavior were not verified in this ingestion.'),
            ('Inspect the relevant part and flow', 'Fonts and icons come from Typewolf, Fonts In Use, WhatTheFont, Fontshare, Flaticon and Icons8; the transcript explicitly says to check licences (15:35 to 16:51). Section-specific galleries include Navbar Gallery, Footer Design, CTA Gallery, 404s Design, Unsection and Bento Grids. Mobbin and Refero are suggested for whole flows; 60fps.design for motion rather than static screenshots (17:35 to 20:54).'),
            ('Critique, clarity and reuse', 'A Design Loop uses a critic against a concrete reference; a five-agent checklist is also mentioned, but its exact five roles are absent from the captured transcript (21:22 to 25:16). He advocates a glance test and lower text density, SlopMonster copy review, simplified technical language, original poster/3D experiments and searchable reusable design assets (25:48 to 34:28). His numerical ASD-STE100 descriptions are unverified. Agent consensus is not proof of quality and no unbounded loop is adopted.')],
        'quotes': ['Hack 3: Premium Micro Interactions', 'Hack 9: The Design Loop'],
        'actions': ['Reference clip plus brand for motion', 'Seamless loops with three styles', 'Microinteraction polish', 'One brand guideline file', 'Higgsfield generation', 'Editable Linearity brand/templates/MCP', 'Typography/icons/licences', 'Section-specific galleries', 'Mobbin/Refero flow study', 'Reference-driven critic loop', 'Five-agent design check', 'Glance-test simplicity variants', 'SlopMonster copy comparison', 'Evaluate simplified technical English', 'Original poster variations', 'Purposeful 3D website experiment', 'Searchable design/media library']
    }
]

for item in specs:
    src = root/'raw/inbox'/item['filename']
    h = digest(src)
    archive = root/'raw/sources/clips'/item['slug']
    archive.mkdir(parents=True, exist_ok=True)
    evidence = archive/'clip.md'
    if evidence.exists():
        assert digest(evidence) == h
    else:
        shutil.copyfile(src, evidence)
    assert digest(src) == digest(evidence) == h
    duplicates = [p.name for p in (root/'raw/inbox').glob('*.md') if p.name != src.name and p.stat().st_size == src.stat().st_size and digest(p) == h]
    item.update(hash=h, duplicates=duplicates)
    put(archive/'PROVENANCE.md', f"# Provenance\n\n- Title: {src.stem}\n- Creator: {item['author']}\n- URL: {item['url']}\n- Origin: `raw/inbox/{src.name}`\n- Original filename: `{src.name}`\n- Capture mechanism: Obsidian-style YouTube clip with description and timestamped transcript.\n- Publication and precise capture dates: unknown.\n- Original filesystem modification time (not publication/capture proof): {datetime.datetime.fromtimestamp(src.stat().st_mtime).isoformat()}\n- Archived: 2026-10-24\n- Size: {src.stat().st_size} bytes\n- SHA-256: `{h}`\n- Transformations: none; archive filename shortened to clip.md.\n- Exact inbox duplicates retained: {', '.join(duplicates) or 'none'}.\n- Coverage: full captured description/transcript through {item['end']}; original video and on-screen-only imagery/prompts not watched.\n")
    put(archive/'SHA256SUMS', f'{h}  clip.md\n')
    slug=item['slug']
    text=f"""---
type: source
subject: "{item['title']}"
created: 2026-10-24
updated: 2026-10-24
aliases: [{json.dumps(src.stem)}, {json.dumps(item['title'])}]
tags: [design, ai-workspace, llm-wiki]
sources:
  - ../../raw/sources/clips/{slug}/PROVENANCE.md
evidence: ../../raw/sources/clips/{slug}/clip.md
sha256: {h}
contradictions: []
---

# {item['title']}

## Source and coverage

- Creator: {item['author']}. [Original video]({item['url']}); publication date unknown.
- Capture date unknown; archived and ingested 2026-10-24.
- [Preserved clip](../../raw/sources/clips/{slug}/clip.md), [provenance](../../raw/sources/clips/{slug}/PROVENANCE.md), [hash manifest](../../raw/sources/clips/{slug}/SHA256SUMS).
- Read all captured description and transcript through {item['end']}. The original video, embedded screen demonstrations and linked prompt packs were not inspected. Claims below are attributed to the transcript, not current provider verification.

## What the source says

"""
    for heading, body in item['sections']:
        text+=f'### {heading}\n\n{body}\n\n'
    text+="## Application and limits\n\nFor the student dashboard, use concrete component references and a visible target, keep the approved charcoal/near-white system coherent, compare meaningful alternatives and inspect actual rendered motion. A clip does not justify adding every effect or tool. Joshua's existing voice and product decisions take priority over generic marketing prescriptions. These are application judgments, distinct from source claims.\n\n## Mentions in source\n\n"
    raw=src.read_text(encoding='utf-8')
    for q in item['quotes']:
        assert q in raw
        text+=f'> "{q}" (captured transcript)\n\n'
    text+='## Related knowledge\n\n- [Website planning and visitor decisions](../../references/website-design-planning.md)\n- [AI workspace hub](../../references/ai-workspace/index.md)\n- [Existing 25-tip readiness evaluation](../../research/2026-10-23-dashboard-design-readiness.md)\n- [Seven installed design skills](top-7-claude-design-skills-chase-ai.md)\n\n## Queue record\n\nEvery actionable suggestion is mapped individually in [batch coverage and queue proposals](../../research/2026-10-24-design-hub/ingest-a.md). Existing resources are distinguished from optional new evaluations. The coordinating agent owns queue IDs and design-hub integration; no installation or paid usage is implied.\n'
    put(root/'wiki/sources'/f'{slug}.md', text)
put(out/'ingest-a-data.json', json.dumps(specs,indent=2))
print(json.dumps([{k:v for k,v in s.items() if k in ['slug','hash','duplicates']} for s in specs],indent=2))
