# Aspiring Attorneys tutoring operation

The language of Joshua's tutoring business as the brain models it: who a student
is, how they pay, and how they get on the calendar. This is a glossary, not a
spec. Implementation lives in the skills and scripts; decisions live in
`decisions/log.md`.

## Language

### Paying and scheduling

**Package**:
Five or ten hours of tutoring bought upfront through Stripe, with
between-session coaching included.
_Avoid_: Bundle, plan, subscription, credits (credits are the pass's units, not the product)

**Booking pass**:
The prepaid entitlement a student holds when sessions are **owed** to them,
carrying the count owed and the count used. Reachable at `/book/<slug>`.
_Avoid_: Booking link (that is the pass's URL, not the thing), booking access, pass token

**Owed sessions**:
Sessions a student has paid for and not yet taken. The booking pass is the
**only** record of these; if no pass exists, nothing is owed.
_Avoid_: Balance, remaining sessions, package balance (there is no separate balance model)

**Arrangement**:
What a student actually bought, and when. A ten-hour package on a given date,
or pay-per-session at a given rate. Authored on the student's page, durable,
and never rewritten: it is history, not state.
_Avoid_: Plan, deal, terms

**Live status**:
The regenerated mirror of a student's current backend state, including how many
owed sessions remain. Lives in `live-status.generated.md`, is rebuilt from the
backend, and is never hand-edited or hand-corrected.
_Avoid_: Balance sheet, status page

**Single session**:
One tutoring session paid for individually through a Stripe-linked Cal.com
link, rather than out of a package. Needs no booking pass.
_Avoid_: One-off, ad hoc session, hourly

**Three-tier offer**:
The standard offer presented after a consultation: a single session at $45 per
hour, a five-hour package at $40 per hour, and a ten-hour package at $35 per
hour. Each offer carries its own verified action link. A prospect-specific
arrangement agreed during the consultation replaces the standard offer
entirely.
_Avoid_: Pricing menu, universal rate, package discount table

**Consultation**:
A free introductory call, booked through the Cal.com complimentary link. Does
not make the person a student.
_Avoid_: Intro call, discovery call, free session

**Consultation follow-up**:
A message to a prospect who completed a consultation and has not paid. Payment
ends the consultation follow-up stage and moves the person into onboarding. The
message presents the three tutoring offers so the prospect can choose how to
begin.
_Avoid_: Onboarding email, post-payment email, student follow-up, application form email

**Onboarding**:
The stage triggered by confirmed payment when a new student receives LSAT U
access and completes intake inside the platform. It does not require the person
to reply to the consultation follow-up.
_Avoid_: Consultation follow-up, application form, sales follow-up

**LSAT U account creation**:
Creating an account at `lsatprep.study`. A prospect may do this before payment,
but account creation alone does not grant student permissions or begin
onboarding.
_Avoid_: Onboarding, student access, enrollment

### Relationship

One path, and everyone is on it. There is no separate category for a
consultation that never converted; that is a prospect who went quiet.

**Prospect**:
Someone who has had a consultation but has never been taught a session.
_Avoid_: Lead, inquiry, non-student

**Active**:
Someone who is owed sessions, or who has been taught recently.
_Avoid_: Current, enrolled, ongoing

**Lapsed**:
Someone owed nothing who has gone quiet. Applies to a prospect who never
converted as much as to a student who stopped.
_Avoid_: Churned, inactive, dormant, lost

**Student record**:
The folder under `students/` holding everything authored about a person. A
person earns one by being **taught a session**, because teaching is what
produces notes, transcripts, and judgments the brain alone holds. A
consultation alone does not earn a record.
_Avoid_: Profile, student file

### Identity

**Contact address**:
The address a student actually replies from, as evidenced in Gmail. The
student page caches it; a booking pass merely records whatever was typed when
the pass was granted and is never authoritative for contact.
_Avoid_: Email on file, registered email, account email

**7Sage analytics URL**:
The shareable URL copied from a person's 7Sage Analytics page. Its canonical
shape is `https://7sage.com/u/usr_<id>/review`.
_Avoid_: 7Sage login-token URL, drill link, settings link, generic 7Sage URL

### Notes on the model

- **A student with no booking pass is the normal case, not a gap.** It means
  nothing is owed to them; they book single sessions through their Cal.com
  link. Only a student who is owed sessions should hold a pass.
- The two paths are not exclusive. Someone can hold a pass from a package and
  also have a Cal.com single-session link.
- A **revoked** pass is a dead link and must never be treated as a way to book.
  An **exhausted** pass is live but has no owed sessions left.
- Status is authored, not computed: it is a judgment about the relationship.
  But hard evidence that contradicts it gets surfaced rather than silently
  tolerated, the same way a contact address that disagrees with the backend
  does.
- A prospect who never converts has no record, but is still tracked by name so
  follow-up remains possible. Losing sight of them is the failure this guards
  against.
- **Arrangement and live status are different things and live apart.** What was
  bought is authored and permanent; what remains is mirrored and regenerated. A
  count that is typed by hand is the failure mode, not the feature: the
  hand-written mirrors drifted within a day of being written.

### Teaching after a session

**Note**:
What the student sees and what Joshua calls it to the student: a note. It teaches one concept with worked reasoning, real drill questions to try, and a session recap section. It is grounded in a completed tutoring session but organised by the idea, not by what happened first. The teaching content comes from the second brain `corpus/`, not from the transcript alone.
_Avoid_: "Conceptual note" in anything a student reads (Joshua, 2026-11-14: students see "note"). It is a working label for the teaching style only.

**Session recap**:
The part of a post-session note that records what happened in this one-to-one session: what the student worked on, where she slipped, what to do next. It is a section inside the note, never a separate page. Every session is one-to-one, so the recap is written to one student.
_Avoid_: Post-session lesson; a standalone recap page (Joshua, 2026-11-14: "the recap should be in the note")

**Teaching note**:
A note that teaches one idea, with worked reasoning and the session recap inside it. The post-session note is a teaching note. Lanae's note is the model.
_Avoid_: Conceptual note (students never see it), Follow-up, Reference

**Warm-Up**:
A standing set of notes (a picker plus its versions) that gets a student into LSAT mode before a section or test day. It is not built from one session, so it carries no session recap and is not a post-session note.
_Avoid_: Warm-up note, session warm-up

**Post-session note**:
A teaching note assigned to a student after one of her sessions. It carries that session's recap section and teaches one idea. Students still only ever see "note".
_Avoid_: Post-session package, post-session lesson, session write-up (Joshua, 2026-11-14: the post-session note and the post-session homework are the two things; there is no umbrella term)

**Post-session homework**:
The practice Joshua assigns after one of her sessions: drills, activities and timed sections. A note is never homework; it teaches, and homework is what she practises on.
_Avoid_: Post-session package, assignment (see below), "the homework" for a whole session's output

**Assignment**:
One item of any kind on a student's account: a note, a drill, an activity, a bootcamp module or a timed section.
_Avoid_: Task, item, post

**Assigned work**:
Everything on one student's account at a given moment, across all kinds.
_Avoid_: Package, her stuff

**Proposal**:
The set of drafts the agent lays out after a session for Joshua to approve: the post-session note and the post-session homework. Nothing is assigned until he says so; on approval each draft becomes an assignment.
_Avoid_: Package, plan, write-up

**Assign**:
Put an item on a student's account so she can see it. It is the only verb for this. Timing is separate: the **unlock date** is when she can start, and the **due date** is when it is expected back.
_Avoid_: Post, publish, add, release, send (send is only for emails and messages)

**Draft**:
Built but not yet on the student's account. A draft becomes an assignment only when it is assigned.
_Avoid_: Pending, staged

**Status**:
Where an assignment stands on the student's account. Exactly four, the platform's own: assigned, in progress, completed, archived. The only word we add is **draft**, for anything not yet on her account.
_Avoid_: Ready, live, pending, posted

**Adapted note**:
A teaching note whose teaching is reused from an earlier note and whose session recap is written fresh for this student and this session. The recap is never copied between students.
_Avoid_: Copied note, duplicate note, template

**Assigned-work archive**:
A dated folder of every note assigned to one student as HTML, with an index of all her assignments and each note's session transcripts. A record for Joshua; students never see it. Lives at `students/<slug>/assigned-work/`.
_Avoid_: Package, bundle

**Model note**:
Joshua's note for Lanae, "Finding the Conclusion by Asking Why". It is the standard the quality bar is measured against, not a template to copy line for line.
_Avoid_: Template, shell (the shell is the reusable file built from it)

**Flaw breakdown**:
The fixed set of parts every flaw gets inside a note, in this order: name, what it is, example with the jump marked, why it fails, how the right answer words it, and the lookalike trap. Every flaw in a note gets the full breakdown.
_Avoid_: shape, card, block

**Quality bar**:
What every note must meet, whatever its length or kind: Joshua's voice, no banned words, the model note's fonts and visual effects, real platform drill questions where a question appears, and a recap section that quotes what the student said. Notes may differ in shape and length; none falls below the bar.
_Avoid_: Style guide, formula

Rules, confirmed by Joshua on 2026-11-14:

- Every note, including the short ones, meets the same quality bar and uses the same visual standard. The look may vary by kind of note; it never drops below the model note's standard. (Softened from "no lighter shell for short notes" on 2026-11-14: same visual standard, not the same layout.)
- A guided drill already carries its own intro, so it gets a paired note only when it has none or when the note teaches the idea the drill practises. (Changed 2026-11-14 from "every guided drill is paired with a note". Before you start, Reference and Follow-up are no longer kinds of note.)
- Questions inside a note are the real LSAT U practice-drill question, interactive and clickable inline, in the platform's own look and colours. They are not redrawn in the note's palette.
