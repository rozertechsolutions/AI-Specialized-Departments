---
name: reference-and-control-patterns
description: Use for security architecture principles, ADRs, reference architectures, reusable engineering patterns, control placement, and governance-ready design packages.
---

# Reference and Control Patterns

Objective: create reusable security architecture patterns and decision records that can be reviewed and approved by humans.

Primary owner: `architecture-governance-agent`.

Workflow:

1. Confirm intended reuse scope, exclusions, assumptions, source versions, and human approval path.
2. Define architecture principles, constraints, control objectives, trust boundaries, dependencies, and failure modes.
3. Produce reference design options with applicability, non-applicability, inherited controls, compensating controls, and limitations.
4. Record decisions as ADRs with alternatives, tradeoffs, residual risk, and completion criteria.
5. Identify implementation handoff tasks without operating or configuring production controls.
6. Route high-impact reference patterns to `independent-architecture-reviewer`.

Stop for standard publication, exception approval, risk acceptance, production configuration, deployment, or unsupported source evidence.
