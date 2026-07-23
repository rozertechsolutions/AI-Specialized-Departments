# Consent-Aware Analytics Deployment

## Purpose
Execute a sequential, evidence-based, review-gated Marketing Engineering process and prepare a complete package for an explicit human decision.

## Invocation
Begin only after intake validation identifies exact scope, owner, required inputs, independent reviewers, and approval authority. This workflow does not authorize external or production actions.

## Stages
1. **Validate approved policy inputs.** Capture owner, inputs, output, evidence, checks, risk, and state. Do not advance while a blocker remains.
2. **Define consent states and regions.** Capture owner, inputs, output, evidence, checks, risk, and state. Do not advance while a blocker remains.
3. **Map tags and data flows to states.** Capture owner, inputs, output, evidence, checks, risk, and state. Do not advance while a blocker remains.
4. **Implement or specify fail-safe gating.** Capture owner, inputs, output, evidence, checks, risk, and state. Do not advance while a blocker remains.
5. **Test grant, deny, revoke, expiry, and failures.** Capture owner, inputs, output, evidence, checks, risk, and state. Do not advance while a blocker remains.
6. **Privacy/security QA.** Capture owner, inputs, output, evidence, checks, risk, and state. Do not advance while a blocker remains.
7. **Prepare deployment approval.** Capture owner, inputs, output, evidence, checks, risk, and state. Do not advance while a blocker remains.

## Stage transition contract
A stage may advance only when its owner, inputs, output, evidence, measurable checks, risks, dependencies, reviewer, and next state are recorded. Failed review returns the work to the responsible stage.

## Mandatory gates
- Intake and scope gate.
- Evidence or technical-baseline gate.
- Privacy, consent, rights, accessibility, security, localization, and policy gate when applicable.
- Independent quality gate.
- Explicit human decision gate before any live action.

## Failure behavior
Stop at the affected stage, preserve valid outputs, issue a blocker record, and resume only when the named condition is satisfied. Do not skip, merge, or fabricate a passed gate.

## Final output
A traceable decision package containing the approved objective, owners, evidence, deliverables, measurement or test plan, findings, risks, unresolved items, review records, rollback/recovery needs where applicable, and the exact next human decision.
