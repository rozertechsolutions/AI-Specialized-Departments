# Web Development — Qwen Code

## Department overview

This is a professional Web Development department for Qwen Code. It is already specialized for Web Development and is not a generic AI template awaiting manual specialization. It is stack-aware rather than tied to one framework and covers frontend, backend/API, architecture, authentication and authorization, sessions and cookies, storage and integrations, responsive design, accessibility, performance and Core Web Vitals, SEO and crawlability, browser compatibility, testing, dependency and supply-chain review, security and privacy, observability, and release readiness.

The lead selects applicable specialists from detected project evidence instead of invoking every specialist blindly. The department works immediately after project installation; customization supplies local constraints and policies.

## Possible uses

- Discover an existing web stack and repository layout.
- Understand unfamiliar frontend, backend, or full-stack code.
- Plan or review a new web feature.
- Review REST, GraphQL, WebSocket, or webhook APIs when applicable.
- Review authentication, authorization, sessions, cookies, CSP, CORS, CSRF, validation, privacy, and secure data handling.
- Debug web regressions.
- Audit responsive behavior, accessibility, performance, Core Web Vitals, SEO, metadata, structured data, crawlability, and rendering strategy.
- Review dependencies and supply-chain risks.
- Prepare testing and release-readiness evidence, including rollback and observability considerations.

## Supported product surface

This package targets Qwen Code project discovery. It uses root `QWEN.md`, `.qwen/settings.json`, project agents in `.qwen/agents/`, and project Skills in `.qwen/skills/<skill>/SKILL.md`. It is static project configuration, not an SDK or deployment package. Qwen Code must be installed and opened in the target repository.

The included `.qwen/settings.json` sets `model.maxSubagentDepth` to `2`. Current Qwen Code documentation describes this as a 1-based nesting limit: the root interaction can call the lead, and the lead can call one specialist layer. Specialists must not spawn another nested specialist layer.

## Included native components

- `QWEN.md`: project-level instruction file discovered from the target repository root; defines the Web Development operating model, evidence rules, and stop conditions.
- `.qwen/settings.json`: native project settings; configures `model.maxSubagentDepth = 2`.
- `.qwen/agents/web-development-lead.md`: lead agent for intake, routing, review reconciliation, and final result.
- `.qwen/agents/*specialist*.md` and `*reviewer*.md`: architecture, frontend, backend/API, security/privacy, accessibility/performance/SEO, and quality/release agents.
- `.qwen/skills/<skill>/SKILL.md`: project Skills for stack discovery, frontend delivery, backend/API/auth, security/privacy, accessibility/performance/SEO, testing/browser compatibility, dependency review, release readiness, and architecture decisions.

## Installation and integration

1. Install Qwen Code and open the actual target Git repository.
2. Copy `qwen-code/web-development/QWEN.md` to the target repository root.
3. Copy the hidden `.qwen/` directory to the target repository root.
4. Keep `.qwen/settings.json`, `.qwen/agents/`, and `.qwen/skills/` in the hidden `.qwen` directory.
5. Reopen, reload, or restart Qwen Code if required for project discovery.
6. Verify that Qwen Code sees `QWEN.md`, the Web Development lead, specialists, and Skills.
7. Keep optional tools, connectors, shell access, web access, and external integrations disabled unless the project owner explicitly configures them.

If the workspace is trusted or a global approval mode is permissive, that parent mode can influence subagent permission behavior according to current Qwen Code documentation. This package cannot override a user's globally permissive runtime mode by itself.

## How to use

Ask Qwen Code to use the Web Development lead for broad work:

```text
Use the web-development-lead to review the checkout page and API session handling. Do not install dependencies, deploy, publish, or mutate Git.
```

Direct a specialist only for clearly scoped work:

```text
Use the security-privacy-reviewer to review CSP, cookies, CSRF, CORS, logging, and sensitive data handling.
```

Invoke a Skill by name when supported by the product UI or prompt:

