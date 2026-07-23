# Web Development — Cursor

## Department overview

This is a project-scoped Cursor specialization for a stack-aware Web Development department. It supports frontend, backend, full-stack architecture, APIs, authentication, accessibility, performance, SEO, testing, security, privacy, and release-readiness work without assuming one framework. Components are applicability-based; the calling Cursor Agent session uses only the relevant project rules, subagents, and Skills for a task.

## Possible uses

- Discovering an existing web stack.
- Planning a web feature.
- Implementing or reviewing frontend changes.
- Designing or reviewing APIs, authentication, sessions, cookies, CSP, CORS, and privacy behavior.
- Debugging regressions.
- Auditing accessibility, performance, responsive behavior, and SEO.
- Reviewing dependencies and supply-chain risk.
- Preparing release-readiness evidence.
- Reviewing architecture and migration decisions.

## Supported product surface

This package targets Cursor project configuration for the Cursor IDE, Cursor CLI, and Cursor Agent surfaces that load project rules, agents, and Skills from `.cursor/`.

- `.cursor/rules/*.mdc`: Cursor Project Rules with YAML frontmatter and `alwaysApply: true`.
- `.cursor/agents/*.md`: project agents with `name`, `description`, `model`, and `readonly` frontmatter.
- `.cursor/skills/*/SKILL.md`: project Skills for reusable procedures.
- Background Agent, web/cloud agents, GitHub integration, Bugbot, and MCP are user-controlled surfaces and are not configured by this package.
- Repository auto-discovery exists only after these files are copied to a target repository root and Cursor is opened or run there.

## Included native components

- `.cursor/rules/web-development.mdc`: always-on operating rules and safety boundaries.
- `.cursor/rules/quality-gates.mdc`: always-on completion and evidence gates.
- `.cursor/agents/*.md`: direct specialist agents. Reviewers have `readonly: true`; implementation specialists have `readonly: false`.
- `.cursor/skills/*/SKILL.md`: domain Skills and workflow Skills loaded on demand.
- `README.md`: human setup and validation guide. It is not loaded by Cursor.

## Installation and integration

1. Copy the contents of `cursor/web-development/` to the target repository root so the target root contains `.cursor/`.
2. Open the target repository in Cursor IDE or run Cursor CLI from that repository.
3. Review all Project Rules, agents, and Skills before trusting the workspace.
4. Keep MCP, Background Agent settings, GitHub integrations, cloud runs, hooks, provider changes, and external tools disabled unless separately reviewed and authorized.
5. Verify discovery by checking Cursor’s Rules, Agents, and Skills UI or asking Cursor to list the active Web Development rules and project agents.

## How to use

Use the calling Cursor Agent session as the coordinator. It may invoke direct specialists: `web-architecture-specialist`, `frontend-specialist`, `backend-api-specialist`, `security-privacy-reviewer`, `accessibility-performance-seo-reviewer`, and `quality-release-reviewer`. There is no separate lead agent and no root `AGENTS.md`; `.cursor/rules/*.mdc` are the single always-on authority.

Invoke Skills by task purpose or name, such as `stack-discovery`, `workflow-plan-web-change`, `security-privacy-review`, or `workflow-verify-release-readiness`. Expected output should cite repository evidence, report unavailable checks as `NOT EXECUTED`, and keep implementation separate from independent review.

## Operating model

The calling Cursor Agent session confirms scope, discovers the stack, requests architecture/frontend/backend specialists when useful, then requests security/privacy and accessibility/performance/SEO reviewers when applicable. `quality-release-reviewer` runs last for final readiness. Specialists are direct and do not recursively delegate. Completion uses `PASS`, `FAIL`, `BLOCKED`, or `NOT APPLICABLE`, with `NOT EXECUTED` for checks that did not run.

## Examples

- Feature/architecture: ask with Cursor in the target repository to plan a passwordless login flow for the current web app. State: `Do not deploy or install packages.`
- Review/audit: request security/privacy review for CSP, cookies, CSRF, CORS, authorization, logging, third-party scripts, and sensitive data handling.
- Stack selection: provide repository evidence and ask the department to use only applicable Web Development specialists for React, Rails, Django, Laravel, static-site, or other detected stacks.
- Project customization: add `Node 22, pnpm only, WCAG 2.2 AA, LCP budget 2.5s, Playwright smoke tests` to task criteria without editing core department files.
- Sensitive action: request a deployment, publication, package-install, or Git checklist without executing it; actual external action requires separate human approval.

## Project-specific and user-specific configuration

The department is already specialized. Already specialized and normally not modified: project rules, agents, and Skills, review responsibilities, security/privacy responsibilities, accessibility/performance/SEO responsibilities, testing responsibilities, quality gates, and the operating model. Project/user values may include framework and runtime versions, package manager policy, repository layout, code style, lint/format/test commands, coverage thresholds, browser support matrix, WCAG target, performance budgets, Core Web Vitals thresholds, SEO requirements, API conventions, auth provider, database/storage technology, approved dependencies, deployment target, CI/CD commands, environment names, feature-flag conventions, observability provider, logging requirements, organization security policy, privacy/legal requirements, data classification, approval owners, release process, branch strategy, protected branches, allowed external integrations, MCP servers or connectors, private endpoints, organization IDs, and workspace IDs. Never hard-code or commit API keys, tokens, passwords, private keys, production credentials, real secret values, or sensitive private URLs; use placeholders or environment-variable names. Project-specific configuration extends the department; it does not create the specialization.

## Safety and human approval

This package does not authorize automatic deployment, publication, authentication, secret use, spending, signing, submission, destructive operations, dependency installation, Git mutation, MCP use, Background Agent execution, cloud run publication, GitHub integration, or production changes. Cursor’s local permission prompts and workspace settings still apply; every sensitive or external action requires exact human authorization.

## Limitations

- Cursor rules, agents, and Skills are instructions, not deterministic enforcement.
- `readonly: true` expresses reviewer intent for Cursor agents; actual behavior depends on Cursor’s current agent implementation and user permissions.
- No MCP configuration, hooks, Background Agent setup, model pinning, cloud publication, or GitHub integration is included.
- Actual Cursor product loading, runtime tests, builds, browser checks, deployment, and Skill invocation were not executed.

## Validation

- Syntax validation: `.mdc` and agent YAML frontmatter, `readonly` fields, and Skill frontmatter were parsed.
- Schema/static validation: retained files were mapped to `.cursor/rules/`, `.cursor/agents/`, and `.cursor/skills/`; no duplicate root `AGENTS.md`, MCP config, hooks, cloud agent config, or unsupported fields remain.
- Actual product loading: `NOT EXECUTED`.
- Runtime tests: `NOT EXECUTED`.
- Browser/build/deployment checks: `NOT EXECUTED`.

## Official documentation

Verified on July 20, 2026:

- Cursor Docs: Rules - https://docs.cursor.com/context/rules
- Cursor Docs: Agents - https://docs.cursor.com/context/agents
- Cursor Docs: Skills - https://docs.cursor.com/context/skills
- Cursor Docs: CLI - https://docs.cursor.com/cli/overview
- Cursor Docs: MCP - https://docs.cursor.com/context/model-context-protocol
- Cursor Docs: Background Agent - https://docs.cursor.com/background-agent
