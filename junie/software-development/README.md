# JetBrains Junie - Software Development

This directory configures JetBrains Junie for the Software Development specialization.

## Stable Surfaces

- `.junie/AGENTS.md` is the authoritative stable instruction surface and makes the main Junie agent the Software Development Lead.
- `.junie/skills/` contains static reusable Skills.
- `.aiignore` protects secrets, credentials, generated outputs, and heavy irrelevant artifacts.
- `docs/workflows/` contains auxiliary workflow references, not a repository workflow engine.

## Intentional Omissions

Early Access custom subagents are intentionally omitted from this stable package. The package also omits simulated agents, hooks, MCP configuration, custom commands, Brave mode configuration, automatic approvals, credentials, endpoints, deployment automation, publication automation, signing automation, and release automation.

Runtime loading and validation execution have not been performed from this repository package.
