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

**Post-session lesson**:
A student-facing teaching note grounded in a completed tutoring session, with worked reasoning and opportunities to check understanding. Joshua also calls it a session write-up, post-session recap, or session notes.
_Avoid_: Chronological summary (that describes a different, narrower artifact)
