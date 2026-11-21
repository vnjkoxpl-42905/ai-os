---
type: operating-layer
subject: Hot last-session cache
updated: 2026-11-18
aliases: []
---

# Hot — last-session cache

Freshest working state; the first page `/pickup` reads. Rebuilt fresh in the 2026-07-16 vault rebuild (the old cache is archived).

## Most recent (2026-11-14): Claude and Codex workspace redesign in progress

- Start at [Start Here](../references/ai-workspace/Start-Here.md), [the task checkpoint](../brainstorms/2026-11-14-workspace-redesign-checkpoint.md), and [the implementation plan](../brainstorms/2026-11-14-claude-codex-workspace-redesign.md). Native chats remain separate.
- Both LSAT U clones contain unfinished work. `C:/Users/Joshu/dev/lsatu` is the navigation home; the separate `ai-os-projects/lsatu` root and worktrees are preserved. The unlisted sidebar project points to an invalid Git worktree requiring recovery.
- Missing Orca registrations removed after an exact backup; unrelated Herdr and scoped teaching hooks retained. Direct tests passed; native review and fresh sessions remain unverified.
- [Workspace health report](../system/generated/workspace-health.md) reports existing skill drift and stale or deferred sync receipts. The documented sync and replacement-backup tasks were absent from the live scheduler. Synthetic backup and restore passed; a current production backup is not proven.
- Claude CLI diagnostic reports expired OAuth. Sign in, then retry the real Claude-to-Codex-to-Claude pilot, restart and stale-checkpoint test. Rollout and the seven-day trial remain open.
- A sandboxed `gws` metadata request attempted credential-cache removals after keyring denial; both were denied and both files remain present. A Firecrawl credential appeared in initial chat metadata output and should be rotated.

Older session entries (2026-10-25 to 2026-10-30): [hot archive, October](hot-archive/2026-10.md).

## Active priorities

- The authoritative Now/Next list remains [[tasks]]. This session did not change task status.
- The Matt Pocock updater now runs automatically; customized skill copies remain protected until Joshua names one for an update.

## Now

- **Conditional practice centre and navigation:** the integration and subsequent direct chapter actions, lesson progress and filters above remain local and uncommitted on the earlier released `bebb4948` course baseline. Keep the original Chapter 2 draft and current checkout. Live student launch, deployed RLS/account acceptance, font-load proof and any release remain separate.


## Open threads

