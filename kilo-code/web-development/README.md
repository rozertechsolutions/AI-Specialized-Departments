# Web Development — Kilo Code

## Department overview

This is a project-scoped Kilo Code specialization for a stack-aware Web Development department. It supports frontend, backend, full-stack architecture, APIs, authentication, accessibility, performance, SEO, testing, security, privacy, and release-readiness work without assuming one framework. Components are applicability-based; Kilo uses the rules, lead agent, specialist subagents, commands, and Skills that match the task.

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

This package targets current Kilo Code VS Code extension and Kilo Code CLI project configuration.

- `kilo.jsonc`: project config with schema `https://app.kilo.ai/config.json`, project rule loading, and default permission policy.
- `.kilo/rules/*.md`: project rules loaded through `kilo.jsonc` `instructions`.
- `.kilo/agents/*.md`: custom modes/agents with YAML frontmatter. `web-development-lead` is `mode: primary`; specialists are `mode: subagent`.
- `.kilo/commands/*.md`: slash-command workflows with `agent: web-development-lead` and `subtask: false`.
- `.kilo/skills/*/SKILL.md`: Agent Skills for reusable procedures.
- Legacy `.kilocode/`, `.kilocodemodes`, memory bank, MCP, hooks, plugins, provider keys, and external integrations are not included.

## Included native components

- `kilo.jsonc`: loads `.kilo/rules/*.md`, denies bash by default, and asks before edits.
- `.kilo/rules/web-development.md`: always-on operating model and delegation rules.
- `.kilo/rules/quality-gates.md`: always-on quality gates and human-review policy.
- `.kilo/agents/web-development-lead.md`: primary coordinator with a restricted `permission.task` allowlist.
- `.kilo/agents/*specialist*.md`: specialist subagents. Reviewers deny edit, bash, and task delegation; implementers ask before edits and deny bash/task delegation.
- `.kilo/commands/*.md`: manual workflow commands.
- `.kilo/skills/*/SKILL.md`: reusable domain Skills.
- `README.md`: human setup and validation guide. It is not loaded by Kilo.

## Installation and integration

1. Copy the contents of `kilo-code/web-development/` to the target repository root so the target root contains `kilo.jsonc` and `.kilo/`.
2. Do not add a root `AGENTS.md` pointer for this package; `kilo.jsonc` and `.kilo/rules/` are the always-on authority.
3. Open the repository in the Kilo Code VS Code extension or start Kilo Code CLI from the repository root.
4. Review `kilo.jsonc`, rules, agents, commands, and Skills before trusting the workspace.
5. Keep MCP, hooks, plugins, provider keys, model pins, legacy configs, deployment, publication, and external integrations disabled unless separately reviewed and authorized.
6. Verify discovery through Kilo’s settings UI, command list, agent/mode selector, and Skills list.

## How to use

Use `web-development-lead` as the primary agent for coordinated work. Manual workflow commands run the lead without launching it as a subtask. The lead may invoke only `web-architecture-specialist`, `frontend-specialist`, `backend-api-specialist`, `security-privacy-reviewer`, `accessibility-performance-seo-reviewer`, and `quality-release-reviewer`.

Use commands such as `plan-web-change`, `implement-web-change`, `review-security-and-privacy`, and `verify-release-readiness` from Kilo’s command surface. Use Skills by task purpose or name, such as `stack-discovery`, `backend-api-auth`, or `release-readiness`.

## Operating model

Kilo loads project rules through `kilo.jsonc`, starts the primary lead for workflows, delegates bounded specialist work through `permission.task`, keeps reviewers read-only, and requires the quality/release reviewer last for final readiness. Completion uses `PASS`, `FAIL`, `BLOCKED`, `NOT APPLICABLE`, or `NOT EXECUTED` with direct evidence.

## Safety and human approval

This package does not authorize automatic deployment, publication, authentication, secret use, spending, signing, submission, destructive operations, dependency installation, Git mutation, bash execution, MCP use, hook execution, plugin execution, provider-key use, or production changes. `kilo.jsonc` denies bash and asks before edits; every sensitive or external action requires exact human authorization.

## Limitations

- Rules, commands, agents, and Skills are instructions plus Kilo permissions, not a full external policy engine.
- Actual enforcement depends on Kilo Code’s installed version, settings, and user approvals.
- No live Kilo loading, runtime validation, browser checks, builds, tests, hooks, MCP, plugins, bash commands, or deployment were executed.
- The package does not include legacy compatibility files.

## Validation

- Syntax validation: `kilo.jsonc`, agent and command YAML frontmatter, and Skill YAML frontmatter were parsed.
- Schema/static validation: `kilo.jsonc` rule paths, schema URL, lead primary mode, command targets, `subtask: false`, task allowlist, reviewer read-only permissions, and absence of legacy/MCP/hook/plugin files were checked locally.
- Actual product loading: `NOT EXECUTED`.
- Runtime tests: `NOT EXECUTED`.
- Browser/build/deployment checks: `NOT EXECUTED`.

## Official documentation

Verified on July 20, 2026:

- Kilo Code Docs: Custom rules - https://kilo.ai/docs/customize/custom-rules
- Kilo Code Docs: Custom modes - https://kilocode.ai/docs/features/custom-modes
- Kilo Code Docs: Custom subagents - https://kilo.ai/docs/customize/custom-subagents
- Kilo Code Docs: Skills - https://kilo.ai/docs/customize/skills
- Kilo Code Docs: Auto-approving actions - https://kilocode.ai/docs/features/auto-approving-actions
- Kilo Code Docs: CLI - https://kilo.ai/docs/code-with-ai/platforms/cli
- Kilo Code Docs: AGENTS.md - https://kilocode.ai/docs/advanced-usage/memory-bank
