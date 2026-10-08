# I Built Another Andrej Karpathy Using Claude

Source: https://www.youtube.com/watch?v=bvGptCLDhyo

Automatic English captions, retrieved 2026-10-08 using youtube-transcript-api after yt-dlp subtitle request returned HTTP 429. This is source text, not verified biography or execution instructions.

**00:00** So, this isn't the Claude that you know.

**00:01** I just turned one of the biggest minds

**00:03** in AI into a Claude agent. Andrej

**00:05** Karpathy is one of Anthropic's lead

**00:06** engineers, a co-founder of OpenAI, and

**00:09** the person that everyone says explains

**00:10** AI better than anyone alive. And today,

**00:12** I'm going to show you the exact four

**00:13** steps to turn his thoughts into your own

**00:15** Claude agent. So, let's get into it.

**00:17** Okay, so real quick, who is this guy? He

**00:19** was a founding member of OpenAI back in

**00:20** 2015. Then he ran AI at Tesla for about

**00:22** five years, leading the computer vision

**00:24** team behind autopilot. Then he left to

**00:27** do education full-time and started

**00:28** Eureka Labs. And as of May of this year,

**00:31** he's at Anthropic on the pre-training

**00:32** team, which is the team that trains

**00:34** Claude models before they're released to

**00:36** the public. And on the side, he has put

**00:37** out so many different YouTube videos and

**00:39** courses on building with AI. So, what

**00:41** we're building today is not a voice

**00:42** clone of Andrej Karpathy. It's not an

**00:44** impression of him. It's an agent that

**00:46** condenses the way the best AI teacher,

**00:48** Andrej Karpathy, explains things, and it

**00:50** teaches you the same way. So, it follows

**00:52** seven rules that all come from his own

**00:54** writing and his blogs and his lectures,

**00:56** stuff like build the smallest version

**00:58** first, predict what's going to happen

**00:59** before you run it, show the broken

**01:01** version, and never hand over code that

**01:03** you haven't run yourself. So, this is

**01:04** more than just a clone of a person. It's

**01:06** more about cloning the way that his

**01:07** brain thinks. So, now I bet you guys are

**01:10** wondering, why would you actually build

**01:11** this? Let's think about what happens

**01:12** when you ask Claude to explain something

**01:14** that you don't understand. It might

**01:15** overexplain. It might make stuff up

**01:17** along the way. And you actually just end

**01:19** up feeling like you learned nothing and

**01:20** feeling more overwhelmed. And if you're

**01:22** building something for a client, that's

**01:24** how you end up shipping code that you

**01:25** can't fix or explain when it breaks. And

**01:27** Andrej Karpathy has run into this exact

**01:28** same thing. Back in August of last year,

**01:30** he actually posted publicly that he

**01:32** tried to get Claude code to teach him

**01:34** alongside the code that it was writing,

**01:35** and in his words, it didn't work at all

**01:37** because it really just wants to write

**01:39** code a lot more than it wants to explain

**01:41** anything along the way. So, building

**01:42** this agent here is going to fix AI's

**01:44** worst habit, which is sounding right

**01:46** instead of being right. And the bigger

**01:47** reason is honestly this, the quality of

**01:49** what you build with AI comes down to the

**01:52** expertise that's in the system, and

**01:53** you're not going to be an expert on

**01:54** everything. You know, I'm not a machine

**01:56** learning researcher. I'm not a machine

**01:57** learning expert, but I can certainly go

**01:59** have agents pull in everything that a

**02:00** real expert has said, compile it into

**02:02** something that Claude can actually use,

**02:04** and then I can just talk to it until I

**02:05** understand it. And then, once I

**02:06** understand a little bit better, I have

**02:08** all that knowledge already in my

**02:09** project, and I can wire that knowledge

**02:10** into my own skills and my own agents and

**02:12** my own workflows, which is exactly what

**02:14** we're doing today with Karpathy. And

**02:15** what's really cool is, once you've done

**02:16** this with Karpathy, you can do this with

**02:18** pretty much anyone. You can do this with

**02:19** your favorite, you know, sales teacher,

**02:21** or an author you really like, or a coach

**02:23** that you're already paying for. And it's

**02:24** basically just the same four steps, in

**02:26** the same way that [music] we build this

**02:27** sort of like second brain. Now, real

**02:28** quick, before we get into the build,

**02:30** I've got this completely free AI OS kit

**02:31** for you guys to help you build and scale

