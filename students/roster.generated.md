---
title: Student roster
type: operating-layer
tags: [students, operating-layer, generated]
generated: true
status: active
---

# Student roster

**Generated file — do not hand-edit.** Rebuild with:

```
python3 system/scripts/build-roster.py
```

Name, email, and status come from the student's own `<slug>.md`
frontmatter (primary, authored). Sessions and last-session come from the
Gemini transcript inventory. To correct a name or email, edit the student's
page and regenerate; editing this file does nothing.

**Booking columns are read live** from the backend's `booking_passes` on each
rebuild, so they are as fresh as the last run and never a stale local copy.
Revoked passes are not shown: a revoked slug is a dead link.

Last-contact is deliberately absent. Gmail owns it.

21 student folders. Booking state read live.

| Student | Email | Status | Sessions | Last session | Booking link | Pass | Credits |
|---|---|---|---|---|---|---|---|
| [[adriana-varea/adriana-varea\|Adriana Varea]] | adrianavarea9@gmail.com | active | 4 | 2026-06-02 | **none** | - | - |
| [[amanda/amanda\|Amanda Huynh]] | amhuynh@asu.edu | active | - | ? | **none** | - | - |
| [[asia/asia\|Asia]] | atamaami@gmail.com | active | - | ? | /book/asia-shrzc7qegvt8ubvny3mnazd3mg | active | 2/5 |
| [[avneet-natt/avneet-natt\|Avneet Natt]] | avneet.2725@gmail.com | active | - | ? | **none** | - | - |
| [[celia-cutler/celia-cutler\|Celia Cutler]] | celiacutler@gmail.com | active | - | ? | /book/celia-hpns2qrxwwb4dvxcx7k4mhmtts | exhausted | 10/10 |
| [[charles-moore/charles-moore\|Charles Moore]] | moorecamooreca1@gmail.com | active | - | ? | /book/charles-jh2qvp2v3p75ktdevgdc9eh4cx | active | 5/20 |
| [[dakota/dakota\|Dakota]] | dakota.brown2010@gmail.com | active | 7 | 2026-06-19 | /book/dakota-2gkn4jy2u4dgy5c6watvufb5hc | active | 0/2 |
| [[david-salgado/david-salgado\|David Salgado]] | davidsalgado0722@gmail.com | active | 3 | 2026-06-07 | **none** | - | - |
| [[ethan/ethan\|Ethan]] | trie@usc.edu | active | 3 | 2026-06-28 | /book/ethan | active | 1/10 |
| [[favour/favour\|Favour]] | favourx23@gmail.com | active | 1 | 2026-07-07 | **none** | - | - |
| [[fernande-charleus/fernande-charleus\|Fernande Charleus]] | fernandecharleus@gmail.com | active | - | ? | /book/fernande-u42u7v46wzdtett29dhm2jbu56 | exhausted | 1/1 |
| [[ivory-johnson/ivory-johnson\|Ivory Johnson]] | ivoryj.johnson3@gmail.com | active | - | ? | **none** | - | - |
| [[nicole/nicole\|Nicole]] | nspinelli44@gmail.com | active | 1 | 2026-06-10 | /book/nicole | active | 1/2 |
| [[non-students/non-students\|Non Students]] | ? | ? | - | ? | **none** | - | - |
| [[ore/ore\|Oreoluwa]] | oreoluwavjames@gmail.com | active | - | ? | /book/oreoluwa-pgavqgtp3weqxmuxy2axt96495 | active | 0/10 |
| [[sofia/sofia\|Sofia]] | sofiaminassian@gmail.com | active | 6 | 2026-07-12 | /book/sofia-k2anhqmpvj6swt2fj7uvdryrvt | active | 14/17 |
| [[steven-morris/steven-morris\|Steven Morris]] | hsmcharlotte@gmail.com | active | - | ? | /book/steven-kx5ach8v2anju9cd8xa9d5hvty | exhausted | 2/2 |
| [[vinay-kalva/vinay-kalva\|Vinay Kalva]] | workemail.vinay@gmail.com | active | - | ? | /book/vinay-r353kkhbwdazhkrt5fk7nq9zj9 | active | 9/10 |
| [[whit-wilson/whit-wilson\|Whit Wilson]] | whitwilson929@gmail.com | active | - | ? | **none** | - | - |
| [[yahunatan-zetvy/yahunatan-zetvy\|Yahunatan Zetvy]] | ynproemail@gmail.com | active | 2 | 2026-07-15 | /book/yahunathan | active | 11/12 |
| [[zeina-borji/zeina-borji\|Zeina Borji]] | zeina.borji5@gmail.com | onboarding | - | ? | **none** | - | - |

## Booking pass exhausted

Has a live link, but no credits left. The page tells them "you've used all your sessions".

- [[celia-cutler/celia-cutler\|Celia Cutler]] (10/10 used)
- [[fernande-charleus/fernande-charleus\|Fernande Charleus]] (1/1 used)
- [[steven-morris/steven-morris\|Steven Morris]] (2/2 used)

## No booking pass (normal)

**Not a gap.** No pass means no sessions are owed. These students schedule individual sessions through their Cal.com link; a pass exists only when a package has been bought and sessions remain. Listed so it is clear there is no link to send them, not as a to-do.

- [[adriana-varea/adriana-varea\|Adriana Varea]]
- [[amanda/amanda\|Amanda Huynh]]
- [[avneet-natt/avneet-natt\|Avneet Natt]]
- [[david-salgado/david-salgado\|David Salgado]]
- [[favour/favour\|Favour]]
- [[ivory-johnson/ivory-johnson\|Ivory Johnson]]
- [[non-students/non-students\|Non Students]]
- [[whit-wilson/whit-wilson\|Whit Wilson]]
- [[zeina-borji/zeina-borji\|Zeina Borji]]

## Status disagrees with the evidence

Status is your judgment and is never auto-corrected. These are flagged because the record and the evidence point different ways.

- [[adriana-varea/adriana-varea\|Adriana Varea]]: recorded as active but owed nothing and not taught since 2026-06-02 (113 days)
- [[david-salgado/david-salgado\|David Salgado]]: recorded as active but owed nothing and not taught since 2026-06-07 (108 days)
- [[favour/favour\|Favour]]: recorded as active but owed nothing and not taught since 2026-07-07 (78 days)

## Email disagrees with the backend

The folder and the booking pass hold different addresses. Confirm which is current before sending anything.

- [[ethan/ethan\|Ethan]]: folder `trie@usc.edu` vs backend `ethantrie@gmail.com`

## Passes with no student folder

Usable booking passes that match nobody in `students/`. Either a missing folder or a leftover test row.

- `josh-tydjsc64zrvsfjhdybvtq25vgb` — josh (joshua.fisseha01@gmail.com), active
- `lydia` — Lydia (lydiahqllee@gmail.com), exhausted
- `c-j85cs4pes2eedtw9ghg7cv4rgn` — C. Alexander (clairealexander.nyc@gmail.com), active
- `sofia` — Sofia Minassian (sofiaminassian@gmail.com), exhausted
- `sandra-wc4kt2xjhcbxc4bqbytas9qmad` — Sandra (koohsandra@gmail.com), active

## Missing an email

Cannot be contacted from the brain until the address is added to the student's frontmatter.

- [[non-students/non-students\|Non Students]]

## Known gaps

Transcripts exist for people with no student folder. See the `## Unresolved` section of [[_aliases]] and run `python3 system/scripts/transcript-inventory.py --unmatched`.
