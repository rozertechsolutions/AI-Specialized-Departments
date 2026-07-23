# Cybersecurity Department for Claude Code

This Cybersecurity department is a Claude Code repository package for static, human-reviewed cybersecurity work. It helps teams use Claude Code subagents, Skills, commands, and `CLAUDE.md` instructions to produce evidence-based artifacts without granting the AI authority to approve risk, run live security actions, or act on production systems.

Possible uses include governance, risk, compliance, and assurance support; security architecture and engineering review; application, product, and DevSecOps security review; exposure, vulnerability, and hardening planning; defensive operations, detection, and threat-intelligence analysis; incident response, DFIR, and recovery planning; explicitly authorized offensive validation planning; and resilience or specialized-technology assurance.

## Department overview

The department contains eight isolated Claude Code project packages under `claude-code/cybersecurity/<area>/`. Each area contains `CLAUDE.md`, Claude Code subagents under `.claude/agents/`, Skills under `.claude/skills/`, and slash-command prompt files under `.claude/commands/`.

The package supports static analysis, planning, review, documentation, and assurance from supplied evidence. It does not authorize live scanning, exploitation, containment, recovery execution, production changes, publication, external integrations, legal determinations, risk acceptance, or closure decisions. Human owners remain accountable for authorization, approvals, exceptions, risk acceptance, incident declaration or closure, offensive testing authorization, and production action.

## Possible uses

- Open a specific area package and ask a Claude Code subagent to review supplied redacted evidence.
- Invoke a canonical Skill such as `/governance-policy-frameworks`, `/threat-modeling`, or `/incident-readiness-triage`.
- Use command prompts in `.claude/commands/` as user-invoked workflows for evidence review and independent assurance.
- Route high-impact outputs to an independent reviewer subagent while preserving human approval gates.

## Platform compatibility

Surface: Claude Code CLI repository configuration. The package relies on current Claude Code support for project `CLAUDE.md`, `.claude/agents/*.md`, `.claude/skills/*/SKILL.md`, `.claude/commands/*.md`, `.claude/settings.json`, permissions, hooks where configured, and MCP where configured.

Validated documentation date: 2026-07-21. Current Claude Code subagent frontmatter supports fields such as `name`, `description`, `tools`, `disallowedTools`, `model`, `permissionMode`, `skills`, `mcpServers`, hooks, memory, isolation, and related current fields. `readonly` is not a supported subagent frontmatter field and is not used.

## Prerequisites

- Claude Code installed locally.
- The repository trusted by the user before use.
- Launch from the selected area directory for strongest area isolation.
- No credentials, MCP servers, connectors, scanners, or cloud accounts are required for this package.

Do not place credentials, tokens, keys, private endpoints, personal data, confidential customer data, or live system access material in this package.

## Installation or import

Keep this tree in the repository. To use a single area, launch Claude Code from that area:

```bash
cd claude-code/cybersecurity/governance-risk-compliance-assurance
claude
```

Then invoke a retained command or Skill:

```text
/governance-policy-frameworks
```

Example input:

```text
Authorized scope: review the supplied redacted policy and control evidence for gaps against the organization's approved framework mapping. Owner: GRC lead. Reviewer: independent assurance reviewer. No live systems, connectors, or scans are authorized.
```

Expected output is a static scoped artifact with evidence states, assumptions, limitations, residual risk, confidence, required human decisions, and independent-review status.

## Working directory and discovery

Start Claude Code from `claude-code/cybersecurity/<area>/` when using one area. Claude Code reads `CLAUDE.md` project memory and discovers project `.claude/` configuration from the current project context. Skills are available from `.claude/skills/*/SKILL.md`; commands in `.claude/commands/*.md` remain supported, though current Claude Code documentation recommends Skills for new command-like workflows.

Subagents are defined in `.claude/agents/*.md`. They can be selected by Claude through the Agent tool, launched where Claude Code supports `--agent`, or referenced according to current Claude Code UI/CLI behavior. The `skills` frontmatter field preloads listed Skills into subagent context; it does not limit all Skill access by itself.

Area isolation depends on launching from the selected area directory. Do not launch from `claude-code/cybersecurity/` if you intend only one area to be discoverable.

## Area map

- `claude-code/cybersecurity/governance-risk-compliance-assurance/` - Governance, cyber risk, compliance mapping, policies, assurance, exceptions, and risk-decision support.
- `claude-code/cybersecurity/security-architecture-engineering/` - Security architecture, engineering patterns, identity, network, cloud, data, platform, and control design review.
- `claude-code/cybersecurity/application-product-devsecops-security/` - Product security, secure SDLC, threat modeling, code/design review, CI/CD, supply chain, PSIRT, and release assurance.
- `claude-code/cybersecurity/exposure-vulnerability-hardening/` - Asset exposure, vulnerability triage, prioritization, hardening, remediation governance, and validation evidence.
- `claude-code/cybersecurity/defensive-security-operations-detection-intelligence/` - SOC operating model, telemetry, detection engineering, alert triage, hunting, intelligence, and coverage quality.
- `claude-code/cybersecurity/incident-response-dfir-recovery/` - Incident planning, evidence governance, DFIR planning, containment planning, recovery coordination, and lessons learned.
- `claude-code/cybersecurity/offensive-security-authorized-validation/` - Explicitly authorized assessment planning, rules of engagement, emulation governance, retest planning, and safety review.
- `claude-code/cybersecurity/cyber-resilience-specialized-technologies/` - Resilience, ransomware recovery planning, OT/ICS, IoT/embedded, AI security, hardware/firmware, cryptographic agility, and critical-infrastructure assurance.