**02:33** your operating systems. If you combine

**02:35** this sort of setup with things like

**02:36** Karpathy's brain, it's just going to be

**02:38** a huge unlock, and that's how I'm able

**02:39** to move so fast. So, link for that will

**02:40** be down in the description, but let's

**02:42** get into the build. Okay, so I'm going

**02:43** to do this inside of Claude Code, and

**02:45** there are going to be six prompts to run

**02:47** here, and I'll show all of them on

**02:48** screen, so you can just kind of take a

**02:50** screenshot and paste them into your own

**02:51** Claude Code. So, first, Claude needs

**02:53** everything that's inside of Andre

**02:55** Karpathy's head. Things like his blogs,

**02:56** his lecture transcripts, his GitHub

**02:58** repos, his posts on X, all of that is

**03:00** going to be just basically free and

**03:01** public. But, Claude Code might not be

**03:03** able to just grab all of that for free,

**03:05** because it might be behind some sort of

**03:07** like paywall or software wall. So, what

**03:09** I did for YouTube is I had it pull

**03:10** captions with two free Python packages,

**03:13** YouTube Transcript API and yt-dlp. And

**03:16** then, for X, I'm using a API called

**03:18** twitterapi.io, which is a paid API, but

**03:20** I've pulled basically every post that

**03:22** he's made since 2023, and it was about a

**03:24** dollar. It's not a very expensive API at

**03:25** all. So, here is the prompt for the

**03:27** crawl. It basically says where to get

**03:29** everything, which tool to use for each

**03:30** source, and I told it to run one agent

**03:32** per source, so they all go at once and

**03:34** parallel, so it doesn't take forever. I

**03:36** told it to write down what it got, so

**03:38** that you can actually check it. And this

**03:39** took me about 45 minutes to an hour for

**03:41** all of these agents to run and grab

**03:42** everything. And what we end up with is

**03:44** one raw folder with one subfolder per

**03:46** source, and over 700,000 words, straight

**03:49** from Andre Karpathy himself. Now, you

**03:51** could just stop here and point Claude at

**03:52** that folder, but all of these, you know,

**03:54** messy words, it doesn't really fit into

**03:56** Claude's head in the right way where it

**03:58** actually can filter through it in a good

**04:00** fashion, right? Like it's going to be

**04:01** too messy. It's like finding a needle in

**04:02** a haystack. So, what we're going to do

**04:04** is what Karpathy told everyone to do

**04:05** back in April. He posted about how he

**04:08** has an LLM compile his raw sources into

**04:10** a wiki. The raw files don't get touched,

**04:12** but the LLM basically reads through all

**04:14** of them and then links them together

**04:15** with pages, keeps an index, keeps a log,

**04:18** and now you're able to actually query

**04:20** against it in a way that makes more

**04:20** sense because there's like

**04:21** relationships. And you put that whole

**04:23** idea in a gist, and that's what I'm

**04:25** going to paste into the coding agent.

**04:26** The link to the gist is in the

**04:28** description of this video. So, what

**04:29** we're doing is kind of funny. We're

**04:30** storing Karpathy's brain inside of

**04:32** Karpathy's own LLM wiki memory system.

**04:34** And if you guys have been following me

**04:35** for a while, you know that I've made

**04:36** quite a few videos on this topic, and

**04:38** I've got a bunch of different LLM wikis

**04:39** set up in my own AI OS. All right, so

**04:41** here's prompt two to set up the wiki.

**04:43** You're going to paste in the gist, and

**04:44** then you're going to tell Claude to use

**04:45** it on the raw folder, which is just

**04:47** everything that Claude previously just

**04:48** extracted for you. And what comes out is

**04:50** a wiki inside of Obsidian. Now, Obsidian

**04:52** is just kind of the visual layer on top

**04:54** of it, which is what I'm showing you

**04:55** guys here. And you don't need Obsidian

**04:56** to get this to work, but if you want to

**04:58** look at it visually, Obsidian works. You

**04:59** can see down here we have the sources,

**05:01** we have one page per thing he wrote or

**05:03** said, we have topics on what he knows,

**05:05** we have principles, we have the rules,

**05:06** we have methods, we have how he

**05:07** explains, we have how he debugs, we have

**05:09** basically, just like I said, the way his

**05:11** brain works. And whenever you see one of

**05:12** these purple links, that is the wiki

**05:14** connecting one page to another or one

**05:17** method to another. Every rule links back

