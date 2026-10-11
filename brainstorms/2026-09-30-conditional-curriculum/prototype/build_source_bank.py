from pathlib import Path
import json,re
root=Path(__file__).resolve().parent
html=(root/'group-1-2-drills.html').read_text(encoding='utf-8')
drills=json.loads(re.search(r'const drills=(.*?);\s*const app=',html,re.S)[1])
# Each row records full propositions, not abbreviations. Negation brackets the whole proposition.
# Format: indicator:group[;indicator:group] | sufficient | necessary | item-specific feedback
intro='''if:1|the product is registered within 30 days|the warranty is valid|The deadline belongs inside the sufficient condition. Registration after 30 days does not meet this trigger.
Whenever:1|you see lightning|you are instructed to expect thunder to follow|The instruction to expect thunder is the result. It does not establish that thunder actually follows.
only if:2|the gate opens|the correct code is entered|Opening requires the correct code. Entering a code alone does not establish that the gate opens.
All:1;must:2|a person is a manager|that person is required to undergo annual training|Keep the requirement in the outcome. A manager who skips training can still be a manager.
any:1|a person is a student who maintains a 4.0 GPA|the scholarship applies to that person|Keep student and maintains a 4.0 GPA together. The sentence does not cover every person with that GPA.
only when:2|you can access the VIP area|your ID is verified|Can access is the condition. Permission to enter is different from actually entering.
Only after:2|the project commences|the agreement has been signed before commencement|The signature must precede commencement. A signature at some later time would not meet the requirement.
Members who:1|a person is a member who pays their dues|that person can attend the meeting|Keep both membership and payment. Can attend does not say that the member attends.
If:1|the alarm sounds|the building should be evacuated immediately|Keep should in the result. Failure to evacuate does not establish that evacuation was not called for or that the alarm was silent.
must:2|a passenger is allowed to board the train|that passenger presents a ticket|This is a boarding requirement. Keep presents a ticket, rather than merely owns a ticket.
only if:2|a refund is issued|the item is returned unopened|Not returned unopened includes no return at all. It does not mean only returned opened.
if:1|the team wins the semifinals|the team goes to the finals|The sufficient condition appears last in the sentence but still goes on the left.
Every:1|a person is an applicant who passes the test|that person receives an interview call|Keep applicant who passes the test together. Passing alone is not the whole trigger.
must:2|a person is eligible to vote in this fictional election|that person is over 18|Over 18 means older than 18. This exercise supplies a fictional eligibility rule, not election-law advice.
If:1|you plant trees|you support the environment|Use the supplied rule. Planting trees is enough for its stated result; the result alone does not establish planting.'''
indicators='''Only if:2|employees qualify for promotion|those employees complete training|The training requirement comes first in the sentence, but qualification goes on the left of the arrow.
Any:1|a person is a student who misses a lesson|that student receives notes|Keep the student and missed-lesson restriction in the trigger.
only when:2|houseguests can enter the backyard|the gate is unlocked|The rule concerns whether entry is possible. It does not claim anyone actually enters.
The only:1|a food spoils quickly|that food has no preservatives|Here the only foods that spoil quickly identifies the sufficient category. Quickly spoiling food requires no preservatives; the reverse is not given.
where:1|maintenance is complete|servers restart|Where introduces the situation sufficient for restarting in this supplied rule.
must:2|a driver avoids fines under this rule|that driver wears a seatbelt|Avoiding fines requires a seatbelt. Wearing one alone does not guarantee avoiding every fine.
if:1|the alarm sounds|workers evacuate|Read the if-clause first when drawing the arrow, even though it appears last.
requires:2|a loan is granted|collateral is provided|The loan requires collateral. Providing collateral alone does not guarantee a loan.
All:1|an application is submitted on time|that application is reviewed|On time belongs to the sufficient condition. The rule does not cover late applications.
when:1|visitors show ID|those visitors can enter|Keep can enter. Permission is not proof that entry occurs.
always:2|troubleshooting begins|errors have been documented before troubleshooting|Before is part of the requirement. Documentation after troubleshooting would not meet it.
only where:2|the park is accessible at a location|pathways lead to that location|Keep the same location on both sides. Accessible park locations require pathways leading there.
Every:1|a person is an author who publishes|that author gains recognition|The publishing restriction is part of the sufficient condition.'''
full='''All:1|a person is an intern who completes the program|that intern is offered a full-time position|Keep intern and program completion together. An offer is not the same as taking the job.
if:1|you submit your report by Friday|your grade is finalized|Negate submission by Friday as a whole. A late submission does not meet the trigger.
when:1|the final bell rings|students exit the building|The bell is sufficient under this rule. Exiting does not establish that the bell rang.
Every:1|a person is a participant who finishes the marathon|that participant receives a medal|Finishing, rather than simply participating, is the full trigger.
Any:1|a device is left unattended|that device powers down automatically|Automatically belongs in the result. A manual shutdown is not the same condition.
whenever:1|the committee meets|minutes are recorded|Meeting is sufficient even though it appears at the end of the sentence.
must:2|employees qualify for bonuses|those employees exceed sales targets|Qualification requires exceeding the targets. Exceeding them alone need not guarantee a bonus.
only if:2|expenditures can occur|managers have approved the budgets first|Preserve can occur and first. The sentence is about authorization, not proof of spending.
requires:2|operations are halted temporarily|system maintenance is performed|The reviewed rule makes maintenance a prerequisite for the halt. Maintenance alone does not establish that operations halt.
only when:2|access is granted|user credentials are verified|Access requires verified credentials. Verification alone does not guarantee access.
only where:2|servers reboot|network security protocols permit the reboot|Permission for this reboot is the requirement, not the mere existence of security protocols.
always:2|entry occurs|security checks have been conducted before entry|The reviewed rule is factual. Keep the checks and their timing together.
if:1|the emergency protocol fails to initiate within one minute|alarms do not deactivate on their own|Negate each complete condition. The contrapositive starts with alarms deactivating on their own and ends with protocol initiation within one minute.
only if:2|the cluster performs backups|it detects low storage for two cycles|Two cycles is part of the requirement. One low-storage reading is not enough to match it.
whenever:1|three reviewers call for revision|reports are published|Negating three reviewers call for revision does not mean three reviewers refuse. It denies the whole condition.
only when:2|passengers are allowed to board|their documents are verified by both authorities|Not verified by both means at least one verification is missing. It does not mean neither verified.
Any:1|a sample is exposed to extreme temperatures|that sample's integrity is compromised|The rule covers any such exposure. Uncompromised integrity rules out that exposure.
only if:2|a reimbursement request can be processed|the employee submits a detailed online report|Preserve can be processed, detailed, and online. An incomplete report does not meet the requirement.
When:1|safety standards are unmet|inspections occur immediately|Not immediately inspected is broader than never inspected. Timing belongs in the condition.
always:2|servers restart|critical software patches have been applied before the restart|The patches must precede this restart. Later patching is not the required condition.'''
rephrase='''All:1;must:2|a person is a runner in a marathon|that runner is required to hydrate before the marathon|The outcome is a hydration duty, not proof that a runner complied. Keep before the marathon.
Whenever:1|sunlight hits the solar panels|the panels generate electricity|Start with the whenever clause. The rule does not say electricity is generated only this way.
Only those:2|a person receives the rebate|that person conserves water|Receiving the rebate requires conservation. Conservation alone need not establish a rebate.
only if:2|the door is unlocked using a key|the blue key is used|This version is limited to unlocking with a key. It does not exclude other possible ways of opening the door.
requires:2|a person succeeds in chess|that person uses strategic thinking|Success requires strategic thinking. Strategic thinking alone is not guaranteed success.
Any:1;must:2|a person is an artist who uses oil paints|that artist is required to clean their brushes thoroughly|The outcome is the cleaning requirement. Noncompliance alone does not establish the artist avoided oil paints.
All:1;require:2|a project is successful|that project involves effective teamwork|The reviewed statement makes teamwork necessary for success. Teamwork alone does not guarantee a successful project.
Only those:2|a person can apply for this position|that person has a degree in architecture|Can apply is not actually applies. Preserve eligibility in both translations.
Whenever:1|the sun sets|the streetlights turn on|Sunset is the trigger in the supplied rule. Lights being on need not establish sunset.
The only:1|wisdom is reached|experience is involved|Treat the path metaphor as a stated requirement. Wisdom requires experience; experience alone need not yield wisdom.
Every:1;must:2|an agreement is legally binding|that agreement is in writing|Every covers the agreements under discussion, but the full sufficient condition is legally binding agreement. Must be in writing to be binding supplies the requirement.
only if:2|you achieve your goals|you remain committed|Achievement requires commitment. The sentence does not guarantee achievement from commitment alone.
Anyone:1|a person studies physics|that person encounters complex mathematical concepts|Anyone makes the rule cover every person who studies physics, not everyone without restriction.
When:1|artists are inspired|those artists create their most celebrated pieces|Assume the sentence as the exercise rule. Do not judge the diagram by whether this claim is realistic.
only when:2|a plant thrives|sunlight reaching that plant's leaves is adequate|Keep sunlight reaching its leaves as the full required condition.
Only those:2|a submission is reviewed|the registrar has confirmed that submission's applicant identity|The identity must belong to this submission's applicant and be confirmed by the registrar.
only where:2|a license is renewed|a payment record matching that license's identifier exists|A payment record for a different license does not satisfy this requirement.
only when:2|certification occurs|an evaluator whose authorization is currently active signs the form|Negation means no currently authorized evaluator signs. One evaluator declining to sign does not rule out another qualifying signer.
only if:2|a request is processed|the request file assigned by the portal to that requester is present|Preserve the assignment to this requester. Just any file is not enough.
Every:1;must:2|a device bears a failed seal|that device must be recalibrated under the maintenance policy|The reviewed policy creates an obligation. A device awaiting recalibration can still bear a failed seal. Keep must in the outcome.
If:1|a person's registration is verified by the registrar|that person is granted admission|Keep the registrar's verification, not registration alone, as the trigger.
The only:1|an entry is accepted|the clerk records that entry in the registry|Accepted entries form the sufficient category. Registry recording is required for acceptance.
Where:1|verification that the training requirement is met appears in the file|access is granted|The trigger is verification appearing in the file, not merely training being completed.
Whenever:1|a complaint meeting the policy threshold is filed with the office|an investigation begins|Both the policy threshold and filing with the office belong in the trigger.
All:1;always:2|a permit is issued by the agency|that permit includes an audit trail matching the transaction record|Keep agency-issued and the matching record. All marks the covered permits; always describes their required feature.'''
independent='''if:1|you leave your burrito on the counter|the burrito thaws|The if-clause comes last. It is still the sufficient condition.
Each and every:1|an individual is a member of the Q continuum|that individual is omnipotent|Treat this as a fictional rule. Membership is sufficient; omnipotence alone does not establish membership.
if:1|there is a bear behind you|you run quickly|The unclear name in the source has been replaced with a clear result. The conditional direction is unchanged.
whenever:1|you reduce your expenses|your disposable income increases|Use the stated relationship as the premise. The exercise is about its direction, not financial advice.
If:1|you study|you beat the LSAT|This is an assumed exercise rule, not a promise about test results. Study is sufficient within this premise.
Where:1|there is beer at a place|there is fun at that place|Keep the location consistent. The supplied rule does not make fun proof that beer is present.
if:1|you pay your taxes|the sun rises|An arrow does not assert causation. Translate the given rule even when its subject matter is implausible.
Whenever:1|it rains|it pours|Read the words literally for this supplied rule. Pouring is the required result.
All:1|a person is one of the King's men|that person swore an oath of allegiance|Keep the King's men as the category. Men alone would change the rule.
The only:1|an animal is a monkey|that animal lives in trees|The only monkeys identifies the sufficient category. Monkeys require tree dwelling in this stipulated rule.
if:1|you drink coffee|you become a magician|Treat this as a fictional rule. A valid diagram need not describe a realistic causal connection.
Every:1|a person is a lawyer|that person can read|Can read is an ability, not evidence that reading is occurring now.
Any:1|an object is a computer|that object can do addition|Keep can. An ability to add does not mean an addition operation is happening.
All:1|an animal is a beaver|that animal loves to eat maple trees|Loves to eat is not the same as eats. Preserve the complete stated result.
must:2|we live|we eat|Living requires eating. Eating alone is not a guarantee of living.
Only:2|a device reveals where you are|that device is a GPS|Only identifies GPS as necessary. Where inside reveals where you are is not a separate conditional indicator.
requires:2|a party is good|alcohol is present at that party|Treat this as the exercise premise, not advice about parties. A requirement is not sufficient on its own.
requires:2|a person has expertise|that person has practiced|Expertise requires practice. Practice does not by itself guarantee expertise.
Only:2|an animal swims|that animal is a fish|Only points to the necessary category, fish. Apply the supplied rule even though other animals swim in real life.
always:2|a moment is in the stated Philadelphia scenario|it is sunny there at that moment|Always is not a condition. The explicit time and place supply the domain; sunny is the required property.
only when:2|food is in the fridge|Rufus is not around|The contrapositive starts with Rufus being around and concludes that food is not in the fridge.
Only:2|a person dies young|that person is good|Dying young is sufficient for goodness within the supplied rule, not the reverse.
if:1|Arun is in the next room|I cannot see Arun|Negating cannot see gives can see, not actually see. Keep ability consistent.
if:1|Amar is over 40|Amar does not want to learn to ski|Negate the desire condition, not skiing itself. Over 40 is also different from 40 or older.
When:1|things cost more|people both buy less and use less of those things|Negating both means at least one result fails. It does not require both buying and use to remain unchanged.
Where:1|judges are independent in a system|that system has a good legal system|Keep the same system on both sides. No causal claim is needed to translate the rule.
All:1|an organism is a tree|that organism is a perennial plant with an elongated stem|Negate the full combined description. Failing either part is enough; both need not fail.
only:2|something is good under the stated theory|it is pleasure|The exclusivity claim makes pleasure necessary for goodness. Good goes left; pleasure goes right.
Every:1|a behavior is a mating ritual|that behavior can be conceptualized as a game to illuminate its underlying strategies|Preserve can be conceptualized and the purpose clause. Possibility is different from actual conceptualization.
All:1|a feature is a Martian gully|that feature is poleward of 30 degrees latitude|Keep Martian and the full latitude boundary. The rule is not about all gullies everywhere.
When:1|a mix of fresh and dried grass clippings is mixed into garden soil|the soil's moisture loss decreases|This explicitly labeled adaptation replaces the unclear source result. Keep both fresh and dried and the garden-soil setting.
When:1|the sky is clear|atmospheric pressure is high|Clear sky is sufficient in the exercise rule. High pressure alone does not establish a clear sky.
anyone:1|a person is infected by virus X|that person's body produces antibodies to fight virus X after a week|Anyone supplies the universal coverage. Will is not the indicator. Keep the one-week timing.
only when:2|economic conditions improved|the policy of free trade had already been implemented|Implementation precedes improvement. The conditional alone does not establish causation.
Where:1|a moral duty exists|that moral duty supersedes every legal duty and every other kind of duty|Negate the whole superseding claim. Failure to supersede at least one covered duty is enough.'''

