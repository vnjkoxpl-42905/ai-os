# Execute the RC repair in eight bounded tickets

Date: 2026-10-08. Status: implementation handoff prepared; no implementation performed by this planning pass. These local tickets are execution instructions, not published GitHub issues. The product authority remains `C:/Users/Joshu/dev/ai-os-projects/lsatu/docs/specs/2026-10-07-rc-drill-quality.md`. Update that specification when an accepted product decision changes; do not create another competing spec.

Execution update, 2026-10-09: Joshua subsequently authorized this chat to implement and release the remaining tickets. Tickets 03–07 are implemented on main in `ab5d33dd` with preview-origin follow-ups `a95d87de`/`4e45b860` and the setup-loading race fix `8ad748b0`. Ticket 08's current test, publication and signed-in acceptance evidence is recorded in [the app release ledger](../../../ai-os-projects/lsatu/docs/specs/2026-10-09-rc-release-evidence.md). That ledger distinguishes passed scenarios from remaining physical-device, screen-reader, live fault and scoring-authority checks. The planning workflow below is preserved as the original handoff, not a request to redo completed work.

## Use a stronger planner and a cheaper implementer

The ask-matt route is **to-spec → to-tickets → implement → code-review**. The current audit already supplies the problem, most interaction decisions and acceptance requirements. This packet performs the local planning and ticket-drafting work so the executor does not need this long chat. It does not publish issues or claim the formal to-spec/to-tickets approval steps have occurred.

Use one fresh chat per ticket with the cheaper coding model. Give it this README and one ticket, not the whole conversation. Let it inspect the current source and implement the defined slice. Have a stronger reviewer review the diff against that ticket before continuing. If the ticket exposes a new architectural or product decision, return that specific decision to the planner; do not let the cheaper executor redesign the whole flow. Choose the cheaper model available in your account; this plan makes no unverified pricing claim.

`ask-matt` routes the process; `to-spec` designs the behavior and test boundaries; `to-tickets` makes bounded tasks; `implement` executes one task. Sequential implement is the recommended process here because it keeps context and review small. An all-at-once implementation run is unnecessary for this handoff.

## Keep the work already completed

Working app: `C:/Users/Joshu/dev/ai-os-projects/lsatu`. Follow its AGENTS.md and scoped instructions. The first reading/builder repair and audit documentation were pushed previously; the latest audit commit was f59ddc48. Refresh HEAD and inspect diffs rather than assuming this remains current. At planning time `supabase/functions/mcp/index.ts` contains unrelated user work. Leave it intact and outside each ticket's commit.

Preserve the existing18px /1.6 reader default, responsive passage-only layout, saved text-size preferences, readable passage rows, Preview drill → Start this drill sequence, suppressed homework inside active setup, direct Question details, and actor-filtered personal history. Rework only the behavior each ticket owns.

## Decisions the executor can rely on

- A question lookup is a read-only task. Changing a selector retains its value and creates no session, answer, annotation or attempt. Opening a preview reveals no correct answer or authored summary.
- Starting a saved drill is deliberate and separate. Show its complete passage/question count before starting. The chosen official question can be the initial focus; make clear the whole passage is included.
- Use the existing shared finder as the single lookup surface. The landing page provides a compact Open a question entry and a separate Create RC drill entry. Both sidebar and landing lookup entries open the same finder.
- Group RC questions by passage, with title and official range. Auto-select a unique RC section. Clear dependent selections when bank/test changes. Keep selected addresses visible.
- Validate return destinations as internal routes and preserve the originating page. A read-only route must remain read-only on refresh and direct entry.
- Maintain official question identity separately from drill ordinal. Protected source answers remain immutable; personal tools have separately stated ownership and save status.
- Annotation ownership is actor+passage across sessions. Annotation hydration explicitly filters by actor and reloads on actor changes. Flag intent/recovery belongs to actor+session+question. Capture the owner before pending work is queued; teardown preserves unsaved intent without writing it under a new owner.
- The PT159S2Q2 key discrepancy is unresolved. The index ticket preserves keys verbatim. Authority investigation and any historical regrading are separate from this UI repair.

