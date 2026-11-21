# Preserve Bootcamps through the selected browser

The Loophole lecture workflow also supports written interactive drills. This helper captures the observed page, not a lecture transcript or a Joshua adaptation.

Use `loophole-bootcamp-browser-capture.mjs` from the documented CUA REPL with its bound tab. It uses visible question controls and browser DOM reads. It does not inspect application state, authentication, or private APIs.

1. Capture the Bootcamps chapter links from the rendered overview and each chapter's drill links into `inventory.json`.
2. Import the helper and pass the selected tab, Node filesystem module, evidence directory, and one observed drill record. Use `maxQuestions: 4` or fewer per call. Keep calls below the browser execution deadline.
3. The helper saves after every question. Resume the same drill until its captured and resolved counts match its observed total. It tries visible choices in order until the site confirms an answer. This changes account progress and attempt scores. Only use it when the user has authorized working through the drills.
4. Keep transient feedback immediately. Revisiting an answered question can omit the explanatory hint. Preserve any earlier manual capture as supplementary evidence rather than replacing it with the later state.
5. Preserve text, diagram choices, emphasis, observed responses, and informational pages. A zero-choice page containing images requires inspection; do not assume it is informational.
6. Run `python system/scripts/package-loophole-bootcamps.py --finalize` only when all expected drills are captured. It preserves observed images locally and refuses completion for missing questions, unknown answers, or failed image downloads.
7. Refresh the Loophole retrieval index and verify the Bootcamps probe after final packaging. Follow the wiki schema for the source summary, catalog, and ingest log.

The raw JSON preserves original HTML; the portable HTML preserves instructional structure and emphasis with local images. It does not reproduce the site's CSS or promise unseen feedback branches. Gated external LSAT stimuli remain explicit source-access limits.
