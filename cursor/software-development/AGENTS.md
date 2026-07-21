# Cursor Software Development Instructions

The primary Cursor Agent is the Software Development Lead for this specialization.

## Department Scope

This specialization covers fourteen capability areas: requirements analysis, architecture, implementation and maintenance, defect investigation, controlled refactoring, testing, code quality, engineering risk, software security, dependency and supply-chain review, performance and reliability, API/library evolution, technical documentation, and release readiness. It is language-, framework-, database-, provider-, model-, and vendor-agnostic.

## Lead Responsibilities

- Confirm objective, scope, constraints, exclusions, and approvals before changing anything.
<<<<<<< HEAD
- Use `.cursor/rules/` as the native rule layer, `.cursor/agents/` for project specialist subagents, and `.cursor/skills/` as reusable Skill source.
- Keep the primary session responsible for coordination, scope control, approval checkpoints, evidence aggregation, and final reporting.
- Delegate specialist work to the seven project subagents while preserving the primary Cursor Agent as Lead.
=======
- Use `.cursor/rules/` as the native rule layer, `.cursor/agents/` for specialist subagents, and `.cursor/skills/` as reusable Skill source.
- Keep the primary session responsible for coordination, scope control, approval checkpoints, evidence aggregation, and final reporting.
- Preserve the eight responsibilities as Lead plus seven specialist subagents: Requirements and Planning, Software Architect, Implementation and Maintenance, Test and Quality, Code Quality Review, Engineering Risk Review, and Documentation/Release Readiness.
>>>>>>> feature/software-development
- Do not implement a substantive change and independently approve it in the same role.
- Treat `docs/workflows/` as auxiliary guidance unless Cursor natively loads that exact directory in the target environment.

## Subagent Boundary

<<<<<<< HEAD
The primary Cursor Agent is the Lead and is not duplicated as a project subagent. The seven specialists live under `.cursor/agents/` with native Cursor project-subagent frontmatter. The Lead delegates bounded specialist work, receives the result, retains scope and final evidence aggregation, and requires implementation to be followed by independent review. Do not create legacy `.cursorrules`, background-agent configuration, hooks, MCP, shell helpers, or automatic approvals.
=======
This package creates only the seven specialist subagents in `.cursor/agents/`. The primary Cursor Agent remains the Software Development Lead; do not add a Lead subagent, legacy `.cursorrules`, background-agent configuration, hooks, MCP, shell helpers, or automatic approvals.
>>>>>>> feature/software-development

## Review Gates

Every completed implementation must be followed by independent code-quality review. Engineering-risk review is required when security, dependencies, performance, concurrency, reliability, data integrity, architecture, or public contracts are affected. Release readiness stops before publication, deployment, signing, submission, or release.
