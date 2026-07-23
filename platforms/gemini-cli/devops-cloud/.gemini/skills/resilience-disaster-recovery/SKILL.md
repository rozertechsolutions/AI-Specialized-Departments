---
name: resilience-disaster-recovery
description: Use for resilience architecture, RTO/RPO definition, backup/restore strategy, DR plans, failover/failback review, chaos experiment design, and recovery evidence review.
---
# Resilience and Disaster Recovery Skill

Use this skill for section 06 static resilience and recovery design. Do not execute restores, failovers, failbacks, chaos experiments, production recovery, or runtime validation.

## Procedure
1. Classify the request as resilience-architecture, rto-rpo-definition, backup-restore-strategy, disaster-recovery-plan, failover-failback-review, chaos-experiment-design, recovery-evidence-review.
2. Identify service requirements, dependencies, RTO, RPO, backup/restore, retention, data consistency, failover/failback, exercise scope, evidence, and gaps.
3. Use cloud-native backup and recovery services, Kubernetes backup patterns, database and storage recovery patterns, chaos engineering tools as design references only, and multi-region or multi-zone architectures only when justified by requirements.
4. Confirm RTO/RPO rationale, restoration verification strategy, failback/data consistency risks, and human authorization for destructive exercises.
5. Return static evidence, risks, gaps, approvals needed, and checks not run.

Reference: `docs/resilience-disaster-recovery.md`.
