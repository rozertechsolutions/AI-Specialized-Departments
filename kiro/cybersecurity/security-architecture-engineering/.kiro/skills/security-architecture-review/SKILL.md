---
name: security-architecture-review
description: Use for structured security architecture review of systems, solutions, platforms, trust boundaries, data flows, controls, and design findings.
---

# Security Architecture Review

Objective: produce a decision-ready security architecture review for an authorized system, solution, or platform.

Primary owner: `enterprise-solution-architecture-agent`.

Workflow:

1. Confirm scope, exclusions, decision needed, owner, reviewer, approver, source versions, and evidence limitations.
2. Inventory assets, actors, identities, management planes, data stores, interfaces, control assumptions, and trust boundaries.
3. Review secure design requirements across identity, network, endpoint, data, cloud, platform, container, IaC, resilience, and operations handoff.
4. Classify findings by severity, confidence, evidence strength, affected asset, dependency, and remediation owner.
5. Separate required changes, recommended patterns, residual risk, and human-only decisions.
6. Route high-impact packages to `independent-architecture-reviewer`.

Stop for architecture approval, risk acceptance, production change, active scanning, authentication, or operation of live controls.
