# Windsurf - Software Development

This directory implements the Software Development specialization for Windsurf Cascade using native repository-scoped rules, Skills, and workflows. The primary Cascade session is the Software Development Lead through `AGENTS.md`; there are no custom-agent files, hooks, MCP configuration, shell helpers, auto-run configuration, background jobs, or external integrations.

## Native content

- `AGENTS.md` defines primary Cascade Lead behavior.
- `.windsurf/rules/` contains always-on rule files using the native metadata format already present in this package.
- `.windsurf/skills/` contains fourteen reusable, non-executable Skills.
- `.windsurf/workflows/` contains eleven differentiated workflow references.

## Safety model

The package is guidance-only and contains no executable automation, credentials, endpoints, provider/model pins, deployment assets, release automation, or automatic authentication. Cascade must stop for human approval before editing sensitive scope, changing architecture or dependencies, running commands, accessing external systems, deploying, publishing, signing, releasing, or performing destructive operations.

## Operating model

The primary Cascade Lead confirms scope, routes responsibility stages, separates implementation from independent review, triggers engineering-risk review when needed, and aggregates final evidence. Implementation, code-quality review, engineering-risk review, and release-readiness assessment remain distinct.
