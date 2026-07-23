# Web Development — Claude Code

## Department overview

This is a project-scoped Claude Code specialization for a stack-aware Web Development department. It supports frontend, backend, full-stack architecture, APIs, authentication, accessibility, performance, SEO, testing, security, privacy, and release-readiness work without assuming one framework. Components are applicability-based; the lead selects only the relevant specialist agents and Skills for a task.

## Possible uses

- Discovering an existing web stack.
- Planning a web feature or architecture decision.
- Implementing or reviewing frontend changes.
- Designing or reviewing APIs, authentication, sessions, cookies, CSP, CORS, and privacy behavior.
- Debugging regressions.
- Auditing accessibility, performance, responsive behavior, browser compatibility, and SEO.
- Reviewing dependencies and supply-chain risk.
- Preparing release-readiness evidence.
- Reviewing architecture and migration decisions.

## Supported product surface

This package targets Claude Code local project configuration. Copy the contents of `claude-code/web-development/` to the root of a target repository so Claude Code can discover project memory, project subagents, and project Skills.

- `CLAUDE.md` project memory is loaded as contextual guidance at session start.
- `.claude/agents/*.md` files are project subagents. They are discovered from `.claude/agents/`, use YAML frontmatter, and can be launched by name or through `Agent`.
- `.claude/skills/*/SKILL.md` files are project Skills. Skills can be invoked with `/skill-name` or by Claude when relevant.
- Minimum version: this package relies on current Claude Code subagent and Skill support, including `Agent` tool naming and `skills` preloading. The official docs note `Agent` replaced `Task` in v2.1.63, and newer releases improve Skill and subagent behavior.
- No `.claude/settings.json`, `.mcp.json`, hooks, plugins, commands, cloud schedules, or external integrations are included.

## Included native components

- `CLAUDE.md`: concise project memory for orchestration, scope, safety, and completion standards.
- `.claude/agents/web-development-lead.md`: coordinator intended for `claude --agent web-development-lead` or explicit delegation from the main session. It has `Agent(...)` allowlisted specialist delegation and access to the `Skill` tool.
- `.claude/agents/*specialist*.md`: project subagents with scoped tools and preloaded role Skills.
- `.claude/skills/*/SKILL.md`: project Skills. Domain Skills provide reusable specialist procedures; workflow Skills provide manual workflow entry points.
- `README.md`: human setup and validation guide. It is not loaded by Claude Code.

## Installation and integration

1. Copy the contents of this directory into the target repository root so the target root contains `CLAUDE.md` and `.claude/`.
2. Review every Skill and agent file before accepting workspace trust for the repository.
3. Start Claude Code from the target repository root.
4. For coordinated work, launch the lead as the main session agent with `claude --agent web-development-lead`, or ask the main session to use `web-development-lead`.
5. Keep MCP servers, hooks, plugins, and project settings disabled unless separately reviewed and authorized.
6. Verify discovery with `/agents` and `/skills` in Claude Code, or by asking Claude Code to list the available Web Development agents and Skills.

## How to use

Use `web-development-lead` for coordinated work. The lead can delegate only to `web-architecture-specialist`, `frontend-specialist`, `backend-api-specialist`, `security-privacy-reviewer`, `accessibility-performance-seo-reviewer`, and `quality-release-reviewer` through its `Agent(...)` allowlist. Specialists do not list `Agent`, so they cannot recursively delegate.

Manual workflow Skills are invoked with slash commands such as `/workflow-plan-web-change`, `/workflow-implement-web-change`, `/workflow-debug-web-regression`, `/workflow-review-security-and-privacy`, and `/workflow-verify-release-readiness`. Domain Skills may also load when their descriptions match the task.

## Operating model

The lead confirms scope, discovers the stack, plans architecture when material, delegates implementation to architecture/frontend/backend specialists, then requests independent security/privacy and accessibility/performance/SEO review where applicable. The `quality-release-reviewer` runs last and returns an evidence-based final readiness verdict. Completion uses `PASS`, `FAIL`, `BLOCKED`, or `NOT APPLICABLE`, with `NOT EXECUTED` for checks that were not actually run.

## Examples

- Feature/architecture: ask with the web-development lead in Claude Code to plan a passwordless login flow for the current web app. State: `Do not deploy or install packages.`
- Review/audit: request security/privacy review for CSP, cookies, CSRF, CORS, authorization, logging, third-party scripts, and sensitive data handling.
- Stack selection: provide repository evidence and ask the department to use only applicable Web Development specialists for React, Rails, Django, Laravel, static-site, or other detected stacks.
- Project customization: add `Node 22, pnpm only, WCAG 2.2 AA, LCP budget 2.5s, Playwright smoke tests` to task criteria without editing core department files.
- Sensitive action: request a deployment, publication, package-install, or Git checklist without executing it; actual external action requires separate human approval.

## Project-specific and user-specific configuration

The department is already specialized. Already specialized and normally not modified: CLAUDE.md, subagents, and Skills, review responsibilities, security/privacy responsibilities, accessibility/performance/SEO responsibilities, testing responsibilities, quality gates, and the operating model. Project/user values may include framework and runtime versions, package manager policy, repository layout, code style, lint/format/test commands, coverage thresholds, browser support matrix, WCAG target, performance budgets, Core Web Vitals thresholds, SEO requirements, API conventions, auth provider, database/storage technology, approved dependencies, deployment target, CI/CD commands, environment names, feature-flag conventions, observability provider, logging requirements, organization security policy, privacy/legal requirements, data classification, approval owners, release process, branch strategy, protected branches, allowed external integrations, MCP servers or connectors, private endpoints, organization IDs, and workspace IDs. Never hard-code or commit API keys, tokens, passwords, private keys, production credentials, real secret values, or sensitive private URLs; use placeholders or environment-variable names. Project-specific configuration extends the department; it does not create the specialization.

## Safety and human approval

This package does not authorize automatic deployment, publication, authentication, secret use, spending, signing, submission, destructive operations, dependency installation, Git mutation, MCP setup, hook execution, plugin installation, or production changes. No agent has Bash access. Reviewers have only `Read`, `Grep`, and `Glob`; implementers have file read/edit/write/search tools but no shell.

## Limitations

- `CLAUDE.md` is contextual guidance, not an enforcement mechanism.
- Actual permission prompts depend on the user’s Claude Code session settings and workspace trust state.
- Live Claude Code loading, Skill invocation, runtime tests, builds, browser checks, deployment, and MCP connections were not executed.
- Workflow Skills are static instructions; they do not run commands by themselves.
- This package does not include hooks, so no deterministic pre-tool enforcement is provided.

## Validation

- Syntax validation: YAML frontmatter was parsed for all retained agents and Skills.
- Schema/static validation: agent names, Skill names, tool declarations, delegation topology, and internal Skill references were checked locally.
- Actual product loading: `NOT EXECUTED`.
- Runtime tests: `NOT EXECUTED`.
- Browser/build/deployment checks: `NOT EXECUTED`.

## Official documentation

Verified on July 20, 2026:

- Claude Code Docs: How Claude remembers your project - https://code.claude.com/docs/en/memory
- Claude Code Docs: Create custom subagents - https://code.claude.com/docs/en/sub-agents
- Claude Code Docs: Extend Claude with skills - https://code.claude.com/docs/en/skills
- Claude Code Docs: Claude Code settings - https://code.claude.com/docs/en/settings
- Claude Code Docs: Automate with hooks - https://code.claude.com/docs/en/hooks
- Claude Code Docs: MCP reference - https://code.claude.com/docs/en/mcp
