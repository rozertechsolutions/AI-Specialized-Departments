# Cybersecurity Department for cursor

This Cybersecurity department is a professional, adaptable baseline for cursor covering governance, architecture, product security, vulnerability management, defensive operations, incident response, authorized offensive validation, and resilience.

Its purpose is to help humans produce evidence-based cybersecurity work products while preserving clear professional ownership, least privilege, independent review, and human authority for consequential decisions.

Possible uses include risk and compliance assessment, security architecture review, threat modeling, secure SDLC review, vulnerability prioritization, detection engineering, incident-response planning, authorized penetration-test planning, resilience exercises, and independent assurance.

## Department overview

The department contains eight Cybersecurity areas under `cursor/cybersecurity/<area>/`. Each area is scoped to a distinct professional ownership boundary and is intended for static analysis, planning, review, documentation, and assurance using supplied evidence.

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

Product surface: Cursor IDE and Cursor CLI project context, nested `AGENTS.md`, project rules in `.cursor/rules/*.mdc`, custom subagents in `.cursor/agents/*.md`, Agent Skills in `.cursor/skills/<name>/SKILL.md`, custom command prompts in `.cursor/commands/*.md`, hooks configuration, MCP configuration, and Cursor permissions.

Validated documentation date: 2026-07-21. Cursor 2.4 introduced Subagents and Agent Skills in the editor and CLI. Plan, account, workspace, model availability, cloud-agent access, CLI features, and team policy vary by vendor release and administrator policy. This package documents static, repository-local components only.

## Prerequisites

Cursor IDE or Cursor CLI with a trusted workspace; repository rules, nested `AGENTS.md`, Agent Skills, and Subagents enabled by the user's plan/workspace policy. No integrations are enabled by this package.

Do not place credentials, tokens, keys, private endpoints, personal data, confidential customer data, or live system access material in this package. Connectors, MCP servers, cloud accounts, scanners, SIEM/EDR/XDR/SOAR tools, ticketing systems, identity providers, and hosted tools are disabled or absent unless a retained native file explicitly documents a human-approved external configuration.

## Installation or import

Open the selected area folder in Cursor so the area's `AGENTS.md`, `.cursor/agents/`, `.cursor/skills/`, `.cursor/commands/`, and any retained `.cursor/rules/*.mdc` are the active project-local package:

```bash
cursor cursor/cybersecurity/governance-risk-compliance-assurance
```

In Cursor IDE, the equivalent is File -> Open Folder and selecting `cursor/cybersecurity/<area>/`. Use one area per session unless the human explicitly asks for a cross-area handoff. Agent Skills are discovered separately from custom subagent frontmatter; do not expect a `skills:` field in `.cursor/agents/*.md` to preload Skills.

Use project-local or repository-local setup only. Do not install tools globally from this package, and do not authenticate services merely to import the instructions.

## Working directory and discovery

Cursor discovers nested `AGENTS.md` in project roots and subdirectories, project rules from `.cursor/rules/*.mdc`, custom subagents from `.cursor/agents/*.md`, Skills from `.cursor/skills/<skill-name>/SKILL.md`, and project MCP servers from `.cursor/mcp.json` when present. This package does not include `.cursor/mcp.json`.

Launch from `cursor/cybersecurity/<area>/` for area isolation. Cursor also supports user-level subagents and Skills under `~/.cursor/`, and team/user rules may apply globally; those are user- or organization-dependent and are not part of this repository. More specific nested `AGENTS.md` instructions take precedence over broader parent instructions for matching paths.

## Area map

