# Security Architecture Workflows

## Perform Security Architecture Review

1. Confirm authorized scope, business context, lifecycle stage, source artifacts, reviewers, and human approval path.
2. Collect context, components, data flows, trust boundaries, identities, dependencies, deployment, and operations.
3. Identify approved policies, risks, requirements, constraints, and cross-functional authorities.
4. Analyze threats, failure modes, control placement, trust assumptions, resilience, and validation criteria.
5. Produce findings, decisions, requirements, residual risks, and remediation roadmap.
6. Run independent architecture assurance.
7. Route approvals, exceptions, and production decisions to humans.

## Create Reference Security Architecture

1. Confirm scope, consumers, supported environments, variables, and non-goals.
2. Identify common risks, controls, dependencies, secure defaults, prohibited patterns, decision points, evidence, and validation criteria.
3. Check compatibility with approved policies and architecture principles.
4. Perform specialist and independent review.
5. Publish only through human-approved repository process.

## Specialist Workflows

- Identity and privileged-access design: confirm populations, trust domains, authentication assurance, authorization, lifecycle, recovery, privileged paths, logging, review, revocation, and evidence.
- Cloud or platform review: confirm provider, service model, tenancy, regions, responsibility boundaries, data classes, identity, network, workloads, managed services, encryption, logging, resilience, administrative paths, guardrails, and evidence.
- Network segmentation and secure communications: confirm assets, zones, flows, protocols, remote access, lateral movement, bypasses, availability, validation, and handoff.
- Data protection and cryptographic controls: confirm data classes, lifecycle, locations, access paths, integrity, availability, privacy/legal dependencies, encryption, key custody, rotation, recovery, and migration evidence.
- Container, Kubernetes, and IaC review: confirm build, registry, deployment, orchestration, tenancy, secret handling, network, runtime, provenance, policy gates, and evidence without running tools.
- Control pattern design: confirm control objective, threat, supported contexts, dependencies, owner, interfaces, permissions, failure behavior, safe defaults, observability, rollback, approval gates, and acceptance criteria.
- Architecture remediation validation: confirm original finding, accepted plan, evidence requirements, reviewer independence, root cause, affected scope, bypass paths, residual risk, and human closure decision.
