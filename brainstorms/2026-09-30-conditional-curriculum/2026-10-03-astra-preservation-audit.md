# Astra opening preservation audit

Checked 2026-10-03 at 2026-10-03T07:46:54-04:00. Read-only app inspection; only this audit artifact was written. No source archives, ledgers, app files or tests were modified by this audit.

## Protected contracts match the frozen input

The [40-file frozen manifest](claude-pages-input/manifest.json) has SHA-256 `b95f3d991bb848268e6a571dc4b73a083d08f13738b22d599f472a2bb88d49d6`. Every preserved snapshot file matches its manifest hash. **All 31 protected files listed below are byte-identical to that snapshot.** This includes assignments, progress, routes, teacher fields, the complete curriculum bundle, source content and historical recorded questions. At the final frozen-app check 32/40 total manifest files match; eight authorized files differ. ConditionalReferenceSequence.test.tsx remains identical but is conservatively excluded from the protected set. The earlier in-progress check was 34/40 and 33 protected; two authorized regression-test updates explain the final reduction.

The snapshot predates this turn and is **not an exact turn-start baseline**. The [preceding clip-integration proof](visual-proof/voice-application/2026-10-03-clipped-group12/README.md) reports 37/40 matching after changes to ConditionalOpeningLesson.tsx, ConditionalReferenceSequence.tsx and ConditionalOpeningLesson.review.test.tsx. Those three already differed before this turn. Their current differences must not all be attributed to Astra. The three opening CSS files differ now but were reported unchanged at that earlier checkpoint. No byte snapshot of the intervening three edited files was supplied for exact turn-only attribution.

## Recorded content inventory is unchanged

Parsed the current UTF-8 curriculum.generated.json after verifying its full-file hash against frozen bytes. It has 30 units and 296 recorded drill questions: 98 beginner, 98 medium, 100 advanced. The four opening units contain 62 questions (20/20/22). The remaining 26 units contain 234 questions (78/78/78). These counts exclude guided examples and new local formative interactions.

Later unit IDs remain: rules-facts, truth-validity, negation, contraposition, group-3, group-4, mixed-translation, implicit-conditionals, direct-linking, no-link, triggering, and-or, de-morgan, domain, biconditionals, whole-rule-negation, mbt, sufficient-assumption, necessary-assumption, flaw, parallel, principle, quantifier-meaning, quantifier-negation, quantifier-linking, quantifier-invalid.

Read existing contract tests without executing them: opening-coverage.test.ts fixes the 62-question current answer contract and four historical originals; assignments.test.ts covers teacher scope, levels, legacy membership and unauthorized widening; progress.test.ts and useConditionalProgress.test.tsx cover edition stamps, resumable choices/diagrams/timers, historical answers, unknown lesson keys, concurrent revisions and owner changes. Byte preservation establishes unchanged implementations and tests, not fresh passing test results. The builder/parent owns execution and final functional proof.

## Final authorized inventory and limits

The application was reported frozen by the parent and builder before this recheck. Eight manifest files differ: ConditionalOpeningLesson.tsx, ConditionalOpeningLesson.review.test.tsx, ConditionalReferenceSequence.tsx, opening.css, opening-polish.css, reference-sequence.css, ConditionalLessonNote.test.tsx and routes.test.tsx. The last two were authorized after the broad suite exposed stale whole-page assumptions. Read their exact diffs: they navigate the real page controls before interacting, verify the completion control is absent before the final page, and retain completion/edition/attempt assertions. The reference-step test now checks the ordered unique step set because a source step can span pages. Actual routes.tsx and ConditionalLessonNote.tsx remain byte-identical, as do all assignment/progress implementations and recorded-content contracts.

Nine files are excluded from the protected set: those eight and the unchanged ConditionalReferenceSequence.test.tsx, retained conservatively as a potentially editable opening regression file. Six new files outside the old manifest were confirmed and hash-recorded below. This is a final local file inventory, not evidence of deployed behavior. Parent owns the final broad test run; no test execution is claimed by this audit.

Git status also contains pre-existing or unclassified dirty paths outside the manifest, including public/data/_bank.generated.json, public/data/finder-address-index.json and supabase/functions/mcp/index.ts. No exact pre-turn hashes for those files are available in this manifest. This audit makes no preservation claim for them and does not treat their dirty status as evidence of changes by this turn. The manifest is bounded and does not cover the whole repository. No live database, authenticated student persistence, assignment delivery or deployed production state was inspected.

