---
name: tutorocean-profile-fill
description: Fill and verify Joshua's TutorOcean tutor profile using vault facts, then stop before uploads, policy agreement, or final submission unless the user explicitly authorizes those actions.
---

# TutorOcean Profile Fill

Use this skill when working in TutorOcean's tutor application or profile flow for Joshua.

## Read first

1. `wiki/knowledge/tutoring-outreach-log.md`
2. `wiki/knowledge/tutoring-profile-facts.md`
3. `wiki/knowledge/tutoring-form-fill-instructions.md`

## Working rules

- Use only confirmed facts from the vault or the user.
- Prefer structured, patient LSAT coaching language.
- Do not invent education dates, credentials, uploads, or years of experience.
- Treat uploads and submission as separate actions that need explicit user confirmation.
- If a save fails, retry once after verifying the field values. If it fails again, stop and report the platform error.

## Defaults

- Email: `contact@aspiringattorneys.com`
- Phone: `613 276 2604`
- Location: `Ottawa, Ontario, Canada`
- Street address: `96 Woodfield Drive`
- Postal code: `K2G 0A3`
- Gender: `Male`
- Rate: `40 USD`
- Subject: `LSAT`
- Levels: `College/University`, `Professional`
- Work experience: `Aspiring Attorneys`, `Founder and CEO`, `May 2018` to `present`

## Profile copy

Use the LSAT story already saved in the vault:

- `138 -> 173`
- the LSAT did not come naturally
- structured and intuitive approach
- teaching for a few years
- helps with stuck-between-two-answers, timing, and inconsistent-plan issues
- LSAT U practice space when the field supports it

## Execution order

1. Fill the confirmed personal information fields.
2. Fill subject, level, rate, and location fields.
3. Fill the bio and verification text with the saved vault copy.
4. Add work experience with the resume-backed facts.
5. Verify the profile state after each save.
6. Stop before education uploads, ID uploads, policy agreement, or application submission unless the user explicitly says to continue.

## Verification standard

After saving, check the page again and confirm the persisted values in the profile view, not just the modal state.
