# Codex - Software Development

This directory configures Codex for the Software Development specialization.

## Native Surfaces

- `AGENTS.md` makes the primary Codex session the Software Development Lead.
- `.codex/config.toml` is project-scoped, model-neutral, endpoint-neutral, approval-gated, and network-disabled with `[agents].max_depth = 1`.
- `.codex/agents/` contains seven specialist agents; there is intentionally no Lead agent.
- `.agents/skills/` contains static reusable Skills.
- `docs/workflows/` contains auxiliary workflow references, not an auto-loaded workflow engine.

## Safety Model

The primary session plans, routes, requests approvals, aggregates evidence, and reports completion. Specialists return bounded evidence to the primary session, cannot recursively delegate, cannot expand scope, and cannot claim final completion. Planning, architecture, testing, code-quality, engineering-risk, and release-readiness specialists are read-only. The implementation specialist is limited to approval-gated workspace edits and has no network, unrestricted shell, external service, Git mutation, deployment, publication, signing, or release authority.

No hooks, MCP entries, scripts, executable helpers, model/provider pins, endpoint pins, credentials, or user-global paths are included.
