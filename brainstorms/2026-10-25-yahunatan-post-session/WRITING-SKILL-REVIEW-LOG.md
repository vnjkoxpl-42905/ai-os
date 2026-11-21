# Claude writing and skill audit

Host: Codex. Reviewer: Claude Opus5.5, medium effort, explicitly requested. One initial review, up to one clarification if needed; no implementation/publication authorized by audit alone. Read-only project tools. Brief: WRITING-SKILL-REVIEW-BRIEF.md.

## Completed independent review

Result: C:\Users\Joshu\AppData\Local\Temp\claudex-xdy7yscc\result.json
Requested and observed model: claude-opus-5-5. Requested effort: medium, present in actual CLI arguments. Status completed; verdict REVISE; 15 findings. Full response and host dispositions: WRITING-SKILL-REVIEW.md. Actual source coverage and limits retained. No implementation or publication.

## First final inspection

Result: C:/Users/Joshu/AppData/Local/Temp/claudex-ywcslnb6/result.json

```json
{
  "verdict": "REVISE",
  "summary": "The three current notes are much better than the versions the earlier review (WRITING-SKILL-REVIEW.md) looked at. Most of the 15 findings are fixed in the current files. F1: the Tokyo plain-sentence point and the sufficient-assumption contrast are back in a narrowed form (recap.src.html:53-54). F3: the old-man analogy is back. F4: the credit lines now name the audit question and the New York/US work. F6: the primer checks both ways (primer:21-23). F10: the reference uses contractions. F12: the rule arrow is gone. F13: 'only' is gone from the Maya setup. F14: browser titles now follow the note's role, and '30 sentences' fits the live activity, which calls its items statements. The scoped list of rejected phrases is read from one config file and checked against visible text, titles, aria labels and hidden answers (build_session_manual.py:35-58). Current HTML titles and kickers are clean.\n\nWhat remains, and nothing here is a factual error in the student copy:\n(1) The strength section still ends on three caveat blocks. Its last sentence ('…a guarantee under every imaginable circumstance') is abstract and works against Joshua's 'conceptually strong vs linguistically strong' point. His plainest line, 'the stronger the claim, the less likely it's required', is rewritten into a weaker sentence.\n(2) Two small clarity slips: 'Those aren't the same thing' (left behind by the F12 fix) and 'he' for a generic author.\n(3) The canonical Markdown still runs callout labels and chip lines into one paragraph, so F11's spacing fix is only partial.\n(4) The skill guidance still contradicts itself. lesson-quality-bar.md (all five homes) still asks for a 'Session Manual' kicker, 'step zero' and 'recognition practice'. The Gemini SKILL.md still prescribes a 'Session Manual · <Month day>' kicker and lacks the student-facing names rule, even though the host disposition says it was updated.\n(5) The builder only prints a warning for dashes, '~' and 'establish'; it does not stop the build. It also quietly rewrites 'Session Manual' in recap sources.\n\nShipping: in my judgment the notes are ready for Joshua's review and contain nothing I'd hold posting for. Finding 1 is a worthwhile 2-minute edit before posting, and the other copy items are optional. The skill-file contradiction (4) should be fixed before the next build (Charles), since it sends the next host back to rejected labels.\n\nPriority order:\n(a) Apply the F-A rewrite to recap.src.html:45/51-53. Rebuild, then rerun sync_current.py.\n(b) In all five homes of lesson-quality-bar.md, replace bullets 1-2 with role kickers and plain section descriptions. In .gemini SKILL.md, change the kicker line and add the student-facing names paragraph. Check the out-of-scope skills/gemini mirror too.\n(c) Make the dash/'establish' check raise an error like the phrase check. Drop the silent 'Session Manual' replacement, or lint before replacing.\n(d) Fix label/body separation in sync_current.py.\n\nDon't add new bans. Acceptance check: grep every skill home for 'Session Manual` kicker|step zero|recognition practice|Session Manual ·' and get zero hits outside the historical model and examples. Have a human read the strength section aloud beside transcript 01:03:52-01:12:06. A machine pass does not settle voice.\n\nThis review is not Joshua's approval of the voice.",
  "findings": [
    {
      "id": "F-A-strength-section-still-ends-on-hedges",
      "severity": "medium",
      "path": "brainstorms/2026-10-25-yahunatan-post-session/recap.src.html",
      "evidence": "CURRENT. Transcript 01:03:52: 'the stronger the claim, the less likely it's required to be true'. 01:07:08: 'the golden rule… be petrified of strong answer choices'. 01:10:11: 'conceptually strong and linguistically strong are not always the same thing'.\n\nThe recap's lines:\n- :45 'A stronger claim has more that the author would need to depend on' is vague and drops his plain causal sentence.\n- :45 the analogy lands on 'something the argument needs to keep working' rather than his point, which is that it's boring and conservative. That makes 'That's why correct answers often sound weak' a non sequitur.\n- :51-54: the callout is followed by a caveat paragraph, the Tokyo callout and the sufficient paragraph.\n- The Tokyo callout ends: 'A prediction isn't automatically a requirement or a guarantee under every imaginable circumstance.' A student can't act on that sentence. It reads as the host protecting itself, and it undercuts Joshua's 'point blank → very strong' teaching (01:11:17-01:12:06).\n\nThe section no longer reverses the emphasis, which is real progress over F3. But the last thing the student reads is a hedge, which is the pattern Joshua corrected.",
      "fix": "BEFORE :45 (last three sentences): 'That was our comparison for a necessary assumption: something the argument needs to keep working. That's why correct answers often sound weak… A stronger claim has more that the author would need to depend on.'\nAFTER: 'A necessary assumption is like that: boring, conservative, just enough to keep the argument running. That's why correct answers often sound weak: **some, may, might, at least one.** The stronger the claim, the less likely the argument actually requires it.'\n\nBEFORE :53, last two sentences: 'Read what the answer commits to, then ask whether the author needs that much. A prediction isn't automatically a requirement or a guarantee under every imaginable circumstance.'\nAFTER: 'A word can sound casual and still make a strong claim. If an answer states something flatly, with no probably or may, read it as a firm commitment and ask whether the author needs that much.'\n\nThis keeps 'will' distinct from logical 'must', so it doesn't claim will = must. Optionally merge :52 into the end of the :51 callout so only one caveat line remains. Rebuild and resync the Markdown."
    },
    {
      "id": "F-B-dangling-referent-and-generic-he",
      "severity": "low",
      "path": "brainstorms/2026-10-25-yahunatan-post-session/recap.src.html",
      "evidence": "CURRENT. Removing the rule arrow (the F12 fix) left :35 'Those aren't the same thing. To get from one to the other…'. The preceding sentence (:34) now names only one thing being treated as proof, so 'Those' has no clear pair. :35 also says 'something he never wrote down' about an unnamed author. Neither is a logic error. Both are small reading bumps a student will notice.",
      "fix": "Merge :34-35: 'The author treats no finished block this month as proof that the promise is broken. Those aren't the same thing. A slow start isn't a broken promise unless the job had to show progress within a month. The author never said that.' Use 'the author' or 'they' instead of 'he'."
    },
    {
      "id": "F-C-quality-bar-and-gemini-mirror-still-prescribe-rejected-labels",
      "severity": "medium",
      "path": ".agents/skills/post-session-recap/references/lesson-quality-bar.md",
      "evidence": "CURRENT skill guidance (F2 residual).\n\nlesson-quality-bar.md:7-8 is identical in .agents, .claude, .gemini, skills/claude and skills/codex (and in skills/gemini, which is outside the review scope). It says: 'a dated `Session Manual` kicker' and 'step zero, kind cards…, recognition practice'. SKILL.md:78 and COPY-CORRECTIONS ban both on student surfaces.\n\n.gemini/skills/post-session-recap/SKILL.md:92 says 'Kicker `Session Manual · <Month day>`', and that file has no 'Student-facing names (2026-10-25)' paragraph. The other homes have it at line 78. The host disposition says 'activated .agents/.claude/.gemini … SKILL.md updated: … internal component labels never visible', which is not true for Gemini.\n\nThe builder masks this only partly. recap() replaces 'Session Manual' in recap sources. Lint would reject 'manual' on Markdown pages. Nothing catches the instruction itself before a host drafts from it. Charles is the next build.",
      "fix": "In all homes of lesson-quality-bar.md, replace bullet 1 with: 'A serif title naming the reasoning, a role kicker (Session recap · date, Before you start · drill, Reference), and a lede that says why students stall.' In bullet 2, replace 'step zero' with 'the first thing to do' and 'recognition practice' with 'practice checks'.\n\nIn .gemini SKILL.md (and the skills/gemini mirror), change line 92 to `Session recap · <Month day>` and add the Student-facing names paragraph.\n\nAcceptance check: a grep across all skill homes for 'Session Manual` kicker|step zero, kind|recognition practice|Kicker `Session Manual' returns nothing outside model/examples."
    },
    {
      "id": "F-D-builder-lint-warns-without-failing",
      "severity": "low",
      "path": ".agents/skills/post-session-recap/references/session-manual/build_session_manual.py",
      "evidence": "CURRENT. :59-60: the em/en dash, '~', 'concept lesson' and 'establish' checks only print 'BAD …' and then write the files anyway (:71-72). The phrase list raises an error (:57-58). So 'lint reports ok' (SKILL.md verify step) depends on someone reading stdout. That is the same gap between assurance and coverage that the brief describes.\n\n:13: recap() silently changes 'Session Manual' to 'Session recap'. A source containing the rejected label therefore passes, and source and output diverge.\n\nLow priority: test :39 expects suffix 'Session notes' for a 'Session recap' kicker passed to from_md. That's harmless but inconsistent with the role names.",
      "fix": "Raise ValueError when `bad` is non-empty, matching the phrase check. Add a unit test for an em dash. Remove the silent replace, or lint the raw source before replacing. Map the 'session recap' label to 'Session recap'. Mirror the change to all five builder homes."
    },
    {
      "id": "F-E-canonical-markdown-labels-still-run-together",
      "severity": "low",
      "path": "students/yahunatan-zetvy/recaps/2026-10-20-recap.md",
      "evidence": "CURRENT (F11 partial). The disposition says the spacing was fixed and the private note says 'Canonical conversion inserts separators after labels'. But the callout labels still sit on the line directly above their body: :31-32 'Grant nothing that isn't written' / 'Common sense…', :44-45, :69-70, :74-75. In Markdown these join into one paragraph ('Grant nothing that isn't written Common sense will…'). The four chip lines :117-120 also merge into one paragraph. The posted artifact is the HTML, so students aren't affected. The skill calls this file the primary record of the student-facing text.",
      "fix": "In sync_current.py, put a blank line, or bold the label and end it with a period, after each span.tag. Emit chips as a list ('- All of the guests arrived. Answer: Not all of the guests arrived'). Resync, then spot-check :31, :44, :69, :74 and :117."
    },
    {
      "id": "F-F-homework-iso-dates-in-student-voice",
      "severity": "low",
      "path": "brainstorms/2026-10-25-yahunatan-post-session/recap.src.html",
      "evidence": "CURRENT. :107-111 use 'Monday, 2026-10-26' style dates seven times. The F5 content problems are resolved:\n- the platform wording is gone\n- the confidence rationale from 01:12:06-01:13:09 is present\n- the order is negation first, then First Taste, then recall every other day\n- the bootcamp hold keeps the tentative 'probably assign' (01:13:09)\n- there is no invented Friday check-in\n\nThe dates match the private status table (:161-163). The ISO format is the one remaining piece of system-speak. The host chose to keep absolute dates, which is legitimate. The weekday plus month-day form keeps them absolute.",
      "fix": "Optional: 'Monday, October 26' … 'due Sunday, November 1'. The dates stay absolute and read like a teacher wrote them. Don't use en-dash ranges."
    }
  ],
  "coverage": [
    "Read all of current recap.src.html, primer-negation-station.md and necessary-assumption.md. Grepped the generated recap.html, primer and reference HTML for titles, kickers, lesson markers and the remaining hedge sentence. Current titles are role-correct and the kickers are clean.",
    "Read canonical students/yahunatan-zetvy/recaps/2026-10-20-recap.md lines 1-185: student copy, current status table and current emphasis map. Did not read the superseded history below line 185 in full.",
    "Read the transcript around 01:03:52-01:15:17 (strength, Tokyo, homework) and grep hits for the audit deadline credit (00:27-00:29) and the New York contrapositive (:523-524). Checked the credits and assignment order against them.",
    "Read the prior review findings F1-F15 and the host bounds in WRITING-SKILL-REVIEW.md, and checked each against the current files.",
    "Read build_session_manual.py, student-copy-exclusions.json and test_build_session_manual.py (.agents copy). The manifest hashes show the copies in all five homes are identical.",
    "Reviewed the SKILL.md, lesson-quality-bar.md, recap-calibration.md and transcript-intake diffs. Grepped all post-session-recap homes for rejected kicker/label wording.",
    "Reviewed the COPY-CORRECTIONS.md diff, including the 2026-10-25 entries and table rows.",
    "Checked the live-readback JSON for the Negation Station title and instructions. The activity calls its items statements, so 'sentences' in the primer is acceptable."
  ],
  "limitations": [
    "I could not run the builder, the unit tests, the browser or verify-accuracy.cjs. The host's PASS reports, byte sizes, overflow and console results, and chip keyboard checks were not reproduced.",
    "I did not open screenshots or rendered pages. Judgments about layout and visual fidelity to the Session Manual model are not part of this review.",
    "No live platform reads. Assignment IDs, dates and the 30-item readback are taken from repository files as recorded.",
    "Did not read in full: sync_current.py, verify-accuracy.cjs, accuracy-verification.generated.json, revise_accuracy.py, INVENTORY.md, model HTML, examples, backup folders, WRITING-FIX-INSPECTION.md, WRITING-SKILL-REVIEW-LOG.md, wiki/teaching-voice.md, references/lsat-teaching-voice-standard.md beyond the diff, the humanizer and lsat-u-voice skills, and the gold-standard ContrapositiveNote.",
    "The full host/user chat history is not available. The voice-calibration capture was not reread in this pass.",
    "Out of scope and unreviewed: skills/gemini mirror (seen only via grep), lsat-u-platform-actions, and the posting code paths. This is not a whole-repository approval.",
    "This is an independent editorial and logic review, not Joshua's personal voice approval."
  ]
}
```

Dispositions: F-A/B/C/D/E applied. F-F optional date formatting declined because Joshua’s explicit global instruction requires YYYY-MM-DD dates. All six runtime/catalog homes now verified byte-identical for SKILL.md, quality bar, builder/config/tests. Historical examples marked superseded. Seven builder tests passed independently.

## Final recheck blocked by provider limit; authorized delivery completed

Second fresh inspection result C:/Users/Joshu/AppData/Local/Temp/claudex-21kiwn03/result.json failed. stdout terminal_reason api_error, HTTP429 usage_limit_reached, session limit resets12:10am America/Toronto. No verdict and no claim of final independent approval. Previous completed review said notes contain no factual error warranting holding posting. User explicitly instructed apply findings then assign; host completed authorized delivery after disclosing failed finalrecheck, with finalresidualfixes hostverified and unreviewedbyClaude. No model/providerfallback. Sevenbuildertests and allsixpagewidthchecks passed; allsixskill/catalogfilesmatch.
