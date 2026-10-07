# launchd definitions

These seven plists are installed in the brain repository only. They are intentionally **not copied to `~/Library/LaunchAgents` and not loaded** until Phase 8. Their common entrypoint also exits successfully without work while `system/.phase8-done` is absent.

Phase 8 must copy/load them inside its journaled transaction after runtime cutover and rollback preparation.

