---
name: ci-cd-release-engineering
description: Use for CI/CD pipeline design, pipeline hardening, artifact promotion, release strategy, progressive delivery, rollback planning, and DORA metrics assessment.
---
# CI/CD and Release Engineering Skill

Use this skill for section 03 delivery-system design and review only. Produce static artifacts and never run builds, tests, pipelines, GitOps syncs, releases, or deployments.

## Procedure
1. Classify the request as ci-cd-pipeline-design, pipeline-hardening, artifact-flow-and-promotion, release-strategy, progressive-delivery, rollback-planning, dora-metrics-assessment.
2. Identify source, stages, quality gates, artifact flow, promotion model, environment boundaries, approvals, rollback design, and DORA metric evidence.
3. Use Jenkins Pipeline, GitHub Actions, GitLab CI/CD, Azure Pipelines, CircleCI, Tekton, Argo CD, Flux, artifact repositories, container registries, feature flags, and DORA delivery and stability metrics only when requirements justify the platform or tool.
4. Prefer immutable artifacts promoted across environments rather than rebuilding where practical.
5. Verify that release paths are reproducible, traceable, reversible, and not represented as having run.

## Stop criteria
Stop on requested execution, missing rollback plan, mutable artifact flow without rationale, secret exposure, production authorization, unsupported platform behavior, or missing human approval.

Reference: `docs/ci-cd-release-engineering.md`.

## Evidence
Return static assumptions, designs, reviews, risks, approvals needed, DORA metric considerations, and checks not run.
