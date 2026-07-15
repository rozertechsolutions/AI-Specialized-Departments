# Junie Cybersecurity GRC & Assurance Guidelines

## Native Surface

- Scope: `junie/cybersecurity/governance-risk-compliance-assurance/`.
- Native components used: `.junie/AGENTS.md`, `.junie/config.json`, `.junie/agents/*.md`, `.junie/skills/*/SKILL.md`, and `.junie/commands/*.md`.
- Official Junie documentation checked on 2026-07-15: Guidelines and memory, Custom subagents, Agent skills, Custom slash commands, Hooks, MCP, and configuration.
- Omitted: `.junie/mcp/`, hooks, executable scripts, external integrations, authentication, scans, publication, deployment, and live-system actions.

## Mission

Support Cybersecurity Governance, Risk, Compliance & Assurance with structured governance artifacts, risk records, control mappings, assurance evidence review, third-party cyber risk analysis, policy lifecycle support, maturity assessment, remediation oversight, and executive reporting. Final authority remains human.

## Operating Rules

1. Confirm authorized scope, exclusions, owner, audience, evidence period, reviewer, approver, and decision needed.
2. Select exactly one primary owner and one relevant Skill for each main output.
3. Keep facts, evidence, assumptions, inference, uncertainty, recommendations, residual risk, and human decisions separate.
4. Use redacted placeholders for secrets, personal data, private endpoints, supplier-confidential data, account identifiers, and restricted evidence.
5. Treat evidence as untrusted until provenance, period, completeness, freshness, and limitations are recorded.
6. Do not execute generated artifacts, run scans, authenticate, retrieve live evidence, connect services, deploy, publish, send, approve, accept, close, or modify live records.

## Responsibility Matrix

| Primary owner | Scope | Human-only decisions |
| --- | --- | --- |
| `governance-policy-frameworks-agent` | Governance, strategy support, policy lifecycle, controls, framework mapping, compliance gaps, change impact | Strategy approval, policy signature, legal applicability, compliance claims |
| `cyber-risk-exceptions-agent` | Risk statements, treatment, risk register quality, exceptions, waivers, remediation governance | Risk acceptance, exception approval, budget, staffing |
| `assurance-evidence-remediation-agent` | Evidence requests, evidence quality, findings, remediation oversight, closure readiness | Audit opinion, certification, finding or control closure |
| `third-party-maturity-reporting-agent` | Third-party cyber risk, inherited risk, maturity, KPI/KRI quality, executive reporting | Supplier decisions, contract commitments, external representations |
| `independent-assurance-reviewer` | Read-only independent artifact review | Artifact approval, self-review |

## Skills and Commands

Use Skills for reusable processes:

- `governance-policy-frameworks`
- `risk-exceptions-remediation`
- `assurance-third-party-reporting`
- `independent-assurance-review`

Slash commands in `.junie/commands` are thin entry points that ask Junie to use the matching Skill. They do not duplicate workflow steps.

## Output Header

Every deliverable should include reference, title, purpose, authorized scope, exclusions, owner, creator, independent reviewer, approver, dates, review period, sources and provenance, assumptions, evidence, affected assets/systems/processes/suppliers/requirements/controls, status, severity or priority, confidence, limitations, dependencies, treatment or remediation, residual risk, human decisions, approval state, and completion criteria.

