# New Feature Development

Identifier: `new-feature-development`

## Purpose

Deliver a new capability from validated requirements through independent review.

## Common Lifecycle

- Lead confirms scope, constraints, exclusions, and available ChatGPT surfaces.
- Requirements and Planning defines acceptance evidence and routing.
- Implementation occurs only after required human approvals.
- Test and Quality records validation evidence and checks not run.
- Code Quality and Engineering Risk reviews remain independent from implementation.
- Documentation and Release Readiness returns a human decision packet and stops before release actions.

## Workflow-Specific Gates

- validated user and system requirements
- acceptance criteria tied to behavior
- architecture fit and boundary review
- implementation slices small enough to validate
- integration evidence and feature-specific documentation

## Required Evidence

- scope and requirement traceability
- approvals needed or obtained
- validation performed and checks not run
- independent review findings
- unresolved limitations and human decisions

# Bug Investigation and Correction

Identifier: `bug-investigation-and-correction`

## Purpose

Find the root cause, apply the smallest safe fix, and prevent regression.

## Common Lifecycle

- Lead confirms scope, constraints, exclusions, and available ChatGPT surfaces.
- Requirements and Planning defines acceptance evidence and routing.
- Implementation occurs only after required human approvals.
- Test and Quality records validation evidence and checks not run.
- Code Quality and Engineering Risk reviews remain independent from implementation.
- Documentation and Release Readiness returns a human decision packet and stops before release actions.

## Workflow-Specific Gates

- observable symptom and reproduction path
- affected versions, paths, and inputs
- root-cause explanation before changing code
- minimal correction that does not mask symptoms
- regression evidence that the symptom is fixed

## Required Evidence

- scope and requirement traceability
- approvals needed or obtained
- validation performed and checks not run
- independent review findings
- unresolved limitations and human decisions

# Controlled Refactoring

Identifier: `controlled-refactoring`

## Purpose

Improve structure while preserving external behavior.

## Common Lifecycle

- Lead confirms scope, constraints, exclusions, and available ChatGPT surfaces.
- Requirements and Planning defines acceptance evidence and routing.
- Implementation occurs only after required human approvals.
- Test and Quality records validation evidence and checks not run.
- Code Quality and Engineering Risk reviews remain independent from implementation.
- Documentation and Release Readiness returns a human decision packet and stops before release actions.

## Workflow-Specific Gates

- explicit invariants and public behavior that must not change
- bounded transformation plan
- compatibility evidence before and after
- regression checks focused on unchanged behavior
- rollback or reversal plan

## Required Evidence

- scope and requirement traceability
- approvals needed or obtained
- validation performed and checks not run
- independent review findings
- unresolved limitations and human decisions

# Architecture Change

Identifier: `architecture-change`

## Purpose

Change boundaries or core structure through a documented decision.

## Common Lifecycle

- Lead confirms scope, constraints, exclusions, and available ChatGPT surfaces.
- Requirements and Planning defines acceptance evidence and routing.
- Implementation occurs only after required human approvals.
- Test and Quality records validation evidence and checks not run.
- Code Quality and Engineering Risk reviews remain independent from implementation.
- Documentation and Release Readiness returns a human decision packet and stops before release actions.

## Workflow-Specific Gates

- decision record with alternatives
- boundary and contract changes
- migration stages and compatibility plan
- engineering-risk and independent architecture review
- rollback plan before implementation

## Required Evidence

- scope and requirement traceability
- approvals needed or obtained
- validation performed and checks not run
- independent review findings
- unresolved limitations and human decisions

# API or Library Evolution

Identifier: `api-or-library-evolution`

## Purpose

Evolve contracts with compatibility, migration, and examples.

## Common Lifecycle

- Lead confirms scope, constraints, exclusions, and available ChatGPT surfaces.
- Requirements and Planning defines acceptance evidence and routing.
- Implementation occurs only after required human approvals.
- Test and Quality records validation evidence and checks not run.
- Code Quality and Engineering Risk reviews remain independent from implementation.
- Documentation and Release Readiness returns a human decision packet and stops before release actions.

## Workflow-Specific Gates

- consumer impact analysis
- contract, schema, source, binary, and behavioral compatibility
- versioning and deprecation plan
- migration notes and examples
- contract tests or explicit untested areas

## Required Evidence

- scope and requirement traceability
- approvals needed or obtained
- validation performed and checks not run
- independent review findings
- unresolved limitations and human decisions

# Dependency Update

Identifier: `dependency-update`

## Purpose

Change dependencies only with need, provenance, and rollback evidence.

## Common Lifecycle

- Lead confirms scope, constraints, exclusions, and available ChatGPT surfaces.
- Requirements and Planning defines acceptance evidence and routing.
- Implementation occurs only after required human approvals.
- Test and Quality records validation evidence and checks not run.
- Code Quality and Engineering Risk reviews remain independent from implementation.
- Documentation and Release Readiness returns a human decision packet and stops before release actions.

