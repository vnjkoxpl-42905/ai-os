import { readFileSync } from "node:fs";
import { validateInteractiveLesson } from "./lsatu-lesson-validate.mjs";
const f = process.argv[2];
if (!f) { console.error("usage: node validate-cli.mjs FILE"); process.exit(2); }
try { const id = validateInteractiveLesson(readFileSync(f, "utf8")); console.log("VALID", id); }
catch (e) { console.error("INVALID", e.message); process.exit(1); }
