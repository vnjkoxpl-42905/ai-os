#!/bin/sh
cd /home/user/ai-os/corpus/lr-explanations/work/2026-10-08-cloud/gap && python3 -I -c "import sys;sys.path.insert(0,\".\");exec(open(\"$1\").read())"
