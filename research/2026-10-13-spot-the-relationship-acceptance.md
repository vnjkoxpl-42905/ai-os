# Spot the Relationship: release and remaining acceptance

## 2026-10-14 introduction repair

Joshua approved fixing all marked introduction defects and reopening the activity. Commit 09962f29 replaces Spot's editorial/orb intro with a scoped, readable launch: three numbered instructions, one worked example and its reason, an optional three-type guide, plain hint/answer wording, and one in-flow Start action. Explicit paper/ink colors avoid the conflicting world theme cascade. Existing assignment snapshots receive the current frontend instructions without rewriting any saved work. Preview and ordinary unsaved runs have truthful distinct copy; only a run explicitly marked persistent promises saved submitted answers.

Local verification passed 49 tests across intro, dock, seeded content shapes, resume and saved practice. The production build and 758-file content guard passed. Browser inspection of the production-equivalent local wrapper confirmed actual visible text and contrasting colors, one static Start below content, no overlap or horizontal overflow at widths 320, 375, 640, 768, 1036 and 1440. Expanded guide reflow and keyboard focus were checked. The shared dock unit test now targets the editorial component; the seeded test asserts Spot's deliberate replacement independently. Independent source review found its two issues addressed. Push/typecheck and production publication are in progress; live reopening is not yet claimed.

Final typecheck passed and 09962f29e5e78748db5bf60538f470b6d3449653 was safely pushed. Lovable ingested that exact SHA; free publication 7c1b9133-5be4-49c7-9063-a277a88bcc5a requested. First live marker read still served the earlier CompletionSummary-Br4tvnn0.js, so publication is not yet verified at this point. No paid agent prompt, provider call, assignment rewrite or notification was made for this UI repair.

Publication subsequently verified through new live index-DxUZykMm.js and CompletionSummary-BVGQS5KV.js, containing all four new intro/guide/action/unsaved-copy markers. Opened a fresh live teacher preview in the in-app browser at ?intro=09962f29 and verified the new three-step instructions, example/reason and exactly one Start. Actual production computed title ink rgb(27,23,19) contrasts with paper rgb(244,239,231); Start is static, the old dock is absent, and there is no horizontal overflow. Screenshot visually confirms the readable introduction. Left that live preview open for Joshua and closed only the temporary local QA tab.

## 2026-10-14 user-marked introduction defects, analysis only

Joshua marked three live introduction areas: Start dock, rules grid and hero/instructions. Reproduced on the actual preview tab. The earlier DOM check missed a visual failure: the title and instructions exist but are not readable. Computed title/task ink is rgb(243,240,231), while the wrapper background is rgb(244,239,231). World selectors map Observatory's pale text tokens into the intro; activity-centre's shared background declaration paints cream instead of the intended dark world canvas. Rules text also uses pale ink at 0.9 alpha. This is a confirmed mixed-theme cascade defect, not missing authored instructions.

At the observed desktop viewport, hero height is about 725px and the rules grid begins at y=796. The sticky Start dock spans y=780..872, z-index 30, and uses the dark --aw-page gradient while its surrounding canvas is cream. Its rectangle overlaps the instructions; a second inline Start exists lower down. Dock observer unit tests do not prove unobscured visual visibility.

The generic editorial intro hardcodes 'credited answer' in its two-try sentence and 'After, any of these' above the worked-example answer list. The same example answer already appears in the After circle. This is an example, not a disclosure of the 48-question key, but the wording and duplicate placement obscure that distinction. The visible rules also define a conditional only as what must be true, omitting sufficient-condition rules.

Recommended direction: restore a coherent intro palette, place brief readable instructions before decorative content, label a worked example explicitly as sentence/answer with a short reason, use ordinary 'answer and explanation' wording where accurate, and present one clear Start action without an overlay across instructions. Scope any change carefully because ActivityEditorialIntro and its CSS serve other activities. This pass made no app edits, publication, paid calls or student-record changes. A substantive layout choice remains a recommendation rather than an approved redesign.

## 2026-10-14 status

The earlier disabled-grading blocker is resolved. Joshua approved one additional deployment prompt, completed for 5.5 credits. Lovable's managed readback confirmed migration 0030, enabled=true, grader revision activity-coach-v2-20261013 and the allowlist containing only activity 12251bd3-d260-4108-bc35-bcf478e483e6. Budgets stayed 60/minute, 600/day per actor, 6000/day global, concurrency 3 and lease 30. The deployed function's submitted fingerprint was 248556b893cd0bc144b6b36496371b97b869c57e25ab94acde511c2e6af352b2; a separate live fingerprint was not returned by the tool.

