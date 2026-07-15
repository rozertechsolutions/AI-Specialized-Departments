---
name: review-mobile-architecture
description: Use when reviewing mobile architecture, modules, dependency direction, state, navigation, shared/platform boundaries, migrations, and ownership conflicts.
---

# review-mobile-architecture

- Objective: Review mobile architecture for correctness, maintainability, ownership clarity, dependency direction, state/navigation design, and migration risk.
- Trigger: User asks for architecture review, migration review, module review, or shared/platform boundary assessment.
- Inputs: Repository structure, architecture docs, build files, dependency graph hints, navigation/state code, module boundaries, and requested change.
- Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, React Native.
- Preconditions: Inspect files before judging, identify actual technologies, and distinguish facts from inferred architecture.
- Primary owner: `mobile-architect`.
- Reviewers: Relevant platform owners, `mobile-security-reviewer` for risk, `mobile-performance-reviewer` for performance impact, and `mobile-code-reviewer`.
- Steps: Map modules and dependencies; identify boundaries and owners; check for cycles/conflicts; compare requested design with conventions; classify criteria; recommend minimal corrections; avoid implementation unless explicitly requested and scoped.
- Validation gates: Unique ownership, no cyclic authority, no implementation role self-review, dependency direction documented, migration gates defined, and unsupported components omitted.
- Failures: Stop on insufficient repository context, conflicting requirements, or unsupported architecture request.
- Stop conditions: Review turns into unapproved implementation, public API change, dependency change, destructive action, or release action.
- Evidence: Files/lines reviewed, diagrams or maps when useful, command output if used, and not-applicable reasons.
- Outputs: Findings, risk ranking, ownership matrix updates if requested, validation gates, and open questions.
- Acceptance criteria: Review is evidence-backed, scoped, actionable, and independent from implementation.
- Human approvals: Required for migration execution, dependency changes, public API changes, security/privacy changes, build/signing config, and release decisions.
- Prohibited actions: Complete feature implementation, self-review, universal adapter creation, publishing, signing, deployment, destructive commands, and fabricated conclusions.

