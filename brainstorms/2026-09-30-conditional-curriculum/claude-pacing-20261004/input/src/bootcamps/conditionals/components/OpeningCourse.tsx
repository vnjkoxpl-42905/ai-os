import { useEffect, useRef, useState, type ReactNode } from 'react';
import { Link } from 'react-router-dom';
import { ArrowLeft, ArrowRight, BookOpen, Bookmark, Dumbbell, Menu, Sparkles } from 'lucide-react';
import { PageHeader } from '@/bootcamps/main-conclusion/components/primitives/PageHeader';
import { Sheet, SheetContent, SheetTitle, SheetTrigger } from '@/components/ui/sheet';
import { OPENING_COURSE_PATH, openingCourseStep, type OpeningCourseStep } from '../openingCoursePath';
import { OpeningCourseContent } from './OpeningCourseContent';
import { StudyDeck } from './StudyDeck';
import './opening-course.css';

export type OpeningCourseUrl = (destination: string, run?: boolean) => string;

export function OpeningCourseNavigation({ view, url }: { view: string; url: OpeningCourseUrl }) {
  const [open, setOpen] = useState(false);
  const focusDestination = useRef(false);
  function closeForNavigation() { focusDestination.current = open; setOpen(false); }
  const navigation = <nav aria-label="Conditional course">
    <p>Intro path</p><Link aria-current={view === 'lessons' || !!openingCourseStep(view) ? 'page' : undefined} to={url('lessons')} onClick={closeForNavigation}><BookOpen size={18}/>Lessons</Link>
    <p>Practice</p><Link aria-current={view === 'practice' ? 'page' : undefined} to={url('practice')} onClick={closeForNavigation}><Sparkles size={18}/>Practice Drills</Link>
    <Link aria-current={view === 'labs' ? 'page' : undefined} to={url('labs')} onClick={closeForNavigation}><Dumbbell size={18}/>Drill Lab</Link>
    <p>Tools</p><Link aria-current={view === 'tools' ? 'page' : undefined} to={url('tools')} onClick={closeForNavigation}><Bookmark size={18}/>Flashcards</Link>
  </nav>;
  return <>
    <aside className="oc-course-rail"><Link className="oc-back" to="/classroom"><ArrowLeft size={15}/>Classroom</Link><div className="oc-brand">Conditional logic</div>{navigation}</aside>
    <div className="oc-mobile-nav"><Link to={url('lessons')}>Conditional logic</Link><Sheet open={open} onOpenChange={setOpen}><SheetTrigger asChild><button type="button"><Menu size={18}/>Course menu</button></SheetTrigger><SheetContent side="left" className="oc-course-drawer" aria-describedby={undefined} onCloseAutoFocus={event => {
      if (!focusDestination.current) return;
      event.preventDefault();
      focusDestination.current = false;
      requestAnimationFrame(() => {
        const heading = document.querySelector<HTMLElement>('.oc-course-screen [data-course-heading] h1');
        if (heading) { heading.tabIndex = -1; heading.focus({ preventScroll: true }); }
      });
    }}><SheetTitle>Conditional logic</SheetTitle>{navigation}</SheetContent></Sheet></div>
  </>;
}

function CourseCard({ step, url }: { step: OpeningCourseStep; url: OpeningCourseUrl }) {
  return <li className="oc-path-card"><span className="oc-label">{step.type}</span><h2>{step.title}</h2><p>{step.description}</p><Link className="oc-action" to={url(step.id)}>{step.type === 'note' ? <BookOpen size={16}/> : <Dumbbell size={16}/>} {step.type === 'note' ? 'Read lesson' : 'View drill'}<ArrowRight size={16}/></Link></li>;
}

