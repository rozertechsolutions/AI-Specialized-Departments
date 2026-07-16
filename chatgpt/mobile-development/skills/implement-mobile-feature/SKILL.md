---
name: implement-mobile-feature
description: Guide scoped mobile feature implementation with one platform owner, independent review, and evidence requirements.
---

# Implement Mobile Feature

## Inputs

- Feature requirements, affected files or supplied project context, target technologies, acceptance criteria, and constraints.

## Preconditions

- Inspect supplied files before planning.
- Select exactly one primary implementation owner for each unit of work.
- ChatGPT cannot run repository builds, tests, devices, simulators, signing, or release actions unless a separately enabled native tool supplies verifiable evidence.

## Owner And Reviewers

- Owner: coordinator-selected `android-engineer`, `ios-engineer`, `kmp-engineer`, `flutter-engineer`, or `react-native-engineer`.
- Reviewers: `mobile-test-engineer`, relevant security/UI/performance reviewers, and `mobile-code-reviewer`.

## Steps

1. Confirm platform evidence and behavior.
2. Partition shared and platform-specific work.
3. Define the smallest complete implementation.
4. Identify tests, fallback/error states, security/privacy impacts, accessibility impacts, and performance risks.
5. Require independent final review after implementation.

## Validation Gates

- Evidence: changed-file plan, owner/reviewer list, required checks, unavailable checks, and stop conditions.
- Completion: all acceptance criteria are addressed or blocked with a concrete reason.

## Prohibited Actions

- Do not self-review, fabricate validation, add dependencies without approval, activate integrations, sign, publish, upload, submit, deploy, or spend money.
