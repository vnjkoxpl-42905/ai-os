from pathlib import Path
import hashlib, json, re

ROOT=Path(__file__).resolve().parents[2]
DATE='2026-10-24'
items=[
dict(pattern='Build $10,000 Website*',slug='astra-website-design-loop-jack',title='References, a design loop and editable website controls',author='Jack (surname unknown in clip)',url='https://www.youtube.com/watch?v=xqCdvm-YoIM',
 claims=[
 'At 0:53–2:07 the narrator starts from reference sites and a mood board. The description lists mobile, animation, navbar, CTA and component galleries. Names differ between the description and automatic transcript, so these are leads to check, not verified URLs.',
 'At 2:07–5:25 he recommends a Design Loop skill, design references and image/video generation through a Higgsfield plugin. He explicitly could not validate which native image model his Codex attempt used (3:52).',
 'At 5:25–7:35 he describes an iterative multi-agent design loop and shows websites at several screen sizes. His satisfaction with the output is subjective, not a controlled comparison.',
 'At 7:35–12:19 he proposes a website operating system: device previews, palette and typography controls, an asset inventory, direct copy edits, image/video regeneration, a prose-review tool and editable SEO metadata. The intent is to avoid rebuilding a whole page for every minor edit.',
 'At 8:45 he calls finding a specific replacement component on 21st.dev UI sniping. At 7:08 he discusses converting still imagery into short looping video; neither is a requirement to animate every dashboard element.'
 ],quotes=[('a website is only as good as the references and the images that you actually give it.','0:31'),('UI sniping','8:45'),('edit more without having to rebuild everything at the same time.','12:00')],
 relevance='The useful transfer is a reusable visual reference library and cheap, narrowly scoped refinement controls. For the student dashboard, direct task access and legible content remain the goal; an asset generator or SEO editor is a separate authoring feature.',
 actions=['Maintain categorized visual references with explicit reasons for selection (overlaps the requested design hub).','Evaluate the promoted Design Loop skill before installation; its linked guide was not retrieved in this ingest.','Evaluate lightweight palette/type/spacing controls and replayable previews on a prototype rather than rebuilding for each adjustment.','Evaluate a small editable content/asset/metadata panel only if repeated maintenance justifies it.','Inspect plugin/model identity and generation cost before adopting Higgsfield asset generation; do not assume source claims prove access.','Compare any promoted prose checker with the existing humanizer instead of installing a duplicate.'],
 limitations='The preserved input contains the description and transcript through 12:19, not the actual rendered websites or linked skill source. Revenue, pricing, model names, plugin capabilities and performance claims were not independently verified. No images, video frames or linked products were inspected during this text ingestion.'),
 dict(pattern='GPT 6 Astra + Blender*',slug='astra-blender-web-design-chase-ai',title='Prototype a 3D concept before building it in Blender',author='Chase AI',url='https://www.youtube.com/watch?v=RhGiG-yZP-c',
 claims=[
 'Step zero (1:02) names Blender, Blender Agent Studio and a Blender-to-web skill as prerequisites. The narrator says a companion repository holds prompts, but the saved description does not provide its exact URL.',
 'At 1:55–3:39 he first generates multiple image concepts, selects an aesthetic, and only then uses it as a Blender reference. This reduces the cost of exploring geometry in the 3D tool.',
 'At 4:05–5:14 he uses scripted Blender work, inspects and iterates, then previews a Three.js version in a stand-in hero. The claimed 12 minute 40 second build is one narrated run.',
 'At 6:13–8:20 he distributes one interactive asset through a page narrative rather than leaving it isolated in a hero. Page mockups precede full implementation.',
 'At 6:51 and 8:38–9:24 he recommends a static mobile alternative, download-size measurement, hardware-level checks and pausing rendering when offscreen. The model-hosting feature is presented for sharing a prototype, not production.'
 ],quotes=[('we want to use Astra to create just some images','1:55'),('making sure we pause rendering when it\'s offscreen','8:57'),('Is this just a visual spectacle or does this actually work?','8:38')],
 relevance='Concept-first exploration and performance budgets transfer directly to dashboard polish. Real-time 3D is optional and should earn its place through useful student feedback or information, rather than becoming a decorative prerequisite.',
 actions=['If interactive 3D is desired, locate and inspect the exact companion repository and skill licence before installing Blender Agent Studio/Blender-to-web.','Prototype multiple still concepts before committing to a 3D build.','For any accepted 3D component, measure transfer size, pause offscreen rendering, test weaker hardware and supply a mobile/static fallback.','Keep prototype sharing distinct from production hosting.'],
 limitations='Full captured transcript through 10:26 was read. No Blender file, repository implementation, rendered asset or licence was inspected. Tool/model claims and build times remain attributed demonstrations, not current capability verification.'),
 dict(pattern='This New Astra Web Design Workflow*',slug='astra-web-design-taste-vault-chase-ai',title='Use a taste vault, compare design families, then refine one direction',author='Chase AI',url='https://www.youtube.com/watch?v=XK6S1hbYv7I',
 claims=[
 'At 1:53–4:01 he collects screenshots into a taste vault grouped by design family. References include Pinterest, Twitter, Landbook and Dribbble. Specific visual examples replace vague adjectives.',
 'At 4:49–7:43 he compares several design families and separately compares baseline output with frontend-design, Impeccable and Taste. His demonstration uses five families times four skill configurations, not a mandated count for every project.',
 'At 8:22–11:25 he says baseline output also looked strong to him. He chooses a family, asks for distinct variations within it, and only then moves to small edits. The point is to judge visible output rather than assume more skills always improve it.',
 'At 13:17–15:23 he adds a customizable tweak panel for typography, imagery, grid, accent, footer and motion settings, with save/reset, entrance replay and comparison against an untouched original.',
 'At 15:54–17:24 he browses specific components on 21st.dev and adapts a component aesthetic across a coherent page. At 17:24–18:20 he describes temporary hosted sharing, explicitly distinguishing it from production.'
 ],quotes=[('I just call it my taste vault.','2:03'),('I want to make three variations within that particular direction.','11:25'),('You need to figure out your own style','19:20')],
 relevance='This closely supports the requested design folder: keep visual examples, reasons, sources and design-family labels together while linking to existing skills and repos. It does not justify overriding Joshua’s accepted charcoal palette or generating twenty versions by default.',
 actions=['Create the requested navigable taste/reference library with screenshots, family tags, selection reasons and provenance.','Compare a small number of meaningfully different compositions, then refine the chosen family rather than endlessly switching themes.','Retain an untouched baseline and add optional tweak controls/replay for efficient comparison.','Browse actual component demonstrations and adapt them to a coherent design instead of accumulating unrelated widgets.','Existing Taste, Impeccable and frontend-design availability should be checked before proposing another installation.'],
 limitations='Full captured transcript through 19:51 was read. No screenshots from the demonstration, pinned repository, live skill star counts, model pricing or hosting claims were verified. The skill comparison is the narrator’s informal aesthetic preference, not a benchmark.'),
 dict(pattern='Dear Higgsfield,*',slug='higgsfield-clone-albert-olgaard',title='A narrated video-generation wrapper build is not proof of a finished platform',author='Albert Olgaard (@albertolgaard in description)',url='https://www.youtube.com/watch?v=hRr-yUSM0_A',
 claims=[
 'The narrator proposes a niche video-generation service using an existing API and open-source starting code. At 0:04 he claims Higgsfield open-sourced part of its code, but the clip supplies no direct upstream repository to verify that attribution.',
 'At 1:52–3:30 he gives a long prompt to Claude, then configures provider/storage/database/authentication secrets. The introduction says one hour, the prompt discussion estimates one to two hours, and the completed-run discussion says three hours and $100 at API pricing; those are internally varying estimates, not reliable planning guarantees.',
 'At 4:41–5:59 the first generation fails. Adding API credit does not immediately fix it; the narrator asks the agent to inspect logs and reports a credit-pricing fix before a successful generation.',
 'At 6:00–7:20 he tours effects, community, pricing, billing, admin, image and video screens. Seeing these screens does not establish production security, billing correctness or completeness.',
 'At 7:20–9:31 he recommends changing the visual identity and specializing in a narrow user task rather than competing with a general platform. Pricing and margin checks are presented as necessary before launch.'
 ],quotes=[('before we launch this','6:50'),('focus on one specific niche','7:20'),('the most important thing to consider is the pricing.','8:08')],
 relevance='The design-relevant lesson is to organize a product around one specific user need and inspect the actual interaction/error path. This clip is mostly a commercial wrapper walkthrough, not evidence that a new component library or model should be installed for the student home.',
 actions=['If evaluating the supplied open-source starter, first resolve its actual repository, upstream ownership and licence; the saved link points to a community page.','If evaluating a niche generation tool, test generation, pricing/error recovery and real unit economics separately from screen appearance.','Check the existing Higgsfield integration before adding another provider path; keep credentials outside knowledge pages.','Treat the linked build prompt as a reference to inspect, not a command to execute or a mandate to clone branding.'],
 limitations='Full captured transcript through 10:10 was read. No source code, billing system, provider account or generated media was checked. Revenue, valuation, market-size, discount and model-capability assertions remain unverified source claims. This ingest authorizes neither API spending nor installation.'),
 dict(pattern='This Viral Open Source Repo Lets Claude*',slug='rea-feature-investigation-chase-ai',title='REA investigation should produce claims with evidence, not a magical clone',author='Chase AI',url='https://www.youtube.com/watch?v=o8LjTSvza0E',
 claims=[
 'At 0:00–2:56 the narrator presents REA as a tool-routing/MCP framework for studying different application types and producing a customized implementation. He uses Wispr Flow (transcribed Whisper Flow) as an example.',
 'At 3:00 he labels investigation claims seen, inferred or unknown, attaching code evidence where available.',
 'At 3:30–5:54 he separates an Electron application from a native helper and routes them to JavaScript analysis versus a Ghidra-backed binary analysis. Narrated timing/function counts are one informal example.',
 'At 6:26–8:38 he describes a question-answer evidence loop followed by a rebuild plan. He also notes the agent sometimes searches accessible JavaScript directly instead of requiring REA for every question.',
 'The final recommendation is customization for a particular use case rather than merely copying software already available. Star counts and universal capability language are promotional, not independently verified in this ingest.'
 ],quotes=[('seen, inferred, or unknown.','3:00'),('a fact and a receipt.','6:26'),('specific tools for all these different types of applications','8:10')],
 relevance='For UI inspiration, capture a specific behavior, inspect what is actually visible and explain what remains unknown. Binary decompilation is not necessary for a calendar strip or question-picker layout. This source complements the existing Nick Saraev REA summary without replacing its earlier caveats.',
 actions=['Add this source to existing REA evaluation/activation work rather than create a competing install task.','For a chosen reference behavior, make a short seen/inferred/unknown evidence ledger before implementing.','Route by application type; use accessible web/JavaScript inspection when that already answers the question.','Validate the rebuilt behavior with concrete interaction tests rather than declaring a clone from a screenshot.'],
 limitations='Full captured transcript through the final 8:38 paragraph was read; its last words are visibly cut off. No REA run, binary analysis or Wispr Flow implementation was reproduced. The exact app-name spelling is uncertain in the transcript. Earlier Nick Saraev operational status is dated 2026-10-12/13 and must not be treated as current installation state.'),
 dict(pattern='I Tested the Viral Reverse Engineer Anything*',slug='rea-output-first-workflow-nate-herk',title='Nate Herk: investigate a narrow feature and test the rebuilt behavior',author='Nate Herk',url='https://www.youtube.com/watch?v=rL5tw6h78zo',
 claims=[
 'At 1:06–2:55 he derives a desired style or workflow from concrete examples, including frame-by-frame motion analysis. References act as a more specific target than a generic request.',
 'At 3:22–4:54 he distinguishes recreating useful behavior from copying exact UI or an entire hosted service. His Loom-inspired recorder saves locally rather than reproducing Loom cloud infrastructure.',
 'At 7:36–10:58 his five-step approach is: pick one feature; route investigation by build type; read a saved summary before traces; mark findings seen/inferred/unknown; rebuild and test. Reusing the summary avoids rerunning very large analyses.',
 'At 9:48 he warns against building on inferred claims as though they were facts. At 10:58–12:27 he limits inspection to accessible/local evidence, warns against copying exact code/assets and says results depend on the model and setup.',
 'At 4:54 he promotes ScrollCraft for scroll-driven animations, layering, typography, spacing, depth and taste. This is a separate resource mention, not proof it outperforms existing GSAP/design skills.',
 'At 12:56–14:29 he reports better but slower results in his own REA comparison and extends the reference-first method to day-to-day processes and skills. This is an informal observation, not a benchmark.'
 ],quotes=[('It\'s easier to pick out features.','7:36'),('seen, inferred, or unknown.','9:23'),('you should never be copying exact code or assets.','10:58')],
 relevance='This strengthens a practical design-reference workflow: inspect a particular picker, calendar or transition, save concise observations, and compare the rebuilt interaction with that target. It supports studying motion visually, not merely accumulating still screenshots.',
 actions=['Use existing ScrollCraft plus GSAP skills where relevant rather than install a duplicate from the promoted link.','Select a specific reference behavior; save its evidence summary with seen/inferred/unknown labels and test criteria.','Reuse saved investigation summaries rather than rerun large analysis files.','Compare source and rebuilt behavior visually and interactively; keep screen appearance separate from functionality.','If REA itself is useful, attach this evidence to the existing evaluation item and verify present setup before installation.'],
 limitations='Full captured transcript through 14:29 was read. No actual reference video, frame sequence, app internals, REA repository or ScrollCraft implementation was inspected in this text-ingest pass. Model names, changing star counts and quality/speed comparisons are attributed source claims only.')
]