## Ticket order and dependencies

| Ticket | Blocks / dependencies | Outcome |
|---|---|---|
| [01](tickets/01-index-completeness.md) | None | Every bank question is discoverable. |
| [02](tickets/02-unified-lookup.md) |01 | One finder retains choices and groups passages. |
| [03](tickets/03-read-only-preview.md) |02 | Opening a question creates no scored drill; start is explicit. |
| [04](tickets/04-layout-preferences.md) |03 | Compact landing, readable tabs and usable preferences. |
| [05](tickets/05-source-review-semantics.md) |03 | Official identities and review restrictions are clear. |
| [06](tickets/06-annotation-ownership.md) |None | Loads and account changes cannot corrupt marks. |
| [07](tickets/07-save-acknowledgement.md) |06 | Annotation/flag failures are visible and recoverable. |
| [08](tickets/08-release-acceptance.md) |01–07 | Builder and lifecycle evidence supports release. |

Recommended sequential order:01,02,03,04,05,06,07,08. Independent edges allow later scheduling changes, not concurrent edits to shared files. Optional features such as prediction, discussion, video, priorities and similar questions are excluded.

## Test boundaries and review

Use existing rendered finder/builder/player tests, hook tests with controlled async responses, and generator input/output integrity. Avoid a broad RC rewrite or a new state management framework. Prefer a dedicated preview surface sharing read-only rendering over partially guarding the live player. Ticket03 must prove zero backend and device-storage writes, not merely check a preview label.

Each executor reads package.json for current commands, captures the pre-edit commit for review, and runs meaningful focused regressions, typecheck and relevant lint. Tickets02–03 belong on the same feature integration branch: commit and review02, then03, and land them together so an intermediate disabled lookup action does not deploy to students. The executor prompt must explicitly authorize this branch/release policy. Use the app's build and safe-push gates at release; do not deploy incomplete intermediate states. The implement skill asks for the full suite at the end; run it at the integration checkpoint and report any unrelated failures separately. UI changes need actual Codex-browser verification. Use390x844,700x900,1024x768,1366x768,1920x900, actual docked width,200% text/zoom and keyboard focus for the surfaces changed. Emulation does not certify physical phones or screen readers.

Return: ticket ID; behavior changed; intended files; test commands/results; screenshots; commit; remaining acceptance failures. A passed build is not production acceptance. Refresh the signed-in deployed app separately before claiming a fix is live.

## Authority lane stays with the stronger investigator

RC01 requires independent authoritative keys/provenance, especially for548 recovered records. Prepare an evidence table of exact official addresses, choices, competing keys and source provenance. Do not resolve the D/B discrepancy by trusting one UI or by majority vote. If authority cannot be obtained, record the blocker. Any content correction, frozen-manifest changes or historical regrading gets a separate concrete proposal and scope; preserve source answers/timing and correction history. The UI/index work can progress while this is investigated, but scoring correctness remains uncertified until adjudicated.

## Paste this into the cheaper model's fresh chat

```text
Work in C:/Users/Joshu/dev/ai-os-projects/lsatu.
Use a codex/rc-quality integration branch. Commit each reviewed ticket separately; do not deploy an incomplete intermediate state. Tickets02 and03 must land together after review. Push the completed release only through the repository's safe-push procedure.
Read its AGENTS.md and scoped instructions, then read:
C:/Users/Joshu/dev/ai-os/brainstorms/2026-10-08-rc-implementation/README.md
C:/Users/Joshu/dev/ai-os/brainstorms/2026-10-08-rc-implementation/tickets/01-index-completeness.md
Implement ticket01 only. Verify the current code before changing it and capture the pre-edit commit for review. Preserve unrelated work. Keep answer keys and historical attempts unchanged. Complete the ticket's meaningful tests and required repository gates. Report evidence and the diff for independent review. Do not proceed to ticket02 or mark production acceptance complete.
```

For later tickets replace the ticket file/number and include the preceding review's approved commit. Read the complete ticket before editing. A source mismatch, missing authority or failed dependency calls for a specific report to the planner.