## Final changed and new file hashes

Checked 2026-10-03T07:52:32-04:00.

| File relative to app root | Current SHA-256 |
|---|---|
| `src/bootcamps/conditionals/routes.test.tsx` | `bedffcfedabf8a47ceeb92c0d3a164eea0703f977ce7c58c8019e9f7c0739f7f` |
| `src/bootcamps/conditionals/components/ConditionalLessonNote.test.tsx` | `2e72358fd103e53508cbfd4f02f52c0f032217aee1b3d7456588aa4386a83871` |
| `src/bootcamps/conditionals/components/ConditionalOpeningLesson.review.test.tsx` | `9cdd9a6e3b2dbce228644b696e8887d19e845f83d2ea463673f7db497bd52b9e` |
| `src/bootcamps/conditionals/components/ConditionalOpeningLesson.tsx` | `09d56267162d6773b08c1d2e9f8e4b3d6fc344380cb42fdc4832a02d216f7ddb` |
| `src/bootcamps/conditionals/components/ConditionalReferenceSequence.tsx` | `2137794d99cf1e2887c83e0534da3b9580696c50d2ee92b9be3f9bffaef1cde5` |
| `src/bootcamps/conditionals/components/opening-polish.css` | `781d6c9cd98c88f013029a129b7147bf3780c2998736d2f12f7bcc5592c9f82e` |
| `src/bootcamps/conditionals/components/opening.css` | `d1c3f838f9337a2682510ecf98f3c32db59be02b123c49fd3d6138d5d4b3d68b` |
| `src/bootcamps/conditionals/components/reference-sequence.css` | `ed0bc7929c0d48a483ffe9f93684bd59b298221eb6fbc9221636a4f5be92e778` |
| `src/bootcamps/conditionals/components/LessonPages.tsx` | `a8330328ec87e40bc2f28a25d8a750254cdfa84af3339f73490a1920a937b500` |
| `src/bootcamps/conditionals/components/StudyDeck.tsx` | `b22fc8f835172832c4099fbe9584b7da341af33a31b29aed1295da739c2fee9b` |
| `src/bootcamps/conditionals/components/CounterexampleLab.tsx` | `7f4dfdc69777b75466b4e95839a0c3eaa2a4b55dc16dfd8539af5f886171161c` |
| `src/bootcamps/conditionals/components/lesson-pages.css` | `b53de48648e6d4ff06c4740056e3a2f3631fc74b29e9ce506ac34891e820d0e8` |
| `src/bootcamps/conditionals/content/indicatorFlashcards.ts` | `7771abc878559b26216b2ee7c30ce0c66ade402954504df45fd7e4ba61a0c6c6` |
| `src/bootcamps/conditionals/components/LessonPages.test.tsx` | `273009fb631a7022c4f33316832272b97e6ee01743de1f8f0497a28937b5b83a` |

## Reproducible protected hashes

