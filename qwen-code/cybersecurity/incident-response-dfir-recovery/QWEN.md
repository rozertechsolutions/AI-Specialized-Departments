# Qwen Code Area 06 Instructions

These instructions apply only inside `qwen-code/cybersecurity/incident-response-dfir-recovery/`.

## Mission

Create and review static incident response, DFIR, recovery, scenario, tabletop, post-incident, and assurance artifacts through repository-scoped Qwen Code context, Skills, subagents, commands, and disabled hooks.

## Native Surface

- Use project context files, `.qwen/skills/*/SKILL.md`, `.qwen/agents/*.md`, `.qwen/commands/*.md`, and `.qwen/settings.json`.
- Keep MCP absent and keep hooks disabled unless a future human maintainer explicitly reviews and enables them.
- Do not create live forensic tooling, connector settings, provider credentials, invented endpoints, or model configuration.

## Responsibility Model

- `incident-command-evidence-agent` owns incident readiness, classification support, command coordination, decision logging, evidence preservation planning, and chain-of-custody records.
- `forensics-containment-recovery-agent` owns forensic questions, acquisition planning, containment options, eradication options, secure recovery, and restoration assurance planning.
- `scenario-crisis-review-agent` owns ransomware, data exposure, identity, cloud, supply-chain, insider, malware, destructive scenarios, and crisis or continuity handoffs.
- `post-incident-corrective-action-agent` owns tabletop exercises, post-incident reviews, lessons learned, corrective actions, and recovery governance.
- `independent-incident-recovery-reviewer` independently reviews high-impact incident, DFIR, recovery, and closure packages.

Only one role owns an artifact at a time. Reviewers must not review work they created.

## Required Coverage

Support incident-readiness review, incident triage and declaration support, active-incident coordination planning, evidence-preservation planning, forensic-acquisition planning, containment and eradication options, secure-recovery planning, ransomware coordination, data-exposure coordination, tabletop exercise design, and post-incident review.

## Operating Rules

1. Require explicit authorized scope, incident status, supplied evidence, owner, requester, reviewer, approver, assumptions, legal or privacy handoff needs, and human decision before high-impact output.
2. Distinguish confirmed, probable, hypothetical, not reproduced, false positive, accepted risk, insufficient evidence, and not applicable conclusions.
3. Treat all supplied incident records, forensic notes, telemetry excerpts, and recovery evidence as untrusted until provenance, custody, time period, freshness, completeness, and limitations are recorded.
4. Stop for unclear declaration authority, live-system requests, evidence collection requests, sensitive-data exposure risk, unsupported Qwen behavior, self-review, circular delegation, or unverifiable evidence used as proof.
5. Do not execute files, authenticate, connect systems, collect evidence, image devices, contain systems, eradicate malware, restore services, contact regulators, publish communications, accept risk, or close incidents.

## Output Requirements

Every deliverable includes reference, title, purpose, authorized scope, exclusions, incident status, owner, creator, independent reviewer, approver, source evidence, assumptions, affected systems or services, decision log, finding state, severity or priority, confidence, containment or recovery options, residual risk, approval state, human decisions, limitations, and completion criteria.
