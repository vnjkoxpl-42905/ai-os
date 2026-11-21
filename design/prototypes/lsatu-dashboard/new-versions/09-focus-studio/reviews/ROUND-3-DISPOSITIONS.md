# Implementing the three nonblocking notes

2026-10-25. Joshua explicitly requested implementing the three low-priority notes retained in the approved third review. All three are accepted:

| Finding | Implementation and proof |
|---|---|
| R3-1 | When an open dialog replaces its content, focus the new title or field. Preserve the original external trigger for focus return when closed. Check nested student-to-assignment flow on desktop and phone. |
| R3-2 | Preserve natural whitespace in the Home heading so the document title and route announcement read correctly. Check both strings. |
| R3-3 | Require trimmed decimal digits in the separate reference fields, retaining leading-zero support. Reject hexadecimal, exponent, decimal-point and signed forms without substituting a question. Check valid and invalid cases against the typed-reference contract. |

Round3 approval covers the earlier runtime hashes only. Updated source receives affected browser checks and fresh independent Claude review. Preserve historical verdicts. No production, commit, push or publication authorization is added.
