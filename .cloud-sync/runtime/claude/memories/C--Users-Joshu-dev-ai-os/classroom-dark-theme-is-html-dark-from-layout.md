---
name: classroom-dark-theme-is-html-dark-from-layout
description: "LSAT U classroom dark palette keys on html.dark, which ClassroomLayout toggles from the theme; ThemeContext only manages .light. Two audits wrongly called the dark rules dead."
metadata:
  type: project
---

In `projects/lsatu`, `ThemeContext.tsx` adds and removes only `.light` on `<html>` (default is light). `ClassroomLayout.tsx` (~line 901) separately toggles `html.dark` from the theme while the classroom is mounted, since commit `0e3dcad` (2026-09-05). `classroom.css` keys its whole dark palette on `html.dark`, so inside the classroom it is live. Outside the classroom (e.g. `/rc`) `html.dark` is never set.

**Why:** RUN3 §7.1 (2026-09-08) declared the 22 dark rules dead and WP-F unshippable; the 2026-09-09 session found the toggle line on `origin/main` and fixed the real, smaller defect (PR #103). The wrong simulation removed `.light` by hand instead of adding `.dark`.

**How to apply:** to test dark inside the classroom, set `localStorage["lsatu-theme"]="dark"` and reload, then confirm `document.documentElement.className === "dark"`. Never judge the classroom's dark rules by reading `ThemeContext` alone. Related: [[in-app-browser-scales-css-widths]], [[branch-per-session-in-lsatu]].
