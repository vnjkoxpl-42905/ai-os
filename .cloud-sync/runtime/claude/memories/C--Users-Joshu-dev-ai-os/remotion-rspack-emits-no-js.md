---
name: remotion-rspack-emits-no-js
description: Remotion's rspack bundler silently emits zero JS on this machine; the ENOENT bundle.js error is a decoy.
metadata:
  type: project
---

In a Remotion project on this Windows box, `Config.setRspack(true)` (which
`create-video` writes by default when you accept Tailwind) makes `remotion
bundle` print "Bundling 100%", exit 0, and emit **no JavaScript** — `build/`
contains only `index.html` and `favicon.ico`.

Every later command then fails with `ENOENT: no such file or directory, open
'...bundle.js'`. That error is a decoy: it is Remotion's source-map reader
failing to symbolicate the real error, not the real error. Chasing it leads
nowhere.

**Fix:** comment out `Config.setRspack(true)` in `remotion.config.ts` and let it
use webpack. Verified 2026-09-09 by rendering MyComp to a real 60-frame MP4.

Second gotcha in the same setup: npm here blocks install scripts, so
`esbuild`'s postinstall never runs. Fix with `npm approve-scripts esbuild`.

Project lives at `dev/ai-os/projects/video`. See
[[video-generation-stack]] and [[lsatu-content-lives-in-postgres]].