- `cursor/cybersecurity/governance-risk-compliance-assurance/` - Governance, Risk, Compliance, and Assurance: governance, cyber risk, compliance mapping, policies, assurance, exceptions, and risk-decision support.
- `cursor/cybersecurity/security-architecture-engineering/` - Security Architecture and Engineering: security architecture, engineering patterns, identity, network, cloud, data, platform, and control design review.
- `cursor/cybersecurity/application-product-devsecops-security/` - Application, Product, and DevSecOps Security: product security, secure SDLC, threat modeling, code/design review, CI/CD, supply chain, PSIRT, and release assurance.
- `cursor/cybersecurity/exposure-vulnerability-hardening/` - Exposure, Vulnerability, and Hardening: asset exposure, vulnerability triage, prioritization, hardening, remediation governance, and validation evidence.
- `cursor/cybersecurity/defensive-security-operations-detection-intelligence/` - Defensive Security Operations, Detection, and Intelligence: SOC operating model, telemetry, detection engineering, alert triage, hunting, intelligence, and coverage quality.
- `cursor/cybersecurity/incident-response-dfir-recovery/` - Incident Response, DFIR, and Recovery: incident planning, evidence governance, DFIR analysis planning, containment planning, recovery coordination, and lessons learned.
- `cursor/cybersecurity/offensive-security-authorized-validation/` - Offensive Security and Authorized Validation: explicitly authorized assessment planning, rules of engagement, emulation governance, retest planning, and safety review.
- `cursor/cybersecurity/cyber-resilience-specialized-technologies/` - Cyber Resilience and Specialized Technologies: resilience, ransomware recovery planning, specialized technology review, cryptography, critical infrastructure, OT/IoT/cloud edge, and transition assurance.

## Native components

- `AGENTS.md`: area instructions loaded by Cursor as nested project instructions.
- `.cursor/agents/*.md`: Cursor custom subagents with native fields `name`, `description`, `model`, and `readonly`.
- `.cursor/skills/<name>/SKILL.md`: Agent Skills discovered separately by Cursor and invoked automatically when relevant or manually from the slash menu.
- `.cursor/commands/*.md`: command prompt files for manual invocation where enabled.
- `.cursor/rules/*.mdc`: retained only where the rule has Cursor rule frontmatter and independent native value.

Unsupported native mechanisms are omitted rather than simulated. The package does not include fake MCP servers, live hooks that execute security actions, hosted scanner integrations, cloud deployment automation, or credentials.

## How to use the department

Select the area that owns the requested work, open that area in Cursor, and provide authorized scope, exclusions, accountable owner, requester, intended audience, decision needed, evidence inventory, assumptions, constraints, reviewer, and approver role.

Examples:

```text
Use governance-policy-frameworks-agent to review these supplied policy excerpts against the attached control matrix. Approved scope is static evidence only. Output a gap table, assumptions, residual risk, and human approval points.
```

```text
Invoke the threat-modeling Skill for the attached API design. Do not edit files or run commands. Expected output is a threat model with abuse cases, mitigations, validation criteria, and independent-review triggers.
```

```text
Use independent-offensive-safety-reviewer on the attached rules of engagement. Confirm authorization, targets, exclusions, stop conditions, and retest boundaries. Do not scan or contact any target.
```

Expected outputs are scoped artifacts with evidence tables, assumptions, findings or recommendations separated by evidence state, limitations, confidence, residual risk, required human decisions, and completion criteria. High-impact outputs must be routed to an independent reviewer that did not create the work. Components stop when authorization is missing, sensitive data is unredacted, scope is unclear, a live action is requested, evidence is insufficient for a conclusion, or self-review would occur.

## Permissions and safety

Default behavior is read-only and static. Custom subagents use `readonly: true`, which Cursor documents as restricted write permissions with no file edits and no state-changing shell commands. Cursor subagents can inherit tools from the parent, including MCP tools from configured servers, so do not enable MCP, browser, shell, or other integrations in the parent session for this package.

Repository writes, where Cursor technically allows them outside a read-only subagent, must stay inside the selected `cursor/cybersecurity/<area>/` directory and require an explicit user task to update static artifacts. Shell, network, installation, deployment, scanning, exploitation, recovery execution, remote Git operations, MCP connections, hosted tools, and external connectors are prohibited by default.

