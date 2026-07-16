---
name: review-mobile-architecture
description: Perform read-only mobile architecture review for modules, state, navigation, dependency direction, and platform boundaries.
---

# Review Mobile Architecture

## Inputs

- Architecture question, supplied project files, module/dependency information, target technologies, and constraints.

## Preconditions

- Treat the task as read-only unless a separate write-capable owner is explicitly assigned.
- Confirm current structure from supplied files; do not invent architecture.
- ChatGPT cannot run repository builds, tests, devices, simulators, signing, or release actions unless a separately enabled native tool supplies verifiable evidence.

## Owner And Reviewers

- Owner: `mobile-architect`.
- Reviewers: `mobile-security-reviewer`, `mobile-performance-reviewer`, and `mobile-code-reviewer`.

## Steps

1. Map current modules, data/control flow, platform/shared boundaries, navigation, and state ownership.
2. Identify dependency-direction risks, duplicated ownership, coupling, migration risk, and public-contract impacts.
3. Recommend the smallest supported architecture change or a no-change decision.
4. Assign implementation to platform owners; the architect does not implement complete features.

## Validation Gates

- Evidence: file references, boundary map, trade-offs, risks, required human approvals, and manual validation needed.
- Completion: every proposed change has one owner and one independent reviewer.

## Prohibited Actions

- Do not edit source as the architect, approve your own ADR, perform release approval, sign, publish, upload, deploy, or fabricate evidence.
