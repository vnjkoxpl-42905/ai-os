# Reading Center: RC Recall implementation plan

## Goal

Add a new **RC Recall** activity to the LSAT U Reading Center. Students choose one of two modes, practise an entire four-passage LSAT RC section, see method-matched worked examples, and keep each attempt and recording in their own history. Add the full instructions and prepare an explainer-video deliverable without requiring a paid external subscription.

## Accepted terms and method mapping

- Side-rail activity: **RC Recall**.
- Within the activity: **RC Recall** is the Cappuccino-style mode (recall each paragraph, then look back and confirm); **Cumulative Recall** is the Decaf-style mode (recall each paragraph and then cumulatively recall all paragraphs read so far without looking back). The source workout names remain provenance only.
- Use the existing LSAT RC section bank (`rcBank.ts` + `rcSections.ts`), not the separate article library. Keep the four passages in published order.
- Build a recall-specific section index from groups that have exactly four passages at Positions 1-4, with non-empty segmentable text. Do not exclude a section because it has no drillable questions. After loading, verify that all four passage IDs match the requested section in order; fail visibly rather than silently shortening the section.
- Preserve each source workout's full procedure, timing guidance, conditions and optional recap language. Do not grade subjective recall quality or claim a score. Save objective attempt facts only: selected mode/section, RC Recall confirmation scope, per-recap voice choice, elapsed time, completion, per-recap recording state, date.
- Exact phase order uses the source's wording: **read, translate and quip** each paragraph. **RC Recall** hides the paragraph for a silent full-translation recall, then shows it for a brief, silent confirmation (paragraph 1 only for the first confirmation, all text read so far for each later confirmation), without rereading from scratch. At passage end, offer the source's optional full-passage recall with text hidden; this recap can be spoken or silent. **Cumulative Recall** hides each paragraph for a full-translation recall; from paragraph 2 onward, hides it for a second cumulative recap of all paragraphs read so far, including Passage A while working on Passage B. It has no confirmation/look-back phase. Repeat for every paragraph and every passage. Test the first, second and fifth paragraph sequences.
- Both modes offer spoken or silent full-passage recaps where the source calls for them. RC Recall paragraph recaps and confirmations remain silent; its optional passage-end recap may be spoken or silent. Cumulative Recall recaps may be spoken or silent. Save each choice and record audio only for spoken recaps. The source recommends spoken recaps while learning, then silent recaps when ready. Per-passage time guidance: RC Recall 6 minutes; Cumulative Recall 12 minutes spoken and 8 minutes silent. Show source section minimums as guidance only: 24+ minutes for RC Recall and 32+ minutes for Cumulative Recall.
- Keep recording and attempt history append-only. A student can run the same section repeatedly without overwriting prior attempts. Give RC Recall its own IndexedDB backup namespace and recovery routine; never send its backups through LR recovery or grading. Insert a UUID attempt before any recording; use a unique object path under that attempt UUID and no-overwrite uploads. Voice is chosen per recap. Record any spoken recap in either mode; silent-only attempts complete with `not_recorded`. Record one audio file per spoken recap, starting only for that recap, so silent reading and recall are not recorded. Save each recap state independently (`not_recorded`, `pending`, `saved`, `failed`) so one failed upload cannot obscure other recaps or falsely report the whole attempt saved. A saved attempt is tied to the authenticated student and Reading Center access entitlement. Do not claim an upload succeeded until the object and row are verified. Instructors may read RC Recall attempt metadata but cannot read or play student recordings.
- For comparative passages, segment the italic source note and `Passage A` / `Passage B` headings as attached labels, not recall units. RC Recall confirmation scope is selected before start and saved with the attempt: the written-source default is all text read so far; students may instead confirm only the current sub-passage. Cumulative Recall always cumulatively recalls Passage A and Passage B together once work on Passage B begins. Do not make headings separate paragraph steps. Add standard and comparative fixtures for both RC Recall scope options.
- The source footnote telling students to open the section in LawHub is adapted out: students select the same full section from this in-app section picker.
- Keep the seven Decaf walkthroughs with **Cumulative Recall** and the three Cappuccino walkthroughs with **RC Recall**. Before Cappuccino playback, show the correction from “A Note on the Cappuccino RC Translation Demo”: confirmations are normally silent; the spoken demo approximates the internal process; students may confirm only the current sub-passage or include Passage A while working on Passage B. The note clip itself need not be another worked example. Leave original local source files untouched.
- New explainer title: **How and Why to Do RC Recall**. Its chapter cards map the source lesson's names to the app names: “The source calls Cumulative Recall ‘Decaf’” and “The source calls RC Recall ‘Cappuccino’.” The original footage may use those names, but all captions, chapter cards and surrounding app copy must clearly map them. Exclude or trim the Cappuccino 35-minute variant because this activity does not offer it; do not present it as a supported option. Spot-check the audio and captions at each edit boundary. Only show a Watch Instructions button after the complete edited video and aligned captions are verified. Keep source video derivatives local in this branch; there is no authorization to publish or upload them.
- Preserve the current Reading Center shell, dashboard, LR Recall and Speed Reading behavior. Add RC Recall progress to the existing progress surfaces only if the existing data contracts can represent it without false analytics.

