# Warp / Oz — Web Development Correction Prompt

*AI Specialized Departments — Independent Platform Prompt*

| Prompt type | Standalone correction and completion prompt |
| --- | --- |
| Target | warp/web-development/ |
| Execution mode | Static repository editing only; no virtual environment or software execution |
| Documentation baseline | Current official sources at execution time; Reddit secondary only |

## 1. Mission

Correct and complete the existing Web Development specialization for this platform only. The result must use current, real, project-scoped native capabilities, remove unsupported or misleading artifacts, repair all audit findings, and leave the platform package internally coherent, safe by default, and professionally complete.

`TARGET_DIRECTORY = warp/web-development/`

**Target product surface:** Warp local agents and current Oz platform rules, Skills, codebase context, MCP, saved prompts/workflows, and cloud automation only where explicitly selected. This package must remain local/static and must not configure Oz cloud runs.

## 2. Immutable execution boundaries

- Work only inside the target directory named in this document. Do not inspect, create, modify, rename, or delete files in any other platform or specialization.
- You may use web research only to consult current official product documentation. High-signal Reddit discussions may be used as secondary evidence for practical limitations, but never as authority over official documentation.
- Do not use a terminal, shell, command execution, scripts, builds, tests, package managers, installers, Git, external authentication, connected services, deployments, publishing, or any other software execution. This platform does not require a Python virtual environment, and this prompt does not authorize creating one.
- Create, modify, move, or delete only static configuration, instruction, documentation, schema, or SDK source files required by this platform package.
- Do not create or add audit reports, validation reports, execution reports, evidence reports, completion reports, manifests, logs, or equivalent artifacts in any format. Do not write the final result into the repository. The final result must be shown only in the visible on-screen response.
- Do not create a common directory, cross-platform adapter, converter, shared runtime, installer, migration utility, or compatibility shim.
- Do not copy another platform's folder structure. Native conceptual consistency is required; identical structures are not.
- Do not retain empty files, placeholder-only files, empty MCP objects, dummy integrations, simulated agents, simulated hooks, or unsupported configuration keys.
- Do not add secrets, tokens, credentials, real endpoints, private URLs, account identifiers, environment-specific paths, or enabled external integrations.
- Do not weaken human approval requirements. Production, authentication, authorization, sensitive data, dependency changes, third-party scripts, trackers, deployment, publication, spending, signing, submission, destructive actions, and Git mutations require explicit human review.
- Do not claim that builds, tests, runtime behavior, browser behavior, integrations, or platform loading were verified unless there is direct evidence. This task is limited to static generation and static verification.
## 3. Mandatory research gate

1. Identify the current product surface and configuration format as of the execution date before editing any file.
1. Use official documentation as the primary source. Record the exact documentation pages or official repository references used in the final on-screen result.
1. For every existing or proposed component, classify it internally as native, conditionally native, manual-only, or unsupported.
1. Delete unsupported components completely. Do not preserve them for symmetry or future possibilities.
1. When official documentation is ambiguous, choose the safest minimal implementation and state the limitation in the final on-screen result. Do not invent behavior.
1. Treat Reddit only as secondary operational evidence. Use established communities, recent posts, reproducible details, and maintainer responses where available.
**Official documentation baseline to verify:** Warp Docs: Agents overview; Warp Docs: Skills for agents; Warp Docs: Rules; Warp Docs: MCP and Oz Platform only to document intentional omission.

## 4. Known audit findings to correct

- The current package uses AGENTS.md and Agent Skills, which are plausible native context mechanisms, but the content is generic and does not define the exact Warp/Oz product surface.
- Warp now spans local agents and Oz cloud orchestration; the package must not silently mix them.
- No custom subagent files are currently justified for Warp's repository configuration.
- MCP, integrations, schedules, and cloud runs would require external trust and are prohibited.
## 5. Required platform-native corrections

1. Declare the target surface in README.md: project-scoped guidance and Skills for Warp's interactive/local agent experience. Do not configure Oz cloud automation.
1. Validate AGENTS.md support and keep it concise, location-based, and non-duplicative.
1. Validate .agents/skills discovery for Warp. Retain distinct instruction-only Skills and ensure workflow Skills are genuinely useful through Warp's Skill invocation model.
1. Do not create custom agent/subagent manifests unless current official Warp documentation defines a repository-scoped custom-agent format. Do not simulate a multi-agent department.
1. Do not create .warp/.mcp.json, Warp Drive IDs, saved prompt IDs, workflows requiring cloud objects, environments, schedules, integrations, API/SDK code, or Oz commands.
1. Rewrite README.md to explain manual Skill invocation, local versus cloud limitations, unsupported automation, and human-review boundaries.
1. Expand Skills with inputs, outputs, evidence, failure states, and stop conditions. Avoid exact copies of other platforms.
1. Keep all deployment, Git, command execution, and external actions prohibited.
1. Use the professional role model conceptually within instructions only; do not label static Skills as autonomous agents.
## 6. Native capability boundary

