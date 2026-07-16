---
name: review-mobile-architecture
description: Review mobile architecture, module boundaries, dependency direction, navigation, state, and shared/platform split.
---

# review-mobile-architecture

Objective: provide a read-only architecture review with concrete findings and owner boundaries.

Trigger: request to review, assess, plan, or validate mobile architecture.

Inputs: target scope, architecture questions, source tree, manifests, build files, dependency configuration, navigation/state code, and validation goals.

Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, React Native.

Preconditions: inspect files read-only; detect technologies; do not edit; identify project commands only when useful for evidence and safe to run.

Primary owner: `mobile-architect`.

Reviewers: `mobile-security-reviewer`, `mobile-performance-reviewer`, and `mobile-code-reviewer` when architecture affects their domains.

Steps:

1. Inventory modules, targets, source sets, packages, routes, and dependency directions.
2. Classify criteria and unsupported areas.
3. Identify ownership boundaries and conflicts.
4. Check shared/platform splits and migration risks.
5. List findings by severity with file evidence.
6. Recommend minimal corrective options and validation gates.

Validation gates: path and technology evidence, dependency-direction evidence, no self-review, explicit unsupported classification, and reviewer handoff when needed.

Failures: insufficient source context, hidden generated config, missing docs, unclear requirements, or architecture change requiring implementation approval.

Stop conditions: requested edits, dependency changes, public contract changes, security/privacy/release impact, or unsupported platform claims.

Evidence: inspected paths, detected technologies, commands if run, architecture findings, criteria classification, and limitations.

Outputs: architecture review report and recommended next actions.

Acceptance criteria: findings are actionable, scoped, evidence-based, and do not fabricate validation.

Human approvals: required before implementing recommendations that affect architecture, dependencies, public APIs, persistent formats, security/privacy, or release behavior.

Prohibited actions: source edits, generated changes, signing, publishing, external uploads, deployment, destructive commands, or final approval of implementation.
