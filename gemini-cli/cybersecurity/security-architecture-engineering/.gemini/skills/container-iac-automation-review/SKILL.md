---
name: container-iac-automation-review
description: Use for container, Kubernetes, IaC, control integration, security tooling, automation boundary, resilience, and remediation validation architecture.
---

# Container, IaC, and Automation Review

Objective: review or design container, orchestration, IaC, and security automation architecture patterns with static, human-approved handoff.

Primary owner: `data-container-automation-agent`.

Inputs: container image model, runtime assumptions, orchestration scope, cluster boundaries, workload identity, IaC excerpts or design evidence, control integration goals, automation triggers, failure modes, owner, reviewer, approver, and decision needed.

Workflow:

1. Confirm scope, exclusions, evidence provenance, source versions, reviewer, approver, and production boundaries.
2. Review image, runtime, workload, namespace, cluster, network, identity, storage, and management-plane boundaries.
3. Map IaC controls to architecture requirements and identify drift, exception, and remediation validation criteria.
4. Define automation boundaries, human approval gates, failure modes, rollback expectations, and observability handoffs.
5. Classify findings, remediation actions, dependencies, residual risk, and completion criteria.
6. Route high-impact findings or closure packages to `independent-architecture-reviewer`.

Outputs: container/Kubernetes review, IaC control mapping, automation pattern, control integration boundary, resilience analysis, finding register, remediation validation package, assumptions, limitations, and approval state.

Stop conditions: live deployment, production automation enablement, active scan, control operation, destructive change, or approval of remediation closure.
