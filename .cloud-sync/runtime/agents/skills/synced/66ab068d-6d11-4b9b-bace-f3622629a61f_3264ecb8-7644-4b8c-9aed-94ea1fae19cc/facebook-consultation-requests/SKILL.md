---
name: facebook-consultation-requests
description: >-
  Joshua's Facebook Messenger assistant for LSAT tutoring service requests. Use this whenever Joshua says
  "run facebook requests", "run messenger requests", "check my facebook messages", or asks to find people
  messaging him about tutoring on Facebook/Messenger and reply to them, even if he doesn't name the skill.
  Trigger on any request to pull unread Messenger conversations, find requests for his LSAT services on
  Facebook, or draft replies to prospects who messaged him there. Reads Messenger through the Codex in
  Chrome browser tools, finds genuine service inquiries, and drafts the consultation reply in Joshua's voice.
  It types the reply into the chat but never sends without Joshua's explicit approval.
---


## Local execution contract (2026-10-10)

Discover the actual supported signed-in Messenger browser surface, not a renamed Claude-in-Chrome tool or assumed Work-profile login. Preserve exact prospect thread. Typing a reply is not proof of persistent draft or absence of send; verify composer/thread state. Send only authorized content and read back/log one copy.

## Workflow

# Facebook Consultation Requests

Joshua gets LSAT tutoring inquiries through Facebook Messenger, not just email. This skill finds the real service requests among his conversations and drafts the same consultation reply he'd send by hand, using the browser (Facebook has no data connector, so this runs through Codex in Chrome on his logged-in Chrome).

Read `references/messenger-consultation-script.md` before drafting.

## Access

Facebook Messenger is a JavaScript app, so plain text extraction only returns the open thread. Use the Codex in Chrome tools: navigate to Messenger, screenshot the conversation list, and read individual threads by opening them. Joshua's Chrome (Work profile) is already logged in.

## Where requests live (check all three)

New inquiries do not reliably land in one place:
- **Unread** tab (left rail) — but this often holds stale system items (missed calls, "you're now friends"), so read the actual latest message, don't assume unread means a new inquiry.
- **Message requests** (the "..." menu next to Chats → Message requests → "You may know") — where strangers' first messages go.
- **Spam** tab within Message requests — legitimate inquiries sometimes get filtered here; skip obvious group-chat noise.

## What counts as a service request

A genuine request is an individual person asking about LSAT tutoring, rates, availability, booking, or help with their score/prep. Skip: group chats, system notifications, "left the group", friend-add notices, and people Joshua is already actively working with (unless they're asking to book again).

## The workflow

1. Open Messenger via Chrome and screenshot the Unread list. Then check Message requests and Spam.
2. For each conversation that looks like a real inquiry, open it and read the person's message so the reply addresses what they actually said.
3. Read `references/messenger-consultation-script.md` and write the reply in Joshua's voice, personalized to their message (mirror their score, timeline, or goal if mentioned). Keep it warm and short, the way he writes.
4. **Type the reply into the message box, but do NOT press Enter/Send.** On Messenger, text left in the composer is effectively the draft. This is the safety gate.
5. Screenshot it and show Joshua the drafted reply for that person. Ask him to approve.
6. Only after he approves, send it (press Enter or click Send). If he wants changes, clear the box, retype, and ask again. Handle one conversation at a time unless he says "all".

Never send a Messenger reply without Joshua's explicit approval, and never message a group chat or someone who isn't clearly a prospect.

## Why it works this way

These messages go to real prospects and personalization matters, so the approval gate is the whole point. Facebook has no API for personal messages, so the browser is the only route, and typing-without-sending is the cleanest way to stage a reviewable draft in a chat app that has no real draft state.
