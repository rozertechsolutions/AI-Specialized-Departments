---
name: final-marketing-quality-gate
description: "Independently verify requirements, evidence, coherence, traceability, reviews, measurement, risks, and readiness for explicit human approval. Use when the named owner has the required inputs and the result must pass independent review."
---

# Final Marketing Quality Gate

## Mission and owner
**Owner:** Independent Marketing Quality Reviewer

Independently verify requirements, evidence, coherence, traceability, reviews, measurement, risks, and readiness for explicit human approval.

This procedure uses only the native mechanisms configured for `github-copilot`.

## Required inputs
- approved objective and scope.
- accountable owner and approval authority.
- constraints, deadline, and acceptance criteria.
- validated evidence and baseline data.
- measurement definitions, risks, dependencies, and review requirements.

## Preconditions
- The request is inside this procedure's exclusive scope and has one accountable owner.
- Sources, data, systems, markets, channels, time periods, and policies are current enough for the decision.
- Personal data is minimized; secrets, credentials, private endpoints, real account identifiers, and production values remain outside the repository.
- Publication, sending, spending, activation, audience upload, production deployment, migration, deletion, and every other external write remain disabled until explicit human approval.

## Procedure
1. Confirm the exact objective, accountable owner, required decision, approved scope, and human approval authority.
2. Validate every required input; list missing information and material assumptions instead of inventing them.
3. Confirm authoritative sources, contracts, grain, keys, time semantics, retention, deletion, freshness, access policy, metric owners, and change process.
4. Define governed ingestion, transformations, semantic metrics, lineage, quality tests, alerts, recovery, and incident ownership.
5. Protect small or sensitive cohorts, avoid re-identification and undocumented joins, and make freshness and data-quality warnings visible.
6. Reconcile outputs to authoritative sources and test schema, uniqueness, completeness, validity, freshness, volume, and failure recovery.
7. Record evidence or technical basis, contradictions, limitations, risks, dependencies, owners, and unresolved questions.
8. Run the required independent review, set a permitted state, and prepare the named human decision without executing external actions.

## Output contract
- complete strategy, campaign, journey, channel, or launch plan.
- owners, dependencies, measurement, risk, review findings, and approval checklist.
- explicit assumptions, blockers, residual risk, required independent reviewer, next human decision, and permitted state.

The final artifact must identify scope, owner, evidence or technical basis, assumptions, decisions, unresolved questions, risks, required reviewers, next human decision, and exactly one state: `draft`, `blocked`, `review_required`, `ready_for_human_approval`, `human_approved`.

## Quality checks
- Every requirement maps to one owned output and a measurable completion criterion.
- Material claims cite evidence; technical changes map to contracts and validation evidence.
- Privacy, consent, rights, accessibility, security, localization, policy, data quality, and rollback are reviewed when applicable.
- The creator does not perform the independent final approval.
- No external or production action has occurred.

## Stop conditions
- A required input, owner, permission, policy, evidence source, contract, environment, test, rollback, reviewer, or approval authority is missing or contradictory.
- The requested method is deceptive, discriminatory, manipulative, insecure, privacy-invasive, policy-evading, or outside approved scope.
- Current official requirements cannot be verified for a material decision.

## Failure behavior
Return a blocker record with completed work, missing items, risk, safe alternatives, required owner, and the exact condition for resumption. Do not silently weaken requirements.

## Completion criteria
- The output contract is fully satisfied.
- Evidence, limitations, risks, dependencies, review results, and next human decision are explicit.
- Independent review is ready or completed as required.
- No forbidden action or scope expansion occurred.
