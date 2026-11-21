from pathlib import Path
import draft as d

b = d.b
examples = {
"nec": ("Taking Pine Street gets you to the library.", "Mina got to the library, so she must have taken Pine Street.", "Mina could have taken Oak Street."),
"causal": ("On mornings the rooster crows, the sun rises soon afterward.", "So the rooster's crow makes the sun rise.", "Dawn explains both. The approaching daylight can also prompt the rooster to crow. The order of the two events cannot establish a cause."),
"part": ("Every brick in this wall is straight.", "So the wall must be straight.", "Straight bricks can form a leaning wall if they are laid at an angle."),
"unproven": ("The evidence box contains no record that the tree was planted in 1902.", "So it must have been planted in another year.", "A missing record leaves the year open."),
"adhom": ("The speaker says the new bus route would shorten the ride. She lives on the proposed route.", "So her claim about travel time must be false.", "Living on the route explains why she might want it changed. Check her claim against the travel times."),
"sampling": ("Every marble I scooped from the top of the jar is red.", "So most marbles in the jar are red.", "The top layer could be red while most marbles below it are gray."),
"appeal": ("The cat in the white coat says this medicine is safe.", "So it must be safe.", "The coat and stethoscope tell us how the cat is dressed. What establishes its medical expertise?"),
"circular": ("Every other route is less reliable than this one.", "So this is the most reliable route.", "To accept the evidence, you already have to accept the conclusion."),
"contradiction": ("The sign says the station is due east of this corner.", "The same sign says the station is due west of this corner.", "From the same corner, the station cannot be both due east and due west."),
"equiv": ("The map shows a bench on the riverbank.", "So the bench must be near a financial institution.", "The map uses bank to mean the land beside a river. The conclusion uses it to mean a business."),
}
previous = b.flaw
def render(f, n):
    html = previous(f, n)
    fact, claim, check = examples[f["q"]]
    start = html.index('  <figure class="dg">')
    end = html.index('  <div class="part" data-part="spot">', start)
    image = b.flaw_image(f,n,small=False)
    header = html[:start].replace(b.flaw_image(f,n,small=True), "")
    if f["q"] == "causal":
        steps = """<div class="cause-paths">
        <details open name="causal-path"><summary>The author's claim</summary><p>Crow → sunrise. The author treats the crow as the cause.</p></details>
        <details name="causal-path"><summary>Could it run the other way?</summary><p>Morning light → crow. The light could prompt the rooster to crow.</p></details>
        <details name="causal-path"><summary>Could something explain both?</summary><p>The time of day could account for both. The rooster can crow on its internal clock before the sun is up. Around the same time, Earth’s rotation brings the sun into view.</p></details></div>"""
    else:
        steps = f'<p class="example-check"><strong>Check the reasoning</strong>{b.e(check)}</p>'
    block = f'''<div class="part example-flow" data-part="example">
    <div class="plabel">Example</div>
    <div class="example-layout"><div class="example-art">{image}</div><div class="example-copy">
    <p><strong>What the author gives you</strong>{b.e(fact)}</p>
    <p><strong>What the author concludes</strong>{b.e(claim)}</p>
    {steps}</div></div></div>'''
    tail = html[end:].replace("The right answer says", "How a choice might describe it")
    if f["q"] == "sampling":
        tail = tail.replace(f["lookalike"]["tell"], "Sampling goes from the scoop to the rest of the jar. Part vs. Whole would say the jar is light because each marble is light.")
        tail = tail.replace("“assumes that what is true of each member of a group is true of the group as a whole”", "“assumes that what is true of each part is true of the whole”")
    return header + block + tail

b.C.HOW["legend"] = "Find the evidence and conclusion in each example. Then check what follows."
b.flaw = render
b.main()
out = Path("out/famous-flaws.html")
html = out.read_text(encoding="utf8")
css = """
.example-layout{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.55fr);border:1px solid var(--edge);border-radius:16px;overflow:hidden;background:var(--card);align-items:start}
.example-art img{display:block;width:100%;height:auto;aspect-ratio:1;object-fit:contain;background:var(--card)}
.example-copy{padding:clamp(16px,3vw,28px)}
.example-copy p{margin:0 0 14px}.example-copy p:last-child{margin-bottom:0}
.example-copy strong{display:block;font:600 13px var(--sans);color:var(--ink-soft);margin-bottom:4px}
.example-check,.cause-paths{border-top:1px solid var(--edge);padding-top:12px}
.cause-paths details{border-bottom:1px solid var(--edge);padding:8px 0}
.cause-paths summary{cursor:pointer;font-weight:600}.cause-paths details p{padding:8px 0 2px;margin:0}
@media (prefers-reduced-motion:no-preference){.cause-paths details[open] p{animation:show-cause .24s ease-out both}@keyframes show-cause{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:translateY(0)}}}
@media(max-width:600px){.example-layout{grid-template-columns:1fr}.example-art img{max-height:220px}}
"""
html = html.replace("</head>", "<style>"+css+"</style></head>")
assert html.count('class="part example-flow"') == 10
assert html.count('name="causal-path"') == 3
assert html.count('class="q" data-answer=') == 10
Path("out/famous-flaws-choices-refined.html").write_text(html,encoding="utf8")
