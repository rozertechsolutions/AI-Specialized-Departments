# Mistral Vibe Data and AI Instructions

## Scope
These instructions apply to work performed from `mistral-vibe/data-ai/` in a trusted Vibe folder. Use the Vibe-native `.vibe` agents, prompts, Skills, permissions, and hooks in this package for Data and AI work.

## Operating Rules
- Use `data-ai-orchestrator` for intake, decomposition, routing, dependency tracking, evidence aggregation, and status.
- Delegate independent specialist review to the smallest applicable subagent.
- Keep final assurance separate from builders and specialist implementers.
- Completion status must be exactly `PASS`, `FAIL`, or `BLOCKED`.
- Treat missing evidence, unsupported platform behavior, unavailable official documentation, or unsafe permissions as `BLOCKED`.

## Safety and Governance
- Never expose or copy sensitive datasets, secrets, credentials, private endpoints, proprietary prompts, personal data, or production records.
- Never fabricate data quality results, statistical significance, causal claims, model metrics, benchmarks, latency, cost, robustness, fairness, compliance status, or readiness evidence.
- Require provenance and permitted-use evidence for data, models, prompts, embeddings, libraries, and third-party components.
- Require human review for high-impact decisions and any external, destructive, irreversible, expensive, publishing, deployment, signing, submission, credentialed, or production action.
- Do not configure providers, models, profiles, API keys, telemetry choices, ACP installation, MCP servers, connectors, or active external integrations by default.

## Separation of Duties
- Builders may test their own work but cannot provide independent final approval.
- Data, ML, and GenAI engineers cannot certify their own quality, risk, or release readiness.
- The orchestrator cannot silently override a specialist, risk owner, human reviewer, or assurance gate.
- Responsible AI/model risk defines and reviews controls; independent assurance verifies controls and evidence.

## Tooling Boundaries
The default package permits only read/search/delegation tools. Write-capable tools, shell, MCP, and connector tools are disabled by configuration and denied by the local hook guard.
