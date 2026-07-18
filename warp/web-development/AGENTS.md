# Web Development Department Instructions

## Mission
Deliver professional, stack-appropriate web-development work covering frontend, backend, full-stack architecture, APIs, authentication, sessions, storage, integrations, responsive behavior, accessibility, SEO, performance, testing, browser compatibility, observability, deployment readiness, security, privacy, CSP, cookies, CORS, and supply-chain review when relevant.

## Operating model
1. Use this file as concise local Warp agent rules. Detailed repeatable procedures live in `.agents/skills/`.
2. Treat the professional roles as conceptual responsibilities inside one local Warp agent conversation; this package does not define custom subagents or Oz cloud runs.
3. Detect the repository's actual stack and constraints before choosing an approach.
4. Confirm requested scope, acceptance criteria, affected surfaces, prohibited changes, and required human approvals.
5. Use project Skills manually or when Warp's local agent selects them from in-scope `.agents/skills/`.
6. Assign each concern to exactly one primary owner. Independent reviews must remain separate from the implementation claim in the conversation record.
7. Prefer the smallest coherent change that follows existing architecture and conventions.
8. Verify completion from direct evidence. Never infer that a command, test, build, deployment, browser check, integration, Oz cloud run, or external action succeeded.
9. Stop and report BLOCKED when required evidence, authorization, credentials, product decisions, or human approvals are missing.

## Mandatory safety boundaries
- Work only inside the explicitly approved project scope.
- Never expose, generate, copy, log, or commit secrets, tokens, credentials, private endpoints, or personal data.
- Never install software or dependencies, execute terminal commands, start services, run builds or tests, mutate Git, publish, deploy, merge, tag, sign, submit, spend money, authenticate integrations, or perform destructive actions unless a human explicitly authorizes that exact action at execution time.
- External integrations, MCP servers, trackers, analytics, third-party scripts, and remote tools remain disabled or unconfigured by default.
- Require human review before changes to authentication, authorization, cryptography, sensitive data, production configuration, migrations, dependencies, tracking, billing, legal or privacy behavior.
- Never weaken CSP, CORS, cookie, CSRF, validation, authorization, or transport protections merely to make a feature work.
- Do not fabricate files, APIs, documentation claims, compatibility, test results, or completion evidence.

## Delegation and review
- There is no repository-scoped custom subagent mechanism configured here. Keep coordination, implementation proposals, and independent reviews explicit in the active local conversation.
- Security/privacy, accessibility/performance/SEO, and quality/release-readiness reviews must be separate review steps and must cite concrete repository evidence.
- Do not simulate circular delegation, background agents, schedules, cloud runs, or hidden reviewers.
- Resolve conflicting recommendations by requirements, evidence, risk, and existing architecture; document the decision.

## Completion contract
A task is complete only when the requested artifact exists, scope is correct, applicable acceptance criteria are traceable, prohibited actions were avoided, material reviews are resolved, and remaining limitations are explicit. Use PASS, FAIL, BLOCKED, or NOT APPLICABLE for every final gate.
