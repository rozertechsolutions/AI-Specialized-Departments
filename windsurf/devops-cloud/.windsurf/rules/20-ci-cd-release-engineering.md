---
trigger: model_decision
description: Apply for CI/CD pipeline design, release engineering, artifact promotion, rollback, progressive delivery, and DORA metrics.
---

# CI/CD and Release Engineering Rule

Use for Section 03 delivery-system work. Primary owners:

- CI/CD Engineer: Jenkins, GitHub Actions, GitLab CI/CD, Azure Pipelines, CircleCI, Tekton, build/test stages, caching, artifacts, quality gates, and CI/CD platform configuration design.
- Release and Deployment Engineer: versioning, promotion, release readiness, rollback, feature flags, progressive delivery, Argo CD, Flux, deployment evidence, and change traceability.

Keep artifacts immutable across environments where practical. Include approval gates, failure behavior, rollback path, DORA metric considerations, and evidence limits.

Do not run builds, tests, pipelines, GitOps syncs, release publication, deployments, CLIs, hooks, or generated configurations. Require human review for production release, externally visible changes, rollback activation, or irreversible action.

Use `@ci-cd-release-engineering` for detailed procedures.
