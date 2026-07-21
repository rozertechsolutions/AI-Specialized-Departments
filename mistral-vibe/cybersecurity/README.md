# Cybersecurity Department for mistral-vibe

This Cybersecurity department is a professional, adaptable baseline for mistral-vibe covering governance, architecture, product security, vulnerability management, defensive operations, incident response, authorized offensive validation, and resilience.

Its purpose is to help humans produce evidence-based cybersecurity work products while preserving clear professional ownership, least privilege, independent review, and human authority for consequential decisions.

Possible uses include risk and compliance assessment, security architecture review, threat modeling, secure SDLC review, vulnerability prioritization, detection engineering, incident-response planning, authorized penetration-test planning, resilience exercises, and independent assurance.

## Department overview

The department contains eight Cybersecurity areas under `mistral-vibe/cybersecurity/<area>/`. Each area is scoped to a distinct professional ownership boundary and is intended for static analysis, planning, review, documentation, and assurance using supplied evidence.

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

Product surface: Mistral Vibe Code CLI/VS Code surfaces, project `.vibe/config.toml`, native TOML agent profiles, project and user prompt directories, Skills, tool filters, permissions, hooks configuration, MCP settings, and update/telemetry settings.

Validated documentation date: 2026-07-21. Validated package version: `mistral-vibe==2.21.0`. Plan, account, workspace, IDE, CLI, SDK, and preview availability vary by vendor release and administrator policy. This package documents static, repository-local or manually importable components only.

## Prerequisites

Current Mistral Vibe package/application, trusted project folder, and no credentials/connectors/MCP/hooks enabled by default. CLI use requires the user or organization to configure an approved model/provider separately. Repository validation does not run Vibe, authenticate, or call a model.

Do not place credentials, tokens, keys, private endpoints, personal data, confidential customer data, or live system access material in this package. Connectors, MCP servers, cloud accounts, scanners, SIEM/EDR/XDR/SOAR tools, ticketing systems, identity providers, and hosted tools are disabled or absent unless a retained native file explicitly documents a human-approved external configuration.

## Installation or import

Open Vibe from `mistral-vibe/cybersecurity/<area>/` as the trusted project root. Vibe discovers the area's `.vibe/config.toml`, `.vibe/agents/*.toml`, project prompt directory, and Skills when the area is the working directory or a trusted project root.

Example safe launch:

```text
cd mistral-vibe/cybersecurity/governance-risk-compliance-assurance
VIBE_HOME="$PWD/.vibe" vibe --agent grc-coordinator
```

`VIBE_HOME="$PWD/.vibe"` is optional only when the project prompt directory is trusted and discovered as intended. It is the repository-local option for resolving config-adjacent user-home files without mutating `~/.vibe`. Do not copy prompts or settings into the user's real home during repository remediation.

Markdown agent profiles are obsolete; retained agents are TOML files under `.vibe/agents/`.

Use project-local or repository-local setup only. Do not install tools globally from this package, and do not authenticate services merely to import the instructions.

## Working directory and discovery

Mistral Vibe 2.21.0 resolves prompt IDs from discovered project prompt directories and from the user Vibe home prompt directory. The package source also honors `VIBE_HOME`, which normally defaults to `~/.vibe`; setting `VIBE_HOME="$PWD/.vibe"` while launched from an area keeps prompts, config-adjacent files, agents, and Skills repository-local for validation or manual use.

Each retained `.vibe/agents/*.toml` has a `system_prompt_id` whose matching prompt file remains in that area. Unreferenced workflow-like prompt copies and exact duplicate prompt pairs were removed; reusable procedures live in `.vibe/skills/*/SKILL.md`.

Default agents and delegation-only subagents remain area-local. Subagents cannot ask user questions; user-question tools are available only to primary agents where the config allows them.

When a platform supports upward discovery, the nearest area-level instructions take precedence for that area. When a platform requires manual import, treat each area as an isolated package and do not mix files across areas unless a human explicitly approves a cross-area handoff.

## Area map

- `mistral-vibe/cybersecurity/governance-risk-compliance-assurance/` - Governance, Risk, Compliance, and Assurance: governance, cyber risk, compliance mapping, policies, assurance, exceptions, and risk-decision support.
- `mistral-vibe/cybersecurity/security-architecture-engineering/` - Security Architecture and Engineering: security architecture, engineering patterns, identity, network, cloud, data, platform, and control design review.
- `mistral-vibe/cybersecurity/application-product-devsecops-security/` - Application, Product, and DevSecOps Security: product security, secure SDLC, threat modeling, code/design review, CI/CD, supply chain, PSIRT, and release assurance.
- `mistral-vibe/cybersecurity/exposure-vulnerability-hardening/` - Exposure, Vulnerability, and Hardening: asset exposure, vulnerability triage, prioritization, hardening, remediation governance, and validation evidence.
- `mistral-vibe/cybersecurity/defensive-security-operations-detection-intelligence/` - Defensive Security Operations, Detection, and Intelligence: SOC operating model, telemetry, detection engineering, alert triage, hunting, intelligence, and coverage quality.
- `mistral-vibe/cybersecurity/incident-response-dfir-recovery/` - Incident Response, DFIR, and Recovery: incident planning, evidence governance, DFIR analysis planning, containment planning, recovery coordination, and lessons learned.
- `mistral-vibe/cybersecurity/offensive-security-authorized-validation/` - Offensive Security and Authorized Validation: explicitly authorized assessment planning, rules of engagement, emulation governance, retest planning, and safety review.
- `mistral-vibe/cybersecurity/cyber-resilience-specialized-technologies/` - Cyber Resilience and Specialized Technologies: resilience, ransomware recovery planning, specialized technology review, cryptography, critical infrastructure, OT/IoT/cloud edge, and transition assurance.

