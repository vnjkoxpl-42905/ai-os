# Final dashboard concept audit, 2026-10-23

## Judgment

Claude improved the originality and interaction craft of the concepts. That is not the same as improving the everyday dashboard. None of the three should replace the product as-is. The original corrected teacher/student handoff remains the stronger operational foundation: consistent sidebar, direct message list, visible search and assignment actions, restrained surfaces and a compact seven-day calendar. The earlier production teacher page that showed assignments TO the teacher was itself wrong; the new concepts are better than that role-confused page. This audit compares design usefulness against the corrected original handoff, not an authenticated current production account.

Among Claude's directions, Lamplight is the strongest composition to develop, Carrel the most materially crafted, and Marginalia the most editorially distinctive. These are judgments, not automated scores.

## Coverage and evidence

Inspected both original handoff screenshots, all six final full-page desktop screenshots, all three teacher full-page phone screenshots and all three student phone viewport captures. Inspected natural-frame contact sheets for Lamplight student, Carrel teacher and Marginalia student. Read-only source audit covered all six pages, shared sample behavior and verification scripts. A fresh independent headless Edge run loaded every page at 1440x900 and 390x844, creating twelve viewport captures and independent-layout-report.json in this folder. All twelve had zero document overflow and no pageerror events. Independent runtime action checks reproduced Clear from Home unread-count regression in all three student pages. Existing Claude report was inspected, not blindly accepted.

No prototype source was changed. No production account, backend persistence, physical phone, screen reader or frame-rate profiling was tested. Motion contact sheets show transitions and sampled intermediate states, not proof of frame pacing or subjective smoothness. Keyboard/reduced-motion evidence below partly comes from Claude's report and source, rather than independent exhaustive re-execution.

## Six-page design comparison

| Page | What improved | What got worse or remains weak | Judgment versus original handoff |
| --- | --- | --- | --- |
| Lamplight student | Strong primary work focus; clear resume location; memorable light/paper contrast; coherent week-window language. | Hanging lamp and greeting use valuable phone space; messages and practice are much farther down; decorative light can distract from work; the next task preview requires swapping the hero. | Better atmosphere; mixed task usability. Strongest student direction to develop, not yet a replacement. |
| Lamplight teacher | Upcoming session is explicit; people combine message and session context; teacher does teacher work. | Student search, assignment strip and calendar are below the large hero; names differentiated by brightness are harder to scan than a stable row list; message priority and session priority compete. | Better upcoming-session emphasis; worse access to frequent teacher actions than original. |
| Carrel student | Card stack, envelope and date ticket form an unusually coherent physical language; swipe, arrows and count give multiple interaction paths. | Hidden/truncated card titles reduce assignment overview; empty ruled-paper area consumes much of the phone viewport; primary continue action falls below the initial 390x844 viewport; large texture/shadow treatment becomes the dominant identity. | Better craft and playful engagement; weaker immediate overview. |
| Carrel teacher | Diary makes session time understandable; explicit work-order flow; messages have concrete previews; role-safe. | Rolodex exposes one student at a time and animates through others to find a person; letters and selected student's message duplicate information; repeated Open letter/Find in rolodex controls inflate the page; mobile assignment form is very far down. | Most creative teacher prototype; original list/search is faster for managing a roster. |
| Marginalia student | Strong typographic identity and reading-oriented voice; clear blue primary action; collapsed mobile notes reduce length. | Routine tasks are embedded in sentences plus sidenotes, requiring two reading locations; names/actions repeat; long large text uses excessive space; completion state is inconsistent. | Editorial originality improved; everyday scanning and status reliability worse. |
| Marginalia teacher | Student context is useful; alphabetical roster is more scalable than a card carousel; restrained surfaces. | Inbox becomes a paragraph to parse; messages and scheduling cross-reference numbered notes; critical status copy equates reading with replying; assignment action is buried after explanatory text. | Good as an optional daily briefing, weaker as the main operational dashboard. |

## Prioritized functional findings

### P1: Clear from Home clears unread inbox state without reading

All three student pages independently reproduced in headless Edge:
- Lamplight: inbox1 becomes0.
- Carrel: inbox1 becomes0.
- Marginalia: 1 unread becomes nothing new.

