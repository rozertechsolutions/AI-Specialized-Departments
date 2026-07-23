# Web Development — Codex

## Department overview

This is a project-scoped Codex specialization for a stack-aware Web Development department. It supports frontend, backend, full-stack architecture, APIs, authentication, accessibility, performance, SEO, testing, security, privacy, and release-readiness work without assuming one framework. Components are applicability-based; the root Codex session invokes only the relevant specialist agents and Skills for a task.

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

This package targets Codex local project customization for the CLI, IDE extension, and Codex app when they operate on a local repository. It is static project configuration, not a deployment or SDK package.

- `AGENTS.md`: Codex reads applicable `AGENTS.md` files before work begins and uses nested files by scope.
- `.codex/config.toml`: project configuration discovered from the repository root. This package sets only `[agents]` concurrency/depth fields.
- `.codex/agents/*.toml`: project-scoped custom subagents. Codex custom agent TOML requires `name`, `description`, and `developer_instructions`; supported config keys such as `sandbox_mode` may be included.
- `.agents/skills/*/SKILL.md`: project Agent Skills for reusable procedures.
- Minimum version: this package relies on current Codex custom agent and Skill support documented in the Codex developer docs. Product availability, model availability, and local client features can vary by plan, workspace policy, and surface.

## Included native components

- `AGENTS.md`: root session orchestration, safety boundaries, completion contract, and specialist ordering.
- `.codex/config.toml`: sets `agents.max_threads = 4`, `agents.max_depth = 1`, and `agents.interrupt_message = true`.
- `.codex/agents/*.toml`: direct specialist custom agents. Implementation specialists use `workspace-write`; independent reviewers use `read-only`.
- `.agents/skills/*/SKILL.md`: domain Skills and workflow Skills loaded on demand.
- `README.md`: human setup and validation guide. It is not loaded by Codex.

## Installation and integration

1. Copy the contents of `codex/web-development/` to the target repository root so the target root contains `AGENTS.md`, `.codex/`, and `.agents/`.
2. Review all custom agents, Skills, and project configuration before trusting the repository.
3. Start Codex from the target repository root.
4. Keep hooks, MCP servers, plugins, custom tools, provider changes, model overrides, and external integrations disabled unless separately reviewed and authorized.
5. Verify discovery by asking Codex to summarize the active Web Development `AGENTS.md`, list available project agents, and list available Web Development Skills.

## How to use

Use the root Codex session as the coordinator. It may request specialist agents directly: `web-architecture-specialist`, `frontend-specialist`, `backend-api-specialist`, `security-privacy-reviewer`, `accessibility-performance-seo-reviewer`, and `quality-release-reviewer`. There is no lead subagent because `agents.max_depth = 1` intentionally permits only root-to-specialist delegation.

Invoke Skills by task purpose or by mentioning a Skill name, such as `stack-discovery`, `workflow-plan-web-change`, `security-privacy-review`, or `workflow-verify-release-readiness`. Expected output should cite repository evidence, report unavailable checks as `NOT EXECUTED`, and distinguish implementation from independent review.

## Operating model

The root session confirms scope, discovers the stack, delegates architecture/frontend/backend implementation as needed, requests security/privacy and accessibility/performance/SEO reviews when applicable, and runs `quality-release-reviewer` last for final readiness. Specialists cannot recursively delegate because `agents.max_depth = 1` blocks deeper spawning. Completion uses `PASS`, `FAIL`, `BLOCKED`, or `NOT APPLICABLE`, with `NOT EXECUTED` for checks that did not run.

## Examples

- Feature/architecture: ask with the Codex Web Development lead to plan a passwordless login flow for the current web app. State: `Do not deploy or install packages.`
- Review/audit: request security/privacy review for CSP, cookies, CSRF, CORS, authorization, logging, third-party scripts, and sensitive data handling.
- Stack selection: provide repository evidence and ask the department to use only applicable Web Development specialists for React, Rails, Django, Laravel, static-site, or other detected stacks.
- Project customization: add `Node 22, pnpm only, WCAG 2.2 AA, LCP budget 2.5s, Playwright smoke tests` to task criteria without editing core department files.
- Sensitive action: request a deployment, publication, package-install, or Git checklist without executing it; actual external action requires separate human approval.

## Project-specific and user-specific configuration

The department is already specialized. Already specialized and normally not modified: AGENTS.md, Codex agents, and Skills, review responsibilities, security/privacy responsibilities, accessibility/performance/SEO responsibilities, testing responsibilities, quality gates, and the operating model. Project/user values may include framework and runtime versions, package manager policy, repository layout, code style, lint/format/test commands, coverage thresholds, browser support matrix, WCAG target, performance budgets, Core Web Vitals thresholds, SEO requirements, API conventions, auth provider, database/storage technology, approved dependencies, deployment target, CI/CD commands, environment names, feature-flag conventions, observability provider, logging requirements, organization security policy, privacy/legal requirements, data classification, approval owners, release process, branch strategy, protected branches, allowed external integrations, MCP servers or connectors, private endpoints, organization IDs, and workspace IDs. Never hard-code or commit API keys, tokens, passwords, private keys, production credentials, real secret values, or sensitive private URLs; use placeholders or environment-variable names. Project-specific configuration extends the department; it does not create the specialization.

## Safety and human approval

This package does not authorize automatic deployment, publication, authentication, secret use, spending, signing, submission, destructive operations, dependency installation, Git mutation, hook execution, MCP use, plugin installation, provider changes, or production changes. Parent session sandbox and approval controls still apply, and every sensitive or external action requires exact human authorization.

## Limitations

- `AGENTS.md` and Skills are instructions, not deterministic enforcement.
- No hooks are included, so there is no pre-tool guardrail beyond Codex approvals and sandboxing.
- No MCP servers, external integrations, plugins, or custom commands are configured.
- Actual Codex product loading, runtime tests, builds, browser checks, deployment, and Skill invocation were not executed.
- The Codex manual helper could not run in this environment because `node` is not installed; official OpenAI web documentation was used instead.

## Validation

- Syntax validation: `.codex/config.toml`, custom agent TOML, and Skill YAML frontmatter were parsed.
- Schema/static validation: supported custom agent fields, `[agents]` config keys, sandbox topology, reviewer read-only mode, and Skill metadata were checked locally.
- Actual product loading: `NOT EXECUTED`.
- Runtime tests: `NOT EXECUTED`.
- Browser/build/deployment checks: `NOT EXECUTED`.

## Official documentation

Verified on July 20, 2026:

- OpenAI Codex Docs: Custom instructions with AGENTS.md - https://developers.openai.com/codex/agent-configuration/agents-md
- OpenAI Codex Docs: Subagents - https://developers.openai.com/codex/subagents
- OpenAI Codex Docs: Build skills - https://developers.openai.com/codex/build-skills
- OpenAI Codex Docs: Config basics - https://developers.openai.com/codex/config-basic
- OpenAI Codex Docs: Configuration reference - https://developers.openai.com/codex/config-reference
- OpenAI Codex Docs: Advanced configuration - https://developers.openai.com/codex/config-advanced
- OpenAI Codex Docs: Automate with hooks - https://developers.openai.com/codex/config-advanced
