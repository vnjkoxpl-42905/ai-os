# Student ↔ Platform Identity Map

Built 2026-09-07. **Emails verified** against the live platform via
`admin-manage-users`, then cross-checked against `students/roster.generated.md`.
This is no longer name-inference — every row below carries the account's real
email address.

Why it exists: assigning work to "every student in my records" requires knowing
which platform account is which student. Three lists disagree, so the mapping
cannot be inferred at assign time.

## The three lists

| Source | Count |
|---|---|
| `students/` folders | 16 |
| `students/roster.generated.md` | 19 |
| Platform accounts | 35 |

The platform is the only one that can receive an assignment, and the least
curated.

## Real students — verified, safe to assign

| Student | Platform name | Email |
|---|---|---|
| Adriana Varea | Adriana Varea | adrianavarea9@gmail.com |
| Antonio Martins | Antonio | antoniomartins0146@gmail.com |
| Asia Tamaami | Asia | atamaami@gmail.com |
| Bella Lorenzo | Isabella Lorenzo | bellalorenzo595@gmail.com |
| C. Alexander | C. Alexander | clairealexander.nyc@gmail.com |
| Celia Syrocki | Celia | celiacutler@gmail.com |
| Dakota | Dakota Brown | dakota.brown2010@gmail.com |
| David Salgado | David Salgado | davidsalgado0722@gmail.com |
| Ethan | Ethan Trie | ethantrie@gmail.com ⚠ |
| Favour | Favour | favourx23@gmail.com |
| Kaden Forges | Kaden Forges | kadenforges@gmail.com |
| Lexi | Lexi A | lexiadler@gmail.com |
| Lydia | Lydia | lydiahqllee@gmail.com |
| Meghan | Meghan Mullins | meglizzy912@gmail.com |
| Nicole | Nicole Spinelli | nspinelli44@gmail.com |
| Priyanka Nambiar | *(no display name)* | priyanka_nambiar@brown.edu |
| Sofia | Sofia Minassian | sofiaminassian@gmail.com |
| Steven Morris | Steven Morris | hsmcharlotte@gmail.com |
| Vinay Kalva | Vinay Kalva | workemail.vinay@gmail.com |
| Yahunathan Zetvy | Yahunathan | ynproemail@gmail.com |

⚠ **Ethan**: the roster records `trie@usc.edu`, the platform account is
`ethantrie@gmail.com`. Same person, two addresses. Platform mail goes to the
gmail one.

**Priyanka** has no display name set, so she shows as a raw email address in the
assign picker. Worth setting.

## Resolved since the first draft

**"Steven" always means Steven Morris** — `hsmcharlotte@gmail.com`. Assign to him
without hesitation. The earlier "possible duplicate account" warning was wrong
and is retired.

## Still unresolved

- **Thaniuska Vivas** — vault folder and roster row, **no platform account**.
  Cannot be assigned anything until she signs up.
- **Amanda** — vault folder, no roster row, no platform account under that name.

## Not students

Three of these are Joshua's own accounts:

- `Joshua Fisseha` — contact@aspiringattorneys.com (the admin account)
- `josh` — joshua.fisseha01@gmail.com
- `lsatmaster` — joshuafisseha@hotmail.com

Two are throwaway test accounts: `tester` and `mark`, both on `duck.com`.

## Real people, no vault record (7)

Ivory Johnson · Fernande charleus · Sandra · Charles · Andrew · Ore · Reet ·
Emily · Habil

These are live accounts with real personal email addresses. Some may be current
students who never got a vault folder; others may be consultations who signed up
and never converted. **Do not bulk-assign across the picker** until this list is
triaged — several would email people who are not current students.

## Assigning

Use the `assign-lsatu-work` skill:

```bash
npx vite-node scripts/assign.ts -- --student "Celia" --activity "Read, Recall, Colour"
```

The script resolves a name or email to exactly one account and **refuses on
ambiguity** rather than guessing, because a misdirected assignment is silent —
she simply never sees it.

Full path and what it fires: [[ASSIGN-AN-ACTIVITY]].

## Open, not yet checked

Whether each account carries the feature flag that makes Activities visible.
`admin-manage-users` returns the flags; nothing here reads them yet. If an
assignment lands but she never sees it, check this first.

Related: [[ASSIGN-AN-ACTIVITY]] · [[tasks]] · [[hot]]
