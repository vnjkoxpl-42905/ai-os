# Cleanup worked on constraints; recognition errors remain

## Final revised prompts passed the focused same-model checks

The revised prompts were tested against the configured models: receipt `dictation-same-model-cli-response.json` reports `claude-sonnet-5`, and `ai-instructions-same-model-cli-response.json` reports `claude-sonnet-5-5`. Both report `is_error: false`. Each received the same five saved transcripts and four synthetic cases. These remain saved-text CLI tests with a batch wrapper, not audio recognition or a fresh Superwhisper runtime recording.

All four synthetic checks passed in both modes. Questions, negations, approval conditions, Left Alt, thanks/goodbye, uncertainty, and fifty were preserved; exact three-copy sentence loops became one; literal "slash slash" and ambiguous "super square" were retained; no answers, actions, or em dashes appeared.

The original recording `1791950951` now retained "slash slash" in both modes. Original `1791951242` now retained "super square" in both, rather than guessing Superwhisper. Other ambiguous recognition errors still remained. The 1.744-second recording `1791950057` still contained nonsensical world/NFT text: Dictation shortened repetition, while AI Instructions left it essentially unchanged. Recognition hallucinations are not fixed by these cleanup changes.

The agent launched one duplicate AI Instructions replay while the initial same-model process was finishing. Both outputs agreed on the relevant checks. The earlier receipt is preserved as `ai-instructions-same-model-initial-cli-response.json`. This extra call was unnecessary and did not mutate app configuration.

## First pass used Opus and exposed the literal-word issue

On 2026-10-14, the authenticated Claude CLI replayed five saved raw transcripts and three synthetic cases with each compiled prompt: Dictation and AI Instructions. Both calls returned successfully after an initial session-limit failure. Exact receipts, compiled prompts, selected inputs, old outputs, and new outputs are saved beside this report.

The replay model was `claude-opus-5-5`, the CLI default. The configured app models are Sonnet, so these results establish approximate prompt behavior on a different model, not Superwhisper runtime acceptance. No audio was replayed or listened to, and no intended-word reference transcript was established.

All three synthetic cases passed their stated checks in both prompts: questions and negations remained; the approval condition and Left Alt were retained; thanks and goodbye survived; an explicit fifteen-to-fifty correction resolved to fifty; uncertainty survived; an exact three-copy sentence loop reduced to one while retaining the instruction not to publish. No output contained an em dash, an answer to the dictated request, or an executed action.

The saved examples reveal limitations:

- `1791951580`: cleaned the false start before "I don't have to" while retaining the request.
- `1791951422`: retained 871 and question intent but kept the unclear phrase "amount of material works."
- `1791951242`: unclear "red list" and "My placements" remained. Dictation retained "super square"; AI Instructions inferred Superwhisper. Neither output constitutes proof of intended wording.
- `1791950951`: both outputs collapsed "slash slash button" to "slash button." This may erase intentional repeated wording, especially in code or a shortcut name. Recommendation sent to the mode owner: explicitly preserve intentional repeated words and add a slash-slash example.
- `1791950057`: the 1.744-second recording's world/NFT nonsense remained substantially present. Prompt cleanup reduced some repetition but did not repair the recognition hallucination. Deleting all of it without listening to the audio would require guessing.

There is no accuracy percentage here. Old app results are comparisons, not reference truth. The conservative prompts reduce uncontrolled guessing but cannot recover words missing or garbled in raw recognition.
