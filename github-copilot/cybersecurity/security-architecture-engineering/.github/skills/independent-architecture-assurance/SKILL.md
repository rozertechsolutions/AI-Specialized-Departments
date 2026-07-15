---
name: independent-architecture-assurance
description: Use for independent quality review of security architecture packages, decision records, findings, remediation evidence, and approval readiness.
---

# Independent Architecture Assurance

Objective: provide a read-only quality review before human approval or decision.

Primary owner: `independent-architecture-reviewer`.

Workflow:

1. Confirm the reviewer did not create the artifact under review.
2. Check scope, exclusions, source versions, evidence provenance, and decision clarity.
3. Validate that findings, severity, confidence, dependencies, and residual risk are supported by evidence or clearly marked as inference.
4. Identify contradictions, missing boundaries, unowned actions, human-only decisions, and unsupported approval claims.
5. Return required corrections and approval-readiness status without approving the artifact.

Stop for request to approve, accept, close, publish, deploy, change production, or self-review.