def digest(b):return hashlib.sha256(b).hexdigest()
def write_new(p,txt):
 p.parent.mkdir(parents=True,exist_ok=True)
 if p.exists():
  if p.read_text(encoding='utf-8')==txt:return
  raise RuntimeError(f'Refuse overwrite existing file: {p}')
 with p.open('x',encoding='utf-8',newline='\n') as f:f.write(txt)

results=[]
for item in items:
 matches=list((ROOT/'raw/inbox').glob(item['pattern']))
 assert len(matches)==1,(item['pattern'],matches)
 src=matches[0]; data=src.read_bytes(); sha=digest(data)
 arc=ROOT/'raw/sources/clips'/item['slug']; arc.mkdir(parents=True,exist_ok=True)
 evidence=arc/'source.md'
 if evidence.exists():assert evidence.read_bytes()==data
 else:
  with evidence.open('xb') as f:f.write(data)
 assert digest(evidence.read_bytes())==sha
 prov=f'''# Provenance\n\n- Original filename: `{src.name}`\n- Origin: `raw/inbox/{src.name}`\n- URL: {item['url']}\n- Author: {item['author']}\n- Publication date: unknown in captured bytes.\n- Capture date: unknown; filesystem times are not publication/capture proof.\n- Archived: {DATE}\n- Capture mechanism: existing Markdown clip containing video description and transcript. Original capture tooling unknown.\n- Archived file: `source.md`\n- Bytes: {len(data)}\n- SHA-256: `{sha}`\n- Transformations: none. Original bytes preserved; concise summary is a separate artifact.\n- Coverage: complete captured text read. Thumbnail/video link is not visual verification of the video.\n'''
 write_new(arc/'PROVENANCE.md',prov)
 write_new(arc/'SHA256SUMS',f'{sha}  source.md\n')
 title=src.stem
 fm=f'''---\ntype: source\nsubject: {json.dumps(item['title'])}\ncreated: {DATE}\nupdated: {DATE}\naliases: [{json.dumps(title)}]\ntags: [design, ai-workspace, source]\nevidence: ../../raw/sources/clips/{item['slug']}/source.md\nsha256: {sha}\nsources:\n  - ../../raw/sources/clips/{item['slug']}/PROVENANCE.md\ncontradictions: []\n---\n\n# {item['title']}\n\n**Source:** {title}. Author: {item['author']}. [Original video]({item['url']}). Publication and capture dates unknown. Ingested {DATE}.\n\n**Evidence:** [preserved complete clip](../../raw/sources/clips/{item['slug']}/source.md), [provenance and hash](../../raw/sources/clips/{item['slug']}/PROVENANCE.md). Status: captured and text-compiled, not independently tested.\n\n## What the source says\n\n'''
 fm+='\n\n'.join('- '+x for x in item['claims'])
 fm+='\n\n## Application here, separated from source claims\n\n'+item['relevance']
 fm+='\n\n## Actionable proposals\n\n'+'\n'.join('- '+x for x in item['actions'])
 fm+='\n\nQueue disposition is coordinated in the [batch report](../../research/2026-10-24-design-hub/ingest-b.md). These proposals are not installations, approvals or production changes.\n\n## Mentions in source\n\n'
 raw=data.decode('utf-8-sig')
 for quote,stamp in item['quotes']:
  assert quote in raw,(title,quote)
  fm+=f'> "{quote}" ({stamp})\n\n'
 fm+='## Limits and conflicts\n\n'+item['limitations']+' No unresolved factual contradiction was established; differences in opinion or demonstration outcomes are not contradictions.\n\n'
 fm+='Related: [website planning](../../references/website-design-planning.md), [AI workspace hub](../../references/ai-workspace/index.md).'
 if 'rea-' in item['slug']:fm+=' [Earlier Nick Saraev REA source](reverse-engineer-anything-rea.md).'
 fm+='\n'
 out=ROOT/'wiki/sources'/f"{item['slug']}.md"
 write_new(out,fm)
 assert src.read_bytes()==data
 results.append({'title':title,'sha256':sha,'source':str(out.relative_to(ROOT)),'archive':str(evidence.relative_to(ROOT)),'actions':item['actions']})
write_new(ROOT/'research/2026-10-24-design-hub/ingest-b-results.json',json.dumps(results,indent=2))
print(json.dumps([{'title':x['title'],'source':x['source'],'sha256':x['sha256']} for x in results],indent=2))
