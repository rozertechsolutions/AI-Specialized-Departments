---
name: container-iac-automation-review
description: Use for container, Kubernetes, IaC, security tooling, and automation architecture review.
compatibility: opencode
metadata:
  owner: data-container-automation-agent
---

# container-iac-automation-review

- Objective: review orchestration, IaC, security tooling, and automation design for safe architecture patterns.
- Trigger: user asks about container, Kubernetes, IaC, security tooling, automation, or guardrail patterns.
- Inputs: orchestration design, IaC modules, automation requirements, data classes, restricted material handling, approval model.
- Primary owner: `data-container-automation-agent`.
- Reviewers: `independent-architecture-reviewer`.
- Steps: confirm assets; map orchestration boundaries; review IaC guardrails; design human approval gates; document residual risk.
- Validation gates: automation gates, restricted material handling, dependencies, status, severity, and confidence are explicit.
- Stop conditions: deployment, cluster operation, live key operation, external integration activation, or production control change.
- Outputs: orchestration review, IaC guardrail map, automation package, residual risk notes.
- Human approvals: production use, control activation, environment changes.
- Prohibited actions: deploying IaC, operating clusters, activating integrations, or generating live auth values.