This violates the explicit distinction between hiding a Home item and marking a conversation read. Relevant sources:
- C:/Users/Joshu/Downloads/LSAT-U-Dashboard-Three-Directions-v2/lamplight/student.html:232 derives count from msg; :377 nulls msg.
- C:/Users/Joshu/Downloads/LSAT-U-Dashboard-Three-Directions-v2/carrel/student.html:296 derives count from msg; :339 nulls msg.
- C:/Users/Joshu/Downloads/LSAT-U-Dashboard-Three-Directions-v2/marginalia/student.html:155 excludes msgCleared from unread; :268 hides it.

Fix: separate Home visibility from conversation read state. Clearing hides the Home preview; unread stays1 until an actual read action.

### P2: Reading is falsely described as replying

Marginalia teacher says Everyone has had a reply after messages are merely read. Lamplight similarly derives Nobody is waiting on a reply from unread count.
- C:/Users/Joshu/Downloads/LSAT-U-Dashboard-Three-Directions-v2/marginalia/teacher.html:119 and :184.
- C:/Users/Joshu/Downloads/LSAT-U-Dashboard-Three-Directions-v2/lamplight/teacher.html:189.

Fix: say all conversations read unless real sent-response state supports a reply claim. Reading can clear unread without resolving a response task.

### P2: Completed Marginalia notes still appear as active/new

C:/Users/Joshu/Downloads/LSAT-U-Dashboard-Three-Directions-v2/marginalia/student.html:113 filters the waiting count, but :115-118 still direct the learner to completed notes and call the sidenote From Joshua, new.

Fix: remove completed work from active narrative and active notes, retain access in history. This is the same lingering-work class of problem the redesign was intended to solve.

## Cross-direction product issues

- All six replace the established sidebar with a small top navigation. On phones links extend into a horizontally scrolling row with weak discoverability. A larger visual change is legitimate under the brief, but access to destinations must be re-proven rather than assumed improved.
- Large greetings and spatial metaphors crowd out the actionable first viewport. Carrel student is the clearest example: the continuation button is below the initial phone view.
- Calendars remain but are no longer the compact, quick-scanning strip the owner liked. Lamplight uses tall windows, Carrel an expansive diary, Marginalia a vertical contents list. These are creative alternatives; they are not a preservation of the original interaction advantage.
- These are fixed sample-data scenes. A 12-student roster, three messages and two sessions do not demonstrate performance or hierarchy with a full teacher workload, long names, many unread messages or multiple sessions per day.
- The original near-white/ink visual family was more consistent with the rest of the app. Claude was explicitly permitted to explore beyond it, so the palette changes are not a brief violation. They would nevertheless require an intentional broader product decision rather than being pasted onto one route.

## Verification quality

Claude genuinely used headless Edge and natural-time sampled screenshots, consulted research and relevant skills, and iterated on bugs. This was substantive work.

However C:/Users/Joshu/Downloads/LSAT-U-Dashboard-Three-Directions-v2/_verify/verify.js is a recorder, not a strong pass/fail suite:
- No assertions fail the run when stored values are wrong.
- Focus ring line32 accepts :focus-visible as proof a ring is drawn.
- onScreen line33 checks nonzero dimensions, not viewport bounds or occlusion.
- Message checks only click read, missing hide/reply state semantics.
- Reduced-motion checks compare initial desktop frames, not interactive and phone behavior.
- record.js phone-drag flow uses mouse events, not actual touch dispatch.

Thus zero logged errors does not establish complete keyboard, accessibility, touch or state acceptance. Existing report is useful partial evidence.

## Recommendation

Do not publish any as-is. Keep the original dashboard's operational clarity while developing the strongest art direction deliberately. If choosing one creative route, develop Lamplight further because its focal hierarchy is strongest, but compact its phone entrance, make teacher search/messages/assignments immediately reachable and fix the state bugs. Carrel is valuable as a craft exploration; retain select tactile details only if they make the frequent actions easier. Marginalia is better suited to a daily briefing than the sole task dashboard.

The next quality bar is not more ornament or more libraries. It is a distinctive design that still lets a teacher find a student, clear an unread conversation correctly and assign work quickly, and lets a student resume work and trust what remains due.
