---
name: lsat-u-operations
description: Use LSAT U's authenticated MCP tools to look up students, review supported student and assignment records, assign homework, and publish classroom notes.
---

# LSAT U operations

Use this skill whenever Joshua asks to look up or update LSAT U through this plugin. The connected LSAT U MCP server is the source of truth for the data and actions it exposes. Its OAuth login and server-side authorization determine what the signed-in account can access; never ask Joshua to paste an access token or service key.

## Available operations

Use the LSAT U MCP tools for these supported workflows:

- Student self-service: get the signed-in user's profile, homework, and classroom items.
- Admin student lookup: search or list students and resolve the exact student ID before a write.
- Homework catalogue and status: list homework sets and inspect assignment status.
- Supported writes: assign an existing homework set, assign structured passage-map homework, post a Classroom note, or send a Classroom note to a student.

Use `echo` only to check whether the MCP connection responds. It does not verify admin access. If a tool is unavailable or the server denies access, report that plainly; do not claim broader access.

## Read and write carefully

- Retrieve only records relevant to Joshua's request. Do not dump rosters, student histories, or unrelated private data unnecessarily.
- Before a student-specific write, use `find_students` or `list_students` to resolve the intended student. If the result is ambiguous, ask which student.
- For homework assignment, obtain the homework-set ID from `list_homework_sets`, then use the resolved student ID. Report the resulting status and any notification or email result returned by the server.
- Use the structured passage-map tool only when the request supplies the required content and settings. Never invent teaching content or student instructions.
- Draft student-facing text in Joshua's teaching voice. Do not send or publish a student-facing message unless Joshua explicitly asks to send or post it. An explicit send or post request authorizes that specific message only.
- After a write, report the tool's returned result. Do not say an email or notification was delivered unless the server reports that outcome.
- Do not attempt direct database access or use credentials outside this MCP server.

## Limits

The current LSAT U MCP server exposes only the operations listed above. It does not provide a universal admin console or unrestricted database access. Sessions, payments, Gmail, access-setting changes, message inbox history, and other unlisted operations are outside this connection unless LSAT U adds and authorizes corresponding MCP tools.
