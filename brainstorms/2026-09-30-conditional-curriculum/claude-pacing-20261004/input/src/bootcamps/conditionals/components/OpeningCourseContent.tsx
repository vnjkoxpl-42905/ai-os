import { Children, cloneElement, Fragment, isValidElement, useId, useState, type ReactElement, type ReactNode } from 'react';
import { Fundamentals, GroupLessons } from './ConditionalOpeningLesson';
import { conditionalReferenceContent, IntegratedItem, referencePracticeItems, ReferenceQuestion, WordFamily } from './ConditionalReferenceSequence';
import { CounterexampleLab, NegativeCaseLab, RuleComparisonLab } from './CounterexampleLab';
import { StudyDeck } from './StudyDeck';

type ContentSection = ReactElement<{ id?: string; number?: number; title?: string; children?: ReactNode; dark?: boolean; 'data-reference-boundary'?: boolean }>;

// Compose the approved source sections directly. Their stateful exercises are
// mounted by React; the former reader-page renderer is never invoked here.
function sections(children: ReactNode): ContentSection[] {
  return Children.toArray(children).flatMap(child => {
    if (!isValidElement<ContentSection['props']>(child)) return [];
    return child.type === Fragment ? sections(child.props.children) : [child];
  });
}

function reference(number: number): ContentSection {
  const section = sections(conditionalReferenceContent().props.children).find(item => item.props.number === number);
  if (!section) throw new Error(`Missing approved conditional reference section ${number}`);
  return section;
}

function groupSections(group: 'group-1' | 'group-2') {
  return sections(GroupLessons({ id: group }).props.children);
}

function groupSection(group: 'group-1' | 'group-2', title: string) {
  const section = groupSections(group).find(item => item.props.title === title);
  if (!section) throw new Error(`Missing approved conditional section: ${title}`);
  const sectionId = `course-${group}-${title.toLowerCase().replace(/[^a-z0-9]+/g, '-')}`;
  return cloneElement(section, { key: sectionId, id: sectionId });
}

function NoteSection({ title, children }: { title: string; children: ReactNode }) {
  return <section className="co-section"><div className="co-section-heading"><h2>{title}</h2></div>{children}</section>;
}

function ReferenceBody({ number, omitTransition = false }: { number: number; omitTransition?: boolean }) {
  const source = reference(number);
  const children = Children.toArray(source.props.children);
  // These source sections end in navigation prose for the former ordering.
  // The course shell now owns transitions; the teaching stays in its source.
  return <section className={`co-section cr-course-section ${source.props.dark ? 'cr-dark' : ''}`} data-reference-source={number}>
    <div className="co-section-heading"><h2>{source.props.title}</h2></div>
    <div className="cr-step-body">{omitTransition ? children.slice(0, -1) : children}</div>
  </section>;
}

function FamilySupplement({ group }: { group: 'group-1' | 'group-2' }) {
  const source = reference(group === 'group-1' ? 3 : 5);
  const family = sections(source.props.children).find(child => child.type === WordFamily);
  if (!family) throw new Error(`Missing approved ${group} supplementary family`);
  return <details className="co-practical-note"><summary>More expressions for the same relationship</summary>
    <p>Use the stated rule: anyone who borrows a locker has a key. These sentences preserve that connection. They do not say every person with a key borrows a locker.</p>
    {family}
  </details>;
}

function IndicatorNote({ group }: { group: 'group-1' | 'group-2' }) {
  const [selected, setSelected] = useState(0);
  const id = useId();
  const content = groupSections(group);
  const expressions = content.slice(2, 9);
  // Two introductions and the seven complete expression explanations belong
  // together in one concept note, not nine separate navigation destinations.
  return <>{content.slice(0, 2)}
    <div className="co-word-tabs" role="group" aria-label="Choose an expression">{expressions.map((section, index) => <button type="button" key={section.props.title} aria-pressed={selected === index} aria-controls={`${id}-${index}`} onClick={() => setSelected(index)}>{section.props.title?.split(':')[0]}</button>)}</div>
    {expressions.map((section, index) => <div key={section.props.title} id={`${id}-${index}`} hidden={selected !== index}>{section}</div>)}
    <FamilySupplement group={group}/>
    <NoteSection title="Recall the expressions"><p>Explain the relationship before turning each card. Compare the complete ideas and the direction with your answer.</p><StudyDeck group={group}/></NoteSection>
  </>;
}

function FoundationPractice() {
  const definitionQuestions = [1, 2, 4].flatMap(number => sections(reference(number).props.children).filter(child => child.type === ReferenceQuestion).map((child, index) => cloneElement(child, { key: `${number}-${index}` })));
  const fresh = sections(Fundamentals().props.children).find(section => section.props.title === 'Enough does not mean the only way');
  if (!fresh) throw new Error('Missing approved fresh sufficient-condition check');
  const freshContent = Children.toArray(fresh.props.children);
  const freshCheck = freshContent[freshContent.length - 1];
  return <>
    <NoteSection title="Separate the rule from the fact"><blockquote>If you win the raffle, you get a bicycle.</blockquote><p>Use the rule to decide what each fact establishes. A wrong answer is a reason to inspect the connection and try again.</p>{definitionQuestions}</NoteSection>
    <NoteSection title="Try a fresh case">{freshCheck}</NoteSection>
    <NoteSection title="Test the limit with a possible case"><ReferenceQuestion prompt="Someone claims that getting a bicycle proves you won the raffle. Which possible case fits our rule but disproves that claim?" options={['You win and get a bicycle.', 'You do not win, but get a bicycle as a gift.', 'You win and never get a bicycle.']} correct={1} feedback={['This fits both the rule and the claim. It does not show why the claim adds something.', 'The rule promises a bicycle to a winner. It does not exclude a bicycle received as a gift without winning, so this case fits the rule and disproves the claim.', 'Winning without getting a bicycle breaks the original rule. We need a case that keeps the rule true.']}/></NoteSection>
  </>;
}

