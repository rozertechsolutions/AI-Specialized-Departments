---
description: Static CI/CD, release, rollback, progressive delivery, migration, and DORA workflow guidance.
agent: ci-cd-engineer
subtask: true
---

# CI/CD and Release Engineering Workflows

## new-pipeline-design
1. Capture source triggers, stages, platform constraints, quality gates, artifact flow, caching, environments, approvals, and evidence needs.
2. Design reproducible static pipeline architecture without executable secrets or live endpoints.
3. Define rollback, traceability, and DORA metric evidence before release readiness.

## pipeline-review
1. Review stages, dependencies, caching, artifact immutability, provenance, permissions, failure behavior, and promotion model.
2. Check that no pipeline is represented as executed and no secret or environment-specific value is committed.
3. Return findings, blockers, and unverified runtime assumptions.

## release-readiness-review
1. Confirm versioning, approvals, artifact provenance, environment promotion, rollback, feature flags, database-change coordination, and evidence.
2. Require human authorization for production release decisions.
3. Do not publish, sign, deploy, or mutate release state.

## progressive-deployment-plan
1. Select rolling, blue-green, canary, or progressive delivery only from explicit requirements and risk constraints.
2. Define stages, metrics, guardrails, pause/abort criteria, rollback, and observability handoff.
3. Keep the plan static and do not perform deployment or GitOps sync.

## rollback-plan
1. Define rollback trigger, owner, artifact or version target, data-change coordination, feature-flag behavior, and evidence.
2. Verify rollback is designed before release readiness is accepted.
3. Escalate irreversible or data-impacting rollback gaps.

## pipeline-migration
1. Capture source and target platform constraints, feature parity, secrets handling, artifact continuity, and cutover risk.
2. Map Jenkins, GitHub Actions, GitLab CI/CD, Azure Pipelines, CircleCI, Tekton, Argo CD, or Flux concepts only as justified.
3. Produce a static migration plan with validation steps not run.
