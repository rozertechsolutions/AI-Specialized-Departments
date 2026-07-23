# Cybersecurity Department for Junie

This Cybersecurity department is a reusable Junie baseline for governance, risk, compliance, and assurance; security architecture and engineering; application, product, and DevSecOps security; exposure, vulnerability, and hardening management; defensive operations, detection, and threat intelligence; incident response, DFIR, and recovery; authorized offensive validation; and resilience and specialized technologies.

It solves the professional problem of turning scoped cybersecurity evidence into reviewable work products while keeping accountability, authorization, approvals, risk acceptance, incident command, offensive testing authorization, and production decisions with humans.

Possible uses include risk and compliance assessment, architecture review, threat modeling, secure SDLC review, vulnerability prioritization, detection engineering review, incident-response planning, authorized assessment planning, resilience exercises, and independent assurance.

## Department overview

The department contains eight isolated Junie project packages under `junie/cybersecurity/<area>/`. Each area has `.junie/AGENTS.md` guidelines, `.junie/agents/*.md` custom subagents, `.junie/skills/<skill>/SKILL.md` Agent Skills, `.junie/commands/*.md` custom slash commands, and `.junie/config.json` discovery controls.

The AI is not authorized to accept enterprise risk, approve its own work, authorize offensive testing, approve production changes, make legal determinations, approve incident closure or recovery completion, hide residual risk, or claim execution without evidence.

## Possible uses

- Produce governance, policy, risk, compliance, exception, assurance, and reporting drafts from supplied evidence.
- Review security architecture decisions, reference patterns, identity, network, cloud, data, platform, and control designs.
- Support threat modeling, secure design and code review, CI/CD and supply-chain review, PSIRT coordination, and release-readiness evidence review.
- Triage supplied vulnerability and exposure findings, plan hardening, and review remediation evidence.
- Draft telemetry requirements, detection logic review notes, SOC triage procedures, threat-hunt plans, and intelligence assessments.
- Prepare incident readiness, DFIR planning, evidence handling, containment planning, recovery coordination, tabletop, and lessons-learned artifacts.
- Plan explicitly authorized offensive validation, rules of engagement, deconfliction, emulation, Purple Team validation, retest, and cleanup assurance.
- Review resilience, ransomware recovery, OT/ICS, IoT, embedded, AI security, hardware, firmware, cryptography, and critical-infrastructure concerns.

## Platform compatibility

Validated against current JetBrains Junie documentation checked on 2026-07-21 for Junie CLI and Junie in JetBrains IDEs. Junie Skills work in CLI and JetBrains IDEs. Custom subagents, custom slash commands, project configuration, MCP discovery controls, and command-line discovery controls are Junie CLI surfaces; IDE support and settings can vary by JetBrains IDE version, AI subscription, administrator policy, and Early Access availability.

Junie CLI discovers project configuration from `<project-root>/.junie/config.json` by default. This package is intentionally arranged so each cybersecurity area can be opened as the Junie project root.

## Prerequisites

- A supported JetBrains IDE with Junie enabled, or Junie CLI installed and authenticated by the user outside this repository.
- A trusted project workspace.
- Explicit authorized scope, exclusions, human owner, reviewer, approver role, and redacted evidence for the requested cybersecurity work.
- No committed credentials, API keys, tokens, private endpoints, live scanner access, SIEM/EDR/XDR/SOAR access, cloud account access, ticketing credentials, or incident contacts.

## Installation or import

For area-isolated CLI use, run Junie from the selected area as the project root:

```bash
junie --project junie/cybersecurity/governance-risk-compliance-assurance --plan --prompt "Use /governance-policy-frameworks for a static policy-control mapping review using the supplied evidence in docs/security-evidence/"
```

For an IDE workflow, open the selected `junie/cybersecurity/<area>/` folder as the project in a supported JetBrains IDE, confirm Junie is enabled, and use the area `.junie/AGENTS.md`, Skills, agents, and commands from that project context.

Do not copy these files to `~/.junie/` unless a user intentionally wants global personal defaults. This repository does not install global configuration, authenticate Junie, connect MCP, start hooks, or run a model during validation.