export function OpeningCourseScreen({ view = 'lessons', run = false, url, steps = OPENING_COURSE_PATH, recordedPractice }: {
  view?: string; run?: boolean; url: OpeningCourseUrl; steps?: OpeningCourseStep[]; recordedPractice?: ReactNode;
}) {
  const current = steps.find(step => step.id === view);
  const [visited, setVisited] = useState<string[]>([]);
  const root = useRef<HTMLDivElement>(null);
  useEffect(() => {
    if (current && (current.type === 'note' || run)) setVisited(prior => prior.includes(view) ? prior : [...prior, view]);
    requestAnimationFrame(() => {
      const heading = root.current?.querySelector<HTMLElement>('[data-course-heading] h1');
      if (heading) heading.tabIndex = -1;
      heading?.focus({ preventScroll: true });
      heading?.scrollIntoView?.({ block: 'start', behavior: 'instant' });
    });
  }, [view, run, current]);
  const index = steps.findIndex(step => step.id === view);
  const prior = steps[index - 1];
  const next = steps[index + 1];
  const list = view === 'labs' || view === 'practice' ? steps.filter(step => step.type === 'drill') : steps;
  const isIndex = ['lessons', 'labs', 'practice'].includes(view);
  return <div ref={root} className="oc-course-screen">
    {isIndex && <div className="oc-course-index">
      <div data-course-heading><PageHeader noBloom eyebrow={view === 'lessons' ? 'Introduction' : 'Practice'} title={view === 'lessons' ? 'Conditional reasoning.' : view === 'labs' ? 'Make the move yourself.' : 'Practice the reasoning.'} description={view === 'lessons' ? 'Learn one idea, use it, then build on it. The drills between lessons give you a chance to test the meaning before moving on.' : 'Make an attempt before reading the explanation. Name the mistake, repair it and try again.'}/></div>
      {view === 'practice' && recordedPractice}
      <ol className="oc-course-path">{list.map(step => <CourseCard key={step.id} step={step} url={url}/>)}</ol>
      {!list.length && <p>No opening lessons are available in this work.</p>}
    </div>}
    {view === 'tools' && <div className="oc-course-note">
      <div data-course-heading><PageHeader noBloom eyebrow="Tools" title="Recall before you turn." description="Say the relationship in your own words. Turn the card to compare your reasoning."/></div>
      <div className="co-opening">{steps.some(step => step.unitId === 'orientation' || step.unitId === 'sufficient-necessary') && <><h2>Enough and required</h2><StudyDeck group="foundation"/></>}{steps.some(step => step.unitId === 'group-1') && <><h2>Sufficient-condition words</h2><StudyDeck group="group-1"/></>}{steps.some(step => step.unitId === 'group-2') && <><h2>Necessary-condition words</h2><StudyDeck group="group-2"/></>}{!steps.length && <p>No flashcards are available in this work.</p>}</div>
    </div>}
    {current && <div className="oc-course-note">
      <div data-course-heading>{current.type === 'note' ? <header className="mb-10">
        <h1 className="font-mc-serif text-ink leading-[0.94] italic text-[clamp(3.1rem,7vw,6rem)] font-medium tracking-[-0.06em]">{current.title}</h1>
        <p className="font-mc-sans text-body-prose mt-4 text-ink-soft max-w-[60ch] leading-relaxed">{current.description}</p>
      </header> : <PageHeader noBloom eyebrow={run ? 'Drill' : 'Practice checkpoint'} title={current.title} description={current.description}/>}</div>
      {current.type === 'drill' && !run && <section className="oc-drill-entry"><h2>Make an attempt. Check the reasoning.</h2><ol><li>Read the rule and the exact question.</li><li>Choose or build your answer before checking.</li><li>Use the feedback to identify what you kept or changed.</li><li>Retry the case and explain your correction.</li></ol><p>Before moving on, explain why your corrected answer follows from the rule.</p><Link className="oc-action" to={url(view, true)}>Start drill<ArrowRight size={16}/></Link></section>}
    </div>}
    <div className="oc-course-bodies">{steps.filter(step => visited.includes(step.id)).map(step => <div key={step.id} hidden={step.id !== view || (step.type === 'drill' && !run)} className="oc-course-body co-opening cr-sequence"><OpeningCourseContent id={step.id}/></div>)}</div>
    {current && (current.type === 'note' || run) && <nav className="oc-course-turn" aria-label="Course navigation">{prior ? <Link to={url(prior.id)}><span>Previous {prior.type === 'note' ? 'lesson' : 'drill'}</span><strong>{prior.title}</strong></Link> : <Link to={url('lessons')}>All lessons</Link>}{next ? <Link to={url(next.id)}><span>Next {next.type === 'note' ? 'lesson' : 'drill'}</span><strong>{next.title}<ArrowRight size={18}/></strong></Link> : <Link to={url('lessons')}>Return to lessons<ArrowRight size={18}/></Link>}</nav>}
    {!isIndex && view !== 'tools' && !current && <div className="oc-course-note"><h1>This lesson is not available here.</h1><Link to={url('lessons')}>Return to lessons</Link></div>}
  </div>;
}