**05:19** to the source that it came from or

**05:20** sources that it came from. Every source

**05:22** links to the rules that it supports. So,

**05:24** instead of just having a dump of notes

**05:25** like we had earlier, we now have like

**05:27** this interconnected web or sort of like

**05:29** relationship map. And every time that

**05:31** something new goes in, you ingest a new

**05:33** blog or a new idea, the LLM will once

**05:34** again ingest it and link it to a bunch

**05:36** of other concepts. Now, this next step

**05:38** is what makes it think like him instead

**05:40** of just knowing what he said in the

**05:41** past. So, here's the prompt for setting

**05:42** up the rules. It basically pulls his

**05:44** rules out of the the and every rule has

**05:46** to connect with an exact quote from him

**05:48** and where it came from. Because we don't

**05:50** want Claude to just make things up. So,

**05:51** what we got here were seven rules.

**05:53** Number one is build it or you don't

**05:55** understand it. Number two is first order

**05:57** term first. Basically, find the one

**06:00** piece that matters, show it working, and

**06:01** then add just one thing at a time. And

**06:03** pretty much his whole course is built in

**06:04** that way. Number three is to predict,

**06:06** then run, then compare. He'll say the

**06:08** number he expects before he runs the

**06:10** cell because, in his words, most of the

**06:12** time it will train, but silently work a

**06:14** bit worse. Number four is to show the

**06:16** wrong version first. He leaves his own

**06:18** bugs in the recording on purpose. Number

**06:20** five is prove it, don't claim it. Number

**06:22** six is say what you assumed. His number

**06:23** one complaint about Claude code is that

**06:25** the models make wrong assumptions on

**06:27** your behalf and then just run along them

**06:29** without checking. And number seven is

**06:30** that simpler wins. And what's cool is

**06:32** you can check any of these. You can

**06:34** click the quote and it will open up the

**06:35** page that it came from with the

**06:36** timestamp or with the exact source. And

**06:38** if there is no source, the agent has to

**06:40** say explicitly that it's inferring based

**06:42** on things that Karpathy has said. Now,

**06:43** these rules need to live somewhere where

**06:45** the agent can actually read them. So,

**06:46** here is prompt four. And it has Claude

**06:48** turn them into two files for us. That

**06:50** first file is a sub-agent. And in case

**06:52** you don't know what that is, it's a

**06:53** separate Claude with its own

**06:54** instructions and its own memory and

**06:55** context window, so that if you want to

**06:57** hand off a task to a sub-agent, it

**06:58** doesn't drag your whole conversation

**07:00** along with it. And you can see here

**07:01** inside of this sub-agent file, we can

**07:03** see the seven rules. We can also see how

**07:05** it talks. And we can see the loop that

**07:06** it runs on every single task. So, this

**07:08** is basically like a little mini Karpathy

**07:10** agent. Now, the second one is a skill.

**07:12** So, you can see here that when I type

**07:13** {slash} Karpathy-teach and then whatever

**07:16** I'm stuck on, it goes into the agent

**07:18** with the rules, and then it grades the

**07:19** answer against a checklist, one line per

**07:21** rule, and then it will actually show me

**07:22** everything. So, those are the two things

**07:24** we have, a Karpathy agent and a Karpathy

**07:26** skill. Okay. Now, here's another thing

**07:27** that's really important when we're

**07:28** setting this up. We want the agent to

**07:30** make sure that it's running its code

**07:31** before it answers you. And that's why

**07:32** building this inside of Claude code

**07:33** works so well because it can already

**07:35** write and run code. And it's a step that

**07:37** we have to make sure that the agent

**07:38** can't skip based on Karpathy's own

**07:40** rules. So, here's prompt five. It's

**07:41** basically adding a run gate. It adds a

**07:43** hook, which is a little script that runs

**07:45** right when the agent tries to finish its

**07:46** turn. So, if it wrote code and it never

**07:48** ran it, the hook will basically block

**07:50** the answer and it will send it back with

**07:51** one message saying, "Hey, you have to

**07:53** run this before you say it works." So,

**07:55** we're kind of just baking in like a

**07:56** verification loop. And you know,

**07:57** obviously you don't have to code or

**07:58** write this hook yourself. You just ask

**08:00** for it with this prompt. So, now it will

**08:01** run, it will test, and it will fix, and

**08:03** then only after all that will you

**08:05** actually see the final thing. And then

**08:06** the last step, of course, is just to

