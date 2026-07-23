---
name: optimize-mobile-performance
description: Optimize mobile performance only with measured baseline, scoped changes, repeatable validation, and no claimed improvement without evidence.
compatibility: opencode
metadata:
  owner: mobile-performance-reviewer
---

# optimize-mobile-performance

- Objective: improve startup, rendering, memory, battery, background work, network/storage efficiency, or binary size with evidence.
- Trigger: user asks for performance optimization or reports a performance issue.
- Inputs: metric target, affected platform, baseline, profiling data, reproduction steps, constraints.
- Supported technologies: Android, iOS, KMP, Flutter, React Native.
- Preconditions: measurable target or reproducible symptom exists; profiling tooling is available or limitation is documented.
- Primary owner: `mobile-performance-reviewer` for diagnosis, then platform owner for implementation.
- Reviewers: `mobile-test-engineer`, `mobile-code-reviewer`, security reviewer when data/telemetry changes.
- Steps: collect baseline; identify hotspot; propose scoped change; implement through platform owner; rerun measurement; compare results; run regression checks.
- Conditional steps: ask before telemetry, profiling data export, dependencies, external services, or invasive architecture changes.
- Validation gates: before/after metric, compile/tests, no functional regressions, limitations reported.
- Failures: stop if no reliable baseline and user requested proven improvement.
- Stop conditions: paid/prod profiling, credentials, destructive device actions, unsupported tooling.
- Evidence: profiler/benchmark output, environment, changed files, commands.
- Outputs: measured result, implementation, remaining risks.
- Acceptance criteria: improvement is measured or reported as unverified risk reduction, never fabricated.
- Human approvals: telemetry, dependencies, background behavior changes, significant architecture changes.
- Prohibited actions: claiming unmeasured gains, hiding regressions, signing, publishing, destructive commands.
