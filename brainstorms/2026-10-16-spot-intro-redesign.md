# Spot introduction: readable instructions and restrained presentation

## Authorization and roles

2026-10-16. Joshua explicitly requested human writing, coherent typography and page order, no gold/beige pairing, a sleek neutral button, supplementary video, and durable visual/copy records. Codex coordinates and implements; Claude independently reviews the plan and final changes. CLI model inherits Claude configuration; identity must be read from results rather than assumed. Maximum plan rounds 5, final inspections 2. Artifacts stay in vault handoffs outside the app checkout. No paid Lovable action or production write is authorized by this plan.

Repo: C:/Users/Joshu/dev/ai-os-projects/lsatu-relationship-ui. Baseline 4ca9306fd7876450dfd1bdbc6f6eaaa2053a9b58. Unrelated generated supabase/functions/mcp/index.ts dirt must remain untouched and uncommitted.

## Evidence and assumptions

- User's three annotated browser comments plus direct signed-in DOM readback show small uppercase title, oversized two-line slogan, small subtitle, full-width dominant video, instructions below it, Worked example, brown text and gold Start on beige.
- Current source: src/features/activity-centre/components/RelationshipIntro.tsx and relationship-intro.css. Live grading/question repairs from the previous task have separate publication status and must remain intact.
- Existing authorities: app DESIGN.md and .impeccable/surfaces/src-features-activity-centre.md; vault wiki/teaching-voice.md, references/lsat-teaching-voice-standard.md, wiki/COPY-CORRECTIONS.md. Use humanizer embedded mode; do not make a new universal design guide.
- Gold is rejected for these page controls; beige is not globally banned. Signal is not a banned word globally, but the formulaic instruction signal it is rejected here. Worked example and What to write are rejected as student labels. Preserve the existing instructional film, captions, fallback, and inline playback; its embedded lamp artwork is not part of the page-control palette revision.
- Sleek means legible type, deliberate spacing and restrained contrast. No microscopic eyebrow, oversized slogan, metallic accent, decorative gradient, new font family, animation or pill/bento treatment is needed.

## Concrete copy and structure

1. Header: Exit control followed by a single h1 using the actual activity title, at roughly 30-34px desktop / 26-30px phone, in the established activity UI sans family. No duplicate title eyebrow and slogan. Lead: **Decide whether each sentence contains a conditional, causal, or comparative relationship.**
2. Main written section headed **Instructions**, with a short, readable sequence:
   - **Read the whole sentence.** The earlier second sentence was deliberately removed after viewing the page because it repeated the lead; the lead already names the three types.
   - **Give the type and a quotation.** Quote the words you used to identify the relationship. If you find more than one type, include each one with its own quotation.
   This copy expresses the existing grading requirement, including multiple types, without requiring a prose justification or using indicator jargon. It must be checked aloud in the page context and may receive minor natural-language edits without changing the task.
3. **Example** follows immediately in the same reading column. Retain the lantern sentence and answer **Conditional, “only if”**. Label its answer **Answer** rather than Example answer. Explain plainly: **The wick has to be dry for the lantern to be lit. “Only if” tells us that. A dry wick alone does not guarantee that the lantern can be lit.** Preserve necessity and no causal inference.
4. Retain a plain expandable relationship reference with accurate sufficient/necessary, causal and comparative definitions. Do not add a transcript or attempt-policy paragraph. Start/Back to question control follows the written example/reference in the main column. Preserve save/preview truth but reduce the preview note to **Preview only. Student progress is unchanged.** Other save modes remain truthful.
5. Supplementary aside headed **Video instructions**, visually smaller than the written column. Retain inline video, caption track, preload none, playsInline, no autoplay and a position-neutral error fallback: The video could not load. You can use the written instructions on this page. The native video fallback also refers to instructions on this page, never below. Desktop layout: main column about 560-620px, video rail about 280-340px; mobile/docked: written instructions, example/reference and primary action precede video in DOM and visual reading order. Video stays fully usable.
6. Use scoped cool-neutral page and white example grounds, dark ink, clear muted slate only for secondary text and hairlines. Use scoped semantic overrides with the existing Workroom light HSL values from index.css and existing typography. Activity Centre pins warm semantic values locally, so inheriting those values is insufficient. Import the real activity-centre.css in the local fixture before verification. Keep the current Activity Centre always-light policy; root-dark fixture mode must also remain neutral light within the activity, not literals scattered through JSX. Primary button is Workroom ink with white text, sober radius and clear hover/focus. No gold control, brown-on-brown text, shadows or warm metallic gradients. The activity runner's scoped scene remains unchanged.
7. Body copy 16px minimum on normal screen widths; section headings about18px, modest consistent weight/spacing. Keep labels readable and close to their content. No uppercase microlabels. No text gradients. Maintain 44px touch targets and visible keyboard focus.

## Durable correction and retrieval

