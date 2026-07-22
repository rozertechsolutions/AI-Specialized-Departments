# Cybersecurity Department for cline

This Cybersecurity department is a professional, adaptable baseline for cline covering governance, architecture, product security, vulnerability management, defensive operations, incident response, authorized offensive validation, and resilience.

Its purpose is to help humans produce evidence-based cybersecurity work products while preserving clear professional ownership, least privilege, independent review, and human authority for consequential decisions.

Possible uses include risk and compliance assessment, security architecture review, threat modeling, secure SDLC review, vulnerability prioritization, detection engineering, incident-response planning, authorized penetration-test planning, resilience exercises, and independent assurance.

## Department overview

The department contains eight Cybersecurity areas under `cline/cybersecurity/<area>/`. Each area is scoped to a distinct professional ownership boundary and is intended for static analysis, planning, review, documentation, and assurance using supplied evidence.

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

Product surface: Cline IDE extension, TUI, CLI, `AGENTS.md` Rule sources, `.clinerules/workflows/` custom workflows, `.cline/skills/` Skills, hooks when separately configured, Cline-managed read-only subagents, Agent Teams on supported SDK/CLI/Kanban surfaces, MCP configuration when separately approved, and approval controls.

Validated documentation date: 2026-07-22. Cline documents `AGENTS.md` and `.clinerules/` as Rule sources, custom workflows under `.clinerules/workflows/`, project Skills, hooks, MCP, plugins, CLI/TUI usage, and Cline-managed experimental subagents. The current official documentation does not establish `.cline/agents/*.md` as a repository-native declarative custom-agent format for project-defined named subagents, so this package does not include that directory. Agent Teams apply to Cline SDK, CLI, and Kanban surfaces, not the VS Code or JetBrains extensions. Plan, account, workspace, IDE, CLI, SDK, and preview availability vary by vendor release and administrator policy. This package documents static, repository-local or manually importable components only.

## Prerequisites

Cline extension installed in a supported IDE, or Cline CLI/TUI installed for terminal use; trusted workspace; user approval prompts retained. CLI use requires provider authentication through Cline or an approved provider before model-backed use. Repository validation of this package does not require authentication and does not run Cline.

Do not place credentials, tokens, keys, private endpoints, personal data, confidential customer data, or live system access material in this package. Connectors, MCP servers, cloud accounts, scanners, SIEM/EDR/XDR/SOAR tools, ticketing systems, identity providers, and hosted tools are disabled or absent unless a retained native file explicitly documents a human-approved external configuration.

## Installation or import

Place the directory in the repository, open the repository as a trusted Cline workspace, and start Cline from the relevant area directory, for example:

```text
cd cline/cybersecurity/governance-risk-compliance-assurance
cline -p "/governance-policy-frameworks Review the supplied policy evidence. Do not modify files."
```

In the IDE extension, open the repository, navigate to the selected `cline/cybersecurity/<area>/`, and ask Cline to use the area's `AGENTS.md`, `.clinerules/workflows/`, and `.cline/skills/` assets. If a Skill is not shown in Cline's Skills UI, copy or import the specific area skill directory into the documented Cline skill location and keep the original repository copy as the source baseline.

Use project-local or repository-local setup only. Do not install tools globally from this package, and do not authenticate services merely to import the instructions.

## Working directory and discovery

Cline loads Rule and project configuration from the trusted workspace. In this package, each area is intended to be used as the effective workspace root so that its local `AGENTS.md`, `.clinerules/workflows/`, and `.cline/skills/` assets describe that area without bleeding into another area.

Current Cline subagents created through `use_subagents` are Cline-managed read-only research workers. They can read files, list files, search, run restricted read-only commands, and use Skills, but cannot edit files, use the browser, access MCP servers, perform web searches, or spawn nested subagents. Do not assume repository-defined named Cline subagents exist; use the retained `AGENTS.md` baseline, workflows, and Skills directly.

When upward discovery applies, the nearest area-level instructions take precedence for that area. When a surface requires manual import, treat each area as an isolated package and do not mix files across areas unless a human explicitly approves a cross-area handoff.

## Area map

- `cline/cybersecurity/governance-risk-compliance-assurance/` - Governance, Risk, Compliance, and Assurance: governance, cyber risk, compliance mapping, policies, assurance, exceptions, and risk-decision support.
- `cline/cybersecurity/security-architecture-engineering/` - Security Architecture and Engineering: security architecture, engineering patterns, identity, network, cloud, data, platform, and control design review.
- `cline/cybersecurity/application-product-devsecops-security/` - Application, Product, and DevSecOps Security: product security, secure SDLC, threat modeling, code/design review, CI/CD, supply chain, PSIRT, and release assurance.
- `cline/cybersecurity/exposure-vulnerability-hardening/` - Exposure, Vulnerability, and Hardening: asset exposure, vulnerability triage, prioritization, hardening, remediation governance, and validation evidence.
- `cline/cybersecurity/defensive-security-operations-detection-intelligence/` - Defensive Security Operations, Detection, and Intelligence: SOC operating model, telemetry, detection engineering, alert triage, hunting, intelligence, and coverage quality.
- `cline/cybersecurity/incident-response-dfir-recovery/` - Incident Response, DFIR, and Recovery: incident planning, evidence governance, DFIR analysis planning, containment planning, recovery coordination, and lessons learned.
- `cline/cybersecurity/offensive-security-authorized-validation/` - Offensive Security and Authorized Validation: explicitly authorized assessment planning, rules of engagement, emulation governance, retest planning, and safety review.
- `cline/cybersecurity/cyber-resilience-specialized-technologies/` - Cyber Resilience and Specialized Technologies: resilience, ransomware recovery planning, specialized technology review, cryptography, critical infrastructure, OT/IoT/cloud edge, and transition assurance.

