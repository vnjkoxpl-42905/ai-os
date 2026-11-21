"""Fills the empty session slots of the neutral Famous Flaws note for one student.

Reads famous-flaws.html (the neutral build, with empty slots) and writes famous-flaws-ore.html.
This step is Claude's own and is not part of the Codex build, so no student content reaches Codex.
Run: py -I finish-for-student.py
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
src = (HERE / "famous-flaws.html").read_text(encoding="utf-8")


def rep(old, new, count=1):
    global src
    assert src.count(old) == count, (old[:70], src.count(old))
    src = src.replace(old, new)


# identity
rep('content="famous-flaws-full"', 'content="ore-2026-11-11-famous-flaws"')
rep("<title>Famous Flaws · Note</title>", "<title>Famous Flaws · Session recap</title>")
rep("<!--SLOT:hero-kicker-->Famous Flaws", "Session recap · November 11")

# which four were taught
rep("<p>Three colours, three groups, fifteen entries. Open any card to see the whole breakdown.</p>",
    "<p>Three colours, three groups, fifteen entries. Open any card to see the whole breakdown. In our session we went through four of them: Necessary vs. Sufficient, Causal, Part vs. Whole and Unproven vs. Proven False. They carry an <strong>In our session</strong> tag.</p>")
for fid in ("necessary-vs-sufficient", "causal", "part-vs-whole", "unproven-vs-proven-false"):
    rep(f'<span class="session-slot fx-session" data-slot="session-{fid}"></span>', f'<span class="session-slot fx-session" data-slot="session-{fid}">In our session</span>')

# her own words, in the panels where they were said
QUOTES = {
    "necessary-vs-sufficient": (
        "In the practice question from our session, a counselor argued that harsh criticism is necessary for people to change. "
        "You named the flaw correctly: sufficient treated as necessary. You first saw the word cause and thought causation. "
        "Then you read the conclusion again and asked, <em>&quot;Why is it only harsh criticism? ... It could be gentle, it could be constructive ... it could be other things.&quot;</em> "
        "That second read is the method."),
    "causal": (
        "You told me you saw the word cause and went straight to causation: <em>&quot;I saw the word cause and I assumed ... oh so this is probably causation.&quot;</em> "
        "A cause word tells you what the sentence is about. It does not tell you the flaw is Causal. Check what the conclusion adds to the evidence."),
    "part-vs-whole": (
        "You said: <em>&quot;Just because the team does well overall doesn't mean every single player on the team does well.&quot;</em> "
        "The names are new. The reasoning is yours."),
    "unproven-vs-proven-false": (
        "You said: <em>&quot;Because I can't prove you're innocent, you're guilty.&quot;</em> "
        "And the reverse: because I can't prove you're guilty, you're innocent. I called that the best example."),
}
for fid, text in QUOTES.items():
    rep(f'<div class="session-quote" data-slot="quote-{fid}" hidden></div>',
        f'<div class="session-quote" data-slot="quote-{fid}"><div class="quote">{text}</div></div>')

# what to do next
rep("<li>SLOT:next-steps</li>",
    "<li><b>Flaw - First Taste.</b> Read the Before you start note first. Then do the seven guided questions. Name the flaw before you read any choice, then find the choice that says it. Famous Flaw (Easier) Set 1 and Abstract + Flaw (set 1) follow on later days.</li>"
    "<li><b>Keep this note open beside every flaw question.</b> Write the name of the flaw next to your answer. When you miss one, write which flaw it was. In a week the pattern in your misses will show.</li>"
    "<li><b>Read one or two Reading Comprehension passages every other day.</b> Keep it light. The goal is to get used to the density of the language before we start the RC modules. Any passage works.</li>"
    "<li><b>Send me a message on the platform if you have a question.</b> I'll be able to get back to you.</li>")

import re
assert not re.search(r">SLOT:|<!--SLOT:", src), "an unfilled slot marker is still in the markup"
(HERE / "famous-flaws-ore.html").write_text(src, encoding="utf-8", newline="\n")
print("wrote famous-flaws-ore.html", len(src.encode("utf-8")), "bytes")
