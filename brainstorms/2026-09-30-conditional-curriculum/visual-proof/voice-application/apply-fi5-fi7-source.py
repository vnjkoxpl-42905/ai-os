import ast
import hashlib
import json
import re
from pathlib import Path

repo = Path('C:/Users/Joshu/dev/ai-os-projects/lsatu-conditional-bootcamp')
proof = Path(__file__).parent
source_path = repo / 'src/bootcamps/conditionals/content/foundations.source.ts'
source = source_path.read_bytes().decode('utf-8')
opening_ids = ['orientation', 'sufficient-necessary', 'group-1', 'group-2']
matches = list(re.finditer(r"(?m)^  \{\r?\n    id: '([^']+)'", source))
legacy_path = repo / 'src/bootcamps/conditionals/content/legacyQuestions.ts'
legacy_before = hashlib.sha256(legacy_path.read_bytes()).hexdigest()

reword = {
    "B could have the ready label or still be waiting for it; either possibility fits what we've been told.": "B could be marked ready or packed without being marked ready. Either possibility fits what we've been told.",
    "A packed order waiting for a ready label would fit the rule.": "An order that's packed but not marked ready would fit the rule.",
    "In the second sentence, a packed order could still be waiting for a ready label.": "In the second sentence, an order could be packed without being marked ready.",
    "Under this rule, that event guarantees evacuation.": "The sentence promises evacuation whenever the alarm sounds.",
    "That person has to receive an invitation under the rule.": "The sentence promises that person an invitation.",
    "Choose a late-submitting applicant and that person pays a fee under the rule.": "A late-submitting applicant pays a fee. That's what the sentence guarantees.",
    "No. The rule requires the underwater certification before it promises a sealed housing.": "No. The rule promises a sealed housing for sensors certified for underwater use.",
    "A verified account has to have a recovery code under this rule.": "The rule requires a recovery code for every verified account.",
    "Acceptance for the student symposium is enough for a faculty sponsor under this rule.": "A paper accepted for the student symposium has to have a faculty sponsor.",
    "A reserved locker has to display a nameplate under this rule, so Reserved locker → displays nameplate preserves it.": "The rule promises a nameplate for a reserved locker, so Reserved locker → displays nameplate preserves it.",
    "The schedule changing is enough for a notice to be printed under the rule.": "Whenever the schedule changes, the rule promises a printed notice.",
    "It didn't. A workshop offering same-day feedback has to be online under this rule.": "It didn't. A workshop offering same-day feedback has to be online.",
    "An online workshop without that feedback fits. Online format is required for the feedback, but it hasn't been made enough to establish it.": "An online workshop without that feedback fits. The sentence requires online format for same-day feedback; it doesn't say every online workshop offers that feedback.",
    "A tray set aside for nut-free orders has to carry a green marker under this rule.": "The rule gives a green marker to every tray set aside for nut-free orders.",
    "Subscriber status alone hasn't been promised that permission. Nor does permission tell us someone actually accessed the recording.": "The sentence doesn't say every subscriber can access the recording. Nor does permission tell us someone actually accessed it.",
    "So Registered buoy → broadcasts identifier preserves the rule. Broadcasting hasn't been made proof of registration, and unregistered buoys haven't been forbidden from broadcasting.": "So Registered buoy → broadcasts identifier preserves the rule. The claim doesn't say every broadcasting buoy is registered or that an unregistered buoy stays silent.",
    "An open kitchen hasn't been made enough for breakfast service. Serves breakfast goes left, and café alone isn't the requirement.": "The kitchen could be open without serving breakfast. Serves breakfast goes left, and café alone isn't the requirement.",
    "A road hasn't been promised service, and absence of service hasn't been made proof of no road. Keep the direction the sentence actually gives.": "Road access alone doesn't tell us the service runs there. No service wouldn't prove there's no road. Keep the direction the sentence actually gives.",
    "Having that form alone hasn't been made enough to borrow. Borrowing is the restricted activity; buying a camera isn't discussed.": "Signing the form doesn't settle whether you borrow the camera. Borrowing is the restricted activity; buying a camera isn't discussed.",
    "Detection alone hasn't been made enough for recording. The sentence also says nothing about the camera being broken.": "Motion could be detected while the camera records nothing. The sentence also says nothing about the camera being broken.",
    "It wasn't. A guest who gets a locker needs a day pass, but a day pass isn't stated enough for a locker.": "It wasn't. The pass is required for a locker, but the rule doesn't promise a locker to every passholder.",
    "Print alone would cover other editions. A date stamp hasn't been made proof of this edition, so the reverse is unsupported too.": "Print alone would cover other editions. A stamped print could come from another edition, so the reverse arrow adds something we weren't given.",
    "A case alone hasn't been promised underwater use, and the sentence doesn't require a case for every camera use. Keep underwater in the left-hand idea.": "Having the case doesn't tell us the camera is used underwater, and the sentence doesn't require a case for every camera use. Keep underwater in the left-hand idea.",
}
usage = dict.fromkeys(reword, 0)

