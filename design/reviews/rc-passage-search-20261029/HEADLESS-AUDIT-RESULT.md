# Headless Opus5.5 High evidence audit

2026-10-29. Observed model: claude-opus-5-5. Requested effort high. CLI2.1.309. Read-only review; no browser. Artifact: C:/Users/Joshu/AppData/Local/Temp/claudex-o3yi_nru/result.json

{
  "verdict": "REVISE",
  "summary": "This works as a standalone Claude Design exploration, but it does not complete the original request. How each requirement stands against the evidence:\n(1) Model: the request asked for Opus 5.5 High. The first pass ran on Medium (REPORT.md:8, :24). The High revision is backed by the host's account (REPORT.md:44) and by the composer showing \"Opus 5.5 High\" in high-phone.jpg. That screenshot only shows the selector setting when it was captured, not which model produced each turn. The reviewer is Opus 5.5 (Claude Code).\n(2) Left-only change with the right builder kept exactly: only partly met. The right panel in the concept is a rebuild at 530x445.3 against a source-inferred 531.6x446.4, the header and nav are approximate, and Customize and Review are stand-ins. The real app was not changed, so the real right builder is untouched only because no integration happened.\n(3) Product functionality: the high-desktop.jpg still shows exact-address lookup, the tutor's-choice copy and \"Review first\". Handoff of a selection to the right builder's Apply/Cancel drawer is not demonstrated, and all data is demo data.\n(4) Local resources: the 16 emil-upstream-* skills exist (checked by Glob); the report says 8 of their entrypoints were read, plus emil-design-eng, React Bits source, Taste v2 and two Mobbin stills. Connected Mobbin needs a paid plan.\n(5) Online visual inspiration: not met. Firecrawl and Tavily returned text and search-index results only. No Pinterest, Raycast or cmdk pixels were inspected, and Claude said the references changed nothing.\n(6) Creative ambition: high-desktop.jpg shows a refined, restrained combobox: a slot plate, a charcoal index panel and a serif result card with a red rule. The 3D is hover-only and was not captured, GSAP was not used, and no alternative directions were recorded. The \"wow\" and \"maximum creativity\" ask is not shown by the stills.\n(7) Motion, readability and accessibility: reduced motion is only \"intended\" and natural playback was not checked. The native accessibility tree left out the desktop accessible name, and that is unresolved. No contrast measurement exists.\n(8) Testing and self-critique: the host ran real interactions (exact Enter, Reset, no-results, 320 sheet, Escape and focus return). Claude's scripted checks are its own claim, and no automated review verdict came back.\n(9) \"Show me the updated version\": only two stills and a cloud link that needs a login.\n(10) Integration: not done, and the report says so correctly.\nThree most important corrective actions:\n(a) Export the High page's source and its dependencies into the review folder before the Claude Design sunset banner's December 14 date, and route any further Claude iteration through the headless runner.\n(b) Actually inspect online and 3D visual references at the pixel level, record what carried into the design, and capture the motion and selected states so the user can judge the creative result.\n(c) Resolve the missing accessible name, check reduced motion and contrast, and in any later integration change only left-side files, with a diff showing the right builder untouched.",
  "findings": [
    {
      "id": "RC-HA-01",
      "severity": "high",
      "path": "C:/Users/Joshu/dev/ai-os/design/reviews/rc-passage-search-20261029/ONLINE-REFERENCES.md",
      "evidence": "The user explicitly asked Claude to find visual inspiration from multiple online sources, including Pinterest and 3D work. ONLINE-REFERENCES.md:16-18 says: Raycast was 'Text extraction only… Do not claim its visual palette/motion was studied'; cmdk's 'Canonical demo not visually opened'; Pinterest was 'Search-result text only… actual pixels not inspected'. In :22, the Philip Davis images were 'not opened'. REPORT.md:48 says search image descriptions 'are not host pixel/flow verification'. REPORT.md:58 says Pinterest and Codefronts 'were text or indexed, not inspected online imagery', and Claude said the references 'supported the current capped/groups/steps without further visual change'. Claude was asked to inspect online images, but no record shows which images it actually opened. So the online visual-inspiration requirement is unproven. The only influence recorded is structural, not visual.",
      "fix": "Open and view the actual reference images (specific Pinterest pins with their authors, the live Raycast and cmdk demos, the Davis article images). Record which visual attributes informed which part of the left side. If that can't be done, say plainly in REPORT.md that the online visual-inspiration requirement was not met, rather than calling it satisfied by text search."
    },
    {
      "id": "RC-HA-02",
      "severity": "high",
      "path": "C:/Users/Joshu/dev/ai-os/design/reviews/rc-passage-search-20261029/REPORT.md",
      "evidence": "The High deliverable ('Passage Finder - High.dc.html', REPORT.md:52) exists only in the authenticated Claude Design project. The review folder (Glob) holds only the older 'Passage Picker.dc.html', which the plan says belongs to the previous prototype. The banner in both high-desktop.jpg and high-phone.jpg reads 'Claude Design is moving to Artifacts in the Claude app. You can keep using this version until December 14.' So the only copy of the requested 'updated version' sits on a product route with a stated end date. It can't be reviewed independently or iterated through the headless runner. REPORT.md:36 ('Export saved as Passage Picker.dc.html') sits in the first-pass section and is easily mistaken for the High export.",
      "fix": "Before December 14, export Passage Finder - High.dc.html and the support.js/runtime it depends on into this review folder. Record SHA-256 hashes. Add an explicit line to REPORT.md separating the older Passage Picker export from the High source."
    },
    {
      "id": "RC-HA-03",
      "severity": "medium",
      "path": "C:/Users/Joshu/dev/ai-os/design/reviews/rc-passage-search-20261029/high-desktop.jpg",
      "evidence": "The request asks for 'maximum creativity', a 'wow factor', 3D inspiration, GSAP and to be surprised. high-desktop.jpg shows a polished but conventional pattern: a search field with a Clear button and a PT/S/P slot plate, a charcoal dropdown with a breadcrumb, a Newsreader result card with a red rule, and a mono shortcut footer. Its depth is an ordinary drop shadow. REPORT.md:52 says the motion is 'CSS rolling slot, staggered lift and hover-only restrained perspective', with no GSAP and no React Bits integration. None of that motion was captured. The host's own brief limited the effects ('Do not make result text tilt, blur or wobble', 'Use GSAP only if…', ONLINE-REFERENCES.md:28; 'without expanding product scope', REPORT.md:48), against the user's 'not feel restricted'. No alternative directions are recorded for the High pass, although the request asked for several to be explored.",
      "fix": "Don't let the record imply the brief was met at its most ambitious. Capture the signature motion (rolling slot, lift, perspective) as video or a frame sequence. Record the alternative directions considered and why this one was chosen, and let the user judge the wow factor. Product scope stays unchanged."
    },
    {
      "id": "RC-HA-04",
      "severity": "medium",
      "path": "C:/Users/Joshu/dev/ai-os/design/reviews/rc-passage-search-20261029/REPORT.md",
      "evidence": "The request says to keep the right-side builder exactly as it is. REPORT.md:56 says the right panel was rebuilt from a screenshot and CSS, measures 530x445.3 against 531.6x446.4, is 'NOT pixel-identical', has 'Header/nav approximate', and has Customize and Review as 'stand-ins'. high-phone.jpg's chat pane adds 'Text inside can sit 1 to 2px off'. Comparing the original screenshot with high-desktop.jpg, the controls and copy match, but the concept's right side is a lookalike, not the preserved builder.",
      "fix": "Keep calling the prototype's right panel a reconstruction. For any real delivery, change only the left-side picker component. Prove the right builder is untouched with a source diff limited to left-side files, plus a pixel diff of the right panel at the same viewport."
    },
    {
      "id": "RC-HA-05",
      "severity": "medium",
      "path": "C:/Users/Joshu/dev/ai-os/design/reviews/rc-passage-search-20261029/REPORT.md",
      "evidence": "REPORT.md:54: 'Native AX representation omitted the desktop name despite correct rendered DOM attribute'. This is an observed accessibility symptom, not just an unverified area. A common cause is aria-label placed on a wrapper or an element that can't take a label, instead of the focusable combobox input. The report leaves it unresolved, so the left-side search may have no accessible name for assistive technology.",
      "fix": "Find which element carries the aria-label versus which gets focus and has role=combobox. Move the name, or add a visible label linked with aria-labelledby, onto the focusable control. Re-check the native accessibility tree and record the result."
    },
    {
      "id": "RC-HA-06",
      "severity": "medium",
      "path": "C:/Users/Joshu/dev/ai-os/design/reviews/rc-passage-search-20261029/high-desktop.jpg",
      "evidence": "The request asks for motion, readability and accessibility checks. design/principles.md:25 says 'Inspect natural playback and reduced-motion behavior separately. Settled screenshots do not establish timing quality.' REPORT.md:52 says only 'reduced-motion path intended', and :56 lists natural motion timing as unverified. The desktop still has small low-contrast text: tiny tracked 'PT/S/P' slot labels, grey mono 'Exact address', the footer shortcuts and 'Demo metadata. Titles are fictional.' on charcoal, and grey helper copy on beige. principles.md:70 warns against spreading tiny tracked labels. No contrast measurement is recorded.",
      "fix": "Record natural playback with reduced motion off and on, measure WCAG contrast for the slot labels, footer hints, metadata and helper text on their actual surfaces, and fix any that fail."
    },
    {
      "id": "RC-HA-07",
      "severity": "medium",
      "path": "C:/Users/Joshu/dev/ai-os/design/reviews/rc-passage-search-20261029/REPORT.md",
      "evidence": "Original product contracts (brainstorms/2026-10-20-rc-builder-refinement-interview.md:10,18; REPORT.md:20) say Pick passages opens a draft manual selection, Apply commits mode and picks, Cancel/Escape discards, selected IDs and order persist, and review comes before Start. In the High concept, Customize and Review are stand-ins (REPORT.md:56). The 'Passages: 1' stepper on the right is not shown reacting to a left-side selection. Data is synthetic ('59 PrepTests · 101–159', 'Titles are fictional'). The original's dependent Test → Section → Passage disabled states ('Test first', 'Section first') and 'Clear test' option are matched only by the host's mention that Reset worked.",
      "fix": "Before calling this complete, integrate it against the authoritative RC index. Show that a left-side selection feeds the existing builder's manual-selection draft without changing that builder, and that dependent resets, Clear, exact lookup, Apply/Cancel and review-before-Start all behave as today. Run the app's existing tests and record the results."
    },
    {
      "id": "RC-HA-08",
      "severity": "low",
      "path": "C:/Users/Joshu/dev/ai-os/design/reviews/rc-passage-search-20261029/REPORT.md",
      "evidence": "The later direct clarification (all Claude communication must go through the headless runner, never browser chat) is not recorded in REPORT.md or wiki/log.md:4919-4923. All Claude turns, including feeding the Firecrawl and Tavily references into Claude's final refinement (REPORT.md:58), went through the web Claude Design chat. Without a note, a future session may iterate again in browser chat.",
      "fix": "Add a constraint note to REPORT.md: the past Claude Design route stays as it was, and all future Claude review or build work on this design goes through the claudex runner, working on the exported High source (see RC-HA-02)."
    },
    {
      "id": "RC-HA-09",
      "severity": "low",
      "path": "C:/Users/Joshu/dev/ai-os/design/reviews/rc-passage-search-20261029/REPORT.md",
      "evidence": "REPORT.md:3 says the user requested 'Opus5.5' and drops the 'high' the user specified. REPORT.md:8 and :24 ('Completed in Claude Design with Opus5.5 Medium') are not marked as falling short of the requested effort or as superseded. The High evidence is the host's account (REPORT.md:44) plus a composer selector visible at capture time (high-phone.jpg), not per-turn generation metadata.",
      "fix": "Correct line 3 to Opus 5.5 High. Mark the first pass as Medium, not meeting the requested effort, and superseded. Describe the High evidence as selector state plus the host's observation."
    },
    {
      "id": "RC-HA-10",
      "severity": "low",
      "path": "C:/Users/Joshu/dev/ai-os/design/reviews/rc-passage-search-20261029/high-phone.jpg",
      "evidence": "In the 320 phone sheet the search box is empty, but the slot plate already reads 'PT 101' and cell 101 has a light 'selected'-looking fill. ONLINE-REFERENCES.md:17 asks for the keyboard highlight to be distinct from the chosen state. The still can't tell whether 101 is highlighted or committed.",
      "fix": "Check whether the default focus and highlight writes into the slot plate. Make highlight and committed selection look different (and have a different ARIA state). Capture both states."
    },
    {
      "id": "RC-HA-11",
      "severity": "low",
      "path": "C:/Users/Joshu/dev/ai-os/design/reviews/rc-passage-search-20261029/REPORT.md",
      "evidence": "Only two High stills exist. The desktop still is at 75% zoom with the header scrolled off, and no frame width is labelled. There are no stills of the chosen state, Reset, no-results, title/subject results, or the 768/390 widths, and no before/after pair at a matched viewport. principles.md:76 asks for 'matched, readable desktop and phone renders' and 'a before/after image'. Most of the host's interaction checks (REPORT.md:54) exist only as text.",
      "fix": "Capture labelled stills at matched viewports for the original and the High version: closed, exact match, chosen, no-results, browse sheet. Save them to the review folder and list them in REPORT.md."
    }
  ],
  "coverage": [
    "Read the full original request in Pasted text.txt, including the design task paragraph",
    "Read REPORT.md (all sections, first pass and High revision) and ONLINE-REFERENCES.md",
    "Viewed the pixels of high-desktop.jpg, high-phone.jpg and the original current-app screenshot codex-clipboard-abcab510…png, and compared the right-builder controls and copy",
    "Read design/README.md and design/principles.md, applying the motion, material and verification rules",
    "Used Glob to confirm all 16 emil-upstream-* skill directories exist under .agents/skills",
    "Confirmed the two Firecrawl JSON outputs exist in .firecrawl/",
    "Checked the review folder contents: no High .dc.html export, only the older Passage Picker.dc.html",
    "Traced related records: wiki/log.md:4879-4923 entries and brainstorms/2026-10-20-rc-builder-refinement-interview.md for the Apply/Cancel and Pick passages contracts",
    "Searched for Outfit font usage elsewhere in design/ (it is used in existing app-related reviews, so the font choice is not flagged)"
  ],
  "limitations": [
    "I could not open the High revision source; it is not exported locally, and per instructions I did not substitute the older Passage Picker.dc.html",
    "No browser, shell or network access: no live interaction, motion playback, reduced-motion check, contrast measurement or accessibility-tree inspection. Every interaction result here is the host's or Claude's claim, not my own test",
    "I can't independently confirm which model produced each Claude Design turn. The evidence is the host's account and the selector state in a screenshot",
    "I didn't read the 16 Emil SKILL.md files, the Taste v2, GSAP or React Bits skill bodies, the Mobbin stills, or the full Firecrawl JSON. The resource-audit claims were checked only for directory existence and internal consistency",
    "I didn't view the earlier first-pass screenshots (search-desktop.jpg, phone-drawer.jpg); they belong to the superseded prototype",
    "I didn't locate or inspect the real app source for the RC picker or right builder; the original behavior comes from the current screenshot, REPORT contracts and the 2026-10-20 interview notes",
    "The judgments on creativity and readability come from scaled stills at 75% zoom and in the 320 frame, not actual-size renders"
  ]
}