## Workflow-Specific Gates

- demonstrated need for the dependency change
- provenance, maintenance, license, and vulnerability signals
- transitive and lockfile impact
- compatibility validation
- rollback path to the previous dependency state

## Required Evidence

- scope and requirement traceability
- approvals needed or obtained
- validation performed and checks not run
- independent review findings
- unresolved limitations and human decisions

# Security Remediation

Identifier: `security-remediation`

## Purpose

Correct a software weakness without unsafe disclosure or broad churn.

## Common Lifecycle

- Lead confirms scope, constraints, exclusions, and available ChatGPT surfaces.
- Requirements and Planning defines acceptance evidence and routing.
- Implementation occurs only after required human approvals.
- Test and Quality records validation evidence and checks not run.
- Code Quality and Engineering Risk reviews remain independent from implementation.
- Documentation and Release Readiness returns a human decision packet and stops before release actions.

## Workflow-Specific Gates

- threat or weakness statement
- affected trust boundary and exploitability assumptions
- secret-safe handling and disclosure-safe reporting
- least-change remediation
- regression evidence for the weakness and related behavior

## Required Evidence

- scope and requirement traceability
- approvals needed or obtained
- validation performed and checks not run
- independent review findings
- unresolved limitations and human decisions

# Performance and Reliability Improvement

Identifier: `performance-and-reliability-improvement`

## Purpose

Improve performance or resilience with guardrails and evidence.

## Common Lifecycle

- Lead confirms scope, constraints, exclusions, and available ChatGPT surfaces.
- Requirements and Planning defines acceptance evidence and routing.
- Implementation occurs only after required human approvals.
- Test and Quality records validation evidence and checks not run.
- Code Quality and Engineering Risk reviews remain independent from implementation.
- Documentation and Release Readiness returns a human decision packet and stops before release actions.

## Workflow-Specific Gates

- observed baseline or explicit absence of one
- hypothesis and resource, concurrency, and failure analysis
- correctness guardrails
- measurement or reasoned evidence
- regression risk and rollback criteria

## Required Evidence

- scope and requirement traceability
- approvals needed or obtained
- validation performed and checks not run
- independent review findings
- unresolved limitations and human decisions

# Technical Debt Reduction

Identifier: `technical-debt-reduction`

## Purpose

Reduce prioritized debt without unrelated cleanup.

## Common Lifecycle

- Lead confirms scope, constraints, exclusions, and available ChatGPT surfaces.
- Requirements and Planning defines acceptance evidence and routing.
- Implementation occurs only after required human approvals.
- Test and Quality records validation evidence and checks not run.
- Code Quality and Engineering Risk reviews remain independent from implementation.
- Documentation and Release Readiness returns a human decision packet and stops before release actions.

## Workflow-Specific Gates

- identified debt and user or maintenance impact
- prioritization rationale
- bounded scope and preserved behavior
- measurable maintainability improvement
- prevention of opportunistic refactors

## Required Evidence

- scope and requirement traceability
- approvals needed or obtained
- validation performed and checks not run
- independent review findings
- unresolved limitations and human decisions

# Maintenance and Compatibility Update

Identifier: `maintenance-and-compatibility-update`

## Purpose

Keep supported environments and contracts working during maintenance.

## Common Lifecycle

- Lead confirms scope, constraints, exclusions, and available ChatGPT surfaces.
- Requirements and Planning defines acceptance evidence and routing.
- Implementation occurs only after required human approvals.
- Test and Quality records validation evidence and checks not run.
- Code Quality and Engineering Risk reviews remain independent from implementation.
- Documentation and Release Readiness returns a human decision packet and stops before release actions.

## Workflow-Specific Gates

- supported environment and contract matrix
- migration, deprecation, data, and configuration implications
- fallback behavior
- compatibility evidence
- explicit non-goals for unrelated modernization

## Required Evidence

- scope and requirement traceability
- approvals needed or obtained
- validation performed and checks not run
- independent review findings
- unresolved limitations and human decisions

# Release Readiness Review

Identifier: `release-readiness-review`

## Purpose

Prepare a human release decision without releasing.

## Common Lifecycle

- Lead confirms scope, constraints, exclusions, and available ChatGPT surfaces.
- Requirements and Planning defines acceptance evidence and routing.
- Implementation occurs only after required human approvals.
- Test and Quality records validation evidence and checks not run.
- Code Quality and Engineering Risk reviews remain independent from implementation.
- Documentation and Release Readiness returns a human decision packet and stops before release actions.

## Workflow-Specific Gates

- acceptance and validation evidence
- unresolved defects and risks
- documentation, changelog, migration, artifact, and version readiness
- rollback readiness
- explicit stop before publication, deployment, signing, submission, or release

## Required Evidence

- scope and requirement traceability
- approvals needed or obtained
- validation performed and checks not run
- independent review findings
- unresolved limitations and human decisions
