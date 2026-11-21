---
type: source
subject: Chase AI's seven Claude design skills
created: 2026-10-21
updated: 2026-10-31
aliases: [Top 7 Claude Design Skills, Chase AI design skills clip]
tags: [ai-workspace, skills, repositories]
sources:
  - ../../raw/sources/clips/top-7-claude-design-skills-chase-ai/Top 7 Claude Design Skills (All Free).md
  - ../../raw/sources/clips/top-7-claude-design-skills-chase-ai/Top 7 Claude Design Skills (All Free) 2.md
evidence: ../../raw/sources/clips/top-7-claude-design-skills-chase-ai/Top 7 Claude Design Skills (All Free).md
sha256: 988210fd0d5c4fa3411ac679d519615ad5e598f5948fa24f3027de348e54454f
contradictions: []
---

# Chase AI's seven design skills

Chase AI's [video, “Top 7 Claude Design Skills (All Free)”](https://www.youtube.com/watch?v=n_iyI-C7WCs) was published 2026-10-21. The Obsidian clip has a partial transcript and no repository links. Its recorded transcript stops mid-sentence at 1:47 although the video is 1:59. `yt-dlp` reported no subtitle tracks. The source archive preserves the clip and pinned repository files reviewed for this intake.

## What the source says

The clip recommends seven items for web design: Taste, Design Lang, React Bits, GSAP skills, Playwright CLI, Impeccable, and an unnamed “transition skill.” It presents Taste and Impeccable as ways to improve visual quality; Design Lang as a way to extract a site's design language; React Bits and GSAP as motion resources; and Playwright CLI as a way to exercise frontend behavior. These are the creator's claims, not independent performance findings.

## Repository check and local result

Checked the actual skill files and licenses at pinned upstream commits. Relevant files are preserved under [repository snapshots](../../raw/sources/clips/top-7-claude-design-skills-chase-ai/repository-snapshots/).

| Clip item | Repo match and existing state | Result |
|---|---|---|
| Taste | `Leonxlnx/taste-skill`; the customized `design-taste-frontend` skill was already in both runtime catalogs and active in Gemini. | Activated the existing Claude and Codex catalog copies. Preserved their custom content. |
| Design Lang | `Manavarya09/design-extract`; `extract-design` was already in both catalogs and user-level skill folders. | Activated the existing copies in Claude and Codex, then synced those already-active user-level copies. Changed prerequisite wording to use `npx` without recommending a global install. No CLI or project dependencies installed. |
| React Bits | The component library is `DavidHDev/react-bits`; the helper is `Philotheephilix/reactbits.dev-skill`. | Added the helper skill to both catalogs and activations. Kept component library source out of the vault. Hardened its fetch script to refuse paths outside the destination, including symlinked parents, and existing-file overwrites. It prints dependency commands; no components or project dependencies were installed. |
| GSAP skills | Official `greensock/gsap-skills`, eight skill entry points. | Added all eight to both catalogs and activations. The upstream skill set is MIT licensed. |
| Playwright CLI | `microsoft/playwright-cli`; it is a CLI rather than another skill from this clip. | Already in both catalogs and active in Claude and Codex. No duplicate installation. |
| Impeccable | `pbakaus/impeccable`; customized local copies were already in both catalogs and active in Gemini. Claude also has a more extensive user-level copy, which remains the version Claude prefers. | Activated the existing Claude and Codex project copies without replacing the user-level customization. |
| “Transition skill” | The clip provides no repository name or URL, and the available transcript is incomplete. | Not identified. Tracked as [AQ-017](../../references/ai-workspace/action-queue.md). No speculative skill installed. |

The source's “all free” framing was not treated as a license grant. The React Bits fetch helper is MIT licensed, while React Bits component code has a separate MIT + Commons Clause license. The helper's catalog metadata and live registry can change; its copy is pinned to the reviewed commit and should be refreshed deliberately.

## Mentions in source

> "Here are seven of the best Claude code skills for web design." (0:00)
> "Number four is GSAP skills." (0:32)
> "And lastly, we have the transition skill." (1:35)

## Revision 2: complete transcript (ingested 2026-10-31)

A second capture of the same video (SHA-256 `aa57b65e401a42719313e80c06cab33f07d7db9b48495c2a8112db450297c288`, archived as [revision 2](../../raw/sources/clips/top-7-claude-design-skills-chase-ai/Top%207%20Claude%20Design%20Skills%20%28All%20Free%29%202.md)) carries the whole transcript to its last sentence at 1:44. The first capture stays the `evidence:` above, because the repository review and the quotes were checked against it; the relationship is recorded in the archive's `PROVENANCE.md`.

- **Qualification retired:** the first capture's cut-off at 1:47 is no longer a coverage gap. Nothing in the complete transcript changes the seven-item list or the repository results above.
- **Corrected hearing:** "slob", "Playright" and "taste scale" in the first capture are "slop", "Playwright" and "taste skill" in the second.
- **Still unidentified:** the closing item is called only "the transition skill", with no repository or URL, so the complete source does not settle AQ-017. That item stays declined; there is nothing new to queue.
- **Added detail (creator's claims):** Playwright CLI runs headlessly and can open many browsers at once to test things like form submissions. Impeccable is described as holding a set of recognized AI-slop patterns it checks builds against. Taste is described as giving the agent an art direction, choosing its own images and running its own browser to check its work.

Other relationships: [design hub sources](../../design/sources.md) lists this page. No other page changes: the existing skill catalog and parity records already cover every identified item.

## Where this is filed

- [AI workspace hub](../../references/ai-workspace/index.md)
- [Skill catalog](../../skills/INDEX.md)
- [Runtime parity record](../../skills/PARITY.md)
- [Original clip and provenance](../../raw/sources/clips/top-7-claude-design-skills-chase-ai/)

## Queue record

- Open: AQ-017 identifies the unnamed transition skill from a fuller source, checks its official repository and license, and then records whether it belongs in this project.

Declined 2026-10-26: AQ-017. The unnamed transition upstream remains unverified, while existing GSAP/React Bits cover current motion needs. Decline chasing/installing an unidentified extra skill. [Implementation record](../../research/2026-10-26-source-implementation/REPORT.md).