## Native components

Each area contains:

- `CLAUDE.md` - area-scoped project memory and operating rules.
- `.claude/agents/*.md` - Claude Code subagents with `permissionMode: plan`, read/search tool allowlists, deny lists for write/shell/network/MCP tools, and preloaded canonical Skills.
- `.claude/skills/*/SKILL.md` - retained canonical Skills referenced by agents and commands.
- `.claude/commands/*.md` - legacy command prompt files that delegate to retained Skills.
- `.claude/settings.json` - present only in high-risk areas that need extra project-level deny rules for Bash, WebFetch, and MCP.

## How to use the department

Select the area that owns the requested work, launch Claude Code from that area, and provide authorized scope, exclusions, accountable owner, requester, intended audience, evidence inventory, assumptions, constraints, reviewer, approver role, and the human decision being supported.

Use a command such as `/threat-modeling`, a Skill such as `/independent-offensive-safety-review`, or ask Claude Code to use the appropriate subagent for a scoped static review. High-impact outputs must go to an independent reviewer that did not create the work. Stop when authorization is missing, sensitive data is unredacted, scope is unclear, a live action is requested, evidence is insufficient for a conclusion, or self-review would occur.

## Permissions and safety

Subagents use `permissionMode: plan`, `tools: [Read, Grep, Glob]`, and `disallowedTools` for write, edit, shell, web, and MCP tools. Claude Code parent-session permission mode and organization-managed settings can still take precedence, so users must keep the parent session in a safe mode and deny unexpected prompts.

Default use is static and read-only. Shell, network, installation, deployment, scanning, exploitation, recovery execution, remote Git operations, MCP connections, hosted tools, and external connectors are prohibited by this baseline. Claude Code may prompt for additional permissions if a user asks for broader action; deny those prompts unless a separate authorized change request exists.

## Configuration and customization

### Project-dependent configuration

Adapt repository paths, source directories, application architecture, build systems, technology stack, deployment model, CI/CD structure, telemetry locations, assets, threat-model scope, approved targets, evidence locations, area working directories, and repository-specific policies inside the selected area.

### User/organization-dependent configuration

Supply account, subscription, user identity, organization policies, frameworks, risk appetite, asset criticality, SLAs, escalation contacts, approval authorities, permitted tools, permitted integrations, API credentials, MCP endpoints, cloud accounts, SIEM/EDR/XDR/SOAR systems, ticketing systems, incident contacts, authorized offensive-testing scope, data-retention requirements, and legal/privacy constraints outside this repository. Real secrets and confidential values must not be committed.

### Fixed baseline configuration

Keep area ownership boundaries, independent review, no self-approval, no automatic risk acceptance, evidence requirements, read-only subagent allowlists, MCP absence by default, prohibited unauthorized actions, stop conditions, and human-approval gates unless a formal governance review approves a change.

## Validation

Static validation can check Markdown frontmatter, JSON settings, native paths, agent Skill references, command Skill references, duplicate or obsolete Skills, empty artifacts, broken references, and absence of unsupported fields such as `readonly`. Runtime behavior, model behavior, permission prompts, hooks, MCP, connectors, scans, incident action, recovery, and production integration require a separate authorized Claude Code session and were not executed by this repository validation.

## Troubleshooting

- If a subagent is not available, confirm Claude Code was launched from the intended area directory and the file exists under `.claude/agents/*.md`.
- If a Skill is not available, confirm the directory is `.claude/skills/<skill-name>/SKILL.md` and the frontmatter `name` matches the directory.
- If a command is not available, check `.claude/commands/*.md`; current Claude Code also exposes Skills as slash commands.
- If a subagent attempts broader action, inspect parent permission mode and managed settings; `permissionMode: plan` can be overridden by parent modes documented by Claude Code.
- If an old Skill name no longer appears, use the retained canonical Skill listed in the relevant command or subagent `skills` field.

## Removal or uninstall

Remove this package by deleting `claude-code/cybersecurity/` from the repository, or remove individual area packages by deleting `claude-code/cybersecurity/<area>/`. To disable one component without deleting the whole area, remove the corresponding `.claude/agents/`, `.claude/skills/`, `.claude/commands/`, or `.claude/settings.json` file from the area and restart Claude Code. Do not delete organizational evidence or platform-global settings unless a human owner explicitly authorizes that cleanup.

## Limitations

This package is a static professional baseline. It is not a managed security service, scanner, SIEM, SOAR, EDR/XDR integration, penetration-testing tool, incident-response platform, legal opinion, compliance certification, or production-control system. Claude Code subagent and permission behavior can change across releases, and organization-managed settings may override project-local behavior.

## Security notice

Offensive testing, incident actions, production changes, external integrations, live scans, exploitation, deployment, recovery, publication, and use of sensitive evidence require explicit authorization, validated scope, and human control. Do not use these components to bypass approval, access secrets, contact external systems, or claim live execution without evidence.
