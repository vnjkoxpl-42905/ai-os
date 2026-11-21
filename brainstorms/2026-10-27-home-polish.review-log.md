# Home polish review log

2026-10-27. mode=review; host=codex; builder=codex; reviewer=Claude; final inspector=fresh Claude session. Models/effort use CLI defaults, identity reported from actual runner output. Plan: C:/Users/Joshu/dev/ai-os/brainstorms/2026-10-27-home-polish.plan.md. Repo: C:/Users/Joshu/dev/ai-os-projects/lsatu-home-polish-20261027. Maximum 2 plan-review rounds, 2 fix rounds, 2 inspections. User approved implementation and explicitly added claude-review. No commit/push/publish. Original role-home dirty checkout preserved. Existing tests and visual claims are historical until rerun.

## claudex-6ax70skm
Result: C:\Users\Joshu\dev\ai-os\research\2026-10-27-home-polish\review\claudex-6ax70skm\result.json
```json
{
  "verdict": "REVISE",
  "summary": "The plan is mostly sound and its guardrails are good. A few gaps would let the build ship wrong behavior. The \"View all assigned work\" link is not gated by access. The teacher preview enrichment has no payload or ordering constraints. The plan treats Home's \"loaded\" state loosely. Its reconciliation baseline is not what the checkout actually contains. I only did a partial source review, and I could not inspect the old role-home worktree.",
  "findings": [
    {
      "id": "F1",
      "severity": "medium",
      "path": "src/lib/destinationAccess.ts:39-43",
      "evidence": "The plan says the \"View all assigned work\" route is the canonical one \"verified in source\". The source shows /my-work/to-do and /my-work/completed are tab entries gated by has_classroom_access and readingCenterEligible, and tabAccess() can return 'locked'. Defaults also differ: Tier 1 and admin land on /my-work/notes, while Tier 3 lands on /my-work/to-do. A hard-coded link can send a student whose assignments came from a different grant path to a locked tab.",
      "fix": "Derive the destination from DESTINATIONS['my-work'].tabs plus tabAccess() for the current permissions. Render the link only when access is 'open'. Add a test covering an open case and a locked case, including readingCenterChecking."
    },
    {
      "id": "F2",
      "severity": "medium",
      "path": "src/hooks/useInbox.ts:184-204",
      "evidence": "The plan enriches the read-only unread scan with the newest incoming body, sender and time. That scan currently selects only id, conversation_id and created_at, and pages 500 at a time from the oldest read timestamp across all conversations. Adding body to every unread message since the oldest read timestamp can pull large payloads for an old or never-read thread. The scan is ordered ascending, so \"newest\" must be computed explicitly, and ties on created_at are broken by id. Math.min over an empty lastReadMap gives Infinity, and new Date(Infinity).toISOString() throws a RangeError. The plan does not say whether that case is reachable here.",
      "fix": "Keep the scan lean (ids and timestamps). Fetch the preview body only for the newest unread incoming message per conversation, or use a bounded per-conversation query. Select the newest by (created_at, id). Add tests for ties, multiple unread messages per conversation, a viewer-authored last message, and the empty read map."
    },
    {
      "id": "F3",
      "severity": "medium",
      "path": "src/hooks/useInbox.ts:244-248",
      "evidence": "The plan exposes \"loaded\" from the current successful conversation-owner state. The hook sets setError(null), setConversationOwner(viewerId) and setConversations together only on a full success. After a failed refetch, the previous owner's data stays in state with error set, and the old unread/preview data can still render. The plan's \"stale\" state is not defined against this. A user switch could also briefly show a previous owner's data if loaded is not tied to the current user id.",
      "fix": "Define loaded as conversationOwner === currentUser.id && !loading. Keep the error and stale state explicit, and label stale previews as stale. Add a regression test for a failed refetch after a success, and for a user switch."
    },
    {
      "id": "F4",
      "severity": "low",
      "path": "src/components/classroom/home/ClassroomHomeView.tsx:135",
      "evidence": "The checkout already contains src/components/classroom/home/ with an existing entrance and matchMedia animation (home.css:1768 mentions a shared entrance). The plan says to \"remove the automatic page entrance\" and port from the old worktree, but does not list which current-main Home files are replaced and which are kept. Overwriting from the old worktree could drop main-only fixes. The existing useClassroomMotion hooks and test-days-animated sessionStorage logic would be left orphaned or duplicated.",
      "fix": "Add a per-file reconcile table (current main vs old worktree) before copying. Reuse the existing useClassroomMotion hooks rather than ad-hoc gsap. Remove or keep the sessionStorage key deliberately, and test the result."
    },
    {
      "id": "F5",
      "severity": "low",
      "path": "plan: Acceptance and proof",
      "evidence": "The plan lists tests to run but names no regression test for the student-side counts coupling or the featured-exclusion rule after refresh. These are stated requirements: no repeated exact key, and counts coupled to the rendered model.",
      "fix": "Add a focused test that the featured item is excluded from the remaining list by its stable key, and that the counts equal the rendered rows after a refetch changes the featured item."
    }
  ],
  "coverage": [
    "Read the plan.",
    "Listed the Home directory in the build checkout.",
    "Read src/lib/myWorkNotesNavigation.ts.",
    "Grepped for my-work and assigned-work routes, and read the destinationAccess.ts tab matches.",
    "Read useInbox.ts lines 170-260, covering the unread scan and the owner and error state.",
    "Grepped for gsap usage and Home motion code."
  ],
  "limitations": [
    "Did not open the old role-home worktree, so the plan's claims about its dirty changes are unverified.",
    "Did not read ClassroomHomeView, useClassroomHome or the permission hooks in full.",
    "Did not check the useUserPermissions additive fields against upstream.",
    "Did not read the design docs or the tasteskill scripts.",
    "Ran no tests, builds or visual checks."
  ]
}
```

