# Web Development — Junie

## Department overview

This is a project-scoped JetBrains Junie specialization for a stack-aware Web Development department. It supports frontend, backend, full-stack architecture, APIs, authentication, accessibility, performance, SEO, testing, security, privacy, and release-readiness work without assuming one framework. Components are applicability-based; Junie loads the guideline source and uses Skills only when relevant.

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

This package targets Junie CLI and Junie in JetBrains IDEs.

- `.junie/AGENTS.md`: project guidelines. Junie documents `.junie/AGENTS.md`, root `AGENTS.md`, and legacy guideline paths, with `.junie/AGENTS.md` having priority in this package.
- `.junie/skills/*/SKILL.md`: project Agent Skills using the open Agent Skills format.
- IDE setup: Junie is available in JetBrains IDEs where the Junie plugin or integrated Junie support is installed and enabled.
- CLI setup: Junie CLI is installed and authenticated separately by the user. This package stores no authentication data.
- No custom subagents are included because this package does not rely on EAP/limited subagent configuration.

## Included native components

- `.junie/AGENTS.md`: the single authoritative project guideline file for operating model, safety, quality gates, and completion behavior.
- `.junie/skills/*/SKILL.md`: project Skills for reusable web-development procedures.
- `README.md`: human setup and validation guide. It is not loaded by Junie.

## Installation and integration

1. Copy the contents of `junie/web-development/` to the target repository root so the target root contains `.junie/`.
2. Do not add a root `AGENTS.md` pointer for this package; `.junie/AGENTS.md` is the only retained guideline source.
3. Open the repository with Junie in a JetBrains IDE or start Junie CLI from the repository root.
4. Review the guideline and Skill files before allowing Junie to act on the repository.
5. Keep MCP, provider keys, model configuration, hooks, commands, remote agents, subagents, terminal auto-execution, deployment, publication, and external integrations disabled unless separately reviewed and authorized.
6. Verify discovery by asking Junie to summarize the Web Development guidelines and list available `.junie/skills/` Skills.

## How to use

Start Junie in the target repository and describe the task. Ask for a Skill by purpose or name when helpful, such as `stack-discovery`, `frontend-delivery`, `backend-api-auth`, `security-privacy-review`, or `release-readiness`. Junie may plan and execute code work depending on IDE/CLI settings, but runtime commands, tests, file edits, and external actions still require human approval according to the active surface.

## Operating model

Junie follows `.junie/AGENTS.md`, discovers the stack, confirms scope and acceptance criteria, uses Skills for focused procedures, separates implementation from independent review, and reports `PASS`, `FAIL`, `BLOCKED`, `NOT APPLICABLE`, or `NOT EXECUTED` with direct evidence. No simulated custom agents are included.

## Examples

- Feature/architecture: ask with Junie in the target repository to plan a passwordless login flow for the current web app. State: `Do not deploy or install packages.`
- Review/audit: request security/privacy review for CSP, cookies, CSRF, CORS, authorization, logging, third-party scripts, and sensitive data handling.
- Stack selection: provide repository evidence and ask the department to use only applicable Web Development specialists for React, Rails, Django, Laravel, static-site, or other detected stacks.
- Project customization: add `Node 22, pnpm only, WCAG 2.2 AA, LCP budget 2.5s, Playwright smoke tests` to task criteria without editing core department files.
- Sensitive action: request a deployment, publication, package-install, or Git checklist without executing it; actual external action requires separate human approval.

## Project-specific and user-specific configuration

The department is already specialized. Already specialized and normally not modified:  .junie/AGENTS.md and Skills, review responsibilities, security/privacy responsibilities, accessibility/performance/SEO responsibilities, testing responsibilities, quality gates, and the operating model. Project/user values may include framework and runtime versions, package manager policy, repository layout, code style, lint/format/test commands, coverage thresholds, browser support matrix, WCAG target, performance budgets, Core Web Vitals thresholds, SEO requirements, API conventions, auth provider, database/storage technology, approved dependencies, deployment target, CI/CD commands, environment names, feature-flag conventions, observability provider, logging requirements, organization security policy, privacy/legal requirements, data classification, approval owners, release process, branch strategy, protected branches, allowed external integrations, MCP servers or connectors, private endpoints, organization IDs, and workspace IDs. Never hard-code or commit API keys, tokens, passwords, private keys, production credentials, real secret values, or sensitive private URLs; use placeholders or environment-variable names. Project-specific configuration extends the department; it does not create the specialization.

## Safety and human approval

This package does not authorize automatic deployment, publication, authentication, secret use, spending, signing, submission, destructive operations, dependency installation, Git mutation, MCP use, provider-key use, terminal execution, remote agents, subagents, or production changes. Every sensitive or external action requires exact human authorization in the active Junie surface.

## Limitations

- Guidelines and Skills are instructions, not deterministic enforcement.
- Junie CLI and IDE behavior can differ by installed version, plugin state, model provider, and account configuration.
- Skill and guideline loading were not tested in a live Junie session.
- No runtime validation, browser checks, builds, tests, hooks, MCP, command execution, remote agents, or subagents were executed.

## Validation

- Syntax validation: retained Skill YAML frontmatter was parsed.
- Schema/static validation: retained files were mapped to `.junie/AGENTS.md` and `.junie/skills/`; the shadowed root `AGENTS.md` pointer was removed; no legacy guideline path, custom subagent, hook, MCP, provider key, command, or remote-agent configuration remains.
- Actual product loading: `NOT EXECUTED`.
- Runtime tests: `NOT EXECUTED`.
- Browser/build/deployment checks: `NOT EXECUTED`.

## Official documentation

Verified on July 20, 2026:

- Junie Docs: Getting started - https://junie.jetbrains.com/docs/
- Junie Docs: Guidelines and memory - https://junie.jetbrains.com/docs/guidelines-and-memory.html
- Junie Docs: Agent skills - https://junie.jetbrains.com/docs/agent-skills.html
- JetBrains Help: Junie by JetBrains - https://www.jetbrains.com/help/ai-assistant/junie-agent.html
- Junie Docs: Subagents - https://junie.jetbrains.com/docs/junie-cli-subagents.html