def parse(block):
    return [line.split('|') for line in block.splitlines()]
blocks=[parse(intro),parse(indicators),parse(intro),[parse(indicators)[i-1] for i in [1,2,3,6,9,8,7,10,13,11]],parse(rephrase),parse(full),parse(independent)]
ids=['source-intro-identify','source-indicators','source-intro-diagrams','source-roles','source-rephrase','source-full-translation','source-independent']
kinds=['identify','indicators','forward','roles','rephrase','contrapositive','contrapositive']
files=[('Intro training set/Homework/2025-06-23_intro training group ½ (3).pdf','93623f4304af75a3c2e009610dfa0fc9ec5316ed3c304c67d6d2166d48c19a4d'),('Indicator ID set (Part 1)/Homework/2025-09-03_G1 &G2 worksheet (1) (1).docx','43dbf02fd4f7ec1002dac4aa69b383eafc110dd2259044a53b1383c2a0935f6d'),('If-Then rephrase set (Sep 5)/Homework/2025-09-05_IF_THEN worksheet.pdf','6e889126da7457708b435ef73d3ccaeec4824ebddfafea6e72881e3f77090ff8'),('Translation set (burrito)/Homework/2025-07-03_Homework For Group 1 & Group 2 (1).pdf','16be3555a66c9313fffa6afcd071ec0ca8816d7c8fbf7808a0acf42e6dd2ac05')]
fixes={
 (0,2):'Whenever you see lightning, you are instructed to expect thunder to follow.',
 (0,10):'Passengers must present a ticket to be allowed to board the train.',
 (0,14):'You must be over 18 to be eligible to vote in this fictional election.',
 (1,8):'Granting a loan requires collateral to be provided.',
 (1,11):'Errors are always documented before troubleshooting begins.',
 (4,1):'All runners in a marathon must hydrate before that marathon.',
 (4,4):'That door is unlocked using a key only if the blue key is used.',
 (4,7):'All successful projects require effective teamwork to have taken place.',
 (4,20):'Every device that bears a failed seal must be recalibrated under the maintenance policy.',
 (5,9):'Halting operations temporarily requires system maintenance to be performed.',
 (5,12):'Security checks are always conducted before entry.',
 (6,3):'You will run quickly if there is a bear behind you.',
 (6,20):'In this fictional Philadelphia scenario, it is always sunny.',
 (6,28):'Under the stated theory, only pleasure is good.',
 (6,31):'When a mix of fresh and dried grass clippings is mixed into garden soil, the soil’s moisture loss decreases.'}
