// Local stdio bridge. Credentials are read at launch and never stored in MCP config.
import fs from 'node:fs';
import {fileURLToPath} from 'node:url';
import {Client} from 'file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/@modelcontextprotocol/sdk/dist/esm/client/index.js';
import {StreamableHTTPClientTransport} from 'file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/@modelcontextprotocol/sdk/dist/esm/client/streamableHttp.js';
import {Server} from 'file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/@modelcontextprotocol/sdk/dist/esm/server/index.js';
import {StdioServerTransport} from 'file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/@modelcontextprotocol/sdk/dist/esm/server/stdio.js';
import {ListToolsRequestSchema, CallToolRequestSchema} from 'file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/@modelcontextprotocol/sdk/dist/esm/types.js';

const envFile = fileURLToPath(new URL('../../.env', import.meta.url));
const line = fs.readFileSync(envFile, 'utf8').split(/\r?\n/).find(l => /^\s*(?:export\s+)?API_KEY_21ST\s*=/.test(l));
const raw = line?.replace(/^\s*(?:export\s+)?API_KEY_21ST\s*=\s*/, '').trim() ?? '';
const key = /^(['"]).*\1$/.test(raw) ? raw.slice(1,-1) : raw.replace(/\s+#.*$/, '').trim();
if (!key) { console.error('21st MCP: central API_KEY_21ST is missing.'); process.exit(1); }
const remote = new Client({name:'ai-os-21st-bridge',version:'1.0.0'});
try {
  await remote.connect(new StreamableHTTPClientTransport(new URL('https://21st.dev/api/mcp'), {requestInit:{headers:{'x-api-key':key}}}));
} catch { console.error('21st MCP: upstream connection failed.'); process.exit(1); }
const local = new Server({name:'ai-os-21st-bridge',version:'1.0.0'}, {capabilities:{tools:{}}});
local.setRequestHandler(ListToolsRequestSchema, request => remote.listTools(request.params));
local.setRequestHandler(CallToolRequestSchema, async request => {
  try { return await remote.callTool(request.params); }
  catch { return {isError:true,content:[{type:'text',text:'21st upstream request failed. Check provider status and saved authentication.'}]}; }
});
const close = async () => { await remote.close(); await local.close(); };
process.on('SIGINT', () => close().finally(() => process.exit(0)));
process.on('SIGTERM', () => close().finally(() => process.exit(0)));
await local.connect(new StdioServerTransport());