| Protected file relative to app root | SHA-256, frozen and current identical |
|---|---|
| `src/App.tsx` | `eef49221a7a4b4f3496c4979abb11355dfd437fd57df109c261c202de3965260` |
| `src/bootcamps/conditionals/assignments.test.ts` | `ec97ae7e4b36cb39855d048d83a2431d93a7f4e7b2eb2f91a9a5001e5bc1ec2f` |
| `src/bootcamps/conditionals/assignments.ts` | `5e1963c6cf4c1a9438164cf3c27215133ed17f0db460570be0882704c88489dd` |
| `src/bootcamps/conditionals/curriculumPath.ts` | `6370b0234fbcd511e0c4676592471651c2d29ebd61df58973a51e48579f7f0c1` |
| `src/bootcamps/conditionals/notes.css` | `f15976462b9d76b8d705e40e87c44912c770c0d30f71a6a5cc49b66126decf17` |
| `src/bootcamps/conditionals/openingRevision.ts` | `4a005ecdca298f1fe1a42319d63eaee51cc9a8679324e8916f981d194de52e92` |
| `src/bootcamps/conditionals/progress.test.ts` | `e820957bb9e7d423ff7355b81709cb7ad6cf997e3401e8b09cbb2f1660297144` |
| `src/bootcamps/conditionals/progress.ts` | `e438914de88dd3166e0758809b5112856ffe32d67813263ef54285a199c0ad7b` |
| `src/bootcamps/conditionals/routes.tsx` | `434a55cfe8dfc785cfd4cea5b7dd459467102c05aa7380f17976eeb70a45ee2e` |
| `src/bootcamps/conditionals/styles.css` | `ff1bd1e737889b5998cf7b6b2cb54b4430b74a78a06f85a2c32218601ddf30e3` |
| `src/bootcamps/conditionals/useConditionalAssignments.ts` | `a8988f5701f5f524e3c6373798c3a0bc0c6511ecec5a95183c652f61e308bd74` |
| `src/bootcamps/conditionals/useConditionalProgress.test.tsx` | `e88c4b5021940330559d103990e3336e8f4ce2c2b2d72d135e89a03900331346` |
| `src/bootcamps/conditionals/useConditionalProgress.ts` | `cdbd57808b39cfdd2de6d57d13af7d1c80249b52c2c789569d337f79e99dcf66` |
| `src/bootcamps/conditionals/components/ConditionalLessonNote.tsx` | `55c7be469bfef6d60c1e0c90b15d83464967a3604e16d50da058bf2d50a170b2` |
| `src/bootcamps/conditionals/components/ConditionalOpeningMedia.tsx` | `459521bcc900015b437f76195da81de5bb6ab74d72a09acef242990916531c38` |
| `src/bootcamps/conditionals/components/LessonInteractions.tsx` | `006385caa44ea18ebf391c044f612c689c3e5634e4c8650f37b0cd01eea7adea` |
| `src/bootcamps/conditionals/content/applications.source.ts` | `3ff62e579aa70d680ca84c8c5b7b7d43125285963fb8107de2373df3a6560c2e` |
| `src/bootcamps/conditionals/content/foundations.source.ts` | `8157785294b3c902382db1cf0d66d2f1a3df74a32e7e0f612eddffafce56eaa0` |
| `src/bootcamps/conditionals/content/index.ts` | `c3b320960054825ad9da6dc259c7c178b92a56bce7decffbdac8420fb77880cd` |
| `src/bootcamps/conditionals/content/legacyQuestions.ts` | `ad91b8a4a6fd59acd5c5d9b72ab3c9bc00e54d64475a2bcb18891b3ad54b04b9` |
| `src/bootcamps/conditionals/content/opening-coverage.test.ts` | `626db89fc67bb6d76eb36548cbc4f618f7522afad8d9ae6d1fd7aee05bfbf540` |
| `src/bootcamps/conditionals/content/types.ts` | `aedac2e250175b85387b1a15e8267ee8f39e0b616bb3cdd6add8f82f77391daf` |
| `src/bootcamps/conditionals/content/validate.ts` | `ab28d0710f35ef4c8aad9cd5d96a903595b5943e753d1634b4b79a139f1af207` |
| `src/bootcamps/conditionals/data/curriculum.generated.json` | `4b2afd7a7a9b4ebe17359131c2eb4873770e1f4e8c6ffce463bc7730d863868b` |
| `src/components/teacher/ConditionalAssignmentFields.test.tsx` | `10c903b7a3533499971e332f577dbd62e0c015bb7300ad51303ad9dcae4a9928` |
| `src/components/teacher/ConditionalAssignmentFields.tsx` | `9975d3cd7bbf3def762ac0acceee66e58579f9923f804829a2ba9a440d6c8e18` |
| `src/components/ui/dynamic-island-toc.inline.test.tsx` | `fe711dbe2cd606b3efe19d41bdddd0c5243b4ac0bb0068b08c826a7b2ff4f111` |
| `src/components/ui/dynamic-island-toc.tsx` | `c3192146db83a500db480512ffa294cc80fe2aed8f637c81225fe3b4cb0fbf3f` |
| `src/dev/ConditionalOpeningPreview.tsx` | `bdc5b3507ee3e1d99635b2d926312a139578481966ddabc21451a7781779dc4c` |
| `src/lib/conditionalBootcampAssignment.test.ts` | `d5e5b20e1c2765a1a32c41edb4458fd971789bcb3bd4d8674c87a1bc4c322ee6` |
| `src/lib/conditionalBootcampAssignment.ts` | `9b9d909aa12cdbeded57577f499ba0bada38ab82b29c96b27c99c55d4e7d8dc8` |
