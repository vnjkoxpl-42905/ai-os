#!/usr/bin/env python3
"""Build wiki/homework-assigning/model-note/note-shell.html from Joshua's Lanae note.

The shell keeps the Lanae head, CSS and script byte for byte, except two fixes the
LSAT U lesson validator needs (system/scripts/lsatu-lesson-validate.mjs):
  - the Google Fonts <link> tags are removed and Outfit is embedded as a data URI;
  - the grain texture's nested url(%23n) is percent-encoded so it is not read as a file.
The body becomes one example of every component, with {{slots}}. An agent copies the
shell, fills the slots, deletes components it does not need, and never edits the CSS.

Fraunces (the headings) is embedded from model-note/fonts/ (latin roman 67 KB and italic
81 KB, downloaded from Google Fonts on 2026-11-14 with Joshua's approval, SIL Open Font
License). JetBrains Mono is NOT embedded: the only local copies are heavy Nerd Font builds,
so labels fall back to Cascadia Mono or Consolas.

Usage: py -I system/scripts/build-note-shell.py
"""
import base64
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "wiki" / "homework-assigning" / "model-note"
MODEL = DIR / "Lanae - Finding the Conclusion by Asking Why.html"
OUTFIT = ROOT / "design/prototypes/lsatu-dashboard/families/06-motion-studies/outfit-latin.woff2"
FRAUNCES = DIR / "fonts" / "fraunces.woff2"  # optional, not present yet


FRAUNCES_ITALIC = DIR / "fonts" / "fraunces-italic.woff2"


def face(family, path, weight, style="normal"):
    b64 = base64.b64encode(path.read_bytes()).decode()
    return f'@font-face{{font-family:"{family}";font-weight:{weight};font-style:{style};font-display:swap;src:url(data:font/woff2;base64,{b64}) format("woff2")}}\n'


h = MODEL.read_text(encoding="utf8")
head, rest = h.split("<body", 1)
body_open = rest.split(">", 1)[0]
script = re.search(r"<script>.*?</script>", rest, re.S).group(0)

head = re.sub(r'<link rel="preconnect"[^>]*>\s*', "", head)
head = re.sub(r'<link href="https://fonts\.googleapis[^>]*>\s*', "", head)
faces = face("Outfit", OUTFIT, "100 900")
if FRAUNCES.exists():
    faces += face("Fraunces", FRAUNCES, "400 700")
if FRAUNCES_ITALIC.exists():
    faces += face("Fraunces", FRAUNCES_ITALIC, "400 600", "italic")
head = head.replace("<style>", "<style>\n" + faces, 1)
head = head.replace("url(%23n)", "url%28%23n%29")
head = re.sub(r"<title>.*?</title>", "<title>{{TITLE}} · Session recap</title>", head, flags=re.S)
head = re.sub(r'(name="lsatu-interactive-lesson" content=")[^"]+', r"\1{{lesson-id: student-yyyy-mm-dd-topic}}", head)

BODY = """
<div class="progress" aria-hidden="true"><i></i></div>
<nav class="rail" aria-label="Sections"><ol></ol></nav>
<div class="page">

<!-- HERO. Kicker is always "Session recap · <Month D>". Title: a plain phrase for what the student learns. -->
<header class="hero"><div class="wrap">
  <div class="kicker">Session recap · {{Month D}}</div>
  <h1>{{First line of title}}<br>{{second line}}</h1>
  <p class="lede">{{What students usually do, why it fails, then the check that always works. 3 to 4 sentences.}}</p>
</div>
<div class="stage" aria-hidden="true"><div class="stack" data-tilt="10">
  <div class="slab base"><i>{{RESULT}}</i><b>{{What the checks lead to}}</b></div>
  <div class="slab c2"><i>CHECK 2</i><b>{{Second question to ask}}</b></div>
  <div class="slab c1"><i>CHECK 1</i><b>{{First question to ask}}</b></div>
</div></div></header>

<main>

<!-- COMPONENT: numbered steps + callout. The workhorse. Every section opens with a sec-kicker and an h2 that says something. -->
<section><div class="wrap">
  <div class="sec-kicker">{{Read it first}}</div>
  <h2>{{A heading that states the idea}}</h2>
  <p>{{One to three plain sentences.}}</p>
  <ol class="steps">
    <li><b>{{Short bold instruction.}}</b> {{One or two sentences of reasoning, with a concrete example in quotes.}}</li>
    <li><b>{{Next step.}}</b> {{Reasoning.}}</li>
  </ol>
  <div class="callout"><span class="tag">{{The one-line lesson}}</span> {{Two sentences. Process over result.}}</div>
</div></section>

<!-- COMPONENT: two-card contrast (kinds). Use for any either/or the student must tell apart. -->
<section><div class="wrap">
  <div class="sec-kicker">{{Two kinds}}</div>
  <h2>{{X or Y?}}</h2>
  <p>{{Why the sort matters.}}</p>
  <div class="kinds">
    <div class="kind apply" data-tilt="5"><span class="bar"></span><div class="name">{{X}}</div>
      <p class="what">{{Definition in one or two sentences.}}</p>
      <div class="words"><b>Looks like</b> <span>{{An example sentence.}}</span></div>
      <div class="test"><b>Test</b>{{The question that identifies it.}}</div></div>
    <div class="kind link" data-tilt="5"><span class="bar"></span><div class="name">{{Y}}</div>
      <p class="what">{{Definition.}}</p>
      <div class="words"><b>Looks like</b> <span>{{An example sentence.}}</span></div>
      <div class="test"><b>Test</b>{{The question that identifies it.}}</div></div>
  </div>
  <div class="callout"><span class="tag">{{A trap, named}}</span> {{Example, then the rule it shows.}}</div>
</div></section>

<!-- COMPONENT: switch gate. Optional. Two switches and four verdict lines; keep the script's expectations (data-state, .v0 to .v3). -->
<section><div class="wrap">
  <div class="sec-kicker">{{The check}}</div>
  <h2>{{What makes it X}}</h2>
  <div class="gate" data-state="0">
    <h3>{{Try the two checks}}</h3><p class="hint">Flip each switch and see what the sentence is.</p>
    <div class="gate-body">
      <button class="sw" type="button" role="switch" aria-checked="false"><span class="track"><span class="knob"></span></span><span>{{First check}}</span></button>
      <button class="sw" type="button" role="switch" aria-checked="false"><span class="track"><span class="knob"></span></span><span>{{Second check}}</span></button>
      <div class="verdict" role="status"><i class="lamp"></i>
        <span class="v0">{{Neither passes.}}</span><span class="v1">{{Only the first.}}</span><span class="v2">{{Only the second.}}</span><span class="v3">{{Both pass. This is it.}}</span></div>
    </div>
  </div>
</div></section>

<!-- COMPONENT: keyword flags, trap callout, and the student's own words. The quote is the recap part: what she said or asked in the session. -->
<section><div class="wrap">
  <div class="sec-kicker">{{Keywords}}</div>
  <h2>{{What the keywords do and do not tell you}}</h2>
  <div class="flags"><span class="flag">{{word}}</span><span class="flag">{{word}}</span></div>
  <p>{{What the words signal.}}</p>
  <div class="callout trap"><span class="tag">{{The trap that costs the most}}</span> {{What students do, and the fix.}}</div>
  <div class="quote">{{You said it yourself: ... Then what she asked, and why it was the right question.}}</div>
</div></section>

<!-- COMPONENT: tap-to-check. Items are the real sentences or answers from the session. data-k: describe (green), assume (brass), object (red), neutral. -->
<section><div class="wrap">
  <div class="sec-kicker">Try it</div>
  <h2>{{Sort these}}</h2>
  <div class="drill">
    <div class="drill-head"><div><h3>Say it out loud, then tap to check</h3><p class="hint">{{The question to ask of each item.}}</p></div></div>
    <p class="passage"><em>{{Optional passage or stimulus the items come from.}}</em></p>
    <div class="chips">
      <div class="chip" data-k="describe" role="button" tabindex="0" aria-expanded="false"><span>{{Item}}</span><span class="stamp" aria-hidden="true">{{Label}}</span><span class="ans">{{Label. Reason in one sentence.}}</span></div>
      <div class="chip" data-k="assume" role="button" tabindex="0" aria-expanded="false"><span>{{Item}}</span><span class="stamp" aria-hidden="true">{{Label}}</span><span class="ans">{{Label. Reason.}}</span></div>
      <div class="chip" data-k="neutral" role="button" tabindex="0" aria-expanded="false"><span>{{Item}}</span><span class="stamp" aria-hidden="true">Not this one</span><span class="ans">{{Not this one. Why.}}</span></div>
    </div>
  </div>
</div></section>

<!-- COMPONENT: the screen. Left is the work, right is the answers. A schematic, not a real question. -->
<section><div class="wrap">
  <div class="sec-kicker">{{On every question}}</div>
  <h2>{{Before you read the answer choices}}</h2>
  <p>{{Why the work happens on the left.}}</p>
  <figure class="screen"><div class="bezel"><div class="panes">
    <div class="pane left"><b>Stimulus</b><i></i><i></i><i class="hit"></i><i></i></div>
    <div class="pane right"><b>Answer choices</b><i data-l="A"></i><i data-l="B"></i><i data-l="C"></i><i data-l="D"></i><i data-l="E"></i></div>
  </div></div><figcaption>{{One line.}}</figcaption></figure>
  <ol class="steps"><li><b>{{Step.}}</b> {{Reason.}}</li></ol>
</div></section>

<!-- CLOSE. Always present. What the student does next, in Joshua's words. -->
<section><div class="wrap">
  <div class="sec-kicker">Your work</div>
  <h2>What to do next</h2>
  <ol class="steps todo">
    <li><b>{{First task, named as on the platform.}}</b> {{Why and how.}}</li>
    <li><b>Send me a message on the platform if you have a question.</b> I'll be able to get back to you.</li>
  </ol>
</div></section>

</main>
<div class="footer-note"><span class="mark">LSAT U</span></div>
</div>
"""

out = head + "<body" + body_open + ">" + BODY + script + "\n</body>\n</html>\n"
(DIR / "note-shell.html").write_text(out, encoding="utf8")
print("wrote", DIR / "note-shell.html", len(out), "bytes; fraunces embedded:", FRAUNCES.exists())
