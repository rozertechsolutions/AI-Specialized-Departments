# Cline - Software Development

This directory configures Cline for the Software Development specialization.

## Native Surfaces

- `.clinerules/` contains project rules for the main Cline session.
- `.cline/skills/` contains static reusable Skills.
- `.cline/workflows/` contains prompt-only workflow references.
- `.clineignore` protects secrets, credentials, generated outputs, and heavy irrelevant artifacts.

## Lead Model

The main Cline session is the Software Development Lead. It starts non-trivial work in Plan mode, requests human approval before Act mode, performs approved edits in Act mode, and then separates implementation evidence from independent code-quality, engineering-risk, and release-readiness review.

Built-in Cline subagents are optional read-only research helpers. They may read, search, list, and use read-only Skills only; they must not edit, use browser tools, use MCP, spawn nested subagents, or claim final completion. This package intentionally does not create `.cline/agents/`.

## Safety Defaults

No hooks, plugins, MCP configuration, Auto Approve/YOLO settings, shell helpers, credentials, endpoints, deployment automation, publication automation, signing automation, release automation, or automatic authentication are included. Human approval is required for edits, commands, browser use, external access, Git mutation, destructive actions, deployment, publication, signing, submission, and release.
