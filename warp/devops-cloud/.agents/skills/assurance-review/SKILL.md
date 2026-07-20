---
name: assurance-review
description: Use for independent DevOps and Cloud assurance review, cross-section consistency, findings, waivers, completion gates and operational readiness review.
---
# Assurance and Independent Review Skill

Use this skill for section 10 static assurance review. Do not create the primary implementation being reviewed, self-approve, execute validation tools or claim runtime validation.

## Procedure
1. Confirm independence, scope, reviewed artifact, owner, quality gates and evidence available.
2. Assess capabilities: independent-assurance-review, architecture-assurance, pipeline-and-release-assurance, iac-and-cloud-assurance, container-kubernetes-assurance, operational-readiness-assurance, devsecops-assurance, finops-assurance, evidence-and-completion-validation.
3. Review against AWS/Azure/Google Well-Architected concepts, DORA, Google SRE, NIST SSDF/SP 800-204D, CNCF platform guidance and FinOps Framework only as static criteria.
4. Record each finding with evidence, impact, owner, severity, closure criteria, waiver option and re-review trigger.
5. Block completion while critical findings remain unresolved unless a human risk owner grants a documented waiver.

## Quality Gates
- Reviewer independence is explicit.
- Every finding includes evidence, impact, owner, severity and closure criteria.
- Static review is never represented as runtime validation.
- Completion is blocked while critical findings remain unresolved.

Reference: `docs/assurance-review-workflows.md`.
