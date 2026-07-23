# Security Architecture Workflows

## Security Architecture Review

1. Confirm authorized scope, business context, lifecycle stage, and required reviewers.
2. Collect context, components, data flows, trust boundaries, identities, dependencies, deployment, and operations.
3. Identify approved policies, risks, requirements, and constraints.
4. Analyze threats, failure modes, control placement, trust assumptions, resilience, and validation criteria.
5. Produce findings, decisions, requirements, residual risks, and remediation roadmap.
6. Perform independent assurance review.
7. Route approvals, exceptions, and production decisions to humans.

## Reference Architecture Maintenance

1. Confirm scope, consumers, environments, variables, and non-goals.
2. Identify common risks, required controls, dependencies, secure defaults, prohibited patterns, decision points, evidence, and validation criteria.
3. Check compatibility with current approved policies and architecture principles.
4. Perform specialist and independent review.
5. Publish only after human approval through the normal repository process.

## Specialist Workflows

- Identity and privileged access: define identity populations, trust domains, assurance level, authorization, lifecycle, recovery, least privilege, separation of duties, just-in-time access, break-glass, logging, review, revocation, and evidence.
- Cloud or platform: review provider, service model, tenancy, regions, responsibility boundaries, data classes, identity, network, workloads, managed services, encryption, logging, resilience, administrative paths, guardrails, and evidence without environment access.
- Network and secure communications: define assets, zones, flows, protocols, remote access, lateral-movement paths, bypasses, availability risks, implementation criteria, and validation criteria.
- Data and cryptography: define data classes, lifecycle, locations, access paths, integrity, availability, protection states, key custody, rotation, recovery, crypto-agility, privacy/legal review, and migration evidence.
- Container, Kubernetes, and IaC: review build, registry, deployment, orchestration, tenancy, protected material handling, network, runtime, provenance, policy gates, and validation criteria without executing tools.
- Control pattern design: define objective, threat, supported contexts, dependencies, interfaces, permissions, failure behavior, safe defaults, observability, rollback, approval gates, evidence, and acceptance criteria.
- Remediation validation: assess supplied design and implementation evidence statically, then record confirmed, partial, insufficient, or not-verifiable status for human closure.