## Native components

- Area `AGENTS.md` files for durable area ownership and safety instructions.
- `.vibe/config.toml` area configuration for default agent selection and conservative tool permissions.
- `.vibe/agents/*.toml` native Vibe agent and subagent profiles.
- `.vibe/prompts/*.md` only for retained agent `system_prompt_id` values.
- `.vibe/skills/*/SKILL.md` reusable Agent Skills.

Unsupported native mechanisms are omitted rather than simulated. The package does not include fake MCP servers, live hooks that execute security actions, hosted scanner integrations, cloud deployment automation, or credentials.

## How to use the department

Select the area that owns the requested work, open or import that area according to the platform rules above, and provide authorized scope, exclusions, accountable owner, requester, intended audience, decision needed, evidence inventory, assumptions, constraints, reviewer, and approver role.

Example input:

```text
Use the incident-command-evidence-agent profile and the incident-readiness-triage Skill. Review only the supplied tabletop notes, identify missing incident-declaration evidence, and prepare a human decision log. Do not connect to SIEM, EDR, ticketing, cloud, or production systems.
```

Expected outputs are scoped artifacts with evidence tables, assumptions, findings or recommendations separated by evidence state, limitations, confidence, residual risk, required human decisions, and completion criteria. High-impact outputs must be routed to an independent reviewer that did not create the work. Components stop when authorization is missing, sensitive data is unredacted, scope is unclear, a live action is requested, evidence is insufficient for a conclusion, or self-review would occur.

## Permissions and safety

Default behavior is read-only and static. Repository writes, where a platform technically allows them, must stay inside the selected `mistral-vibe/cybersecurity/<area>/` directory and require an explicit user task to update static artifacts. Shell, network, installation, deployment, scanning, exploitation, recovery execution, remote Git operations, MCP connections, hosted tools, and external connectors are prohibited by default.

AI components cannot self-approve, accept enterprise risk, authorize offensive testing, approve production changes, close incidents, certify compliance, make legal determinations, or conceal residual risk. Human review is mandatory for approvals, exceptions, risk acceptance, release or closure decisions, incident command, offensive authorization, external reporting, and production actions.

## Configuration and customization

Organizations may add policies, frameworks, asset context, risk appetite, service-level targets, tool names, responsible roles, approved integrations, sector requirements, and evidence templates as static files in the relevant area after human review. Keep values organization-neutral in shared packages, redact sensitive information, and document any integration without enabling it by default.

### Project-dependent configuration

Adapt repository paths, source directories, application architecture, build systems, deployment model, telemetry locations, product requirements, threat-model scope, project assets, approved targets, area working directories, and repository-specific policies per project. These values must not be hard-coded globally.

### User/organization-dependent configuration

Supply or approve account/subscription, user identity, organization policies, regulatory frameworks, risk appetite, asset criticality, SLAs, escalation contacts, approval authorities, permitted tools, permitted integrations, credentials, MCP endpoints, cloud accounts, SIEM/EDR/XDR/SOAR systems, ticketing systems, incident contacts, authorized offensive-testing scope, data-retention requirements, and legal/privacy constraints outside this repository. Never commit real secrets or confidential organization values.

### Fixed baseline configuration

Keep area ownership boundaries, independent review, no self-approval, no automatic risk acceptance, evidence requirements, disabled MCP/connectors/write/shell defaults, prohibited unauthorized actions, stop conditions, and human-approval gates intact.

## Validation

Static validation can check file syntax, native paths, frontmatter, JSON/TOML/YAML parsing, prompt references, Skill structure, duplicate or obsolete files, empty artifacts, broken links, and absence of secrets or active integrations. Live system behavior, connector access, model behavior, scanner operation, incident action, recovery, and production integration require a separate authorized environment and were not exercised by this repository package.

## Troubleshooting

- If prompts do not resolve, launch from the area directory and either trust the project prompt directory or set `VIBE_HOME="$PWD/.vibe"` for repository-local resolution.
- If instructions are ignored, confirm the platform was opened from the documented working directory or the files were manually imported into the correct Vibe agent, prompt, Skill, or config location.
- If an agent or Skill is unavailable, verify the platform feature is enabled for the plan/workspace and that the TOML filename, `agent_type`, `display_name`, `description`, `safety`, and `system_prompt_id` match the current product documentation.
- If permissions appear broader than intended, inspect platform settings before use and deny shell, network, MCP, connector, deployment, scanner, and remote Git access.
- If paths fail to resolve, use paths relative to the selected area package unless the platform documentation states otherwise.
- If a platform preview feature changes, re-check official documentation and update `mistral-vibe/cybersecurity/NATIVE_SOURCES.md` before relying on it.

## Removal or uninstall

Remove imported Skills or agents from Vibe's configured user/project locations, unset any temporary `VIBE_HOME` used for repository-local launch, or delete the selected `mistral-vibe/cybersecurity/` directory from the repository. Do not delete `~/.vibe`, organization evidence, credentials, or platform-global settings unless a human owner explicitly authorizes that cleanup.

## Limitations

This package is a static professional baseline. It is not a managed security service, scanner, SIEM, SOAR, EDR/XDR integration, penetration-testing tool, incident-response platform, legal opinion, compliance certification, or production-control system. Platform support and schema details can change, especially for preview agent, Skill, hook, and permission features.

## Security notice

Offensive testing, incident actions, production changes, external integrations, live scans, exploitation, deployment, recovery, publication, and use of sensitive evidence require explicit authorization, validated scope, and human control. Do not use these components to bypass approval, access secrets, contact external systems, or claim live execution without evidence.
