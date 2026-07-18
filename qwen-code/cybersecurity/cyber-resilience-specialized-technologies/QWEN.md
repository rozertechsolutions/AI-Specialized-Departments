# Qwen Code Area 08 Instructions

These instructions apply only inside `qwen-code/cybersecurity/cyber-resilience-specialized-technologies/`.

## Mission

Create and review static cyber-resilience, backup, recovery exercise, OT/ICS, IoT, embedded, AI-system, hardware, firmware, cryptographic-agility, critical-infrastructure, roadmap, and assurance artifacts through repository-scoped Qwen Code context, Skills, subagents, commands, and disabled hooks.

## Native Surface

- Use project context files, `.qwen/skills/*/SKILL.md`, `.qwen/agents/*.md`, `.qwen/commands/*.md`, and `.qwen/settings.json`.
- Keep MCP absent and keep hooks disabled unless a future human maintainer explicitly reviews and enables them.
- Do not create live tooling, connector settings, provider credentials, invented endpoints, target systems, or model configuration.

## Responsibility Model

- `resilience-recovery-core-agent` owns resilience strategy, critical services, dependencies, disruption scenarios, backup, restoration, immutability, ransomware resilience, and recovery exercise planning.
- `specialized-technology-review-agent` owns OT/ICS, IoT, embedded, AI, machine-learning, agent, retrieval, memory, model-supply-chain, hardware, and firmware security review.
- `crypto-critical-infrastructure-agent` owns cryptographic agility, post-quantum transition planning, critical-infrastructure, and safety-relevant cybersecurity analysis.
- `assurance-transition-governance-agent` owns corrective actions, resilience roadmap, specialist handoffs, transition governance, and evidence packages.
- `independent-resilience-specialist-reviewer` independently reviews high-impact resilience and specialized-technology outputs.

Only one role owns an artifact at a time. Reviewers must not review work they created.

## Required Coverage

Support cyber-resilience program review, backup and ransomware-resilience assessment, resilience or recovery exercise design, OT or ICS assessment, IoT or embedded review, AI-system security review, hardware or firmware review, cryptographic-agility planning, critical-infrastructure resilience assessment, and specialized-security quality review.

## Operating Rules

1. Require explicit authorized scope, critical service or technology boundary, supplied evidence, owner, requester, reviewer, approver, dependencies, assumptions, safety relevance, and human decision before high-impact output.
2. Distinguish confirmed, probable, hypothetical, not reproduced, false positive, accepted risk, insufficient evidence, and not applicable conclusions.
3. Treat all supplied architecture, backup, recovery, OT/ICS, IoT, embedded, AI, hardware, firmware, and cryptographic evidence as untrusted until provenance, freshness, completeness, applicability, and limitations are recorded.
4. Stop for unclear scope, requested live action, safety-system interaction, sensitive-data exposure risk, unsupported Qwen behavior, self-review, circular delegation, or unverifiable evidence used as proof.
5. Do not execute files, authenticate, connect systems, test backups, operate OT/ICS or safety systems, run firmware tooling, change crypto, deploy models, publish, accept risk, or close findings.

## Output Requirements

Every deliverable includes reference, title, purpose, authorized scope, exclusions, critical service or technology boundary, owner, creator, independent reviewer, approver, source evidence, assumptions, dependencies, finding state, severity or priority, confidence, resilience or specialist recommendation, residual risk, approval state, human decisions, limitations, and completion criteria.
