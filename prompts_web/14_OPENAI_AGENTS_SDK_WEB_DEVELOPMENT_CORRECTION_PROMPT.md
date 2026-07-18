# OpenAI Agents SDK — Web Development Correction Prompt

*AI Specialized Departments — Independent Platform Prompt*

| Prompt type | Standalone correction and completion prompt |
| --- | --- |
| Target | openai-agents-sdk/web-development/ |
| Execution mode | Static repository editing plus one isolated temporary Python final-validation environment |
| Documentation baseline | Current official sources at execution time; Reddit secondary only |

## 1. Mission

Correct and complete the existing Web Development specialization for this platform only. The result must use current, real, project-scoped native capabilities, remove unsupported or misleading artifacts, repair all audit findings, and leave the platform package internally coherent, safe by default, and professionally complete.

`TARGET_DIRECTORY = openai-agents-sdk/web-development/`

**Target product surface:** A real Python OpenAI Agents SDK implementation package with typed agents, manager orchestration, tools, guardrails, human-in-the-loop approvals, structured results, and offline wiring tests. No server, UI, deployment, installer, or live credentials.

## 2. Immutable execution boundaries

- Work only inside the target directory named in this document. Do not inspect, create, modify, rename, or delete files in any other platform or specialization.
- You may use web research only to consult current official product documentation. High-signal Reddit discussions may be used as secondary evidence for practical limitations, but never as authority over official documentation.
- Do not use a terminal, shell, command execution, scripts, builds, tests, package managers, or installers except for the single isolated temporary Python validation environment explicitly authorized in Section 10.1. Git, external authentication, live model/API calls, connected services, deployments, publishing, and all unrelated execution remain prohibited.
- Create, modify, move, or delete only static configuration, instruction, documentation, schema, or SDK source files required by this platform package.
- Do not create or add audit reports, validation reports, execution reports, evidence reports, completion reports, manifests, logs, or equivalent artifacts in any format. Do not write the final result into the repository. The final result must be shown only in the visible on-screen response.
- Do not create a common directory, cross-platform adapter, converter, shared runtime, installer, migration utility, or compatibility shim.
- Do not copy another platform's folder structure. Native conceptual consistency is required; identical structures are not.
- Do not retain empty files, placeholder-only files, empty MCP objects, dummy integrations, simulated agents, simulated hooks, or unsupported configuration keys.
- Do not add secrets, tokens, credentials, real endpoints, private URLs, account identifiers, environment-specific paths, or enabled external integrations.
- Do not weaken human approval requirements. Production, authentication, authorization, sensitive data, dependency changes, third-party scripts, trackers, deployment, publication, spending, signing, submission, destructive actions, and Git mutations require explicit human review.
- Do not claim that builds, tests, runtime behavior, browser behavior, integrations, or platform loading were verified unless there is direct evidence. This task is limited to repository editing, three static verification passes, and the isolated temporary final compatibility test authorized in Section 10.1.
## 3. Mandatory research gate

1. Identify the current product surface and configuration format as of the execution date before editing any file.
1. Use official documentation as the primary source. Record the exact documentation pages or official repository references used in the final on-screen result.
1. For every existing or proposed component, classify it internally as native, conditionally native, manual-only, or unsupported.
1. Delete unsupported components completely. Do not preserve them for symmetry or future possibilities.
1. When official documentation is ambiguous, choose the safest minimal implementation and state the limitation in the final on-screen result. Do not invent behavior.
1. Treat Reddit only as secondary operational evidence. Use established communities, recent posts, reproducible details, and maintainer responses where available.
**Official documentation baseline to verify:** OpenAI Agents SDK: Agents; OpenAI Agents SDK: Agent orchestration and agents as tools; OpenAI Agents SDK: Handoffs; OpenAI Agents SDK: Guardrails; OpenAI Agents SDK: Human-in-the-loop; OpenAI Agents SDK: Results and RunState.

## 4. Known audit findings to correct