Lovable ran no real provider checks because its preview login was unavailable. The parent used the existing admin login, verified preview ownership, then issued exactly six grading requests. All returned HTTP 200 with expected results: type-only partial; mislabeled indicator partial; missing half of split comparison partial; contradictory indicator denial incorrect; valid item 48 prose correct; corrected second attempt correct. First hints did not reveal the missing answers. This is a bounded live grading sample, not proof against every model error. Exact evidence: research/2026-10-14-spot-the-relationship-live-grades.json. No Gianna answers or completed student snapshots were modified by these preview checks.

Gianna Jean received one verified assignment, 9a438155-71d0-4019-9ab6-356b4fe69a09, with a visible Classroom item and all 48 current keys and explanations. Normal inbox/bell/email notifications reported success. Final merged typecheck, 75 focused grading regressions and build/content guard passed. Free frontend publication 4c9c802c-3b17-44b4-88f7-cb83f4f36ba8 is awaiting live asset verification.

Publication verified: live entry /assets/index-QPF82Kvz.js references report-card-gFikLqmK.js containing strict instant matching and earned-dial markers, plus CompletionSummary-BmN7spE0.js containing grader_revision_changed and durable retry recovery. The initial marker check looked in report-card only; correction followed the actual referenced shared chunk and confirmed the recovery code is served. Final main e2b1236efac8da4e37ac316b8478f8afe2960248.

## Verified release

One paid Lovable prompt completed for 20.1 credits. Its resulting source commit is d8f82e8ac26830de619419ed22c80fb2b858f628. All 48 live questions, explanations and instructions match current source. The unstarted assignment contains the upgraded structured keys and rubric; both completed snapshots remain unchanged.

The grader receives the authoritative key and active rubric. Isolated mock-provider tests confirm receipt admission and payload behavior. Exact affirmative type/indicator pairs earn free instant credit. Contradictory prose and additional unexplained indicators fall through to AI assessment instead of receiving automatic credit.

Frontend repair 83cd8903 was merged into f3faa4639feee6080fa07ea96ed72aaa2adf18c4, safely pushed and published through free deployment 3e39ae65-3aeb-46a4-8e1e-99afecf48f93. Production markers verified in index-CuKguElX.js and report-card-D4PO-Z9y.js. Local browser checks confirmed earned dials and harder-question explanations. Mobile layout checked at 375 pixels. Focused tests: 1769 passed. Final merged typecheck and production build passed, with canonical-content guard across 771 build files.

## Costs and the remaining blocker

Source pins google/gemini-3.1-flash-lite in both activity-coach and gemini-proxy. Output is capped at 220 tokens. The proxy prevents caller escalation. Exact-key recognition and replayed cache results avoid provider charges. The model is Lovable's supported budget text choice; no paid comparison benchmark was run, so absolute cheapest adequate grading quality is not established by these tests.

The paid agent's live configuration query showed activity_ai_configuration_v1.enabled=false. AI grading activation and real model grading quality therefore remain unverified. No paid live grading requests were made.

## Corrections needed before activation

1. First hints must not disclose missing indicators as unquoted or backtick answers, or reveal a missing conditional type as 'if-then'. Hints must not falsely praise wholly incorrect work.
2. Malformed keys, including a missing traps field, must be rejected before a receipt lease or paid budget reservation. SQL NULL must behave as invalid.
3. Cache identity must include a trusted grader revision so prior judgments cannot bypass new grading and hint rules. Completed student records stay unchanged.
4. Enable only this activity through an explicit allowlist; preserve unrelated AI activity behavior.

## Live acceptance after a separately approved deployment

Verify the exact managed migration and activity-coach deployment fingerprint. Read back enabled configuration and the Spot activity allowlist. Exercise a small approved sample: an exact answer with no provider call; type-only partial feedback; a mislabeled indicator; a split comparison with one half missing; item 48 with a correct paraphrase; contradictory prose; first unsuccessful hint versus second-attempt final explanation; cache replay; and reload/resume with correct dials and unchanged completed snapshots. Keep real-call count and cost explicit. Do not use student records for acceptance fixtures.

Another paid Lovable prompt has not been authorized or sent. Deployment and AI activation remain pending that approval.

## Prepared patch

Local draft commits 7d24ff42 and 4b56a99d in ../ai-os-projects/lsatu-str-backend implement the remaining backend guards, allowlist, cache revision and durable retry recovery. Final verification passed: 93 focused tests, 77 isolated SQL identity assertions, 30 Edge/SQL assertions with six mocked provider calls, typecheck and production build with 757-file content guard. The earlier baseline admission run passed 123 assertions. No draft changes were deployed or enabled. The exact prepared next prompt is research/2026-10-13-spot-the-relationship-final-deployment-prompt.md.

## 2026-10-14 follow-up: remove attempt-policy paragraph

