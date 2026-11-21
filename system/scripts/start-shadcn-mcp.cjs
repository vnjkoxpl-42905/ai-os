// Pin the MCP CLI and set its real process cwd; shadcn 4.22.1 MCP ignores --cwd in registry handlers.
const { spawn } = require("node:child_process");
const child = spawn(process.env.ComSpec || "cmd.exe", ["/d", "/s", "/c", "npx -y shadcn@4.22.1 mcp"], {
  cwd: "C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022",
  stdio: "inherit",
  windowsHide: true,
});
child.on("error", (error) => { console.error(error.message); process.exitCode = 1; });
child.on("exit", (code) => { process.exitCode = code ?? 1; });