AI components cannot self-approve, accept enterprise risk, authorize offensive testing, approve production changes, close incidents, certify compliance, make legal determinations, or conceal residual risk. Human review is mandatory for approvals, exceptions, risk acceptance, release or closure decisions, incident command, offensive authorization, external reporting, and production actions.

## Configuration and customization

Project-dependent configuration: repository paths, source directories, application architecture, technology stack, deployment model, CI/CD layout, telemetry locations, threat-model scope, asset lists, approved targets, area-specific working directories, and repository-specific policies must be supplied per project and should not be hard-coded globally.

User/organization-dependent configuration: Cursor account or subscription, user identity, team rules, model availability, cloud-agent policy, organization policies, regulatory frameworks, risk appetite, asset criticality, SLAs, escalation contacts, approval authorities, permitted tools, permitted integrations, MCP endpoints, cloud/SIEM/EDR/XDR/SOAR/ticketing systems, incident contacts, offensive-testing authorization, retention rules, and legal/privacy constraints must be supplied or approved by the user or organization. Do not commit real secrets or confidential organization values.

Fixed baseline configuration: area ownership boundaries, independent review, no self-approval, no automatic risk acceptance, evidence requirements, read-only custom subagents, absent MCP/connectors, prohibited unauthorized actions, stop conditions, and human-approval gates normally remain unchanged because they define the reusable safety model.

Organizations may add static policies, frameworks, asset context, service-level targets, approved tool names, sector requirements, and evidence templates in the relevant area after human review. Keep values organization-neutral in shared packages, redact sensitive information, and document any integration without enabling it by default.

## Validation

Static validation can check file syntax, native paths, frontmatter, JSON/TOML/YAML parsing, prompt references, Skill structure, duplicate or obsolete files, empty artifacts, broken links, and absence of secrets or active integrations. Live system behavior, connector access, model behavior, scanner operation, incident action, recovery, and production integration require a separate authorized environment and were not exercised by this repository package.

## Troubleshooting

- If instructions are ignored, confirm the platform was opened from the documented working directory or the files were manually imported into the correct Project, Skill, agent, or rule location.
- If an agent is unavailable, verify `.cursor/agents/<name>.md` exists under the opened area and contains only native custom-subagent frontmatter.
- If a Skill is unavailable, verify `.cursor/skills/<name>/SKILL.md` exists under the opened area and use Cursor's Skills view or slash menu to confirm discovery.
- If permissions appear broader than intended, inspect Cursor mode, parent session tools, MCP configuration, team/user rules, and approval settings before use; deny shell, network, MCP, connector, deployment, scanner, browser, and remote Git access.
- If paths fail to resolve, use paths relative to the selected area package unless the platform documentation states otherwise.
- If a platform preview feature changes, re-check official documentation and update `cursor/cybersecurity/NATIVE_SOURCES.md` before relying on it.

## Removal or uninstall

Close the Cursor session, remove any manually copied area files from a consuming project, or delete the selected `cursor/cybersecurity/<area>/` directory from a repository that no longer needs it. To remove one component, delete that area's `.cursor/agents/<name>.md`, `.cursor/skills/<name>/`, `.cursor/commands/<name>.md`, or retained `.cursor/rules/<name>.mdc` and restart or refresh Cursor. Do not delete organizational evidence, user settings, team rules, provider credentials, or platform-global settings unless a human owner explicitly authorizes that cleanup.

## Limitations

This package is a static professional baseline. It is not a managed security service, scanner, SIEM, SOAR, EDR/XDR integration, penetration-testing tool, incident-response platform, legal opinion, compliance certification, or production-control system. Platform support and schema details can change, especially for preview agent, Skill, hook, and permission features.

## Security notice

Offensive testing, incident actions, production changes, external integrations, live scans, exploitation, deployment, recovery, publication, and use of sensitive evidence require explicit authorization, validated scope, and human control. Do not use these components to bypass approval, access secrets, contact external systems, or claim live execution without evidence.
