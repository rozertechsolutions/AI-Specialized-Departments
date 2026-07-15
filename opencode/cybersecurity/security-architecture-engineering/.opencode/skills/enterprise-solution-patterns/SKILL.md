---
name: enterprise-solution-patterns
description: Use for enterprise, solution, platform, endpoint, or workspace architecture pattern review.
compatibility: opencode
metadata:
  owner: enterprise-solution-architecture-agent
---

# enterprise-solution-patterns

- Objective: review architecture assets for secure reusable patterns and decision readiness.
- Trigger: user asks for enterprise, solution, platform, endpoint, or workspace architecture review.
- Inputs: architecture diagrams, requirements, assets, trust boundaries, data flows, dependencies, constraints.
- Primary owner: `enterprise-solution-architecture-agent`.
- Reviewers: `independent-architecture-reviewer`.
- Steps: inventory assets; map trust boundaries; map patterns; identify gaps; document tradeoffs; prepare decision package.
- Validation gates: assets are mapped; assumptions are labeled; dependencies and residual risk are documented.
- Stop conditions: deployment request, product-security delivery request, production control operation, or missing design context.
- Outputs: design review, pattern map, gap register, dependency register, decision package.
- Human approvals: architecture acceptance, production use, external distribution.
- Prohibited actions: deploying changes, operating controls, approving architecture, or changing live records.

