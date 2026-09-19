For the complete documentation index, see [llms.txt](https://learn.chatgpt.com/llms.txt). Markdown versions of documentation pages are available by appending
`.md` to the page URL.

## Search the docs

Search docs

### Suggested

responses createreasoning\_effortrealtimeprompt caching

Primary navigation

Search docs

### Suggested

responses createreasoning\_effortrealtimeprompt caching

Overview  Features  Configuration  Developers  Security  Administration  Use Cases  Resources

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocsFeatures

- [Overview](https://learn.chatgpt.com/docs/features)

### Workflows

- [Projects and chats](https://learn.chatgpt.com/docs/projects)
- [Sites](https://learn.chatgpt.com/docs/sites)
- [Visualizations](https://learn.chatgpt.com/docs/visualizations)
- [Scheduled tasks](https://learn.chatgpt.com/docs/automations)
- [Long-running work](https://learn.chatgpt.com/docs/long-running-work)
- [Notifications](https://learn.chatgpt.com/docs/notifications)
- [Pets](https://learn.chatgpt.com/docs/pets)
- [Codex Micro](https://learn.chatgpt.com/docs/features/codex-micro)

### Capabilities

- [Browser](https://learn.chatgpt.com/docs/browser)
- [Computer use](https://learn.chatgpt.com/docs/computer-use)
- [Voice](https://learn.chatgpt.com/docs/features/voice)
- [Plugins](https://learn.chatgpt.com/docs/plugins)
- [Web search](https://learn.chatgpt.com/docs/web-search)
- [Image generation](https://learn.chatgpt.com/docs/image-generation)
- [Image inputs](https://learn.chatgpt.com/docs/image-inputs)
- [Appshots](https://learn.chatgpt.com/docs/appshots)
- [Browser extension](https://learn.chatgpt.com/docs/chrome-extension)
- [Work with files](https://learn.chatgpt.com/docs/artifacts-viewer)

### Reference

- [Commands](https://learn.chatgpt.com/docs/reference/commands)
- [Slash commands](https://learn.chatgpt.com/docs/reference/slash-commands)
- [Settings](https://learn.chatgpt.com/docs/reference/settings)
- [Troubleshooting](https://learn.chatgpt.com/docs/reference/troubleshooting)

[API Dashboard](https://platform.openai.com/login)

[Try ChatGPT](https://chatgpt.com/)

![](https://learn.chatgpt.com/images/codex/surface-icons/chatgpt-app.webp)ChatGPT desktop app

Copy Page

## Overview

Plugins bundle capabilities into reusable workflows in ChatGPT and Codex. They
can include skills and MCP servers. Both products use one universal plugin
directory, so the same public plugins are discoverable from their supported
surfaces.

Plugins work in Chat and Work across ChatGPT on the web, desktop, and mobile,
and in Codex in the ChatGPT desktop app. Codex CLI also has a plugin browser
for Codex environments. The IDE extension doesn’t support plugins.

On mobile, you can use plugins available to your account in Chat or Work.

Plugins marked **Desktop only** require the ChatGPT desktop app. You can discover these plugins on the web,
but you must open the ChatGPT desktop app to install and use them. They aren’t
available on mobile.

Open the **Plugins** tab to browse and install plugins. After installation, you
can use plugins in Chat or Work in ChatGPT, or in Codex. Installed plugins can
add skills and MCP tools to new chats.

Open the **Plugins** tab to browse and install plugins. After installation, you
can use plugins in Chat or Work. A plugin can prompt you to connect an external
service before its tools become available.

In Codex CLI, enter `/plugins` to open the plugin browser. Install a plugin from
a configured marketplace, then start a new session before using its bundled
skills or tools.

### Use plugins from a supported surface

Plugins aren’t available in the IDE extension. To browse and install plugins
for Codex, use the ChatGPT desktop app or Codex CLI.

Extend what ChatGPT and Codex can do, for example:

- Install the Codex Security plugin to scan authorized code and confirm
plausible vulnerability findings.
- Install the Gmail plugin to work with Gmail.
- Install the Google Drive plugin to work across Drive, Docs, Sheets, and
Slides.
- Install the Slack plugin to summarize channels or draft replies.

A plugin can contain one or more of these parts:

- **Skills:** reusable instructions for specific kinds of work. ChatGPT and
Codex can load them when needed so they follow the right steps and use the
right references or helper scripts for a task.
- **MCP servers:** services that connect ChatGPT and Codex to tools and
information in systems such as GitHub, Slack, or Google Drive. They define
tools, enforce authentication, return structured data, and perform actions
against external systems. They can optionally include custom UI.
- **Browser extensions:** browser capabilities that a plugin needs for its
workflow.
- **Hooks:** commands that run at configured lifecycle points in the Codex
runtime, including ChatGPT Work and Codex. Hook scripts must be
available in the execution environment; installing a plugin on the web doesn’t
deploy those scripts. Enterprise admins can deploy required scripts through
mobile device management (MDM). Review and trust plugin hooks before they run.
See [Hooks](https://learn.chatgpt.com/docs/hooks) for setup and managed-hook policies.

You can share plugins by publishing them through a marketplace source, such as a
repo marketplace for a project or team. See [Build plugins](https://developers.openai.com/plugins/build/plugins)
for marketplace setup, packaging, and distribution guidance.

If you are building an integration, start with
[Build an MCP server](https://developers.openai.com/plugins/build/mcp-server).
If the plugin needs custom UI, use the
[optional UI guide](https://developers.openai.com/plugins/build/chatgpt-ui).

## Use and install plugins

### Universal plugin directory

ChatGPT and Codex use the same public plugin catalog. On the web or in the
ChatGPT desktop app, open the **Plugins** tab to browse and install plugins.

PluginsSkills ManageCreate

Make Codex work your way

Curated by OpenAIShared with youCreated by meMore Search plugins

Gmail Draft replies for every email I'm behind on![](https://learn.chatgpt.com/images/codex/icons/computer-use-plugin-icon.png)Computer UsePlay a playlist to help me lock in

Try in chat

Featured

![](https://learn.chatgpt.com/images/codex/icons/computer-use-plugin-icon.png)Computer UseControl Mac apps from Codex

![](https://learn.chatgpt.com/images/codex/icons/chrome-production-large.png)ChromeControl Chrome with Codex

![](https://learn.chatgpt.com/images/codex/icons/file-spreadsheet.svg)SpreadsheetsCreate and edit spreadsheet files

![](https://learn.chatgpt.com/images/codex/icons/file-presentation.svg)PresentationsCreate and edit presentations

Coding

![](https://raw.githubusercontent.com/openai/plugins/main/plugins/hugging-face/assets/logo.png)Hugging FaceInspect models, datasets, Spaces, and apps

![](https://raw.githubusercontent.com/openai/plugins/main/plugins/netlify/assets/app-icon.png)NetlifyDeploy projects and manage releases

![](https://learn.chatgpt.com/images/codex/icons/vercel.svg)VercelBuild and deploy web apps and agents

![](https://learn.chatgpt.com/images/codex/icons/plugin-game-studio.svg)Game StudioDesign, prototype, and ship browser games

![](https://learn.chatgpt.com/images/codex/icons/plugin-superpowers.svg)SuperpowersPlanning, TDD, debugging, and delivery

GitHubTriage PRs, issues, CI, and publish flows

![](https://learn.chatgpt.com/images/codex/icons/plugin-circleci.svg)CircleCIBuild, test, and deploy any application

![](https://raw.githubusercontent.com/openai/plugins/main/plugins/cloudflare/assets/cloudflare.png)CloudflareCloudflare platform guidance and workflows

The Plugins Directory organizes plugins into tabs:

- **OpenAI:** plugins built by OpenAI.
- **Your workspace name:** plugins provided by your workspace.
- **Personal:** personal marketplace plugins, including **Created by me** and
**Shared with me** sections when those plugins are available.

Use the separate **Installed** row to review plugins you already installed.

Workspace admins can import and sync a GitHub marketplace for their team. See
[Plugin management](https://learn.chatgpt.com/docs/enterprise/plugin-management) for setup and access
requirements.

### Install and use a plugin

Once you open the Plugins Directory:

1. Search or browse for a plugin, then open its details.
2. Select the plus button to install the plugin.
3. If the plugin needs an MCP server connection, connect it when prompted. Some plugins
ask you to authenticate during install. Others wait until the first time you
use them.
4. After installation, start a new chat and ask ChatGPT or Codex to use the
plugin.

### Connect supported partners with Sign in with ChatGPT

**Sign in with ChatGPT** is rolling out in beta for supported plugins and
partner sites, including Airtable, GitLab, HubSpot, Notion, Supabase, and
Vercel. When the option is available, select **Sign in with ChatGPT** while
connecting the plugin to create or link your account with that service.

Signing in shares only your name, email address, and profile picture, when
available, with the partner. It doesn’t grant the plugin access to your data or
approve actions automatically. Review and approve the plugin’s requested
permissions as a separate step before using the connection.

After you install a plugin, you can use it directly in the prompt window:

GitHubaddress the latest comments on my PR and summarize changes

5.6 SolExtra High![](https://learn.chatgpt.com/images/codex/icons/app-mic.svg)![](https://learn.chatgpt.com/images/codex/icons/arrow-up.svg)

LocalDefault permissionsmain

Describe the task directly

Ask for the outcome you want, such as “Summarize unread Gmail threads
from today” or “Pull the latest launch notes from Google Drive.”

Use this when you want ChatGPT to choose the right installed tools for the
task.

Choose a specific plugin

Type `@` to invoke the plugin or one of its bundled skills
explicitly.

Use this when you want to be specific about which plugin or skill ChatGPT
should use. See [Skills & Plugins](https://learn.chatgpt.com/docs/skills-and-plugins).

### Use Apple Messages from Codex

The Apple Messages plugin is available on all plans in the ChatGPT desktop app
for macOS. In Codex and ChatGPT Work, it can read and search iMessage, SMS, and
RCS chats on your Mac and send messages on your behalf through the Messages app.
It doesn’t let you interact with ChatGPT remotely through Messages, and it
doesn’t work in regular ChatGPT chats.

For this release, the Messages plugin is included only in the Apple Silicon
(arm64) build of the ChatGPT desktop app.

1. Open **Plugins**, find the Apple Messages plugin, and install it.
2. Start a new Codex or ChatGPT Work chat and ask it to find, summarize, draft,
or send a message.
3. Grant the requested macOS permissions before ChatGPT reads Messages.
4. Review the message and its recipients before allowing a send.

By default, ChatGPT sends messages only after you approve the message and its
recipients. Choose **Allow once** to approve only that send. If you select
**Always allow sending to this chat**, ChatGPT can send future messages to that
Messages chat without another send approval.

Keep per-send approval for chats that may contain untrusted or misleading
instructions. Persistent approval removes your final chance to review a message
before ChatGPT sends it as you. Use it only when you accept that risk.

To restore per-send approval, open **Settings** \> **Computer use** and select
**Manage** next to **Messages**. Under **Always allowed to send**, select the
trash icon next to the chat, then confirm **Remove**. ChatGPT will ask
before sending to that chat again.

**Known issue:** If your task is set to **Full access** or otherwise disables
approval prompts, Apple Messages may be unable to show the confirmation needed
to send. Switch to **Ask for approval** or **Approve for me** and try again.

Apple Messages runs on your Mac. It isn’t directly available in ChatGPT on the
web or mobile, Codex CLI, or the IDE extension.

In managed workspaces, administrators can disable Apple Messages through the
existing Computer Use control.

### Plugin browser in Codex CLI

In Codex CLI, run the following command to open the plugin browser:

```
codex
/plugins


```

>\_OpenAI Codex(v0.117.0-alpha.15)

model:5.6 Sol medium5.6 Sol xhigh/modelto change

directory:~/code/OpenAIDevelopers/openai

Tip:New Try theCodex App with 2x rate limits until April 2nd. Run 'codex app' or visit https://chatgpt.com/codex?app-landing-page=true

Plugins

Browse plugins from available marketplaces.

Installed 119 of 29 available plugins.

Type to search plugins

›CanvaInstalledPress Enter to view plugin details.

FigmaInstalled· Codex official · Design-to-code workflows powered by the Figma integration

GitHubInstalled· Codex official · Triage PRs, issues, CI, and publish flows

GmailInstalled· Codex official · Read and manage Gmail

Google CalendarInstalled· Codex official · Manage Google Calendar events and schedules

Google DriveInstalled· Codex official · Work across Drive, Docs, Sheets, and Slides

LinearSentryInstalled· Codex official · Find and reference issues and projects.· Codex official · Inspect recent Sentry issues and events

NotionSlackInstalled· Codex official · Notion workflows for specs, research, meetings, and knowledge capture· Codex official · Read and manage Slack

Press esc to close.

The CLI plugin browser groups plugins by marketplace. Use the marketplace tabs
to switch sources, open a plugin to inspect details, install or uninstall
marketplace entries, and press `Space` on an installed plugin to turn it
on or off.

### API key availability

If you [sign in to Codex with an OpenAI API\\
key](https://learn.chatgpt.com/docs/auth#sign-in-with-an-api-key), you can browse, install, and manage
supported OpenAI-curated plugins in Codex CLI and Codex in the ChatGPT desktop
app. Some plugins aren’t available with API key authentication because their
connection flows require unsupported OAuth capabilities. Review plugin usage
on the [Platform Usage page](https://platform.openai.com/usage).

### How permissions and data sharing work

In ChatGPT on the web, Chat and Work use the workspace permissions and tools
available to that chat. MCP servers still require their own sign-in and access.

When a plugin capability runs through a Codex host, the host’s [sandbox and\\
approval policy](https://learn.chatgpt.com/docs/agent-approvals-security) applies.
Connections to external services use that service’s own authentication and
access controls.

- Bundled skills become available when you start a new chat or CLI session
after installation.
- If a plugin includes MCP servers, they may require extra setup or
authentication before you can use them.
- When ChatGPT sends data through an MCP server, that service’s terms and privacy
policy apply.

### Remove a plugin

To remove a plugin, open it from a supported plugin browser and select
**Uninstall plugin** when that action is available. Workspace-installed or
default plugins may not offer that action; your workspace administrator controls
them instead.

Uninstalling a plugin removes the plugin bundle from that ChatGPT or Codex
environment. Separately connected MCP server integrations remain connected in
ChatGPT until you disconnect them there.

## Build your own plugin

If you want to create, test, or distribute your own plugin, see
[Build plugins](https://developers.openai.com/plugins/build/plugins). That page covers local scaffolding,
manual marketplace setup, workspace sharing, plugin manifests, and packaging
guidance.

If your plugin includes server-backed capabilities, see
[Build an MCP server](https://developers.openai.com/plugins/build/mcp-server).
MCP tools can work without custom UI or return UI when a visual surface helps
the workflow.

When your plugin is ready for review, see
[Submit plugins](https://developers.openai.com/plugins/deploy/submission) for the OpenAI Platform submission
flow, required permissions, review materials, MCP checks, and test case
requirements.

## Plugin guides

- [Record & Replay](https://learn.chatgpt.com/docs/extend/record-and-replay): Show ChatGPT a workflow
once and turn it into a reusable skill.
- [Codex Security plugin](https://learn.chatgpt.com/docs/security/plugin): Scan authorized code,
confirm findings, and prepare reviewed fixes.

Ask AI

Loading docs agent...