## Working directory and discovery

Use the selected area directory as `<project-root>`, for example `junie/cybersecurity/application-product-devsecops-security/`.

Junie discovers:

- `.junie/AGENTS.md` as the project guidelines file.
- `.junie/config.json` as project configuration.
- `.junie/agents/*.md` as project custom subagents.
- `.junie/skills/<skill-name>/SKILL.md` as project Skills.
- `.junie/commands/*.md` as project slash commands.

The retained `.junie/config.json` files set explicit area-local `agent-locations`, `skill-locations`, and `command-locations`, disable default user/project discovery for those component classes, disable default MCP discovery, disable custom model profile discovery, and disable auto-update checks. Command-line flags and user settings still have higher Junie precedence than project config, so the user must avoid overriding these safety defaults for security work unless an authorized human approves the change.

Area isolation matters: do not open `junie/cybersecurity/` as the Junie project root and expect all eight nested area packages to merge correctly. Choose one area root per task.

## Area map

- `junie/cybersecurity/governance-risk-compliance-assurance/` - governance, policy, risk, compliance mapping, exceptions, evidence assurance, third-party review, and reporting.
- `junie/cybersecurity/security-architecture-engineering/` - enterprise, solution, identity, cloud, network, data, container, automation, and control architecture review.
- `junie/cybersecurity/application-product-devsecops-security/` - product security, secure SDLC, threat modeling, secure design/code review, CI/CD, supply chain, PSIRT, and release assurance.
- `junie/cybersecurity/exposure-vulnerability-hardening/` - exposure management, vulnerability triage, asset/finding prioritization, remediation, hardening, and validation reporting.
- `junie/cybersecurity/defensive-security-operations-detection-intelligence/` - SOC governance, telemetry, detection, triage, hunting, intelligence, malware-analysis planning, automation review, and coverage quality.
- `junie/cybersecurity/incident-response-dfir-recovery/` - incident command support, evidence governance, DFIR planning, containment planning, recovery coordination, scenarios, and post-incident corrective action.
- `junie/cybersecurity/offensive-security-authorized-validation/` - authorization, scope, rules of engagement, assessment planning, emulation governance, deconfliction, retest, cleanup, and independent safety review.
- `junie/cybersecurity/cyber-resilience-specialized-technologies/` - resilience program review, backup/recovery, ransomware recovery, specialized technology, OT/ICS, IoT, AI security, hardware, firmware, cryptography, and critical infrastructure.

## Native components

Each area retains only native Junie components:

- `.junie/AGENTS.md` project guidelines.
- `.junie/config.json` documented CLI project configuration.
- `.junie/agents/*.md` custom subagents with YAML frontmatter.
- `.junie/skills/<skill>/SKILL.md` Agent Skills.
- `.junie/commands/*.md` custom slash commands.

No project hooks, MCP server definitions, global settings, scanner connectors, cloud connectors, or live-action workflows are included.

## How to use the department

Select the area that owns the work, open that area as the Junie project, and provide an input such as:

```text
Use /threat-modeling for the payment-service design. Scope: repository files under services/payments and the attached architecture note. Exclusions: production access, scanning, exploitation, and deployment. Output: threat model, assumptions, evidence gaps, findings, and independent review checklist.
```

Expected output is a static artifact with scope, evidence table, assumptions, findings separated by evidence state, limitations, confidence, residual risk, required human decisions, handoffs, stop conditions, and completion criteria.

Custom subagents are selected by Junie delegation based on `name` and `description`; they are not manually invoked as slash commands. Use slash commands such as `/threat-modeling`, `/independent-assurance-review`, or `/incident-readiness-triage` when the current area provides the command file. Skills load when their names and descriptions match the task or when an agent/command body explicitly directs their use.

Stop if authorization is missing, evidence is insufficient for the requested conclusion, sensitive data is unredacted, the task asks for live action, a self-review would occur, or a human-only decision is requested.

## Permissions and safety

Agent frontmatter uses the read-only built-in Junie tool groups `Read`, `Grep`, and `Glob`. Because `tools` is present and non-empty, other built-in tool groups are not available to those subagents by default.

