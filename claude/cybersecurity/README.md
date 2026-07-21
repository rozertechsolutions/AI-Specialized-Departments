<<<<<<< HEAD
# Cybersecurity Department for Claude

This Cybersecurity department is a professional, adaptable Claude web and desktop baseline covering governance, architecture, product security, vulnerability management, defensive operations, incident response, authorized offensive validation, and resilience. Its purpose is to help qualified humans prepare structured cybersecurity analysis, plans, reviews, evidence requests, and assurance outputs in Claude Projects and Claude Skills without granting the AI authority to execute security actions or accept risk. Realistic uses include risk and compliance assessment, security architecture review, threat modeling, secure SDLC review, vulnerability prioritization, detection engineering, incident-response planning, authorized penetration-test planning, resilience exercises, and independent assurance.

## Department overview

This package contains Claude-native manual import materials for the eight Cybersecurity areas under `claude/cybersecurity/`. It covers static advisory work using Project instructions, Project knowledge, uploaded files, and optional Claude Skills. It does not authorize live scans, exploitation, containment, recovery, production changes, legal determinations, external communication, connector authentication, risk acceptance, or security-tool operation. Accountable humans remain responsible for authorization, evidence quality, approvals, implementation, risk decisions, and final sign-off.

## Possible uses

- Governance, risk, compliance, policy, exception, and assurance review.
- Security architecture and engineering review for identity, cloud, network, data, containers, IaC, and automation.
- Product security, secure SDLC, threat modeling, code-review planning, CI/CD, release, supply-chain, and PSIRT support.
- Exposure, vulnerability, hardening, remediation, and validation-prioritization support from authorized evidence.
- Detection engineering, telemetry coverage, SOC triage, hunting, intelligence, malware-analysis planning, and quality review.
- Incident readiness, evidence governance, DFIR planning, containment planning, recovery planning, and lessons learned.
- Explicitly authorized offensive validation planning, rules of engagement, purple-team exercises, findings, cleanup, and retest assurance.
- Cyber-resilience, ransomware-resilience, recovery exercises, specialized technology review, critical infrastructure, cryptography, AI, OT, IoT, hardware, and firmware assurance.

## Platform compatibility

Validated against official Claude Help Center and Anthropic documentation checked on 2026-07-20 for Claude Projects, project instructions, project knowledge, RAG for projects, Claude Skills, connectors, custom remote MCP connectors, artifacts, file creation, and release notes. Projects are available to all Claude users, with free users limited to a maximum of five projects. Project sharing is a Team and Enterprise capability. Skills are available on Free, Pro, Max, Team, and Enterprise plans and require code execution and file creation to be enabled. Claude web and Claude Desktop can use Projects, uploaded knowledge, Skills, artifacts, and connectors subject to plan and organization settings. This `claude/` package is not a Claude Code repository package and does not use Claude Code `CLAUDE.md`, subagents, commands, hooks, local MCP configuration, or `.claude/` discovery.

## Prerequisites

- A Claude account with access to Projects.
- Permission to create or edit the target Project and, for Team or Enterprise, permission to share or manage it.
- Code execution and file creation enabled if using Claude Skills or artifacts.
- Organization owner approval where Team or Enterprise settings control Skills, project sharing, code execution, file creation, network egress, or connectors.
- Repository trust review before uploading any files or Skill bundles.
- No secrets, credentials, private keys, tokens, personal data, private endpoints, or confidential organization values unless the organization has approved that data handling and the data is minimized or redacted.

## Installation or import

Use one area as one Claude Project or Skill set.

1. Open Claude web or Claude Desktop and create a Project for the selected Cybersecurity area.
2. Copy the area's `PROJECT_INSTRUCTIONS.md` into the Project instructions field.
3. Upload the area's `knowledge/`, `templates/`, and `workflows/` files to Project knowledge.
4. If using Skills, package each `skills/<skill-name>/` directory as an uploadable Skill ZIP or recreate it through Claude's custom Skill flow. Each Skill must contain its top-level `SKILL.md`.
5. Keep connectors, remote MCP, browser access, local-file access, network egress, and write-capable external integrations disabled unless separately authorized by accountable humans and workspace owners.

Do not use global installers or Claude Code commands for this package. Claude web and desktop do not automatically load repository files from disk.

## Working directory and discovery

