import base from 'C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-final-release-20261021/vitest.config.ts';
import { execFileSync } from 'node:child_process';
const repo = 'C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-final-release-20261021';
base.plugins.unshift({
  name: 'read-only-baseline-home', enforce: 'pre',
  load(id) {
    if (id.replaceAll('\\', '/').endsWith('/src/components/classroom/home/ClassroomHomeView.tsx')) {
      return execFileSync('git', ['show', 'c0fe7c8b8343946339d34e202e395259ff6f76ca:src/components/classroom/home/ClassroomHomeView.tsx'], { cwd: repo, encoding: 'utf8' });
    }
  },
});
export default base;
