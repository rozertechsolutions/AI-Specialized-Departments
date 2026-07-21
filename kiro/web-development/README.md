# Web Development — Kiro

## Department overview

This is a project-scoped Kiro specialization for a stack-aware Web Development department. It supports frontend, backend, full-stack architecture, APIs, authentication, accessibility, performance, SEO, testing, security, privacy, and release-readiness work without assuming one framework. Components are applicability-based; Kiro uses steering, agents, and Skills only when relevant.

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

This package targets Kiro IDE and Kiro CLI project configuration.

- `.kiro/steering/*.md`: steering files with `inclusion: always` frontmatter.
- `.kiro/agents/*.md`: custom agents with documented tool category tags.
- `.kiro/skills/*/SKILL.md`: workspace Agent Skills.
- Kiro CLI can carry over `.kiro` project configuration from the IDE, but CLI custom-agent behavior and invocation can differ by installed CLI version.
- No AGENTS.md, MCP settings, powers, hooks, command hooks, shell tools, wildcard tools, broad built-in access, provider keys, or model pins are included.

## Included native components

- `.kiro/steering/web-development.md`: always-on operating model and safety rules.
- `.kiro/steering/quality-gates.md`: always-on quality gates and human-review policy.
- `.kiro/agents/web-development-lead.md`: main coordinator with `read`, `write`, and `subagent` tools.
- `.kiro/agents/*specialist*.md`: implementation specialists have `read` and `write`; independent reviewers have `read` only.
- `.kiro/skills/*/SKILL.md`: reusable domain Skills.
- `README.md`: human setup and validation guide. It is not loaded by Kiro.

## Installation and integration

1. Copy the contents of `kiro/web-development/` to the target repository root so the target root contains `.kiro/`.
2. Open the repository in Kiro IDE or start Kiro CLI from the repository root.
3. Review steering, agent, and Skill files before trusting the workspace.
4. Keep MCP, powers, hooks, shell access, provider keys, model pins, deployment, publication, and external integrations disabled unless separately reviewed and authorized.
5. Verify discovery in Kiro’s Agent Steering & Skills section, agent selector, and Skills slash-command list.

## How to use

Use `web-development-lead` as the main coordinator for multi-step web work. It may use `subagent` to launch only the documented specialists: `web-architecture-specialist`, `frontend-specialist`, `backend-api-specialist`, `security-privacy-reviewer`, `accessibility-performance-seo-reviewer`, and `quality-release-reviewer`. Specialists do not have `subagent`, so they cannot recursively delegate.

Invoke Skills automatically through matching descriptions or directly through Kiro’s slash-command Skill picker, such as `stack-discovery`, `frontend-delivery`, `backend-api-auth`, or `release-readiness`.

## Operating model

Kiro loads always-on steering, confirms scope, discovers the stack, uses the lead for coordinated work, delegates implementation and independent reviews to specialist agents, and runs the quality/release reviewer last. Completion uses `PASS`, `FAIL`, `BLOCKED`, `NOT APPLICABLE`, or `NOT EXECUTED` with direct evidence.

## Safety and human approval

This package does not authorize automatic deployment, publication, authentication, secret use, spending, signing, submission, destructive operations, dependency installation, Git mutation, MCP use, powers, hook execution, shell commands, provider-key use, or production changes. Every sensitive or external action requires exact human authorization in the active Kiro surface.

## Limitations

- Steering, agents, and Skills are instructions and tool-category constraints, not a complete policy engine.
- CLI and IDE behavior can differ by Kiro version and configuration.
- Steering inheritance was reviewed statically; live IDE/CLI loading was not executed.
- No runtime validation, browser checks, builds, tests, hooks, MCP, powers, shell commands, or deployment were executed.

## Validation

- Syntax validation: steering, agent, and Skill YAML frontmatter was parsed.
- Schema/static validation: tool categories were restricted to documented tags; only the lead has `subagent`; reviewers have `read` only; no MCP settings, powers, hooks, shell tools, wildcard tools, or empty settings remain.
- Actual product loading: `NOT EXECUTED`.
- Runtime tests: `NOT EXECUTED`.
- Browser/build/deployment checks: `NOT EXECUTED`.

## Official documentation

Verified on July 20, 2026:

- Kiro Docs: Steering - https://kiro.dev/docs/steering/
- Kiro Docs: CLI steering - https://kiro.dev/docs/cli/steering/
- Kiro Docs: Agent Skills - https://kiro.dev/docs/skills/
- Kiro Docs: CLI Agent Skills - https://kiro.dev/docs/cli/skills/
- Kiro Docs: Kiro CLI - https://kiro.dev/cli/
- Kiro Docs: Powers - https://kiro.dev/docs/powers/