## Native components

- Area `AGENTS.md` files for persistent area ownership and safety instructions.
- `.clinerules/workflows/*.md` custom slash-command workflows.
- `.cline/skills/*/SKILL.md` on-demand Skills.

Workflows and Skills are distinct native mechanisms: workflows provide custom slash-command entry points, while Skills provide reusable on-demand procedural guidance. Unsupported native mechanisms are omitted rather than simulated. The package does not include `.cline/agents/*.md`, fake MCP servers, live hooks that execute security actions, hosted scanner integrations, cloud deployment automation, or credentials.

## How to use the department

Select the area that owns the requested work, open or import that area according to the platform rules above, and provide authorized scope, exclusions, accountable owner, requester, intended audience, decision needed, evidence inventory, assumptions, constraints, reviewer, and approver role.

Example prompt:

```text
/exposure-lifecycle-triage Review these supplied scanner findings only as static evidence, classify prioritization confidence, identify missing asset context, and prepare a human remediation-decision package. Do not scan, connect to tools, or modify production.
```

Expected outputs are scoped artifacts with evidence tables, assumptions, findings or recommendations separated by evidence state, limitations, confidence, residual risk, required human decisions, and completion criteria. High-impact outputs must be routed to an independent reviewer that did not create the work. Components stop when authorization is missing, sensitive data is unredacted, scope is unclear, a live action is requested, evidence is insufficient for a conclusion, or self-review would occur. Stop or disable the configuration by closing the Cline task, disabling `use_subagents` in Settings -> Features -> Agent when experimental subagents are not wanted, removing imported Skills from the Skills UI, or deleting the selected area package from the repository.

## Permissions and safety

Default behavior is read-only and static. Repository writes, where a platform technically allows them, must stay inside the selected `cline/cybersecurity/<area>/` directory and require an explicit user task to update static artifacts. Shell, network, installation, deployment, scanning, exploitation, recovery execution, remote Git operations, MCP connections, hosted tools, and external connectors are prohibited by default.

AI components cannot self-approve, accept enterprise risk, authorize offensive testing, approve production changes, close incidents, certify compliance, make legal determinations, or conceal residual risk. Human review is mandatory for approvals, exceptions, risk acceptance, release or closure decisions, incident command, offensive authorization, external reporting, and production actions.

## Configuration and customization

Organizations may add policies, frameworks, asset context, risk appetite, service-level targets, tool names, responsible roles, approved integrations, sector requirements, and evidence templates as static files in the relevant area after human review. Keep values organization-neutral in shared packages, redact sensitive information, and document any integration without enabling it by default.

### Project-dependent configuration

Adapt repository paths, source directories, build systems, application architecture, deployment model, telemetry locations, approved evidence locations, assessment scope, area working directories, technology stack, and project-specific policies per repository or engagement. Do not hard-code these values globally.

### User/organization-dependent configuration

Supply or approve account access, subscription, identity, organization policies, regulatory frameworks, risk appetite, asset criticality, SLAs, escalation contacts, approval authorities, permitted tools, permitted integrations, API credentials, MCP endpoints, cloud accounts, SIEM/EDR/XDR/SOAR systems, ticketing systems, incident contacts, authorized offensive-testing scope, data-retention requirements, and legal or privacy constraints outside this repository. Never commit real secrets or confidential organization values.

### Fixed baseline configuration

Keep area ownership boundaries, independent review, no self-approval, no automatic risk acceptance, evidence requirements, safe defaults, prohibited unauthorized actions, stop conditions, and human-approval gates intact. These controls define the reusable safety and governance model.

## Validation

Static validation can check file syntax, native paths, frontmatter, JSON/TOML/YAML parsing, prompt references, Skill structure, duplicate or obsolete files, empty artifacts, broken links, and absence of secrets or active integrations. Live system behavior, connector access, model behavior, scanner operation, incident action, recovery, and production integration require a separate authorized environment and were not exercised by this repository package.

## Troubleshooting

- If instructions are ignored, confirm the platform was opened from the documented working directory or the files were manually imported into the correct Project, Skill, agent, or rule location.
- If an agent or Skill is unavailable, verify the platform feature is enabled for the plan/workspace and that the directory name and native filename match the current product documentation.
- If a named specialist role is needed, use the equivalent Rule, Skill, workflow, or area `AGENTS.md` section directly; Cline-managed `use_subagents` remains a separate experimental read-only research feature and is not a repository-defined named-agent system.
- If permissions appear broader than intended, inspect platform settings before use and deny shell, network, MCP, connector, deployment, scanner, and remote Git access.
- If paths fail to resolve, use paths relative to the selected area package unless the platform documentation states otherwise.
- If a platform preview feature changes, re-check official documentation and update `cline/cybersecurity/NATIVE_SOURCES.md` before relying on it.

## Removal or uninstall

Remove the imported Project, GPT, Skill, agent, rule, command, workflow, or workspace configuration from the platform UI or delete the selected `cline/cybersecurity/` directory from the repository. Remove any manually uploaded knowledge files from the platform. Do not delete organizational evidence or platform-global settings unless a human owner explicitly authorizes that cleanup.

## Limitations

This package is a static professional baseline. It is not a managed security service, scanner, SIEM, SOAR, EDR/XDR integration, penetration-testing tool, incident-response platform, legal opinion, compliance certification, or production-control system. Platform support and schema details can change, especially for preview agent, Skill, hook, and permission features.

## Security notice

Offensive testing, incident actions, production changes, external integrations, live scans, exploitation, deployment, recovery, publication, and use of sensitive evidence require explicit authorization, validated scope, and human control. Do not use these components to bypass approval, access secrets, contact external systems, or claim live execution without evidence.