## claudex-vil328h2
Result: C:\Users\Joshu\dev\ai-os\research\2026-10-27-home-polish\review\claudex-vil328h2\result.json
```json
{
  "verdict": "APPROVED",
  "summary": "The revised plan resolves the five round-1 findings, and I found no new material defects. F1 is covered: the assigned-work link now comes from the tab registry and tabAccess, with open, locked and checking tests. F2 is covered: the unread scan stays lean, previews are chosen by (created_at, id), and bodies are fetched in bounded batches. The empty-map case returns a successful empty snapshot. F3 is covered: I accept your correction that loaded means an actor-owned snapshot exists, independent of the loading flag. Stale = loaded + error, unavailable = !loaded + error, and previous-actor data is masked. F4 is covered by the per-file reconciliation and the retirement of the Home entrance. F5 is covered by the exact-key exclusion and count-coupling tests. The shared motion hook excludes data-motion-skip (useClassroomMotion.ts:11), so the Home exclusion mechanism exists. Two things to watch during implementation: the loaded-during-refetch semantics must also be applied to the Home teacher components so they never treat loaded as \"not loading\", and the My Work link must handle readingCenterChecking without flashing in and out.",
  "findings": [],
  "coverage": [
    "Compared the revised plan and your dispositions against the round-1 findings F1 to F5.",
    "Confirmed that data-motion-skip is an exclusion in src/hooks/useClassroomMotion.ts and is used by existing navs.",
    "Reused my round-1 reads of destinationAccess.ts tab gating and of useInbox.ts lines 170-260 (the unread scan and the owner/error state)."
  ],
  "limitations": [
    "Plan-level review only; no implementation exists to inspect.",
    "Did not open the old role-home worktree. The claim that git diff HEAD origin/main for src/components/classroom/home is empty is taken from your report.",
    "Did not read the full permission hooks or the 2026-10-22 role-home spec.",
    "Ran no tests, builds or visual checks."
  ]
}
```

Approval check passed. New baseline e4035d9c. Original checkout preserved. Home files ported only after approval.


## Implementation inspection claudex-ccr3pir7

