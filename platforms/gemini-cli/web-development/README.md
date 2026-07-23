# Web Development — Gemini CLI

## Department overview

This is a project-scoped Gemini CLI specialization for a stack-aware Web Development department. It supports frontend, backend, full-stack architecture, APIs, authentication, accessibility, performance, SEO, testing, security, privacy, and release-readiness work without assuming one framework. Components are applicability-based; the root Gemini CLI session chooses the relevant custom command, subagent, or Skill for a task.

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

This package targets Gemini CLI project configuration in a trusted local folder.

- `GEMINI.md`: hierarchical project context loaded by Gemini CLI.
- `.gemini/commands/web/*.toml`: project custom commands invoked manually with slash-command syntax.
- `.gemini/agents/*.md`: local project subagents discovered by Gemini CLI when subagents are enabled.
- `.gemini/skills/*/SKILL.md`: project Agent Skills for reusable procedures.
- Trusted folder behavior: Gemini CLI asks the user to trust a folder before loading project-specific configuration.
- No settings file, hooks, extensions, MCP, A2A, remote subagents, or external tools are included.

## Included native components

- `GEMINI.md`: root project context for operating model, delegation, safety, and completion gates.
- `.gemini/commands/web/*.toml`: prompt-only workflow commands that pass user input through `{{args}}`.
- `.gemini/agents/*.md`: local specialist subagents. Reviewers have read-only repository tools; implementation specialists have file read/edit tools and no shell tool.
- `.gemini/skills/*/SKILL.md`: domain Skills only. Duplicate workflow Skills were removed because commands own those manual workflow entry points.
- `README.md`: human setup and validation guide. It is not loaded by Gemini CLI.

## Installation and integration

1. Copy the contents of `gemini-cli/web-development/` to the target repository root so the target root contains `GEMINI.md` and `.gemini/`.
2. Start Gemini CLI from the target repository root.
3. Approve folder trust only after reviewing `GEMINI.md`, command TOML, subagents, and Skills.
4. Keep hooks, extensions, MCP, A2A, remote agents, shell auto-approval, provider changes, and external tools disabled unless separately reviewed and authorized.
5. Verify discovery with Gemini CLI commands such as `/commands`, `/agents list`, `/agents reload`, and the Skills UI or command surface available in the installed CLI.

## How to use

Use custom commands for explicit manual workflows under the `web` namespace, for example `/web:plan-web-change`, `/web:implement-web-change`, `/web:review-security-and-privacy`, and `/web:verify-release-readiness`. Pass task context as command arguments; command TOML treats `{{args}}` only as user-supplied context.

Use local subagents for focused work: `web-architecture-specialist`, `frontend-specialist`, `backend-api-specialist`, `security-privacy-reviewer`, `accessibility-performance-seo-reviewer`, and `quality-release-reviewer`. Use domain Skills by name or purpose, such as `stack-discovery`, `backend-api-auth`, or `security-privacy-review`.

## Operating model

The root Gemini CLI session confirms scope, discovers the stack, uses commands for repeatable manual workflows, delegates to local subagents when focused context is useful, and loads domain Skills for reusable procedures. Security/privacy and accessibility/performance/SEO reviewers run after relevant work, and `quality-release-reviewer` runs last. Completion uses `PASS`, `FAIL`, `BLOCKED`, or `NOT APPLICABLE`, with `NOT EXECUTED` for checks that did not run.

## Examples

- Feature/architecture: ask with Gemini CLI in the target repository to plan a passwordless login flow for the current web app. State: `Do not deploy or install packages.`
- Review/audit: request security/privacy review for CSP, cookies, CSRF, CORS, authorization, logging, third-party scripts, and sensitive data handling.
- Stack selection: provide repository evidence and ask the department to use only applicable Web Development specialists for React, Rails, Django, Laravel, static-site, or other detected stacks.
- Project customization: add `Node 22, pnpm only, WCAG 2.2 AA, LCP budget 2.5s, Playwright smoke tests` to task criteria without editing core department files.
- Sensitive action: request a deployment, publication, package-install, or Git checklist without executing it; actual external action requires separate human approval.

## Project-specific and user-specific configuration

The department is already specialized. Already specialized and normally not modified: GEMINI.md, agents, commands, and Skills, review responsibilities, security/privacy responsibilities, accessibility/performance/SEO responsibilities, testing responsibilities, quality gates, and the operating model. Project/user values may include framework and runtime versions, package manager policy, repository layout, code style, lint/format/test commands, coverage thresholds, browser support matrix, WCAG target, performance budgets, Core Web Vitals thresholds, SEO requirements, API conventions, auth provider, database/storage technology, approved dependencies, deployment target, CI/CD commands, environment names, feature-flag conventions, observability provider, logging requirements, organization security policy, privacy/legal requirements, data classification, approval owners, release process, branch strategy, protected branches, allowed external integrations, MCP servers or connectors, private endpoints, organization IDs, and workspace IDs. Never hard-code or commit API keys, tokens, passwords, private keys, production credentials, real secret values, or sensitive private URLs; use placeholders or environment-variable names. Project-specific configuration extends the department; it does not create the specialization.

## Safety and human approval

This package does not authorize automatic deployment, publication, authentication, secret use, spending, signing, submission, destructive operations, dependency installation, Git mutation, hook execution, extension execution, MCP use, A2A, remote agents, shell commands, or production changes. Gemini CLI tool confirmations and trusted-folder controls still apply; every sensitive or external action requires exact human authorization.

## Limitations

- Commands, subagents, and Skills are instructions, not deterministic enforcement.
- Subagent and Skill availability can depend on the installed Gemini CLI version and feature settings.
- Trusted-folder approval is a user action outside this package.
- No runtime validation, browser checks, builds, tests, hooks, extensions, MCP, shell commands, or live Gemini CLI loading were executed.

## Validation

- Syntax validation: command TOML, subagent YAML frontmatter, and Skill YAML frontmatter were parsed.
- Schema/static validation: retained files were mapped to `GEMINI.md`, `.gemini/commands/`, `.gemini/agents/`, and `.gemini/skills/`; duplicate workflow Skills, settings, hooks, extensions, MCP, A2A, and remote-agent configs are absent.
- Actual product loading: `NOT EXECUTED`.
- Runtime tests: `NOT EXECUTED`.
- Browser/build/deployment checks: `NOT EXECUTED`.

## Official documentation

Verified on July 20, 2026:

- Gemini CLI Docs: GEMINI.md context files - https://google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html
- Gemini CLI Docs: Custom commands - https://google-gemini.github.io/gemini-cli/docs/cli/custom-commands.html
- Gemini CLI Docs: Subagents - https://geminicli.com/docs/core/subagents/
- Gemini CLI Docs: Agent Skills - https://geminicli.com/docs/cli/skills/
- Gemini CLI Docs: Trusted folders - https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/trusted-folders.md
- Gemini CLI Docs: CLI commands - https://geminicli.com/docs/reference/commands/
- Gemini CLI Docs: MCP servers - https://google-gemini.github.io/gemini-cli/docs/tools/mcp-server.html
