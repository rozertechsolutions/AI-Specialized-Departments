# ChatGPT Cybersecurity Department

This Cybersecurity department is a professional manual-import package for ChatGPT covering governance, risk, compliance, assurance, security architecture and engineering, application/product/DevSecOps security, exposure and hardening, defensive operations and intelligence, incident response and recovery, authorized offensive validation, and resilience or specialized technology security.

It solves the problem of setting up consistent cybersecurity Projects, GPTs, Skills, or Workspace Agents in ChatGPT without pretending that ChatGPT reads repository files automatically. Possible uses include risk assessment, architecture review, threat modeling, secure SDLC review, vulnerability prioritization, detection planning, incident readiness, authorized validation planning, resilience review, and independent assurance.

## Department Overview

The department contains eight area packages under `chatgpt/cybersecurity/<area>/`. Each area contains Project/GPT instructions, knowledge files, reusable Skills, static workflow guidance, and output templates for human import into ChatGPT.

ChatGPT can assist with reasoning, drafting, review, and handoff planning. It is not authorized to accept risk, approve exceptions, authorize offensive testing, approve production changes, declare or close incidents, make legal determinations, certify compliance, operate live security tooling, or act without a human accountable owner.

## Possible Uses

- Build one ChatGPT Project per cybersecurity area for recurring static review work.
- Create a Custom GPT that uses the area instructions and knowledge for reusable organization guidance.
- Upload area Skills when the user's ChatGPT plan and workspace allow Skills.
- Build a Workspace Agent only when the organization explicitly wants a repeatable, governed workflow with approved tools and review gates.
- Review supplied policies, designs, findings, incidents, telemetry plans, assessment scopes, or resilience evidence.

## Platform Compatibility

Validated on 2026-07-21 against current OpenAI Help Center and OpenAI Academy documentation.

Supported manual/import surfaces:

- ChatGPT Projects with project instructions, files, chats, sources, tools, memory, and sharing controls.
- Custom GPTs with instructions, knowledge, and Skills where the user's plan/workspace supports them.
- ChatGPT Skills as uploaded, created, installed, or shared reusable workflows.
- Workspace Agents in eligible workspaces where administrators enable agent building, sharing, tools, and app permissions.
- Apps/plugins/connectors only as optional, separately authorized integrations.

ChatGPT does not auto-load this repository. This package contains no repository-discovered agents, hooks, MCP runtime, coding-agent permissions, scanner integrations, or cloud deployment automation.

## Prerequisites

- A logged-in ChatGPT account.
- Required plan and workspace permissions for Projects, GPT creation, Skills, app/plugin use, or Workspace Agents.
- Human authorization to import each area package and any organization evidence.
- Admin approval for workspace-wide Skills, apps/plugins/connectors, Workspace Agents, Slack use, schedules, or MCP-backed custom apps where applicable.

No API keys, credentials, connectors, scanners, cloud accounts, or production access are required to import this static package.

## Installation Or Import

Use one area at a time.

For a ChatGPT Project:

1. Create a new Project in ChatGPT.
2. Name it for the area, for example `Cybersecurity - Application Product DevSecOps Security`.
3. Open Project settings and paste the area's `PROJECT_INSTRUCTIONS.md` into project instructions.
4. Upload the area's `knowledge/`, `workflows/`, and `templates/` Markdown files as project files or sources.
5. Start new chats inside that Project and keep area-specific evidence in that Project.

For Skills:

1. Open ChatGPT Skills from the Plugins/Skills area when available.
2. Upload or create each `skills/<skill>/SKILL.md` package that the area needs.
3. Review ChatGPT's skill scan result before use.
4. Share or publish the Skill only if workspace policy allows it.

For a Custom GPT:

1. Create or edit a GPT.
2. Paste the area's `PROJECT_INSTRUCTIONS.md` into GPT instructions.
3. Upload the area's knowledge, workflow, and template files as GPT knowledge where supported.
4. Add only the Skills and tools explicitly approved for that GPT.

For a Workspace Agent:

1. Use the ChatGPT Agents builder only in an eligible workspace.
2. Convert one bounded area workflow into an agent job with trigger, process, knowledge, tools, approvals, review, and owner.
3. Add apps/plugins/connectors only through workspace-approved controls.
4. Test with redacted static evidence before sharing.

## Working Directory And Discovery

ChatGPT has no working-directory discovery for this repository. The local paths are source material for manual import only.

Auto-discovered by ChatGPT: nothing in `chatgpt/cybersecurity/`.

Manual import/copy:

- `PROJECT_INSTRUCTIONS.md` into Project, GPT, or Workspace Agent instructions.
- `knowledge/*.md`, `workflows/*.md`, and `templates/*.md` as Project/GPT/agent knowledge or sources.
- `skills/<skill>/SKILL.md` through ChatGPT's Skill create/upload/install flow.

Keep areas isolated by creating separate Projects, GPTs, or Workspace Agents. Do not mix area files unless a human explicitly approves a cross-area handoff.

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

- `PROJECT_INSTRUCTIONS.md`: primary Project/GPT/Workspace Agent instruction source.
- `knowledge/*.md`: area responsibility model or specialist knowledge.
- `skills/<skill>/SKILL.md`: ChatGPT Skill packages using the Agent Skills structure.
- `workflows/*.md`: static workflow guidance for Project/GPT/agent knowledge.
- `templates/*.md`: output schema guidance.

