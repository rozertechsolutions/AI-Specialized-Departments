# Web Development Department Instructions

This file is the Claude Code project memory for this package. Keep it concise: detailed role behavior lives in `.claude/agents/`, and reusable procedures live in `.claude/skills/`.

## Mission
Deliver professional, stack-appropriate web-development work covering frontend, backend, full-stack architecture, APIs, authentication, sessions, storage, integrations, responsive behavior, accessibility, SEO, performance, testing, browser compatibility, observability, deployment readiness, security, privacy, CSP, cookies, CORS, and supply-chain review when relevant.

## Operating model
1. Detect the repository's actual stack and constraints before choosing an approach.
2. Confirm requested scope, acceptance criteria, affected surfaces, and prohibited changes.
3. For coordinated work, launch `web-development-lead` as the main-session agent. The lead may delegate only to approved specialists through its `Agent(...)` allowlist.
4. Use the required order for material work: discovery and architecture, implementation, security/privacy review, accessibility/performance/SEO review, then quality/release review.
5. Reviewers remain independent, read-only, and evidence-based. The lead reconciles findings but cannot self-approve security or final readiness.
6. Prefer the smallest coherent change that follows existing architecture and conventions.
7. Verify completion from direct evidence. Never infer that a command, test, build, deployment, or external action succeeded.
8. Stop and report BLOCKED when required evidence, authorization, credentials, product decisions, or human approvals are missing.

## Mandatory safety boundaries
- Work only inside the explicitly approved project scope.
- Never expose, generate, copy, log, or commit secrets, tokens, credentials, private endpoints, or personal data.
- Never install software or dependencies, execute terminal commands, start services, run builds or tests, mutate Git, publish, deploy, merge, tag, sign, submit, spend money, authenticate integrations, or perform destructive actions unless a human explicitly authorizes that exact action at execution time.
- External integrations, MCP servers, trackers, analytics, third-party scripts, and remote tools remain disabled or unconfigured by default.
- Require human review before changes to authentication, authorization, cryptography, sensitive data, production configuration, migrations, dependencies, tracking, billing, legal or privacy behavior.
- Never weaken CSP, CORS, cookie, CSRF, validation, authorization, or transport protections merely to make a feature work.
- Do not fabricate files, APIs, documentation claims, compatibility, test results, or completion evidence.

## Native package boundaries
- Agents are in `.claude/agents/`.
- Skills are in `.claude/skills/` and load through Claude Code's native Skill mechanism or agent `skills` preload field.
- This package intentionally includes no MCP server configuration and no executable hooks.
- Do not add Bash access, external MCP servers, hooks, deployment scripts, or credentials without explicit human approval for the exact change.

## Completion contract
A task is complete only when the requested artifact exists, scope is correct, applicable acceptance criteria are traceable, prohibited actions were avoided, material reviews are resolved, and remaining limitations are explicit. Use PASS, FAIL, BLOCKED, or NOT APPLICABLE for every final gate.
