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

Machine-readable twin: `students/roster.generated.json`, written by the
same run from the same rows. The command center's student picker reads
it through `/api/students`. A folder with no `<slug>.md` page is not a
student and appears in neither file.

Name, email, and status come from the student's own `<slug>.md`
frontmatter (primary, authored). Sessions and last-session come from the
Gemini transcript inventory. To correct a name or email, edit the student's
page and regenerate; editing this file does nothing.

**7Sage** is the second column on purpose: it is a core part of the student's
profile and must never be missed. A linked value means they are set up for the
`7sage-onboarding` / `7sage-update` skills; **⚠️ NOT SET** means their
`7sage_review:` frontmatter URL is missing and they cannot be pulled. The
"Not set up on 7Sage" section below lists every such student.

**Booking columns are read live** from the backend's `booking_passes` on each
rebuild, so they are as fresh as the last run and never a stale local copy.
Revoked passes are not shown: a revoked slug is a dead link.

Last-contact is deliberately absent. Gmail owns it.

18 student folders. Booking state read live.

| Student | 7Sage | Email | Status | Sessions | Last session | Booking link | Pass | Credits |
|---|---|---|---|---|---|---|---|---|
| [[adriana-varea/adriana-varea\|Adriana Varea]] | [review](https://7sage.com/u/usr_030dpzlBMSz4DRX5SKKOfW/review) | adrianavarea9@gmail.com | lapsed | 4 | 2026-06-02 | **none** | - | - |
| [[asia-tamaami/asia-tamaami\|Asia Tamaami]] | [review](https://7sage.com/u/usr_032mRfIVGbRhtRbkrNpJW5/review) | atamaami@gmail.com | active | - | ? | /book/asia-shrzc7qegvt8ubvny3mnazd3mg | active | 2/5 |
| [[non-students/bella-lorenzo/bella-lorenzo\|Bella Lorenzo]] | **⚠️ NOT SET** | bellalorenzo595@gmail.com | active | 2 | 2026-07-02 | **none** | - | - |
| [[non-students/c-alexander/c-alexander\|C. Alexander]] | **⚠️ NOT SET** | clairealexander.nyc@gmail.com | active | 1 | 2026-06-19 | /book/c-j85cs4pes2eedtw9ghg7cv4rgn | active | 0/1 |
| [[celia-syrocki/celia-syrocki\|Celia Syrocki]] | [review](https://7sage.com/u/usr_030mKLrP8oA6e46yNIzQVx/review) | celiacutler@gmail.com | active | - | ? | /book/celia-hpns2qrxwwb4dvxcx7k4mhmtts | active | 6/10 |
| [[dakota/dakota\|Dakota]] | [review](https://7sage.com/u/usr_033429aLhr7xbgxbF1AM3n/review) | dakota.brown2010@gmail.com | active | 7 | 2026-06-19 | /book/dakota-2gkn4jy2u4dgy5c6watvufb5hc | active | 0/2 |
| [[david-salgado/david-salgado\|David Salgado]] | [review](https://7sage.com/u/usr_02yzfmW4LeOYZ1FdDHEC6W/review) | davidsalgado0722@gmail.com | active | 3 | 2026-06-07 | **none** | - | - |
| [[ethan/ethan\|Ethan]] | **⚠️ NOT SET** | trie@usc.edu | active | 3 | 2026-06-28 | /book/ethan | active | 1/10 |
| [[non-students/kaden-forges/kaden-forges\|Kaden Forges]] | **⚠️ NOT SET** | ? | lapsed | 1 | 2026-05-19 | **none** | - | - |
| [[non-students/lydia/lydia\|Lydia]] | [review](https://7sage.com/u/usr_030FDEkRfWiaFXB85F8rpF/review) | lydiahqllee@gmail.com | active | 8 | 2026-07-13 | /book/lydia | exhausted | 1/1 |
| [[non-students/meghan/meghan\|Meghan]] | **⚠️ NOT SET** | meglizzy912@gmail.com | active | 5 | 2026-06-03 | **none** | - | - |
| [[nicole/nicole\|Nicole]] | **⚠️ NOT SET** | nspinelli44@gmail.com | active | 1 | 2026-06-10 | /book/nicole | active | 0/2 |
| [[priyanka-nambiar/priyanka-nambiar\|Priyanka Nambiar - Profile]] | [review](https://7sage.com/u/usr_033CCn4peoTfr2XMH3sgQX/review) | ? | ? | - | ? | **none** | - | - |
| [[sofia/sofia\|Sofia]] | [review](https://7sage.com/u/usr_031dHpQ3aQrsJM3i9Ys5wB/review) | sofiaminassian@gmail.com | active | 6 | 2026-07-12 | /book/sofia-k2anhqmpvj6swt2fj7uvdryrvt | active | 4/10 |
| [[steven-morris/steven-morris\|Steven Morris - Profile]] | [review](https://7sage.com/u/usr_032iy0TWkPN5SZpEuSkw4x/review) | ? | ? | - | ? | /book/steven-kx5ach8v2anju9cd8xa9d5hvty | exhausted | 2/2 |
| [[non-students/thaniuska-vivas/thaniuska-vivas\|Thaniuska Vivas]] | **⚠️ NOT SET** | thanivivas@gmail.com | lapsed | 1 | 2026-05-08 | **none** | - | - |
| [[vinay-kalva/vinay-kalva\|Vinay Kalva]] | [review](https://7sage.com/u/usr_033Qu2yTr4I5vkERVDyPFg/review) | workemail.vinay@gmail.com | active | - | ? | /book/vinay-r353kkhbwdazhkrt5fk7nq9zj9 | active | 7/10 |
| [[yahunatan-zetvy/yahunatan-zetvy\|Yahunatan Zetvy]] | [review](https://7sage.com/u/usr_0328ZS7IYo3u2qTpCs2UtQ/review) | ynproemail@gmail.com | active | 2 | 2026-07-15 | /book/yahunathan | active | 5/9 |

## Booking pass exhausted

Has a live link, but no credits left. The page tells them "you've used all your sessions".

- [[non-students/lydia/lydia\|Lydia]] (1/1 used)
- [[steven-morris/steven-morris\|Steven Morris - Profile]] (2/2 used)

## No booking pass (normal)

**Not a gap.** No pass means no sessions are owed. These students schedule individual sessions through their Cal.com link; a pass exists only when a package has been bought and sessions remain. Listed so it is clear there is no link to send them, not as a to-do.

- [[adriana-varea/adriana-varea\|Adriana Varea]]
- [[non-students/bella-lorenzo/bella-lorenzo\|Bella Lorenzo]]
- [[david-salgado/david-salgado\|David Salgado]]
- [[non-students/kaden-forges/kaden-forges\|Kaden Forges]]
- [[non-students/meghan/meghan\|Meghan]]
- [[priyanka-nambiar/priyanka-nambiar\|Priyanka Nambiar - Profile]]
- [[non-students/thaniuska-vivas/thaniuska-vivas\|Thaniuska Vivas]]

## Status disagrees with the evidence

Status is your judgment and is never auto-corrected. These are flagged because the record and the evidence point different ways.

- [[david-salgado/david-salgado\|David Salgado]]: recorded as active but owed nothing and not taught since 2026-06-07 (80 days)
- [[non-students/meghan/meghan\|Meghan]]: recorded as active but owed nothing and not taught since 2026-06-03 (84 days)

## Email disagrees with the backend

The folder and the booking pass hold different addresses. Confirm which is current before sending anything.

- [[ethan/ethan\|Ethan]]: folder `trie@usc.edu` vs backend `ethantrie@gmail.com`

## Passes with no student folder

Usable booking passes that match nobody in `students/`. Either a missing folder or a leftover test row.

- `josh-tydjsc64zrvsfjhdybvtq25vgb` — josh (joshua.fisseha01@gmail.com), active
- `sofia` — Sofia Minassian (sofiaminassian@gmail.com), exhausted
- `fernande-u42u7v46wzdtett29dhm2jbu56` — Fernande Charleus (fernandecharleus@gmail.com), exhausted
- `oreoluwa-pgavqgtp3weqxmuxy2axt96495` — Oreoluwa James (oreoluwavjames@gmail.com), active

## Not set up on 7Sage

**Action item.** These students have no `7sage_review:` URL in their frontmatter, so their 7Sage analytics cannot be pulled. Add the `https://7sage.com/u/usr_.../review` link to each one's page and regenerate.

- [[non-students/bella-lorenzo/bella-lorenzo\|Bella Lorenzo]]
- [[non-students/c-alexander/c-alexander\|C. Alexander]]
- [[ethan/ethan\|Ethan]]
- [[non-students/kaden-forges/kaden-forges\|Kaden Forges]]
- [[non-students/meghan/meghan\|Meghan]]
- [[nicole/nicole\|Nicole]]
- [[non-students/thaniuska-vivas/thaniuska-vivas\|Thaniuska Vivas]]

## Missing an email

Cannot be contacted from the brain until the address is added to the student's frontmatter.

- [[non-students/kaden-forges/kaden-forges\|Kaden Forges]]
- [[priyanka-nambiar/priyanka-nambiar\|Priyanka Nambiar - Profile]]
- [[steven-morris/steven-morris\|Steven Morris - Profile]]

## Known gaps

Transcripts exist for people with no student folder. See the `## Unresolved` section of [[_aliases]] and run `python3 system/scripts/transcript-inventory.py --unmatched`.
