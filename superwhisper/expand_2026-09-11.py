"""One-off, 2026-09-11: expand vocabulary.md and replacements.md per Joshua's request
(every skill, every student, LSAT terms, tools, sensible replacements). Kept for the record."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
D = "2026-09-11"

skills = [d for d in sorted(os.listdir("../skills/claude")) if not d.startswith("_") and d != "README.md"]
students = """Adriana Varea;Amanda;Asia Tamaami;Avneet Natt;Bella Lorenzo;Celia Cutler;Celia Syrocki;Charles Moore;Claire Alexander;Dakota Brown;David Salgado;Ethan;Favour;Fernande Charleus;Ivory Johnson;Kaden Forges;Kaia Reid;Kristin Silva;Lydia;Meghan Mullins;Nicole Spinelli;Ore;Oreoluwa James;Priyanka Nambiar;Sofia Minassian;Steven Morris;Thaniuska Vivas;Vinay Kalva;Whit Wilson;Yahunatan Zetvy;Zeina""".split(";")
tools = """Superwhisper;Claude Code;Claude Desktop;Claude Design;Claude Opus;Claude Sonnet;Codex;Firecrawl;Lovable;Lovable Cloud;Supabase;Cal.com;Google Drive;Google Calendar;Gmail;Google Workspace;gws;GitHub;Obsidian;Vite;shadcn;Tailwind;Remotion;Higgsfield;ElevenLabs;Gemini;TutorOcean;Discord;NotebookLM;Postgres;edge function;RLS;RPC;MCP;CLI;API key;Stripe;Kling;Ghostty;Vercel;Notion;Slack;PowerShell;Task Scheduler;7Sage;LSAT Demon;LawHub;LSAC;PowerScore;Khan Academy;Manhattan Prep;Blueprint;React;TypeScript;JSON;Markdown;CLAUDE.md;README;OpenAI;ChatGPT;Anthropic""".split(";")
lsat = """LSAT;LSAT U;Aspiring Attorneys;Logical Reasoning;Reading Comprehension;Argumentative Writing;LSAT Writing;PrepTest;diagnostic;timed section;untimed;blind review;guided drill;drill;RRC;Read it;Tell it back;Colour it;The Recall;anti-conclusion;stimulus;question stem;answer choices;main conclusion;intermediate conclusion;premise;sub-conclusion;Must Be True;Most Strongly Supported;Necessary Assumption;Sufficient Assumption;Strengthen;Weaken;Flaw;Parallel Reasoning;Parallel Flaw;Principle;Point at Issue;Method of Reasoning;Argument Part;Role;Resolve the Paradox;Evaluate the Argument;Inference;Except question;Main Point;Author's Attitude;Comparative Reading;comparative passage;passage structure;conditional logic;contrapositive;sufficient condition;necessary condition;correlation versus causation;causal reasoning;sampling flaw;ad hominem;equivocation;quantifier;scope shift;score band;score report;percentile;law school admissions;Canadian law schools;Osgoode;U of T Law;Western Law;Queen's Law;UBC Law;McGill Law;consultation;booking link;booking pass;credits;session recap;homework;Activities;classroom;portal;AI grader;score band floor;judge model;feature flag;send ledger;teaching voice;handoff;wrapup;pickup;level up;brief me;second brain;vault;wiki;ingest;corpus;raw inbox;Web Clipper;transcript;Gemini transcript;consultation check-in""".split(";")

head = open("vocabulary.md", encoding="utf-8").read().split("\n- ", 1)[0].rstrip()
excl = """
## Exclude (replacement targets that should NOT be vocabulary)

