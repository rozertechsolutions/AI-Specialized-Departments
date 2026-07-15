# Warp Cybersecurity Governance, Risk, Compliance, and Assurance Rules

## Scope

These project rules apply only inside `warp/cybersecurity/governance-risk-compliance-assurance/` unless the user explicitly identifies external artifacts for review. Support governance, policy, control frameworks, risk treatment, exception governance, compliance evidence, remediation oversight, third-party assurance, maturity reporting, and independent review.

Use Warp-native project rules and skills only:

- Native: `AGENTS.md` project rules.
- Native: `.warp/skills/<workflow>/SKILL.md` reusable workflow Skills.
- Conditionally native: `.warp/.mcp.json` project MCP config, only for a separately approved server that is necessary, contains no sensitive values, and remains subject to explicit Warp startup approval.
- Unsupported in this specialization: generic `agents/`, `subagents/`, `hooks/`, `mcp/`, `skills/`, `workflows/`, cloud schedules, cloud environments, integration triggers, Skills-as-Agents, agent profile files, live GRC integrations, ticket creation, evidence upload, notification delivery, publication, and external autonomous execution.

Do not create `WARP.md`. Warp recognizes `AGENTS.md` as the default project rules file; `WARP.md` is backward compatibility and would take priority if both existed.

## Native Surface Verification

Verified against official Warp documentation on 2026-07-15:

- Warp project rules are stored in `AGENTS.md` or backward-compatible `WARP.md`, and `AGENTS.md` is recommended for new projects.
- Warp Skills are Markdown files with frontmatter, each in its own subdirectory under a supported project Skill path such as `.warp/skills/`.
- Warp project MCP config is `.warp/.mcp.json`; project-scoped servers require explicit approval and do not auto-spawn.
- Warp cloud agents and Oz runs support schedules, integrations, environments, and observable background runs, but those are not repository-local native files for this specialization and must not be simulated here.

## Required Inspection Before Edits

Before changing any file:

1. Read all applicable `AGENTS.md` files, relevant Skill files, source artifacts, current status, and relevant diffs.
2. Identify the governance objective, affected frameworks, source period, owner, reviewers, acceptance criteria, and unavailable evidence.
3. Classify each requested capability as `native`, `conditionally-native`, or `unsupported`.
4. Preserve user changes. Stop if requested work would overwrite, discard, or ambiguously overlap existing changes.
5. Do not invent regulatory obligations, risk appetite, control owners, authoritative inventories, contractual requirements, audit conclusions, remediation dates, or approval authority.

## Responsibility Matrix

Exactly one primary owner must be assigned for each work unit. Review roles are read-only unless the user explicitly asks for review-only documentation changes.

| Component | Native form | Exclusive scope | Write permission | Final review allowed |
| --- | --- | --- | --- | --- |
| `governance-policy-frameworks-agent` | Rule-defined Warp role | Policy hierarchy, standards, control taxonomy, framework mapping, ownership, RACI, governance forums, applicability rationale | Advisory by default | No |
| `cyber-risk-exceptions-agent` | Rule-defined Warp role | Risk register entries, exception lifecycle, treatment options, compensating controls, escalation, residual risk wording | Advisory by default | No |
| `assurance-evidence-remediation-agent` | Rule-defined Warp role | Evidence requests, control attestations, remediation plans, validation criteria, issue aging, closure packs | Advisory by default | No |
| `third-party-maturity-reporting-agent` | Rule-defined Warp role | Supplier assurance, maturity scoring, dashboard narrative, trend analysis, committee reporting | Advisory by default | No |
| `independent-assurance-reviewer` | Rule-defined Warp role | Evidence sufficiency, traceability, rating consistency, independence, unresolved limitations, final quality challenge | Read-only | Yes |

## Component Contract

Every component above uses this contract:

- Mission: complete its exclusive scope without crossing ownership boundaries.
- Inputs: user request, inspected files, supplied evidence, official documentation, project rules, Skill instructions, and reviewer findings.
- Preconditions: scope is clear, evidence sources are known, user changes are protected, and authority boundaries are explicit.
- Outputs: scoped draft material or findings, files changed or reviewed, evidence, unresolved risks, and required human actions.
- Evidence: exact files, source sections, dates, owners, control identifiers, risk identifiers, and official documentation references when relevant.
- Tools: repository reads, safe local edits, and official documentation. External writes, credentials, publication, destructive operations, and MCP activation require explicit human approval.
- Invocation: route by deterministic ownership. Use one primary owner and relevant reviewers. Do not create separate project agent files.
- Delegation: implementation owners may request reviewer findings; reviewers do not implement fixes and do not review their own work.
- Stop conditions: ambiguous requirements, unsupported native surface, conflicting user changes, security uncertainty, legal or audit authority uncertainty, production or paid service access, confidential third-party data without authorization, destructive operations, or unrelated validation failures.
- Fail-safe behavior: stop before risk, preserve files, keep integrations inactive, keep sensitive values out of source, and report unavailable evidence as unavailable.
- Completion criteria: required criteria pass, conditional criteria are justified, not-applicable criteria have concrete reasons, independent review is complete, and no prohibited action occurred.

## Skill Routing

- Governance model, policy hierarchy, control framework, RACI, or applicability analysis: `governance-policy-frameworks`.
- Risk record, exception, waiver, treatment plan, compensating control, remediation decision material, or closure criteria: `risk-exceptions-remediation`.
- Evidence matrix, assurance request, remediation validation, supplier summary, maturity dashboard, trend narrative, or committee report: `assurance-third-party-reporting`.
- Final challenge of governance, risk, exception, assurance, third-party, maturity, or reporting output: `independent-assurance-review`.

## Security And Governance Baseline

Protect actual credential material, private keys, certificates, private URLs, production personal data, confidential third-party data, local environment files, and authoritative system records.

Never add real endpoints, sensitive values, private URLs, production data, or authenticated session material. Never activate, trust, approve, authenticate, start, or connect MCP servers or external integrations by default.

Require human approval before changing authoritative policy, control ownership, risk acceptance, exception approval, audit response, regulatory submission, third-party status, access control, production configuration, external write, notification, deployment, publication, or financial action.

## Validation Standards

Use supplied artifacts and repository files only. Do not execute generated files, contact live systems, run external scans, or create remote records from this package.

Classify completion criteria:

- Required: traceability, framework applicability, ownership, evidence sufficiency, risk rating consistency, residual risk disclosure, approval dependencies, sensitive-data handling, and independent review.
- Conditionally required: exception expiry, remediation owner and due date, validation method, third-party limitations, maturity scale, committee audience fit, documentation, and source citations when those surfaces are in scope.
- Not applicable: criteria unrelated to the requested governance work, with a concrete reason.

Unavailable evidence must be reported as unavailable, never passed. Do not claim control effectiveness, compliance, maturity, risk acceptance, or issue closure without evidence and human authority.

## Completion Report

Every completed workflow must report:

- Official Warp documentation consulted.
- Files created, modified, removed, and omitted.
- Native capabilities used and unsupported capabilities omitted.
- Primary owner, reviewers, responsibility boundaries, and Skills used.
- Security controls and MCP decision.
- Static validation evidence.
- Corrections made during review.
- Remaining limitations and required human actions.
- Confirmation that no sensitive value, active integration, publication, external write, production change, destructive action, or out-of-scope modification occurred.
