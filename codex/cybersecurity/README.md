# Codex Cybersecurity Department

This Cybersecurity department is a professional Codex baseline for governance, risk, compliance, assurance, security architecture and engineering, application/product/DevSecOps security, exposure and hardening, defensive operations and intelligence, incident response and recovery, authorized offensive validation, and resilience or specialized technology security.

It solves the problem of producing evidence-based cybersecurity artifacts inside Codex while preserving native discovery, least privilege, independent review, and human accountability. Possible uses include risk assessment, security architecture review, threat modeling, secure SDLC review, vulnerability prioritization, detection planning, incident readiness, authorized assessment planning, resilience review, and independent assurance.

## Department Overview

The department contains eight isolated Cybersecurity area workspaces under `codex/cybersecurity/<area>/`. Each area provides `AGENTS.md`, project-scoped `.codex/config.toml`, Codex custom agent TOML files, and repository Skills under `.agents/skills/`.

Codex can assist with static analysis, drafting, review, and handoff planning. It is not authorized to accept risk, approve exceptions, authorize offensive testing, approve production changes, declare or close incidents, make legal determinations, certify compliance, operate live security tooling, or act without a human accountable owner.

## Possible Uses

- Produce GRC packages from supplied policies, control mappings, exceptions, and evidence.
- Review security architecture, identity, cloud, network, data, container, and automation designs.
- Run static threat modeling, secure design review, supply-chain review, release-readiness support, and PSIRT planning.
- Prioritize supplied findings and draft remediation or hardening plans.
- Design telemetry, detections, triage paths, threat-hunt plans, and SOC quality reviews.
- Prepare incident command artifacts, DFIR plans, containment plans, recovery coordination, and lessons learned.
- Plan explicitly authorized validation, rules of engagement, deconfliction, retest, and Purple Team assurance.
- Review resilience, ransomware recovery, OT/ICS, IoT, embedded, AI, firmware, cryptographic agility, and critical infrastructure security.

## Platform Compatibility

Validated on 2026-07-21 against current OpenAI Codex documentation for ChatGPT desktop app, Codex CLI, and Codex IDE extension.

Supported repository-local surfaces in this package:

- `AGENTS.md` area instructions.
- `.codex/config.toml` project-scoped config layers.
- `.codex/agents/*.toml` custom agent files.
- `.agents/skills/<skill>/SKILL.md` repository Skills.

Not used:

- `.codex/commands/`, because Codex custom prompts are deprecated, user-home based, and should be replaced by Skills.
- `.codex/skills/`, because Codex repository Skill discovery uses `.agents/skills`.
- Project-local provider/auth/profile/telemetry settings, because Codex ignores those keys in trusted project config.
- Hooks and MCP servers, because this baseline must not execute commands or connect external services by default.

## Prerequisites

- ChatGPT desktop app with Codex, Codex CLI, or Codex IDE extension.
- A trusted project if you want `.codex/config.toml`, custom agents, hooks, or other project `.codex/` layers to load.
- The selected area directory used as the current working directory for area-local config and Skills.
- No API key, MCP server, connector, scanner, cloud account, or production credential is required for this package.

Do not commit credentials, private keys, tokens, private endpoints, personal data, confidential customer data, or unredacted incident evidence.

## Installation Or Import

Use one area at a time. From the repository root, change into the selected area and start Codex:

```bash
cd codex/cybersecurity/application-product-devsecops-security
codex
```

For IDE use, open the selected area folder or start the IDE chat with that folder as the active workspace. Trust the project only after reviewing the local `.codex/config.toml` and confirming it contains only intended safe settings.

To use a custom agent, ask Codex to use the named agent or to delegate to it, for example:

```text
Use the requirements-threat-modeling-agent to review the supplied checkout-service design notes. Scope is static review only. Exclude live testing and production access. Return a threat model with evidence gaps, assumptions, recommended controls, and independent-review requirements.
```

To invoke a Skill explicitly, mention it with `$`, for example `$threat-modeling`, or use `/skills` where available.

## Working Directory And Discovery

Launch from the selected area directory, such as `codex/cybersecurity/governance-risk-compliance-assurance/`. Codex discovers project configuration by walking from the project root to the current working directory; closer config and guidance win for overlapping settings.

Auto-discovered or applicable when the selected area is in scope:

- `AGENTS.md`: Codex reads guidance from the project root down to the current directory.
- `.codex/config.toml`: loaded only when the project is trusted; closest config wins.
- `.codex/agents/*.toml`: project-scoped custom agents.
- `.agents/skills/<skill>/SKILL.md`: repository Skills scanned from the current working directory upward to the repository root.

Not auto-discovered as shipped:

- `codex/cybersecurity/README.md` as runtime instructions.
- `.codex/commands/` custom prompts; they were removed because they are not the current repo-native mechanism.
- Hooks, MCP servers, connectors, scanners, SIEM/EDR/XDR/SOAR tools, ticketing systems, cloud accounts, and production tools.

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