function GroupPractice({ group }: { group: 'group-1' | 'group-2' }) {
  const meaningCheck = groupSection(group, 'Check the meaning, not just the word');
  return <>
    {groupSection(group, group === 'group-1' ? 'Find the target, then place it' : 'Find the requirement, then place it')}
    {groupSection(group, 'From sentence to diagram')}
    {group === 'group-1' && groupSection(group, 'Read the only as a complete expression')}
    {cloneElement(meaningCheck, {}, Children.toArray(meaningCheck.props.children).slice(0, -1))}
    <details className="co-practical-note"><summary>More sentences to recall and explain</summary>{groupSection(group, 'Say the rule without the clues')}</details>
  </>;
}

function PermissionBoundary() {
  const boundary = sections(conditionalReferenceContent().props.children).find(section => section.props['data-reference-boundary'] !== undefined);
  if (!boundary) throw new Error('Missing approved permission and instruction boundary');
  return <NoteSection title="Keep permission and instructions distinct"><p>A conditional can give permission or an instruction. Preserve that strength instead of turning it into a report of what someone did.</p>{Children.toArray(boundary.props.children).slice(3)}</NoteSection>;
}

function ContrapositivePractice() {
  const [current, setCurrent] = useState(0);
  const [checked, setChecked] = useState<boolean[]>(() => referencePracticeItems.map(() => false));
  return <NoteSection title="Build an original and its contrapositive">
    <p>For each sentence, identify the indicator and both complete conditions. Choose the original diagram, then its contrapositive. Read both back before checking. If an answer needs revision, inspect the direction, qualifications and negation, then retry.</p>
    <p className="co-kicker" role="status">Sentence {current + 1} of {referencePracticeItems.length}</p>
    {referencePracticeItems.map((item, index) => <div key={item.sentence} hidden={current !== index} data-course-practice-item={index + 1}><IntegratedItem item={item} number={index + 1} onChecked={value => setChecked(previous => previous.map((old, itemIndex) => itemIndex === index ? value : old))}/></div>)}
    <div className="co-choices"><button type="button" disabled={current === 0} onClick={() => setCurrent(current - 1)}>Previous sentence</button><button type="button" disabled={current === referencePracticeItems.length - 1 || !checked[current]} onClick={() => setCurrent(current + 1)}>Next sentence</button></div>
    <p>Moving between sentences keeps your choices and feedback.</p>
  </NoteSection>;
}

function Content({ id }: { id: string }) {
  switch (id) {
    case 'meaning': return <ReferenceBody number={1} omitTransition/>;
    case 'sufficient': return <ReferenceBody number={2} omitTransition/>;
    case 'necessary': return <><ReferenceBody number={4} omitTransition/><ReferenceQuestion prompt="You get a bicycle. Does that establish that you won the raffle?" options={['Yes. Getting a bicycle proves winning.', 'No. You could get a bicycle without winning.']} correct={1} feedback={['You made the required result enough to establish winning. The rule does not say winning is the only way to get a bicycle.', 'You could buy a bicycle or receive one as a gift. Neither possibility breaks the rule, which only tells us what must follow if you win.']}/></>;
    case 'must-arrow': return <><ReferenceBody number={8}/><NoteSection title="Recall enough and required"><p>Use these new examples to check the roles and their direction.</p><StudyDeck group="foundation"/></NoteSection></>;
    case 'sufficient-words': return <IndicatorNote group="group-1"/>;
    case 'necessary-words': return <><IndicatorNote group="group-2"/><PermissionBoundary/></>;
    case 'whole-meaning': return <><ReferenceBody number={11} omitTransition/>{groupSection('group-1', 'Keep the whole condition')}{groupSection('group-2', 'Keep the whole condition')}{groupSection('group-2', 'Compare only with the only')}<ReferenceBody number={12} omitTransition/></>;
    case 'missing-requirement': return <><ReferenceBody number={6}/><ReferenceBody number={7} omitTransition/></>;
    case 'contrapositive': return <><ReferenceBody number={9}/><details className="co-practical-note"><summary>Practical questions about diagramming</summary><ReferenceBody number={10} omitTransition/></details><NoteSection title="Two possible rooms, one limit"><NegativeCaseLab/></NoteSection></>;
    case 'foundation-practice': return <FoundationPractice/>;
    case 'sufficient-practice': return <><GroupPractice group="group-1"/><NoteSection title="Build a case that proves the limit"><CounterexampleLab/></NoteSection></>;
    case 'mixed-practice': return <><GroupPractice group="group-2"/><NoteSection title="Keep the rule while the wording changes"><RuleComparisonLab/></NoteSection></>;
    case 'contrapositive-practice': return <ContrapositivePractice/>;
    default: throw new Error(`Unknown opening course content: ${id}`);
  }
}

/** Article body only. Course routes own titles, navigation and completion. */
export function OpeningCourseContent({ id }: { id: string }) {
  return <div className="co-opening cr-sequence opening-course-content"><Content key={id} id={id}/></div>;
}
