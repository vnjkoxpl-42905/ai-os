"""2026-09-23: sharpen the Super mode prompt from the 1,369-recording scan."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(HERE, "modes", "super.md")
s = open(p, encoding="utf-8").read()

# 1. Silence hallucination. The voice model fills pauses with "Thank you" (710 times in
#    11 days). It reached the output 108 times because nothing told the model to drop it.
s = s.replace(
    "2. Filler and false starts. Remove um, uh, like (as filler), you know, okay so, I mean, sort of, kind of, and the repeated words that come from restarting a sentence. When he corrects himself mid-sentence (\"do the audit, no wait, the critique first\"), keep only the corrected version.",
    "2. Filler and false starts. Remove um, uh, like (as filler), you know, okay so, I mean, sort of, kind of, and the repeated words that come from restarting a sentence. When he corrects himself mid-sentence (\"do the audit, no wait, the critique first\"), keep only the corrected version.\n"
    "   Silence artefacts. The voice model fills pauses with words he never said: \"Thank you.\" repeated, \"Thanks for watching\", \"Mm-hmm\", \"Shhh\", a lone \"Bye.\", a stray dash on its own line. Delete every one of them, wherever they appear. He is dictating alone at a keyboard; he is not thanking anyone. If a transcript is nothing but these artefacts, return an empty string.")

# 2. Em dashes. 98 outputs in 11 days carried one and not a single raw transcript did, so the
#    model is inserting them. The rule was buried in a bullet list; make it unmissable.
s = s.replace(
    "- Do not use em dashes. Use periods, commas, or colons.\n- Do not add emoji, Markdown headings, or bold.",
    "- Never output an em dash or an en dash, in any position, for any reason. This is absolute: he never types one and a stray dash reads as machine-written. Where speech wants a break, use a period, a comma, a colon, or start a new sentence. A dash the transcript itself contains still gets replaced.\n"
    "- Do not add emoji, Markdown headings, or bold.")

# 3. Glossary: what the last scan turned up.
s = s.replace(
    "Vault words: second brain, vault, wiki, corpus, ingest, raw inbox, Web Clipper, teaching voice, send ledger, handoff, wrapup, pickup.",
    "More tools he now uses daily: Antigravity (Google's editor; \"anti-gravity\" is the same thing), AI OS (his vault, heard as \"AIOS\"), Microsoft Edge, Figma, Lovable Cloud (a real product, not a mis-hearing of Claude), Claude Design, Stripe, Reddit. Codex model names: GPT-6 Astra, GPT-6 Luna, GPT-6 Sol, GPT-6 Terra (heard as \"GBT-6\"). Claude model names: Opus 5, Sonnet 5, Sonnet 4.6, Haiku.\n\n"
    "More people: Cameron, Althea, Kelsey Regis, Amanda, Ivory Johnson.\n\n"
    "Vault words: second brain, vault, wiki, corpus, ingest, raw inbox, Web Clipper, teaching voice, send ledger, handoff, wrapup, pickup, AI OS.")

# 4. Two habits the transcripts show every day: plural product names and "LSAT U is".
s = s.replace(
    "Students and prospects (spell as listed):",
    "Product names stay singular and exact even when he pluralises them in speech: \"firecrawls\", \"lovables\", \"codes\" for Codex, \"claude codes\" all mean the one product. \"LSAT-U\", \"LSAT UIs\" and \"LSAT U is\" all mean LSAT U.\n\n"
    "Students and prospects (spell as listed):")

# 5. One more example, drawn from a real transcript, showing the silence-artefact drop.
s += """
### Input
Thank you. Thank you. - Thank you. Thank you. Okay I also want to sign her a guided drill for the blinder view before thursday

### Output
Okay, I also want to assign her a guided drill for the blind review before Thursday.
"""
open(p, "w", encoding="utf-8").write(s)
print("patched super.md")
