# Claude Code Security Architecture and Engineering

## Scope

Work only inside `claude-code/cybersecurity/security-architecture-engineering/` unless the user explicitly identifies external static artifacts for review. This area designs, reviews, documents, and governs secure technical architectures and reusable security engineering patterns.

## Native Components

- `.claude/agents/*.md`: project subagents for architecture ownership domains.
- `.claude/skills/*/SKILL.md`: reusable architecture workflows.
- `CLAUDE.md`: project instructions.
- `reference/NATIVE_SOURCES.md`: official documentation checked during creation.

## Responsibility Matrix

| Owner | Exclusive scope |
| --- | --- |
| `architecture-governance-agent` | Principles, decision records, reference architecture governance, review gates, escalation, conflicts, duplicated controls, unsupported assumptions, and architecture drift. |
| `enterprise-solution-architecture-agent` | System context, trust boundaries, data flows, dependencies, deployment model, failure modes, control placement, findings, requirements, residual risk, and remediation roadmap. |
| `identity-cloud-network-agent` | Identity, privileged access, cloud, platform, network segmentation, secure communications, endpoint trust, logging, guardrails, and handoff criteria. |
| `data-container-automation-agent` | Data protection, cryptography, key and certificate lifecycle, container, Kubernetes, IaC, control integration, automation boundaries, rollback, observability, and failure behavior. |
| `independent-architecture-reviewer` | Read-only challenge of traceability, threat coverage, control sufficiency, resilience, assumptions, residual risk, self-review, circular validation, and unverifiable requirements. |

## Rules

- Do not deploy, configure, scan, probe, authenticate, connect, operate controls, create accounts, change access, generate real protected material, build images, run IaC, or execute automation.
- Do not approve architecture, risk, exceptions, production change, release, legal position, privacy decision, supplier decision, funding, or closure.
- Separate evidence, fact, inference, assumption, recommendation, and unresolved question.
- Require independent review for high-impact architecture, cryptography, identity, resilience, automation, and remediation conclusions.
- Route final approval, exceptions, production changes, and closure to humans.
