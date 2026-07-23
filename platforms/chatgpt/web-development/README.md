# Web Development — ChatGPT

## Department overview

This is a manual ChatGPT configuration package for a stack-aware Web Development department. It can support frontend, backend, full-stack architecture, APIs, authentication, accessibility, performance, SEO, testing, security, privacy, and release-readiness work across different web stacks. Components are applicability-based; a task should use only the relevant instruction, knowledge, or Skill surface.

## Possible uses

- Discovering an existing web stack from uploaded or pasted project evidence.
- Planning a web feature or architecture decision.
- Implementing or reviewing frontend changes.
- Designing or reviewing APIs, authentication, sessions, cookies, CSP, CORS, and privacy behavior.
- Debugging regressions from supplied files, logs, screenshots, or test output.
- Auditing accessibility, performance, responsive behavior, browser compatibility, and SEO.
- Reviewing dependencies, third-party scripts, trackers, and supply-chain risk.
- Preparing release-readiness evidence and rollback notes.
- Reviewing architecture and migration decisions.

## Supported product surface

This package targets manual ChatGPT surfaces only. ChatGPT does not auto-discover this repository directory and this package is not executable configuration.

- ChatGPT Projects: available to logged-in ChatGPT users; project files, project sources, and project instructions are configured in the ChatGPT UI. Project instructions apply only inside that project and override global custom instructions.
- Custom GPTs: available only to users and managed workspaces with GPT creation/editing enabled. Configure them manually in the GPT builder; mobile clients may be limited for building/editing.
- Skills in ChatGPT: available for eligible Business, Enterprise, Healthcare, and Edu users, subject to workspace permissions, admin controls, surface differences, and rollout. Personal Skills must be installed separately across desktop and web/mobile surfaces.
- Workspace Agents: available in eligible Business, Enterprise, and Edu workspaces, subject to role permissions, admin enablement, app/tool controls, region, and rollout. They are created in the Agents builder and can include files, Skills, apps, tools, channels, schedules, and API triggers only when enabled by workspace policy.
- Apps/connectors and GPT Actions are optional manual integrations. None are configured, connected, trusted, or enabled by this package.

## Included native components

- `project-instructions.md`: paste into ChatGPT Project settings, a Custom GPT instruction field, or a Workspace Agent instruction field when that surface is the single primary surface for the task.
- `knowledge/*.md`: upload as Project sources, GPT Knowledge, or Workspace Agent files as factual reference material. These files are not hidden instructions.
- `skills/*/SKILL.md`: install or create as ChatGPT Skills only where the Skills UI and workspace policy allow uploaded or user-created Skills.
- `README.md`: human setup and validation guide. It is not loaded by ChatGPT.

## Installation and integration

1. Choose one primary ChatGPT surface: Project, Custom GPT, or Workspace Agent. Avoid installing the same full instruction body into more than one active surface for the same task.
2. For a Project, create or open the project, paste `project-instructions.md` into Project settings, and upload only safe reference material from `knowledge/`.
3. For a Custom GPT, create or edit a GPT named `Web Development Department`, paste `project-instructions.md` into Instructions, upload the `knowledge/` files, and leave Apps or Actions disabled unless separately approved.
4. For a Workspace Agent, create a blank agent named `Web Development Department`, paste `project-instructions.md` into Instructions, attach safe `knowledge/` files, attach Skills only if available, and keep apps, custom MCPs, tools, schedules, API triggers, and Slack disabled unless explicitly reviewed.
5. Install Skills from `skills/` only after reviewing their contents and confirming that workspace permissions allow Skill creation, uploading, installation, or sharing.
6. Verify discovery by starting a safe chat in the chosen surface and asking for the Web Development department operating model and unavailable checks.

Do not place secrets, production configuration, personal data, private endpoints, or privileged logs in project sources, GPT Knowledge, Skill files, or agent files.

## How to use

Start a chat in the configured Project, Custom GPT, or Workspace Agent and describe the task with available files or pasted evidence. Ask for a specific lens when needed, such as stack discovery, frontend delivery, backend/API/auth review, security/privacy review, accessibility/performance/SEO review, dependency review, architecture decision, testing/browser compatibility, or release readiness.

