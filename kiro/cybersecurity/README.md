# Kiro Cybersecurity Department

This Cybersecurity department is a professional Kiro baseline for governance, risk, compliance, assurance, security architecture and engineering, application/product/DevSecOps security, exposure and hardening, defensive operations and intelligence, incident response and recovery, authorized offensive validation, and resilience or specialized technology security.

It solves the problem of turning supplied, authorized evidence into reviewable cybersecurity artifacts while preserving area ownership, least privilege, independent review, and human accountability. Realistic uses include risk and compliance review, architecture assessment, threat modeling, secure SDLC review, vulnerability prioritization, detection planning, incident readiness, authorized assessment planning, recovery exercises, and independent assurance.

## Department Overview

The department contains eight isolated area workspaces under `kiro/cybersecurity/<area>/`. Each area includes Kiro-compatible workspace instructions, Skills, and CLI custom agents for static analysis, planning, documentation, and assurance from repository-local or user-supplied evidence.

Kiro can assist with drafting and review, but it is not authorized to accept risk, approve exceptions, authorize offensive testing, approve production changes, declare or close incidents, make legal determinations, certify compliance, operate live security tooling, or act without a human accountable owner.

## Possible Uses

- Map policies, controls, evidence, exceptions, and risks to a reviewable GRC package.
- Review security architecture, identity, cloud, network, data, container, and automation patterns.
- Perform static threat modeling, secure design review, supply-chain review, release-readiness support, and PSIRT planning.
- Prioritize supplied vulnerability findings and produce remediation or hardening plans.
- Design telemetry, detections, triage paths, threat-hunt plans, and SOC quality reviews.
- Prepare incident command artifacts, DFIR plans, containment plans, recovery coordination, and lessons learned.
- Plan explicitly authorized offensive validation, rules of engagement, deconfliction, retest, and Purple Team validation.
- Review resilience, ransomware recovery, OT/ICS, IoT, embedded, AI, firmware, cryptographic agility, and critical infrastructure security.

## Platform Compatibility

Validated on 2026-07-22 against current Kiro documentation for IDE and CLI surfaces.

Supported repository-local surfaces in this package:

- Kiro CLI custom agents in each area at `.kiro/agents/*.json`.
- Kiro workspace Skills in each area at `.kiro/skills/<skill>/SKILL.md`.
- `AGENTS.md` in each area as the canonical always-included area baseline.

Kiro IDE custom subagents are Markdown files in `.kiro/agents/*.md`; this package does not use that IDE subagent format. Kiro Specs are generated IDE artifacts based on `requirements.md` or `bugfix.md`, `design.md`, and `tasks.md`; this package does not ship prebuilt flat `.kiro/specs/*.md` prompt files. Hooks and MCP are supported by Kiro, but they are intentionally absent here.

Kiro availability, models, credits, and feature access depend on the user's Kiro IDE or CLI version, account, workspace trust, administrator policy, and selected model.

## Prerequisites

- Kiro IDE or Kiro CLI installed and allowed for the user's workspace.
- The selected area directory opened or used as the current working directory.
- Workspace trust granted according to Kiro's trust model.
- No credentials or live integrations are required for this package.

Do not commit credentials, private keys, tokens, private endpoints, personal data, confidential customer data, or unredacted incident evidence into this repository.

## Installation Or Import

Use one area at a time. From the repository root, change into the area that owns the work:

```bash
cd kiro/cybersecurity/application-product-devsecops-security
kiro-cli
```

In Kiro CLI, switch to a custom cybersecurity agent with:

```text
> /agent swap
```

Then choose an agent such as `requirements-threat-modeling-agent`, or start directly when supported:

```bash
kiro-cli --agent requirements-threat-modeling-agent
```

For Kiro IDE, open the selected area folder as the workspace if you want area-local `.kiro/skills/` and `AGENTS.md` to apply without mixing areas. Workspace Skills can also be imported through the Kiro Agent Steering & Skills panel by choosing a local Skill folder. The repository does not copy anything into `~/.kiro/`.

## Working Directory And Discovery

Launch Kiro from the selected area directory, for example `kiro/cybersecurity/governance-risk-compliance-assurance/`. Area isolation depends on this working directory.