### Retain or create only when verified native

- AGENTS.md
- .agents/skills/*/SKILL.md
- Warp local agent context and manual Skill use
### Omit or delete

- Oz cloud runs
- Schedules
- Integrations
- MCP
- Warp Drive object IDs
- API/SDK
- Simulated custom subagents
## 7. Professional department coverage to preserve

- Stack discovery and preservation across HTML, CSS, JavaScript, TypeScript, frontend frameworks, server runtimes, APIs, storage, and existing project conventions.
- Web architecture decisions covering frontend, backend, full-stack boundaries, rendering strategy, API contracts, sessions, storage, integrations, and deployment readiness without performing deployment.
- Frontend implementation guidance for semantics, responsive behavior, state, forms, error states, progressive enhancement, and browser compatibility.
- Backend and API guidance for contracts, validation, authentication, authorization, sessions, cookies, CORS, persistence, integrations, and failure handling.
- Independent security and privacy review covering secrets, data minimization, CSP, cookies, CORS, supply chain, trackers, third-party scripts, and sensitive flows.
- Independent accessibility, performance, responsive design, SEO, metadata, rendering, resilience, and user-impact review.
- Independent quality and release-readiness review covering requirement traceability, static evidence, test expectations, browser support, observability readiness, documentation, risks, and unresolved blockers.
Do not force one role into a separate agent when the platform does not support agents or when a Skill, rule, command, manual instruction, or reviewer procedure is the more native representation. Completeness is measured by responsibility coverage and usable native behavior, not by identical file counts.

## 8. Precision standard for every retained component

- Exact mission and exclusive ownership.
- Explicit non-ownership and prohibited actions.
- Inputs, preconditions, assumptions, and dependencies.
- Expected outputs and evidence format.
- Allowed tools, permissions, and access boundaries where the platform supports them.
- Invocation, activation, or selection conditions.
- Delegation conditions and allowed delegate targets where delegation is native.
- Stop conditions, failure states, error handling, and blocked-state behavior.
- Completion criteria and mandatory human-review points.
- No self-review, circular delegation, hidden overlap, or authority conflicts.
Rewrite generic cloned text. Platform-specific files must describe how this platform actually discovers, activates, invokes, delegates, restricts, reviews, and completes work. Do not preserve wording merely because another platform uses it.

## 9. Platform-specific acceptance checks

- README explicitly targets local/interative Warp and distinguishes Oz cloud.
- Every Skill is discoverable from the official project path.
- No file references external IDs, accounts, environments, or integrations.
- No automatic orchestration claim remains.
## 10. Mandatory three-pass static verification

1. Pass A — Native structure: verify every file path, filename, frontmatter field, schema key, and discovery mechanism against current official documentation.
1. Pass B — Responsibility and safety: verify ownership boundaries, reviewer independence, least privilege, human approvals, prohibited actions, and absence of unsupported or empty artifacts.
1. Pass C — Coherence and completeness: verify all references resolve, all skills or commands are discoverable by the intended surface, workflows have evidence-bearing completion criteria, README instructions match the actual package, and no duplicate instruction source causes conflicting or repeated loading.
1. Compare the three passes. Correct every defect and restart the affected pass. Do not declare completion until all three passes return PASS.
1. Show runtime, build, test, browser, and integration checks as `NOT EXECUTED` rather than `PASS` whenever they were not performed. Do not create a virtual environment or broaden execution permissions for this platform.
## 10.1 Temporary virtual environment restriction

- This platform does not require a Python virtual environment for final verification. Do not create one.
- Do not install packages or execute platform software merely to obtain a stronger verdict.
- If a newly discovered official native requirement would make Python environment execution indispensable, stop and display `BLOCKED`; do not broaden this prompt's permissions.

## 11. Required final on-screen result

- Platform and exact target directory.
- Official documentation consulted, including page titles and access dates.
- Files created, modified, moved, and deleted.
- Native capability map: instructions, agents/subagents, skills, commands/workflows, hooks, MCP, permissions, and manual-only surfaces.
- Corrections completed and the direct evidence for each correction.
- Intentional omissions and the official limitation that justifies each omission.
- Static verification results for Pass A, Pass B, and Pass C.
- Temporary environment status: `NOT REQUIRED — NOT CREATED`.
- Items not executed or not independently verifiable.
- Display this complete result directly on screen as the final assistant/terminal response. Do not save it as Markdown, JSON, YAML, text, PDF, DOCX, HTML, XML, log, manifest, or any other file.
- Final verdict: PASS, FAIL, or BLOCKED. Stop immediately after displaying this platform result.
## 12. Final stop condition

Do not modify another platform after completing this prompt. Do not generate a master prompt. Do not continue automatically to the next platform. Do not generate an audit, validation, evidence, execution, or completion document in any format. End only after the target platform has passed all three static verification passes or has been displayed as `FAIL` or `BLOCKED` with exact evidence.
