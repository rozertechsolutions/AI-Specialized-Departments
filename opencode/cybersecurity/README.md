# OpenCode Cybersecurity Department

This Cybersecurity department is a professional OpenCode configuration package covering governance, risk, compliance, assurance, security architecture and engineering, application/product/DevSecOps security, exposure and hardening, defensive operations and intelligence, incident response and recovery, authorized offensive validation, and resilience or specialized technology security.

It solves the problem of opening a bounded cybersecurity area in OpenCode with area instructions, subagents, Skills, custom commands, and conservative permissions already colocated in the area directory. Possible uses include policy review, control mapping, risk exception support, architecture review, threat modeling, secure SDLC review, vulnerability prioritization, detection planning, incident readiness, authorized validation planning, resilience review, and independent assurance.

## Department Overview

The department contains eight area packages under `opencode/cybersecurity/<area>/`. Each area is an isolated OpenCode project root with `AGENTS.md`, `opencode.jsonc`, `.opencode/agents/`, `.opencode/commands/`, and `.opencode/skills/`.

OpenCode can assist with static repository review, drafting, evidence organization, and handoff planning. It is not authorized to accept enterprise risk, approve exceptions, authorize offensive testing, approve production changes, declare or close incidents, make legal determinations, certify compliance, operate live security tooling, or act without a human accountable owner.

## Possible Uses

- Start OpenCode in one cybersecurity area for area-scoped analysis.
- Use `AGENTS.md` as the area instruction source.
- Invoke named subagents with `@subagent-name` for specialized static review.
- Invoke custom commands with `/command-name` for repeatable prompt workflows.
- Load area Skills from `.opencode/skills/` according to OpenCode Skill permissions.

## Platform Compatibility

Validated on 2026-07-21 against current OpenCode documentation and `https://opencode.ai/config.json`.

Supported OpenCode surfaces:

- Project instructions through `AGENTS.md`.
- Project config through JSON/JSONC config files.
- Per-project `.opencode/agents/*.md` Markdown agents.
- Per-project `.opencode/commands/*.md` custom command files.
- Per-project `.opencode/skills/*/SKILL.md` Agent Skills.
- Permission controls through the current `permission` config.
- MCP configuration through `mcp`, intentionally empty in this package.

OpenCode is a coding-agent CLI. This package does not configure providers, models, credentials, remote MCP servers, local MCP servers, plugins, LSP servers, formatters, hooks, or production integrations.

## Prerequisites

- OpenCode installed by the user outside this repository.
- A trusted local checkout.
- A provider/model configured by the user outside this package if OpenCode requires one.
- Human authorization for the selected cybersecurity scope and any supplied evidence.

No API keys, credentials, connectors, scanners, cloud accounts, MCP servers, or production access are included in this package.

## Installation Or Import

Use one area at a time.

1. Open a terminal at the repository root.
2. Change into the selected area, for example:

   ```text
   cd opencode/cybersecurity/governance-risk-compliance-assurance
   ```

3. Start OpenCode from that area directory using the user's normal OpenCode launch command.
4. Confirm OpenCode loads the area `AGENTS.md`, `opencode.jsonc`, and `.opencode/` directory.
5. Provide redacted static evidence and an explicit scope.

Do not start from `opencode/cybersecurity/` if the intent is strict area isolation. Start from the area directory so the nearest `AGENTS.md`, area `opencode.jsonc`, and area `.opencode/` files are the active project artifacts.

## Working Directory And Discovery

Launch directory:

```text
opencode/cybersecurity/<area>/
```

Auto-discovered or project-loaded by OpenCode from that area:

- `AGENTS.md` for project rules.
- `opencode.jsonc` for area permissions and empty MCP config.
- `.opencode/agents/*.md` for Markdown agents.
- `.opencode/commands/*.md` for custom commands.
- `.opencode/skills/*/SKILL.md` for Skills.

OpenCode rule precedence checks local `AGENTS.md` or compatible rule files by traversing upward from the current directory, then global files. OpenCode config merges remote, global, custom, project, `.opencode`, and inline configuration, with later config overriding conflicting keys. The eight identical `opencode.jsonc` files are retained intentionally because each area is an isolated runnable project root.

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

- `AGENTS.md`: area instructions loaded as project rules.
- `opencode.jsonc`: area config with read/search/list allowed, Skill loading allowed, edit requiring approval, bash denied, webfetch/websearch denied, task/todo actions denied, external directories denied, and no MCP servers.
- `.opencode/agents/*.md`: current Markdown subagents with `description`, `mode: subagent`, `temperature`, and documented `permission` keys.
- `.opencode/commands/*.md`: user-invoked slash-command prompt files.
- `.opencode/skills/*/SKILL.md`: Agent Skills.

No hooks, plugins, providers, models, MCP servers, scanner connectors, or live app integrations are included.

## How To Use The Department

Select the area that owns the work, launch OpenCode from that area, and provide:

- authorized scope and explicit exclusions;
- accountable owner, requester, reviewer, approver role, and intended audience;
- evidence inventory with provenance, period, freshness, and limitations;
- decision needed, assumptions, constraints, and required output.

Example input:

```text
@governance-policy-frameworks-agent use /governance-policy-frameworks to review the supplied access-control policy draft. Scope is static review only. Exclude publication and external submission. Return control mappings, ambiguity, evidence gaps, required approvers, and independent-review requirements.
```

Expected output is a scoped artifact with evidence tables, findings separated by evidence state, assumptions, limitations, confidence, residual risk, required human decisions, and completion criteria. High-impact, closure-facing, exception, release, incident, offensive, or external-facing outputs must go to an independent reviewer that did not create the artifact.

Stop when authorization is missing, evidence is unredacted or insufficient, scope is unclear, a live action is requested, an output would self-review, or a human-only decision is requested.

## Permissions And Safety

The area `opencode.jsonc` and agent frontmatter use current OpenCode `permission` keys:

- `read`, `list`, `glob`, and `grep`: `allow`.
- `skill`: `allow`.
- `edit`: `ask`.
- `bash`, `webfetch`, `websearch`, `external_directory`, `task`, and `todowrite`: `deny`.
- `mcp`: `{}`.

Auto mode does not override explicit `deny` rules. Any static repository edit still requires a human approval prompt and must remain inside the selected area. Do not add MCP servers, plugins, providers, credentials, scanner commands, deployment commands, or external references unless a human explicitly approves them in the consuming environment.

Human approval is required for risk acceptance, exception approval, policy publication, architecture approval, release readiness, incident declaration or closure, external distribution, supplier decisions, offensive authorization, production recovery, and critical finding closure.

## Configuration And Customization

### Project-dependent configuration

Adapt repository paths, source directories, application architecture, build systems, languages, deployment model, cloud provider, CI/CD structure, telemetry locations, asset inventory, data-flow scope, threat-model scope, vulnerability evidence, approved test scope, area-specific working directories, and repository-specific policies per project.

### User/organization-dependent configuration

Supply or approve OpenCode installation, provider/model configuration, account identity, organization policies, regulatory frameworks, risk appetite, asset criticality, SLAs, escalation contacts, approval authorities, permitted tools, permitted integrations, API credentials, MCP endpoints, cloud accounts, SIEM/EDR/XDR/SOAR systems, ticketing systems, incident contacts, authorized offensive-testing scope, retention rules, and legal/privacy constraints outside this repository. Do not commit secrets or confidential values.

### Fixed baseline configuration

Keep area ownership boundaries, independent review, no self-approval, no automatic risk acceptance, evidence requirements, static-by-default behavior, prohibited unauthorized actions, stop conditions, denied live integrations, denied shell/web/task behavior, empty MCP config, and human approval gates intact.

## Validation

Repository validation can check JSON/JSONC parsing, current OpenCode config schema compatibility, Markdown frontmatter, area coverage, file existence, exact duplicates, empty files, empty directories, and absence of providers, credentials, MCP servers, plugins, hooks, and live integrations.

Runtime behavior, provider/model behavior, OpenCode UI behavior, app/plugin behavior, scanner output, incident actions, recovery, and production changes require a separately authorized runtime and were not executed.

## Troubleshooting

- If area instructions are not loaded, confirm OpenCode was launched from `opencode/cybersecurity/<area>/`.
- If a subagent is unavailable, confirm the file exists under `.opencode/agents/` and has `mode: subagent`.
- If a command is unavailable, confirm the Markdown file exists under `.opencode/commands/` and invoke it as `/file-name`.
- If a Skill is hidden or rejected, inspect `permission.skill` in `opencode.jsonc`.
- If an MCP tool appears, inspect merged remote/global/user config; this package defines no MCP servers.
- If permissions appear broader than intended, inspect OpenCode's merged config because remote, global, custom, project, `.opencode`, and inline config are merged.

## Removal Or Uninstall

Stop OpenCode, delete or stop using the selected `opencode/cybersecurity/<area>/` import, or remove that area's `AGENTS.md`, `opencode.jsonc`, and `.opencode/` files from a copied consuming project. Remove user/global provider, model, MCP, plugin, or credential configuration from OpenCode's user settings only through the user's approved process. Do not delete unrelated organization evidence or global OpenCode settings without human approval.

## Limitations

This package is a static professional baseline for OpenCode, not a managed security service, scanner, SIEM, SOAR, EDR/XDR integration, penetration-testing platform, incident command system, recovery orchestrator, legal opinion, compliance certification, or production-control system. OpenCode configuration, permission keys, Skill behavior, and `.opencode` discovery can change.

## Security Notice

Explicit authorization and human control are mandatory for offensive testing, incident actions, production changes, external integrations, live scans, exploitation, deployment, recovery, publication, and sensitive evidence handling. Do not use this package to bypass approval, access secrets, contact external systems, or claim execution without evidence.
