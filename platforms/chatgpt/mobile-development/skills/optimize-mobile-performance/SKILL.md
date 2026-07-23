---
name: optimize-mobile-performance
description: Guide measured mobile performance work for startup, rendering, memory, battery, network, storage, and binary size.
---

# Optimize Mobile Performance

## Inputs

- Performance concern, target platform, baseline evidence, affected flow, measurement tools, and acceptance criteria.

## Preconditions

- Require a measurable problem or clearly state when only static risk review is possible.
- Do not claim improvements without before/after evidence.
- ChatGPT cannot run repository builds, tests, devices, simulators, signing, or release actions unless a separately enabled native tool supplies verifiable evidence.

## Owner And Reviewers

- Owner: platform engineer for implementation; `mobile-performance-reviewer` for read-only review and measurement design.
- Reviewers: `mobile-performance-reviewer` and `mobile-code-reviewer`.

## Steps

1. Define metric, baseline, scenario, device/simulator constraints, and measurement method.
2. Identify likely causes from code and platform behavior.
3. Propose the smallest change with a rollback path.
4. Define manual measurement commands or profiler steps.
5. Require performance review and final code review.

## Validation Gates

- Evidence: baseline requirement, measurement plan, risks, manual validation needed, and residual uncertainty.
- Completion: no performance claim is made without evidence.

## Prohibited Actions

- Do not fabricate metrics, remove functionality, weaken correctness, hide failures, sign, publish, upload, deploy, or spend money.
