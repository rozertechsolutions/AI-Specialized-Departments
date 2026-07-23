---
description: "user-invoked Offensive Security Authorized Validation workflow for `authorization-scope-roe`. This command is a prompt artifact only and is not executed during repository implementation."
---

# /authorization-scope-roe

Purpose: user-invoked Offensive Security Authorized Validation workflow for `authorization-scope-roe`. This command is a prompt artifact only and is not executed during repository implementation.

Authorized scope: static repository files and supplied redacted evidence for `offensive-security-authorized-validation`.

Inputs: authorized scope, explicit exclusions, evidence inventory, owner, reviewer, approver, intended audience, decision needed, and selected Skill.

Prerequisites: no live system action, authentication, scan, exploit, deployment, publication, external write, or connector/MCP activation is requested.

Stages:

1. Confirm scope, owner, evidence, assumptions, and human decision.
2. Invoke the relevant Skill from: authorization-scope-roe, assessment-campaign-planning, purple-bas-social-governance, findings-cleanup-retest-assurance, independent-offensive-safety-review.
3. Assign one primary owner from: authorization-assessment-planning-agent, emulation-purple-safety-agent, findings-retest-assurance-agent, white-team-deconfliction-agent, independent-offensive-safety-reviewer.
4. Produce intermediate evidence and decision records.
5. Require independent review for high-impact or closure-facing outputs.
6. Return final output with limitations, confidence, approval state, residual risk, and blocked items.

Decision points: stop for missing authorization, unsupported evidence, self-review, out-of-scope request, sensitive-data exposure, human-only approval, or requested live action.

Completion criteria: all required sections are present, evidence states are explicit, reviewers are independent, and no action is claimed executed without supplied proof.
