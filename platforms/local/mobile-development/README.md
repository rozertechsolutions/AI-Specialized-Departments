# Local Mobile Development

This specialization defines a local, model/runtime-independent configuration for mobile development work across Android, iOS, Kotlin Multiplatform, Flutter, and React Native.

It is a project-defined specification, not a runtime, daemon, API server, installer, provider client, model downloader, or autonomous loop. Provider and MCP examples are disabled by default and require explicit human configuration before use.

## Native Components

- `local.yaml`: specialization entry point, discovery rules, precedence, lifecycle, routing, and capability negotiation.
- `agents/` and `subagents/`: coordinator and twelve specialist role manifests.
- `skills/`: reusable domain capabilities for mobile technologies, architecture, tests, release readiness, security, performance, accessibility, and independent code review.
- `workflows/`: ten named orchestration processes.
- `hooks/`: standard-library Python guard contracts and tests.
- `tools/`: least-privilege tool contract manifests only.
- `policies/`: permissions, security, approvals, data handling, and model routing.
- `mcp/`: disabled MCP server example and lifecycle documentation.
- `providers/`: disabled provider examples for local and OpenAI-compatible runtimes.
- `schemas/`: JSON Schemas for manifest validation.

## Unsupported Components

This specialization omits unsupported behavior rather than simulating it:

- No universal adapter, shared cross-platform runtime, or `common/` directory.
- No active MCP server, provider connection, model selection, endpoint, port, credential, hardware limit, or context-size assumption.
- No signing, publishing, submission, upload, deployment, destructive device operation, or spending action.
- No final-review authority for implementation roles.

## Use

1. Open this directory as the local specialization root.
2. Validate manifests against `schemas/` before use.
3. Enable providers or MCP servers only through explicit human review.
4. Run hook tests with `python3 -m unittest discover -s hooks/tests`.

Cross-file references such as `tools/project-read.yaml`, subagent IDs, and skill IDs must be checked by the host after schema validation; JSON Schema only verifies local field shape.

Any unavailable project infrastructure must be reported as unavailable, never treated as passed.
