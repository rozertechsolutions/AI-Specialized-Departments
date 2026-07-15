---
name: independent-architecture-assurance
description: Use when independently reviewing security architecture artifacts for evidence, assumptions, residual risk, and approval readiness.
user-invocable: true
allowed-tools:
  - read_file
  - grep
  - ask_user_question
---

# Independent Architecture Assurance

Use this procedure only for artifacts you did not author.

1. Confirm the artifact scope, owner, reviewer independence, acceptance criteria, sources, and approval path.
2. Check evidence, assumptions, assets, dependencies, limitations, status, severity, confidence, actions, and residual risk.
3. Identify unsupported claims, missing human decisions, production-operation risk, and out-of-scope content.
4. Return severity-ordered findings and readiness recommendation.

Do not approve architecture, accept risk, close findings, perform self-review, or represent drafts as approved.