for n in [2,10,14]:fixes[(2,n)]=fixes[(0,n)]
fixes[(3,6)]=fixes[(1,8)]
fixes[(3,10)]=fixes[(1,11)]
def negate(proposition):
    # Explicit scope exceptions come before grammatical transformations. Do not negate a relative clause.
    exceptions={
      'an evaluator whose authorization is currently active signs the form':'no evaluator whose authorization is currently active signs the form',
      'three reviewers call for revision':'it is not the case that three reviewers call for revision',
      'people both buy less and use less of those things':'people do not both buy less and use less of those things',
      'that moral duty supersedes every legal duty and every other kind of duty':'that moral duty fails to supersede at least one legal duty or other kind of duty',
      'the emergency protocol fails to initiate within one minute':'the emergency protocol initiates within one minute',
      'alarms do not deactivate on their own':'alarms deactivate on their own',
      'Rufus is not around':'Rufus is around',
      'I cannot see Arun':'I can see Arun',
      'Amar does not want to learn to ski':'Amar wants to learn to ski',
      'safety standards are unmet':'safety standards are met',
      'the building should be evacuated immediately':'it is not the case that the building should be evacuated immediately',
      'that device must be recalibrated under the maintenance policy':'that device is not required to be recalibrated under the maintenance policy',
      "sunlight reaching that plant's leaves is adequate":"sunlight reaching that plant's leaves is not adequate",
      "a payment record matching that license's identifier exists":"no payment record matching that license's identifier exists",
      'verification that the training requirement is met appears in the file':'verification that the training requirement is met does not appear in the file',
      'the request file assigned by the portal to that requester is present':'the request file assigned by the portal to that requester is not present',
      'that person swore an oath of allegiance':'that person did not swear an oath of allegiance',
      'a person has expertise':'that person does not have expertise',
      'the policy of free trade had already been implemented':'the policy of free trade had not already been implemented',
      'economic conditions improved':'economic conditions did not improve',
      'there is fun at that place':'there is no fun at that place',
      'there is beer at a place':'there is no beer at that place',
      'the park is accessible at a location':'the park is not accessible at that location',
      'judges are independent in a system':'judges are not independent in that system',
      'something is good under the stated theory':'it is not good under the stated theory',
    }
    if proposition in exceptions:return exceptions[proposition]
    # These auxiliaries negate the main verb for the remaining reviewed propositions.
    for old,new in [(' is ',' is not '),(' are ',' are not '),(' can ',' cannot '),(' has ',' has not '),(' have ',' have not ')]:
        if old in proposition:
            # Possessive has/have use do-support; perfect constructions retain the auxiliary.
            if old==' has ' and not any(x in proposition for x in [' has been ',' has practiced',' has confirmed',' has a ',' has no ']):continue
            if ' has a ' in proposition:return proposition.replace(' has a ',' does not have a ',1)
            if ' has no ' in proposition:return proposition.replace(' has no ',' has ',1)
            return proposition.replace(old,new,1)
    verbs={'presents':'present','spoils':'spoil','wears':'wear','avoids':'avoid','gains':'gain','hits':'hit','conserves':'conserve','sets':'set','studies':'study','rings':'ring','meets':'meet','performs':'perform','submits':'submit','exists':'exist','sounds':'sound','opens':'open','commences':'commence','wins':'win','goes':'go','applies':'apply','receives':'receive','bears':'bear','succeeds':'succeed','uses':'use','involves':'involve','encounters':'encounter','thrives':'thrive','occurs':'occur','signs':'sign','records':'record','begins':'begin','includes':'include','thaws':'thaw','increases':'increase','rises':'rise','rains':'rain','pours':'pour','lives':'live','loves':'love','reveals':'reveal','swims':'swim','dies':'die','decreases':'decrease','produces':'produce','powers':'power','detects':'detect','supersedes':'supersede'}
    for word,base in verbs.items():
        if f' {word} ' in proposition or proposition.endswith(' '+word):
            return re.sub(r'\b'+word+r'\b','does not '+base,proposition,count=1)
    for word in ['qualify','lead','cost','see','plant','support','complete','restart','wear','evacuate','show','enter','submit','exit','meet','exceed','permit','reboot','occur','hit','generate','achieve','remain','create','leave','run','reduce','study','beat','pay','drink','become','live','eat','turn']:
        if f' {word} ' in proposition or proposition.endswith(' '+word):
            return re.sub(r'\b'+word+r'\b','do not '+word,proposition,count=1)
    return 'it is not true that '+proposition

