---
name: independent-architecture-assurance
description: Use for independent security architecture review of evidence, assumptions, residual risk, and approval readiness.
compatibility: opencode
metadata:
  owner: independent-architecture-reviewer
---

# independent-architecture-assurance

- Objective: independently review security architecture artifacts before formal use.
- Trigger: user asks for final review, evidence challenge, readiness review, or independent assurance.
- Inputs: draft artifact, source evidence, assumptions, scope, acceptance criteria, prior findings.
- Primary owner: `independent-architecture-reviewer`.
- Reviewers: none.
- Steps: confirm independence; verify scope; compare claims to evidence; identify gaps; order findings by severity; report readiness.
- Validation gates: self-review is excluded; findings are sourced; approval needs are explicit; unavailable evidence is reported.
- Stop conditions: self-review, approval request from reviewer, production operation, or insufficient evidence.
- Outputs: severity-ordered findings, evidence gaps, residual risk notes, approval requirements, readiness recommendation.
- Human approvals: final acceptance, external use, risk acceptance, architecture approval.
- Prohibited actions: approving architecture, accepting risk, closing findings, modifying files by default, or self-review.