```text
Use the stack-discovery Skill, then select only applicable Web Development specialists.
```

`PASS` requires evidence from applicable reviews. `FAIL` reports defects. `BLOCKED` means missing scope, evidence, permission, approval, credentials, or product decision. `NOT_APPLICABLE` must include a reason. `NOT_EXECUTED` is not a pass.

## Operating model

1. Task and scope intake.
2. Existing-project stack discovery.
3. Acceptance criteria confirmation.
4. Applicable specialist selection under the root -> lead -> one specialist layer limit.
5. Proposal or implementation support.
6. Security/privacy review.
7. Accessibility, performance, SEO, testing, and release-readiness review.
8. Independent final review.
9. Evidence reconciliation.
10. Human approval where required.
11. Final result.

Framework behavior is adapted from detected project evidence rather than requiring users to rewrite the department.

## Examples

- Feature development: ask the lead to plan a Vue dashboard and REST endpoint; it can route to frontend, backend/API, security, accessibility/performance/SEO, and release review.
- Review/audit: ask the security/privacy reviewer to audit auth middleware, session cookies, logging, and third-party scripts.
- Stack selection: if the snapshot shows Django templates and HTMX, the frontend review adapts to that stack rather than assuming React.
- Project customization: supply "Python 3.12, Django 5, PostgreSQL, ruff, pytest, WCAG 2.2 AA, p95 LCP 2.5s" in project instructions or task criteria without changing core agents.
- Sensitive action: "Prepare npm install documentation; do not run it" is allowed. "Run npm install" depends on Qwen Code permissions and should require explicit human approval outside this package.

## Project-specific and user-specific configuration

Already specialized and normally not modified: agents, specialists/subagents, Skills, review responsibilities, security responsibilities, accessibility/performance/SEO responsibilities, testing responsibilities, quality gates, and the operating model.

Project/user values may include framework and runtime versions, package manager policy, repository layout, lint/format/test commands, coverage thresholds, browser support, WCAG target, performance budgets, SEO requirements, API conventions, auth provider, database/storage, approved dependencies, deployment provider, CI/CD names, environments, feature flags, observability provider, logging requirements, organization security policy, privacy/legal requirements, data classification, approval owners, release process, branch strategy, protected branches, allowed integrations, MCP servers/connectors, local model/runtime/provider configuration, private endpoints, organization IDs, and workspace IDs.

Never hard-code or commit API keys, tokens, passwords, private keys, production credentials, real secret values, or sensitive private URLs. Project-specific configuration extends the department; it does not create the specialization.

## Safety and human approval

Qwen Code permissions and approval mode determine whether file edits, commands, or tool calls can actually execute. This package documents strict review behavior but cannot defeat a globally permissive user runtime. Package installation, command execution, Git mutation, deployment, publication, authentication, secret access, spending, signing, submission, destructive operations, and external integrations require human authorization and should be treated as non-executing unless explicitly approved in the product.

## Limitations

Static validation cannot prove Qwen Code UI discovery or live model behavior. Approval-mode inheritance and trusted-folder settings are controlled by the user environment. Runtime tests, browser tests, deployment tests, API calls, and external integrations are `NOT_EXECUTED` unless the user runs them separately.

## Validation

Validated July 21, 2026: `QWEN.md` exists, `.qwen/settings.json` parses as JSON, `model.maxSubagentDepth = 2` is present, agent and Skill paths are current, internal references resolve, reviewers are read-only by instruction, and no secrets or active external integrations are included. Live Qwen Code loading and live model runs were not executed.

## Official documentation

Verified July 21, 2026:

- Qwen Code documentation: https://qwenlm.github.io/qwen-code/
- Configuration: https://qwenlm.github.io/qwen-code/docs/cli/configuration
- Agents/subagents: https://qwenlm.github.io/qwen-code/docs/cli/agents
- Skills: https://qwenlm.github.io/qwen-code/docs/cli/skills