def negate_same_subject(proposition):
    return re.sub(r'^(a|an) ', 'that ', negate(proposition))

sets=[]
for di,(d,rows) in enumerate(zip(drills,blocks)):
    assert len(rows)==len(d['items']),(di,len(rows),len(d['items']))
    file,sha=files[[0,1,0,1,2,1,3][di]]
    items=[]
    for j,(original,row) in enumerate(zip(d['items'],rows),1):
        indicator,left,right,explanation=row
        statement=fixes.get((di,j),original)
        notes=[]
        if str(j) in d['flags']:notes.append(d['flags'][str(j)])
        if statement!=original:notes.append('Reviewed derivative: the learner-facing statement clarifies the source. The exact original remains in originalStatement.')
        items.append(dict(id=f'{ids[di]}-{j:02}',sourceId=f'{["intro-p1","indicator-p1","intro-p2","indicator-p2","rephrase","indicator-p3","translation"][di]}-{j:02}',originalStatement=original,statement=statement,indicators=[dict(text=x.rsplit(':',1)[0],group=int(x.rsplit(':',1)[1])) for x in indicator.split(';')],sufficient=left,necessary=right,diagram=f'{left} → {right}',contrapositive=f'NOT ({right}) → NOT ({left})',ifThen=f'If {left}, then {right}.',contrapositiveWords=f'If {negate_same_subject(right)}, then {negate_same_subject(left)}.',explanation=explanation,correctionNotes=notes,source=dict(file=file,sha256=sha,part=d['source'],item=j)))
    instruction=d['instruction']
    if di==0:instruction='Select the indicator expressions and their groups. Then write the two complete conditions before comparing with the model. Keep words that limit who, when, or what the rule covers.'
    if di==1:instruction='Select each indicator expression and identify its group. A sentence may contain expressions from both groups. Check which condition each expression helps you find.'
    if di==2:instruction='Return to the 15 intro statements. Write the complete conditions, assign each a symbol, then construct the original arrow using your own legend. Compare its direction and complete meaning.'
    if di==3:instruction='Write the two complete conditions. Compare their meaning, then place the sufficient condition on the left and the necessary condition on the right. Their order in the sentence may differ.'
    if di==4:instruction='Rewrite the statement as “If …, then …” before looking at a model. Then identify each indicator and its group and build the original arrow. Keep permissions, duties, deadlines, and restrictions.'
    if di==5:instruction='Identify each indicator and its group, then write the complete conditions and define your symbols. Build the original diagram and its contrapositive, then read both back in ordinary if/then language. Complete your own translation before revealing the model.'
    if di==6:instruction='Translate each statement independently: identify the indicators, write the complete conditions, define your symbols, build both arrows, and read them back in words. Complete your attempt before comparing with the model. Keep every qualifier and negate whole conditions.'
    sets.append(dict(id=ids[di],title=d['title'],shortTitle=d['short'],stage=d['stage'],taskKind=kinds[di],instructions=instruction,items=items))
