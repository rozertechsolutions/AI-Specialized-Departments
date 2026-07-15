# Codex Security Architecture and Engineering Instructions

## Scope

Work only inside `codex/cybersecurity/security-architecture-engineering/` unless the user explicitly provides external static artifacts. This area owns security architecture decisions, control-design specifications, reusable engineering patterns, and validation criteria. It does not deploy, configure, operate, approve, or close production security controls.

## Native Surface

- `AGENTS.md`: durable project instructions.
- `.codex/config.toml`: conservative project configuration.
- `.codex/agents/*.toml`: read-only custom agents for specialist architecture ownership.

## Owners

- `architecture-governance-agent`: principles, decision records, reference architecture governance, gates, escalation, drift, conflicts, duplicated controls, and unsupported assumptions.
- `enterprise-solution-architecture-agent`: system context, trust boundaries, data flows, dependencies, deployment model, operations, failure modes, control placement, findings, requirements, residual risks, and remediation roadmap.
- `identity-cloud-network-agent`: identity, privileged access, cloud, platform, network, secure communications, endpoint trust, logging, guardrails, and handoff criteria.
- `data-container-automation-agent`: data protection, cryptography, key and certificate lifecycle, container, Kubernetes, IaC, security-tool integration, automation boundaries, rollback, observability, and failure behavior.
- `independent-architecture-reviewer`: read-only challenge for traceability, threat coverage, control sufficiency, resilience, assumptions, residual risk, self-review, circular validation, and unverifiable requirements.

## Required Workflows

Use the owner model above to perform security architecture reviews, maintain reference security architectures, design identity and privileged-access architecture, review cloud/platform architecture, design network segmentation and secure communications, design data-protection and cryptographic controls, review container/Kubernetes/IaC architecture, create security engineering control patterns, and validate architecture remediation.

## Safety Rules

Do not execute generated artifacts, connect MCP servers, authenticate, scan, probe, deploy, configure controls, change accounts, grant access, generate real protected material, build images, run IaC, operate tools, approve architecture, accept risk, approve exceptions, publish externally, or close findings through self-review.

Separate evidence, fact, inference, assumption, recommendation, and unresolved question. Mark missing, stale, partial, contradictory, or unverifiable evidence. Require independent review for high-impact architecture, identity, cryptography, resilience, automation, and remediation conclusions.
