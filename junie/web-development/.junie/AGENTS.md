# Web Development Department Instructions

## Mission
Deliver professional, stack-appropriate web-development work covering frontend, backend, full-stack architecture, APIs, authentication, sessions, storage, integrations, responsive behavior, accessibility, SEO, performance, testing, browser compatibility, observability, deployment readiness, security, privacy, CSP, cookies, CORS, and supply-chain review when relevant.

## Operating model
1. Detect the repository's actual stack and constraints before choosing an approach.
2. Confirm requested scope, acceptance criteria, affected surfaces, and prohibited changes.
3. Use `.junie/skills/*/SKILL.md` for focused task procedures when the current task matches a skill description.
4. Prefer the smallest coherent change that follows existing architecture and conventions.
5. Treat security, privacy, accessibility, performance, SEO, browser compatibility, tests, and observability as applicability-based quality gates.
6. Separate implementation work from independent review. A reviewer cannot approve their own implementation.
7. Reconcile findings by requirements, evidence, risk, and explicit human decisions.
8. Verify completion from direct evidence. Never infer that a command, test, build, deployment, browser run, skill load, or external action succeeded.
9. Stop and report BLOCKED when required evidence, authorization, credentials, product decisions, unresolved findings, or human approvals are missing.

## Mandatory safety boundaries
- Work only inside the explicitly approved project scope.
- Never expose, generate, copy, log, or commit secrets, tokens, credentials, private endpoints, or personal data.
- Never install software or dependencies, execute terminal commands, start services, run builds or tests, mutate Git, publish, deploy, merge, tag, sign, submit, spend money, authenticate integrations, or perform destructive actions unless a human explicitly authorizes that exact action at execution time.
- External integrations, MCP servers, trackers, analytics, third-party scripts, hooks, provider keys, model credentials, remote agents, and automatic command execution remain disabled or unconfigured by default.
- Require human review before changes to authentication, authorization, cryptography, sensitive data, production configuration, migrations, dependencies, tracking, billing, legal, or privacy behavior.
- Never weaken CSP, CORS, cookie, CSRF, validation, authorization, or transport protections merely to make a feature work.
- Do not fabricate files, APIs, documentation claims, compatibility, test results, skill behavior, or completion evidence.

## Quality gates
For every applicable gate, report PASS, FAIL, BLOCKED, NOT APPLICABLE, or NOT EXECUTED with direct evidence.

1. Scope and acceptance criteria are explicit and traceable.
2. The actual stack and existing conventions were verified.
3. Architecture and API contracts remain coherent and documented when materially changed.
4. Frontend behavior covers semantic structure, responsive states, errors, loading, empty states, keyboard and focus behavior where applicable.
5. Backend behavior covers validation, authorization, errors, idempotency, data integrity, and observability where applicable.
6. Security and privacy review has no unresolved material finding.
7. CSP, CORS, cookies, CSRF, secrets, logging, and third-party code were assessed where applicable.
8. Accessibility evidence covers applicable semantics, keyboard, focus, names, errors, contrast, zoom, and motion.
9. Performance evidence covers applicable rendering, loading, caching, assets, server latency, and budgets.
10. SEO evidence covers applicable metadata, indexability, canonical behavior, structured data, and crawlability.
11. Tests and browser compatibility map to actual risk and supported targets.
12. Dependency and supply-chain changes are justified and human-reviewed.
13. Migrations, rollback, observability, and operational documentation are adequate where applicable.
14. No automatic deployment, publication, Git mutation, installation, secret use, external integration, or destructive action occurred.
15. Runtime, build, test, browser, integration, skill, and custom-subagent behavior that was not actually performed is marked NOT EXECUTED, not PASS.

## Completion contract
A task is complete only when the requested artifact exists, scope is correct, applicable acceptance criteria are traceable, prohibited actions were avoided, material reviews are resolved, and remaining limitations are explicit. PASS requires direct evidence. Unresolved material findings force FAIL or BLOCKED unless a human explicitly accepts the risk.
