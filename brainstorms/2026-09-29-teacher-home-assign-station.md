# Teacher Home: access changes and assigning station: Brainstorm / Discovery Notes
Date: 2026-09-29 · Goal: Define (1) changing a current student's access tier from teacher Home and (2) a fast "assigning station" on teacher Home, browsable by topic and difficulty.
Status: in progress
Context sources: `brainstorms/2026-09-27-teacher-command-center.md`; mockup https://claude.ai/artifact/3sQ2ivCXrRMkRaksoq8Suf; `src/data/guidedDrillHtmlManifest.ts` (lsatu).

## Starting request (Joshua, 2026-09-29, paraphrased)
- Change a current student's tier access from Home.
- An assigning station on Home: pick a student, find a guided drill, Activity, or practice test by topic and difficulty level, and assign it fast. Possibly also save notes. Organized by topic (e.g. Conditionals) and level.

## Fact check (code, 2026-09-29)
- ~~108 Guided Drills exist in `guidedDrillHtmlManifest.ts`... No topic or difficulty field exists.~~ **Superseded (Round 1, Joshua corrected; verified):** that manifest is only the HTML file list. The `guided_drills` database table is already categorized per drill: `week` + `order_in_week` (curriculum order), `category` (Process / Pacing), `difficulty_min`/`difficulty_max` (1-5 scale), `question_types` (e.g. Flaw, Necessary Assumption), `question_features` (e.g. Famous Flaws, Missing Links, Explain Curious Fact), `reasoning_types` (Conditional Logic, Causation, Comparisons), and a `level` column (beginner / intermediate / advanced, mapped to difficulty bands in `src/lib/studentLevel.ts`). Assigning already accepts a student level (`src/lib/assignWork.ts`). No re-tagging needed.
- Tier model (from 2026-09-27 capture): Tier 1 all 12 features, Tier 3 Classroom + Messages + Schedule, Tier 2 custom switches; the student dossier already has per-feature toggles.

## Summary / key decisions
- **Student access:** an expandable panel (dropdown / expand) on Home listing current students with their tier, each changeable. Archived students are excluded.
- **Topic and level:** use the existing `guided_drills` categorization; do not re-tag.
- **Station assigns:** guided drills, Activities, practice sections, and whole practice tests.
- **Multiple students per assign:** yes.
- **Notes in the station:** Joshua's private session notes about the student (not a message to the student).
- **Due date:** optional, blank by default.
- **Tiers panel:** separate expandable panel on Home, current students, tier + Change menu.
- **Practice tests:** both whole PrepTest and single timed section.

## Q&A log
### Round 1
#### Q1 - Where the tier control lives
- Recommended: inside the assigning station next to the chosen student.
- Captured: "I should have either a dropdown... have an expand option. And they can change students' tier." Show current students' tiers, excluding "that student" if archived. Read as: an expandable list of current, non-archived students with tier and a change control.
- Tentative: whether this panel is separate from the station or part of it was not stated.
#### Q2/Q3 - Topic list and meaning of level
- Recommended: Claude drafts topics; level = teaching order.
- Captured: "The list I already have, it's categorized... It's already been done." Recommendation superseded. Verified in code (see Fact check).
#### Q4 - Who tags the drills
- Captured: moot; already tagged.
#### Q5 - What the station assigns
- Captured: guided drills, Activities, and "a practice test or a practice section as well." Joshua asked "More notes?"; meaning unclear.
- Flags: what "notes" means here -> Joshua.
#### Q6 - Fields at assign time
- Captured: not answered.
#### Q7 - Several students at once
- Captured: accepted recommendation (yes).

### Round 2
#### Q8 - Browse filters
- Recommended: search + Topic (question type and feature) + Reasoning + Level, sorted by curriculum week.
- Captured: not answered.
#### Q9 - Notes
- Captured: "b": private session notes about that student. Resolves the Q5 flag.
#### Q10 - Due date
- Captured: "a": optional, blank by default. Resolves Q6.
#### Q11 - Tiers panel
- Captured: "a": separate expandable panel on Home.
#### Q12 - Practice tests
- Captured: "both": whole PrepTest and single section.

## Open flags (pending input)
- Browse filters (Q8) -> Joshua.
