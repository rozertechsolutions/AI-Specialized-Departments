---
name: enterprise-solution-patterns
description: Use when reviewing enterprise, solution, platform, endpoint, or workspace architecture for secure reusable patterns.
user-invocable: true
allowed-tools:
  - read_file
  - grep
  - ask_user_question
---

# Enterprise Solution Patterns

Use this procedure to review designs and document security architecture decisions.

1. Identify assets, trust boundaries, data flows, endpoint and workspace assumptions, and platform dependencies.
2. Map design choices to security patterns and note gaps, conflicts, severity, and confidence.
3. Document alternatives, residual risk, limitations, dependencies, and required human decisions.
4. Produce a decision package with sources and completion criteria.
5. Request `independent-architecture-reviewer` before completion.

Stop for deployment requests, product-security delivery, live control operation, or missing architecture context.

