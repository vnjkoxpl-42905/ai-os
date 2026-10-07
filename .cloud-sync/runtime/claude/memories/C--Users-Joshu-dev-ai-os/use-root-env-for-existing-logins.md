---
name: Use root env for existing logins
description: Joshua authorizes existing-account sign-in for his requested work and wants credentials retrieved from the AI OS root env before asking him to log in.
type: feedback
---

On 2026-10-02 Joshua explicitly authorized Codex to use his existing account logins for requested work. Retrieve the applicable credentials from `C:/Users/Joshu/dev/ai-os/.env` before asking him to sign in manually. Use the destination's normal sign-in flow. Do not expose values in chat, tool output, notes, memory, or Git. Store only this preference in memory, never passwords or tokens. Existing restrictions on billing, Lovable credits and Claude weekly-reset redemption still apply; login permission does not authorize those actions.

On 2026-10-07 Joshua reiterated that Codex should sign into his LSAT U admin account using stored credentials for authorized app work and use the Codex in-app browser. Do not ask him to log in when the applicable credential is already available.

On 2026-10-07 Joshua supplied and authorized saving his LSAT Lab login. Root .env contains LSATLAB_EMAIL and LSATLAB_PASSWORD. Sign-in was verified in the Codex in-app browser. Retrieve these variables for LSAT Lab instead of asking again; never store their values in memory.
