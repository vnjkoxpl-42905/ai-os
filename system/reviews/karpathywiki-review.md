# Karpathy LLM Wiki plugin static review

## Artifact reviewed

- Official-registry repository: `green-dalii/obsidian-llm-wiki`
- Installed release: `1.24.1` (disabled)
- `main.js` SHA-256: `fae49038ce9cadcdd789352ced1084854f4e84884cdea0e3e39205ddfa1a2068`
- `manifest.json` SHA-256: `c53bc2238e147a2b94de29fa9949f0dbd44e334705cdb5e7ab4e811d6434db26`

## Capabilities found

- Makes outbound requests to configurable LLM providers, including OpenAI, Anthropic, Google-compatible endpoints, OpenRouter, DeepSeek, and local Ollama/LM Studio endpoints.
- Handles provider API keys and authorization headers in plugin runtime/settings code.
- Creates and modifies vault notes and writes through the Obsidian vault adapter.
- No `child_process`, process-spawn, or direct Node `fs` import marker was found in the bundled artifact by the static token review.

## Decision

Keep disabled. Enabling requires a separate review of:

1. exact secret storage and redaction behavior;
2. which vault paths can be read and transmitted;
3. whether the write surface can be restricted to generated files/sections;
4. provider selection and explicit data-sharing consent;
5. compatibility with the brain's Tier A exclusion and compare-and-swap rules.

The brain does not depend on this plugin. `community-plugins.json` remains empty.
