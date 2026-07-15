---
name: review-mobile-architecture
description: Review mobile architecture, module boundaries, dependency direction, navigation, state, and shared/platform separation.
---

# review-mobile-architecture

Objective: evaluate mobile architecture and produce actionable, evidence-backed findings without implementing broad changes.

Trigger: request for architecture review, migration planning, cross-module change, framework boundary question, or design risk.

Inputs: requirements, project structure, build files, module graph, navigation/state patterns, shared/platform boundaries, migration constraints.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, React Native.

Preconditions: inspect files and user changes; detect technologies; identify module ownership; avoid changing source unless a separate implementation workflow is explicitly requested.

Primary owner: `mobile-architect`.

Reviewers: `mobile-code-reviewer`; `mobile-security-reviewer`, `mobile-performance-reviewer`, or `mobile-release-engineer` when their domains are affected.

Ordered steps:

1. Map technologies, modules, dependencies, and ownership.
2. Classify criteria and review scope.
3. Identify dependency direction, state, navigation, data, and platform boundary risks.
4. Check migration and compatibility constraints.
5. Produce findings with severity, evidence, and remediation options.
6. Define owners and validation gates for any follow-up implementation.

Conditional steps: request user approval before public API, storage, dependency, security, or release-impacting recommendations become edits.

Validation gates: architecture evidence, ownership matrix, no cycles/conflicts, compatibility analysis, security/performance/release review when relevant, and final code review of recommendations.

Failures: missing project evidence, ambiguous goals, unsupported technology, unavailable files, or requested edit beyond review scope.

Stop conditions: source edit requested without explicit implementation approval, dependency/security/release change, signing/publishing/deployment, destructive commands.

Evidence: files inspected, module graph observations, risks, alternatives, criteria classification, unavailable infrastructure.

Outputs: architecture review report, ownership recommendations, validation plan, risks, human decisions.

Acceptance criteria: review is specific, actionable, scoped, and does not fabricate project facts.

Human approvals: any subsequent implementation affecting public contracts, dependencies, persistence, security/privacy, release, or architecture.

Prohibited actions: complete feature implementation, final release approval, unsupported architecture simulation, publication, signing, uploading, deployment.
