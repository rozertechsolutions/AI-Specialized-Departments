# Cybersecurity Department for github-copilot

This Cybersecurity department is a professional, adaptable baseline for github-copilot covering governance, architecture, product security, vulnerability management, defensive operations, incident response, authorized offensive validation, and resilience.

Its purpose is to help humans produce evidence-based cybersecurity work products while preserving clear professional ownership, least privilege, independent review, and human authority for consequential decisions.

Possible uses include risk and compliance assessment, security architecture review, threat modeling, secure SDLC review, vulnerability prioritization, detection engineering, incident-response planning, authorized penetration-test planning, resilience exercises, and independent assurance.

## Department overview

The department contains eight Cybersecurity areas under `github-copilot/cybersecurity/<area>/`. Each area is scoped to a distinct professional ownership boundary and is intended for static analysis, planning, review, documentation, and assurance using supplied evidence.

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

Product surface: GitHub Copilot in VS Code, GitHub Copilot CLI, Copilot coding agent/cloud agent where enabled, workspace custom instructions in `.github/copilot-instructions.md`, custom agents in `.github/agents/*.agent.md`, prompt files in `.github/prompts/*.prompt.md`, Agent Skills in `.github/skills/<name>/SKILL.md`, optional hooks, and optional MCP only when separately configured.

Validated documentation date: 2026-07-21. Copilot subscription, VS Code version, CLI/cloud-agent access, organization customizations, available models, hooks, and MCP policy vary by account, plan, preview flag, and administrator policy. This package documents static, repository-local components only.

## Prerequisites

GitHub Copilot subscription; supported VS Code/Copilot CLI or Copilot coding-agent surface; trusted workspace; repository customizations enabled; Agent Skills/custom agents available for the user's version and plan.

Do not place credentials, tokens, keys, private endpoints, personal data, confidential customer data, or live system access material in this package. Connectors, MCP servers, cloud accounts, scanners, SIEM/EDR/XDR/SOAR tools, ticketing systems, identity providers, and hosted tools are disabled or absent unless a retained native file explicitly documents a human-approved external configuration.

## Installation or import

Open the selected area folder as the workspace so its `.github/` directory is the active customization root:

```bash
code github-copilot/cybersecurity/governance-risk-compliance-assurance
```

In VS Code, the equivalent is File -> Open Folder and selecting `github-copilot/cybersecurity/<area>/`. Confirm Copilot Chat customization diagnostics show the area's `.github/copilot-instructions.md`, `.github/agents/*.agent.md`, `.github/prompts/*.prompt.md`, and `.github/skills/`. Use one area per session unless the human explicitly asks for a cross-area handoff.

Use project-local or repository-local setup only. Do not install tools globally from this package, and do not authenticate services merely to import the instructions.

## Working directory and discovery

VS Code automatically detects `.github/copilot-instructions.md` at the workspace root for all chat requests, custom agents from `.github/agents/*.agent.md`, prompt files from `.github/prompts/*.prompt.md`, and Agent Skills from `.github/skills/<skill-name>/SKILL.md`. Prompt files are slash-command style prompts invoked manually. Skills are discovered separately and can load when relevant or be invoked from the Skills menu where supported.

Launch from `github-copilot/cybersecurity/<area>/` for area isolation. In monorepos, parent repository discovery settings can cause parent customizations to load; disable or account for those settings if you need strict area isolation. Organization-level instructions, organization custom agents, user prompts, user Skills, and user settings are user/organization-dependent and are not included here.

## Area map

