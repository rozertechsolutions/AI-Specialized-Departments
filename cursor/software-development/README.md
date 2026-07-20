# Cursor - Software Development

This directory configures Cursor for the Software Development specialization.

## Native Surfaces

- `AGENTS.md` makes the primary Cursor Agent the Software Development Lead.
- `.cursor/agents/` contains the seven native Cursor project specialist subagents. There is no Lead subagent.
- `.cursor/rules/` contains Cursor project rules.
- `.cursor/skills/` contains static reusable Skills.
- `docs/workflows/` contains auxiliary workflow references, not a guaranteed native workflow engine.

## Project Subagents

The primary Cursor Agent remains the Software Development Lead. It delegates to seven project subagents for requirements/planning, architecture, implementation/maintenance, test/quality, code-quality review, engineering-risk review, and documentation/release readiness. Only the implementation specialist is writable; the other six are read-only. Implementation must be followed by independent review before final evidence aggregation.

## Safety Defaults

No hooks, MCP configuration, shell helpers, automatic approvals, background-agent configuration, credentials, endpoints, deployment automation, publication automation, signing automation, release automation, or automatic authentication are included. Human approval is required for sensitive actions, edits, command execution, external access, Git mutation, deployment, publication, signing, submission, and release.
