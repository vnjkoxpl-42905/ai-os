# Saved transcript cleanup replay

This test submits saved `rawResult` text to the authenticated Claude CLI using compiled mode prompts. It does not replay audio through Superwhisper, measure recognition accuracy, establish intended wording, or prove the app's effective runtime prompt. Five recordings are selected from the latest ten available, plus three synthetic cases. Saved old results are comparison material, not an authoritative reference transcript.

Each mode receives one bounded batch. Claude runs in safe mode, without tools or persistent sessions. The batch JSON wrapper is a testing harness instruction added to the system prompt, so this is an approximation of individual dictation cleanup rather than a byte-for-byte Superwhisper request.

The first attempt failed before generating output with HTTP 429 `usage_limit_reached`. Its exact receipt is preserved. A single retry after the reported reset is allowed; a failure is reported explicitly.

Manual checks focus on preserving questions, negation, conditions, numbers, uncertainty, and intentional gratitude, avoiding answers/actions and added em dashes, and reducing exact accidental sentence loops. Genuine recognition errors cannot reliably be repaired without listening to audio. A faithful editor may deliberately retain an ambiguous recognition error that an aggressive editor would guess away.
