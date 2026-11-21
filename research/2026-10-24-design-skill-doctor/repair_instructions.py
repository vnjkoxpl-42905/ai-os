from pathlib import Path
import hashlib,json,zipfile,datetime

root=Path('C:/Users/Joshu/dev/ai-os')
out=root/'research/2026-10-24-design-skill-doctor'
roots=[root/'skills/codex',root/'skills/claude',root/'.agents/skills',root/'.claude/skills',Path('C:/Users/Joshu/.agents/skills'),Path('C:/Users/Joshu/.codex/skills'),Path('C:/Users/Joshu/.claude/skills')]
families=['impeccable','high-end-visual-design','design-taste-frontend','react-bits']
changes=[]
patches={
'impeccable/SKILL.md':[
('node .agents/skills/impeccable/scripts/', 'node "<resolved-skill-directory>/scripts/'),
('load-context.mjs`','load-context.mjs"`'),
('load-context.mjs\n','load-context.mjs"\n'),
('pin.mjs <pin|unpin>','pin.mjs" <pin|unpin>'),
('Locate the installed skill and support directory before loading references.', 'Locate the installed skill and support directory before loading references. Replace `<resolved-skill-directory>` in commands with that absolute installed directory, quote paths containing spaces, and retain the target project as the command working directory. Preserve IMPECCABLE_CONTEXT_DIR when supplied.'),
('`$impeccable craft` has a user-confirmed shape brief for this task.', '`$impeccable craft` has a task brief supplied/approved by the user, or records choices the user explicitly delegated.'),
('Run `$impeccable shape` and wait for explicit brief confirmation.', 'Run `$impeccable shape`; ask only material questions not answered or delegated by the user.'),
('For `$impeccable craft`, `shape=pass` is only valid after a separate user response approving the shape design brief, or when the user provided an already-confirmed brief in the request. Do not mark `shape=pass` after writing PRODUCT.md, summarizing assumptions, or drafting an unconfirmed brief yourself.', 'For `$impeccable craft`, `shape=pass` is valid with a user-supplied/approved task brief or explicit user delegation of the remaining design decisions. Record which basis applies and the choices made. PRODUCT.md alone or an invented approval does not satisfy authorization. Ask only when a material scope or constraint remains unresolved outside that delegation.'),
],
'impeccable/reference/craft.md':[
('2. The shape design brief is explicitly confirmed by the user for this task, unless the user already provided a confirmed brief.', '2. A task-specific shape brief is supplied/approved by the user, or records the remaining design choices explicitly delegated by the user.'),
('PRODUCT.md and `teach` answers do **not** satisfy the shape gate. They are project context only. A compact self-authored brief does not satisfy the shape gate either. `shape=pass` requires a separate user response approving the shape brief or an already-confirmed brief supplied by the user.', 'PRODUCT.md and `teach` answers supply project context, not independent task authorization. Record the task brief and whether it is user-supplied, user-approved, or completed under explicit creative delegation. Do not invent approval or reopen settled decisions; ask only about material unresolved scope outside the delegation.'),
('1. Confirmed design brief from `shape`.', '1. Authorized task brief from `shape`, supplied/approved by the user or completed under explicit creative delegation.'),
('Wait for the design brief to be fully confirmed by the user before proceeding. The brief is your blueprint, and every implementation decision should trace back to it.', 'Use the existing supplied/approved brief, or record decisions made under explicit creative delegation and proceed. Ask for confirmation only when a material unresolved decision falls outside the authorized scope. Every implementation decision should trace back to this task brief.'),
('and explicit brief confirmation.', 'and the brief authorization basis.'),
],
'impeccable/reference/shape.md':[
('This is a required interaction, not optional guidance. Ask these questions in conversation, adapting based on answers. Don\'t dump them all at once; have a natural dialogue. STOP and use Codex\'s structured user-input/question tool when available; if unavailable, ask directly in chat to clarify what you cannot infer.', 'Discovery is required thinking, not a mandatory extra approval round. Reuse the user\'s supplied brief and prior answers. Where the user explicitly delegates creative decisions, make and record those choices. Ask only material unresolved questions outside that delegation, using the available question tool or chat.'),
('Discovery must include at least one user-answer round unless PRODUCT.md, DESIGN.md, or an already-confirmed brief directly answers the needed design inputs. With a sparse prompt, do **not** synthesize a complete brief for confirmation on the first response.', 'Discovery needs a user-answer round only when material design inputs remain unresolved outside the supplied brief, project context and explicit delegation. Do not invent facts or approval to fill a sparse prompt; distinguish delegated choices from unknown constraints.'),
('Always ask. Sketch quality and shipped quality are different outputs; don\'t guess between them.', 'Resolve scope from the current request and prior answers. Ask only if fidelity, breadth or delivery scope is materially unclear and not delegated.'),
('After the interview and any required probes, synthesize everything into a structured design brief. Present it to the user for explicit confirmation before considering this command complete. Stop after asking for confirmation; do not proceed to craft or implementation in the same response unless the user has already approved the brief.', 'After discovery and any required probes, synthesize a structured task brief and record its authorization basis: user-supplied, user-approved, or explicit creative delegation. Proceed within that basis when implementation is requested. Ask and stop only for material unresolved decisions outside the authorized scope.'),
('STOP and use Codex\'s structured user-input/question tool when available; if unavailable, ask directly in chat to clarify what you cannot infer. Ask for explicit confirmation of the brief before finishing. If the user disagrees with any part, revisit the relevant discovery questions. A shape run is incomplete until the brief is confirmed.', 'If a material unresolved decision falls outside the supplied brief or delegation, ask with the available question tool or chat and wait for that answer. Otherwise record the authorization basis and finish the brief without a redundant confirmation. If the user changes direction, revise the relevant decisions.'),
],
'high-end-visual-design/SKILL.md':[
('Build the DOM strictly using the "Double-Bezel" (Doppelrand) technique for all major cards, inputs, and feature grids. Use exaggerated squircle radii (`rounded-[2rem]`).', 'Use the selected component architecture. When the Double-Bezel technique fits the chosen direction, apply concentric shell/core radii; flat cards, inputs and grids remain valid. Preserve the project design system.'),
('All major cards and containers use the Double-Bezel nested architecture (outer shell + inner core)', 'Double-Bezel nesting is used only where selected and useful; flat containers remain valid and radii follow the project system'),
('Scroll entry animations are present — no element appears statically', 'Scroll entries follow the selected motion direction; reduced-motion and no-animation paths retain readable, accessible content'),
('transition-all duration-700','transition-[transform,opacity] duration-700'),
],
'design-taste-frontend/SKILL.md':[
('**TECHNICAL UI RULE:** Serif fonts are strictly BANNED for Dashboard/Software UIs. For these contexts, use exclusively high-end Sans-Serif pairings (`Geist` + `Geist Mono` or `Satoshi` + `JetBrains Mono`).', '**TECHNICAL UI DEFAULT:** Sans-serif pairings (`Geist` + `Geist Mono` or `Satoshi` + `JetBrains Mono`) suit many dense software surfaces. Editorial serif headings are valid when selected in the brief or existing system; preserve legibility and hierarchy.'),
('Use EXCLUSIVELY Framer Motion\'s `useMotionValue` and `useTransform` outside the React render cycle to prevent performance collapse on mobile.', 'Use the project\'s selected animation engine outside the React render cycle, such as Motion values or GSAP setters/tweens. Avoid competing engines controlling the same element properties.'),
('When `MOTION_INTENSITY > 5`, embed continuous, infinite micro-animations (Pulse, Typewriter, Float, Shimmer, Carousel) in standard components (avatars, status dots, backgrounds). Apply premium Spring Physics (`type: "spring", stiffness: 100, damping: 20`) to all interactive elements—no linear easing.', 'When motion is selected, consider continuous micro-animations only if they help the chosen experience. A high intensity dial does not require infinite loops. Supply static reduced-motion equivalents, pause offscreen loops, and choose easing suited to the interaction rather than forcing springs onto every element.'),
('Always utilize Framer Motion\'s `layout` and `layoutId` props for smooth re-ordering, resizing, and shared element transitions across state changes.', 'Use the selected engine for purposeful layout transitions, such as Motion layout/layoutId or GSAP Flip when available. Do not introduce a second engine solely to follow this preset.'),
('`transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1)`', '`transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1)`'),
('**Serif Constraints:** Use Serif fonts ONLY for creative/editorial designs. **NEVER** use Serif on clean Dashboards.', '**Serif Choice:** Editorial serif headings can suit dashboards when selected by the brief. Prefer legible type for dense data and retain the project\'s established typography.'),
('**CRITICAL:** Never mix GSAP/ThreeJS with Framer Motion in the same component tree. Default to Framer Motion for UI/Bento interactions. Use GSAP/ThreeJS EXCLUSIVELY for isolated full-page scrolltelling or canvas backgrounds, wrapped in strict useEffect cleanup blocks.', '**ENGINE CHOICE:** Preserve the project\'s selected engine. GSAP is valid for UI transitions as well as scrolltelling; Motion is an alternative where already selected. ThreeJS handles appropriate canvas work. Isolate ownership so engines never animate the same properties concurrently; clean up timelines, listeners and render loops on teardown.'),
('Use the following Framer Motion principles:', 'Use the selected engine; the following Motion APIs are examples only when Motion is already chosen:'),
],
'react-bits/SKILL.md':[
('## Fetch\n','## Fetch\n\nResolve `<resolved-skill-directory>` to this installed skill\'s absolute directory. Keep the target application as the working directory so `--dest` stays app-relative. Quote the helper path when it contains spaces. Catalog refresh writes this skill\'s catalog, not the application.\n'),
('node scripts/rb-add.mjs', 'node "<resolved-skill-directory>/scripts/rb-add.mjs"'),
('node scripts/gen-catalog.mjs', 'node "<resolved-skill-directory>/scripts/gen-catalog.mjs"'),
]}

