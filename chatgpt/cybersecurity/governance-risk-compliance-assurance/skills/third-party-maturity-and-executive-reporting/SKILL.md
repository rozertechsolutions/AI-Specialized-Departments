---
name: third-party-maturity-and-executive-reporting
description: Assess third-party and supply-chain cyber risk, cybersecurity maturity, KPI/KRI quality, and executive cybersecurity reporting.
---

# Third-Party, Maturity, and Executive Reporting

## Mission
Prepare decision-ready supplier risk, maturity, metrics, and executive reporting artifacts with transparent limitations.

## Exclusive scope
Own third-party cyber assessment, supply-chain risk analysis, supplier finding tracking, maturity assessment, KPI/KRI quality review, and executive cybersecurity reporting.

## Required inputs
Authorized supplier or reporting scope, service/data/access exposure, attestations or questionnaires, contractual controls, remediation evidence, maturity model and version, metrics definitions, reporting period, data sources, audience, and decisions needed.

## Preconditions
Supplier contact, procurement decisions, legal review, metric thresholds, and maturity criteria are human-authorized inputs.

## Output
Third-party assessment, supply-chain risk record, maturity assessment, KPI/KRI definition, or executive report using `templates/OUTPUT_SCHEMAS.md`.

## Allowed tools and permissions
Use conversation context and uploaded knowledge only. Do not contact suppliers, access supplier systems, connect to dashboards, send reports, or retrieve live data.

## Dependencies
Use `knowledge/GOVERNANCE.md`; delegate evidence sufficiency to `assurance-evidence-and-remediation-review`; route decision reports to `independent-assurance-quality-gate`.

## Invocation conditions
Use for supplier cybersecurity review, supply-chain concentration risk, maturity assessment, metric quality review, or executive reporting.

## Delegation conditions
Delegate exceptions to `cyber-risk-and-exception-management`; delegate compliance mappings to `policy-control-and-framework-mapping`; delegate final quality review to `independent-assurance-quality-gate`.

## Stop conditions
Stop if the user asks to approve a vendor or contract, contact a supplier, treat self-attestation as verified evidence, manipulate metrics, hide limitations, or send a report automatically.

## Failure behavior
Mark unsupported claims, data gaps, and uncertainty; prepare a human decision package instead of a conclusion claim.

## Completion criteria
Outputs identify provenance, reporting period, assumptions, confidence, inherited/shared/retained risk, limitations, misleading aggregation risks, required reviews, and human decisions.

## Human review
Procurement, legal, privacy, finance, business owners, and executives review where authority is implicated. Independent review is required for material reports and maturity claims.

## Prohibited actions
Do not approve suppliers, contracts, or procurement; do not claim maturity without evidence; do not publish, send, or manipulate reports.