def improve(text):
    for old, new in reword.items():
        if old in text:
            usage[old] += text.count(old)
            text = text.replace(old, new)
    return text

patches = []
nonopening_before = []
question_contracts = []
for index, match in enumerate(matches[:-1]):
    block = source[match.start():matches[index + 1].start()]
    if match.group(1) not in opening_ids:
        nonopening_before.append(block)
        continue
    revised_lines = []
    for line in block.splitlines(keepends=True):
        question = re.match(r'(\s+(?:guidedExample: )?)question\((.*)\),(\r?\n)?$', line)
        if not question:
            revised_lines.append(improve(line))
            continue
        arguments = list(ast.literal_eval('(' + question.group(2) + ')'))
        question_contracts.append(arguments[:4])
        arguments[4] = improve(arguments[4])
        arguments[5] = [improve(step) for step in arguments[5]]
        revised = question.group(1) + 'question(' + ', '.join(json.dumps(value, ensure_ascii=False) for value in arguments) + '),' + (question.group(3) or '')
        after = list(ast.literal_eval('(' + re.match(r'\s+(?:guidedExample: )?question\((.*)\),', revised).group(1) + ')'))
        assert after[:4] == arguments[:4]
        revised_lines.append(revised)
    patches.append((match.start(), matches[index + 1].start(), ''.join(revised_lines)))

assert len(patches) == 4
assert all(usage.values()), [text for text, count in usage.items() if not count]
for start, end, replacement in reversed(patches):
    source = source[:start] + replacement + source[end:]
assert all(block in source for block in nonopening_before)
source_path.write_bytes(source.encode('utf-8'))
assert hashlib.sha256(legacy_path.read_bytes()).hexdigest() == legacy_before
print(json.dumps({'rewordedPassages': sum(usage.values()), 'questionContractsUntouched': len(question_contracts), 'nonopeningAuthoredBlocksBytePreserved': len(nonopening_before), 'legacyFileBytePreserved': True}, indent=2))

draft_path = proof.parent.parent / 'voice-opening-source-draft.md'
draft_text = draft_path.read_text(encoding='utf-8')
for old, new in reword.items():
    draft_text = draft_text.replace(old, new)
draft_text += '\n## Actual inspection 2 source cleanup, 2026-10-02\n\nFI-5: All current opening ready-label waiting descriptions now describe an order that is packed but not marked ready. No later labeling or timeline is implied. FI-7: Repeated passive phrasing in the four units and their feedback now names the specific unsupported promise. Necessary qualifications remain where they clarify a supplied rule. No prompt, option, numeric key, ID, level membership or historical row changed. What Test and Personalized If/Then stay named; the renderer worker now teaches both. Current62, preserved61 and historical4 fingerprints remain exactly as recorded above.\n'
draft_path.write_text(draft_text, encoding='utf-8')