- `AGENTS.md`: always-relevant area instructions.
- `.codex/config.toml`: trusted project config with `sandbox_mode = "read-only"` and `approval_policy = "on-request"`.
- `.codex/agents/*.toml`: custom agents with required `name`, `description`, and `developer_instructions`, plus read-only sandbox settings.
- `.agents/skills/<skill>/SKILL.md`: reusable Skills with required `name` and `description` frontmatter.

No hooks are included because Codex hooks can execute commands during lifecycle events. No MCP servers are included because this baseline must not connect external systems by default.

## How To Use The Department

Select the area that owns the work, start Codex from that area, and provide:

- authorized scope and explicit exclusions;
- accountable owner, requester, reviewer, approver role, and intended audience;
- evidence inventory with provenance, period, freshness, and limitations;
- decision needed, assumptions, constraints, and required output.

Expected output is a scoped artifact with evidence tables, findings separated by evidence state, assumptions, limitations, confidence, residual risk, required human decisions, and completion criteria. High-impact, closure-facing, exception, release, incident, offensive, or external-facing outputs must go to an independent reviewer that did not create the artifact.

Stop when authorization is missing, evidence is unredacted or insufficient, scope is unclear, a live action is requested, an output would self-review, or a human-only decision is requested.

## Permissions And Safety

Area `.codex/config.toml` files request `sandbox_mode = "read-only"` and `approval_policy = "on-request"`. These settings rely on Codex project trust and the user's active client policy. They do not override provider credentials, profile selection, telemetry routing, notifications, or user/global policy.

The package does not configure MCP, hooks, shell allowlists, network access, scanners, write permissions, deployment tools, or production integrations. If the user has broader global Codex settings, review them before relying on this package for static-only work.

Human approval is required for risk acceptance, exception approval, policy publication, architecture approval, release readiness, incident declaration or closure, external distribution, supplier decisions, offensive authorization, production recovery, and critical finding closure.

## Configuration And Customization

### Project-dependent configuration

Adapt repository paths, source directories, application architecture, build systems, languages, deployment model, cloud provider, CI/CD structure, telemetry locations, asset inventory, data-flow scope, threat-model scope, vulnerability evidence, approved test scope, area-specific working directories, and repository-specific policies per project.

### User/organization-dependent configuration

Supply or approve account access, user identity, organization policies, regulatory frameworks, risk appetite, asset criticality, SLAs, escalation contacts, approval authorities, permitted tools, permitted integrations, API credentials, MCP endpoints, cloud accounts, SIEM/EDR/XDR/SOAR systems, ticketing systems, incident contacts, authorized offensive-testing scope, retention rules, and legal/privacy constraints outside this repository. Do not commit secrets or confidential values.

### Fixed baseline configuration

Keep area ownership boundaries, independent review, no self-approval, no automatic risk acceptance, evidence requirements, read-only defaults, prohibited unauthorized actions, stop conditions, no live integrations by default, and human approval gates intact.

## Validation

Repository validation can parse TOML, check Markdown frontmatter, confirm all eight areas exist, verify custom agent required fields, verify `.agents/skills` discovery paths, confirm no `.codex/commands` or `.codex/skills` remain, confirm no hooks or MCP servers are included, and scan for temporary residue or secrets.

Runtime behavior, model availability, project trust prompts, subagent spawning, hooks, MCP, connector behavior, live tool access, scanner output, incident actions, recovery, and production changes require a separately authorized Codex environment and were not executed.

## Troubleshooting

- If a custom agent is unavailable, confirm the project is trusted and the file exists under the selected area's `.codex/agents/`.
- If Skills are unavailable, confirm they are under `.agents/skills/<skill>/SKILL.md`, not `.codex/skills/`.
- If old slash command instructions are expected, use the corresponding Skill instead; repository `.codex/commands/` prompt files are not retained.
- If config appears ignored, confirm project trust and check whether the setting is one of the project-local keys Codex intentionally ignores.
- If permissions appear broader than this README states, inspect user-level Codex config, managed policy, MCP, hooks, sandbox mode, and approval policy before proceeding.

## Removal Or Uninstall

To remove repository-local configuration, stop opening the selected area as a Codex workspace or delete the selected `codex/cybersecurity/<area>/` directory from the repository. To remove copied user-global Skills or custom agents, delete only the specific cybersecurity files from the user's Codex or `.agents` locations after confirming they are not used elsewhere.

## Limitations

This package is a static professional baseline, not a managed security service, scanner, SIEM, SOAR, EDR/XDR integration, penetration-testing platform, incident command system, recovery orchestrator, legal opinion, compliance certification, or production-control system. Codex schemas and feature availability can change, especially around custom agents, Skills, hooks, MCP, permissions, and model access.

## Security Notice

Explicit authorization and human control are mandatory for offensive testing, incident actions, production changes, external integrations, live scans, exploitation, deployment, recovery, publication, and sensitive evidence handling. Do not use this package to bypass approval, access secrets, contact external systems, or claim execution without evidence.
