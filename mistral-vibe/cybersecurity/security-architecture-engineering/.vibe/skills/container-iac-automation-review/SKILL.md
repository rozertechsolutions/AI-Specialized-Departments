---
name: container-iac-automation-review
description: Use when reviewing container, Kubernetes, IaC, security tooling, or automation architecture patterns.
user-invocable: true
allowed-tools:
  - read_file
  - grep
  - ask_user_question
---

# Container IaC Automation Review

Use this procedure for container, Kubernetes, IaC, security tooling, and automation architecture.

1. Confirm scope, assets, orchestration boundaries, IaC modules, automation purpose, owner, reviewer, and approver.
2. Map guardrails, policy gates, image and runtime assumptions, restricted material handling, and human approval points.
3. Document status, severity, confidence, limitations, dependencies, actions, and residual risk.
4. Separate design recommendations from any production action request.
5. Request `independent-architecture-reviewer` before completion.

Stop for deployment, cluster operation, live key operation, external integration activation, or production control changes.