- Zeina's (possessive; base word covers it)
- aspiringattorneys.com (Joshua: no, 2026-09-11)
- mattpocock's (possessive; the base word covers it)
- thank you (target of the silence-hallucination collapse row, not a hint)
"""
tl = {x.lower() for x in tools}
body = "\n\n## Tools and products\n\n" + "\n".join(f"- {t}" for t in tools)
body += "\n\n## LSAT, teaching, and the vault\n\n" + "\n".join(f"- {t}" for t in lsat if t.lower() not in tl)
body += "\n\n## Students and prospects\n\n" + "\n".join(f"- {t}" for t in students)
body += "\n\n## Identity\n\n- Joshua Fisseha\n- Fisseha\n- joshua.fisseha01@gmail.com\n- lsatprep.study\n- contact@aspiringattorneys.com\n- Pre-workout\n- mattpocock"
body += "\n\n## Skills (spoken names; the slash form comes in through replacements)\n\n" + "\n".join(f"- {s}" for s in skills)
open("vocabulary.md", "w", encoding="utf-8").write(head + body + "\n" + excl)

rows = []
def r(h, w, n=""):
    rows.append(f"| {h} | {w} | {D} | {n} |")

for s in skills:
    sp = s.replace("-", " ")
    r(f"slash {sp}", f"/{s}", "skill")
    if sp != s:
        r(f"slash {s}", f"/{s}", "skill")

bare = {"grill me": "grill-me", "grill me codex": "grill-me-codex", "grill me cortex": "grill-me-codex", "grillme": "grill-me",
        "grill me codecs": "grill-me-codex", "codex review": "codex-review", "lovable prompt": "lovable-prompt", "lovable migrate": "lovable-migrate",
        "skill creator": "skill-creator", "skill doctor": "skill-doctor", "skill lint": "skill-lint",
        "research deep": "research-deep", "second brain ingest": "second-brain-ingest", "second brain query": "second-brain-query", "second brain lint": "second-brain-lint",
        "lsat lab transcribe": "lsat-lab-transcribe", "lsat lab mega set": "lsat-lab-mega-set", "guided drill assignment": "guided-drill-assignment",
        "pre consultation check in": "pre-consultation-check-in", "consultation follow up drafts": "consultation-followup-drafts",
        "inbound tutoring replies": "inbound-tutoring-replies", "ask matt": "ask-matt", "loop me": "loop-me", "wait what": "wait-what",
        "systematic debugging": "systematic-debugging", "claude handoff": "claude-handoff", "claude md improver": "claude-md-improver",
        "prompt architect": "prompt-architect-refiner", "tutorocean profile fill": "tutorocean-profile-fill", "setup matt pocock skills": "setup-matt-pocock-skills"}
for h, w in bare.items():
    r(h, f"/{w}", "skill, bare spoken form")
    r(h + ".", f"/{w}", "")

extra = [("claude design", "Claude Design"), ("cloud design", "Claude Design"), ("cloud desktop", "Claude Desktop"), ("claude desktop", "Claude Desktop"),
("cal com", "Cal.com"), ("cal dot com", "Cal.com"), ("calcom", "Cal.com"), ("law hub", "LawHub"), ("lawhub", "LawHub"), ("el sac", "LSAC"), ("l sac", "LSAC"), ("lsack", "LSAC"),
("prep test", "PrepTest"), ("preptest", "PrepTest"), ("prep tests", "PrepTests"), ("lsat demon", "LSAT Demon"), ("lsat daemon", "LSAT Demon"), ("seven stage", "7Sage"), ("7sage", "7Sage"), ("seven sages", "7Sage"),
("super base", "Supabase"), ("supa base", "Supabase"), ("soup a base", "Supabase"), ("loveable", "Lovable"), ("lovable cloud", "Lovable Cloud"), ("shad cn", "shadcn"), ("shad c n", "shadcn"), ("chad cn", "shadcn"),
("get hub", "GitHub"), ("github", "GitHub"), ("gmail", "Gmail"), ("google drive", "Google Drive"), ("google calendar", "Google Calendar"), ("google workspace", "Google Workspace"), ("tutor ocean", "TutorOcean"), ("tutorocean", "TutorOcean"),
("notebook lm", "NotebookLM"), ("notebook l m", "NotebookLM"), ("eleven labs", "ElevenLabs"), ("11 labs", "ElevenLabs"), ("higgs field", "Higgsfield"), ("remotion", "Remotion"), ("obsidian", "Obsidian"),
("codecs", "Codex"), ("codex", "Codex"), ("open ai codex", "OpenAI Codex"), ("l s a t", "LSAT"), ("lsat", "LSAT"), ("elsat", "LSAT"), ("lsat you", "LSAT U"), ("lsat u", "LSAT U"),
("logical reasoning", "Logical Reasoning"), ("reading comprehension", "Reading Comprehension"), ("argumentative writing", "Argumentative Writing"), ("lsat writing", "LSAT Writing"),
("must be true", "Must Be True"), ("most strongly supported", "Most Strongly Supported"), ("necessary assumption", "Necessary Assumption"), ("sufficient assumption", "Sufficient Assumption"),
("parallel reasoning", "Parallel Reasoning"), ("parallel flaw", "Parallel Flaw"), ("point at issue", "Point at Issue"), ("method of reasoning", "Method of Reasoning"), ("resolve the paradox", "Resolve the Paradox"),
("comparative reading", "Comparative Reading"), ("main point", "Main Point"),
("r r c", "RRC"), ("rrc", "RRC"), ("air grader", "AI grader"), ("a i grader", "AI grader"), ("recall color", "Recall colour"), ("color it", "Colour it"), ("colour it", "Colour it"),
("aspiring attorneys", "Aspiring Attorneys"), ("aspiring attorney", "Aspiring Attorneys"), ("yahunathan", "Yahunatan"), ("yahu nathan", "Yahunatan"), ("yohanatan", "Yahunatan"), ("zetvy", "Zetvy"),
("avneet", "Avneet"), ("avnit", "Avneet"), ("avneet nat", "Avneet Natt"), ("fernand", "Fernande"), ("fernanda", "Fernande"), ("charleus", "Charleus"), ("vinay", "Vinay"), ("vinay calva", "Vinay Kalva"), ("kalva", "Kalva"),
("whit wilson", "Whit Wilson"), ("wit wilson", "Whit Wilson"), ("whitt wilson", "Whit Wilson"), ("ore oluwa", "Oreoluwa"), ("oreoluwa", "Oreoluwa"), ("priyanka", "Priyanka"), ("nambiar", "Nambiar"), ("thaniuska", "Thaniuska"),
("tanyuska", "Thaniuska"), ("tamaami", "Tamaami"), ("asia tamami", "Asia Tamaami"), ("syrocki", "Syrocki"), ("celia cutler", "Celia Cutler"), ("celia", "Celia"), ("dakota", "Dakota"), ("salgado", "Salgado"), ("minassian", "Minassian"),
("sophia minassian", "Sofia Minassian"), ("sofia", "Sofia"), ("sophia", "Sofia"), ("kaden forges", "Kaden Forges"), ("bella lorenzo", "Bella Lorenzo"), ("meghan mullins", "Meghan Mullins"), ("megan mullins", "Meghan Mullins"),
("nicole spinelli", "Nicole Spinelli"), ("ivory johnson", "Ivory Johnson"), ("favour", "Favour"), ("kaia reid", "Kaia Reid"), ("kristin silva", "Kristin Silva"), ("kristen silva", "Kristin Silva"),
("osgoode", "Osgoode"), ("osgood", "Osgoode"), ("os good", "Osgoode"), ("u of t law", "U of T Law"), ("mcgill", "McGill"), ("queen's law", "Queen's Law"), ("queens law", "Queen's Law"), ("ubc", "UBC"),
("joshua fisseha", "Joshua Fisseha"), ("joshua fasaya", "Joshua Fisseha"), ("joshua faseya", "Joshua Fisseha"), ("joshua fesaya", "Joshua Fisseha"), ("fisseha", "Fisseha"),
("super whisperer's", "Superwhisper's"), ("superwhisper's", "Superwhisper's"), ("thank you thank you thank you", "thank you"), ("g w s", "gws"), ("power shell", "PowerShell"), ("powershell", "PowerShell"),
("react", "React"), ("typescript", "TypeScript"), ("type script", "TypeScript"), ("tailwind", "Tailwind"), ("vercel", "Vercel"), ("stripe", "Stripe"), ("postgres", "Postgres"), ("post gres", "Postgres"),
("json", "JSON"), ("jason file", "JSON file"), ("markdown", "Markdown"), ("mark down file", "Markdown file"), ("md file", "Markdown file"),
("claude dot md", "CLAUDE.md"), ("claude md", "CLAUDE.md"), ("claudemd", "CLAUDE.md"), ("claude.md", "CLAUDE.md"), ("readme", "README"), ("read me file", "README file"), ("dot env file", ".env file"),
("obsidian vault", "Obsidian vault"), ("web clipper", "Web Clipper"), ("gemini", "Gemini"), ("kling", "Kling"), ("ghostty", "Ghostty"), ("anthropic", "Anthropic"), ("open ai", "OpenAI"), ("openai", "OpenAI"),
("chat gpt", "ChatGPT"), ("chatgpt", "ChatGPT"), ("mcp", "MCP"), ("m c p", "MCP"), ("cli", "CLI"), ("c l i", "CLI"), ("api", "API"), ("a p i", "API"), ("u i", "UI"), ("url", "URL"), ("u r l", "URL"), ("pdf", "PDF"), ("html", "HTML"), ("css", "CSS"), ("sql", "SQL"), ("s q l", "SQL"), ("rls", "RLS"), ("rpc", "RPC"), ("llm", "LLM"), ("llms", "LLMs"), ("jwt", "JWT"), ("oauth", "OAuth")]

existing = {l.split("|")[1].strip().lower() for l in open("replacements.md", encoding="utf-8") if l.startswith("| ") and not l.startswith("| Heard")}
seen = set()
for h, w in extra:
    if h.lower() in existing or h.lower() in seen:
        continue
    seen.add(h.lower())
    r(h, w, "casing pin" if h.lower() == w.lower() else "")
rows = [x for x in rows if x.split("|")[1].strip().lower() not in existing]
with open("replacements.md", "a", encoding="utf-8") as f:
    f.write("\n".join(rows) + "\n")
print(len(rows), "rows added;", len(skills), "skills")
