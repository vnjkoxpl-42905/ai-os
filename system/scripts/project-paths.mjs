import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

export const vaultRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const sibling = path.join(path.dirname(vaultRoot), 'ai-os-projects');
export const projectsRoot = fs.existsSync(sibling) ? sibling : path.join(vaultRoot, 'projects');
export const projectPath = (...parts) => path.join(projectsRoot, ...parts);