The project config disables default MCP discovery and this package contains no `.junie/mcp/mcp.json`. Shell, write, edit, network, MCP, connector, scanner, deployment, incident containment, recovery execution, and production changes are prohibited unless a separate authorized environment and human approval explicitly allow them outside this baseline.

Junie IDE and CLI approval settings still matter. Do not add broad Action Allowlist rules for terminal commands, MCP tools, repository writes, or external actions when using this package for cybersecurity review.

## Configuration and customization

### Project-dependent configuration

Adapt repository paths, source directories, application architecture, build systems, technology stack, deployment model, cloud provider, CI/CD structure, telemetry locations, product requirements, threat-model scope, project assets, approved targets, area working directory, and repository-specific policies per project. These values belong in project evidence or area-local static context, not in global user configuration.

### User/organization-dependent configuration

Supply or approve account/subscription, user identity, organization policies, regulatory frameworks, risk appetite, asset criticality, SLAs, escalation contacts, approval authorities, permitted tools, permitted integrations, API credentials, MCP endpoints, cloud accounts, SIEM/EDR/XDR/SOAR systems, ticketing systems, incident contacts, offensive-testing scope, data retention, legal constraints, and privacy constraints outside this repository. Never commit real secrets or confidential organization values.

### Fixed baseline configuration

Keep area ownership boundaries, independent review, no self-approval, no automatic risk acceptance, evidence requirements, read-only defaults, prohibited unauthorized actions, stop conditions, and human approval gates unless a formal governance change approves a different baseline.

## Validation

Repository validation covers JSON parsing, Markdown/YAML frontmatter parsing, area coverage, native path layout, Skill names and descriptions, command file format, agent name uniqueness, read-only tool allowlists, reference reachability, duplicate/orphan review, empty artifact checks, and absence of secrets or temporary residue.

Runtime validation of actual Junie delegation, model behavior, IDE UI behavior, authenticated CLI use, MCP availability, connector access, live scans, incident actions, and production changes requires a separate authorized environment and was not performed by this repository remediation.

## Troubleshooting

- If Junie ignores the files, confirm the selected area directory, not `junie/cybersecurity/`, is opened as the project root.
- If commands are missing, confirm `.junie/config.json` points to `./commands` and the command file is under `.junie/commands/<command>.md`.
- If a Skill is not used, check `.junie/skills/<name>/SKILL.md`, the YAML `name`, and the specificity of `description`.
- If a subagent is not delegated to, check the `.junie/agents/*.md` YAML `name`, `description`, and supported tool group labels.
- If MCP tools appear, inspect CLI flags, user settings, and IDE settings; command-line flags and user settings can override project config.
- If model selection fails, remove unsupported project model overrides and select an available model through Junie's normal UI or CLI.

## Removal or uninstall

To remove this package from a repository, delete the selected `junie/cybersecurity/<area>/` or the whole `junie/cybersecurity/` directory after preserving any project evidence stored elsewhere. To remove an imported global copy, delete the copied files from `~/.junie/agents/`, `~/.junie/skills/`, `~/.junie/commands/`, or `~/.junie/config.json` only when the user owns those global settings and explicitly approves.

For IDE removal, remove any manually imported commands, Skills, agents, MCP entries, or Action Allowlist rules through the Junie or JetBrains IDE settings. Do not delete organizational evidence, incident records, tickets, scanner data, or platform-global settings unless the responsible human owner authorizes it.

## Limitations

This package is a static professional baseline, not a managed security service, scanner, SIEM, SOAR, EDR/XDR integration, penetration-testing tool, DFIR platform, legal opinion, compliance certification, or production-control system. Junie feature availability, subagent behavior, model support, and IDE/CLI parity can change, especially for Early Access capabilities.

## Security notice

Offensive testing, incident actions, production changes, external integrations, live scans, exploitation, deployment, recovery, publication, and sensitive evidence handling require explicit authorization, validated scope, and human control. Do not use these components to bypass approval, access secrets, contact external systems, or claim live execution without evidence.
