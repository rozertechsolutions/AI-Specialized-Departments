# /secure-design-code-review

Purpose: user-invoked Application, Product, and DevSecOps Security workflow for `secure-design-code-review`. This command is a prompt artifact only and is not executed during repository implementation.

Authorized scope: static repository files and supplied redacted evidence for `application-product-devsecops-security`.

Inputs: authorized scope, explicit exclusions, evidence inventory, owner, reviewer, approver, intended audience, decision needed, and selected Skill.

Prerequisites: no live system action, authentication, scan, exploit, deployment, publication, external write, or connector/MCP activation is requested.

Stages:

1. Confirm scope, owner, evidence, assumptions, and human decision.
2. Invoke the relevant Skill from: secure-sdlc-review, threat-modeling, secure-design-code-review, supply-chain-ci-release-review, testing-findings-psirt-assurance.
3. Assign one primary owner from: product-security-governance-agent, requirements-threat-modeling-agent, secure-design-code-review-agent, supply-chain-ci-release-agent, testing-findings-psirt-agent, independent-appsec-reviewer.
4. Produce intermediate evidence and decision records.
5. Require independent review for high-impact or closure-facing outputs.
6. Return final output with limitations, confidence, approval state, residual risk, and blocked items.

Decision points: stop for missing authorization, unsupported evidence, self-review, out-of-scope request, sensitive-data exposure, human-only approval, or requested live action.

Completion criteria: all required sections are present, evidence states are explicit, reviewers are independent, and no action is claimed executed without supplied proof.