## Acceptance criteria

1. RC Recall appears in Reading Center navigation for users admitted to the Reading Center and opens a clear activity page.
2. Students can choose RC Recall or Cumulative Recall, choose a complete eligible section from the existing RC bank, and start the passages in order.
3. Each mode implements the exact paragraph-level sequence above, full passage/section completion, mode-specific confirmation/recall behavior, optional recap where the source specifies it, count-up timing, and the source's timing guidance. Text is available during ordinary read/review and hidden during recall where the selected mode requires it.
4. The entry page gives students the complete instructions and method-matched examples. Existing source-video originals are unchanged; playback remains accessible, source captions are identified accurately, and media sizes stay within the defined budget.
5. Every saved attempt is tied to the authenticated student and current Reading Center access, preserves the chosen mode, section, confirmation scope, each recap's voice, completion/time and recording state, and never replaces an earlier attempt. Spoken RC Recall passage-end recaps and silent-only attempts both work. RLS covers reads/inserts/recording uploads; only the student's own attempt can be finalized.
6. The interface is responsive and keyboard-accessible, respects reduced motion, and follows the existing Reading Center/LR Recall visual system without duplicating LR-specific four-step instructions.
7. Add focused tests for mode sequencing, section composition/order, persistence isolation/append-only behavior, and critical failure states. Run relevant tests, `npm run typecheck`, `npm run build`, and visually inspect the actual local app at narrow, medium and wide widths.
8. The full original strategy videos for Decaf and Cappuccino exist locally as MP4s with the instructor on screen, original natural audio and VTT captions. Assemble them, with clear **Cumulative Recall** and **RC Recall** chapter cards mapping the names used in the source lesson to the app's modes, into a single new **How and Why to Do RC Recall** MP4. Keep the audio genuine; do not clone or synthesize the instructor's voice. Exclude or trim the unsupported Cappuccino 35-minute variant. Add combined WebVTT captions with offsets matched to the edits. Keep the original files and new derivatives outside Git and outside the app's public assets; the player defaults to hidden when `VITE_RC_RECALL_MEDIA_BASE` is absent. A local development media server may serve ignored files for preview. No public distribution, upload or deployment is authorized.
9. Do not commit, push, upload assets to a hosted bucket, or deploy without further authorization. Leave a reviewable local branch.

## Sources and code areas

- Authoritative source instructions: `C:/Users/Joshu/dev/ai-os/corpus/loophole-online/workouts/decaf-rc-translation-drill/README.md` and `.../cappuccino-rc-translation-drill/README.md`.
- Worked-example assets: `C:/Users/Joshu/dev/ai-os/Loophole Lecture/Day One/Decaf RC Translation Demo ...` (seven); `.../Day Six/Cappuccino RC Translation Demo ...` (three). Keep source roots immutable.
- Existing RC bank and section composition: `src/features/rc/lib/rcBank.ts`, `rcSections.ts`, `rcTypes.ts`.
- Existing Reading Center navigation/routes/dashboard/progress: `src/features/reading-center/`.
- LR Recall recorder/attempt patterns: `src/features/activity-centre/recall/SectionRunner.tsx`, `recordingBackup.ts`, `sectionCompletion.ts` and existing migrations.
- Existing local explainer project for workflow reference only: `C:/Users/Joshu/dev/ai-os-projects/lr-recall-instructions-video`.

## Known limits and risks

- The ten matched walkthrough videos total approximately 680 MB including separate M4A sidecars. Source media must remain intact. Source inspection shows the walkthroughs are instructor-only footage; passage text is spoken and appears in the accompanying captions, not on screen. A local 480p/30fps H.264/AAC test frame remains clear for the presenter, so use 480p/30fps, CRF 32, mono AAC 64 kbps derivatives and MP3 sidecars to target a total media size under 200 MB. Use each original WebVTT after verifying it matches its video; label it auto-generated and not human-verified. Inspect representative presenter frames and verify caption timing against each video's duration. Keep all derivatives outside Git and outside the app's public assets regardless of size. `VITE_RC_RECALL_MEDIA_BASE` is unset by default; hide players when it is absent. A local development media server may serve ignored local files for preview. Do not upload to hosted storage or deploy without authorization. Optimize the new instruction MP4 with the same tested profile.
- The source lesson footage is instructor-created content downloaded to the local project corpus. User authorized using those materials for this feature, but this task does not authorize public distribution, hosted upload or deployment. Captions are auto-generated and not verified; spot-check the edited tutorial's chapter/edit boundaries before showing it.
- Database migrations are authored locally only; no remote schema, storage, or media changes will be applied during this work. Do not reuse the existing recordings bucket, since its updates can overwrite files and its LR recovery path can grade data.
- This is a local feature branch from current `origin/main`. No production state will be changed.

## Review dispositions

