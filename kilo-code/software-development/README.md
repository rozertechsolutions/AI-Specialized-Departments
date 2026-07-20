# Kilo Code - Software Development

This directory configures Kilo Code for the Software Development specialization.

## Native Surfaces

- `AGENTS.md` makes the primary Kilo Code agent the Software Development Lead.
- `kilo.jsonc` keeps broad fallback ask, denies Bash and web fetch, and makes edits approval-gated.
- `.kilo/agents/` contains seven specialist subagents; there is intentionally no Lead subagent.
- `.kilo/commands/*.md` contains native prompt-only workflows migrated from the former auxiliary `docs/workflows/` directory.
- `.kilo/skills/` contains static reusable Skills.

## Safety Model

Specialists return bounded evidence to the primary agent, explicitly deny Task to prevent recursive delegation, cannot expand scope, and cannot claim final completion. Reviewers and planners deny edits, Bash, and web. The implementation specialist may request edits but may not use Task, Bash, web, MCP, Git mutation, deployment, publication, signing, or release actions.

No schema URI is declared because no exact official schema URI was verified in this target. Runtime loading and command execution have not been performed from this repository package.
