# Mistral Vibe Security Architecture Engineering Instructions

These instructions apply only inside `mistral-vibe/cybersecurity/security-architecture-engineering/` and cybersecurity security architecture artifacts intentionally placed below it. Keep work scoped to architecture governance, enterprise and solution design, identity and privileged access design, cloud and platform architecture, network and communications architecture, endpoint and workspace architecture, data protection, cryptography, key handling, restricted material architecture, container, Kubernetes, IaC, reusable security engineering patterns, automation design, and independent architecture review.

Start Vibe with this directory as the working directory so project `.vibe/` configuration, agents, prompts, and Skills are discovered.

## Native Surface

- Vibe Code project configuration: `.vibe/config.toml`.
- User-facing coordinator: `.vibe/agents/security-architecture-coordinator.toml` with `.vibe/prompts/security-architecture-coordinator.md`.
- Delegation-only subagents: `.vibe/agents/*-agent.toml` and `.vibe/agents/independent-architecture-reviewer.toml`.
- Reusable procedures: `.vibe/skills/*/SKILL.md`.
- Official docs checked on July 15, 2026: Vibe mode selection, Work Skills, Code CLI agents, Code CLI configuration, and Code CLI Skills.

## Scope and Boundaries

- Do not configure providers, models, connectors, MCP servers, hooks, scripts, remote sessions, automation schedules, or external tools.
- Do not read, copy, log, expose, or embed secrets, credentials, private keys, customer data, employee data, vulnerability details, restricted design details, or regulator communications unless the user explicitly supplies and authorizes the material for the task.
- Do not approve architecture, accept risk, waive controls, certify compliance, deploy, configure, operate production controls, publish, submit filings, spend money, or perform destructive operations.
- Treat unsupported evidence as unavailable. Never turn missing evidence into a pass.

## Delegation

Use only these project subagents:

- `architecture-governance-agent`
- `enterprise-solution-architecture-agent`
- `identity-cloud-network-agent`
- `data-container-automation-agent`
- `independent-architecture-reviewer`

Assign exactly one primary owner per deliverable. Drafting roles do not perform their own independent final review.

## Completion Standard

Every result must list reference, title, scope, owner, reviewer, approver, dates, sources inspected, assumptions, evidence state, assets, status, severity, confidence, limitations, dependencies, actions, residual risk, human decisions, approval needs, and completion criteria. Formal claims require human approval.