stamp=datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
backup=out/f'instruction-backup-{stamp}.zip'
with zipfile.ZipFile(backup,'w',zipfile.ZIP_DEFLATED) as z:
 for base in roots:
  for relative,rules in patches.items():
   p=base/relative
   if not p.is_file() or p.is_symlink() or any(x.is_symlink() for x in [p.parent,p.parent.parent]): continue
   old=p.read_bytes(); text=old.decode('utf-8-sig'); normalized=text.replace('\r\n','\n')
   updated=normalized
   hits=[]
   for source,target in rules:
    n=updated.count(source)
    if n: updated=updated.replace(source,target); hits.append({'source':source,'count':n})
   if updated==normalized: continue
   new=updated.replace('\n','\r\n').encode('utf-8') if b'\r\n' in old else updated.encode('utf-8')
   archive=p.as_posix().replace(':','')
   z.writestr(archive,old)
   if p.read_bytes()!=old: raise RuntimeError(f'Concurrent change: {p}')
   p.write_bytes(new)
   changes.append({'path':str(p),'before':hashlib.sha256(old).hexdigest(),'after':hashlib.sha256(new).hexdigest(),'replacements':hits})
(out/'instruction-repair-receipts.json').write_text(json.dumps({'backup':str(backup),'changes':changes},indent=2),encoding='utf-8')
print(json.dumps({'backup':str(backup),'changed_files':len(changes),'paths':[x['path'] for x in changes]},indent=2))
