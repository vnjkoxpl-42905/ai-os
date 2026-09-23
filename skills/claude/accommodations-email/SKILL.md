---
name: accommodations-email
description: >
  Send Joshua's LSAT accommodations email ("Request for Accommodations", LSAC
  Qualified Professional Form PDF attached) to one or more students. Use
  whenever Joshua mentions accommodations together with a person, in any
  wording: "send the accommodations email to X", "accommodations for X",
  "send X the accommodations", "X needs accommodations", "email X about extra
  time", "send X the LSAC form", "run/execute/do the accommodations skill for
  X", "accommodations email to X and Y". Dictation often hears "skill" as
  "scale", so "the accommodations scale" means this skill. Pre-approved
  template: naming the students is the go-ahead to send. Sends and logs itself.
allowed-tools: Bash Read Edit Grep
---

# Accommodations email

**What it does:** sends Joshua's fixed accommodations email to each student he names, with
the LSAC Qualified Professional Form attached, then logs the send. Just give a name:
"accommodations email to Gianna". The same file runs in Claude and Codex, from any folder.

**Approved as a send template on 2026-09-23.** Naming students is the go-ahead, so don't ask
again. Stop and ask only if the recipient's address is unclear (step 1).

## The email (fixed; never reword it)

```
Hello {First}

I want to make sure you get this started and the process moving.

I have all the additional accommodations that might be best suited for you, listed below:

- 100% extra time (double time)
- Stop/start breaks
- Permission to read aloud
- Removal of Experimental Section (Has to be written under "Other")

Before you can request them, you have to register for an LSAT test date. LSAC won't let you start the accommodations request until you're registered.

You can go on the link below and you'll see the forms for that.

https://www.lsac.org/lsat/register-lsat/accommodations/how-request-accommodations-lsat

Thanks
You must complete the Candidate Form / Statement of Need explaining why the requested accommodations are necessary.

Thanks
Joshua
```

Subject: `Request for Accommodations`. Always a new email, never a reply in an existing thread.
The source is `assets/body.html`, and only Joshua changes it. Skip the voice pass and don't tidy
anything, including the doubled "Thanks", which he kept on purpose.

## Step 1: Find each address

The vault is `~/dev/ai-os` on Windows or `~/ai-os` on the Mac.

1. **Roster:** look the name up in `<vault>/students/roster.generated.md`.
2. **Not there, or no email:** search Gmail for the name and read the From/To headers:
   ```
   gws gmail users messages list --params '{"userId":"me","q":"<name>","maxResults":10}'
   gws gmail users messages get --params '{"userId":"me","id":"<id>","format":"metadata","metadataHeaders":["From","To"]}'
   ```
   Use the address only if every matching message agrees. If the student's page has a blank
   `email:`, fill it in so the next lookup is instant.
3. **No address, or two that conflict:** stop and ask Joshua. Never guess.

`--first` is the first name as Joshua writes it. `--slug` is the student's folder name under
`students/`. Leave it out when the folder name is simply their first name, lowercased.

## Step 2: Send

`<skill>` below is this skill's own folder (the base directory shown when it loads).

```
python "<skill>/scripts/send.py" --to <email> --first <First> [--slug <folder>] --dry-run
python "<skill>/scripts/send.py" --to <email> --first <First> [--slug <folder>]
```

- Run the dry run first. It sends nothing and catches a bad command before a student sees it.
- If Joshua names different accommodations, pass one `--item "..."` for each line, on both
  commands. The "Other" note is added to any experimental-section item automatically.
- For several students, do both commands for each, one student per send. Never put two
  students on one email.
- Use `--draft` instead of sending only if Joshua says "draft".

After each send, the script prints `SENT: <email> (<First>), Msg <id>; logged to ...`. It appends
the row to `wiki/send-ledger.md` itself, and a follow-up line to the student's `open-loops.md`
when they have a folder. Report the printed line to Joshua and stop. There's nothing to log by hand.

## Upkeep

- LSAC revises the form every testing year. From June 2027 on, download a fresh copy from
  https://www.lsac.org/document-library/133 and replace it in `assets/`, updating `PDF` in
  `scripts/send.py` if the filename changes.
- Deadlines and LSAC background, for Joshua: `<vault>/wiki/ACCOMMODATIONS-REQUEST-TEMPLATE.md`.
- The master copy is `<vault>/skills/claude/accommodations-email/`. The other copies (Codex
  catalog, project `.claude/skills` and `.agents/skills`, global `~/.claude/skills` and
  `~/.agents/skills`) must be byte-identical copies of it.