Kiro CLI local custom agents are discovered from `.kiro/agents/` in the current workspace and take precedence over same-named global agents. The retained JSON agents use current fields including `name`, `description`, `mcpServers`, `includeMcpJson`, `tools`, `allowedTools`, and `prompt`.

The package uses Kiro's default resource inheritance model. Current Kiro CLI custom agents inherit default resources, including workspace Skills and `AGENTS.md`, unless `chat.disableInheritingDefaultResources` is set to `true`. This package does not require that user or workspace setting and does not duplicate inherited resources in each custom-agent JSON file.

Auto-discovered in this package when the area is the workspace:

- `.kiro/agents/*.json` for Kiro CLI custom agents.
- `.kiro/skills/<skill>/SKILL.md` for Kiro Skills.
- `AGENTS.md` for area guidance.

Not auto-discovered as shipped:

- Repository-level `kiro/cybersecurity/README.md` as runtime instructions.
- Kiro IDE custom subagent Markdown, because this package uses the CLI JSON custom-agent surface.
- Kiro Specs, because native Specs are created in the IDE workflow.
- Hooks, MCP servers, connectors, scanners, SIEM/EDR/XDR/SOAR tools, ticketing systems, cloud accounts, or hosted tools.

## Area Map

- `governance-risk-compliance-assurance/`: governance, policy, control mapping, compliance, risk records, exceptions, assurance, evidence, suppliers, maturity, and reporting.
- `security-architecture-engineering/`: security architecture, engineering patterns, identity, cloud, network, data, containers, infrastructure as code, automation, and architecture assurance.
- `application-product-devsecops-security/`: product security, secure SDLC, threat modeling, secure code/design review, CI/CD, software supply chain, PSIRT, release readiness, and appsec assurance.
- `exposure-vulnerability-hardening/`: exposure management, vulnerability triage, prioritization, hardening, remediation governance, validation, and reporting.
- `defensive-security-operations-detection-intelligence/`: SOC governance, telemetry, detection engineering, triage, hunting, intelligence, malware-analysis planning, automation review, and coverage quality.
- `incident-response-dfir-recovery/`: incident command, evidence governance, DFIR planning, containment planning, recovery coordination, scenarios, crisis review, and corrective action.
- `offensive-security-authorized-validation/`: authorization, scope, rules of engagement, assessment planning, deconfliction, emulation, Purple Team validation, findings, cleanup, retest, and safety review.
- `cyber-resilience-specialized-technologies/`: resilience programs, ransomware recovery, backups, specialized technology security, OT/ICS, IoT, embedded, AI systems, firmware, cryptographic agility, critical infrastructure, and transition governance.

## Native Components

Each area contains:

- `AGENTS.md`: always-included area instructions and AGENTS.md standard compatibility.
- `.kiro/agents/*.json`: Kiro CLI custom agents with read-only `tools` and `allowedTools` set to `read`, no MCP servers, `includeMcpJson: false`, and no redundant declarations for default-inherited `AGENTS.md` or Skills.
- `.kiro/skills/<skill>/SKILL.md`: Agent Skills with required `name` and `description` frontmatter.

`.kiro/steering/<area>.md` copies were removed because they were byte-identical to `AGENTS.md`, had no inclusion-mode frontmatter, and would duplicate the same always-on baseline. No hooks are included because Kiro hooks can execute shell commands or agent prompts automatically. No MCP servers are included because this baseline must not connect external systems by default.

## How To Use The Department

Select the area that owns the work, start Kiro from that area directory, and provide:

- authorized scope and explicit exclusions;
- accountable owner, requester, reviewer, approver role, and intended audience;
- evidence inventory with provenance, period, freshness, and limitations;
- decision needed, assumptions, constraints, and required output.

Example input:

```text
Use the requirements-threat-modeling-agent to review the supplied design summary and data-flow notes for the checkout service. Scope is static review only. Exclude live testing and production access. Output a threat model with assumptions, evidence gaps, recommended controls, and independent-review requirements.
```

Expected output is a scoped artifact with evidence tables, findings separated by evidence state, assumptions, limitations, confidence, residual risk, required human decisions, and completion criteria. High-impact, closure-facing, exception, release, incident, offensive, or external-facing outputs must go to an independent reviewer that did not create the artifact.

Stop when authorization is missing, evidence is unredacted or insufficient, scope is unclear, a live action is requested, an output would self-review, or a human-only decision is requested.

