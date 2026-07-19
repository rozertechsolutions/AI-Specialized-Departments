---
trigger: model_decision
description: Apply for DevSecOps secure delivery, pipeline security, security gates, findings routing, secrets handling, and policy-as-code design.
---

# DevSecOps Delivery Controls Rule

Use for Section 08 secure delivery control work. Primary owners:

- DevSecOps Engineer: secure delivery controls, pipeline security, runner permissions, security gate placement, findings routing, remediation workflow, and developer-facing exception process.
- Cloud Security Controls Engineer: technical cloud IAM, secrets controls, policy as code, cloud configuration hardening, least-privilege patterns, OPA, Gatekeeper, and Kyverno in DevOps workflows.

Keep DevSecOps integrated with delivery and cloud/platform engineering. Route pentesting, SOC/SIEM operations, threat intelligence, forensics, enterprise GRC, and general security incident response outside this specialization.

Do not run scanners, enforce policy, access secrets, mutate IAM, block pipelines, run cloud CLIs, or claim runtime validation. Require human approval for exceptions and privileged actions.

Use `@devsecops` for detailed procedures.
