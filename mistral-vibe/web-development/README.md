# Web Development — Mistral Vibe

## Department overview

The Web Development department is a stack-aware Vibe Code package for frontend, backend, full-stack architecture, APIs, authentication, accessibility, performance, SEO, testing, security, privacy, and release-readiness work. It is not tied to one framework. Components are applicability-based: a task may use the coordinator, one specialist, several reviewers, or only a Skill.

## Possible uses

- Discover an existing web stack before changing it.
- Plan a web feature or migration.
- Review frontend semantics, state, forms, responsiveness, and browser behavior.
- Design or review APIs, authentication, sessions, cookies, CSP, CORS, and privacy boundaries.
- Debug web regressions from repository evidence.
- Audit accessibility, performance, responsive behavior, and SEO.
- Review dependencies and supply-chain risk.
- Prepare release-readiness evidence without deploying.
- Review architecture and migration decisions.

## Supported product surface

This package targets Mistral Vibe Code CLI project configuration. Official Vibe documentation describes project-level custom agents in `./.vibe/agents/`, prompt files referenced by `system_prompt_id`, project Skills in `./.vibe/skills/`, and project `AGENTS.md` discovery from trusted folders. The CLI can run with Mistral-hosted models, configured API plans, or local model setups according to the user's Vibe installation. This repository package is static configuration; it does not install Vibe, authenticate, configure a provider, run Vibe, or prove product loading.

## Included native components

- `AGENTS.md`: project-level Vibe instructions loaded from a trusted project folder.
- `.vibe/agents/web-development-coordinator.toml`: user-selectable lead agent.
- `.vibe/agents/*-specialist.toml` and `.vibe/agents/*-reviewer.toml`: delegation-only subagents spawned through Vibe's `task` tool.
- `.vibe/prompts/*.md`: prompt bodies referenced by each agent's `system_prompt_id`.
- `.vibe/skills/*/SKILL.md`: project Skills exposed as slash commands when `user-invocable: true`.

No MCP server, connector, hook, plugin, custom executable tool, provider profile, endpoint, telemetry setting, or install script is included.

## Installation and integration

Copy the contents of `mistral-vibe/web-development/` into the root of the target repository so these paths remain exact:

- `AGENTS.md`
- `.vibe/agents/*.toml`
- `.vibe/prompts/*.md`
- `.vibe/skills/*/SKILL.md`

Install and configure Vibe separately using official product instructions. Do not store credentials in this package. Start Vibe from the target repository root after the folder is trusted by Vibe. Verify discovery manually by confirming the `web-development-coordinator` agent is selectable and department Skills appear in slash-command autocomplete.

## How to use

Start the coordinator with:

```sh
vibe --agent web-development-coordinator
```

Inside an interactive session, Vibe can switch agents with its documented agent selector. Use Skills by their slash command names, for example `/stack-discovery`, `/workflow-plan-web-change`, `/frontend-delivery`, `/security-privacy-review`, or `/workflow-verify-release-readiness`. The coordinator may delegate read-only analysis to the configured subagents through `task` after approval when Vibe requests it.

Expected outputs are scoped plans, findings, recommendations, evidence summaries, and PASS/FAIL/BLOCKED/NOT EXECUTED gate status for human review.

## Operating model

The coordinator confirms scope and acceptance criteria, discovers the stack from repository evidence, selects applicable specialists, reconciles findings, and reports final limitations. Specialists and reviewers return bounded text-only results with concrete evidence. Security/privacy and release readiness remain independent reviews and cannot be self-approved by implementers. Completion requires direct evidence; absent checks are reported as NOT EXECUTED.

## Safety and human approval

No automatic deployment, publication, authentication, secret use, spending, signing, submission, destructive operation, dependency installation, command execution, Git mutation, MCP use, connector use, or external side effect may occur without exact human authorization. Reviewer agents disable write and shell-capable tools. The coordinator has `task` set to ask for approval and disables shell, write, MCP, and connector tool patterns.

## Limitations

Validation for this package is static. Actual Vibe loading, model behavior, prompt routing, workspace policy, local model configuration, and provider authentication were not executed. Vibe CLI setup, trusted-folder state, account or API-plan availability, and VS Code extension behavior are user-environment dependent. Skills can expose write-capable tools for implementation workflows; humans must review those Skills and grant tool approvals according to the active Vibe session.

## Validation

- Syntax validation: TOML agent files and Skill YAML frontmatter parsed locally.
- Schema/static validation: agent prompt references, agent types, reviewer read-only configuration, and internal README paths checked locally.
- Actual product loading: NOT EXECUTED.
- Runtime tests: NOT EXECUTED.
- Browser/build/deployment checks: NOT EXECUTED.

## Official documentation

Verified on 2026-07-20:

- Mistral Docs, "Install and setup": https://docs.mistral.ai/vibe/code/cli/install-setup
- Mistral Docs, "Configuration": https://docs.mistral.ai/vibe/code/cli/configuration
- Mistral Docs, "Agents": https://docs.mistral.ai/vibe/code/cli/agents
- Mistral Docs, "Skills": https://docs.mistral.ai/vibe/code/cli/skills
- Mistral Docs, "Safety, approvals, and permissions": https://docs.mistral.ai/vibe/code/safety-approvals-permissions
