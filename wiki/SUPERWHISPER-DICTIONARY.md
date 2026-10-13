# Superwhisper dictionary

**Moved 2026-09-11.** The source of truth is now the `superwhisper/` folder at the vault root:
[[../superwhisper/CLAUDE]] explains it; `superwhisper/vocabulary.md`, `superwhisper/replacements.md`,
and `superwhisper/modes/*.md` hold the config; `python superwhisper/sync.py` pushes it into the app.
Research: [[../superwhisper/research/SUPERWHISPER-CUSTOMIZATION-REPORT-2026-09-11]].

This note is kept as the dated history of what was loaded and why.

Running list of what is loaded into Superwhisper on the Windows box. Source of truth is
`%LOCALAPPDATA%\com.superwhisper.app\settings\settings.json`; this note mirrors it so a
new session can see the list without opening the file. Add via Claude ("add X to my
dictionary", "replace X with Y"); the app is restarted after each change. Full transcript
export used for the 2026-09-11 analysis: [SUPERWHISPER-TRANSCRIPTS-2026-09-11](../raw/sources/superwhisper/SUPERWHISPER-TRANSCRIPTS-2026-09-11.md).

## Replacements (heard → wanted)

| Heard | Wanted | Added |
|---|---|---|
| Super Whisperer, SuperWhisperer, Super Whisper, Super Whispert, Superwhisperers | Superwhisper | 2026-09-11 |
| cloud code, CloudCode, Cloud Code | Claude Code | 2026-09-11 |
| cloud, Cloud | Claude | 2026-09-11 (Joshua: "cloud should say claude") |
| Seven Sage, 7-Sage, 7 Sage | 7Sage | 2026-09-11 |
| LSATU | LSAT U | 2026-09-11 |
| Firecall | Firecrawl | 2026-09-11 |
| Heggsfield | Higgsfield | 2026-09-11 |
| AI Grater | AI grader | 2026-09-11 |
| Yohonatan, Yohona Tan, Yohonathan | Yahunatan | 2026-09-11 |
| Oriolua | Ore | 2026-09-11 |
| Steven Kostel | Steven Morris | 2026-09-11 |
| impecable | impeccable | 2026-09-11 |
| anti-consultion | anti-conclusion | 2026-09-11 |

## Vocabulary (words the model should recognise)

Tools: Superwhisper, Claude, Claude Code, Firecrawl, Lovable, Supabase, Postgres, GitHub,
MCP, Gemini, Kling, Higgsfield, Obsidian, Vite, Remotion, Cal.com, 7Sage

LSAT: LSAT, LSAT U, LR, RC, LG, PT, RRC, stimulus, anti-conclusion, guided drill,
Activity, bootcamp, golden standard

Brand: Aspiring Attorneys, Joshua Fisseha

People: Adriana Varea, Amanda, Asia, Avneet Natt, Celia Cutler, Charles Moore, Dakota,
David Salgado, Ethan, Favour, Fernande Charleus, Ivory Johnson, Nicole, Ore, Sofia,
Steven Morris, Vinay Kalva, Whit Wilson, Yahunatan Zetvy, Cameron, Nate Herc

## Open questions (not loaded)

- "call" → "Cal" (Cal.com): too ambiguous, left alone.
- Modes per situation: Joshua wants them; waiting on the list of situations.

## Modes (created 2026-09-11)

Files in `%LOCALAPPDATA%\com.superwhisper.app\modes\`. Switch with Ctrl+Shift+M. Voice model
is S1-Voice (`sv-1`) on all of them.

| Mode | Key | Language model | Use for |
|---|---|---|---|
| Claude Code | claude-code | Claude Sonnet 4.5 (`sw-claude-4p5-sonnet`) | Instructions pasted into Claude Code. Keeps every detail, imperative voice, numbered list when he lists tasks. Never answers the request. |
| Student Email | student-email | Claude Sonnet 4.5 | Finished email in his voice per [[teaching-voice]]. Reads selection + clipboard for context. |
| Lesson Notes | lesson-notes | Claude Sonnet 4.5 | Spoken teaching → structured notes, reasoning preserved. |
| Message | message | S1-Language (`sl-1`) | Texts, Slack, DMs. Light cleanup, fast. |
| Session | session | none | Live tutoring sessions. No auto-paste, raw transcript only. System audio off (Joshua toggles it himself when needed). |
| Super (original) | new-mode | S1-Language | Generic cleanup. Kept as fallback. |
| Default | default | none | Verbatim. |

Model IDs for Sonnet were read from the app binary's built-in catalog, not from the live
picker. If a Sonnet mode errors, open the mode in the app and re-pick the model; the
prompt is unaffected.
- 2026-09-11: `scan.py` added; first scan over 283 recordings found 9 more mis-hearings (firecrawls, firecrowl, fireclaw, cloudcode, two email variants, superwhispero/e), now rules. 87 recordings recovered from the sandbox copy into the real History. `superwhisper` skill created.

- 2026-09-11 (evening): big expansion at Joshua's request. Vocabulary 32 → 654 (all 210 skill names, 31 students/prospects, ~110 LSAT/teaching/vault terms, ~60 tools); replacements 160 → 792 ("slash <skill>" → `/<skill>` for every skill, bare spoken forms for unambiguous ones, casing pins for LSAT question types and tools, student full names, silence-hallucination collapse "thank you thank you thank you" → "thank you"). Script kept as `superwhisper/expand_2026-09-11.py`. Watch the next scan for accuracy drift; the docs warn long vocabularies hurt.
- 2026-09-11 (later): reversed. The 654-entry vocabulary made transcription noticeably worse within the hour. Vocabulary cut to 37 hand-picked terms; the auto-add-targets rule is removed from sync.py, CLAUDE.md, the skill, and memory. Replacements kept (780) minus Favour and single-ordinary-word pins (sofia, dakota, celia, react, codex, gmail, lsat…). Favour removed from all Superwhisper config.
- 2026-09-23: full scan of 1,369 recordings (2026-09-07 to 2026-09-23). Found and fixed a defect introduced 2026-09-12: Superwhisper replacements are substring matches with no word boundaries, so bare acronym rules mangled ordinary words ("click" -> "CLIck" 48x, "you install" -> "yoUInstall", "per capita" -> "per cAPIta"), and `firecraw` matched inside "firecrawl" producing "Firecrawll". 42 unsafe rules deleted, 57 real mis-hearings added (867 total). scan.py patched: section 2 now tests the post-replacement `result` (it was testing the raw transcript, so every rule read as failing), plus new sections 2b (rules firing inside words) and 2c (silence hallucination). Super mode prompt sharpened: hard no-em-dash rule (98 of 806 outputs carried one, none from the raw), silence-artefact drop rule ("Thank you" appeared 710 times in raw), and new glossary entries (Antigravity, AI OS, Lovable Cloud, GPT-6 Astra/Luna/Sol, Cameron, Althea, Kelsey Regis).
- 2026-09-23: Claude Code, Rewrite and Student Email moved from S1-Language to Sonnet 5, on the scan's evidence (over 736 Super-mode recordings Sonnet 5 removed 28% of silence hallucinations and 49% of filler; S1-Language removed 8% and once doubled the hallucination). Super was already on Sonnet 5. Consult Notes, Lesson Notes, Message, Student Message and Vault Note stay on S1-Language: unused since 2026-09-13.
- 2026-09-26: "scale" -> skill added (his own transcripts: 21 uses, nearly all meaning skill), "skill" saved to vocabulary. Glossary and house rules (silence artefacts, no em dash, never answer, no emoji) moved out of the Super mode into `superwhisper/shared.md`; `sync.py` now appends it to all 9 AI modes, so a term added once reaches every mode. Verified: all 9 carry it, Verbatim and Session correctly do not.
- 2026-09-26: built `superwhisper/sw.py` + `dev/tools/bin/sw.cmd` (on PATH), a Windows stand-in for Superwhisper's macOS-only CLI: search, last, stats, add, vocab, rules, export, scan, sync, mode. Re-confirmed the official CLI (release v0.1.0, 2026-06-16) ships a macOS binary only and the Claude Code plugin needs Superwhisper 2.13+ on macOS; Windows is on 1.6.5 and does not answer the `superwhisper://record` deep link.
- 2026-09-26: silence rule moved to the top of every AI mode prompt as `<step_zero>`, because measured over 1,592 dictations the appended version cleaned only 5% (195 recordings heard "Thank you", 186 kept it). It now names every artefact form, says he is alone at a keyboard with no audience, forbids repeating one back more times than it appeared (one S1-Language run looped 19 into 2,346 on 2026-09-11), and returns an empty string when the whole transcript is artefacts. Verified in all 9 AI modes. Re-measure with `sw stats`.
- 2026-10-09: current configuration supersedes the older mode table above. Reduced picker from 11 to five modes: Dictation, AI Instructions, Student Writing, Rewrite, Session Recording. Six retired source files preserved under `superwhisper/modes/archived/`; app JSON preserved. Rewrote prompts for faithful dictation without answers, invented content, forced structures, or changed request modality. Shared rules now preserve intentional thanks/goodbyes and require context for product spelling corrections. Corrected shortcut guidance and sync output: live recording uses `AltLeft`, toggle start/stop, `p2t=false`. Background restart verified one process, 876 replacements, 38 vocabulary entries, all five mode keys accepted. Configuration readback verified; spoken output quality remains untested.
- 2026-10-12: removed 6 archived modes from the app (JSONs moved to modes-archived-2026-10-12); app now loads 5.
