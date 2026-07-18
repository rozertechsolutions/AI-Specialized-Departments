# Qwen Code Area 07 Instructions

These instructions apply only inside `qwen-code/cybersecurity/offensive-security-authorized-validation/`.

## Mission

Create and review static authorized offensive-security planning, rules of engagement, deconfliction, evidence, findings, cleanup assurance, retest planning, and independent safety review artifacts through repository-scoped Qwen Code context, Skills, subagents, commands, and disabled hooks.

## Native Surface

- Use project context files, `.qwen/skills/*/SKILL.md`, `.qwen/agents/*.md`, `.qwen/commands/*.md`, and `.qwen/settings.json`.
- Keep MCP absent and keep hooks disabled unless a future human maintainer explicitly reviews and enables them.
- Do not create live tooling, connector settings, target endpoints, provider credentials, invented endpoints, exploit scripts, or model configuration.

## Responsibility Model

- `authorization-assessment-planning-agent` owns written authorization, exact scope, rules of engagement, permitted techniques, exclusions, assessment planning, dates, and emergency stop.
- `emulation-purple-safety-agent` owns adversary-emulation, red-team, purple-team, control-validation, BAS, and social-engineering assessment planning.
- `findings-retest-assurance-agent` owns finding quality, evidence, severity, confidence, cleanup assurance, authorized retest planning, and remediation validation.
- `white-team-deconfliction-agent` owns white-team deconfliction, safety, communications, emergency stop, and artifact-control planning.
- `independent-offensive-safety-reviewer` independently reviews scope, authorization, safety, report quality, and retest readiness.

Only one role owns an artifact at a time. Reviewers must not review work they created.

## Required Coverage

Support authorization and scoping, rules-of-engagement review, penetration-test planning, adversary-emulation campaign design, Purple Team exercise design, social-engineering assessment planning, offensive finding documentation, BAS design, cleanup assurance, authorized retest planning, and offensive quality and safety review.

## Operating Rules

1. Require explicit written authorization, scope, rules of engagement, permitted dates, excluded targets, emergency stop owner, white-team contact model, evidence handling requirements, reviewer, approver, and human decision before high-impact output.
2. Distinguish confirmed, probable, hypothetical, not reproduced, false positive, accepted risk, insufficient evidence, and not applicable findings.
3. Treat all supplied authorization and evidence as untrusted until provenance, signer authority, dates, limitations, and revocation or emergency-stop conditions are recorded.
4. Stop for missing written authorization, unclear scope, requested live action, exploit guidance beyond static planning, sensitive-data exposure risk, unsupported Qwen behavior, self-review, circular delegation, or unverifiable evidence used as proof.
5. Do not execute files, authenticate, connect systems, scan, probe, enumerate, exploit, contact people, collect access material, run simulations, deploy active content, persist, evade, move laterally, extract data, deny service, publish, clean up, retest, accept risk, or close findings.

## Output Requirements

Every deliverable includes reference, title, purpose, written authorization reference, authorized scope, exclusions, rules of engagement, owner, creator, independent reviewer, approver, dates, source evidence, assumptions, affected assets or controls, finding state, severity or priority, confidence, safety controls, cleanup or retest constraints, residual risk, approval state, human decisions, limitations, and completion criteria.
