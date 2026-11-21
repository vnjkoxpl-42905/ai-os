"""Build out/famous-flaws.html from the shell, content, diagrams, questions and images. Stdlib only."""
import base64, html, json, re, sys
from pathlib import Path

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT / "src"))
import content as C  # noqa: E402
from diagrams import DIAGRAMS  # noqa: E402

shell = (ROOT / "shell/note-shell.html").read_text(encoding="utf8")
SHELL_STYLE = re.search(r"<style>.*?</style>", shell, re.S).group(0)
SHELL_SCRIPT = re.search(r"<script>.*?</script>", shell, re.S).group(0)
Q = json.loads((ROOT / "src/questions.json").read_text(encoding="utf8"))
e = html.escape


def img(name):
    b = base64.b64encode((ROOT / f"img/{name}.webp").read_bytes()).decode()
    return f"data:image/webp;base64,{b}"


def marks(s):
    s = e(s, quote=False)
    s = s.replace("&lt;ev&gt;", '<span class="ev">').replace("&lt;/ev&gt;", "</span>")
    s = s.replace("&lt;con&gt;", '<span class="con">').replace("&lt;/con&gt;", "</span>")
    s = s.replace("&lt;j&gt;", '<span class="jump">').replace("&lt;/j&gt;", "</span>")
    return s


TIER_NAME = ["Most common", "Not-so-common"]


def hero():
    h = C.HERO
    return f'''<header class="hero art">
  <figure class="hero-img"><img src="{img('hero-bridge')}" alt="Ink drawing of a person striding confidently across a wooden footbridge toward missing planks, above a deep ravine." width="1200" height="675">
    <figcaption class="hero-title"><div class="kicker">{e(h['kicker'])}</div><h1>{e(h['title'])}</h1></figcaption></figure>
  <p class="lede">{e(h['lede'])}</p>
</header>'''


def flaw_image(f, n, small=False):
    path = ROOT / f"img/flaw-{f['id']}.webp"
    cls = "flaw-image small" if small else "flaw-image"
    if path.exists():
        return f'<img class="{cls}" src="{img("flaw-" + f["id"])}" alt="{e(f["img_alt"])}" width="240" height="160" loading="lazy">'
    return f'<div class="{cls} placeholder" aria-label="Illustration {n}"><span aria-hidden="true">{n}</span></div>'


def sheet():
    groups = ""
    for t in range(2):
        cards = ""
        for n, f in enumerate(C.FLAWS, 1):
            if f["tier"] != t:
                continue
            cards += f'''<li><a class="flaw-card" href="#f-{f['id']}" data-flaw="{f['id']}">
              <div class="card-heading"><span class="fi-n">{n}</span><h3>{e(f['name'])}</h3><span class="fi-dot" aria-hidden="true"></span><span class="fi-sr">not done yet</span></div>
              <p class="card-definition">{e(f['what'])}</p>{flaw_image(f, n)}<span class="entry-link">Read the breakdown</span></a></li>'''
        groups += f'<div class="sheet-group" data-tier="{t}"><h2>{e(TIER_NAME[t])}</h2><ol class="sheet-cards">{cards}</ol></div>'
    return f'<section id="sheet"><div class="wrap"><div class="sec-kicker">The ten flaws</div><p class="fi-progress" aria-live="polite">0 of 10 done</p><nav class="flaw-sheet" aria-label="The ten flaws">{groups}</nav></div></section>'


def how():
    h = C.HOW
    steps = "".join(f"<li><b>{e(a)}</b> {e(b)}</li>" for a, b in h["steps"])
    return f'''<section id="how"><div class="wrap">
  <div class="sec-kicker">{e(h['kicker'])}</div>
  <h2>{e(h['h2'])}</h2>
  <p>{e(h['intro'])}</p>
  <ol class="steps">{steps}</ol>
  {said(h)}
  <p class="legend">{marks(h['legend'])}</p>
</div></section>'''


def tier(t):
    T = C.TIERS[t]
    return f'''<section class="tier" id="{T['id']}"><div class="wrap">
  <figure class="tier-img"><img src="{img(T['img'])}" alt="{e(T['alt'])}" width="1200" height="675" loading="lazy"></figure>
  <div class="sec-kicker">{e(T['kicker'])}</div>
  <h2>{e(T['h2'])}</h2>
  <p>{e(T['p'])}</p>
</div></section>'''


def question(f):
    q = Q[f["q"]]
    ex = C.EXPLAIN[f["q"]]
    stim = "<br>".join(e(line) for line in q["stimulus"].split("\n"))
    choices = "".join(
        f'<button class="choice" type="button" data-l="{L}" aria-pressed="false"><span class="cl">{L}</span><span class="ct qtext">{e(t)}</span></button>'
        for L, t in q["answerChoices"].items())
    exps = f'<div class="exp" data-l="{q["correctAnswer"]}" data-right="1" hidden>{e(ex["right"])}</div>'
    exps += "".join(f'<div class="exp" data-l="{L}" hidden>{e(ex[L])}</div>' for L in q["answerChoices"] if L != q["correctAnswer"])
    return f'''<div class="q" data-answer="{q['correctAnswer']}" data-flaw="{f['id']}">
    <div class="q-head"><div class="plabel">Try a real one</div><p class="hint">A real LSAT question. Say the flaw in your own words first, then pick the choice that describes it.</p></div>
    <div class="passage qtext">{stim}</div>
    <p class="qstem qtext">{e(q['questionStem'])}</p>
    <div class="choices" role="group" aria-label="Answer choices">{choices}</div>
    <div class="qfb" role="status" aria-live="polite"></div>
    <div class="exps" hidden>{exps}</div>
    <div class="others" hidden><div class="plabel">Why the other choices miss</div><ul></ul></div>
  </div>'''


def said(f):
    if not f.get("said"):
        return ""
    return f'<div class="said"><span class="tag">From our session</span><p>{e(f["said"])}</p></div>'


def flaw(f, n):
    ll = f["lookalike"]
    exs = "".join(f'<div class="passage ex">{marks(x)}</div>' for x in f["examples"])
    why = "".join(f"<p>{e(p)}</p>" for p in f["why"])
    wording = "".join(f"<li>“{e(w)}”</li>" for w in f["wording"])
    return f'''<section class="flaw" id="f-{f['id']}" data-flaw="{f['id']}" data-tier="{f['tier']}"><div class="wrap">
  <div class="sec-kicker">{e(TIER_NAME[f['tier']])} · {n} of 10</div>
  {flaw_image(f, n, small=True)}
  <h2 data-part="name">{e(f['name'])}</h2>
  <div class="plabel">What it is</div>
  <p class="what" data-part="what">{e(f['what'])}</p>
  <figure class="dg">{DIAGRAMS[f['diagram']]()}</figure>
  <div class="part" data-part="example"><div class="plabel">{'Examples' if len(f['examples']) > 1 else 'Example'}</div>{exs}</div>
  <div class="part" data-part="why"><div class="plabel">Why it’s wrong</div>{why}</div>
  <div class="part" data-part="spot"><div class="plabel">Spot it</div><p>{e(f["spot"])}</p></div>
  <div class="part" data-part="wording"><div class="plabel">The right answer says</div><ul class="wording">{wording}</ul></div>
  <div class="callout trap" data-part="lookalike"><span class="tag">Don’t confuse it with · {e(ll['name'])}</span>
    <p class="ll-quote">“{e(ll['text'])}”</p><p class="ll-tell">{e(ll['tell'])}</p></div>
  {said(f)}
  {question(f)}
</div></section>'''


def nxt():
    N = C.NEXT
    steps = "".join(f"<li><b>{e(a)}</b> {e(b)}</li>" for a, b in N["steps"])
    return f'''<section id="next"><div class="wrap">
  <div class="sec-kicker">{e(N['kicker'])}</div>
  <h2>{e(N['h2'])}</h2>
  <ol class="steps todo">{steps}</ol>
</div></section>'''


def main():
    sections = [sheet(), how()]
    n = 0
    for t in range(2):
        sections.append(tier(t))
        for f in C.FLAWS:
            if f["tier"] == t:
                n += 1
                sections.append(flaw(f, n))
    sections += [nxt()]
    css = (ROOT / "src/layer.css").read_text(encoding="utf8")
    js = (ROOT / "src/layer.js").read_text(encoding="utf8")
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="lsatu-interactive-lesson" content="{C.LESSON_ID}">
<title>Famous Flaws · Note</title>
{SHELL_STYLE}
<style>
{css}
</style>
</head>
<body>
<div class="progress" aria-hidden="true"><i></i></div>
<nav class="rail" aria-label="Sections"><ol></ol></nav>
<div class="page">
{hero()}
<main>
{chr(10).join(sections)}
</main>
<div class="footer-note"><span class="mark">LSAT U</span></div>
</div>
{SHELL_SCRIPT}
<script>
{js}
</script>
</body>
</html>
'''
    out = ROOT / "out/famous-flaws.html"
    out.write_text(doc, encoding="utf8")
    print(out, len(doc.encode("utf8")), "bytes")


if __name__ == "__main__":
    main()
