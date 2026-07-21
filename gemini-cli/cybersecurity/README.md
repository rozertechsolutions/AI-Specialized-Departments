# Cybersecurity Department for Gemini CLI

This Cybersecurity department is a Gemini CLI repository package for static, human-reviewed cybersecurity work. It helps teams use Gemini CLI `GEMINI.md`, custom subagents, Agent Skills, and command prompts to produce evidence-based artifacts without granting the AI authority to approve risk, run live security actions, or act on production systems.

Possible uses include governance, risk, compliance, and assurance support; security architecture and engineering review; application, product, and DevSecOps security review; exposure, vulnerability, and hardening planning; defensive operations, detection, and threat-intelligence analysis; incident response, DFIR, and recovery planning; explicitly authorized offensive validation planning; and resilience or specialized-technology assurance.

## Department overview

The department contains eight isolated Gemini CLI project packages under `gemini-cli/cybersecurity/<area>/`. Each area contains `GEMINI.md`, custom agents under `.gemini/agents/`, Agent Skills under `.gemini/skills/`, and command prompt files under `.gemini/commands/`.

The package supports static analysis, planning, review, documentation, and assurance from supplied evidence. It does not authorize live scanning, exploitation, containment, recovery execution, production changes, publication, external integrations, legal determinations, risk acceptance, or closure decisions. Human owners remain accountable for authorization, approvals, exceptions, risk acceptance, incident declaration or closure, offensive testing authorization, and production action.

## Possible uses

- Launch Gemini CLI from a specific area package and use the area `GEMINI.md` as persistent project guidance.
- Invoke a custom subagent with `@agent-name` for scoped static review.
- Use workspace Skills such as `/threat-modeling`, `/exposure-lifecycle-triage`, or `/independent-offensive-safety-review`.
- Use command prompt files in `.gemini/commands/` as user-invoked workflows that delegate to retained Skills.

## Platform compatibility

Surface: Gemini CLI, not Gemini API alone, Gemini Code Assist IDE configuration, or a generic Markdown package.

Current official Gemini CLI documentation supports custom agent files in `.gemini/agents/*.md` and user agents in `~/.gemini/agents/*.md`. Supported agent frontmatter includes `name`, `description`, `kind`, `tools`, `mcpServers`, `model`, `temperature`, `max_turns`, and `timeout_mins`. This package does not use unsupported `readonly` or agent-level `skills` fields.

Gemini CLI Agent Skills are discovered separately from `.gemini/skills/` and `.agents/skills/`. The retained Skills live in `.gemini/skills/` under each area. Agents do not preload Skills through frontmatter.

## Prerequisites

- Gemini CLI installed by the user, usually with `npm install -g @google/gemini-cli` or another documented installer.
- A trusted repository/workspace.
- Account, API key, Vertex AI, or Google sign-in setup handled outside this package when the user intentionally runs Gemini CLI.
- No credentials, MCP servers, browser automation, scanners, or cloud accounts are required for this repository package.

Do not place credentials, tokens, keys, private endpoints, personal data, confidential customer data, or live system access material in this package.

## Installation or import

Keep this tree in the repository. To use a single area, launch Gemini CLI from that area:

```bash
cd gemini-cli/cybersecurity/application-product-devsecops-security
gemini
```

Invoke a retained Skill or direct a custom subagent:

```text
/threat-modeling
```

```text
@requirements-threat-modeling-agent Review the supplied architecture notes for static threat-model gaps. Authorized scope: this repository and redacted evidence only. Do not run shell commands, browse, connect MCP, scan, or write files.
```

Expected output is a static scoped artifact with evidence states, assumptions, limitations, residual risk, confidence, required human decisions, and independent-review status.

## Working directory and discovery

Start Gemini CLI from `gemini-cli/cybersecurity/<area>/` when using one area. Gemini CLI discovers:

- `GEMINI.md` as persistent workspace guidance;
- `.gemini/agents/*.md` as project custom agents;
- `.gemini/skills/*/SKILL.md` as workspace Agent Skills;
- `.gemini/commands/*.md` as repository command prompt files where supported by the installed CLI.

Subagents use their own isolated context and only the tools granted in the agent frontmatter. Skills are discovered independently and activated through Gemini CLI's Skill mechanism with user consent. Area isolation depends on launching from the selected area directory.

## Area map

- `gemini-cli/cybersecurity/governance-risk-compliance-assurance/` - Governance, cyber risk, compliance mapping, policies, assurance, exceptions, and risk-decision support.
- `gemini-cli/cybersecurity/security-architecture-engineering/` - Security architecture, engineering patterns, identity, network, cloud, data, platform, and control design review.
- `gemini-cli/cybersecurity/application-product-devsecops-security/` - Product security, secure SDLC, threat modeling, code/design review, CI/CD, supply chain, PSIRT, and release assurance.
- `gemini-cli/cybersecurity/exposure-vulnerability-hardening/` - Asset exposure, vulnerability triage, prioritization, hardening, remediation governance, and validation evidence.
- `gemini-cli/cybersecurity/defensive-security-operations-detection-intelligence/` - SOC operating model, telemetry, detection engineering, alert triage, hunting, intelligence, and coverage quality.
- `gemini-cli/cybersecurity/incident-response-dfir-recovery/` - Incident planning, evidence governance, DFIR planning, containment planning, recovery coordination, and lessons learned.
- `gemini-cli/cybersecurity/offensive-security-authorized-validation/` - Explicitly authorized assessment planning, rules of engagement, emulation governance, retest planning, and safety review.
- `gemini-cli/cybersecurity/cyber-resilience-specialized-technologies/` - Resilience, ransomware recovery planning, OT/ICS, IoT/embedded, AI security, hardware/firmware, cryptographic agility, and critical-infrastructure assurance.

