[← Back to Blog](https://thomas-wiegold.com/blog/)

Listen to this article

0:000:00

1×

Nearly every benchmark I read measures coding. Bug fixing, tool use, agentic loops, how many turns it takes to get a test suite green. Almost nobody measures taste.

That's a problem, because when I start a new site the first decision isn't which model writes the cleanest TypeScript. It's which one gives me a layout I don't immediately want to throw away. Those are different jobs, and there's no law saying the same model has to win both. Finding the best LLM for frontend design is a separate question from finding the best coding model, and I wanted an answer I'd actually tested rather than a leaderboard screenshot.

So I ran one. Four design briefs, one run per model, same prompt for everyone, no per-model tuning, single file HTML. Everything is browsable at [webdesign-test.thomas-wiegold.com](https://webdesign-test.thomas-wiegold.com/) and you can click through the grid yourself.

The honest headline is that I struggled to pick winners at all. Most of the time the results were close enough that I couldn't articulate why I preferred one over another. It was a vibe. That sounds like a cop-out for a post with this title, but stay with me, because "I can't tell them apart" turns out to be the useful finding.

## The short answer

There is no single best LLM for frontend design right now, at least not among the models I use. Across four briefs, GPT-5.6 Sol took two, Claude Opus 5 took one and tied another, and Qwen3.8-Max shared that tie. The gaps were small enough that a different judge would produce a different table. The practical move is to run one prompt through three or four models and pick whichever output you like, because that costs ten minutes and beats agonising over the correct choice.

| Brief | My pick | Notes |
| --- | --- | --- |
| Pip & Pocket (early learning) | GPT-5.6 Sol | Opus 5 very close, better illustrations |
| Still Running (conference) | Claude Opus 5, barely | Kimi K3 and Luna right behind |
| Three in a Row (game) | Opus 5 and Qwen3.8-Max, tied | Sol and DeepSeek Flash had a layout bug |
| Ordinary Hours (perfume) | GPT-5.6 Sol | Changed my mind, see below |

## Which models, and why these ones

The lineup is Claude Opus 5, GPT-5.6 Sol, GPT-5.6 Luna, Qwen3.8-Max, Grok 4.6 and DeepSeek V4 Flash. On the conference brief I also managed to run DeepSeek V4 Pro, Kimi K3 and MiniMax M3.

These are the models I actually use and pay for. That's the whole selection criterion, and I'd rather state it plainly than pretend this is a comprehensive benchmark.

The obvious absences are Kimi and GLM, which I know are strong at this. I don't have a Kimi Code or GLM Code subscription. I have [opencode go](https://thomas-wiegold.com/blog/opencode-go-review/), but running those models through it is expensive enough and limited enough that I couldn't do a full grid, which is why Kimi shows up on exactly one brief. Gemini isn't in here either, and that one bothers me most, because [I liked a lot of what Gemini 3.5 Flash produced](https://thomas-wiegold.com/blog/google-antigravity-review-i-tested-gemini-3-5-flash/) for web design and I want to see whether 3.7 kept it. All three are on the list to add to the comparison site later.

## How I ran it

Four briefs, picked to stress different things.

Pip & Pocket is an early learning centre. Still Running is a running conference. Three in a Row is tic-tac-toe, the only brief with real interaction. Ordinary Hours is a perfume brand, and that prompt asks for something specific: three genuinely different visual styles on one page, switchable with a button.

One run per model per brief. I didn't tune anything, didn't feed anyone a design system, didn't specify fonts. That's deliberate, and I'll come back to why.

The site holding the results was built in one shot by Grok 4.6. Keyboard shortcuts, a compare view, click a model name to see its whole row or column. I asked for a way to browse test results and got something better than I would have specced.

The usual caveats apply and I'd rather say them than have you find them. Single judge, no blind voting, no accessibility or performance audit, HTML only. Nothing here tells you how these models behave inside a real React codebase.

The one that matters most: every cell in this grid is a single generation. These models are not deterministic, so any given result is one sample from a range, and a rerun could land somewhere else entirely. Keep that in mind for everything below, especially anywhere I say a model got something wrong.

## Brief by brief

### Pip & Pocket, and why cute is hard

This is the brief I'd keep if I could only keep one, because it's the one that isn't on home turf.

These models are excellent at modern, dark, techy, minimal, slightly artsy. That's the register they default to and it's clearly the register they've seen most. Ask for cute, bright, friendly and colourful and things get shakier. It's the same reason a session musician who's played nothing but jazz for ten years sounds a bit odd playing country.

Opus and Sol were both strong and very close. Opus produced nicer SVG illustrations, no argument there. But I preferred Sol's section layout and its colour choices, and layout and colour is more of the page than the illustrations are. So Sol takes it, narrowly, and I'd understand anyone picking the other way.

Test Results: [Pip & Pocket](https://webdesign-test.thomas-wiegold.com/t/daycare)

### Still Running, where everything worked

All good. That's the summary.

The conference brief is exactly the modern dark techy thing these models are best at, and it shows. I slightly prefer Opus for the animation on the symbols, but Kimi K3 is great, Luna is very good. If you looked at those three side by side and picked a different one, I'd shrug and agree.

The one weaker result was DeepSeek V4 Pro, which didn't land the way the others did. I want to be careful here, because Pro only ran on this single brief, which makes it unfair to call it the loser of the whole test. It's one result. Worth noting, not worth a verdict.

Test Results: [Still Running](https://webdesign-test.thomas-wiegold.com/t/event)

### Three in a Row, and a real bug

The only brief with actual interaction, so the criteria change. What happens on hover, does the win state get any celebration, do the tap targets work on a phone.

Sol and DeepSeek Flash both had the same concrete problem: the grid squares weren't holding their aspect ratio, so dropping an X or an O into a cell stretched it into a rectangle. The layout was just broken.

Opus and Qwen3.8-Max both produced designs that fit a game. Nothing clever, it just works, which for a game is the entire job. Luna was good too.

Worth flagging that Sol's box bug is almost certainly not a fixed property of Sol. It's one generation. Ask again and there's every chance the sizing comes out fine, and I'd have written a different paragraph.

That's the clearest illustration in the whole test of why you generate several times before concluding anything about a model. Including anything I've concluded here.

Test Results: [Three in a Row](https://webdesign-test.thomas-wiegold.com/t/gameui)

### Ordinary Hours, where I changed my mind

The perfume prompt asks for three distinct visual styles on one page with a button to switch between them, which makes it a test of range. Can the model produce three different aesthetics, or does it produce one aesthetic three times?

My original pick was Luna, and I was pleased about that because Luna is OpenAI's cheap tier and Sol is the flagship, with more than twenty times the per-token price between them. Cheap model wins beauty contest, nice story.

Then I went back through the results while writing this and found a bug: Luna's second theme doesn't render properly. So the story changes. Sol gets it instead, and on its own merits: its three themes are properly distinct from each other, which is the thing the brief was actually asking for.

I'm leaving the reversal in rather than quietly editing the table, because it's a decent illustration of what these comparisons are actually like. You look, you form an impression, you look again and the impression moves.

Test Results: [Ordinary Hours](https://webdesign-test.thomas-wiegold.com/t/perfume)

## Where the models separate, and where they don't

Line up the four briefs and a pattern falls out that I didn't expect going in.

On the conference site, everyone was good. On the perfume site, most were interesting. On tic-tac-toe, two models had a sizing bug but the designs were fine. On the early learning centre, the field spread out.

The briefs where models are hard to tell apart are the briefs that sit right in the middle of what they've been trained on. Dark, modern, sans-serif, generous whitespace, a bit of motion. Anthropic has a name for the underlying effect: distributional convergence, models drifting toward the median of their training data. Inter, purple to blue gradients, four identical rounded stat cards in a row. You know the look, and you know it because you've now seen it four hundred times.

Push a model off that median and the differences show up. Cute, bright and colourful is off the median. So, in a different way, is "give me three unrelated styles in one file."

Which suggests something for anyone benchmarking this themselves: test the thing your models are bad at, not the thing they're good at. A test where everyone scores well isn't measuring much.

## What the leaderboards say, and where I disagree

The public picture as of mid-August 2026: [Arena's WebDev board](https://arena.ai/leaderboard/code/webdev) has Claude Opus 5 at number one, with Kimi K3 and Qwen3.8-Max next. The [Design Arena website board](https://www.designarena.ai/leaderboard/website) has Kimi K3 in front, with Opus 5, GLM-5.2, Gemini 3.7 Flash and Grok 4.6 packed into roughly ten Elo points behind it.

Two caveats I'd rather state than pretend precision. The gaps in that top group are smaller than the confidence intervals, so the ordering shuffles week to week. And the Design Arena figures everyone quotes, including the ones above, come from third-party mirrors labelled display-only, because the live board is JavaScript-gated. Treat any specific number as approximate.

Now the interesting bit. Design Arena says Kimi K3 is the best design model going. On the one brief where I ran Kimi against Opus 5, it was close enough that I gave Opus the edge on a feeling about some animations, which is not exactly a rigorous tiebreak.

The board isn't wrong. It's answering a different question. Design Arena runs thousands of blinded pairwise votes across thousands of prompts, and their [methodology](https://notes.designarena.ai/methodology/) hides model identity, updates every couple of hours and uses Bradley-Terry ratings. What comes out is average preference across a crowd, and that's a good design for the question they're asking.

It just isn't my question. I'm picking one output for one brief with my own preferences attached. Average preference and my preference are allowed to disagree, and when the top five are within ten Elo of each other, they will disagree all the time. Two of my four picks are GPT models, which the frontend boards don't rank as design leaders at all.

Use the leaderboards to decide which four models to try. Don't use them to decide which one to ship.

## Is it the model, or the system prompt?

A while back I wrote about [the Claude Code frontend design plugin](https://thomas-wiegold.com/blog/claude-code-frontend-design-plugin/) and how much it improved raw output. I've since stopped using it, because the models got good enough that I stopped noticing the difference.

Which leaves a question I can't fully answer: did the weights get better, or did the scaffolding around them get better?

There's real evidence for scaffolding. Anthropic ships a frontend-design skill inside Claude Design specifically to push the model away from that convergence problem. The Claude web app often produces nicer UI than raw Claude Code, and the gap there is instructions, not capability. Design Arena also [publishes its exact system prompts](https://www.designarena.ai/system-prompts), rendered from source, so this half of the question is testable by anyone with a spare afternoon.

My test used plain prompts with no design system, which measures each model's default taste. That's worth measuring, because the default is what most people get. It's also the floor. Every model here would do better work with an actual brief attached, and none of them got one.

If you want the single highest-leverage habit here: constrain before you generate, and use positive constraints rather than negative ones. Telling a model "no blue" fails often. Aliasing the whole blue, indigo and purple range to a named custom scale works, because you've replaced the default instead of forbidding it.

## The workflow I'd actually use now

Generate simple single-file HTML across three or four models, several runs each. Cheap, fast, disposable. Pick the winner on taste alone and ignore the code quality completely, because you're throwing the code away. Then hand that HTML to whichever coding model you trust and convert it into a real React app, a Shopify theme, a WordPress theme, whatever you're building.

This beats one-model-does-everything because the two passes reward opposite things. The design pass wants variance, so you want several models producing several different answers. The build pass wants correctness, so you want one model that doesn't hallucinate imports.

And given how often my picks came down to a vibe, running more variations is worth more than choosing the right model. That's the actual takeaway from all of this.

Which does leave me open to the obvious charge, so I'll make it myself: my test does exactly one run per model, which is precisely the thing I'm telling you not to do. Fair. I was going for breadth across models, which is a different exercise from actually designing something. But if I ran it again I'd do three passes on the early learning brief at minimum, because that's the one where the spread between models was widest and a single sample tells you the least.

### Do you still need to hire a designer?

In the plugin post I said yes, hire one for anything that matters. I'm less sure now, and I'd rather revise that in public than quietly leave it up.

Where I've landed: large company or brand-defining project, hire the designer. SMB or solo operator, the output has crossed the line where it stops looking like slop, and the money is probably better spent elsewhere.

The obvious objection is that AI design is homogenising everything, and the objection is correct. Kyle Chayka called it "Claudian sameness" in The New Yorker this July. Michal Malewicz's Slopless manifesto is an explicit rebellion against it. There's academic backing too: Doshi and Hauser found in _Science Advances_ (volume 10, issue 28, July 2024) that generative AI makes individual writers more creative while making the collective output more similar to itself.

But look at what my advice actually is. Generate a spread, then choose between the options deliberately, even when you can't fully articulate the choice.

That's a direct antidote to convergence. Sameness is what you get from one model, one run, zero judgment. The judgment didn't disappear, it moved. It used to happen while drawing and now it happens while choosing. Smaller job, and I won't pretend otherwise, but it's still the part that decides whether the result is any good.

[Subscribe](https://thomas-wiegold.com/rss.xml)

### Thomas Wiegold

AI Solutions Developer & Full-Stack Engineer with 15+ years of experience building custom AI systems, chatbots, and modern web applications. Based in Sydney, Australia.

[LinkedIn](https://www.linkedin.com/in/wiegold)[GitHub](https://github.com/Keldrik)[X](https://x.com/Keldrik)

### Related Articles

[AI News **Claude Fable 5.1 review: I built an image codec with it** \\
I used Claude Fable 5.1 to build an image codec that beats WebP and a full agency-grade site. Here's what changed from Fable 5, and what it cost.\\
\\
11 min read](https://thomas-wiegold.com/blog/claude-fable-5-1-review/) [AI News **Qwen3.8-Max Review: I Tested Alibaba's 2.4T Model** \\
I ran Alibaba's new 2.4T Qwen3.8-Max-Preview through 4 real coding tests. Results rival Fable 5 and Grok 4.5 — with one big catch: speed.\\
\\
8 min read](https://thomas-wiegold.com/blog/qwen-3-8-max-review/) [AI News **Claude Fable 5 Review: Best AI Coding Model Yet** \\
My hands-on Claude Fable 5 review. I ran my usual coding tests and it one-shotted a poker sim no model ever beat. Best coding model yet, with caveats.\\
\\
11 min read](https://thomas-wiegold.com/blog/claude-fable-5-review/)