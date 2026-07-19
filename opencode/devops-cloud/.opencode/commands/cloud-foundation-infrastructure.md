---
description: Static cloud foundation, IaC, networking, managed-service, lifecycle, and decommissioning workflows.
agent: cloud-foundation-engineer
subtask: true
---

# Cloud Foundation and Infrastructure Workflows

## new-cloud-foundation
1. Capture provider constraints, organization/account/subscription/project model, environment classes, ownership, compliance constraints, and lifecycle requirements.
2. Define landing-zone structure, promotion boundaries, baseline governance, tagging, and decommissioning expectations.
3. Require human review for provider commitment, account structure, material risk, or cost-impacting decisions.

## infrastructure-change-design
1. Define desired state, IaC tool constraints, module boundaries, state ownership, rollback expectations, and drift strategy.
2. Keep infrastructure declarative, reproducible, idempotent, and provider-specific choices isolated.
3. Produce static change-plan guidance only; do not run plan/apply or validators.

## iac-review
1. Review module interface, inputs, outputs, state, dependencies, idempotency, lifecycle handling, and provider isolation.
2. Check that secrets, real identifiers, private endpoints, and environment-specific values are absent.
3. Return findings, required corrections, and unverified runtime assumptions.

## network-change-review
1. Review VPC/VNet, subnets, routes, DNS, load balancing, ingress/egress, service endpoints, and segmentation.
2. Identify exposure risks, ownership, rollback path, and downstream dependencies.
3. Require human review for public exposure, cross-environment connectivity, or private network assumptions.

## managed-service-adoption
1. Capture workload requirements, operational model, data classification, lifecycle needs, portability concerns, and cost/risk constraints.
2. Compare managed service options only against explicit requirements.
3. Hand off application logic, schema design, analytics pipelines, security governance, and FinOps decisions to their owners.

## infrastructure-decommissioning
1. Identify owner, dependency map, data retention constraints, rollback window, state cleanup, and evidence requirements.
2. Require human approval before any destructive or irreversible action.
3. Produce static decommissioning guidance only; do not delete, revoke, destroy, or run tooling.
