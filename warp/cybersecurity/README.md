# Warp Cybersecurity Department

This Cybersecurity department is a professional Warp Project Rules and Skills package covering governance, risk, compliance, assurance, security architecture and engineering, application/product/DevSecOps security, exposure and hardening, defensive operations and intelligence, incident response and recovery, authorized offensive validation, and resilience or specialized technology security.

It solves the problem of opening a bounded cybersecurity area in Warp with area-specific Project Rules and reusable Skills while keeping Oz cloud-agent setup, schedules, integrations, and MCP servers out of the repository. Possible uses include policy review, control mapping, risk exception support, architecture review, threat modeling, secure SDLC review, vulnerability prioritization, detection planning, incident readiness, authorized validation planning, resilience review, and independent assurance.

## Department Overview

The department contains eight area packages under `warp/cybersecurity/<area>/`. Each area contains an `AGENTS.md` Project Rules file and `.warp/skills/*/SKILL.md` Skill packages.

Warp agents can assist with static repository review, drafting, evidence organization, and handoff planning. They are not authorized to accept enterprise risk, approve exceptions, authorize offensive testing, approve production changes, declare or close incidents, make legal determinations, certify compliance, operate live security tooling, or act without a human accountable owner.

## Possible Uses

- Open Warp in one cybersecurity area so its `AGENTS.md` Project Rules apply.
- Ask Warp Agent to use a discovered Skill by natural language.
- Invoke a discovered Skill as a slash command, for example `/governance-policy-frameworks`, when Warp lists it.
- Use `AGENTS.md` as persistent constraints and Skills as specific task workflows.
- Copy the area into an Oz project only after a human approves cloud-agent execution and environment controls.

## Platform Compatibility

Validated on 2026-07-21 against current Warp documentation.

Supported Warp surfaces:

- Local Warp Agent Mode and Auto-Detection Mode.
- Project Rules through uppercase `AGENTS.md`; `WARP.md` remains a supported fallback, but this package uses `AGENTS.md`.
- Project Skills through `.warp/skills/*/SKILL.md`.
- Skill invocation by natural language or slash command.
- Oz CLI, Oz web app, schedules, integrations, and cloud agents only as optional manual setup outside this repository.

This package does not configure Warp settings, Agent Profiles, Oz environments, Oz runs, schedules, Slack/Linear triggers, providers, custom inference endpoints, MCP servers, or terminal automation.

## Prerequisites

- Warp installed with Agent features available to the user.
- A trusted local checkout.
- Human authorization for the selected cybersecurity scope and any supplied evidence.
- Workspace approval before using Oz cloud agents, shared Skills, MCP servers, integrations, schedules, or remote environments.

No API keys, credentials, MCP servers, scanners, cloud accounts, Oz environments, schedules, or production access are included in this package.

## Installation Or Import

Use one area at a time.

1. Open Warp at the repository root.
2. Change into the selected area, for example:

   ```text
   cd warp/cybersecurity/offensive-security-authorized-validation
   ```

3. Start a Warp Agent conversation from that directory.
4. Confirm the area `AGENTS.md` appears as applied Project Rules or as a referenced rule.
5. Ask what Skills are available, or invoke a specific Skill by name.

Do not use `/cloud-agent`, Oz schedules, Oz environments, or integrations merely to install this package. Those are separate Warp/Oz features requiring explicit authorization and configuration outside this repository.

## Working Directory And Discovery

Launch directory:

```text
warp/cybersecurity/<area>/
```

Auto-discovered by Warp from that area:

- `AGENTS.md` as Project Rules.
- `.warp/skills/*/SKILL.md` as project Skills.

Warp applies Project Rules from the current directory and repository root, with current-subdirectory rules taking precedence over root rules and Global Rules. Skill discovery is based on the current working directory; in Git repositories, Warp includes skills from the current directory up through the repository root. Keep areas isolated by launching from exactly one area directory.

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

- `AGENTS.md`: Warp Project Rules for the selected area.
- `.warp/skills/*/SKILL.md`: project Skills with required `name` and `description` frontmatter.

No repository custom-agent files, Oz run definitions, schedules, environments, Agent Profiles, MCP servers, Warp settings files, hooks, plugins, scanner connectors, or live app integrations are included.

## How To Use The Department

Select the area that owns the work, launch Warp from that area, and provide:

- authorized scope and explicit exclusions;
- accountable owner, requester, reviewer, approver role, and intended audience;
- evidence inventory with provenance, period, freshness, and limitations;
- decision needed, assumptions, constraints, and required output.

Example input:

```text
Use the /authorization-scope-roe Skill in this Offensive Security Authorized Validation area. Review the supplied rules of engagement draft. Scope is static review only. Exclude live testing. Return missing authorization terms, safety gates, evidence gaps, emergency-stop requirements, and independent-review needs.
```

Expected output is a scoped artifact with evidence tables, findings separated by evidence state, assumptions, limitations, confidence, residual risk, required human decisions, and completion criteria. High-impact, closure-facing, exception, release, incident, offensive, or external-facing outputs must go to an independent reviewer that did not create the artifact.

Stop when authorization is missing, evidence is unredacted or insufficient, scope is unclear, a live action is requested, an output would self-review, or a human-only decision is requested.

## Permissions And Safety

Warp local agents can use terminal context and may run commands depending on user interaction, profiles, settings, and approvals. This repository provides text rules and Skills only; it does not enforce terminal permissions by configuration.

Keep the Warp Agent AI toggle, Agent Profiles, MCP servers, full terminal use, web search, custom endpoints, and Oz permissions configured by the user or workspace. Do not add MCP servers, integrations, cloud environments, schedules, or production credentials unless a human explicitly approves them outside this repository.

Human approval is required for risk acceptance, exception approval, policy publication, architecture approval, release readiness, incident declaration or closure, external distribution, supplier decisions, offensive authorization, production recovery, and critical finding closure.

## Configuration And Customization

### Project-dependent configuration

Adapt repository paths, source directories, application architecture, build systems, languages, deployment model, cloud provider, CI/CD structure, telemetry locations, asset inventory, data-flow scope, threat-model scope, vulnerability evidence, approved test scope, area-specific working directories, and repository-specific policies per project.

### User/organization-dependent configuration

Supply or approve Warp installation, account identity, workspace policy, Agent Profile, provider/model choice, custom endpoint, Oz cloud-agent eligibility, environment, schedule, integration, MCP endpoints, organization policies, regulatory frameworks, risk appetite, asset criticality, SLAs, escalation contacts, approval authorities, permitted tools, cloud accounts, SIEM/EDR/XDR/SOAR systems, ticketing systems, incident contacts, authorized offensive-testing scope, retention rules, and legal/privacy constraints outside this repository. Do not commit secrets or confidential values.

### Fixed baseline configuration

Keep area ownership boundaries, independent review, no self-approval, no automatic risk acceptance, evidence requirements, static-by-default behavior, prohibited unauthorized actions, stop conditions, no live integrations by default, and human approval gates intact.

## Validation

Repository validation can check Markdown frontmatter, area coverage, file existence, exact duplicates, empty files, empty directories, and absence of fake custom agents, Oz run definitions, schedules, MCP configs, credentials, and live integrations.

Runtime behavior, model behavior, Warp Agent settings, Agent Profiles, terminal-command approval, MCP behavior, Oz CLI behavior, Oz cloud runs, schedules, integrations, scanner output, incident actions, recovery, and production changes require a separately authorized Warp/Oz environment and were not executed.

## Troubleshooting

- If Project Rules are not applied, confirm the file is uppercase `AGENTS.md` and Warp was launched from `warp/cybersecurity/<area>/`.
- If the wrong rules apply, check for a `WARP.md` in the same directory because Warp gives it priority over `AGENTS.md`.
- If a Skill is unavailable, confirm it is under `.warp/skills/<skill>/SKILL.md` and has `name` and `description` frontmatter.
- If Skills from another area appear, restart the agent conversation from the intended area directory.
- If an MCP server, integration, cloud run, or schedule appears, inspect Warp/Oz user or workspace settings; this repository does not configure them.

## Removal Or Uninstall

Stop the Warp Agent conversation, leave the selected area directory, or remove the imported/copied `AGENTS.md` and `.warp/skills/` files from a consuming project. Remove Warp/Oz global rules, project links, MCP servers, Agent Profiles, cloud schedules, environments, integrations, or credentials only through the user's approved Warp/Oz settings process. Do not delete unrelated organization evidence or global Warp settings without human approval.

## Limitations

This package is a static professional baseline for Warp rules and Skills, not a managed security service, scanner, SIEM, SOAR, EDR/XDR integration, penetration-testing platform, incident command system, recovery orchestrator, legal opinion, compliance certification, production-control system, Oz environment, or scheduled cloud-agent workflow. Warp/Oz behavior, Skill discovery, and cloud-agent capabilities can change.

## Security Notice

Explicit authorization and human control are mandatory for offensive testing, incident actions, production changes, external integrations, live scans, exploitation, deployment, recovery, publication, and sensitive evidence handling. Do not use this package to bypass approval, access secrets, contact external systems, or claim execution without evidence.
