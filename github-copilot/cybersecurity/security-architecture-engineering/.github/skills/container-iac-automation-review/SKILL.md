---
name: container-iac-automation-review
description: Use for container, Kubernetes, IaC, control integration, security tooling, automation boundary, resilience, and remediation validation architecture.
---

# Container, IaC, and Automation Review

Objective: review or design container, orchestration, IaC, and security automation architecture patterns with static, human-approved handoff.

Primary owner: `data-container-automation-agent`.

Workflow:

1. Confirm scope, exclusions, evidence provenance, source versions, reviewer, approver, and production boundaries.
2. Review image, runtime, workload, namespace, cluster, network, identity, storage, and management-plane boundaries.
3. Map IaC controls to architecture requirements and identify drift, exception, and remediation validation criteria.
4. Define automation boundaries, human approval gates, failure modes, rollback expectations, and observability handoffs.
5. Classify findings, remediation actions, dependencies, residual risk, and completion criteria.
6. Route high-impact findings or closure packages to `independent-architecture-reviewer`.

Stop for live deployment, production automation enablement, active scan, control operation, destructive change, or approval of remediation closure.