- **RC Training immersive exercise published (2026-10-20):** Joshua authorized [main a52b3ff5](https://github.com/vnjkoxpl-42905/lsatu-684d89db/commit/a52b3ff5570be1653d0fa7b82b44f6f496599d06); safe-push typecheck passed and Lovable matched the exact SHA before free deployment `afc5033a-fefd-4cc0-93fa-608799b6db81`. Public root changed to `index-CUSnvITg.js`; HTTP-200 imported `index-FkLOZP26.js` contains the approved instruction and new waveform/action markers. This supersedes the local-only release status below. Signed-in production saves and feedback remain unverified. [Evidence](../../ai-os-projects/lsatu-rc-focus-release/docs/verification/rc-immersive-verification.md). Task statuses unchanged.

- **RC Training immersive exercise, local ready (2026-10-20):** approved redesign in `lsatu-rc-focus-release` has stable reading/recall actions, actual-input waveform and truthful recording/save states. Final hardware-microphone browser checks, 320 through 1440 px plus landscape, 771 tests, typecheck and build/postbuild passed. [Evidence and limits](../../ai-os-projects/lsatu-rc-focus-release/docs/verification/rc-immersive-verification.md). Backend/feedback were local fixtures; no signed-in production persistence proof. Uncommitted and unpublished, separate from the older `549620f7` release. Vite-generated backend stub restored; no backend changes. Task statuses preserved.

- **RC Training focus redesign published (2026-10-19):** Joshua authorized release. [Main 549620f](https://github.com/vnjkoxpl-42905/lsatu-684d89db/commit/549620f788e4b3642065266fa2f0451be1b69983) passed safe-push typecheck and 766 RC tests; Lovable matched the exact SHA before free deployment `01af468f-55d0-4490-9335-526eba01b26f`. Public root changed to `index-D61EYAeA.js`; new imported `index-74Rzvc_S.js` returned HTTP 200 and contains the pause-description, Recall paragraph and pause-overlay markers. This supersedes the local-only publication status below. Signed-in production recording persistence remains unverified. Task statuses unchanged; full release proof in [[log]].


- **Spot practice final publication verified (2026-10-16):** merge 6c1ddd7050887d5e4ecca79971d893caae630af5 is published and parent-observed in fresh signed-in Q1, including resolved retry-hint suppression and reveal without earned-credit upgrade. All four public markers now pass after following runner static imports; shared hint chunk useStudentActivities-CQyQ6wDO.js resolves the scanner limitation. Original tab 1 is ready at Question 1 with 0 of 48 completed and an empty focused input. See the Spot checkpoint and final verification in [[log]]. Task statuses unchanged.


- **Loophole workout library completed (2026-10-15):** [84 workout details and 71 inline instruction footnotes](../corpus/loophole-online/workouts/README.md), with 29 working prep-map pages and 33 preserved source errors linked to related observed working variants. Eight instructional documents saved as nine exports. [Source summary and corrected immutable archive](sources/loophole-workouts-2026-10-14.md). RC/LR/shared routes and local expandable catalog are connected; task statuses unchanged.

- Loophole library is now unified: [main README](../corpus/loophole-online/README.md), [ROUTER](../corpus/loophole-online/ROUTER.md), RC/LR/shared hubs and full source catalog. 59 new lectures and older references routed, originals preserved. Ten Day One note sections remain unexamined; automatic captions remain unverified by listening. Four adoption-review ideas are new and unapproved. Task statuses unchanged.


- Loophole RC Day Three: [11-lecture source archive](../Loophole%20Lecture/Day%20Three/README.md), 81.4 minutes, ten exact written-notes blocks, original video/audio, captions and checkpoint screenshot saved 2026-10-14. Complete capture verified; word-level listening checks and curriculum adaptations remain open.

- Loophole RC Day One: [11-video archive](../Loophole%20Lecture/Day%20One/README.md) captured 2026-10-14 with native captions, original video/audio, frames and hashes. [Comparison](../Loophole%20Lecture/Day%20One/comparison.md) flags suspected ASR errors and a timing discrepancy. Word-level listening verification and Joshua adaptations remain open; task statuses unchanged.

- RC repair: published code and passed scenarios are in the [release evidence](../../ai-os-projects/lsatu/docs/specs/2026-10-09-rc-release-evidence.md). Physical-device/screen-reader and remaining live fault checks are open. The [answer-key investigation](../../ai-os-projects/lsatu/docs/audits/2026-10-14-rc-answer-key-repair.md) completed with 56 verified corrections released; immutable source captures and historical records were preserved.

- Matt Pocock guide: if a rendered browser preview is needed, open `references/matt-pocock-skills-field-guide.html` locally; the Codex browser denied its `file:` URL, so its live interactions were not checked in-browser.
- Conditional centre: preserve the current local integration and its evidence before release work. Actual student question-bank launch, deployed RLS/account history, physical-device/screen-reader and slow-network acceptance remain open. The earlier course release is recorded in [[log]]; it does not publish these additional centre changes. Final fixes are host-tested, not independently re-inspected.

- Yahunatan: await approval of the V7 recap before posting the exact reviewed package. Current preview and primary record are linked above.
- RRC films: seeking is dead on production because the host ignores Range; hosting move is a P0 decision in [[tasks]] Next.
- Testing Centre: copy decisions, P3 design notes, practice-test freshness filter, scoped-world question, pre-`776f69b` run repair. All in [[tasks]] Next.
- Booking is not production-safe on cancellation or recent Google Calendar changes until the P1 batch is fixed and live-verified.
- Archived knowledge (product specs, entities, concepts) re-enters organically via `raw/` ingests when actually needed — do not bulk re-import.

<!-- brain-automation-alerts:start -->
<!-- brain-automation-alerts:end -->

### Latest study-tools release checkpoint (2026-10-01)

On Joshua's explicit publication instruction, study-tools commit 72df696 reached GitHub main, Lovable imported the exact SHA, and free deployment d46bba89-061f-4264-8b59-f4814ca1ed39 reached lsatprep.study. Fresh HTTP shell and new LR/RC assets verified on the custom domain. Production build SHA is unknown; new entry index-Dh0ahrE2.js and build time 2026-10-01T09:42:34.167Z prove refreshed delivery together with feature-code checks. Earlier unpublished-study status is superseded. Narrow-pane authenticated browser interaction remains blocked/unverified. AI remains disabled; #179 and broader audit remain open.




