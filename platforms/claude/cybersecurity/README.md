# Claude Cybersecurity Department

This Cybersecurity department is a professional manual-import package for Claude web and Claude Desktop. It covers governance, risk, compliance, assurance, security architecture and engineering, application/product/DevSecOps security, exposure and hardening, defensive operations and intelligence, incident response and recovery, authorized offensive validation, and resilience or specialized technology security.

It solves the problem of setting up consistent Claude Projects and Claude Skills for evidence-based cybersecurity work without pretending that Claude web or Desktop auto-discovers repository folders. Possible uses include policy review, control mapping, risk exception support, architecture review, threat modeling, secure SDLC review, vulnerability prioritization, detection planning, incident readiness, authorized validation planning, resilience review, and independent assurance.

## Department Overview

The department contains eight area packages under `claude/cybersecurity/<area>/`. Each area provides project instructions, reusable Skills, static workflow guidance, output templates, and, where useful, additional knowledge files for manual import into a Claude Project.

Claude can assist with reasoning, drafting, review, evidence organization, and handoff planning. It is not authorized to accept enterprise risk, approve exceptions, authorize offensive testing, approve production changes, declare or close incidents, make legal determinations, certify compliance, operate live security tooling, or act without a human accountable owner.

## Possible Uses

- Create one Claude Project per cybersecurity area for recurring static review work.
- Paste the selected area's `PROJECT_INSTRUCTIONS.md` into Project instructions.
- Upload the selected area's templates, workflow guidance, and unique knowledge files to Project knowledge.
- Import or recreate the relevant `skills/<skill>/SKILL.md` packages as Claude Skills when the user's plan and workspace support Skills.
- Review supplied policies, designs, findings, incident notes, telemetry plans, assessment scopes, and resilience evidence.

## Platform Compatibility

Validated on 2026-07-21 against current Anthropic Help Center and Anthropic documentation.

Supported manual/import surfaces:

- Claude web and Claude Desktop conversations.
- Claude Projects with project instructions, project knowledge, sharing controls, and project-scoped chats.
- Claude Project knowledge with uploaded documents, text, or code snippets; paid plans may use RAG mode when project knowledge approaches the context-window limit.
- Claude Skills where available to the user or workspace.
- Claude connectors only as separately approved web connectors, desktop extensions, or custom remote MCP connectors.

Claude web and Desktop do not auto-load this repository. This package contains no repository-discovered agents, hooks, MCP runtime, coding-agent permissions, scanner integrations, schedules, or cloud deployment automation.

## Prerequisites

- A Claude account in a supported location.
- Project creation rights and the required plan/workspace permissions for Projects, Skills, sharing, memory, and connectors.
- Human authorization to import each area package and any organization evidence.
- Admin approval for shared Projects, workspace Skills, connectors, remote MCP, desktop extensions, or other external integrations where applicable.

No API keys, credentials, connectors, scanners, cloud accounts, or production access are required to import this static package.

## Installation Or Import

Use one area at a time.

For a Claude Project:

1. Open `claude.ai/projects` or the Projects view in Claude.
2. Create a new Project named for the area, for example `Cybersecurity - Incident Response DFIR Recovery`.
3. Open the Project and choose `Set project instructions`.
4. Paste the area's `PROJECT_INSTRUCTIONS.md` into the instructions field and save.
5. Upload the area's `workflows/*.md`, `templates/*.md`, and any remaining `knowledge/*.md` files to Project knowledge.
6. Start chats inside that Project and keep area evidence in the same Project.

For Claude Skills:

1. Confirm that Skills are available for the user's account or workspace.
2. Create, upload, or install the relevant `skills/<skill>/SKILL.md` packages using Claude's current Skill interface.
3. Review the Skill instructions before enabling or sharing them.
4. Share Skills only when workspace policy allows it.

For connectors:

1. Do not connect anything merely to install this repository.
2. If a human later approves connector use, configure the connector in Claude settings or the approved workspace control surface.
3. Keep connector permissions limited to the user's existing authorization in the connected service.

## Working Directory And Discovery

Claude web and Desktop have no working-directory discovery for this repository. The local paths are source material for manual import only.

Auto-discovered by Claude web/Desktop: nothing in `claude/cybersecurity/`.

Manual import/copy:

- `PROJECT_INSTRUCTIONS.md` into the Claude Project instruction field.
- `workflows/*.md`, `templates/*.md`, and any `knowledge/*.md` files as Project knowledge.
- `skills/<skill>/SKILL.md` through Claude's Skill create/upload/install flow where supported.

Project instructions apply to all chats inside the selected Project. Project knowledge is separate from instructions and is used only after upload. Keep areas isolated by creating separate Projects or clearly named Skill sets. Do not mix area files unless a human explicitly approves a cross-area handoff.

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

- `PROJECT_INSTRUCTIONS.md`: primary Claude Project instruction source.
- `skills/<skill>/SKILL.md`: Claude Skill source packages.
- `workflows/*.md`: static workflow guidance for Project knowledge.
- `templates/*.md`: output schema guidance for Project knowledge.

Additional unique knowledge remains only where it has independent value:

- `governance-risk-compliance-assurance/knowledge/GOVERNANCE.md`.
- `security-architecture-engineering/knowledge/ARCHITECTURE_GOVERNANCE.md`.

The duplicate `knowledge/RESPONSIBILITY_MODEL.md` copies were removed because they were exact copies of `PROJECT_INSTRUCTIONS.md` and did not add independent Project knowledge value.

No hooks, MCP servers, coding-agent config, repository agents, scanner connectors, or live app integrations are included.

## How To Use The Department

Select the area that owns the work, import that area into a Claude Project, and provide:

- authorized scope and explicit exclusions;
- accountable owner, requester, reviewer, approver role, and intended audience;
- evidence inventory with provenance, period, freshness, and limitations;
- decision needed, assumptions, constraints, and required output.

Example input:

```text
Using the Incident Response DFIR Recovery Project and the incident-command-evidence Skill, review the uploaded ransomware tabletop notes. Scope is static readiness review only. Exclude containment execution and live log access. Return decision log gaps, evidence requirements, recovery assumptions, escalation points, and independent-review requirements.
```

Expected output is a scoped artifact with evidence tables, findings separated by evidence state, assumptions, limitations, confidence, residual risk, required human decisions, and completion criteria. High-impact, closure-facing, exception, release, incident, offensive, or external-facing outputs must go to an independent reviewer that did not create the artifact.

Stop when authorization is missing, evidence is unredacted or insufficient, scope is unclear, a live action is requested, an output would self-review, or a human-only decision is requested.

## Permissions And Safety

Claude Projects can use project instructions, project knowledge, memory, and available tools according to the user's plan and workspace settings. Connectors can retrieve data or take actions only after separate connection, authentication, and permissions. Claude inherits the user's permissions from the connected service.

This repository does not enable any connector, remote MCP server, desktop extension, scanner, write action, schedule, deployment, or production integration. Keep connector permissions at least as restrictive as organizational policy requires, and require human confirmation for any action outside Claude.

Human approval is required for risk acceptance, exception approval, policy publication, architecture approval, release readiness, incident declaration or closure, external distribution, supplier decisions, offensive authorization, production recovery, and critical finding closure.

## Configuration And Customization

### Project-dependent configuration

Adapt repository paths, source directories, application architecture, build systems, languages, deployment model, cloud provider, CI/CD structure, telemetry locations, asset inventory, data-flow scope, threat-model scope, vulnerability evidence, approved test scope, area-specific working directories, and repository-specific policies per project.

### User/organization-dependent configuration

Supply or approve account access, workspace role, Project sharing, Skill availability, organization policies, regulatory frameworks, risk appetite, asset criticality, SLAs, escalation contacts, approval authorities, permitted tools, permitted integrations, connector access, MCP endpoints, cloud accounts, SIEM/EDR/XDR/SOAR systems, ticketing systems, incident contacts, authorized offensive-testing scope, retention rules, and legal/privacy constraints outside this repository. Do not commit secrets or confidential values.

### Fixed baseline configuration

Keep area ownership boundaries, independent review, no self-approval, no automatic risk acceptance, evidence requirements, static-by-default behavior, prohibited unauthorized actions, stop conditions, no live integrations by default, and human approval gates intact.

## Validation

Repository validation can check Markdown frontmatter, area coverage, reference wording, file existence, duplicate or obsolete artifacts, empty files, and absence of fake agents, hooks, MCP runtime, credentials, or live integrations.

Runtime behavior, model availability, Project file limits, project knowledge RAG mode, memory behavior, Skill availability, sharing, connector behavior, scanner output, incident actions, recovery, and production changes require a separately authorized Claude environment and were not executed.

## Troubleshooting

- If Claude ignores area guidance, confirm `PROJECT_INSTRUCTIONS.md` was pasted into Project instructions rather than uploaded only as knowledge.
- If Claude cannot reference a workflow or template, upload the relevant files to the same Project knowledge base.
- If a Skill is unavailable, verify the account or workspace supports Skills and that the Skill was created, uploaded, installed, or shared in the current Claude surface.
- If connector results appear, confirm the connector was intentionally enabled and that its source-system permissions are approved.
- If shared users cannot see content, review Project visibility and sharing permissions.

## Removal Or Uninstall

Archive or delete the imported Claude Project, remove uploaded Project knowledge files, clear or replace Project instructions, and remove imported Skills from the Skill management surface. Disconnect connectors in Claude settings or ask a workspace administrator to disable them. Delete only the selected cybersecurity imports; do not remove unrelated organization evidence or global workspace settings without human approval.

## Limitations

This package is a static professional baseline, not a managed security service, scanner, SIEM, SOAR, EDR/XDR integration, penetration-testing platform, incident command system, recovery orchestrator, legal opinion, compliance certification, or production-control system. Claude plan limits, file limits, project knowledge RAG behavior, memory behavior, Skill availability, connector permissions, and admin controls can change.

## Security Notice

Explicit authorization and human control are mandatory for offensive testing, incident actions, production changes, external integrations, live scans, exploitation, deployment, recovery, publication, and sensitive evidence handling. Do not use this package to bypass approval, access secrets, contact external systems, or claim execution without evidence.