Update DESIGN.md near its entry as the pre-design reading/checklist pointer: read the relevant surface brief, teaching voice, and dated correction examples before drafting. Add these exact user preferences with scope and provenance, superseding the earlier recommendation to say signal it. Update the existing activity surface brief and vault COPY-CORRECTIONS ledger. Store before/after screenshots and a compact visual comparison in the existing documentation/evidence homes; include the rejected pattern, replacement, reason and responsive checks. Do not overwrite historical evidence or claim the replacement is Joshua-approved before he views it.

Add one native-memory update note under C:/Users/Joshu/.codex/memories/extensions/ad_hoc/notes/ because Joshua explicitly asked to remember these preferences. Do not edit MEMORY.md. Do not modify protected AGENTS.md/CLAUDE.md merely to grow instructions. A document is persistent guidance, not a guarantee every future agent automatically reads it; strengthen the existing design entry points and state this limit honestly.

## Acceptance and verification

- The first viewport makes the task and example easy to find; written instructions precede video in DOM and phone layout. No duplicated mini-title/giant-slogan/micro-subtitle hierarchy.
- No student-facing Worked example, What to write, signal it or old create-it instruction in the revised introductory copy. Preserve valid uses of signal in scientific content, grading keys, internal names, and film assets. Check the active response placeholder too: if it repeats the rejected stock instruction, replace only the generic task prompt with **Give each relationship type and quote the relevant words.** Update only JSON subtitle, instructions.task, instructions.answer_placeholder and the presentation constant. Leave instructions.coach.drill, all coach rubrics/rules and item keys untouched. Section mode may show those student fields, so cover its copy while preserving its workflow. The exact-title/non-section ActivityIntro dispatch remains unchanged; renamed titles still use the editorial fallback and are outside this layout revision. Do not perform a global find/replace.
- Existing exit/start/resume callbacks and truthful persistence modes still work. Video remains inline, captioned, controllable and recoverable on failure. No transcript returns.
- Run existing intro/copy tests and any narrowly necessary regressions for reading order and controls. Rewrite RelationshipIntro.test.tsx ordering assertions to require Instructions, Example/reference and Start before video, with Instructions/Example/Answer labels and new preview notice. Assert rejected copy absent; retain exit/resume/captions/no-autoplay/error/no-transcript/save-mode coverage. Update relationshipPresentation.test.ts for the new every-type placeholder; retain the coach.drill signal-it assertion because that internal grading instruction is deliberately unchanged. Add a section-mode dispatch/props regression with the real JSON student fields, without changing section dispatch. This verifies the handoff contract to SectionLaunch; its RRC-specific rendered method layout is not the Spot introduction and is outside this redesign. Run npm run typecheck and npm run build before delivery/push.
- Inspect rendered 390/768/1230-1440px and docked ~520px widths, actual Activity Centre always-light host with both light and root-dark ancestor contexts, no horizontal overflow, readable type, keyboard focus and actual text/button contrast >=4.5:1. Use supported browser viewport capability rather than DOM mutation. Save before/after evidence and final screenshot. Test Start and resume without production state writes or provider calls.
- Claude final inspection must examine actual changed source/tests and evidence references; disclose if the reviewer cannot view images. Approval of source or plan is not proof of visual preference or deployment.
- Commit intended app files and push via .claude/safe-push.sh, preserving concurrent main work. Deployment/content/database changes remain separate, no paid prompts. Keep the user's live tab intact; show a local preview as a reviewable deliverable when possible and label it local.


## Plan review arbitration

See 2026-10-16-spot-intro-dispositions.md for F1-F6. All responsive widths retain usable Start/resume; no No Start in docked requirement exists. Use the existing Lexend/Outfit UI family and Workroom semantic variables.


## Inspection fix round 1

Claude inspection claudex-upy71e44 correctly found that the first isolated fixture omitted activity-centre.css, whose local warm tokens defeated global neutral inheritance. Fixed the scoped neutral semantic values and imported the real stylesheet. Regenerate screenshots/measurements and label the older root-dark image as an invalid integration reference, not production. Preserve documented pre-existing generated MCP dirt outside the intended commit; do not restore or delete unrelated work. Final commit path inspection must prove its exclusion. Use a fixed dark video ground and an explicit comment for the deliberate media-query fallback.


## Inspection budget closeout

Two independent source inspections completed. Second result claudex-kqyfg_of remains REVISE because the promised section-mode test was missing. Parent added ActivityIntro.sectionCopy.test.tsx and documented the duplicate lead/step removal. Source inspection confirms SectionLaunch is an RRC-specific renderer that may prioritize instructions.tagline; this new test verifies dispatch/props, not a claim that a synthetic Spot section has a redesigned RRC UI. No more reviewer calls are made beyond the configured two-inspection budget. The final test/plan-only follow-up is host-verified and not independently re-reviewed. The generated MCP file remains excluded from commits.
