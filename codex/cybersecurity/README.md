# Cybersecurity Department for codex

This Cybersecurity department is a professional, adaptable baseline for codex covering governance, architecture, product security, vulnerability management, defensive operations, incident response, authorized offensive validation, and resilience.

Its purpose is to help humans produce evidence-based cybersecurity work products while preserving clear professional ownership, least privilege, independent review, and human authority for consequential decisions.

Possible uses include risk and compliance assessment, security architecture review, threat modeling, secure SDLC review, vulnerability prioritization, detection engineering, incident-response planning, authorized penetration-test planning, resilience exercises, and independent assurance.

## Department overview

The department contains eight Cybersecurity areas under `codex/cybersecurity/<area>/`. Each area is scoped to a distinct professional ownership boundary and is intended for static analysis, planning, review, documentation, and assurance using supplied evidence.

It does not authorize live scanning, exploitation, containment, recovery execution, production changes, publication, external integrations, legal determinations, risk acceptance, or closure decisions. Human owners remain accountable for authorization, approvals, exceptions, risk acceptance, incident declaration or closure, offensive testing authorization, and production action.

## Possible uses

- Risk and compliance assessment using supplied policies, control evidence, and framework mappings.
- Security architecture and engineering review for proposed designs and reference patterns.
- Threat modeling, secure SDLC review, release-readiness support, and supply-chain evidence review.
- Vulnerability prioritization, remediation planning, and hardening governance from provided findings.
- Detection engineering, telemetry coverage review, SOC triage methods, and threat-hunt planning.
- Incident-response readiness, DFIR planning, evidence governance, recovery planning, and lessons learned.
- Authorized offensive assessment planning, rules of engagement review, validation planning, and retest assurance.
- Resilience exercises, ransomware recovery planning, specialized technology review, and independent assurance.

## Platform compatibility

Product surface: OpenAI Codex CLI/IDE project AGENTS.md, .codex/config.toml, subagent configuration, Skills, hooks, and documented permissions.

Validated documentation date: 2026-07-21. Plan, account, workspace, IDE, CLI, SDK, and preview availability vary by vendor release and administrator policy. This package documents static, repository-local or manually importable components only.

## Prerequisites

Codex CLI/IDE with a trusted repository; project-local .codex config ignored until trusted; no provider credentials stored here.

Do not place credentials, tokens, keys, private endpoints, personal data, confidential customer data, or live system access material in this package. Connectors, MCP servers, cloud accounts, scanners, SIEM/EDR/XDR/SOAR tools, ticketing systems, identity providers, and hosted tools are disabled or absent unless a retained native file explicitly documents a human-approved external configuration.

## Installation or import

Keep this tree in the repository and open Codex from codex/cybersecurity/<area>/ for area-local discovery. Do not create project-local profiles; use human-managed user-level profiles outside the repository only.

Use project-local or repository-local setup only. Do not install tools globally from this package, and do not authenticate services merely to import the instructions.

## Working directory and discovery

Codex walks from the working directory to the project root and loads AGENTS.md and trusted .codex layers. Closest AGENTS.md/config wins for overlapping guidance.

When a platform supports upward discovery, the nearest area-level instructions take precedence for that area. When a platform requires manual import, treat each area as an isolated package and do not mix files across areas unless a human explicitly approves a cross-area handoff.

## Area map

- `codex/cybersecurity/governance-risk-compliance-assurance/` - Governance, Risk, Compliance, and Assurance: governance, cyber risk, compliance mapping, policies, assurance, exceptions, and risk-decision support.
- `codex/cybersecurity/security-architecture-engineering/` - Security Architecture and Engineering: security architecture, engineering patterns, identity, network, cloud, data, platform, and control design review.
- `codex/cybersecurity/application-product-devsecops-security/` - Application, Product, and DevSecOps Security: product security, secure SDLC, threat modeling, code/design review, CI/CD, supply chain, PSIRT, and release assurance.
- `codex/cybersecurity/exposure-vulnerability-hardening/` - Exposure, Vulnerability, and Hardening: asset exposure, vulnerability triage, prioritization, hardening, remediation governance, and validation evidence.
- `codex/cybersecurity/defensive-security-operations-detection-intelligence/` - Defensive Security Operations, Detection, and Intelligence: SOC operating model, telemetry, detection engineering, alert triage, hunting, intelligence, and coverage quality.
- `codex/cybersecurity/incident-response-dfir-recovery/` - Incident Response, DFIR, and Recovery: incident planning, evidence governance, DFIR analysis planning, containment planning, recovery coordination, and lessons learned.
- `codex/cybersecurity/offensive-security-authorized-validation/` - Offensive Security and Authorized Validation: explicitly authorized assessment planning, rules of engagement, emulation governance, retest planning, and safety review.
- `codex/cybersecurity/cyber-resilience-specialized-technologies/` - Cyber Resilience and Specialized Technologies: resilience, ransomware recovery planning, specialized technology review, cryptography, critical infrastructure, OT/IoT/cloud edge, and transition assurance.

