# RC Practice and Drilling: work done, plan, and self-review (for Codex)

Prepared 2026-10-17 by Claude (Sonnet 5.5). Audience: Codex, to review the plan and the execution so far and say what must change.

Scope is LSAT U Reading Comprehension Practice and Drilling only. Out of scope and untouched: the RC Bootcamp (`/bootcamp/rc-engaging-with-the-passage`) and the RC Recall / Reading Center workstream (`/reading-center/rc-recall`).

Read first, in this order:
1. `MASTER-FINDINGS-AND-PLAN.md` (21 findings, T01 to T10, section 5 = my independent review and corrected specs, section 5.5 = Joshua's decision log)
2. `PLAN.md`
3. This file

Repo: `C:\Users\Joshu\dev\ai-os-projects\lsatu-rc-create`, GitHub `vnjkoxpl-42905/lsatu-684d89db`. All work went through branch plus PR, then merge to `main`, then publish with the free Lovable `deploy_project` (standing rule from Joshua, 2026-10-17).

---

## 1. What shipped, in order

| PR | Packet | Merge commit | Live? | What and why |
|---|---|---|---|---|
| #213 | T01 history and analytics integrity | `a0db5421` | yes | `getQuestionHistory` now ignores excluded sessions, pages past 1,000 rows (`created_at`, `id` order), never counts a skipped question as correct, scores "last try" and rolling accuracy from first takes only. New passage states: not_attempted, partial, skipped_only, completed. Why: findings A1, A2, A3, RC-02. Joshua chose option A: blind-review re-answers never change "Incorrect on last try"; they set `reviewCorrected`. |
| #214 | T02 launch, section preflight, wording | `5ce6e486` | yes | Start vs recovery copy (RC-07), "Question 17 (1 of 2)" labels (RC-10), "Reset filters" replaces "Cancel" on Create (A8), RC section Status (Fresh) filter on the section launcher, protected launch only when the manual-section flag, coverage and pace all allow it, otherwise the old `/rc` fallback (RC-08, A4). |
| #216 | T03 search, Finder, picker | `9258d3c5` | yes | `/rc/search` opens the read-only preview with the question id, never a live drill (RC-01). Search defaults to PT 101 to 148, held-back 149 to 159 are badged and counted with an Include control, found by exact address (RC-03). Soft hyphens ignored at match time in search and in-passage Find (A7). Finder shows "Couldn't load tests" with Retry instead of "Loading..." (A5, partial). Manual picker draws 40 at a time (RC-12). Search count separated from pool count (RC-06). |
| #217 | T04 part 1 history cards and Discard | `3b5f1d31` | yes | RC cards read `PT 139 · S3 · P1 · Title`, completed cards show a first-answer score, in-progress drills get Discard (marks `abandoned`, never deletes) (A6). |
| #218 | T05 part 1 standalone RC reader | `21bfefd0` | yes (code present in served chunk, not exercised on a real sitting) | New shared `RcTimedReader` extracted from the full-test child runner; standalone timed RC sections use it with text size, marker, find, passage-only. Marks stay on the device (localStorage) because the sitting has no field for them (RC-09, A4). |
| #215 | docs | not merged | no | Adds the publish-after-merge rule to the LSAT U repo's CLAUDE.md, AGENTS.md, GEMINI.md. Open on purpose. The repo's GEMINI.md still says "git push origin main", which conflicts with branch-and-PR; Joshua has not approved changing that line. |

Also changed outside the app repo (uncommitted in the ai-os vault): `CLAUDE.md`, `AGENTS.md`, `GEMINI.md` (publish rule), `decisions/log.md`, `wiki/log.md`, and a memory note.

## 2. Independent reviews I ran on Argon's work

- T01 first pass: REQUEST CHANGES. Found that recent accuracy used the first-ever answer while "last try" used the latest (disagreed across drills; a mastered question stayed wrong forever), a skipped retake erased an earlier miss, abandoned-only passages were labelled "Skipped". Argon fixed all in `15c67a43`; approved.
- T02: REQUEST CHANGES. Clock copy ("clock begins only after Start section") was shown on paths where the clock starts straight away (LR and the live-drill fallback); a failed sitting lookup silently reported every section Fresh; duplicated "Question N · Question M". I fixed these in `fc8107a3` and approved.
- T03: Argon stopped mid-work (quota). I found it in the working tree (2 type errors, 3 failing tests), kept it, finished it.

## 3. What is NOT done (honest list, most important first)

1. **RC-04 spoiler on `RcResults` is still open and it is a P1.** The "EVERY QUESTION" table shows the student's pick and the credited answer right above "Review all", which spoils blind review. This is T06 and I deferred it behind T04/T05. I now think that order was wrong; see section 5.
2. **A8 link from the RC builder to question-level filters is missing.** T03 was supposed to expose Question Family/Type/Feature filtering (or a link to `/rc/search`) from the builder. I replaced Cancel with Reset filters but did not add the link.
3. **RC-03 exposure tracking is missing.** Preview shows the full passage without recording exposure; "Fresh" still means "no attempt rows". The plan's Exposure policy (metadata-first preview, explicit reveal, separate exposure events) is unimplemented.
4. **Saved RC sets and selection recipes (RC-05).** Not built. The Saved sets tab on RC still shows the LR page. Needs a storage decision from Joshua: (A) new table, or (B) reuse `user_saved_sets` with a type column and make the LR page ignore RC rows. A bare reuse would leak RC rows into the LR list.
5. **T05 part 2 not done:** comparative `[Both | Passage A | Passage B]` switcher, consolidated Display menu (Paragraph focus and the six colour schemes hidden behind "Aa"), responsive split breakpoint, `0/0` counter when Find has no matches.
6. **T06 other items:** `drillMisses()` double-click guard and idempotent create, `toggleExcluded` rollback, left-pane Passage Summary during review, acknowledged review-reanswer saves, `/inbox` context link, persisted reveal state.
7. **T07 not done.** T01 supplies the data (`firstTakeCorrect`, `reviewCorrected`), but the UI does not yet show the target difficulty level or the "Fixed in review" label.
8. **T08 (training overlays), T09 (explanation coverage), T10 (acceptance and release) not started.**
9. **`****` markdown cleanup in `RC-PT125`** was deliberately skipped: saved highlights are character offsets into passage text, so changing the text could shift students' existing highlights. Needs an offset audit first.

## 4. Known weaknesses in what I did (fix or re-check)

- **Verification is thin for T03 to T05.** Unit and component tests pass (typecheck clean, 548 tests across the RC, timed, SectionSelector and AcademyMainhub suites at last run), and I checked a few things live (default PT range, held-back note, Preview going to `/rc/preview`, history card names, Discard button present). I did **not** run: the standalone RC section in a browser, the Finder failure/retry, the Show more picker, soft-hyphen Find, or Discard. No accessibility pass (keyboard, screen reader, 200% zoom) and no phone/tablet check.
- **No CI on the PRs.** `statusCheckRollup` is empty on every PR. I merged and published on my own local test runs. Please confirm whether CI exists and should gate merges.
- **Standalone runner test mocks the reader.** The runner test replaces `RcTimedReader` with a stub; the real reader is tested separately but there is no integration test of real reader plus real controller plus a real RC sitting.
- **Standalone marks are device-only.** They vanish on another device and are not available in post-section review. Acceptable only because the sitting schema has no field and extending it needs a Lovable edge-function deploy (credits, Joshua's confirmation). Decide whether that limit is acceptable.
- **The standalone toolbar is a second bespoke bar.** It copies the child runner's minimal bar instead of `OfficialDrillToolbar`/`RcPlayer`'s toolbar, so the reader is shared but the controls are not. The plan's Display consolidation is meant to fix that.
- **Section freshness has a hack.** `buildRcSectionFreshness` forces `unseen = total - 1` when a passage was touched through a timed sitting but unseen still equals total. Check this is right.
- **Unverified assumption:** whether opening a timed section's preflight (before pressing Start section) creates an `rc_drill_sessions` row. If it does, merely opening the preflight would remove that section from Fresh. The sitting RPC code is not in the repo migrations (Lovable-managed), so I could not check.
- **Live oddity:** one completed four-passage drill shows `0/27 correct · 0%` on the new card. Probably all skipped or wrong answers, but unconfirmed. The score counts skipped rows as not correct.
- **Minor T01 leftovers:** a skipped or abandoned retake still adds to `attempts` and moves `lastSeenAt`, so a skipped retake of an answered question can rank as "most recent" with its old score in the 40-question window.
- **Open decisions defaulted, not confirmed:** MASTER section 5.4 items 2 to 4 (partial answers remove a passage from Fresh; held-back PTs shown with badge and default-off toggle; no change to stored passage text). I used my recommended answers.
- **Deploy risk:** `deploy_project` ships every unpublished commit on `main`, not only mine. I checked `get_project latest_commit_sha` against the merged HEAD before each deploy.

## 5. Recommended next order (my view, challenge it)

1. **T06 now** (RC-04 spoiler, `drillMisses` guard, review-save acknowledgement). It is a P1 and affects every student who finishes a drill.
2. **T03 leftovers:** the A8 builder link and the preview exposure policy.
3. **T05 part 2** (comparative switcher, Display menu, `0/0`, breakpoint).
4. **T04 part 2** (saved sets and recipes) once Joshua picks A or B.
5. **T07**, then **T10** (full acceptance: real sitting, accessibility, mobile, flag-off path, sealed mode, CI), then T08 and T09.

## 6. What I want Codex to answer

1. Is the T01 first-take semantics right, and does the abandoned/in_progress/completed rule hold up against `src/lib/firstAnswerProgress.ts`?
2. Does the T02 protected-launch condition (flag, coverage, pace) cover every entry, including assignment and practice-test legs? Is the clock copy now true on every path?
3. T03: is soft-hyphen handling at match time correct for highlight offsets (offsets map back to original text)? Is "Show more" acceptable as the windowing, or does the plan require true virtualization?
4. T05: is device-only marks acceptable? Is extracting `RcTimedReader` and leaving the toolbar bespoke the right split? Any sealed-mode leak (answers, explanations, aids)?
5. Is the order in section 5 right, and is anything from the 21 findings missing from the packets?
6. Did I merge anything too early, given there is no CI?
7. Does the Discard rule (mark `abandoned`, keep rows) respect "student work must be preserved" end to end, including analytics, history, and review?

## 7. How to verify quickly

```bash
cd C:\Users\Joshu\dev\ai-os-projects\lsatu-rc-create
git fetch origin && git log origin/main --oneline -8
npm run typecheck
npx vitest run src/features/rc src/components/timed src/components/testing src/lib/timedSection src/lib/standaloneDrillHistory.test.ts src/pages/AcademyMainhub src/components/drill/SectionSelector.test.tsx src/components/questionfinder
```

Live site: lsatprep.study serves bundle `index-B9OE8OxJ.js` as of 2026-10-17. Do not start a section clock to test the standalone reader; open Practice Exams, Take a section, Reading Comprehension only when ready to sit it.
