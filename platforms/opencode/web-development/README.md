# Web Development — OpenCode

## Department overview

This is a professional Web Development department for OpenCode. It is already specialized for Web Development and is not a generic AI template awaiting manual specialization. It is stack-aware rather than tied to one framework and covers frontend, backend/API, architecture, authentication and authorization, sessions and cookies, storage and integrations, responsive design, accessibility, performance and Core Web Vitals, SEO and crawlability, browser compatibility, testing, dependency and supply-chain review, security and privacy, observability, and release readiness.

The lead and specialists are selected according to task applicability rather than invoked blindly. After installation, the department can be used immediately; customization is for project constraints, not for creating the specialization.

## Possible uses

- Discover an existing web stack and repository conventions.
- Understand an unfamiliar frontend, backend, or full-stack project.
- Plan or review a web feature.
- Review REST, GraphQL, WebSocket, or webhook APIs when applicable.
- Review authentication, authorization, sessions, cookies, CSP, CORS, CSRF, validation, privacy, and secure data handling.
- Debug web regressions.
- Audit responsive behavior, accessibility, performance, Core Web Vitals, SEO, metadata, structured data, crawlability, and rendering strategy.
- Review dependencies and supply-chain risks.
- Prepare testing, browser compatibility, observability, rollback, and release-readiness evidence.

## Supported product surface

This package targets OpenCode project configuration. It uses root `AGENTS.md`, `opencode.json`, project Markdown agents in `.opencode/agents/`, custom commands in `.opencode/commands/`, and project Skills in `.opencode/skills/<name>/SKILL.md`. It is static configuration, not an executable SDK package. OpenCode must be installed by the user, and native discovery happens in the target repository.

The included `opencode.json` keeps editing, bash, task/subtask, web fetch/search, and external directory access denied by default. `subtask: false` behavior belongs to commands that stay on the configured primary lead instead of spawning an extra task.

## Included native components

- `AGENTS.md`: repository-level OpenCode instructions loaded at the target repository root; defines Web Development scope, stop conditions, evidence expectations, and human-review boundaries.
- `opencode.json`: project configuration and permission policy; keeps reviewers read-only and sensitive operations denied unless the user changes policy.
- `.opencode/agents/web-development-lead.md`: primary lead agent for intake, routing, review reconciliation, and final result.
- `.opencode/agents/*specialist*.md` and `*reviewer*.md`: native specialist agents for architecture, frontend, backend/API, security/privacy, accessibility/performance/SEO, and quality/release review.
- `.opencode/commands/*.md`: manual slash-command workflows for planning, implementation support, reviews, debugging, dependency review, and release readiness.
- `.opencode/skills/<skill>/SKILL.md`: reusable project Skills for stack discovery, frontend delivery, backend/API/auth, security/privacy, accessibility/performance/SEO, testing/browser compatibility, dependency review, release readiness, and architecture decisions.

## Installation and integration

1. Install OpenCode and open the actual target Git repository.
2. Copy `opencode/web-development/AGENTS.md` to the target repository root as `AGENTS.md`.
3. Copy `opencode/web-development/opencode.json` to the target repository root as `opencode.json`.
4. Copy the entire hidden `.opencode/` directory to the target repository root.
5. Keep `.opencode/agents/`, `.opencode/commands/`, and `.opencode/skills/` as hidden project directories.
6. Reopen or reload OpenCode if project configuration was already loaded.
7. Verify discovery by checking that the Web Development lead, specialist agents, slash commands, and Skills are available.
8. Keep optional integrations disabled by default; add project-specific MCP, web, shell, or external permissions only after local review.

No secrets, tokens, private endpoints, or organization IDs are required by this package.

## How to use

Select or cycle to the Web Development lead as the primary agent, then describe the task with scope and acceptance criteria. Use direct specialist agents only when the task is clearly owned by one surface, for example a security/privacy review.

Examples of supported OpenCode usage:

```text
Ask the web-development-lead:
Plan a passwordless login flow for this Next.js app. Do not deploy or install packages.
```

```text
/review-api-and-auth Review session cookie handling for the current Express API.
```

```text
/audit-accessibility-performance-seo Audit the product detail page for WCAG, LCP, CLS, metadata, and crawlability risks.
```

Skills may be invoked by OpenCode when useful, or referenced explicitly by name when the UI supports Skill selection. A `PASS` means the applicable reviews and evidence support the result. `FAIL` means a defect was found. `BLOCKED` means required scope, evidence, permission, credentials, approval, or product decision is missing. `NOT_APPLICABLE` and `NOT_EXECUTED` must not be treated as `PASS`.

## Operating model

1. Task and scope intake.
2. Stack and convention discovery from repository evidence.
3. Acceptance criteria confirmation.
4. Applicable specialist selection.
5. Proposal or implementation support within the configured permission policy.
6. Security/privacy review.
7. Accessibility, performance, SEO, testing, and release-readiness review.
8. Independent final quality review.
9. Evidence reconciliation.
10. Human approval for sensitive actions.
11. Final result.

Framework-specific behavior is adapted from detected project files and conventions.

## Examples

- Feature development: ask the lead to plan a React checkout form and API endpoint; it routes frontend, backend/API, security, accessibility/performance/SEO, and testing review.
- Review/audit: run `/review-security-and-privacy Review auth middleware, CSP, cookies, logging, and sensitive data handling.`
- Stack selection: if discovery finds Rails views and Stimulus, the frontend review adapts to that stack instead of assuming React.
- Project customization: add local acceptance criteria such as "pnpm only, Node 22, WCAG 2.2 AA, Playwright smoke tests" in the prompt or project instructions without editing core agents.
- Sensitive action: "Prepare a Git push checklist; do not push" is allowed as documentation. "Git push main" remains denied by default permissions and requires human execution outside this package.

## Project-specific and user-specific configuration

Already specialized and normally not modified: agents, specialists/subagents, Skills, workflows, review responsibilities, security responsibilities, accessibility/performance/SEO responsibilities, testing responsibilities, quality gates, and the operating model.

Project/user values may include framework and runtime versions, package manager policy, repository layout, lint/format/test commands, coverage thresholds, browser support, WCAG target, performance budgets, SEO rules, API conventions, auth provider, database/storage, approved dependencies, deployment provider, CI/CD names, environments, feature flags, observability, security policy, privacy/legal requirements, data classification, approval owners, release process, branch strategy, protected branches, allowed integrations, MCP servers, private endpoints, organization IDs, and workspace IDs.

Never hard-code or commit API keys, tokens, passwords, private keys, production credentials, real secret values, or sensitive private URLs. Project-specific configuration extends the department; it does not create the specialization.

## Safety and human approval

OpenCode may edit files or run commands only if the user changes permissions or grants approval in the actual product. This package denies edit, bash, task, web, and external directory access by default. Package installation, Git mutation, deployment, publication, authentication, secret access, spending, signing, submission, destructive operations, and external integrations require explicit human action and should remain non-executing in reviews unless locally authorized.

## Limitations

This package cannot guarantee native loading until copied into and opened by OpenCode in the target repository. Runtime tests, browser tests, deployment tests, live integrations, and model behavior are not executed by static validation. Permission inheritance from user/global OpenCode settings remains the user's responsibility.

## Validation

Validated July 21, 2026: required files exist, JSON parses, Markdown paths resolve, native component paths match current OpenCode docs, command and specialist references are internal, reviewers are documented as read-only, and no secrets or active external integrations are included. Actual OpenCode UI loading and live model runs were not executed.

## Official documentation

Verified July 21, 2026:

- OpenCode documentation: https://opencode.ai/docs/
- Agents: https://opencode.ai/docs/agents/
- Commands: https://opencode.ai/docs/commands/
- Skills: https://opencode.ai/docs/skills/
- Configuration and permissions: https://opencode.ai/docs/config/