## Native components

Each area contains:

- `GEMINI.md` - area-scoped persistent instructions.
- `.gemini/agents/*.md` - native custom subagents using `kind: local`, `model: inherit`, conservative turn/time limits, and native read-only tool IDs.
- `.gemini/skills/*/SKILL.md` - retained workspace Skills referenced by commands and discoverable by Gemini CLI.
- `.gemini/commands/*.md` - command prompt files that delegate to retained Skills.

## How to use the department

Select the area that owns the requested work, launch Gemini CLI from that area, and provide authorized scope, exclusions, accountable owner, requester, intended audience, evidence inventory, assumptions, constraints, reviewer, approver role, and the human decision being supported.

Use a Skill, a command prompt, or an `@agent-name` subagent invocation. High-impact outputs must go to an independent reviewer that did not create the work. Stop when authorization is missing, sensitive data is unredacted, scope is unclear, a live action is requested, evidence is insufficient for a conclusion, or self-review would occur.

## Permissions and safety

Subagents use only native read-only tool identifiers:

```yaml
tools: [read_file, grep_search, glob, list_directory]
```

They do not include write, replace, shell, web, browser, MCP, or remote-agent tools. Gemini CLI's policy engine can add user or organization deny/ask rules for tools such as `run_shell_command`, `write_file`, `replace`, web/browser tools, and `mcp_*`; this repository does not install those user-global policies.

Default use is static and read-only. Shell, network, installation, deployment, scanning, exploitation, recovery execution, remote Git operations, MCP connections, hosted tools, browser automation, and external connectors are prohibited by this baseline.

## Configuration and customization

### Project-dependent configuration

Adapt repository paths, source directories, application architecture, build systems, technology stack, deployment model, CI/CD structure, telemetry locations, assets, threat-model scope, approved targets, evidence locations, area working directories, and repository-specific policies inside the selected area.

### User/organization-dependent configuration

Supply account, subscription, user identity, organization policies, frameworks, risk appetite, asset criticality, SLAs, escalation contacts, approval authorities, permitted tools, permitted integrations, API credentials, MCP endpoints, cloud accounts, SIEM/EDR/XDR/SOAR systems, ticketing systems, incident contacts, authorized offensive-testing scope, data-retention requirements, and legal/privacy constraints outside this repository. Real secrets and confidential values must not be committed.

### Fixed baseline configuration

Keep area ownership boundaries, independent review, no self-approval, no automatic risk acceptance, evidence requirements, native read-only tool allowlists, MCP absence by default, prohibited unauthorized actions, stop conditions, and human-approval gates unless a formal governance review approves a change.

## Validation

Static validation can check Markdown frontmatter, native tool IDs, agent Skill-field absence, command Skill references, retained Skill structure, duplicate or obsolete Skills, empty artifacts, broken references, and absence of unsupported fields such as `readonly`. Runtime behavior, model behavior, Skill activation consent, policy engine enforcement, MCP, remote agents, browser agents, scans, incident action, recovery, and production integration require a separate authorized Gemini CLI session and were not executed by this repository validation.

## Troubleshooting

- If a subagent is not available, confirm Gemini CLI was launched from the intended area directory and the file exists under `.gemini/agents/*.md`.
- If a subagent errors on tools, confirm it uses native tool IDs such as `read_file`, `grep_search`, `glob`, and `list_directory`.
- If a Skill is not available, confirm the directory is `.gemini/skills/<skill-name>/SKILL.md`; workspace Skills can also be managed with Gemini CLI's `/skills` or `gemini skills` commands.
- If a command is not available, use the equivalent retained Skill directly.
- If broader tool access appears, inspect user or organization Gemini CLI settings and policy-engine rules.

## Removal or uninstall

Remove this package by deleting `gemini-cli/cybersecurity/` from the repository, or remove individual area packages by deleting `gemini-cli/cybersecurity/<area>/`. To disable one component without deleting the whole area, remove the corresponding `.gemini/agents/`, `.gemini/skills/`, `.gemini/commands/`, or `GEMINI.md` file from the area and restart Gemini CLI. Do not delete user-global Gemini CLI settings or policies unless a human owner explicitly authorizes that cleanup.

## Limitations

This package is a static professional baseline. It is not a managed security service, scanner, SIEM, SOAR, EDR/XDR integration, penetration-testing tool, incident-response platform, legal opinion, compliance certification, or production-control system. Gemini CLI feature availability varies by installed release, account/provider mode, trusted folder state, policy-engine configuration, and preview/stable channel.

## Security notice

Offensive testing, incident actions, production changes, external integrations, live scans, exploitation, deployment, recovery, publication, and use of sensitive evidence require explicit authorization, validated scope, and human control. Do not use these components to bypass approval, access secrets, contact external systems, or claim live execution without evidence.