The documented working directory is the selected area path, for example `claude/cybersecurity/incident-response-dfir-recovery/`. Claude web and desktop discover only what a user manually pastes into Project instructions, uploads to Project knowledge, uploads as a Skill, or enables in Claude settings. There is no upward or downward repository discovery for this package. Each area is an isolated import package; do not combine areas unless a human intentionally wants a multi-area Project. Project instructions apply only inside the Project. Uploaded Project knowledge is available across chats in that Project, while Skills activate dynamically when enabled and relevant.

## Area map

- `governance-risk-compliance-assurance/`: governance, risk, compliance, policy, assurance, exceptions, third-party risk, maturity, reporting, and risk-decision support.
- `security-architecture-engineering/`: security architecture, engineering patterns, identity, cloud, network, data, container, IaC, and automation review.
- `application-product-devsecops-security/`: application, product, secure SDLC, threat modeling, software supply chain, CI/CD, release, and PSIRT review.
- `exposure-vulnerability-hardening/`: exposure management, vulnerability triage, hardening, remediation, validation, and reporting assurance.
- `defensive-security-operations-detection-intelligence/`: telemetry, SOC governance, detection, triage, hunting, intelligence, malware-analysis planning, and escalation handoff.
- `incident-response-dfir-recovery/`: incident command, evidence governance, DFIR planning, containment planning, recovery planning, crisis scenarios, and post-incident review.
- `offensive-security-authorized-validation/`: authorization, scope, rules of engagement, assessment planning, emulation, purple-team safety, findings, cleanup, and retest assurance.
- `cyber-resilience-specialized-technologies/`: resilience, backup, ransomware recovery, specialized technology, cryptography, critical infrastructure, AI, OT, IoT, hardware, firmware, and transition assurance.

## Native components

This package uses Claude Project instructions, Project knowledge files, uploaded workflow files, output templates, and Claude Skills. It intentionally omits Claude Code instructions, Claude Code Skills discovery paths, subagents, commands, hooks, local MCP server files, desktop extension manifests, connector definitions, plugins, browser automation, and fake integrations because those are not native repository-loaded surfaces for Claude web/desktop Projects.

## How to use the department

Choose the area that owns the request, open that area's Claude Project, and provide authorized scope, exclusions, objective, source evidence, evidence period, accountable human owner, desired output, constraints, and review expectations. Invoke an enabled Skill by describing the task naturally or naming the Skill's purpose. Expected outputs include reviews, evidence tables, decision records, plans, findings, validation criteria, escalation notes, and assurance summaries. Human review is mandatory for high-impact outputs, risk acceptance, exception approval, policy publication, release readiness, incident declaration or closure, recovery completion, external distribution, supplier decisions, offensive authorization, and critical finding closure. The component must stop for missing authorization, insufficient evidence, sensitive-data exposure, requested live action, self-review, circular delegation, or unsupported platform behavior.

## Permissions and safety

Claude Projects and uploaded Skills do not define repository-local read/write permissions. They can use only conversation context, manually uploaded knowledge, enabled capabilities, and separately configured connectors. For this package, use supplied static evidence and redacted placeholders by default. Disable connector access, remote MCP, browser use, local-file access, network egress, and write-capable external actions unless separately approved. Claude must not self-approve, accept risk, authorize offensive testing, approve production changes, close incidents, approve recovery, make legal determinations, or claim execution without evidence.

## Configuration and customization

Organizations may safely add approved policies, frameworks, asset context, risk appetite, severity models, SLAs, tool names, responsible roles, approved integration names, sector requirements, evidence standards, and review-board requirements as Project knowledge or instruction additions. Keep reusable package content organization-neutral. Use placeholders for sensitive facts unless upload and processing have been approved.

## Validation

Static validation can confirm the eight areas exist, Markdown and Skill frontmatter parse, local references resolve, no empty files or directories remain, no unsupported Claude Code surfaces are claimed, and no connectors or MCP servers are configured. Live import, Skill upload scanning, Project behavior, connector permissions, artifact behavior, and organization settings require an authorized Claude workspace and were not live-tested by this repository package.

## Troubleshooting

- If instructions are ignored, confirm they were pasted into the selected Project instructions and the chat is inside that Project.
- If knowledge is unavailable, check upload status, file limits, Project selection, and whether RAG is retrieving the expected file.
- If a Skill does not activate, confirm code execution and file creation are enabled, the Skill was uploaded or shared correctly, and the Skill is toggled on.
- If sharing fails, confirm Team or Enterprise project-sharing settings and member permissions.
- If connectors appear in responses, disable them or remove authorization unless a separate approved integration plan exists.
- If Claude Code behavior is expected, use the separate `claude-code/` platform package instead.

