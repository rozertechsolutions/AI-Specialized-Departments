# Experiment Implementation and Validation

## Purpose
Execute a sequential, evidence-based, review-gated Marketing Engineering process and prepare a complete package for an explicit human decision.

## Invocation
Begin only after intake validation identifies exact scope, owner, required inputs, independent reviewers, and approval authority. This workflow does not authorize external or production actions.

## Stages
1. **Freeze experiment contract.** Capture owner, inputs, output, evidence, checks, risk, and state. Do not advance while a blocker remains.
2. **Implement assignment, flags, and exposure.** Capture owner, inputs, output, evidence, checks, risk, and state. Do not advance while a blocker remains.
3. **Validate balance, persistence, contamination, metrics, and failure behavior.** Capture owner, inputs, output, evidence, checks, risk, and state. Do not advance while a blocker remains.
4. **Configure monitoring and kill switch.** Capture owner, inputs, output, evidence, checks, risk, and state. Do not advance while a blocker remains.
5. **Independent QA.** Capture owner, inputs, output, evidence, checks, risk, and state. Do not advance while a blocker remains.
6. **Prepare launch/stop approval.** Capture owner, inputs, output, evidence, checks, risk, and state. Do not advance while a blocker remains.

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
