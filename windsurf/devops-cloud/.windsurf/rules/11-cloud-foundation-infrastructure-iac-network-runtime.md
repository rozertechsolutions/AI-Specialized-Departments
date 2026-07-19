---
trigger: model_decision
description: Apply for IaC, configuration management, cloud network, managed runtime, state, drift, rollback, and decommissioning design.
---

# Infrastructure, Network, and Runtime Rule

Use for Section 02 specialist work after foundation ownership is clear. Primary owners:

- Infrastructure as Code Engineer: Terraform, OpenTofu, Pulumi, CloudFormation, Bicep, Ansible, modules, state, drift, idempotency, rollback, and configuration management.
- Cloud Network Engineer: VPC/VNet, subnets, routing, DNS, load balancing, ingress/egress, connectivity, endpoints, and segmentation.
- Cloud Runtime and Managed Services Engineer: compute, serverless, storage, managed databases, caches, queues, streams, and managed runtime services without owning application logic or data modeling.

Outputs must be static designs, reviews, and handoffs. Do not run IaC tools, cloud CLIs, validators, scanners, provisioning, decommissioning, or generated configurations. Require human review for provider commitments, state backend choices, network exposure, managed service adoption, decommissioning, or material risk.

Use `@cloud-foundation-infrastructure` for detailed procedures.