## Permissions And Safety

The retained custom agents only expose Kiro's `read` tool and allow only `read` without prompting. They do not define shell, write, network, scanner, deployment, MCP, or connector tools. `includeMcpJson` is set to `false` and `mcpServers` is empty.

Kiro itself may have broader user or workspace capabilities outside this package. Before use, confirm the selected Kiro session has not inherited global MCP, hooks, write tools, shell tools, cloud accounts, or connectors that conflict with the requested static work. If a user or workspace sets `chat.disableInheritingDefaultResources = true`, custom agents will not receive default `AGENTS.md` or Skills; either unset that setting for this package or explicitly import only the needed area baseline and Skills after human review.

Human approval is required for risk acceptance, exception approval, policy publication, architecture approval, release readiness, incident declaration or closure, external distribution, supplier decisions, offensive authorization, production recovery, and critical finding closure.

## Configuration And Customization

### Project-dependent configuration

Adapt repository paths, source directories, application architecture, build systems, languages, deployment model, cloud provider, CI/CD structure, telemetry locations, asset inventory, data-flow scope, threat-model scope, vulnerability evidence, approved test scope, area-specific working directories, and repository-specific policies per project.

### User/organization-dependent configuration

Supply or approve account access, user identity, organization policies, regulatory frameworks, risk appetite, asset criticality, SLAs, escalation contacts, approval authorities, permitted tools, permitted integrations, API credentials, MCP endpoints, cloud accounts, SIEM/EDR/XDR/SOAR systems, ticketing systems, incident contacts, authorized offensive-testing scope, retention rules, and legal/privacy constraints outside this repository. Do not commit secrets or confidential values.

### Fixed baseline configuration

Keep area ownership boundaries, independent review, no self-approval, no automatic risk acceptance, evidence requirements, read-only defaults, prohibited unauthorized actions, stop conditions, no live integrations by default, and human approval gates intact.

## Validation

Repository validation can parse JSON, check Markdown frontmatter, confirm all eight areas exist, verify 41 Kiro CLI JSON agents, verify Skills have required frontmatter, confirm default-inherited area-local `AGENTS.md` and Skills exist, confirm no hooks or MCP servers are included, detect obsolete flat Specs, detect metadata-only settings, and scan for temporary residue or secrets.

Runtime behavior, model availability, workspace trust prompts, IDE Spec creation, hooks, MCP, connector behavior, live tool access, scanner output, incident actions, recovery, and production changes require a separately authorized Kiro environment and were not executed.

## Troubleshooting

- If a custom agent is missing, confirm Kiro CLI was launched from the selected area directory and check `.kiro/agents/*.json`.
- If a global agent shadows the intended one, use the area-local agent from the current workspace; local agents take precedence over global agents with the same name.
- If Skills are not available, verify each Skill is under `.kiro/skills/<skill>/SKILL.md` and that frontmatter `name` matches the folder name.
- If area instructions do not apply, confirm the area is the workspace root and that default resource inheritance has not been disabled.
- If Kiro Specs are needed, create them through the IDE Spec workflow; do not treat deleted flat prompt files as native Specs.
- If permissions appear broader than this README states, inspect Kiro global settings, inherited resources, hooks, MCP configuration, and active model/tool permissions before proceeding.

## Removal Or Uninstall

To remove repository-local configuration, delete or stop opening the selected `kiro/cybersecurity/<area>/` workspace. To remove imported Skills, delete them through the Kiro Agent Steering & Skills panel or from the workspace `.kiro/skills/` directory. To remove user-global imports, delete only the specific copied cybersecurity files from `~/.kiro/skills/`, `~/.kiro/steering/`, or `~/.kiro/agents/` after confirming they are not used elsewhere.

## Limitations

This package is a static professional baseline, not a managed security service, scanner, SIEM, SOAR, EDR/XDR integration, penetration-testing platform, incident command system, recovery orchestrator, legal opinion, compliance certification, or production-control system. Kiro schemas and feature availability can change, especially around CLI v3, hooks, global resources, MCP, subagents, and model access.

## Security Notice

Explicit authorization and human control are mandatory for offensive testing, incident actions, production changes, external integrations, live scans, exploitation, deployment, recovery, publication, and sensitive evidence handling. Do not use this package to bypass approval, access secrets, contact external systems, or claim execution without evidence.