- `github-copilot/cybersecurity/governance-risk-compliance-assurance/` - Governance, Risk, Compliance, and Assurance: governance, cyber risk, compliance mapping, policies, assurance, exceptions, and risk-decision support.
- `github-copilot/cybersecurity/security-architecture-engineering/` - Security Architecture and Engineering: security architecture, engineering patterns, identity, network, cloud, data, platform, and control design review.
- `github-copilot/cybersecurity/application-product-devsecops-security/` - Application, Product, and DevSecOps Security: product security, secure SDLC, threat modeling, code/design review, CI/CD, supply chain, PSIRT, and release assurance.
- `github-copilot/cybersecurity/exposure-vulnerability-hardening/` - Exposure, Vulnerability, and Hardening: asset exposure, vulnerability triage, prioritization, hardening, remediation governance, and validation evidence.
- `github-copilot/cybersecurity/defensive-security-operations-detection-intelligence/` - Defensive Security Operations, Detection, and Intelligence: SOC operating model, telemetry, detection engineering, alert triage, hunting, intelligence, and coverage quality.
- `github-copilot/cybersecurity/incident-response-dfir-recovery/` - Incident Response, DFIR, and Recovery: incident planning, evidence governance, DFIR analysis planning, containment planning, recovery coordination, and lessons learned.
- `github-copilot/cybersecurity/offensive-security-authorized-validation/` - Offensive Security and Authorized Validation: explicitly authorized assessment planning, rules of engagement, emulation governance, retest planning, and safety review.
- `github-copilot/cybersecurity/cyber-resilience-specialized-technologies/` - Cyber Resilience and Specialized Technologies: resilience, ransomware recovery planning, specialized technology review, cryptography, critical infrastructure, OT/IoT/cloud edge, and transition assurance.

## Native components

- `.github/copilot-instructions.md`: area custom instructions automatically applied in the selected workspace.
- `.github/agents/*.agent.md`: VS Code/GitHub Copilot custom agents with native frontmatter `name`, `description`, and read/search `tools`.
- `.github/prompts/*.prompt.md`: manual prompt files for reusable slash-command workflows.
- `.github/skills/<name>/SKILL.md`: Agent Skills with `name` and `description` frontmatter plus procedural instructions.

Unsupported native mechanisms are omitted rather than simulated. The package does not include fake MCP servers, live hooks that execute security actions, hosted scanner integrations, cloud deployment automation, or credentials.

## How to use the department

Select the area that owns the requested work, open that area in VS Code or the supported Copilot surface, and provide authorized scope, exclusions, accountable owner, requester, intended audience, decision needed, evidence inventory, assumptions, constraints, reviewer, and approver role.

Examples:

```text
Select governance-policy-frameworks-agent and review the supplied policy excerpts against the attached control matrix. Use static evidence only. Return a gap table, assumptions, confidence, residual risk, and human approval points.
```

```text
/threat-modeling
Scope: attached API design only.
Output: threat model with abuse cases, mitigations, validation criteria, evidence gaps, and independent-review triggers.
No file edits, shell commands, web access, or live scans.
```

```text
Use independent-offensive-safety-review on the attached rules of engagement. Confirm authorization, targets, exclusions, stop conditions, and retest boundaries. Do not scan or contact any target.
```

Expected outputs are scoped artifacts with evidence tables, assumptions, findings or recommendations separated by evidence state, limitations, confidence, residual risk, required human decisions, and completion criteria. High-impact outputs must be routed to an independent reviewer that did not create the work. Components stop when authorization is missing, sensitive data is unredacted, scope is unclear, a live action is requested, evidence is insufficient for a conclusion, or self-review would occur.

## Permissions and safety

Default behavior is read-only and static. Custom agents use VS Code/GitHub Copilot tool identifiers `search/codebase` and `search/usages` only; they do not include edit, terminal, web, MCP, pull-request, issue, or deployment tools. If a user changes the active tools, starts a different built-in agent, enables MCP, enables hooks, or uses a cloud/coding-agent environment, those permissions are outside this baseline and require separate human approval.

Repository writes, where a Copilot surface technically allows them outside the restricted custom agents, must stay inside the selected `github-copilot/cybersecurity/<area>/` directory and require an explicit user task to update static artifacts. Shell, network, installation, deployment, scanning, exploitation, recovery execution, remote Git operations, MCP connections, hosted tools, and external connectors are prohibited by default.

