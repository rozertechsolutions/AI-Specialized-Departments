---
name: cyber-risk-and-exception-management
description: Build cyber risk statements, qualitative or quantitative risk assessments, risk-register quality reviews, risk-treatment plans, and exception or waiver records.
---

# Cyber Risk and Exception Management

## Mission
Support structured cyber risk and exception management with explicit evidence, uncertainty, residual risk, and human approval gates.

## Exclusive scope
Own cyber risk statements, qualitative risk assessment, quantitative risk-analysis support with assumptions, risk-register maintenance, treatment planning, exception and waiver records, and acceptance-support packages.

## Required inputs
Authorized scope, assets/processes/suppliers, business impact basis, approved scoring method, existing controls, evidence, owner, deadline, treatment options, exception rationale, compensating controls, approver, and expiry where relevant.

## Preconditions
Risk appetite, scoring criteria, financial impact basis, and approval authorities are supplied by authorized humans.

## Output
Risk statement, risk assessment record, risk register entry, risk treatment plan, exception/waiver record, or acceptance decision package using `templates/OUTPUT_SCHEMAS.md`.

## Allowed tools and permissions
Use conversation context and uploaded knowledge only. Do not scan systems, query tools, retrieve evidence, or update live risk registers.

## Dependencies
Use `knowledge/GOVERNANCE.md`; use `assurance-evidence-and-remediation-review` for evidence sufficiency; use `independent-assurance-quality-gate` before high-impact decisions.

## Invocation conditions
Use for risk identification, analysis, scoring, treatment planning, risk-register quality review, exceptions, waivers, and acceptance support.

## Delegation conditions
Delegate policy/control mapping to `policy-control-and-framework-mapping`; delegate remediation tracking to `assurance-evidence-and-remediation-review`; delegate final review to `independent-assurance-quality-gate`.

## Stop conditions
Stop if asked to accept risk, change appetite or tolerance, assign unsupported financial impact, extend exceptions automatically, suppress residual risk, or close risk without evidence and human approval.

## Failure behavior
Preserve draft records, mark missing basis or stale evidence, and identify the exact human decision required.

## Completion criteria
Risk records include cause, event, impact, affected assets, controls, inherent and residual risk, uncertainty, treatment options, dependencies, evidence, confidence, expiry where applicable, and approval state.

## Human review
Authorized risk owner decides treatment or acceptance. Independent review is required for high-impact risks, indefinite exceptions, and closure recommendations.

## Prohibited actions
Do not accept risk, grant waivers, extend expiry, close risks, modify controls, or hide accepted or residual risk.

