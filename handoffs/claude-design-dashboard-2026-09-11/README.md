# Claude Design handoff: LSAT U student dashboard

Prepared 2026-09-11. Everything Claude Design needs to redesign `/classroom`, the page a student sees first after logging in.

## What is in this folder

| Path | What it is |
|---|---|
| `PROMPT-FOR-CLAUDE-DESIGN.md` | The prompt. Paste it whole into the Claude Design chat. |
| `screenshots/` | Four full-page captures of the current design: light full, light empty, dark full, mobile. 1440px at 2x, straight from the real component with fixture data. |
| `source/dashboard/` | The exact production files for the page. Nothing edited. |
| `source/shell/` | The Classroom shell (left rail, stage, tokens) the page renders inside. |
| `source/tokens/` | App-wide `index.css` tokens and `tailwind.config.ts`. |
| `source/preview-harness/` | The dev harness that rendered the screenshots. Also lives in the repo at `src/dev/classroom-home-preview.html`. |
| `source/TEACHING-VOICE.md` | Copy voice rules for anything student-facing. |
| `inspiration/` | Empty. Drop your inspiration images here before zipping so they travel with the bundle. |
| `claude-design-dashboard-handoff.zip` | Everything above, zipped, ready to upload. Rebuild it after adding inspiration images (see below). |

## How to run this in Claude Design (verified against the help center on 2026-09-11)

Claude Design is at **claude.ai/design**, or in the Claude Desktop sidebar. It is included in your Pro/Max plan and draws from the same usage pool as chat and Claude Code, so a five-prototype run is a heavy session; start it with headroom.

1. **Open Claude Design and create a new project.** Name it "LSAT U dashboard, five prototypes".
2. **Add context before you prompt.** Use the attach control in the chat panel:
   - Upload `claude-design-dashboard-handoff.zip` (or the whole folder). Claude Design reads codebases, images, and documents from uploads.
   - Alternatively, or additionally, link the GitHub repo `vnjkoxpl-42905/lsatu-684d89db` via the GitHub connector, so it can read `src/components/classroom/home/` directly. The zip is enough on its own; the repo link is a bonus.
   - Upload your inspiration images in the same message. Say "inspiration, mood not template" so it does not clone them.
3. **Paste the full contents of `PROMPT-FOR-CLAUDE-DESIGN.md`** as the message. Send.
4. **Let it finish the first pass without steering.** The prompt tells it not to ask questions first. If it stops to ask anyway, reply "make the call and keep going".
5. **Refine.** Chat for structural changes ("show me a denser version of #3"), inline comments on the canvas for targeted ones ("this button, larger"), or edit directly on the canvas for spacing and colour. To branch without losing work: "Save what we have and try a completely different approach."
6. **Hand the winner back to code.** Export → "Handoff to Claude Code" → "Send to local coding agent" produces a bundle with the design intent that Claude Code can implement against the real component. The implementation target is `src/components/classroom/home/ClassroomHomeView.tsx` and `home.css`. Remember: a git push builds a Lovable preview only; the frontend publish is a separate step.

### Optional: register LSAT U as the design system first

If you want every future Claude Design project to inherit LSAT U's tokens automatically, do this once: in Claude Design, lower-left organisation picker → your org → onboarding → upload the repo (or `source/tokens/` + `source/shell/`) as the design system source, review the extracted kit, toggle "Published". For this run it is not required; the prompt carries the tokens.

There is also a Claude Code side of this: `/design-sync` pulls a design system into Claude Code, and the Claude Design MCP server (`claude mcp add --scope user --transport http claude-design https://api.anthropic.com/v1/design/mcp`, then `/design-login`) lets Claude Code create and edit designs directly. Useful for the round trip after you pick a winner.

## Rebuilding the zip after adding inspiration images

From PowerShell:

```powershell
cd C:\Users\Joshu\dev\ai-os\handoffs\claude-design-dashboard-2026-09-11
Remove-Item claude-design-dashboard-handoff.zip -ErrorAction SilentlyContinue
Compress-Archive -Path PROMPT-FOR-CLAUDE-DESIGN.md, README.md, screenshots, source, inspiration -DestinationPath claude-design-dashboard-handoff.zip
```

## Re-shooting the screenshots

The harness is in the repo. Start the dev server and open
`http://localhost:8080/src/dev/classroom-home-preview.html?state=full` (also `?state=empty`, `&theme=dark`). It renders the real `ClassroomHomeView` with fixture data, no login needed. The Playwright script used for the captures is not in the repo; the four states are documented in the prompt.

## Notes on what the screenshots do and do not show

- They show the page column only, not the left rail. The rail needs an authenticated session to render. The prompt describes the rail (336px, grouped nav) so Claude Design can draw it in context.
- The fixture student is "Ada" on Friday 2026-09-11 with one activity due today. Your own admin account view drops the "Assigned to you" card by design, so it is a worse reference than the fixture.