## Removal or uninstall

Delete or archive the Claude Project created from this package, remove uploaded knowledge files, disable or delete uploaded custom Skills, and remove project sharing. For Team or Enterprise, owners should remove provisioned Skills or connector access through organization settings if they were separately enabled. No repository-local uninstall command exists for Claude web/desktop.

## Limitations

Claude web and desktop do not automatically read this repository. This package does not configure Claude Code, Cowork plugins, subagents, hooks, scheduled tasks, local MCP, remote MCP, connectors, browser use, or production integrations. Feature availability depends on plan, app surface, region, rollout, and organization settings. The package provides professional analysis scaffolding, not proof that any live system was tested.

## Security notice

Offensive testing, incident actions, production changes, external integrations, connector use, credential handling, live-system access, browser control, local-file writes, and remote MCP use require explicit authorization, human control, and applicable organizational approvals. Do not use this package to bypass security, privacy, legal, change-management, or incident-command processes.
=======
# Cybersecurity Department for claude

This Cybersecurity department is a professional, adaptable baseline for claude covering governance, architecture, product security, vulnerability management, defensive operations, incident response, authorized offensive validation, and resilience.

Its purpose is to help humans produce evidence-based cybersecurity work products while preserving clear professional ownership, least privilege, independent review, and human authority for consequential decisions.

Possible uses include risk and compliance assessment, security architecture review, threat modeling, secure SDLC review, vulnerability prioritization, detection engineering, incident-response planning, authorized penetration-test planning, resilience exercises, and independent assurance.

## Department overview

The department contains eight Cybersecurity areas under `claude/cybersecurity/<area>/`. Each area is scoped to a distinct professional ownership boundary and is intended for static analysis, planning, review, documentation, and assurance using supplied evidence.

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

Product surface: Claude web and desktop Projects, project instructions, project knowledge, and Claude Agent Skills.

Validated documentation date: 2026-07-21. Plan, account, workspace, IDE, CLI, SDK, and preview availability vary by vendor release and administrator policy. This package documents static, repository-local or manually importable components only.

## Prerequisites

Claude plan with Projects and Skills where available; connector access disabled unless separately approved.

Do not place credentials, tokens, keys, private endpoints, personal data, confidential customer data, or live system access material in this package. Connectors, MCP servers, cloud accounts, scanners, SIEM/EDR/XDR/SOAR tools, ticketing systems, identity providers, and hosted tools are disabled or absent unless a retained native file explicitly documents a human-approved external configuration.

## Installation or import

