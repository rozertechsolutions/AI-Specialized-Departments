---
name: cloud-foundation-infrastructure
description: Use for landing-zone design, infrastructure-as-code design and review, state and drift strategy, cloud network design, managed service selection, and resource lifecycle/decommissioning.
---
# Cloud Foundation and Infrastructure Skill

Use this skill for section 02 foundation and infrastructure design only. Produce static artifacts and never execute provisioning or validation tools.

## Procedure
1. Classify the request as `landing-zone-design`, `infrastructure-as-code-design`, `iac-module-review`, `state-and-drift-strategy`, `cloud-network-design`, `managed-service-selection`, or `resource-lifecycle-and-decommissioning`.
2. Confirm requirements before any provider or tool choice. Keep AWS, Azure, Google Cloud, Terraform, OpenTofu, Pulumi, CloudFormation, Bicep, and Ansible references isolated to justified decisions.
3. Define ownership, environment boundaries, state and drift handling, rollback or decommissioning path, and handoff criteria.
4. Review for declarative design, reproducibility, idempotency, no secrets, no real identifiers, and no runtime claims.
5. Escalate provider commitments, state backends, network exposure, managed service adoption, decommissioning, and material risk for human review.

## Stop criteria
Stop on missing requirements, requested cloud authentication, plan/apply/provisioning execution, real account identifiers, private endpoints, secret exposure, or unsupported platform mechanisms.

Reference: `docs/cloud-foundation-infrastructure-workflows.md`.

## Evidence
Return static requirements, assumptions, design decisions, tradeoffs, risks, owners, handoffs, human approvals needed, and checks not run.
