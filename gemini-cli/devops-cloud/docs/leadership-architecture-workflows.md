# Leadership and Architecture Workflows

## new-devops-cloud-request
1. Capture objective, requester constraints, environment class, risk, urgency, and excluded actions.
2. Classify as coordination, architecture, or later-section specialist work.
3. Assign one primary owner and list dependencies, approvals, and evidence.
4. Stop if the request requires secrets, authentication, platform execution, production mutation, or missing authority.

## cloud-target-architecture
1. Gather business outcome, constraints, ownership, non-functional goals, and expected environments.
2. Model target context and deployment boundaries without real account identifiers or endpoints.
3. Define guardrails, exception process, standards, and cross-section handoffs.
4. Record decisions as ADRs and mark review status.

## technology-selection
1. Define requirements, evaluation criteria, constraints, and disqualifiers.
2. Compare options including AWS, Azure, Google Cloud, hybrid, and multicloud only when relevant.
3. Document tradeoffs across operations, security, reliability, performance, cost, and sustainability.
4. Require human approval before adopting a provider, product, or standard.

## architecture-exception-review
1. Name the standard or guardrail and the proposed exception.
2. Record rationale, duration, compensating controls, risk owner, approval need, and expiry trigger.
3. Reject exceptions that bypass safety, hide risk, or lack an accountable owner.

## cross-section-dependency-resolution
1. Map dependency, upstream owner, downstream owner, artifact, acceptance criteria, and blocker.
2. Route implementation to the appropriate later section.
3. Escalate unresolved conflicts without self-approval.