- All seven agents currently have tools=[] and cannot inspect any supplied repository context or produce actionable structured artifacts.
- The lead uses handoffs, which transfer control, instead of manager-style agent-as-tool orchestration that preserves coordinator control.
- Static policy sets are not connected to function tools, approvals, guardrails, runner state, or workflow execution.
- No input, output, or tool guardrails are wired.
- No human-in-the-loop pause, approval, rejection, serialization, or resume flow exists.
- No structured result models define plans, findings, evidence, decisions, or final verdicts.
- Tests cover only two isolated policy predicates and compiled __pycache__ artifacts were included.
- The dependency constraint is unbounded above.
## 5. Required platform-native corrections

1. Delete all __pycache__ directories and .pyc files. Add appropriate source-control ignore guidance without performing Git actions.
1. Redesign department.py around a manager-controlled workflow. Expose specialist agents to the lead with Agent.as_tool() or the current recommended manager pattern so results return to the lead. Use handoffs only when transfer of control is explicitly intended and justified.
1. Define typed Pydantic or dataclass models for repository snapshot input, task scope, architecture decision, implementation proposal, reviewer finding, evidence item, approval request, unresolved risk, and final verdict.
1. Implement safe function tools that operate only on caller-supplied in-memory repository content or abstract injected interfaces. Do not perform filesystem, shell, network, Git, deployment, package installation, or external service actions by default.
1. Separate read/context tools, proposal tools, and sensitive action request tools. Sensitive tools must use the current SDK human-approval mechanism and default to interruption rather than execution.
1. Wire input guardrails for empty, out-of-scope, secret-bearing, destructive, deployment, publication, or unsupported requests. Wire output guardrails for unsupported success claims, missing evidence, unresolved critical findings, and invalid final verdicts.
1. Implement RunState or the current SDK state mechanism so approval interruptions can be serialized, presented to a human, approved or rejected, and resumed deterministically.
1. Implement a complete manager sequence: validate request; inspect supplied snapshot; obtain architecture/front-end/back-end analyses as needed; obtain independent security and accessibility/performance/SEO reviews; obtain final quality review; reconcile; emit structured PASS, FAIL, or BLOCKED.
1. Reviewers must not receive mutation tools. The lead may propose changes but may not self-approve sensitive actions or override critical reviewer findings.
1. Rewrite policy.py so policies are enforced by tools and guardrails rather than existing as disconnected constants.
1. Rewrite workflow.py to expose explicit entry points for normal run, interrupted run, approval decision, resume, and structured final result.
1. Add comprehensive offline tests for agent wiring, manager retention of control, tool availability, reviewer read-only constraints, guardrail trips, approval interruptions, rejection behavior, resume behavior, and structured verdict rules. Do not require live API calls.
1. Bound dependency versions according to the current supported SDK release policy and document compatibility. Do not use @latest or an unbounded major range.
1. Update README.md with architecture, safety model, non-goals, integration contract, example in-memory invocation, approval lifecycle, testing scope, and limitations. Do not include real keys or execution instructions that install dependencies.
## 6. Native capability boundary

### Retain or create only when verified native

- Python OpenAI Agents SDK agents and Runner
- Agents as tools for manager orchestration
- Function tools
- Input/output/tool guardrails
- Human-in-the-loop approvals and RunState
- Structured outputs
- Offline unit tests
### Omit or delete

- Terminal or filesystem mutation by default
- Server
- UI
- Deployment
- Installer
- Live credentials
- Uncontrolled handoff chain
- Compiled artifacts
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

- The lead remains the final manager after every specialist call.
- Every specialist has a real, bounded tool or context surface appropriate to its role.
- Reviewer agents cannot mutate state.
- Sensitive tool calls generate approval interruptions and can be rejected safely.
- Guardrails are attached to actual agents or tools and are exercised by offline tests.
- Final PASS is impossible with unresolved critical findings, missing required reviews, or unsupported evidence claims.
- No code path performs external or local mutation without caller-supplied implementation and explicit approval.
## 10. Mandatory three-pass static verification before runtime validation

