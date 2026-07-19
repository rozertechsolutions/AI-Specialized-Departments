# Cloud Foundation and Infrastructure

Use this rule for static cloud foundation and infrastructure design. Do not authenticate to cloud accounts, run IaC tools, inspect live state, provision resources, or mutate infrastructure.

## Owners

- Cloud Foundation Engineer: landing zones, organizations/accounts/subscriptions/projects, environment separation, baseline governance, resource lifecycle.
- Infrastructure as Code Engineer: declarative design, modules, state, drift, idempotency, configuration management, change plans.
- Cloud Network Engineer: VPC/VNet, subnets, routing, DNS, load balancing, ingress/egress, connectivity, segmentation.
- Cloud Runtime and Managed Services Engineer: compute, serverless, storage, managed databases, caches, queues, streams, runtime infrastructure.

## Capabilities

Use the `cloud-foundation-infrastructure` Skill and workflow for landing-zone-design, infrastructure-as-code-design, iac-module-review, state-and-drift-strategy, cloud-network-design, managed-service-selection, and resource-lifecycle-and-decommissioning.

## Technology Knowledge

Cover AWS, Azure, Google Cloud, hybrid, multicloud, Terraform, OpenTofu, Pulumi, CloudFormation, Bicep, Ansible, cloud networking, DNS, load balancing, managed services, tagging, ownership, and decommissioning when requirements justify them.

## Quality Gates

- Infrastructure is declarative, reproducible, and idempotent where applicable.
- State, drift, rollback, ownership, and lifecycle are explicit.
- No credentials, real account IDs, private endpoints, or environment-specific values are committed.
- Provider-specific choices are justified and isolated.
- Human review is required for provider selection, network exposure, state backends, managed service adoption, decommissioning, cost impact, and irreversible change.
