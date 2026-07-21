# Web Development — Cline

## Department overview

This is a project-scoped Cline specialization for a stack-aware Web Development department. It supports frontend, backend, full-stack architecture, APIs, authentication, accessibility, performance, SEO, testing, security, privacy, and release-readiness work without assuming one framework. Rules provide concise always-on behavior; Skills load only when applicable.

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

This package targets Cline project configuration in a repository workspace.

- IDE extension: Cline runs in VS Code-compatible IDEs and uses Plan/Act modes, approval prompts, project rules, and Skills.
- CLI/SDK surfaces: Cline configuration is shared through `.cline/` project configuration where supported, but UI features such as rule toggles and Plan/Act controls can differ by surface.
- Project configuration path: current official configuration documents project rules at `.cline/rules/` and project Skills at `.cline/skills/`.
- Legacy `.clinerules/`: not retained here because it would duplicate the same always-on instructions.
- Repository auto-discovery exists only after these files are copied to the target repository root and Cline is run in that workspace.
- This package is static configuration. It includes no executable hooks, plugins, cron, MCP, agents, provider settings, or workflows.

## Included native components

- `.cline/rules/*.md`: project rules loaded as persistent project instructions.
- `.cline/skills/*/SKILL.md`: project Skills loaded on demand when their descriptions match a request.
- `README.md`: human setup and validation guide. It is not loaded by Cline.

## Installation and integration

1. Copy the contents of `cline/web-development/` to the target repository root so the target root contains `.cline/rules/` and `.cline/skills/`.
2. Open the repository in Cline through the IDE extension or CLI surface.
3. Review the rules and Skills before enabling or relying on them.
4. Enable Skills only if the Cline surface and settings expose Skill support.
5. Keep hooks, plugins, MCP, cron, provider configuration, terminal auto-approval, deployment, publication, and destructive actions disabled unless a human approves the exact use.
6. Verify discovery by checking the Cline Rules and Skills UI or asking Cline to list the active project rules and available Web Development Skills.

## How to use

Use Plan mode for discovery, architecture, reviews, security analysis, and unclear changes. Switch to Act mode only after scope and approach are clear and the human approves the implementation direction. Ask for a Skill by purpose, for example: `Use the backend-api-auth Skill to review this endpoint change.`

Cline may propose file edits or tool use. Expected output should cite repository evidence, distinguish assumptions, and mark tests, builds, browser checks, deployment, and external actions as `NOT EXECUTED` unless Cline actually ran them with approval.

## Operating model

Cline starts from the always-on project rules, discovers the stack, confirms scope and acceptance criteria, then uses on-demand Skills for specialist procedures. The model remains a single Cline task flow rather than simulated custom agents. Completion uses `PASS`, `FAIL`, `BLOCKED`, or `NOT APPLICABLE`, with `NOT EXECUTED` for checks that did not run.

## Examples

- Feature/architecture: ask with Cline in the target repository to plan a passwordless login flow for the current web app. State: `Do not deploy or install packages.`
- Review/audit: request security/privacy review for CSP, cookies, CSRF, CORS, authorization, logging, third-party scripts, and sensitive data handling.
- Stack selection: provide repository evidence and ask the department to use only applicable Web Development specialists for React, Rails, Django, Laravel, static-site, or other detected stacks.
- Project customization: add `Node 22, pnpm only, WCAG 2.2 AA, LCP budget 2.5s, Playwright smoke tests` to task criteria without editing core department files.
- Sensitive action: request a deployment, publication, package-install, or Git checklist without executing it; actual external action requires separate human approval.

## Project-specific and user-specific configuration

The department is already specialized. Already specialized and normally not modified: rules and Skills, review responsibilities, security/privacy responsibilities, accessibility/performance/SEO responsibilities, testing responsibilities, quality gates, and the operating model. Project/user values may include framework and runtime versions, package manager policy, repository layout, code style, lint/format/test commands, coverage thresholds, browser support matrix, WCAG target, performance budgets, Core Web Vitals thresholds, SEO requirements, API conventions, auth provider, database/storage technology, approved dependencies, deployment target, CI/CD commands, environment names, feature-flag conventions, observability provider, logging requirements, organization security policy, privacy/legal requirements, data classification, approval owners, release process, branch strategy, protected branches, allowed external integrations, MCP servers or connectors, private endpoints, organization IDs, and workspace IDs. Never hard-code or commit API keys, tokens, passwords, private keys, production credentials, real secret values, or sensitive private URLs; use placeholders or environment-variable names. Project-specific configuration extends the department; it does not create the specialization.

## Safety and human approval

This package does not authorize automatic deployment, publication, authentication, secret use, spending, signing, submission, destructive operations, dependency installation, Git mutation, hook execution, plugin execution, MCP use, or production changes. Cline may have tool capabilities depending on the user’s configuration, so terminal commands, file edits, browser actions, and external effects must remain subject to explicit human approval and local Cline settings.

## Limitations

- Rules and Skills are instructions, not deterministic enforcement.
- Plan/Act availability, Skill support, approvals, and auto-approve settings depend on the installed Cline surface and configuration.
- No custom agents are included; Cline project agents are intentionally omitted.
- No runtime validation, browser checks, builds, tests, hooks, plugins, MCP, cron, or terminal commands were executed.

## Validation

- Syntax validation: `SKILL.md` YAML frontmatter was parsed for retained Cline Skills.
- Schema/static validation: retained files were mapped to `.cline/rules/` and `.cline/skills/`; no `.clinerules/`, hooks, plugins, MCP, cron, provider settings, custom agents, or executable workflows remain.
- Actual product loading: `NOT EXECUTED`.
- Runtime tests: `NOT EXECUTED`.
- Browser/build/deployment checks: `NOT EXECUTED`.

## Official documentation

Verified on July 20, 2026:

- Cline Docs: Config - https://docs.cline.bot/getting-started/config
- Cline Docs: Rules - https://docs.cline.bot/customization/cline-rules
- Cline Docs: Skills - https://docs.cline.bot/customization/skills
- Cline Docs: Plan and Act - https://docs.cline.bot/core-workflows/plan-and-act
- Cline Docs: Auto Approve - https://docs.cline.bot/features/auto-approve
- Cline Docs: Hooks - https://docs.cline.bot/customization/hooks
- Cline Docs: Plugins - https://docs.cline.bot/customization/plugins