AI components cannot self-approve, accept enterprise risk, authorize offensive testing, approve production changes, close incidents, certify compliance, make legal determinations, or conceal residual risk. Human review is mandatory for approvals, exceptions, risk acceptance, release or closure decisions, incident command, offensive authorization, external reporting, and production actions.

## Configuration and customization

Project-dependent configuration: repository paths, source directories, application architecture, technology stack, deployment model, CI/CD layout, telemetry locations, threat-model scope, asset lists, approved targets, area-specific working directories, and repository-specific policies must be supplied per project and should not be hard-coded globally.

User/organization-dependent configuration: GitHub/Copilot subscription, organization customizations, user identity, available models, cloud/coding-agent policy, organization policies, regulatory frameworks, risk appetite, asset criticality, SLAs, escalation contacts, approval authorities, permitted tools, permitted integrations, MCP endpoints, cloud/SIEM/EDR/XDR/SOAR/ticketing systems, incident contacts, offensive-testing authorization, retention rules, and legal/privacy constraints must be supplied or approved by the user or organization. Do not commit real secrets or confidential organization values.

Fixed baseline configuration: area ownership boundaries, independent review, no self-approval, no automatic risk acceptance, evidence requirements, read/search-only custom agents, absent MCP/connectors/hooks, prohibited unauthorized actions, stop conditions, and human-approval gates normally remain unchanged because they define the reusable safety model.

Organizations may add static policies, frameworks, asset context, service-level targets, approved tool names, sector requirements, and evidence templates in the relevant area after human review. Keep values organization-neutral in shared packages, redact sensitive information, and document any integration without enabling it by default.

## Validation

Static validation can check file syntax, native paths, frontmatter, JSON/TOML/YAML parsing, prompt references, Skill structure, duplicate or obsolete files, empty artifacts, broken links, and absence of secrets or active integrations. Live system behavior, connector access, model behavior, scanner operation, incident action, recovery, and production integration require a separate authorized environment and were not exercised by this repository package.

## Troubleshooting

- If instructions are ignored, confirm the selected area is the VS Code workspace root and Copilot diagnostics list the area's `.github/copilot-instructions.md`.
- If an agent is unavailable, verify `.github/agents/<name>.agent.md` exists under the opened area and that Copilot custom agents are enabled.
- If a prompt is unavailable, verify `.github/prompts/<name>.prompt.md` exists under the opened area and invoke it from the slash-command menu.
- If a Skill is unavailable, verify `.github/skills/<name>/SKILL.md` exists under the opened area and that the Skill name matches the directory name.
- If permissions appear broader than intended, inspect active agent, selected tools, VS Code settings, MCP state, hooks, organization policy, and cloud/coding-agent mode before use.
- If paths fail to resolve, use paths relative to the selected area package unless the platform documentation states otherwise.
- If a platform preview feature changes, re-check official documentation and update `github-copilot/cybersecurity/NATIVE_SOURCES.md` before relying on it.

## Removal or uninstall

Close the Copilot session, remove any manually copied area files from a consuming project, or delete the selected `github-copilot/cybersecurity/<area>/` directory from a repository that no longer needs it. To remove one component, delete that area's `.github/agents/<name>.agent.md`, `.github/prompts/<name>.prompt.md`, `.github/skills/<name>/`, or `.github/copilot-instructions.md` and refresh VS Code/Copilot customizations. Do not delete organizational evidence, user settings, organization customizations, credentials, or platform-global settings unless a human owner explicitly authorizes that cleanup.

## Limitations

This package is a static professional baseline. It is not a managed security service, scanner, SIEM, SOAR, EDR/XDR integration, penetration-testing tool, incident-response platform, legal opinion, compliance certification, or production-control system. Platform support and schema details can change, especially for preview agent, Skill, hook, and permission features.

## Security notice

Offensive testing, incident actions, production changes, external integrations, live scans, exploitation, deployment, recovery, publication, and use of sensitive evidence require explicit authorization, validated scope, and human control. Do not use these components to bypass approval, access secrets, contact external systems, or claim live execution without evidence.
