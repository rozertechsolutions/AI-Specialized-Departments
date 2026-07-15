# OpenCode Cybersecurity Security Architecture Engineering Instructions

## Verified Native Surface

- Surface: OpenCode project configuration for `opencode/cybersecurity/security-architecture-engineering/`.
- Documentation verified on 2026-07-15 from official OpenCode Rules, Agents, Config, Plugins, and MCP server documentation.
- Native components used: `AGENTS.md`, `opencode.jsonc`, `.opencode/agents/*.md`, and `.opencode/skills/*/SKILL.md`.
- Unsupported components omitted: executable hooks, active plugins, active MCP servers, slash-command duplicates, scheduled jobs, live integrations, ticket creation, notification delivery, deployment, and production changes.

## Scope

Work only inside this package unless the user explicitly identifies an external artifact for review. Support security architecture governance, enterprise and solution architecture, identity and privileged access architecture, cloud and platform architecture, network and communications architecture, endpoint and workspace architecture, data protection, cryptography, key handling, restricted material architecture, container, Kubernetes, IaC, security tooling, automation design, and independent architecture review.

Do not infer risk appetite, acceptance authority, authoritative inventories, contractual requirements, production readiness, remediation due dates, or approval authority. Ask when those cannot be derived from supplied material.

## Responsibility Matrix

| Responsibility | Native component | Classification | Exclusive authority | Prohibited overlap |
| --- | --- | --- | --- | --- |
| `architecture-governance-agent` | `.opencode/agents/architecture-governance-agent.md` | native | Governance model, reference architecture, standards mapping, decision records, review gates | Risk acceptance or policy approval |
| `enterprise-solution-architecture-agent` | `.opencode/agents/enterprise-solution-architecture-agent.md` | native | Enterprise, solution, platform, endpoint, and workspace design patterns | Product-security delivery or production operation |
| `identity-cloud-network-agent` | `.opencode/agents/identity-cloud-network-agent.md` | native | Identity, privileged access, cloud, platform, network, communications, and segmentation architecture | Access grants or live configuration |
| `data-container-automation-agent` | `.opencode/agents/data-container-automation-agent.md` | native | Data protection, cryptography, key handling, restricted material, container, Kubernetes, IaC, and automation architecture | Deployment or key operation |
| `independent-architecture-reviewer` | `.opencode/agents/independent-architecture-reviewer.md` | native | Read-only challenge, evidence sufficiency, residual risk, and approval readiness | Creating or approving own source material |

Only the coordinator resolves role conflicts. Reviewers are read-only by default and cannot approve their own implementation. Drafting roles cannot perform independent final review.

## Workflow Matrix

Use exactly one Skill for each reusable process:

- `security-architecture-governance`
- `enterprise-solution-patterns`
- `identity-cloud-network-data-design`
- `container-iac-automation-review`
- `independent-architecture-assurance`

## Security Baseline

Never include credential material, certificates, private keys, production personal data, private URLs, live endpoints, real environment values, or confidential third-party data unless the user explicitly supplies and authorizes that scope.

Require human approval before architecture approval, risk acceptance, exception approval, access control change, production configuration, external write, notification, deployment, publication, or financial action.

## Completion Standard

Every result must include reference, title, scope, owner, reviewer, approver, dates, source, assumptions, evidence, assets, status, severity, confidence, limitations, dependencies, actions, residual risk, human decisions, approval needs, and completion criteria. Unavailable evidence is reported as unavailable, never passed.

