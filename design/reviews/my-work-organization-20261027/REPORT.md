# Make My Work easier to scan

2026-10-27. Local refinement on `codex/my-work-organization-20261027` in `C:/Users/Joshu/dev/ai-os-projects/lsatu-my-work-20261026`. This revision has not been pushed or published.

## What the live review found

Inspected signed-in `/my-work/notes`, `/my-work/to-do` and `/my-work/completed`, compared with source and the user-supplied marked Notes screenshot. This is the My Work destination, not the separate Classroom Home dashboard.

| Finding | Why it matters | Local correction |
|---|---|---|
| Notes tab, Notes & recaps and Browse your notes repeat orientation | Three labels consume space before the actual notes | One Teaching notes heading inside the shared paper surface, with Personal notes nearby |
| Content type and reading state are mixed | A recap and an unread note answer different retrieval questions | Exact source-type selector independent from All/Unread and search |
| Global All/Unread counts ignore selected type | Button counts do not predict the next result set | Counts now reflect current type and search, ignoring only unread state |
| Short archives span months without month labels | Chronology is harder to skim | Month headings whenever visible results cross months |
| Excerpts repeat the title; links announce entire note bodies | Visual repetition and excessive screen-reader output | Prefer authored descriptions, remove one exact leading title from the displayed excerpt, concise link names; full body remains searchable |
| Assignments are one flat list | In-progress work and work to start have equal structure | In progress, To start and Progress to confirm groups based on stored status/evidence |
| Repeated completed titles have no date context | Separate assignment instances appear indistinguishable | Show assignment type and actual assigned date, retain all identities |
| Weekly plan and assignment feed can contain the same work | They can look like separate competing work queues | Name the lower feed All assigned work; preserve the existing weekly plan and its independent error handling |

## Categories come from evidence

Notes use actual `ClassroomItem.type`: note, session recap, announcement and whiteboard recap. Available type controls reflect the collection, including a valid selected category with zero results so recovery remains possible. No title-based topic guessing or content rewriting.

Assignments use the existing feed's kind, status, subject evidence, createdAt and dueAt. Subject search uses confirmed LR/RC/mixed/unknown evidence. No fabricated completion timestamp: dates say Assigned, never Recently completed. Progress warnings and partial-feed warnings remain visible. Search and subject filters are URL-backed; guided drills preserve that query in their existing returnTo contract. Other assignment destinations retain their established return behavior.

## Material and interaction choices

Preserve warm paper, charcoal, restrained contact/ambient shadows and continuous rows. A section plane carries the controls and records; status headings and rules group rows without turning each task into another card. Preserve readable excerpts, due dates, real statuses, keyboard focus, reduced motion and all current access gates.

Reused existing app components and dependencies. No new library was necessary. The improvement is a clearer model of the student's work, not more widgets.

## Evidence and limits

- Read-only live review used the signed-in teacher account. No production notes or assignments were changed.
- Actual page/archive components exercised locally with synthetic account/data adapters. The sidebar is a representative fixture, not the full production ClassroomLayout. The weekly plan is omitted from this fixture; existing refetch/access tests cover its boundary.
- Notes, Assigned work and Completed measured at 320, 390, 684, 768, 1024, 1281 and 1441 CSS pixels: no page overflow. See [matrix](viewport-matrix.json), [surface checks](surface-checks.json), [Notes desktop](notes-1440.png), [Notes phone](notes-390.png), [Assigned phone](assigned-work-390.png), [Completed desktop](completed-1440.png).
- Visually read Notes desktop/phone and Assigned desktop/phone. Browser exercised type plus unread filtering, note open, Back preserving filters, empty result recovery and focus fallback after reading the last matching unread note. Source tests cover subject plus search and guided return state.
- Assignment surfaces measured paper/ink/meta in both themes; metadata and placeholders resolve to the same readable supporting ink. Reduced-motion assignment row transition measured 0s. No new animation or dependency.
- Broad regression run: 84 tests across 10 files passed before the final count regression was added; final Notes-focused run: 37 tests across four files passed. Typecheck passed; final production build result is recorded by the host separately.
- Independent source review found no material high-confidence findings. It was not a Claude review and did not independently exercise the browser. No claim of real student RLS/persistence or full-host acceptance.

## What remains a separate product decision

Topic tags and per-session associations need authored metadata, not guesses from titles. Completion dates need an explicit source field in the shared feed. Detail pages currently leave the top-level My Work tabs but retain the existing Back link and active sidebar section; that is a separate navigation boundary, not a broken selected tab. No records were merged or deleted.

Final verification: production build and postbuild passed (1m24s); corrected final typecheck exited0 without diagnostics; final archive15tests passed. The first final typecheck caught unsupported Testing Library exact options in the new test; those were fixed and the gate rerun. Supporting ink/placeholder contrast from actual sampled colors: light5.88:1, dark7.91:1. Notes and Assigned work at390px with32px root text (200%) had no page overflow; see text-zoom.json. Existing large-chunk build warning remains. Changes stay local and uncommitted on codex/my-work-organization-20261027.


## Release authorized 2026-10-27
User authorized push to main and strengthened read/unread behavior. Organization plus recipient-scoped note/message read fixes merged through PR #242 to main e4035d9c8ec97a3aaec01b0b3464533872328bc8 (implementation37f22d1e plus authenticated-reader guarde4035d9c). Local129tests/17filespassed, badgefollow-up15passed, finalmessage8passed, finaltypecheck/buildpassed. GitHub RC workflow failed at npm ci because existing @lovable.dev/email-js optional peer @react-email/render>=1 conflicts with @react-email/components0.0.22/render0.0.17; package files unchanged. No dependency/schema/Edge Function changes. Lovable synced exactmainSHA; deploymentc0edc71b-d21f-4d8b-be43-5edf4f22c48a pending. Liveverificationfollows. The earlier local/uncommitted status above is historical.


Published exact main e4035d9c on2026-10-27 through Lovable deploymentc0edc71b-d21f-4d8b-be43-5edf4f22c48a. UI confirmed websiteupdated; livebundlechanged index-CTmshJ2_.js toindex-LMt1KUTz.js andcontains organization,typefilter,authenticatedreaderguardmarkers. Signed-in operator opened unreadconversation; messagerailcount6became4 afterloadedforegroundreader, remained4afterfullreload, andreadthreadwasabsentfromUnreadfilter. No messages sent. This provesoperatorflow, not manualverificationofeveryaccount. Initialread-onlyIvorythreadopenleftcount6unchanged, asitwasalreadyread. Actualstudent/accountisolationcoveredbytests.


### Final live acceptance

PR #242 is merged. Production is on main commit e4035d9c8ec97a3aaec01b0b3464533872328bc8 and serves index-LMt1KUTz.js. Opening an unread conversation reduced the operator's message count from 6 to 4. A full reload retained 4, and the opened conversation was absent from the Unread filter. Opening an already-read note and returning to the archive retained 4 notes, zero unread notes and 4 unread messages. No console warnings/errors were captured in these flows. No message was sent. The published screenshot is live-published.png.

Local regression tests, final typecheck and final production build passed. GitHub's RC workflow did not reach tests because npm ci failed on the unchanged email peer-dependency conflict. Do not report that CI check as passing. Student/teacher account isolation is covered by tests; live acceptance used the signed-in operator only. Legacy generic alerts require individual clicks, and cross-device classroom realtime delivery remains unverified.
