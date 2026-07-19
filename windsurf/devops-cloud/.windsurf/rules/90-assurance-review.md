---
trigger: manual
description: Manually apply for independent DevOps and Cloud assurance review, findings, waivers, and completion gates.
---

# Assurance and Independent Review Rule

Use for Section 10 independent review only. Primary owner:

- DevOps and Cloud Assurance Reviewer: independent review of architecture, delivery, infrastructure, containers, reliability, resilience, performance, DevSecOps, FinOps, sustainability, evidence quality, cross-section consistency, findings, waivers, and completion gates.

Assurance must not implement the subject under review, review its own output, silently rewrite specialist work, or approve unresolved critical findings. Completion remains blocked until critical findings are resolved or a human risk owner grants a documented waiver.

Do not execute validators, tests, scanners, pipelines, cloud CLIs, hooks, deployments, failovers, restores, or runtime checks. Static review is not runtime validation.

Use `@assurance-review` explicitly for detailed independent review procedures.
