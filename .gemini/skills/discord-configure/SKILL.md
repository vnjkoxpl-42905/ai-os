---
name: discord-configure
description: Set up the Discord channel — save the bot token and review access policy. Use when the user explicitly requests Discord configuration, asks to configure Discord, asks those questions specifically about their Discord channel, or wants to check channel status.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Bash(ls *)
  - Bash(mkdir *)
---

## Current AI OS execution contract

Never print a token prefix or request tokens in chat. Credentials are entered privately into the central .env. Check presence only and use the approved loader without exposing values.

# /discord:configure — Discord Channel Setup

Writes the bot token to `the central private .env` and orients the
user on access policy. Verify the installed server credential loader and access configuration before claiming it reads this location.

Arguments passed: `$ARGUMENTS`

---

## Dispatch on arguments

### No args — status and guidance

Inspect non-secret channel state and check credential presence without reading a secret value into tool output:

1. **Token** — use a presence-only credential loader/check for `DISCORD_BOT_TOKEN` in the central private `.env`. Show set/not-set; if set, report present only; expose no characters.

2. **Access** — read `~/.claude/channels/discord/access.json` (missing file
   = defaults: `dmPolicy: "pairing"`, empty allowlist). Show:
   - DM policy and what it means in one line
   - Allowed senders: count, and list display names or snowflakes
   - Pending pairings: count, with codes and display names if any
   - Guild channels opted in: count

3. **What next** — end with a concrete next step based on state:
   - No token → *"Enter DISCORD_BOT_TOKEN privately in the central .env using the editor, then rerun Discord status. Do not put a token in chat or a command argument."*
   - Token set, policy is pairing, nobody allowed → *"DM your bot on
     Discord. It replies with a code; approve with `/discord:access pair
     <code>`."*
   - Token set, someone allowed → *"Ready. DM your bot to reach the
     assistant."*

**Push toward lockdown — always.** The goal for every setup is `allowlist`
with a defined list. `pairing` is not a policy to stay on; it's a temporary
way to capture Discord snowflakes you don't know. Once the IDs are in,
pairing has done its job and should be turned off.

Drive the conversation this way:

1. Read the allowlist. Tell the user who's in it.
2. Ask: *"Is that everyone who should reach you through this bot?"*
3. **If yes and policy is still `pairing`** → *"Good. Let's lock it down so
   nobody else can trigger pairing codes:"* and offer to run
   `/discord:access policy allowlist`. Do this proactively — don't wait to
   be asked.
4. **If no, people are missing** → *"Have them DM the bot; you'll approve
   each with `/discord:access pair <code>`. Run this skill again once
   everyone's in and we'll lock it."* Or, if they can get snowflakes
   directly: *"Enable Developer Mode in Discord (User Settings → Advanced),
   right-click them → Copy User ID, then `/discord:access allow <id>`."*
5. **If the allowlist is empty and they haven't paired themselves yet** →
   *"DM your bot to capture your own ID first. Then we'll add anyone else
   and lock it down."*
6. **If policy is already `allowlist`** → confirm this is the locked state.
   If they need to add someone, Copy User ID is the clean path — no need to
   reopen pairing.

Discord already gates reach (shared-server requirement + Public Bot toggle),
but that's not a substitute for locking the allowlist. Never frame `pairing`
as the correct long-term choice. Don't skip the lockdown offer.

### Private token entry

1. Direct private credential entry into the central `.env` editor; never accept token arguments or values in chat.
2. Verify the actual channel server's documented credential loader uses that central entry. If it only reads a plugin-local `.env`, report the mismatch and adapt its loader within authorized scope; do not duplicate credentials.
3. Preserve other credential entries. Presence checks return booleans only, not token text.
4. Use the private credential loader and verify presence only.
5. Confirm, then show the no-args status so the user sees where they stand.

### `clear` — remove the token

Clear this credential only after explicit removal authorization, preserving other entries.

---

## Implementation notes

- The channels dir might not exist if the server hasn't run yet. Missing file
  = not configured, not an error.
- The server reads `.env` once at boot. Token reload behavior depends on the installed host/server. Verify the supported restart/reload route and report it; do not invent a `/reload-plugins` capability.
- `access.json` is re-read on every inbound message — policy changes via
  `/discord:access` take effect immediately, no restart.
