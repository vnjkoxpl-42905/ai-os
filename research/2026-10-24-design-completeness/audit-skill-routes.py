from pathlib import Path
import os,re,json,hashlib,collections,sys

VAULT=Path('C:/Users/Joshu/dev/ai-os')
HOME=Path('C:/Users/Joshu')
ROOTS=[('catalog-claude',VAULT/'skills/claude'),('catalog-codex',VAULT/'skills/codex'),('project-codex',VAULT/'.agents/skills'),('project-claude',VAULT/'.claude/skills'),('home-agents',HOME/'.agents/skills'),('home-codex',HOME/'.codex/skills'),('home-claude',HOME/'.claude/skills'),('plugin-codex',HOME/'.codex/plugins/cache'),('plugin-claude',HOME/'.claude/plugins/cache')]
SKIP={'node_modules','.git','.venv','venv','__pycache__','_snapshots'}
PRIMARY=re.compile(r'\b(?:design|typography|color palette|colour palette|visual|frontend|front-end|interface|animation|gsap|scroll|motion|canvas|figma|shadcn|react.bits|hyperframes|remotion|impeccable|image.to.code|imagegen|image generation|artwork|illustration)\b',re.I)
SUPPORT=re.compile(r'\b(?:browser|playwright|devtools|webapp.testing|web application.*test|web.app.*build|build.web.app|component librar|screenshot|accessibility|site.teardown|firecrawl|tavily|web research|ux|ui)\b',re.I)
GENERAL_EXCLUDE=re.compile(r'\b(?:email|consultation|session recap|payment|accommodations|student transcript|gmail|seo|keyword|link.prospect|video.transcri)\b',re.I)
GENERAL_NAMES=set('api-and-interface-design codebase-design design-an-interface documentation-and-adrs build-mcp-server create-cowork-plugin fix-finding metric-pack-designer build-business-case plan-deal-strategy sales-leadership-dashboard seller-account-dashboard metronome assign-lsatu-work audit notebooklm reverse-engineer-anything supabase-postgres-best-practices openai-platform-api-key artifact-template-system-design artifact-template-design-report update-plugin writing-great-skills lsat-lab-transcribe lsat-lab-question-features lsat-lab-set-builder facebook-consultation-requests lsatu-cc-handoff lsat-u-architecture grill-me grill-with-docs brainstorming improve-codebase-architecture handoff loop-me troubleshooting memory-leak-debugging firecrawl-company-directories firecrawl-competitive-intel firecrawl-dashboard-reporting firecrawl-knowledge-base firecrawl-knowledge-ingest firecrawl-lead-gen firecrawl-lead-research firecrawl-market-research firecrawl-monitor firecrawl-research-papers firecrawl-seo-audit firecrawl-shop'.split())
PRIMARY_NAMES=set('algorithmic-art brand-guidelines theme-factory higgsfield-generate higgsfield-marketplace-cards higgsfield-product-photoshoot higgsfield-soul-id higgsfield-websites sites sites-remix visualize playground'.split())
SUPPORT_NAMES=set('research-synthesis react-best-practices expo-dom expo-router expo-web-to-native appkit-interop swiftui-patterns view-refactor presentations pptx docx google-slides gws-slides template-creator remotion-best-practices remotion-docs remotion-create remotion-render remotion-studio remotion-upgrade'.split())

def classify(name,meta,path):
    primary=PRIMARY.search(meta);support=SUPPORT.search(meta)
    if name in GENERAL_NAMES:
        if name=='audit' and ('product-design' in path or 'capturing screenshots first' in meta):return 'primary','Product Design visual and UX audit, distinct from AI OS audit'
        return 'general','Metadata reviewed: operational, architecture, commercial or general workflow; not a design skill'
    if name in PRIMARY_NAMES:return 'primary','Metadata and workflow reviewed: visual creation, themes, brand styling or website design'
    if name in SUPPORT_NAMES:return 'supporting','Metadata reviewed: direct research, component implementation, visual authoring or preview support'
    if primary:return 'primary','Descriptive metadata identifies visual/UI/motion purpose: '+primary.group(0)
    if support:return 'supporting','Descriptive metadata identifies direct design-tool support: '+support.group(0)
    return 'general','Metadata reviewed: no design or direct design-tool purpose'

def metadata(text):
    if text.startswith('---'):
        end=text.find('\n---',3)
        if end!=-1:return text[3:end]
    return '\n'.join(text.splitlines()[:35])

def gather():
    rows=[]
    for kind,base in ROOTS:
        if not base.exists():continue
        for directory,dirs,files in os.walk(base,followlinks=False):
            dirs[:]=[d for d in dirs if d not in SKIP]
            if 'SKILL.md' not in files:continue
            p=Path(directory)/'SKILL.md'
            try:
                data=p.read_bytes(); txt=data.decode('utf-8-sig');meta=metadata(txt)
                # Classify on actual descriptive metadata, never directory name alone.
                cls,reason=classify(p.parent.name,meta,p.as_posix())
                readonly=kind.startswith('plugin') or 'synced' in p.parts or '.system' in p.parts or p.is_symlink() or any(x.is_symlink() for x in p.parents if x!=base.parent)
                rows.append(dict(path=p.as_posix(),root=kind,name=p.parent.name,classification=cls,reason=reason,metadata=meta,sha256=hashlib.sha256(data).hexdigest(),readonly=readonly,editable=not readonly,routed='design/README.md' in txt,route='existing' if 'DESIGN DOMAIN ROUTER' in txt or 'design/README.md' in txt else 'missing'))
            except Exception as e:rows.append(dict(path=p.as_posix(),root=kind,error=str(e),classification='unreadable'))
    return rows

if __name__=='__main__':
    rows=gather()
    if '--apply' in sys.argv:
        for row in rows:
            if row['classification'] not in ('primary','supporting'):continue
            if row['readonly']:
                row['route']='companion-registry';continue
            if row['routed']:continue
            p=Path(row['path']);before=p.read_bytes()
            if hashlib.sha256(before).hexdigest()!=row['sha256']:
                row['route']='concurrent-change-skipped';continue
            newline=b'\r\n' if b'\r\n' in before else b'\n'
            lines=['','<!-- BEGIN GENERATED DESIGN HUB ROUTE -->','For design work, first read the shared Claude Code/Codex design hub at','`C:/Users/Joshu/dev/ai-os/design/README.md` for relevant principles, sources,','skills, repositories and research. Keep this skill in its required runtime home.','<!-- END GENERATED DESIGN HUB ROUTE -->','']
            addition=newline.join(line.encode('utf-8') for line in lines)
            after=before+addition
            p.write_bytes(after)
            check=p.read_bytes()
            row.update(routed=True,route='appended-generated-pointer',before_sha256=row['sha256'],sha256=hashlib.sha256(check).hexdigest(),preserved_original_bytes=check[:len(before)]==before)
    dest=VAULT/'research/2026-10-24-design-completeness/skills.json'
    dest.write_text(json.dumps(dict(roots=[dict(kind=k,path=p.as_posix()) for k,p in ROOTS],records=rows),indent=2,ensure_ascii=False),encoding='utf-8')
    print(json.dumps(dict(total=len(rows),counts=dict(collections.Counter(r['classification'] for r in rows)),unique_relevant_names=sorted({r['name'] for r in rows if r['classification'] in ('primary','supporting')})),indent=2))
