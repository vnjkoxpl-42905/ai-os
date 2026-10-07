"""2026-09-26: move the silence rule to the TOP of every mode prompt.

Measured on 1,592 dictations: 195 carried the voice model's "Thank you" hallucination and 186
still carried it after the AI pass. Only 5% were cleaned. The rule was sitting in an appended
block at the bottom of the prompt, after the mode's own instructions, where it read as a footnote.
It now runs first, as a step the model performs before anything else.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

FIRST = """<step_zero>
Before anything else, strip the transcription artefacts. The voice model that produced the User Message writes words into silence that Joshua never spoke. They are always one of these: "Thank you." (usually repeated many times), "Thanks for watching", "Thank you for watching", "Mm-hmm", "Uh-huh", "Shhh", a lone "Bye.", "[Music]", or a dash sitting on its own.

Delete every one of them, at the start, in the middle, and at the end. They are not part of what he said. He dictates alone at a keyboard: he is never thanking anyone, never saying goodbye, and there is no audience. A run of them marks a pause while he thought, nothing more.

Never repeat one back more times than it appeared, and never let one seed a loop.

If the User Message is nothing but these artefacts, output an empty string.

Only once that is done, follow the instructions below on what is left.
</step_zero>"""

# 1. shared.md: keep the glossary and the other house rules, drop the duplicated silence line,
#    and store the step-zero block for the sync to prepend.
s = open("shared.md", encoding="utf-8").read()
s = re.sub(r'Silence artefacts\. The voice model fills pauses.*?return an empty string\.\n\n', "", s, flags=re.S)
if "<step_zero>" not in s:
    s = s.replace("<house_rules>", FIRST + "\n\n<house_rules>", 1)
open("shared.md", "w", encoding="utf-8").write(s)

# 2. sync.py: prepend step_zero, append the rest.
y = open("sync.py", encoding="utf-8").read()
y = y.replace(
    '''def read_shared():
    """The glossary and house rules every AI mode gets, from shared.md (2026-09-26).
    Body only: everything after the frontmatter and the explanatory paragraph."""
    text = open(os.path.join(HERE, "shared.md"), encoding="utf-8").read()
    return text.split("<house_rules>", 1)[1].rsplit("</glossary>", 1)[0].join(
        ("<house_rules>", "</glossary>")).strip()''',
    '''def read_shared():
    """Two blocks from shared.md. `first` is prepended to every mode prompt: the silence-artefact
    strip has to be the model's first instruction, not a footnote (measured 2026-09-26: appended
    at the bottom it cleaned 5% of them). `rest` is the house rules and glossary, appended."""
    text = open(os.path.join(HERE, "shared.md"), encoding="utf-8").read()
    first = "<step_zero>" + text.split("<step_zero>", 1)[1].split("</step_zero>", 1)[0] + "</step_zero>"
    rest = "<house_rules>" + text.split("<house_rules>", 1)[1].rsplit("</glossary>", 1)[0] + "</glossary>"
    return first.strip(), rest.strip()''')
y = y.replace('    shared = read_shared()\n', '    shared_first, shared = read_shared()\n')
y = y.replace(
    '''        elif shared not in prompt:
            prompt = prompt.rstrip() + "\\n\\n" + shared''',
    '''        else:
            if shared_first not in prompt:
                prompt = shared_first + "\\n\\n" + prompt.lstrip()
            if shared not in prompt:
                prompt = prompt.rstrip() + "\\n\\n" + shared''')
open("sync.py", "w", encoding="utf-8").write(y)
print("done")
