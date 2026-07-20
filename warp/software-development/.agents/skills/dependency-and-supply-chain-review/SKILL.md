---
name: dependency-and-supply-chain-review
description: Assess necessity, provenance, licensing signals, maintenance, compatibility, transitive risk, and update impact.
---

# Dependency and Supply-Chain Review

## Mission

Assess necessity, provenance, licensing signals, maintenance, compatibility, transitive risk, and update impact.

## Use when

- new dependency
- dependency update
- build-tool change

## Inputs

- dependency proposal or update
- manifest and lock data
- compatibility constraints

## Preconditions

- The task scope and authorized repository area are known.
- Required human approvals are available before sensitive actions.
- Existing project conventions take precedence over generic preferences.

## Procedure

1. Confirm scope, constraints, assumptions, and exclusions.
2. Gather only the evidence necessary for this Skill.
3. Apply the smallest complete professional method.
4. Record findings and distinguish facts from inferences.
5. Escalate decisions outside this Skill's exclusive scope.
6. Return structured evidence to the owning role.

## Outputs

- dependency assessment
- risk and alternatives
- approval requirement

## Failure behavior

Stop without fabricating a result when evidence, permissions, product support, or required context is missing. State exactly what remains unresolved.

## Human review

Human approval is mandatory for destructive, external, dependency, architecture, public-contract, migration, release, deployment, publication, signing, submission, credential, or permission changes.

## Prohibited actions

- Silent scope expansion or unrelated modifications.
- Secret or credential exposure.
- Invented validation results.
- Automatic Git, release, deployment, publication, signing, submission, installation, authentication, or destructive operations.

## Completion criteria

The output is scoped, traceable, evidence-based, compatible with project conventions, explicit about unexecuted checks, and ready for independent review.