No hooks, MCP servers, coding-agent config, repository agents, scanner connectors, or live app integrations are included.

## How To Use The Department

Select the area that owns the work, import that area into the selected ChatGPT surface, and provide:

- authorized scope and explicit exclusions;
- accountable owner, requester, reviewer, approver role, and intended audience;
- evidence inventory with provenance, period, freshness, and limitations;
- decision needed, assumptions, constraints, and required output.

Example input:

```text
Using the Application Product DevSecOps Project and the threat-modeling Skill, review the uploaded checkout-service data-flow notes. Scope is static review only. Exclude live testing and production access. Return threats, assumptions, evidence gaps, recommended controls, and independent-review requirements.
```

Expected output is a scoped artifact with evidence tables, findings separated by evidence state, assumptions, limitations, confidence, residual risk, required human decisions, and completion criteria. High-impact, closure-facing, exception, release, incident, offensive, or external-facing outputs must go to an independent reviewer that did not create the artifact.

Stop when authorization is missing, evidence is unredacted or insufficient, scope is unclear, a live action is requested, an output would self-review, or a human-only decision is requested.

## Permissions And Safety

Projects and GPTs can use files, memory, tools, and apps according to the user's plan and workspace settings. Apps/plugins/connectors can read external data or take actions only after separate connection, authentication, and permissions. Workspace Agents use per-agent controls set by the builder and workspace administrators.

This repository does not enable any app, connector, MCP server, scanner, write action, schedule, Slack deployment, or production integration. Keep app permissions at least as restrictive as organizational policy requires, and require human confirmation for any action outside ChatGPT.

Human approval is required for risk acceptance, exception approval, policy publication, architecture approval, release readiness, incident declaration or closure, external distribution, supplier decisions, offensive authorization, production recovery, and critical finding closure.

## Configuration And Customization

### Project-dependent configuration

Adapt repository paths, source directories, application architecture, build systems, languages, deployment model, cloud provider, CI/CD structure, telemetry locations, asset inventory, data-flow scope, threat-model scope, vulnerability evidence, approved test scope, area-specific working directories, and repository-specific policies per project.

### User/organization-dependent configuration

Supply or approve account access, workspace role, project sharing, Skill permissions, GPT visibility, Workspace Agent publishing, organization policies, regulatory frameworks, risk appetite, asset criticality, SLAs, escalation contacts, approval authorities, permitted tools, permitted integrations, API credentials, app/plugin access, MCP endpoints, cloud accounts, SIEM/EDR/XDR/SOAR systems, ticketing systems, incident contacts, authorized offensive-testing scope, retention rules, and legal/privacy constraints outside this repository. Do not commit secrets or confidential values.

### Fixed baseline configuration

Keep area ownership boundaries, independent review, no self-approval, no automatic risk acceptance, evidence requirements, static-by-default behavior, prohibited unauthorized actions, stop conditions, no live integrations by default, and human approval gates intact.

## Validation

Repository validation can check Markdown frontmatter, area coverage, reference wording, file existence, duplicate or obsolete artifacts, empty files, and absence of fake agents, hooks, MCP runtime, credentials, or live integrations.

Runtime behavior, model availability, Project file limits, memory behavior, Skill scanning, workspace sharing, app/plugin permissions, Workspace Agent publishing, schedules, Slack integration, connector behavior, scanner output, incident actions, recovery, and production changes require a separately authorized ChatGPT environment and were not executed.

## Troubleshooting

- If ChatGPT ignores instructions, confirm `PROJECT_INSTRUCTIONS.md` was pasted into the Project/GPT/agent instruction field, not only uploaded as a file.
- If a Skill is unavailable, verify the account supports Skills, the workspace admin has enabled Skills, and the Skill was uploaded or installed on the surface being used.
- If evidence is missing, upload the relevant knowledge, workflow, and template files to the same Project/GPT/agent.
- If apps or connectors appear, confirm they were intentionally connected and review app permissions before using them.
- If a Workspace Agent can take action, inspect per-agent tools, approvals, schedules, triggers, Slack deployment, and app controls.

## Removal Or Uninstall

Delete the imported Project, GPT, Skill, or Workspace Agent from ChatGPT, or remove the uploaded files and instructions from that surface. Disconnect apps/plugins/connectors from Settings or ask a workspace administrator to disable them. Delete only the selected cybersecurity imports; do not remove unrelated organization evidence or global workspace settings without human approval.

## Limitations

This package is a static professional baseline, not a managed security service, scanner, SIEM, SOAR, EDR/XDR integration, penetration-testing platform, incident command system, recovery orchestrator, legal opinion, compliance certification, or production-control system. ChatGPT plan limits, file limits, memory behavior, Skill availability, app permissions, Workspace Agent availability, and admin controls can change.

## Security Notice

Explicit authorization and human control are mandatory for offensive testing, incident actions, production changes, external integrations, live scans, exploitation, deployment, recovery, publication, and sensitive evidence handling. Do not use this package to bypass approval, access secrets, contact external systems, or claim execution without evidence.
