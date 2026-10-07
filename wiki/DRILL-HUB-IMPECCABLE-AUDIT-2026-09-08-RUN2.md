# Drill hub: impeccable audit and critique, run 2 (2026-09-08)

Second pass after the fixes from [[DRILL-HUB-IMPECCABLE-AUDIT-2026-09-08]] shipped (commits 211d982, 1d1d351, f4cf062, f791016, published to lsatprep.study). Measured live on production, signed in as Joshua, at 1134px, 1024px and 375px. Messages are out of scope by decision; the assignment list is one shared computation between the hero and Today.

## Audit Health Score

| # | Dimension | Run 1 | Run 2 | Key finding |
|---|---|---|---|---|
| 1 | Accessibility | 1 | 4 | Zero contrast failures, zero targets under 44px, keyboard focus ring on every control, h1 > h2 order |
| 2 | Performance | 3 | 3 | Three backdrop-filter surfaces remain, all over photographs; no layout animation left |
| 3 | Responsive | 2 | 3 | No overflow at 375px; the fixed menu button still floats over content once you scroll on a phone |
| 4 | Theming | 2 | 3 | Every colour resolves from a token; 206 `!important` and the theme-toggle gap remain as recorded debt |
| 5 | Anti-patterns | 2 | 3 | Carousel gone, shadows quiet, one pill per card; the serif-over-photo lane is still recognisable |
| **Total** | **10/20** | **16/20** | **Good** |

### Verified on production

- Contrast scan of every text node in the hub: 0 failures (run 1: 8, including 1.07:1).
- Interactive elements under 44px: 0 (run 1: 15).
- Tab reaches the Start button with a solid ivory outline; `:focus-visible` matches.
- Headings: h1 greeting, h2 console, h2 Your practice, h2 Also today.
- Em-dashes in rendered text: 0.
- 375px: document width 375, zero elements past the right edge, jump row starts at 72px, below the menu button.
- Today card 228px tall beside a 474px practice card, no longer stretched.
- Insight actions: 1 pill, 2 text links.

### Remaining findings

**[P2] Fixed menu button rides over content on phones.** It is clear at the top of the page but floats over "Your practice" once scrolled. Classroom-wide behaviour, not the hub's; the fix is a top bar that scrolls with the page or a bottom placement. `$impeccable adapt`, classroom shell.

**[P2] Glass on three surfaces.** Console, Today primary, Today rails. All sit over photographs, which the surface brief allows. Worth one more look at whether the rails need blur or just a tint.

**[P3] At 1024px the date wraps to two lines** ("TUESDAY · SEPTEMBER 8 / 2026") because the greeting column is 356px wide. Let the label shrink to the short month at that width.

**[P3] `!important` count unchanged.** The observatory overrides shadcn by force. Recorded in the brief.

**[P3] The hub ignores the dark toggle.** Recorded in the brief as acceptable while the stage is documented cream.

## Design Health Score

| # | Heuristic | Run 1 | Run 2 | Note |
|---|---|---|---|---|
| 1 | Visibility of system status | 3 | 4 | Next up with status on one line; loading skeleton holds the CTA's place |
| 2 | Match system / real world | 3 | 3 | "Smart Drill" still an adjective; kept as the product's name |
| 3 | User control and freedom | 3 | 3 | Unchanged |
| 4 | Consistency and standards | 1 | 3 | Jump row tone fixed, date matches Home, one focus treatment; three families remain by brief |
| 5 | Error prevention | 3 | 3 | Launcher error now has a reload action |
| 6 | Recognition rather than recall | 3 | 4 | All insights visible at once, nothing hidden behind a timer |
| 7 | Flexibility and efficiency | 3 | 3 | Shortcut still works, no longer advertised |
| 8 | Aesthetic and minimalist design | 2 | 3 | One door, one pill, hero leaves during a stage |
| 9 | Error recovery | 2 | 3 | Reload button in the launcher |
| 10 | Help and documentation | 2 | 2 | Nothing explains the adaptive drill beyond one sentence |
| **Total** | **25/40** | **31/40** | |

### Anti-patterns verdict

Pass, with one honest caveat. The page no longer has the tells that made it fail: no carousel, no hero-metric block, no side-stripes, no three-equal-pills column, no orphaned chip word, shadows at 12 to 16 percent. What remains is the lane itself: a serif greeting over a planet photograph with mono micro-labels. It is well executed and now documented as this room's identity, but a design director would still name the family. Changing that is a rebrand of the hub, not a fix, and it is not recommended.

### Overall impression

The page now does the one thing PRODUCT.md asks for: it says what to do. A client sees their assignment and one button before anything else, on every viewport. The utilities row reads as one strip. The practice card reads as a record, not a menu. The work left is polish and classroom-shell debt, not structure.

### Persona check

- **Celia (client, assigned work waiting):** first thing on screen is her assignment with Start. On her phone the same, one screen. Pass.
- **Alex (keyboard):** Tab order reaches the jump row, search, switch, Start, the alternative link, the console, all with visible rings. Pass.
- **Jordan (first session, phone):** menu button clear at the top; the hero's two options are one button and one link, not two buttons. Pass, with the scrolled-menu-button caveat.

### Minor observations

- The Today rails truncate long titles ("Conditional Logic: the Cheat Sh…"); the full title is in the hero, so acceptable.
- "Start a Smart Drill instead" underline is faint (0.35 alpha) on the photo. Legible, but a 0.5 alpha would read more clearly as a link.
- The console paragraph on a 375px phone runs five lines. A shorter phone variant would tighten the hero.

## Recommended actions

1. `$impeccable adapt` (classroom shell): the fixed menu button on phones.
2. `$impeccable polish`: date label at 1024px, link underline alpha, phone console copy.
3. `$impeccable quieter`: decide whether the Today rails need blur.