- Claude review round 1 returned `REVISE` (result `C:/Users/Joshu/AppData/Local/Temp/claudex-mgqhlgt8/result.json`, observed model `claude-opus-5-5`, CLI default model unresolved). Accept F1-F10 and fold them into the plan: separate backup/recovery; UUID + no-overwrite storage and explicit recording visibility; spoken/silent choice and source timing; comparative segmentation and confirmation scope; Cappuccino demo correction; exact phase sequences; RLS entitlement checks; RC-specific full-section eligibility and post-load integrity check; compressed/captioned media delivery; in-app replacement of the LawHub footnote. The external plan review cost/usage is recorded by the runner and is not a media-generation charge.
- F8 disposition: the RC-specific section builder includes all four text-bearing passages regardless of question count. F9 disposition: the source walkthroughs already have local MP4/audio/VTT files; the new instruction video can use the original instructor footage and voice by joining the two full strategy videos with title cards, rather than generating a synthetic presenter.

## Proof

- Unit/component tests for the new logic and UI.
- `npm run typecheck`, `npm run build`, targeted `npm run test -- <new specs>` and the relevant existing Reading Center tests.
- Run the local app and inspect RC Recall, both mode paths, example players, and section list with a browser at narrow, medium, and wide widths.
- Inspect Git diff, including new/untracked assets and migration. Do not report an MP4, database persistence, or production integration as complete unless its exact artifact is present and verified.

## RC Training visual rebuild, 2026-10-16

Joshua rejected the first local page as substantially below LR Recall's visual quality and requested a ground-up redesign. The latest handoff's names supersede the earlier product labels above: **RC Training**, **Check as you go**, and **Retell from the beginning**. The route stays `/reading-center/rc-recall`.

The revised local experience uses an indigo editorial hero, an interactive demonstration using original passage text, native selectable method cards, a three-stage method explanation, expandable complete instructions, a dedicated section setup area, and truthful attempt history states. The practice workspace and completion screen share that visual language. Layouts respond to the available content width, including space lost to the Reading Center rail.

The instructional vision remains complete translation and recall, with details and connections intact. Retell from the beginning preserves the individual paragraph recap before the additional cumulative recap. Check as you go preserves silent paragraph recall, a brief silent confirmation, and optional passage-end recall. Existing instruction/media gates, account scoping, recording isolation, and persistence contracts remain in place. The scope copy now correctly identifies the current A or B rather than promising the whole passage pair.

This remains local on `feat/rc-recall`. Browser checks found that attempt history and real section launch fail in this preview. Do not describe persistence or authenticated end-to-end acceptance as complete. No commit, push, deployment, hosted media upload, or remote schema change is authorized by this visual rebuild.

## Approved workout hierarchy, 2026-10-16

Joshua confirmed one RC Training tab containing two workouts: RC Recall (cumulative retelling, previously Retell from the beginning) and RC Flow (paragraph recall with brief silent text confirmation, previously Check as you go). These names supersede earlier naming proposals above. No additional category hierarchy or separate RC workout tabs. LR Training stays unchanged. Implementation remains local with the existing procedures and deployment boundary.


## Single paragraph workout, 2026-10-16 (supersedes two-workout hierarchy)

Joshua requested one RC Training workout and asked to verify the recorded source. The original Cappuccino lecture notes and corpus workout confirm: read/translate a whole paragraph; hide text and silently recall that paragraph; briefly check all text read so far; continue. Cumulative hidden retelling is the separate Decaf procedure and is no longer offered for new attempts. Whole-passage recall remains optional at passage end. Historical modes and records stay intact.

Joshua selected untimed practice with an elapsed timer. Setup now offers an optional elapsed display; passage time resets between passages, section total continues, and total duration is tracked even when hidden. No countdown, forced cutoff, or required six-minute goal.

The local page follows LR Training's centered introduction and direct setup order. Removed workout-selection cards and comparison slogans; clarified instructions and the original-text demo; added section/history retries and mobile anchor offsets. The legacy mixed-method video is hidden from this single-workout workflow. No source media changes or uploads.

Verified: 79 focused tests, typecheck, initial production build; browser setup and navigation at 320/768/1024/1440, keyboard PrepTest selection, and isolated synthetic runner through completion with simulated saves. Passage timer reset and timer hiding were exercised. Real save/history acceptance remains blocked by the existing backend connection/schema issue; no remote migration or deployment performed. Final production build after polish is being checked separately.


Final verification, 2026-10-16: production build and postbuild passed after the last polish; 79 focused tests passed. Source and UI reviews found no blockers in the local single-workout change. Real save/history acceptance remains unresolved; not published.

## Subsequent full audit, 2026-10-16

The broader read-only audit supersedes the narrow no-blockers statement above. It confirmed missing-backend-table failures, incorrect LR/RC scroll transitions, and instructional/history gaps, and identified additional recovery risks in source. See [RC Training audit and proposed plan](2026-10-16-rc-training-audit-and-plan.md). Joshua requested audit and planning only at this stage; no further implementation or media production is authorized by that audit.

