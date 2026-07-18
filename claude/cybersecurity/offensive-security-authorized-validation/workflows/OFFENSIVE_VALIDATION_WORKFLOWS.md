# Offensive Validation Workflows Readme

This artifact belongs to `claude/cybersecurity/offensive-security-authorized-validation/` and supports static Offensive Security Authorized Validation work only. It is a repository-authored instruction artifact and is not executed during validation or implementation.

## Purpose

Preserve professional coverage for: authorization and scoping, rules-of-engagement review, penetration-test planning, adversary-emulation campaign design, Purple Team exercise design, social-engineering assessment planning, offensive finding documentation, BAS design, cleanup assurance, authorized retest planning, offensive quality and safety review.

## Required Inputs

- Authorized scope, explicit exclusions, requester, owner, intended audience, reviewer, approver, and required human decision.
- Supplied static evidence with provenance, source period, freshness, completeness, confidence, and limitations.
- Known assumptions, dependencies, constraints, unresolved questions, and required handoffs.

## Ordered Stages

1. Confirm scope, exclusions, evidence inventory, owner, reviewer independence, and prohibited actions.
2. Classify each conclusion as confirmed, probable, hypothetical, not reproduced, false positive, accepted risk, insufficient evidence, or not applicable.
3. Produce the static artifact with facts, inference, recommendation, residual risk, confidence, and limitations separated.
4. Escalate high-impact, closure, exception, external-facing, safety-relevant, or executive outputs for independent review.
5. Record completion criteria, human-only decisions, blockers, and evidence gaps.

## Stop Conditions

Stop for missing authorization, live-system requests, unredacted sensitive material, external connection requests, unsupported platform behavior, self-review, circular delegation, or unverifiable evidence used as proof.

## Prohibited Actions

Do not execute generated content, install dependencies, authenticate services, connect MCP or apps, scan, probe, exploit, deploy, publish, accept risk, approve decisions, close findings, or claim validation without supplied evidence.
