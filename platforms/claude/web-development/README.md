# Web Development — Claude

## Department overview

This is a manual Claude project package for a stack-aware Web Development department. It supports frontend, backend, full-stack architecture, APIs, authentication, accessibility, performance, SEO, testing, security, privacy, and release-readiness work without assuming one framework. Components are applicability-based; not every task should invoke every specialist Skill or review lens.

## Possible uses

- Discovering an existing web stack from uploaded project evidence.
- Planning a web feature or architecture decision.
- Implementing or reviewing frontend changes.
- Designing or reviewing APIs, authentication, sessions, cookies, CSP, CORS, and privacy behavior.
- Debugging regressions from supplied files, logs, screenshots, or test output.
- Auditing accessibility, performance, responsive behavior, browser compatibility, and SEO.
- Reviewing dependencies, third-party scripts, trackers, and supply-chain risk.
- Preparing release-readiness evidence and rollback notes.
- Reviewing architecture and migration decisions.

## Supported product surface

This package targets Claude web and Claude Desktop manual project surfaces. Claude does not auto-discover this repository directory and this package is not executable configuration.

- Claude Projects: available to all Claude users, with free accounts limited by documented project limits. Project instructions and Project Knowledge are configured manually in the Claude UI.
- Project Knowledge: files uploaded to a Project are used as context across chats in that Project. Paid plans may enable expanded Project Knowledge with RAG as content approaches context limits.
- Project sharing: Team and Enterprise plans can share Projects with organization members according to workspace visibility and permissions.
- claude.ai custom Skills: available on Pro, Max, Team, and Enterprise plans when code execution is enabled. Custom Skills are uploaded as zip files through Claude settings, are user-specific on claude.ai, and do not centrally distribute to the organization.
- Claude Code, Claude API Skills, and MCP are separate surfaces. This directory intentionally contains no `.claude/` files, SDK code, MCP configuration, connector configuration, shell permissions, or repository automation.

## Included native components

- `project-instructions.md`: paste into the Claude Project `Set project instructions` field.
- `project-knowledge/*.md`: upload to Claude Project Knowledge as factual reference material, not hidden instructions.
- `skills/*/SKILL.md`: package each Skill folder as a custom Claude Skill only where Skills are available and permitted.
- `README.md`: human setup and validation guide. It is not loaded by Claude.

## Installation and integration

1. Open Claude web or Claude Desktop and create a Project named `Web Development Department`.
2. Add a human-readable Project description, but do not rely on the description as model instructions.
3. Paste the full contents of `project-instructions.md` into `Set project instructions`.
4. Upload only reviewed files from `project-knowledge/` into Project Knowledge.
5. If claude.ai Skills are available, review each folder in `skills/`, package one Skill folder at a time, upload it through Claude settings, and enable only the Skills needed for this Project.
6. Leave connectors, MCP, desktop extensions, external tools, scripts, write actions, deployment, publication, and Git mutation disabled unless a human approves the exact provider, permissions, data flow, retention, and external effects.
7. Start a safe Project chat and verify that Claude distinguishes uploaded knowledge from instructions, marks unexecuted checks as `NOT EXECUTED`, and asks for approval before external or destructive actions.

## How to use

Start a chat inside the configured Claude Project and provide the files, snippets, screenshots, logs, or decisions needed for the task. Ask for a specific lens when appropriate, such as stack discovery, frontend delivery, backend/API/auth review, security/privacy review, accessibility/performance/SEO review, dependency review, architecture decision, testing/browser compatibility, or release readiness.

When custom Skills are installed in claude.ai, Claude can trigger a Skill when the request matches the Skill description. A user can also ask directly, for example: `Use the testing-browser-compatibility Skill to review this change.` Expected output should separate evidence from assumptions and mark unavailable runtime checks as `NOT EXECUTED`.

## Operating model

The department confirms scope, stack evidence, acceptance criteria, constraints, and approved actions before recommending work. It applies specialist lenses only when relevant, keeps implementers and independent reviewers separate, cites evidence, and reports unresolved risks. Final review uses `PASS`, `FAIL`, `BLOCKED`, or `NOT APPLICABLE` gates, with `NOT EXECUTED` for checks that were not actually run.

## Examples

- Feature/architecture: ask in the configured Claude Project to plan a passwordless login flow for the current web app. State: `Do not deploy or install packages.`
- Review/audit: request security/privacy review for CSP, cookies, CSRF, CORS, authorization, logging, third-party scripts, and sensitive data handling.
- Stack selection: provide repository evidence and ask the department to use only applicable Web Development specialists for React, Rails, Django, Laravel, static-site, or other detected stacks.
- Project customization: add `Node 22, pnpm only, WCAG 2.2 AA, LCP budget 2.5s, Playwright smoke tests` to task criteria without editing core department files.
- Sensitive action: request a deployment, publication, package-install, or Git checklist without executing it; actual external action requires separate human approval.

## Project-specific and user-specific configuration

The department is already specialized. Already specialized and normally not modified: Project instructions and Skills, review responsibilities, security/privacy responsibilities, accessibility/performance/SEO responsibilities, testing responsibilities, quality gates, and the operating model. Project/user values may include framework and runtime versions, package manager policy, repository layout, code style, lint/format/test commands, coverage thresholds, browser support matrix, WCAG target, performance budgets, Core Web Vitals thresholds, SEO requirements, API conventions, auth provider, database/storage technology, approved dependencies, deployment target, CI/CD commands, environment names, feature-flag conventions, observability provider, logging requirements, organization security policy, privacy/legal requirements, data classification, approval owners, release process, branch strategy, protected branches, allowed external integrations, MCP servers or connectors, private endpoints, organization IDs, and workspace IDs. Never hard-code or commit API keys, tokens, passwords, private keys, production credentials, real secret values, or sensitive private URLs; use placeholders or environment-variable names. Project-specific configuration extends the department; it does not create the specialization.

## Safety and human approval

This package does not authorize automatic deployment, publication, authentication, secret use, spending, signing, submission, destructive operations, dependency installation, Git mutation, connector setup, MCP setup, desktop extension use, or production changes. Each such action requires exact human authorization in the active Claude surface and must also be supported by the configured product permissions.

## Limitations

- Static repository files here are not auto-loaded by Claude.
- Product availability varies by plan, workspace role, administrator policy, device, and rollout.
- Project Knowledge is context material, not an access-control boundary.
- claude.ai custom Skills are user-specific and must be uploaded separately from Claude Code and API Skills.
- Runtime tests, builds, browser checks, connector setup, Skill upload, Project creation, and integrations were not executed.

## Validation

- Syntax validation: `SKILL.md` YAML frontmatter was parsed for retained Claude Skills.
- Schema/static validation: retained files were mapped to documented Claude Projects, Project Knowledge, and custom Skill mechanisms; no `.claude/`, MCP, connector, shell, credential, endpoint, or repository automation file is included.
- Actual product loading: `NOT EXECUTED`.
- Runtime tests: `NOT EXECUTED`.
- Browser/build/deployment checks: `NOT EXECUTED`.

## Official documentation

Verified on July 20, 2026:

- Claude Help Center: What are projects? - https://support.claude.com/en/articles/9517075-what-are-projects
- Claude Help Center: How can I create and manage projects? - https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
- Claude Platform Docs: Agent Skills - https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Claude Help Center: When to use desktop and web connectors - https://support.claude.com/en/articles/11725091-when-to-use-desktop-and-web-connectors
- Claude Help Center: Use the GitHub integration - https://support.claude.com/en/articles/10167454-use-the-github-integration
