# OpenCode Data and AI Instructions

## Scope
Use these instructions only inside `opencode/data-ai/`. The native OpenCode assets are `opencode.json`, `.opencode/agents/`, `.opencode/skills/`, `.opencode/commands/`, and this `AGENTS.md`.

## Operating Rules
- Start with `data-ai-orchestrator` for intake, decomposition, routing, dependency control, evidence collection, status, and stop conditions.
- Delegate independent review to the smallest applicable specialist.
- Keep final assurance separate from builders and specialist implementers.
- Completion status must be exactly `PASS`, `FAIL`, or `BLOCKED`.
- Treat missing evidence, unsupported platform behavior, unsafe permissions, or absent human approval as `BLOCKED`.

## Safety
- Never expose or copy sensitive datasets, secrets, credentials, private endpoints, proprietary prompts, personal data, or production records.
- Never fabricate data quality results, statistical significance, causal claims, model metrics, benchmarks, latency, cost, robustness, fairness, compliance status, or readiness evidence.
- Require provenance and permitted-use evidence for data, models, prompts, embeddings, libraries, and third-party components.
- Require human review for high-impact decisions and any external, destructive, irreversible, expensive, publishing, deployment, signing, submission, credentialed, or production action.
- Do not configure active MCP servers, custom providers, credentials, share settings, plugins, model downloads, or global OpenCode settings by default.

## Separation
- Builders may test their own work but cannot provide independent final approval.
- Data, ML, and GenAI engineers cannot certify their own quality, risk, or release readiness.
- The orchestrator cannot silently override a specialist, risk owner, human reviewer, or assurance gate.
- Responsible AI/model risk defines and reviews controls; independent assurance verifies controls and evidence.
