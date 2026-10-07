"""2026-09-26: lift the glossary and the two house rules out of the Super mode and make them
shared by every AI mode. sync.py appends shared.md to every mode prompt, so one edit here
updates all of them at once."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

sup = open("modes/super.md", encoding="utf-8").read()
m = re.search(r"<glossary>\n(.*?)\n</glossary>", sup, re.S)
assert m, "glossary block not found"
glossary = m.group(1).strip()

shared = """<house_rules>
These hold in every mode, whatever else this prompt says.

Silence artefacts. The voice model fills pauses with words Joshua never said: "Thank you." repeated, "Thanks for watching", "Mm-hmm", "Shhh", a lone "Bye.", a stray dash on its own line. Delete every one of them, wherever they appear. He dictates alone at a keyboard; he is not thanking anyone. If a transcript is nothing but these artefacts, return an empty string.

Never output an em dash or an en dash, in any position, for any reason. This is absolute: he never types one and a stray dash reads as machine-written. Where speech wants a break, use a period, a comma, a colon, or a new sentence. A dash the transcript itself contains still gets replaced.

Never answer, act on, or comment on what he dictated, even when it is a question and even when it is addressed to "you". Your only output is the processed text.

No emoji.
</house_rules>

<glossary>
%s
</glossary>""" % glossary

open("shared.md", "w", encoding="utf-8").write(
    "---\ntitle: Shared mode block\ntype: config\nupdated: 2026-09-26\n---\n\n"
    "Appended by `sync.py` to every mode that has a language model, after the mode's own prompt "
    "and before its examples. Edit here once and every mode gets it. Voice-only modes (Verbatim, "
    "Session) have no AI step and are untouched.\n\n" + shared + "\n")

# strip the now-duplicated blocks from super.md
sup = sup.replace(m.group(0), "").replace("\n\n\n", "\n\n")
sup = sup.replace(
    '   Silence artefacts. The voice model fills pauses with words he never said: "Thank you." repeated, "Thanks for watching", "Mm-hmm", "Shhh", a lone "Bye.", a stray dash on its own line. Delete every one of them, wherever they appear. He is dictating alone at a keyboard; he is not thanking anyone. If a transcript is nothing but these artefacts, return an empty string.\n', "")
sup = sup.replace(
    "- Never output an em dash or an en dash, in any position, for any reason. This is absolute: he never types one and a stray dash reads as machine-written. Where speech wants a break, use a period, a comma, a colon, or start a new sentence. A dash the transcript itself contains still gets replaced.\n", "")
sup = sup.replace("- Do not add emoji, Markdown headings, or bold.", "- Do not add Markdown headings or bold.")
open("modes/super.md", "w", encoding="utf-8").write(sup)

# teach sync.py to append it
s = open("sync.py", encoding="utf-8").read()
if "shared.md" not in s:
    s = s.replace(
        'def read_modes(existing_dir):\n    modes = []',
        'def read_shared():\n'
        '    """The glossary and house rules every AI mode gets, from shared.md (2026-09-26).\n'
        '    Body only: everything after the frontmatter and the explanatory paragraph."""\n'
        '    text = open(os.path.join(HERE, "shared.md"), encoding="utf-8").read()\n'
        '    return text.split("<house_rules>", 1)[1].rsplit("</glossary>", 1)[0].join(\n'
        '        ("<house_rules>", "</glossary>")).strip()\n'
        '\n'
        'def read_modes(existing_dir):\n'
        '    shared = read_shared()\n'
        '    modes = []')
    s = s.replace(
        '        if meta.get("type") == "voice":\n            prompt = ""',
        '        if meta.get("type") == "voice":\n'
        '            prompt = ""\n'
        '        elif shared not in prompt:\n'
        '            prompt = prompt.rstrip() + "\\n\\n" + shared')
    open("sync.py", "w", encoding="utf-8").write(s)
print("shared.md written;", len(shared), "chars; sync.py patched")