1. Pass A — Native structure: verify every file path, filename, frontmatter field, schema key, and discovery mechanism against current official documentation.
1. Pass B — Responsibility and safety: verify ownership boundaries, reviewer independence, least privilege, human approvals, prohibited actions, and absence of unsupported or empty artifacts.
1. Pass C — Coherence and completeness: verify all references resolve, all skills or commands are discoverable by the intended surface, workflows have evidence-bearing completion criteria, README instructions match the actual package, and no duplicate instruction source causes conflicting or repeated loading.
1. Compare the three passes. Correct every defect and restart the affected pass. Do not declare completion until all three passes return PASS.
1. Static verification alone is insufficient for final PASS. Complete the temporary-environment compatibility test in Section 10.1. Show every other runtime, browser, live integration, and external-service check that was not performed as `NOT EXECUTED`, never as `PASS`.
## 10.1 Mandatory temporary Python validation environment

This exception exists only to prove real OpenAI Agents SDK compatibility. It does not authorize general environment changes.

1. Create exactly one isolated Python virtual environment in the operating system temporary directory, outside the repository and outside `TARGET_DIRECTORY`.
2. Determine a concrete currently supported `openai-agents` version from official release information, install that exact version, and display the resolved version in the final on-screen result. Do not use an unpinned `latest` dependency.
3. Install only the minimum package and test dependencies required for this target. Use package-manager no-cache options where available. Do not install globally or modify user/system Python environments.
4. Set `PYTHONDONTWRITEBYTECODE=1` and prevent `.pyc`, `__pycache__`, coverage files, test reports, lockfiles, or other generated artifacts from being written into the repository.
5. Verify that the imported `agents` package comes from the temporary environment, not from a local stub or repository shadow package.
6. Run the real import, object-construction, agent/tool/guardrail/approval wiring, serialization, and offline test checks required by the corrected package. Do not make live model calls, API requests, external authentications, deployments, or filesystem mutations outside the temporary environment.
7. Keep validation output transient. Do not create audit documents, validation documents, JUnit XML, coverage reports, or any other report file.
8. Whether validation passes or fails, remove the complete temporary environment before displaying the final result. Use guaranteed cleanup behavior equivalent to `finally` and verify that the environment path no longer exists.
9. A failed import, failed construction, failed offline test, unresolved SDK incompatibility, or failed environment cleanup prevents `PASS`. Cleanup failure must produce `BLOCKED` and identify the undeleted path on screen.
10. Final `PASS` requires both successful authorized tests and confirmed deletion of the temporary environment.

## 11. Required final on-screen result

- Platform and exact target directory.
- Official documentation consulted, including page titles and access dates.
- Files created, modified, moved, and deleted.
- Native capability map: instructions, agents/subagents, skills, commands/workflows, hooks, MCP, permissions, and manual-only surfaces.
- Corrections completed and the direct evidence for each correction.
- Intentional omissions and the official limitation that justifies each omission.
- Verification results for Pass A, Pass B, Pass C, and the mandatory temporary-environment compatibility test.
- Exact temporary environment status: created path, resolved SDK version, tests executed, cleanup result, and confirmation that the path was deleted.
- Items not executed or not independently verifiable.
- Display this complete result directly on screen as the final assistant/terminal response. Do not save it as Markdown, JSON, YAML, text, PDF, DOCX, HTML, XML, log, manifest, or any other file.
- Final verdict: PASS, FAIL, or BLOCKED. Stop immediately after displaying this platform result.
## 12. Final stop condition

Do not modify another platform after completing this prompt. Do not generate a master prompt. Do not continue automatically to the next platform. Do not generate an audit, validation, evidence, execution, or completion document in any format. End only after the target platform has passed all three static verification passes, passed the mandatory temporary-environment compatibility test, and confirmed environment deletion, or has been displayed as `FAIL` or `BLOCKED` with exact evidence.
