# Kiro Cybersecurity Security Architecture Engineering Specialization

This directory contains only the Kiro package for Cybersecurity Area 02: Security Architecture Engineering. Work here must stay scoped to security architecture governance, secure design review, reference architectures, IAM/PAM, cloud and platform security, network segmentation, endpoint and workspace security, data protection, cryptography, protected material handling, container, Kubernetes, IaC, automation boundaries, remediation validation, and independent architecture assurance.

## Native Surface

- Target surface: current Kiro IDE and CLI behavior documented on July 15, 2026.
- Project instructions are loaded from this `AGENTS.md`.
- Steering guidance is provided through `.kiro/steering/security-architecture-engineering.md`.
- Custom agents are Kiro CLI JSON agents in `.kiro/agents/`.
- Reusable architecture processes are Kiro Agent Skills in `.kiro/skills/`.
- Hooks, MCP servers, Specs, Powers, executable scripts, and live integrations are intentionally not configured for this static package.

## Scope Rules

- Modify only files under `kiro/cybersecurity/security-architecture-engineering/`.
- Do not create shared cross-platform adapters, runtime abstractions, or common directories for this specialization.
- Do not activate external integrations, authenticate services, import credentials, start servers, publish, deploy, approve risk, approve exceptions, operate controls, or run destructive operations.
- Do not hardcode model versions. Agents inherit the active model unless a future user explicitly requests a supported override.
- Treat genuine restricted material, personal data, private endpoints, certificates, architecture diagrams, and supplier confidential data as protected material.
- Review agents are read-only and must not implement or approve their own recommendations.

## Responsibilities

Use the five project custom agents exactly as defined in `.kiro/agents/`:

- `architecture-governance-agent`
- `enterprise-solution-architecture-agent`
- `identity-cloud-network-agent`
- `data-container-automation-agent`
- `independent-architecture-reviewer`

Implementation roles may prepare designs, reviews, ADRs, patterns, findings, and remediation validation packages. `independent-architecture-reviewer` performs final independent review and never reviews implementation it authored.

## Workflow Selection

Use these project Skills for repeatable work:

- `security-architecture-review`
- `reference-and-control-patterns`
- `identity-cloud-network-data-design`
- `container-iac-automation-review`
- `independent-architecture-assurance`

Do not duplicate these workflows as hooks, Specs, Powers, MCP servers, or executable commands. If a later user requests another Kiro-native surface, migrate only after preserving one authoritative workflow owner.

## Validation Standard

Every completed task must report actual evidence, assumptions, source gaps, human approval needs, and unavailable context. Do not claim architecture approval, risk acceptance, exception approval, production readiness, or control effectiveness without explicit evidence and human approval.
