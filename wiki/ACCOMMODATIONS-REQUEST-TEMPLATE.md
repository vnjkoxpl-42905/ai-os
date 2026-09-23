# Accommodations request email

The email Joshua sends a student after they've talked through LSAT testing accommodations.
Based on his 2026-09-19 send to Celia ("Request for Accommodations",
`students/celia-cutler/correspondence/`). LSAC process checked with Firecrawl on 2026-09-23
(scrapes in `.firecrawl/lsac-*.md`).

**Approved 2026-09-23. Sent by the `accommodations-email` skill** (source of truth:
`skills/claude/accommodations-email/assets/body.html`, with the PDF in `assets/`). It's a
pre-approved template: saying "send the accommodations email to X" is the go-ahead. The skill
logs every send in [[send-ledger]].

## The email

Subject: `Request for Accommodations`. Attachment: LSAC Qualified Professional Form
(2026-2027, revised 5/2026).

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

This is Joshua's 2026-09-19 wording with three changes (2026-09-23): "that we discussed" removed, the "process moving" opener added, and the registration line; plus the
"Other" note on the experimental section. The list can change per student. Everything else
stays as written.

## Reference for Joshua (not in the email)

### Accommodation deadlines (2026-2027 cycle, from lsac.org on 2026-09-23)

Accommodation requests are due on the registration deadline, by 11:59 p.m. ET. Not in the email; here so you can answer "when is it due?"

| LSAT | Deadline |
|---|---|
| November 2026 | 2026-10-01 |
| January 2027 | 2026-12-01 |
| February 2027 | 2026-12-29 |
| April 2027 | 2027-02-25 |
| June 2027 | 2027-04-29 |

Confirm the November date on its own admin page. The other dates come from the registration
deadlines table. LSAC says accommodation requests are due on those same dates, but I didn't
check each test's admin page.

### Background

- **Double time is Category 3 ("Exceptional Needs")** unless the student has a severe visual impairment. It needs an *objective rationale based on history and objective evidence* from the clinician, or proof of up to 100% time in a prior academic setting. LSAC can partly or fully deny a request for more time than the student got before, or more than the clinician supports.
- **Stop/start breaks up to 60 minutes total count as Category 1.** Anything over 60 minutes is Category 3. Since August 2026, stop/start breaks also cover sit/stand, walk/stretch, and food.
- **Removing the experimental section is not an official LSAC accommodation.** Test-prep sites (Juris Education, 7Sage forum posts) report students getting it approved under "Other," usually on fatigue grounds. That comes from those sites, not from LSAC.
- **Read aloud may mean a separate room.** LSAC is moving almost everyone to in-center testing for 2026-2027. Separate-room accommodations are listed as a possible reason to test remotely instead, so an approval could change where the student tests. That link is my inference; LSAC doesn't say so directly.
- **Form mechanics.** Fill forms in Adobe Acrobat. LSAC rejects PDFs saved in Mac Preview. Files must be in English, 10 MB max each, and uploaded only once.
- **Returning test takers** who were approved before get the same accommodations automatically. They only file a new request to *add* or *change* accommodations.
