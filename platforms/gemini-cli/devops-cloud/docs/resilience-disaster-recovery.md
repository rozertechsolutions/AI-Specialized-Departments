# Resilience and Disaster Recovery Workflows

## resilience-assessment
1. Map service, dependencies, failure domains, RTO/RPO, owners, and current evidence.
2. Identify resilience gaps without running tests.
3. Return prioritized remediation and approvals.

## backup-and-restore-design
1. Define backup scope, retention, integrity, restore sequence, verification strategy, owners, and evidence.
2. Treat backups as unverified until restore verification is designed.
3. Do not restore data.

## disaster-recovery-plan
1. Define scenario, dependencies, recovery order, communications, roles, RTO/RPO, and evidence.
2. Include failback and data consistency risks.
3. Keep runbook static.

## recovery-exercise-plan
1. Define game-day or chaos objective, blast radius, preconditions, abort criteria, approvals, and evidence.
2. Require explicit human authorization.
3. Do not execute experiments.

## failover-readiness-review
1. Review readiness, dependencies, data consistency, rollback/failback, owners, and evidence.
2. Identify blockers and unverified assumptions.
3. Do not trigger failover.

## recovery-gap-remediation
1. Track gap, risk, owner, remediation option, evidence required, and target date.
2. Hand off implementation to the appropriate owner.
3. Reassess only with static evidence.