Joshua explicitly rejected the entry paragraph beginning "You have up to 2 attempts per question", including its retry/hint and answer-review narration. Source commit 1e6fba1a removes only that paragraph and unused maxAttempts destructuring. Existing mode/save status and grading behavior remain. Four existing intro tests and merged safe-push typecheck passed; main 27ee8e0cb20f6c60535bededbeabd572a257ad39 was ingested by Lovable. Free deployment 891102de-a571-45f6-8bd2-7c39953128c3 requested. First live read still showed the old paragraph; publication remains pending at this checkpoint. Correction captured in COPY-CORRECTIONS and all six matching preference ledgers.

## 2026-10-15 inline instruction video, work in progress

Joshua requested locating the second-brain JavaScript video workflow, creating a creative instruction film and embedding it inline. Found wiki/sources/claude-now-does-video-free-javascript.md and the existing contrapositive-video local Kokoro setup. New source under scripts/media/spot-the-relationship draws eight deterministic canvas scenes with local narration (65.21 seconds). Contact sheet reviewed: task, whole sentence, conditional indicator and requirement, two-part response, causal example, comparative example, mixed types, learner handoff. The narrative avoids the rejected attempt-policy paragraph and does not use live exercise questions.

Inline native player is above written instructions, with user-initiated controls, preload none, a poster, default English captions, a verbatim expandable transcript and error fallback. Six component tests pass after updating the transcript assertion to match the final narration. Local DOM layout checks found no overflow at 320, 375, 640, 768, 1036, 1280 and 1440 pixels. Production build and 759-file content guard pass. Video encoding still stalls during full audio/video export; short samples and video-only checks pass. Do not infer full playback or publication from this checkpoint. No paid generator/provider or Lovable prompt was used.

Encode resolved: this FFmpeg build's default AAC coder stalls on the narration WAV. The fast AAC coder completes; the renderer now encodes local audio separately, then copies it into H.264 video. Final MP4: 65.208333 seconds, 1280x720, 24 fps, H.264/AAC, 1,605,939 bytes. Full decode passed. The browser played from 0 through ended=true at 65.208333 with readyState=4, no reported media error, and English captions showing. Captions were then positioned at 90% to keep the worked answer cards readable. Source/asset commit 7ea139df is awaiting gated push and live publication.

Publication checkpoint: final merged typecheck passed and main 564b9832d4953896f25df5ccb08ac0572909e007 pushed. Lovable briefly reported a separate older sync commit 036dd6b0; inspection confirmed it lacked the video, so it was not published as the video release. Waited until latest_commit_sha matched 564b9832 exactly, then requested free deployment fc12d7f6-4c5b-41b8-b2d6-f709661944b4. Live verification pending. This does not deploy or validate unrelated backend changes from concurrently merged work.

Live publication verified: the public MP4 returns HTTP 200 video/mp4 and SHA-256 matches the local 1,605,939-byte tested file. Poster bytes also match. Live VTT is text/vtt, has all 19 cues and lower caption placement, and matches source after normalizing Git line endings. The signed-in teacher preview now renders Watch how it works, native video, transcript and one Start, with the rejected attempt paragraph absent. Production playback was started successfully with duration 65.208333, autoplay=false, playsInline=true and English caption mode showing. No student progress was changed by this preview.

Production playback subsequently advanced to 43.197415 seconds with readyState=4 and no media error. Verified native Home on the time scrubber returns playback to 0 while paused. Opened the published preview in the in-app browser for Joshua. Temporary local QA tab closed and the owned dev server stopped; no user tabs were closed. Screenshot saved under the task's Codex visualizations directory.

## 2026-10-15 remove transcript disclosure

Joshua marked Read the video transcript and requested removal. Commit 87a26554 removes the disclosure and expanded narration, obsolete transcript styles and stale playback-fallback references. Video, captions, concise written instructions and Start remain. Updated existing tests and generator README; all six intro tests pass. Captured the newer scoped correction in COPY-CORRECTIONS and all six teaching-preference copies, explicitly superseding the earlier transcript instruction for this activity. Gated push and publication pending.

Final merged typecheck passed and main 56b69919 was safely pushed. No full build was repeated for this bounded removal; existing component tests and the required merged typecheck passed. Awaiting Lovable ingestion before free publication. Video media bytes and grading behavior were not changed.

Lovable ingested exact main SHA 56b6991962a55c2ece29ef4c9bd94d05e5c0c411; requested free publication 990205ee-1608-4337-a6cc-e44d10075a3d. First public verification still served index-XnhUXW_t.js / CompletionSummary-DEQfRLip.js containing the old transcript class, so that first check did not establish publication. No paid Lovable prompt was sent.

Publication verified: Lovable's free publish panel reports Published / Your website is up to date. Public index-Bk1k_eSg.js references CompletionSummary-BNIktqlA.js, which retains how-to-play-v1.mp4 and contains neither relationship-video-transcript nor Read the video transcript. Free deployment 990205ee-1608-4337-a6cc-e44d10075a3d. No paid prompt or billing changes were made.