```json
{
  "verdict": "REVISE",
  "summary": "I found two CSS defects in home.css and one low-severity item. I only partly reviewed the rest: I read the diff but did not trace every caller or run anything. The main problem is that five `@media (hover: hover) and (pointer: fine)` blocks in the working-tree home.css are malformed. Their hover rules never apply. The \"today\" cell styling is also gated behind the hover query.",
  "findings": [
    {
      "id": "F1",
      "severity": "high",
      "path": "src/components/classroom/home/home.css:392",
      "evidence": "I confirmed this with grep on the working-tree file. Five rules end like this: `width: 100%;` / `@media (hover: hover) and (pointer: fine) {` / `}`. The media block opens inside the base rule and is closed at once with an empty body. The base rule stays unclosed, so the `:hover` rule that follows nests inside it and the final `}` closes the outer rule. The same shape appears at lines 392, 507, 727, 799 and 1006. Affected selectors: row/thread-row/session-row/student-row, cta, action, message and search-clear. With CSS nesting, `.classroom-root .classroom-home-row:hover` nested without `&` becomes a descendant selector and never matches. Browsers without nesting support drop the whole base rule, which would also lose its layout. Either way the hover feedback the plan specifies does not work. The base rules may also be damaged, because later declarations such as `.classroom-home-cta` `transition` and `min-height` sit before the stray at-rule.",
      "fix": "Close each base rule before the at-rule, then wrap the hover rule: `width:100%; }` / `@media (hover:hover) and (pointer:fine){ .selector:hover{...} }`. Add a CSS parse check, such as a stylelint or postcss parse step or a built-CSS assertion, so unbalanced blocks fail the build."
    },
    {
      "id": "F2",
      "severity": "medium",
      "path": "src/components/classroom/home/home.css:862",
      "evidence": "The `@media (hover: hover) and (pointer: fine)` block wraps the base `.classroom-home-day-today` rule (dark background, light text), not only the `:hover` variant. On touch devices (hover:none) the 'today' cell therefore gets no highlight. Its children are still styled `color: inherit` and the `.classroom-home-day` base colours. The 'today' cell is meant to be the visual anchor of the week strip.",
      "fix": "Move `.classroom-root .classroom-home-day-today { ... }` out of the media query. Keep only `button.classroom-home-day-today:hover` (if it needs a distinct style) inside it."
    },
    {
      "id": "F3",
      "severity": "low",
      "path": "src/components/classroom/home/useHomeEntrance.ts",
      "evidence": "The plan says the old useHomeEntrance is replaced by scoped pointer and state feedback in useHomeFeedback. The file is still in the scope manifest. ClassroomHomeView now imports only useHomeFeedback, so useHomeEntrance may be dead code. I did not read the file or search for other callers, so this is unverified.",
      "fix": "Search for remaining importers of useHomeEntrance. If there are none, delete the file so no page-entrance code remains. Otherwise confirm that nothing mounts it on Home."
    }
  ],
  "coverage": [
    "I read the plan and the full tracked diff, including ClassroomHome.tsx, ClassroomHomeView.tsx, homeModel.ts, useClassroomHome.ts, useInbox.ts, useUserPermissions.ts and home.css.",
    "I grepped the working-tree home.css to confirm F1 and F2.",
    "I did not open the untracked files: teacher/*, HomeWeekStrip, useHomeFeedback, useHomeFreshness, the new tests and the docs/verification harness."
  ],
  "limitations": [
    "I did not review the untracked files named in coverage. Their absence is not an approval.",
    "I did not run any tests, build or browser checks.",
    "I did not trace callers outside the listed scope: ClassroomLayout, thread consumers, useUnreadCounters and the destinationAccess registry.",
    "I did not verify that the ClassroomHomeView tests match the new markup beyond reading the diff.",
    "The useInbox unread-preview logic looks plausible from the diff but is untested by me."
  ]
}
```


## Implementation inspection claudex-wa3x1j4h