When Skills are installed, ChatGPT may use them automatically when relevant. A user can also ask directly, for example: `Use the security-privacy-review Skill to review this auth change.` Expected output should separate verified evidence from assumptions, mark unavailable checks as `NOT EXECUTED`, and require human review for sensitive or external actions.

## Operating model

The department first confirms scope, stack evidence, acceptance criteria, constraints, and approved actions. It then applies specialist lenses as needed, keeps implementation and independent review responsibilities separate, cites trusted evidence, and reports unresolved risks. Completion uses `PASS`, `FAIL`, `BLOCKED`, or `NOT APPLICABLE` gates, with `NOT EXECUTED` for checks that were not actually run.

## Examples

- Feature/architecture: ask in the configured Project, Custom GPT, or Workspace Agent to plan a passwordless login flow for the current web app. State: `Do not deploy or install packages.`
- Review/audit: request security/privacy review for CSP, cookies, CSRF, CORS, authorization, logging, third-party scripts, and sensitive data handling.
- Stack selection: provide repository evidence and ask the department to use only applicable Web Development specialists for React, Rails, Django, Laravel, static-site, or other detected stacks.
- Project customization: add `Node 22, pnpm only, WCAG 2.2 AA, LCP budget 2.5s, Playwright smoke tests` to task criteria without editing core department files.
- Sensitive action: request a deployment, publication, package-install, or Git checklist without executing it; actual external action requires separate human approval.

## Project-specific and user-specific configuration

The department is already specialized. Already specialized and normally not modified: Project/GPT instructions and Skills, review responsibilities, security/privacy responsibilities, accessibility/performance/SEO responsibilities, testing responsibilities, quality gates, and the operating model. Project/user values may include framework and runtime versions, package manager policy, repository layout, code style, lint/format/test commands, coverage thresholds, browser support matrix, WCAG target, performance budgets, Core Web Vitals thresholds, SEO requirements, API conventions, auth provider, database/storage technology, approved dependencies, deployment target, CI/CD commands, environment names, feature-flag conventions, observability provider, logging requirements, organization security policy, privacy/legal requirements, data classification, approval owners, release process, branch strategy, protected branches, allowed external integrations, MCP servers or connectors, private endpoints, organization IDs, and workspace IDs. Never hard-code or commit API keys, tokens, passwords, private keys, production credentials, real secret values, or sensitive private URLs; use placeholders or environment-variable names. Project-specific configuration extends the department; it does not create the specialization.

## Safety and human approval

This package does not authorize automatic deployment, publication, authentication, secret use, spending, signing, submission, destructive operations, dependency installation, Git mutation, connector setup, app actions, schedules, API triggers, Slack actions, or production changes. Each such action requires exact human authorization in the active ChatGPT surface and must also be supported by the configured product permissions.

## Limitations

- Static repository files here are not auto-loaded by ChatGPT.
- Availability varies by plan, role, administrator policy, region, device, workspace configuration, and staged rollout.
- Knowledge files and project sources are retrievable reference material, not a security boundary.
- Skills may include instructions, supporting files, and code; uploaded Skills are scanned by ChatGPT, but human review remains required.
- Runtime tests, builds, browser checks, app connections, Workspace Agent publishing, GPT publishing, and integrations were not executed.

## Validation

- Syntax validation: `SKILL.md` frontmatter was parsed for retained ChatGPT Skills.
- Schema/static validation: retained files were mapped to documented ChatGPT manual surfaces; no repository agent manifest, hooks, MCP configuration, action schemas, credentials, endpoints, or enabled connectors are included.
- Actual product loading: `NOT EXECUTED`.
- Runtime tests: `NOT EXECUTED`.
- Browser/build/deployment checks: `NOT EXECUTED`.

## Official documentation

Verified on July 20, 2026:

- OpenAI Help Center: Projects in ChatGPT - https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- OpenAI Help Center: Creating and editing GPTs - https://help.openai.com/en/articles/8554397-creating-and-editing-gpts
- OpenAI Help Center: Skills in ChatGPT - https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- OpenAI Help Center: Apps in ChatGPT - https://help.openai.com/en/articles/11487775-connectors-in-chatgpt
- OpenAI Help Center: ChatGPT Workspace Agents for Enterprise and Business - https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business
- OpenAI Help Center: ChatGPT Work and Codex - https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex
