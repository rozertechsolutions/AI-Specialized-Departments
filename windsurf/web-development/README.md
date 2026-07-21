# Web Development — Windsurf / Devin Desktop

## Department overview

This is a professional Web Development department for Devin Desktop / Cascade-compatible Windsurf workspaces. It is already specialized for Web Development and is not a generic AI template awaiting manual specialization. It is stack-aware rather than tied to one framework and covers frontend, backend/API, architecture, authentication and authorization, sessions and cookies, storage and integrations, responsive design, accessibility, performance and Core Web Vitals, SEO and crawlability, browser compatibility, testing, dependency and supply-chain review, security and privacy, observability, and release readiness.

The lead selects applicable specialists and workflows according to project evidence. The package is intended to work immediately after installation; customization supplies local constraints, not the core specialization.

## Possible uses

- Discover an existing web stack and conventions.
- Understand unfamiliar frontend, backend, or full-stack code.
- Plan or review a new web feature.
- Review REST, GraphQL, WebSocket, or webhook APIs when applicable.
- Review authentication, authorization, sessions, cookies, CSP, CORS, CSRF, validation, privacy, and secure data handling.
- Debug web regressions.
- Audit responsive behavior, accessibility, performance, Core Web Vitals, SEO, metadata, structured data, crawlability, and rendering strategy.
- Review dependency and supply-chain risks.
- Prepare testing, observability, rollback, browser compatibility, and release-readiness evidence.

## Supported product surface

This package targets current Devin Desktop / Cascade workspace configuration. It uses root `AGENTS.md`, current workspace Rules in `.devin/rules/`, Cascade workspace Skills in `.windsurf/skills/<skill>/SKILL.md`, and Cascade workflows in `.windsurf/workflows/*.md`. It is static configuration, not an SDK, hook package, MCP server, App Deploy setup, browser automation package, or external integration.

Current official documentation prefers `.devin/rules/*.md` for workspace Rules. `.windsurf/rules/` is legacy fallback only and is not retained here. Current official documentation still uses `.windsurf/skills/` and `.windsurf/workflows/` for Cascade workspace Skills and Workflows.

## Included native components

- `AGENTS.md`: repository-root instruction surface for Devin-compatible agents; defines Web Development scope, evidence, review model, and stop conditions.
- `.devin/rules/web-development.md`: current workspace Rule loaded by Devin Desktop / Cascade for always-on Web Development behavior.
- `.devin/rules/quality-gates.md`: current workspace Rule for readiness, security, privacy, accessibility, performance, SEO, testing, and human-review gates.
- `.windsurf/skills/<skill>/SKILL.md`: Cascade workspace Skills for stack discovery, architecture decisions, frontend delivery, backend/API/auth, security/privacy, accessibility/performance/SEO, testing/browser compatibility, dependency review, and release readiness.
- `.windsurf/workflows/*.md`: manual Cascade workflow slash commands for planning, implementation support, debugging, audits, dependency review, API/auth review, and release readiness.

Rules are automatic according to their triggers. Skills may be selected by the model or invoked by the user where the product exposes Skills. Workflows are manual slash-command runbooks.

## Installation and integration

1. Install/open Devin Desktop or Cascade-compatible Windsurf.
2. Open the actual target Git repository.
3. Copy `windsurf/web-development/AGENTS.md` to the target repository root.
4. Copy `windsurf/web-development/.devin/rules/` to the target repository root as `.devin/rules/`.
5. Copy `windsurf/web-development/.windsurf/skills/` and `.windsurf/workflows/` to the target repository root.
6. Keep `.devin/` and `.windsurf/` as hidden project directories.
7. Reopen, reload, or refresh the workspace if discovery has already occurred.
8. Verify the Web Development Rules, Skills, and Workflows are visible or active in the product.
9. Keep hooks, MCP, App Deploy, browser automation, remote connectors, and external integrations disabled unless the user explicitly configures them.

## How to use

Use the lead behavior through normal Cascade/Devin chat:

```text
Plan a checkout address form and session API review. Use applicable Web Development specialists. Do not deploy, install packages, publish, or mutate Git.
```

Use a manual workflow slash command when available:

```text
/plan-web-change Add passwordless login to the existing web app with security and rollback review.
```

```text
/review-security-and-privacy Review authz, cookies, CSP, CORS, CSRF, logging, and sensitive data handling.
```

`PASS` requires evidence. `FAIL` means defects remain. `BLOCKED` means required scope, evidence, permission, approval, credential, or product decision is missing. `NOT_APPLICABLE` must include a reason. `NOT_EXECUTED` is not a pass.

## Operating model

1. Task and scope intake.
2. Existing-project stack discovery.
3. Acceptance criteria confirmation.
4. Applicable specialist/Skill/workflow selection.
5. Proposal or implementation support.
6. Security/privacy review.
7. Accessibility, performance, SEO, testing, and release-readiness review.
8. Independent final review.
9. Evidence reconciliation.
10. Human approval where required.
11. Final result.

Framework-specific behavior is adapted from detected project evidence. Devin Local and Cascade compatibility can differ by product rollout; install only the surfaces supported in the active product.

## Examples

- Feature development: `/implement-web-change Add a React form with server validation, no dependency changes without approval.`
- Review/audit: `/audit-accessibility-performance-seo Audit keyboard flow, focus, responsive layout, LCP, CLS, metadata, canonical tags, and crawlability.`
- Stack selection: if the repository shows Phoenix LiveView, Skills adapt review guidance to LiveView rather than assuming SPA behavior.
- Project customization: add "Elixir 1.17, Phoenix 1.8, WCAG 2.2 AA, p95 LCP 2.5s, no new dependencies" in project criteria without editing Skills or Rules.
- Sensitive action: "Prepare deployment readiness and rollback notes; do not deploy" is review-only. Actual deployment, publication, Git push, package installation, authentication, or secret access remains human-controlled.

## Project-specific and user-specific configuration

Already specialized and normally not modified: agents/specialist responsibilities, Skills, workflows, Rules, review responsibilities, security responsibilities, accessibility/performance/SEO responsibilities, testing responsibilities, quality gates, and the operating model.

Project/user values may include framework and runtime versions, package manager policy, repository layout, code style, lint/format/test commands, coverage thresholds, browser support, WCAG target, performance budgets, SEO rules, API conventions, auth provider, database/storage, approved dependencies, dependency policies, deployment provider, CI/CD commands, environments, feature flags, observability, logging, organization security policy, privacy/legal requirements, data classification, approval owners, release process, branch strategy, protected branches, allowed integrations, MCP servers/connectors, private endpoints, organization IDs, and workspace IDs.

Never hard-code or commit API keys, tokens, passwords, private keys, production credentials, real secret values, or sensitive private URLs. Project-specific configuration extends the department; it does not create the specialization.

## Safety and human approval

The product and user permissions determine whether file edits or command execution can occur. This package does not configure hooks, MCP, App Deploy, browser automation, deployment, publication, package installation, Git mutation, authentication, secret access, spending, signing, submission, destructive operations, or external integrations. Require explicit human approval for production, external systems, auth/authz, cryptography, secrets, sensitive data, database migrations, dependencies, tracking, payments, DNS, certificates, signing, publishing, deployment, release, merge, and destructive operations.

## Limitations

Static validation cannot prove live product discovery, model behavior, browser behavior, runtime tests, deployment, publication, or external integration behavior. Devin Desktop, Cascade, and Devin Local compatibility may vary by product version and rollout. Checks not executed must remain `NOT_EXECUTED`.

## Validation

Validated July 21, 2026: root `AGENTS.md` exists, `.devin/rules/` contains current workspace Rules with valid frontmatter, legacy `.windsurf/rules/` copies are removed, `.windsurf/skills/` and `.windsurf/workflows/` remain current native surfaces, Markdown references resolve, no secrets are included, and no hooks/MCP/App Deploy/browser automation/external integrations are configured. Live Devin Desktop/Cascade loading and live model runs were not executed.

## Official documentation

Verified July 21, 2026:

- Devin documentation: https://docs.devin.ai/
- Devin / Cascade rules: https://docs.devin.ai/workspaces/rules
- Windsurf/Cascade Skills: https://docs.windsurf.com/
- Windsurf/Cascade Workflows: https://docs.windsurf.com/