```json
{
  "verdict": "REVISE",
  "summary": "I found no security or role-gating defects in the dispatcher, permissions additions, teacher hooks or preview harness. Two defects in the new Home/inbox behavior should be fixed first: one (F1) can make the Up next \"new\" badge undercount the full dataset, the other (F2) widens a failure path in the shared inbox hook. Three low-severity items are also listed. I could not run tests, typecheck, build or any browser, and I made no claim that they pass. I did not open the test files, the full `useClassroomHome.ts` or the full `home.css`.",
  "findings": [
    {
      "id": "F1",
      "severity": "medium",
      "path": "src/components/classroom/home/ClassroomHomeView.tsx",
      "evidence": "`remainingNew = upNext.filter(row => row.isNew).length` counts only the rows `useClassroomHome` passes in, which is `rows.slice(0, 5)` minus the featured row. `model.newCount` is computed over every row and is no longer used for the badge. With more than five rows, the \"N new\" badge in Up next undercounts the full dataset. The plan says \"only visible list is capped, totals remain full dataset\" and \"counts coupled to rendered models\". The existing refetch test passes only because its model has two rows and a hand-set `newCount`, so it never exercises the cap.",
      "fix": "Derive the badge from the full-dataset count. Use `model.newCount - (featuredRow?.isNew ? 1 : 0)`, clamped at 0. Or have the hook expose the uncapped new count explicitly. Add a test with more than 5 rows where some new rows fall outside the visible slice."
    },
    {
      "id": "F2",
      "severity": "medium",
      "path": "src/hooks/useInbox.ts",
      "evidence": "The new preview-body fetch (`.in('id', previewIds…)`) is treated as fatal. On error it calls `setError('Could not load your messages')` and returns, so `setConversations` and `setConversationOwner` never run. Every consumer of `useInbox` then keeps a stale list and unread count (rail badge, Inbox page, Home). The only data lost to a preview failure is a snippet. The teacher view already falls back to \"New message\" when `latest_unread_message` is null, and the attachment and name fetches in this same function are non-fatal. A transient failure or an RLS hiccup on this one extra query therefore blocks all inbox refreshes, including read-state reconciliation after acknowledgement.",
      "fix": "Make the preview failure non-fatal. Log a warning, leave `unreadPreviewMap` empty for the failed batch, and continue to `setConversations`, so unread state stays accurate and only snippets degrade. Add a test where the preview query errors while the unread scan succeeds, and assert the conversations are still set and flagged unread."
    },
    {
      "id": "F3",
      "severity": "low",
      "path": "src/hooks/useInbox.ts",
      "evidence": "`readTimes` filters out non-finite values, but `lastReadMap` itself keeps NaN for an unparseable `last_read_at`. `timestamp <= (lastReadMap.get(id) ?? 0)` is then false against NaN, because `??` does not catch NaN. Every message in that thread counts as unread. The empty-map case is handled correctly. This is only a malformed-data edge.",
      "fix": "Normalize at map construction: `const t = p.last_read_at ? new Date(p.last_read_at).getTime() : 0; Number.isFinite(t) ? t : 0`. Then the `readTimes` filter is unnecessary."
    },
    {
      "id": "F4",
      "severity": "low",
      "path": "src/components/classroom/home/useHomeFreshness.ts",
      "evidence": "The `focusManager` and `onlineManager` subscriptions invalidate eight key prefixes on every focus event with no throttle. Each tab switch triggers a refetch burst. `setRefreshing(true)` also flips the visible Refresh button to a disabled \"Refreshing\" state. Focus events can fire in rapid pairs (window and visibility), and overlapping calls set `refreshing` false when the first finishes while the second is still running.",
      "fix": "Skip the focus-triggered refresh if one is already in flight (use a ref guard), or if the last refresh was under a few seconds ago. Alternatively, use a counter for `refreshing` instead of a boolean."
    },
    {
      "id": "F5",
      "severity": "low",
      "path": "src/components/classroom/home/useHomeEntrance.ts",
      "evidence": "The plan retires the page entrance and says the old `useHomeEntrance` is replaced. The host disposition kept the file as a \"compatibility export\" of `useHomeFeedback`. I found no importer in the files I read. A dead module with the old name invites re-adding entrance behavior.",
      "fix": "Delete the file if nothing imports it, which a grep confirms. Otherwise state the remaining caller in the verification report."
    }
  ],
  "coverage": [
    "Fully read: teacher/useTeacherHome.ts, teacher/teacherHomeModel.ts, teacher/TeacherHomeView.tsx, useHomeFeedback.ts, useHomeFreshness.ts, HomeWeekStrip.tsx, docs/verification/role-home-preview.tsx, docs/verification/home-preview.vite.config.ts.",
    "Read in the supplied diff and in the checkout: ClassroomHome.tsx (role dispatcher, role-error and stale-notice states), ClassroomHomeView.tsx, homeModel.ts changes, useClassroomHome.ts changes, home.css, .gitignore.",
    "Read in the checkout: src/hooks/useInbox.ts lines 90-399 (load path, unread scan, newest-unread selection, preview fetch, acknowledgement, returned `loaded`). src/hooks/useUserPermissions.ts lines 75-285 (query, resolved/resolvedFor/isError/retry).",
    "Checked that /teacher/library/assignments, the /teacher/students routes and the teacher inbox splat route exist in the source. Did not mount any route.",
    "Role gating: neither role's hooks mount until `permissions.resolved`. The key `${role}:${resolvedFor}` remounts on an actor change. The teacher queries are enabled only when resolved and admin, and are keyed by actor id."
  ],
  "limitations": [
    "I could not run tests, typecheck, build, the preview, or a browser. There is no visual, contrast, overflow, console, or motion verification, and nothing is claimed as passing.",
    "I did not open any test files (ClassroomHome.role, TeacherHomeView, HomeWeekStrip, useHomeFreshness, assignedWorkPath, homeStyles, useInbox.summary, useUserPermissions.resolved, the Home view tests), so I did not check what they actually assert.",
    "I did not read the full useClassroomHome.ts, the full home.css cascade (the diff showed late override blocks), or useHomeEntrance.ts.",
    "I did not inspect the rest of the repo for other consumers of useInbox or useUserPermissions, ClassroomLayout, or the rail and sidebar unread-count paths. Out-of-scope files are unreviewed.",
    "I did not verify the actual Edge Function admin enforcement for `admin-manage-users`, the `student_sessions` RLS, or live RLS and backend behavior. No real signed-in acceptance was possible or claimed.",
    "Every tasteskill script and screenshot step in the plan was out of reach and unreviewed."
  ]
}
```

Dispositions after second inspection: F1 full-dataset new count minus exact featured row; test covers capped rows. F2 preview failure is nonfatal with fresh unread state and null snippet, cold and refresh tests. F3 invalid read timestamp normalized. F4 concurrent refreshes share one promise, tested. F5 unused compatibility export retained because user forbids deletion; no entrance behavior remains. Two fresh inspections exhausted; final fixes are host-tested, not independently approved.
