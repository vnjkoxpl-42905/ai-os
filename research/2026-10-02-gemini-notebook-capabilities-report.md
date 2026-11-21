---
type: research
subject: Gemini Notebook capabilities for Conditional Bootcamp
verified: 2026-10-02
status: reference, not approved curriculum
---

# Choose each Notebook feature for a specific learning job

Verified against Joshua's open Codex notebook and current official Google help on 2026-10-02. Public documentation describes product capabilities; live UI evidence establishes which controls Joshua currently has. Curriculum uses below are recommendations, not Google claims. No artifacts were intentionally generated, added, edited, or shared. During subsequent source review, an attempted report-opening interaction unexpectedly created an empty New Note; this was disclosed and left untouched.

Notebook: [Conditional Logic | LSAT Logical Reasoning](https://notebook.google.com/notebook/e38c0aff-bb6e-498e-a5ef-a6b1bc3a6f5c). The page displays PRO, three selected sources, nine Studio tools, and an Interactive Reports announcement.

## What each Studio tool can do

| Tool | Capability and controls | Outputs, interaction, and limits | Proposed conditional teaching use |
|---|---|---|---|
| Audio Overview | Deep Dive, Brief, Critique, Debate; source selection, focus prompt, language, and length. All four formats verified in Joshua's UI. | Downloadable audio and sharing. English interactive mode allows questions to the hosts; a shared audio link does not give recipients that interaction. Length adjustment is documented as English-only. | Optional recap after the lesson; Critique for reviewing our teaching draft. |
| Slide Deck | Detailed Deck for reading independently; Presenter Slides for teaching aloud. Language, audience, outline, style, source scope. | PDF and PPTX exports. Slide revisions can change text, layout, visuals, deletion, and order; revision generation creates a new deck. Google says source material is not considered during revisions. Documentation lists short/default/long, but Joshua's inspected panel showed only short/default. | A small worked sequence showing a rule, a fact, and what follows. |
| Video Overview | Cinematic, Short, Explainer, all verified in the live panel. Focus prompts and source selection. Documentation describes language and visual styles for applicable formats. | Playback speed, seek, fullscreen, download, sharing. Short is approximately 60 seconds; Cinematic is English-only and 18+. Style controls exclude Cinematic and Short. | Optional visual explanation of a single idea, such as one-way guarantees. |
| Mind Map | Branching topic overview; expand/collapse branches, zoom, and select nodes to ask chat questions. | Download and notebook sharing. A concept hierarchy is not proof of a logical implication. | Teacher map of concepts and prerequisites; optional student recap. |
| Reports: Document | Structured written outputs, configurable structure and focus. Live templates include Briefing Doc, Study Guide, Blog Post, Create Your Own, and source-specific suggested templates. | Document output; Docs export, and tables to Sheets. Exported edits do not synchronize back. | Main teaching explanation, worked examples, glossary, and recap. |
| Reports: Interactive | Learning Overview with written sections and embedded Studio content. Live customization offers language and a prompt to restrict topics, sources, or artifact types. | Web-only. In Joshua's existing report, a table of contents and readable sections accompany recommended artifact cards with Add buttons. Recommendations are not completed embedded artifacts. Some content is 18+. | Candidate lesson container connecting explanation, illustration, and practice. |
| Flashcards | Fewer/standard/more, easy/medium/hard, source scope and topic prompt. Live UI additionally offers images versus text only. | Explain, self-mark got/missed, retained progress, missed-card review, shuffle, and CSV export are documented. CLI already retrieved the existing deck as JSON. | Recall the meaning of a guarantee and explain what is unknown when the trigger is absent. |
| Quiz | Fewer/standard/more, easy/medium/hard, source scope and topic. Live question types: multiple choice, multiple select, fill in the blank, short answer. | Hints, explanations, results, review/retake. CLI already retrieved the existing quiz as JSON. Each question type's grading behavior has not been tested here. | Require a student to distinguish guaranteed, possible, and impossible; short answers can expose reasoning. |
| Infographic | Single visual summary. Language, landscape/portrait/square, concise/standard/detailed beta, style and focus. Live styles include instructional, scientific, sketch note, professional, and others. | PNG download, zoom, sharing. Text, arrows, and factual details require review. | A visual reference showing the one forbidden case of a conditional. |
| Data Table | Structured extraction/comparison using prompted rows and columns, language, and source selection. | Sheets export puts table data on one tab and citations on another. Table structure does not automatically establish the correctness of reasoning. | Teacher coverage matrix: concept, lesson, example, misconception, interaction, drill, answer rationale. |

Feature references: [Audio](https://support.google.com/gemininotebook/answer/16212820?hl=en), [Slides](https://support.google.com/gemininotebook/answer/16757456?hl=en), [Video](https://support.google.com/gemininotebook/answer/16454555?hl=en), [Mind Maps](https://support.google.com/gemininotebook/answer/16212283?hl=en), [Reports](https://support.google.com/gemininotebook/answer/18323649?hl=en), [Flashcards and Quizzes](https://support.google.com/gemininotebook/answer/16958963?hl=en), [Infographics](https://support.google.com/gemininotebook/answer/16758265?hl=en), [Data Tables and exports](https://support.google.com/gemininotebook/answer/16206563?hl=en).

## Source choice controls the scope of learning

Source selection is visible in the artifact creation controls. We should supply narrowly scoped, reviewed teaching notes for each lesson instead of relying on an entire course to stay within introductory boundaries. Existing artifacts show different source counts: some use one source, others three.

Google supports documents, presentations, spreadsheets, images, audio, web text, and public captioned YouTube videos. A YouTube import contains the transcript rather than the video's visual demonstration. This matters for conditional diagrams shown on screen: we may need reviewed written descriptions or separate visual sources. Source guides, Fast Research, and Deep Research support finding and inspecting material. [Source capabilities](https://support.google.com/gemininotebook/answer/16215270?hl=en).

## Notes and chat serve different purposes

Notes can contain Joshua's own text or saved chat responses. Saved response notes are not editable; notes can become sources and can export to Docs or Sheets. Notes and exported documents are separate copies. [Notes](https://support.google.com/gemininotebook/answer/16262519?hl=en).

Source chat provides citations and Default, Learning Guide, or Custom styles. Current documentation also describes experimental agentic chat for research, code, charts, file creation, and artifact versions. Treat these as a separate capability from ordinary source-grounded answers; availability and behavior were not tested in this account. Mobile live voice chat is distinct from joining an Audio Overview. [Chat](https://support.google.com/gemininotebook/answer/16179559?hl=en).

## Current usage documentation supersedes old daily quota assumptions

Google's dedicated usage page says compute-based limits began 2026-09-02, with five-hour refreshes constrained by weekly limits. Feature choice and request complexity affect usage; Studio can display expected usage and offer Generate later. Some individual feature pages still show daily counts. Preserve this documentation mismatch and consult the account Usage screen before budgeting a production workflow. We did not inspect Joshua's remaining quota. [Current usage policy](https://support.google.com/gemininotebook/answer/17670842?hl=en).

## What we can access now

- CLI authentication and notebook listing are verified. Existing flashcards, quiz, study guide, and mind map contents were successfully retrieved in the preceding access check.
- Three CLI unknown-type items are identified by the browser as Interactive Learning Overviews. One was opened and read during this inspection. CLI listing does not mean this new type is supported for export.
- Audio, video, infographic, slides, flashcards, quiz, Data Table, and report customization panels were inspected without selecting Generate. The existing mind map's interactions were established through official documentation, not by creating another map.
- We did not test generation, every export path, every quiz grading mode, shared recipient interaction, mobile behavior, or embedding these outputs in LSAT U. No claim of full end-to-end interoperability is made.

## Start the introduction with one clear learning outcome

Recommendation for joint review: the student should understand that a conditional guarantees an outcome when its trigger is met, while other cases may remain open.

Proposed sequence: **short explanation -> worked example -> manipulable case activity -> guided reasoning -> independent drill -> recap**.

Use a Document or Interactive Learning Overview as the explanatory container. Use our nested-box activity to experience inclusion, then a four-case activity to test the rule. Use a quiz to explain which conclusions follow; use flashcards for later recall. Audio and video are optional alternative explanations. A Data Table helps us audit coverage as teachers.

These are curricular judgments, not verified learning-effectiveness comparisons. Joshua still controls the lesson boundaries, assignments, and approval. Students should see their assigned lesson and practice; generation difficulty settings are teacher authoring controls, not a student level selector.

The inspected generated overview mixes fundamentals, contraposition, indicators, and chaining in one report. It is broader than our first lesson. Its formula rendering is broken in several places, and it includes an unsupported numerical claim about questions lost. It also labels Groups 3 and 4 in generated text; reconcile those labels against Joshua's authoritative notes before reuse. The report is reference material, not approved lesson copy.

## Research provenance

Two Firecrawl agents were launched with structured schemas and 10-credit caps. Both failed with max-credit refusal and returned no research; both reported creditsUsed: 0. We did not raise the cap or claim successful agent findings.

Firecrawl subsequently scraped ten official help pages successfully. Two additional pages hit HTTP 429 and were read through the web tool instead. Raw responses, page hashes, and scrape failures are preserved in `.firecrawl/notebooklm-capabilities-2026-10-02/` and the agent job/result JSON files. Research synthesis uses official pages and direct UI observations.
