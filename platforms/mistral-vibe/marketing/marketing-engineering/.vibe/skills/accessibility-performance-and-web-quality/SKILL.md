---
name: accessibility-performance-and-web-quality
description: "Validate accessible interaction, performance, resilience, privacy behavior, security basics, and user-visible quality before release. Use when the named owner has the required inputs and the result must pass independent review."
---

# Accessibility, Performance, and Web Quality

## Mission and owner
**Owner:** Web & Landing Page Engineer

Validate accessible interaction, performance, resilience, privacy behavior, security basics, and user-visible quality before release.

This procedure uses only the native mechanisms configured for `mistral-vibe-code`.

## Required inputs
- approved objective and scope.
- accountable owner and approval authority.
- constraints, deadline, and acceptance criteria.
- approved content/design, site scope, stack, environment, and target indexation.
- form/data purpose, analytics contract, accessibility/performance thresholds, and rollback.

## Preconditions
- The request is inside this procedure's exclusive scope and has one accountable owner.
- Sources, data, systems, markets, channels, time periods, and policies are current enough for the decision.
- Personal data is minimized; secrets, credentials, private endpoints, real account identifiers, and production values remain outside the repository.
- Publication, sending, spending, activation, audience upload, production deployment, migration, deletion, and every other external write remain disabled until explicit human approval.

## Procedure
1. Confirm the exact objective, accountable owner, required decision, approved scope, and human approval authority.
2. Validate every required input; list missing information and material assumptions instead of inventing them.
3. Validate metric definitions, data lineage, comparison windows, baseline, sample integrity, instrumentation quality, and privacy thresholds.
4. Define primary, supporting, diagnostic, and guardrail metrics with formula, grain, owner, source, window, timezone, and exclusions.
5. Separate observed change, plausible driver, correlation, attribution assumption, and supported causal conclusion.
6. Refuse analysis when data quality, sample size, consent, or measurement validity is insufficient.
7. Record evidence or technical basis, contradictions, limitations, risks, dependencies, owners, and unresolved questions.
8. Run the required independent review, set a permitted state, and prepare the named human decision without executing external actions.

## Output contract
- bounded implementation or remediation specification.
- functional, accessibility, performance, privacy, SEO, security, and rollback evidence.
- explicit assumptions, blockers, residual risk, required independent reviewer, next human decision, and permitted state.

The final artifact must identify scope, owner, evidence or technical basis, assumptions, decisions, unresolved questions, risks, required reviewers, next human decision, and exactly one state: `draft`, `blocked`, `review_required`, `ready_for_release_approval`, `human_approved`.

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
