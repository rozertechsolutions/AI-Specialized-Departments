# Web Development — GitHub Copilot

## Department overview

This is a repository-scoped GitHub Copilot specialization for a stack-aware Web Development department. It supports frontend, backend, full-stack architecture, APIs, authentication, accessibility, performance, SEO, testing, security, privacy, and release-readiness work without assuming one framework. Components are applicability-based; Copilot uses only the relevant instructions, agent profile, prompt file, or Skill for a task.

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

This package targets repository customization for GitHub Copilot.

- GitHub.com Copilot cloud agent: supports repository instructions, custom agents, and Agent Skills. Prompt files are IDE-oriented and are not assumed for GitHub.com cloud agent.
- Copilot CLI: supports repository custom instructions, custom agents, and Agent Skills when the CLI is authenticated and run in the repository.
- VS Code: supports custom instructions, instruction files, prompt files, custom agents, and Skills according to the installed GitHub Copilot extension and VS Code version.
- Visual Studio: supports Copilot customization features where the Visual Studio Copilot extension documents them; support can differ from VS Code.
- JetBrains IDEs: support for some workspace customizations is narrower or preview depending on the installed Copilot plugin version.
- This package includes no GitHub Actions workflow, automation, hook, MCP server, model pin, secret, token, cloud runner setting, PR automation, deployment, or publication configuration.

## Included native components

- `.github/copilot-instructions.md`: repository-wide custom instructions.
- `.github/instructions/web-development.instructions.md`: path-specific instructions with `applyTo` frontmatter for web-relevant files.
- `.github/agents/*.agent.md`: custom agent profiles. Reviewers expose only `read` and `search`; implementers expose `read`, `search`, and `edit`; the lead exposes `read`, `search`, and `agent`.
- `.github/prompts/*.prompt.md`: reusable IDE prompt files for manual workflows.
- `.github/skills/*/SKILL.md`: Agent Skills for reusable specialist procedures.
- `README.md`: human setup and validation guide. It is not loaded by Copilot.

## Installation and integration

1. Copy the contents of `github-copilot/web-development/` to the target repository root so the target root contains `.github/`.
2. Review all instruction, agent, prompt, and Skill files before enabling Copilot on the repository.
3. Ensure repository custom instructions are enabled for the intended Copilot surface.
4. In GitHub.com or Copilot CLI, verify custom agents and Skills are discovered for the repository.
5. In IDEs, verify prompt files, instruction files, custom agents, and Skills through the Copilot customization UI supported by that IDE.
6. Keep MCP servers, hooks, GitHub Actions, secrets, cloud agent environment changes, automatic PR settings, deployment, publication, and external integrations disabled unless separately reviewed and authorized.

## How to use

Select `web-development-lead` manually for multi-step coordination. It can use the `agent` tool only on surfaces where custom-agent delegation is available; otherwise the user should manually select specialist profiles. Use specialist agents directly for focused tasks: `web-architecture-specialist`, `frontend-specialist`, `backend-api-specialist`, `security-privacy-reviewer`, `accessibility-performance-seo-reviewer`, and `quality-release-reviewer`.

Use prompt files from supported IDE prompt pickers only. Skills are selected automatically by supported Copilot surfaces when relevant, or manually where the surface exposes Skill invocation. Expected output should cite repository evidence and mark unexecuted tests, builds, browser checks, deployments, prompt files, Skills, or custom-agent behavior as `NOT EXECUTED`.

## Operating model

Repository instructions provide broad behavior, path instructions provide web quality gates, prompt files provide manual workflows, custom agents provide focused personas, and Skills provide on-demand procedures. Implementation agents may edit only within approved scope. Independent reviewers remain read/search only. Completion uses `PASS`, `FAIL`, `BLOCKED`, or `NOT APPLICABLE`, with `NOT EXECUTED` for checks that did not run.

## Examples

- Feature/architecture: ask in Copilot Chat using the Web Development lead agent to plan a passwordless login flow for the current web app. State: `Do not deploy or install packages.`
- Review/audit: request security/privacy review for CSP, cookies, CSRF, CORS, authorization, logging, third-party scripts, and sensitive data handling.
- Stack selection: provide repository evidence and ask the department to use only applicable Web Development specialists for React, Rails, Django, Laravel, static-site, or other detected stacks.
- Project customization: add `Node 22, pnpm only, WCAG 2.2 AA, LCP budget 2.5s, Playwright smoke tests` to task criteria without editing core department files.
- Sensitive action: request a deployment, publication, package-install, or Git checklist without executing it; actual external action requires separate human approval.

## Project-specific and user-specific configuration

The department is already specialized. Already specialized and normally not modified: Copilot instructions, agents, prompts, and Skills, review responsibilities, security/privacy responsibilities, accessibility/performance/SEO responsibilities, testing responsibilities, quality gates, and the operating model. Project/user values may include framework and runtime versions, package manager policy, repository layout, code style, lint/format/test commands, coverage thresholds, browser support matrix, WCAG target, performance budgets, Core Web Vitals thresholds, SEO requirements, API conventions, auth provider, database/storage technology, approved dependencies, deployment target, CI/CD commands, environment names, feature-flag conventions, observability provider, logging requirements, organization security policy, privacy/legal requirements, data classification, approval owners, release process, branch strategy, protected branches, allowed external integrations, MCP servers or connectors, private endpoints, organization IDs, and workspace IDs. Never hard-code or commit API keys, tokens, passwords, private keys, production credentials, real secret values, or sensitive private URLs; use placeholders or environment-variable names. Project-specific configuration extends the department; it does not create the specialization.

## Safety and human approval

This package does not authorize automatic deployment, publication, authentication, secret use, spending, signing, submission, destructive operations, dependency installation, Git mutation, GitHub Actions changes, PR creation, merge, MCP use, hook execution, cloud agent environment changes, or production changes. Every sensitive or external action requires exact human authorization and must be supported by the active Copilot surface.

## Limitations

- Copilot customization support differs across GitHub.com, Copilot CLI, VS Code, Visual Studio, and JetBrains.
- Custom instructions, prompt files, agents, and Skills are instructions, not deterministic enforcement.
- The `tools` field filters available agent tools, but unrecognized tool names may be ignored by some surfaces.
- No runtime validation, browser checks, builds, tests, live Copilot loading, GitHub.com cloud run, CLI invocation, IDE prompt invocation, or Skill invocation was executed.

## Validation

- Syntax validation: instruction, agent, prompt, and Skill YAML frontmatter was parsed.
- Schema/static validation: custom agent fields were checked against documented GitHub Copilot properties; reviewer tool sets exclude `edit` and `execute`; no MCP server, hook, GitHub Actions workflow, secret, or automation file is included.
- Actual product loading: `NOT EXECUTED`.
- Runtime tests: `NOT EXECUTED`.
- Browser/build/deployment checks: `NOT EXECUTED`.

## Official documentation

Verified on July 20, 2026:

- GitHub Docs: Adding repository custom instructions for GitHub Copilot - https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot
- GitHub Docs: Custom agents configuration - https://docs.github.com/en/copilot/reference/custom-agents-configuration
- GitHub Docs: Adding agent skills for GitHub Copilot - https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills
- GitHub Docs: Adding agent skills for GitHub Copilot CLI - https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills
- GitHub Docs: Customization cheat sheet - https://docs.github.com/en/copilot/reference/customization-cheat-sheet
- VS Code Docs: Custom instructions and prompt files - https://code.visualstudio.com/docs/agent-customization/custom-instructions
