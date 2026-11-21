# The check-in email

Taken verbatim from Joshua's sent mail (201 messages with this subject as of
2026-09-11; the two below are Madison Kline, 2026-09-02, and Kelsey, 2026-08-29).
The script sends exactly this. Do not "improve" it: it is deliberately short, and
the reply it invites ("still good" / "need to reschedule") is the whole point.

```
From: Joshua <contact@aspiringattorneys.com>
To: <student address from the calendar event>
Subject: Consultation check-in

Hi {First},

Just checking in before our consultation today. Looking forward to speaking with you. I just wanted to make sure everything is still good for our meeting.

If anything has come up or you need to reschedule, just let me know.

Best,

Joshua
```

## Facts about how it has always gone out

- **Subject is `Consultation check-in`**, lowercase c, lowercase i. The older
  spec file wrote "Check-In"; the mailbox says otherwise.
- **Always a new email, never a reply.** None of the 201 carried `In-Reply-To`.
  The post-consultation follow-up then replies *into* this thread
  (`Re: Consultation check-in`), so this message is the root of the student's
  thread. Do not go hunting for an earlier thread to reply in; for a first-time
  prospect there usually is none (Cal.com sends the booking confirmation itself).
- **Sent 30 minutes before the start**, to the second, from 2026-08-26 through
  2026-09-03 (an earlier automation). Before that, by hand, 10-25 minutes out.
- **"today"** is always true at T-30 for a 30-minute lead; the sentence needs no
  date logic. If the lead time ever grows past a few hours, revisit this word.
- **First name only**, taken from the Cal.com title (`Consultation between Joshua
  and <Name>`), first token, trailing spaces stripped, capitalised only if the
  prospect typed it all-lowercase. "Hi Farid," and "Hi Sandra," are both right.
- Plain text. No HTML, no signature block, no Meet link (Joshua chose the fixed
  body on 2026-09-11; the Cal.com confirmation already has the link).
- Voice check against `wiki/teaching-voice.md`: "Hi [Name]," greeting, "Best,"
  sign-off, signed "Joshua", "just wanted to make sure" and "let me know" are
  his own signature phrases. No em dashes. Nothing to fix.

## If Joshua changes the wording

Edit `SUBJECT` / `BODY` at the top of `scripts/checkin.py` and this file
together. Keep the subject stable unless he says otherwise: the follow-up skill
and Gmail search both key on it.
