---
name: create-mobile-project
description: Plan a new Android, iOS, Kotlin Multiplatform, Flutter, or React Native project with native ownership, validation, and security gates.
---

# Create Mobile Project

## Inputs

- Product goal, target platforms, supported mobile technology, repository constraints, package or bundle identifiers supplied by the user, and acceptance criteria.

## Preconditions

- Confirm the target technology from the user or supplied files.
- Do not invent package names, bundle identifiers, signing teams, credentials, endpoints, or store metadata.
- ChatGPT cannot run repository builds, tests, devices, simulators, signing, or release actions unless a separately enabled native tool supplies verifiable evidence.

## Owner And Reviewers

- Owner: `mobile-architect` until a concrete platform implementation owner is selected.
- Reviewers: `mobile-security-reviewer`, `mobile-test-engineer`, and `mobile-code-reviewer`.

## Steps

1. Identify target platforms and one primary implementation owner.
2. Define module boundaries, project layout, dependency policy, navigation/state direction, and test strategy.
3. List required human decisions for identifiers, accounts, analytics, permissions, privacy, signing, and publication.
4. Produce a smallest viable setup plan with validation commands to run manually.
5. Stop before dependency installation, credential creation, signing, publication, deployment, external integration activation, or paid service use.

## Validation Gates

- Evidence: target technology, ownership map, project layout rationale, required manual commands, risk list, and unresolved user decisions.
- Completion: plan is implementable, reviewers are independent, and all runtime validation is marked pending manual execution.

## Prohibited Actions

- Do not create real credentials, connect services, publish, sign, upload, deploy, run shell commands, or claim runtime checks passed.
