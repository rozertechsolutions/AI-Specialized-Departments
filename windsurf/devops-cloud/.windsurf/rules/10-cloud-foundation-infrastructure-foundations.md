---
trigger: model_decision
description: Apply for cloud foundation, landing-zone, account/subscription/project, environment boundary, governance, and lifecycle design.
---

# Cloud Foundation Rule

Use for Section 02 cloud foundation work. Primary owners:

- Cloud Foundation Engineer: landing zones, organizations/accounts/subscriptions/projects, environment separation, baseline governance, ownership, tagging, and lifecycle.
- Cloud and Platform Architect remains owner for provider-neutral architecture decisions before foundation implementation detail.

Required coverage includes AWS, Azure, Google Cloud, hybrid and multicloud only when justified by requirements. Keep provider-specific identifiers, private endpoints, account IDs, subscription IDs, project IDs, and environment-specific values out of repository files.

Stop on requested authentication, provisioning, cloud CLI use, plan/apply execution, private endpoint disclosure, secret exposure, destructive change, unsupported platform behavior, or missing human approval.

Use `@cloud-foundation-infrastructure` for detailed procedures and `/cloud-foundation-infrastructure` only when the user explicitly invokes the manual workflow.