Create a Claude Project per area, paste PROJECT_INSTRUCTIONS.md into project instructions, upload knowledge/templates/workflows as project knowledge, and import skills/*/SKILL.md manually where custom Skills are supported.

Use project-local or repository-local setup only. Do not install tools globally from this package, and do not authenticate services merely to import the instructions.

## Working directory and discovery

Claude web/desktop does not automatically load repository folders. Files require manual Project knowledge upload or Skill import; preserve isolation with one area per project or clearly named Skill set.

When a platform supports upward discovery, the nearest area-level instructions take precedence for that area. When a platform requires manual import, treat each area as an isolated package and do not mix files across areas unless a human explicitly approves a cross-area handoff.

## Area map

- `claude/cybersecurity/governance-risk-compliance-assurance/` - Governance, Risk, Compliance, and Assurance: governance, cyber risk, compliance mapping, policies, assurance, exceptions, and risk-decision support.
- `claude/cybersecurity/security-architecture-engineering/` - Security Architecture and Engineering: security architecture, engineering patterns, identity, network, cloud, data, platform, and control design review.
- `claude/cybersecurity/application-product-devsecops-security/` - Application, Product, and DevSecOps Security: product security, secure SDLC, threat modeling, code/design review, CI/CD, supply chain, PSIRT, and release assurance.
- `claude/cybersecurity/exposure-vulnerability-hardening/` - Exposure, Vulnerability, and Hardening: asset exposure, vulnerability triage, prioritization, hardening, remediation governance, and validation evidence.
- `claude/cybersecurity/defensive-security-operations-detection-intelligence/` - Defensive Security Operations, Detection, and Intelligence: SOC operating model, telemetry, detection engineering, alert triage, hunting, intelligence, and coverage quality.
- `claude/cybersecurity/incident-response-dfir-recovery/` - Incident Response, DFIR, and Recovery: incident planning, evidence governance, DFIR analysis planning, containment planning, recovery coordination, and lessons learned.
- `claude/cybersecurity/offensive-security-authorized-validation/` - Offensive Security and Authorized Validation: explicitly authorized assessment planning, rules of engagement, emulation governance, retest planning, and safety review.
- `claude/cybersecurity/cyber-resilience-specialized-technologies/` - Cyber Resilience and Specialized Technologies: resilience, ransomware recovery planning, specialized technology review, cryptography, critical infrastructure, OT/IoT/cloud edge, and transition assurance.

## Native components

- `governance-risk-compliance-assurance/`: `PROJECT_INSTRUCTIONS.md`, `knowledge/`, `skills/`, `workflows/`, `templates/`
- `security-architecture-engineering/`: `PROJECT_INSTRUCTIONS.md`, `knowledge/`, `skills/`, `workflows/`, `templates/`
- `application-product-devsecops-security/`: `PROJECT_INSTRUCTIONS.md`, `knowledge/`, `skills/`, `workflows/`, `templates/`
- `exposure-vulnerability-hardening/`: `PROJECT_INSTRUCTIONS.md`, `knowledge/`, `skills/`, `workflows/`, `templates/`
- `defensive-security-operations-detection-intelligence/`: `PROJECT_INSTRUCTIONS.md`, `knowledge/`, `skills/`, `workflows/`, `templates/`
- `incident-response-dfir-recovery/`: `PROJECT_INSTRUCTIONS.md`, `knowledge/`, `skills/`, `workflows/`, `templates/`
- `offensive-security-authorized-validation/`: `PROJECT_INSTRUCTIONS.md`, `knowledge/`, `skills/`, `workflows/`, `templates/`
- `cyber-resilience-specialized-technologies/`: `PROJECT_INSTRUCTIONS.md`, `knowledge/`, `skills/`, `workflows/`, `templates/`

Unsupported native mechanisms are omitted rather than simulated. The package does not include fake MCP servers, live hooks that execute security actions, hosted scanner integrations, cloud deployment automation, or credentials.

## How to use the department

Select the area that owns the requested work, open or import that area according to the platform rules above, and provide authorized scope, exclusions, accountable owner, requester, intended audience, decision needed, evidence inventory, assumptions, constraints, reviewer, and approver role.

Expected outputs are scoped artifacts with evidence tables, assumptions, findings or recommendations separated by evidence state, limitations, confidence, residual risk, required human decisions, and completion criteria. High-impact outputs must be routed to an independent reviewer that did not create the work. Components stop when authorization is missing, sensitive data is unredacted, scope is unclear, a live action is requested, evidence is insufficient for a conclusion, or self-review would occur.

## Permissions and safety

Default behavior is read-only and static. Repository writes, where a platform technically allows them, must stay inside the selected `claude/cybersecurity/<area>/` directory and require an explicit user task to update static artifacts. Shell, network, installation, deployment, scanning, exploitation, recovery execution, remote Git operations, MCP connections, hosted tools, and external connectors are prohibited by default.

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
- If a platform preview feature changes, re-check official documentation and update `claude/cybersecurity/NATIVE_SOURCES.md` before relying on it.

## Removal or uninstall

Remove the imported Project, GPT, Skill, agent, rule, command, workflow, or workspace configuration from the platform UI or delete the selected `claude/cybersecurity/` directory from the repository. Remove any manually uploaded knowledge files from the platform. Do not delete organizational evidence or platform-global settings unless a human owner explicitly authorizes that cleanup.

## Limitations

This package is a static professional baseline. It is not a managed security service, scanner, SIEM, SOAR, EDR/XDR integration, penetration-testing tool, incident-response platform, legal opinion, compliance certification, or production-control system. Platform support and schema details can change, especially for preview agent, Skill, hook, and permission features.

## Security notice

Offensive testing, incident actions, production changes, external integrations, live scans, exploitation, deployment, recovery, publication, and use of sensitive evidence require explicit authorization, validated scope, and human control. Do not use these components to bypass approval, access secrets, contact external systems, or claim live execution without evidence.
>>>>>>> feature/cybersecurity-department
