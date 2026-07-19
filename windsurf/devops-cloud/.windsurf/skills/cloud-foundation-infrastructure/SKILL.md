---
name: cloud-foundation-infrastructure
description: Use for landing zones, IaC, state and drift, cloud networks, managed services, resource lifecycle, and decommissioning.
---

# Cloud Foundation and Infrastructure Skill

Use for Section 02 static foundation and infrastructure work.

1. Classify the request as landing-zone design, IaC design/review, state and drift strategy, cloud network design, managed service selection, or lifecycle/decommissioning.
2. Keep provider-neutral until requirements justify AWS, Azure, Google Cloud, hybrid, multicloud, Terraform, OpenTofu, Pulumi, CloudFormation, Bicep, or Ansible.
3. Define ownership, environment boundaries, state, drift, rollback/decommissioning path, dependencies, and handoffs.
4. Review for declarative design, reproducibility, idempotency, no secrets, no real identifiers, and no runtime claims.

Do not authenticate, provision, run plans, mutate infrastructure, execute CLIs, or inspect real cloud state.