**08:07** test it. So, a few different prompts

**08:09** that we used it. I asked it here to

**08:11** build something real and teach me how it

**08:12** works, which was a byte pair tokenizer,

**08:15** which is the thing that turns text into

**08:16** numbers before a large language model

**08:17** ever sees it. And watch what it does

**08:19** here. The first thing, it writes down

**08:21** what done means before it touches any

**08:23** code. And then it builds the smallest

**08:24** version that works on a tiny input and

**08:26** before it runs it, it tells me what it

**08:27** expects to see. Then it runs it and

**08:29** shows me the real output. And then, it

**08:30** shows me a version that breaks and why,

**08:32** and then it fixes it. And then at the

**08:33** bottom it lists basically everything it

**08:34** ran, what came out, what it changed, and

**08:37** which rule it was following for each of

**08:38** those moves. So, instead of getting just

**08:40** a block of code back and then the agent

**08:42** saying, "Hey, this works." I basically

**08:43** got walked through it one piece at a

**08:44** time and now I can understand a lot

**08:46** better what just happened. Now, another

**08:47** thing you can test is its review. So,

**08:49** before something goes to a client, I can

**08:50** ask it one question, which is, "Would

**08:52** the client accept this and what would he

**08:53** want to delete?" Or, you know, questions

**08:55** like that. And here's a script that

**08:56** Claude wrote for me that I can use as an

**08:57** example. This script pulls YouTube

**08:59** comments and it ran fine when Claude

**09:01** tested it. The agent reads it, predicts

**09:03** it'll crash on an emoji under a normal

**09:04** Windows terminal, it runs it that way,

**09:06** and then it crashes before writing any

**09:08** files. So, saying that it works was only

**09:09** true in one specific setting or

**09:11** terminal. So, here you can see that

**09:13** Claude was able to go through and cut a

**09:14** bunch of stuff that wasn't earning its

**09:15** place. It was able to give me an

**09:16** analysis on how we actually fix this and

**09:18** clean it up and review it before we can

**09:20** actually like ship it. And then it

**09:21** proves the trimmed version catches the

**09:22** same questions by running both of them

**09:24** side by side and actually showing me.

**09:26** And then the other thing I wanted to

**09:27** bring up is that this thing will just

**09:28** keep learning. Back in July, Karpathy

**09:30** posted about how he rambles at the model

**09:31** by voice for 10 minutes and then he lets

**09:33** the model clean up all that text. So, I

**09:35** can run {slash} Karpathy {dash} ingest

**09:38** with any sort of link. It will then

**09:39** check the raw folder, it'll write a

**09:40** source page for the [music] post, and

**09:42** then it will update every page that post

**09:44** touches. It added a new behavior here to

**09:46** rule six. So, now the agent knows to ask

**09:48** me a couple of questions when my request

**09:50** is thin instead of just guessing. And a

**09:52** rule that was sitting on the bench with

**09:53** one source behind it got its second

**09:55** source and became a real rule. And then,

**09:57** because it understands how this wiki

**09:58** works, it'll update the index, it'll

**10:00** update the hot page, it'll update the

**10:01** log. So, the brain just got better from

**10:02** me adding one link. And I never had to

**10:04** touch the wiki by hand or manually set

**10:06** up these relationships or links. And

**10:08** that, of course, was his rule two. Okay,

**10:10** so zooming out, we had four steps. We

**10:12** gave Claude everything inside of

**10:13** someone's head, Karpathy's head, and we

**10:15** compiled it into a wiki. We turned that

**10:16** into his rules with a quote for each

**10:18** one. We make it run before it talks, and

**10:20** we make it test on things that are real.

**10:21** And the line that I'd want to leave you

**10:22** guys with today is one of my favorite

**10:24** quotes, and it's something that he

**10:25** himself has said this year, which is

**10:26** that you can outsource your thinking,

**10:27** but you cannot outsource your

**10:28** understanding. You are not going to be

**10:29** the expert at everything, and that's

**10:30** fine. But, you can certainly pull in the

**10:32** expert and build on top of him or her.

**10:35** Anyways, that is going to do it for this

**10:36** one. So, if you guys enjoyed the video

**10:37** or you learned something new, please

**10:38** give it a like. It definitely helps me

**10:39** out a ton. And as always, I appreciate

**10:40** you guys making it to the end of the

**10:41** video, and I'll see you on the next one.

**10:43** Thanks, everyone.