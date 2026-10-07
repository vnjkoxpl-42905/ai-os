---
name: 7sage-analytics-are-student-supplied-urls
description: 7Sage student analytics come from student-sent /u/usr_.../review URLs and need Joshua's logged-in session to read.
metadata:
  type: reference
---

Joshua pulls student analytics from 7Sage. There is no API and no tutor dashboard in play.

**How the data is addressed:** each student has a stable 7Sage user id, and every page
hangs off `https://7sage.com/u/usr_XXXXXXXX`. The analytics page is `/review`.

**How he gets the id:** he asks the student to log in, open analytics, and email him the
URL. A mailbox sweep on 2026-09-09 found 17 such URLs.

**The access wall:** an anonymous fetch of a `/review` URL returns 200 but redirects to
`7sage.com/subscribe`. Reading real numbers requires his signed-in 7Sage browser session,
so use Claude in Chrome (his real Chrome, already logged in), not curl or Firecrawl.

**Where it lives:** every folder under `students/` has a `7sage.md` holding the id, the
URL, and an empty Snapshot table plus a Pull log. The map is
`wiki/SEVENSAGE-ANALYTICS-INDEX.md`.

**How to apply:** when he says "pull updated 7Sage analytics", read the index, open the
`/review` URLs in his authenticated Chrome, and fill each Snapshot table and Pull log.
See [[ore-and-yahunatan-identities]] for name resolution.