## Native components

- `governance-risk-compliance-assurance/`: `AGENTS.md`, `.codex/`
- `security-architecture-engineering/`: `AGENTS.md`, `.codex/`
- `application-product-devsecops-security/`: `AGENTS.md`, `.codex/`
- `exposure-vulnerability-hardening/`: `AGENTS.md`, `.codex/`
- `defensive-security-operations-detection-intelligence/`: `AGENTS.md`, `.codex/`
- `incident-response-dfir-recovery/`: `AGENTS.md`, `.codex/`
- `offensive-security-authorized-validation/`: `AGENTS.md`, `.codex/`
- `cyber-resilience-specialized-technologies/`: `AGENTS.md`, `.codex/`

Unsupported native mechanisms are omitted rather than simulated. The package does not include fake MCP servers, live hooks that execute security actions, hosted scanner integrations, cloud deployment automation, or credentials.

## How to use the department

Select the area that owns the requested work, open or import that area according to the platform rules above, and provide authorized scope, exclusions, accountable owner, requester, intended audience, decision needed, evidence inventory, assumptions, constraints, reviewer, and approver role.

Expected outputs are scoped artifacts with evidence tables, assumptions, findings or recommendations separated by evidence state, limitations, confidence, residual risk, required human decisions, and completion criteria. High-impact outputs must be routed to an independent reviewer that did not create the work. Components stop when authorization is missing, sensitive data is unredacted, scope is unclear, a live action is requested, evidence is insufficient for a conclusion, or self-review would occur.

## Permissions and safety

Default behavior is read-only and static. Repository writes, where a platform technically allows them, must stay inside the selected `codex/cybersecurity/<area>/` directory and require an explicit user task to update static artifacts. Shell, network, installation, deployment, scanning, exploitation, recovery execution, remote Git operations, MCP connections, hosted tools, and external connectors are prohibited by default.

AI components cannot self-approve, accept enterprise risk, authorize offensive testing, approve production changes, close incidents, certify compliance, make legal determinations, or conceal residual risk. Human review is mandatory for approvals, exceptions, risk acceptance, release or closure decisions, incident command, offensive authorization, external reporting, and production actions.

## Configuration and customization

Organizations may add policies, frameworks, asset context, risk appetite, service-level targets, tool names, responsible roles, approved integrations, sector requirements, and evidence templates as static files in the relevant area after human review. Keep values organization-neutral in shared packages, redact sensitive information, and document any integration without enabling it by default.

## Validation

Static validation can check file syntax, native paths, frontmatter, JSON/TOML/YAML parsing, prompt references, Skill structure, duplicate or obsolete files, empty artifacts, broken links, and absence of secrets or active integrations. Live system behavior, connector access, model behavior, scanner operation, incident action, recovery, and production integration require a separate authorized environment and were not exercised by this repository package.

## Troubleshooting

- If instructions are ignored, confirm the platform was opened from the documented working directory or the files were manually imported into the correct Project, Skill, agent, or rule location.
- If an agent or Skill is unavailable, verify the platform feature is enabled for the plan/workspace and that the directory name and native filename match the current product documentation.
- If permissions appear broader than intended, inspect platform settings before use and deny shell, network, MCP, connector, deployment, scanner, and remote Git access.
- If paths fail to resolve, use paths relative to the selected area package unless the platform documentation states otherwise.
- If a platform preview feature changes, re-check official documentation and update `codex/cybersecurity/NATIVE_SOURCES.md` before relying on it.

## Removal or uninstall

Remove the imported Project, GPT, Skill, agent, rule, command, workflow, or workspace configuration from the platform UI or delete the selected `codex/cybersecurity/` directory from the repository. Remove any manually uploaded knowledge files from the platform. Do not delete organizational evidence or platform-global settings unless a human owner explicitly authorizes that cleanup.

## Limitations

This package is a static professional baseline. It is not a managed security service, scanner, SIEM, SOAR, EDR/XDR integration, penetration-testing tool, incident-response platform, legal opinion, compliance certification, or production-control system. Platform support and schema details can change, especially for preview agent, Skill, hook, and permission features.

## Security notice

Offensive testing, incident actions, production changes, external integrations, live scans, exploitation, deployment, recovery, publication, and use of sensitive evidence require explicit authorization, validated scope, and human control. Do not use these components to bypass approval, access secrets, contact external systems, or claim live execution without evidence.
