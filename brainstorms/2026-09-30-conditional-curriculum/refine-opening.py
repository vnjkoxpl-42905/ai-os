from pathlib import Path

repo = Path('C:/Users/Joshu/dev/ai-os-projects/lsatu-conditional-bootcamp')
p = repo / 'src/bootcamps/conditionals/components/ConditionalOpeningLesson.tsx'
s = p.read_text(encoding='utf-8')
s = s.replace('export function ConditionalOpeningLesson({ unit, onComplete, continueHref, previousHref, reviewed }: ConditionalLessonNoteProps) {', 'export function ConditionalOpeningLesson({ unit, onComplete, continueHref, previousHref, reviewed }: ConditionalLessonNoteProps) {\n  const [motionPaused, setMotionPaused] = useState(false);')
s = s.replace('className="conditional-note co-opening"', 'className="conditional-note co-opening" data-motion-paused={motionPaused}')
s = s.replace('<div className="co-hero-orbit" aria-hidden="true">', '<button type="button" className="co-motion-toggle" aria-pressed={motionPaused} onClick={() => setMotionPaused(!motionPaused)}>{motionPaused ? \'Resume motion\' : \'Pause motion\'}</button><div className="co-hero-orbit" aria-hidden="true">')
s = s.replace('These lesson activities give immediate feedback. They do not record a drill attempt or a mastery score.', 'Use these examples to learn the relationship. Your skill drill is a separate set.')
s = s.replace('Anyone inside must have an electric vehicle.', 'Every permitted vehicle must be electric.')
p.write_text(s, encoding='utf-8')
p = repo / 'src/bootcamps/conditionals/routes.tsx'
s = p.read_text(encoding='utf-8')
s = s.replace('label: `${levelLabel(difficulty)} skill drill: ${unit.title}`', 'label: `Skill drill: ${unit.title}`')
s = s.replace('`3. Skill drill · ${levelLabel(selection.difficulty)}`', "'3. Skill drill'")
s = s.replace('Next action: {levelLabel(selection.difficulty)} skill drill', 'Next action: skill drill')
p.write_text(s, encoding='utf-8')
p = repo / 'src/bootcamps/conditionals/routes.test.tsx'
s = p.read_text(encoding='utf-8').replace('Next action: Level 3 skill drill', 'Next action: skill drill')
p.write_text(s, encoding='utf-8')