header='''/** Reviewed derivatives of Joshua's Group 1/2 worksheets. Original source text and hashes are retained.
 * NOT (...) negates the entire proposition, including qualifiers and compound predicates.
 * Sets before contraposition contain its reference data for later use; the UI must gate its display by taskKind.
 */
export type SourceWorksheetTaskKind = 'identify' | 'indicators' | 'forward' | 'roles' | 'rephrase' | 'contrapositive';
export interface SourceWorksheetItem {
  id: string; sourceId: string; originalStatement: string; statement: string;
  indicators: { text: string; group: 1 | 2 }[];
  sufficient: string; necessary: string; diagram: string; contrapositive: string;
  ifThen: string; contrapositiveWords: string; explanation: string; correctionNotes: string[];
  source: { file: string; sha256: string; part: string; item: number };
}
export interface SourceWorksheetDrillSet {
  id: string; title: string; shortTitle: string; stage: string; taskKind: SourceWorksheetTaskKind;
  instructions: string; items: SourceWorksheetItem[];
}
export const sourceWorksheetDrills: SourceWorksheetDrillSet[] = '''
out=Path('C:/Users/Joshu/dev/ai-os-projects/lsatu-conditional-bootcamp/src/bootcamps/conditionals/content/sourceWorksheetDrills.ts')
footer=''';

// Later visits reuse source items without counting them as new worksheet questions.
const contrapositiveRevisits: Record<string, { sourceSetId: string; title: string; shortTitle: string }> = {
  'source-intro-diagrams-contrapositive': {
    sourceSetId: 'source-intro-diagrams',
    title: 'Revisit the intro: build the contrapositive',
    shortTitle: 'Intro training: contrapositives',
  },
  'source-rephrase-contrapositive': {
    sourceSetId: 'source-rephrase',
    title: 'Revisit the rules: write both directions',
    shortTitle: 'Rephrasing: contrapositives',
  },
};

export const getSourceWorksheetDrill = (id: string): SourceWorksheetDrillSet | undefined => {
  const canonical = sourceWorksheetDrills.find((set) => set.id === id);
  if (canonical) return canonical;
  const revisit = contrapositiveRevisits[id];
  if (!revisit) return undefined;
  const source = sourceWorksheetDrills.find((set) => set.id === revisit.sourceSetId);
  if (!source) return undefined;
  return {
    ...source,
    id,
    title: revisit.title,
    shortTitle: revisit.shortTitle,
    stage: 'After contraposition',
    taskKind: 'contrapositive',
    instructions: 'Return to these familiar statements. Identify the indicators, write the complete conditions, and define your symbols. Build the original diagram and its contrapositive, then write both in ordinary if/then language. Reverse the conditions and negate each complete idea, including its restrictions.',
  };
};
'''
out.write_text(header+json.dumps(sets,ensure_ascii=False,indent=2)+footer,encoding='utf-8')
print('Wrote',sum(len(s['items']) for s in sets),'reviewed source tasks')
