# Quality And Completion Standards

## General Completion Criteria

Classify each criterion in every final answer as `required`, `conditionally-required`, or `not-applicable` with a concrete reason for every `not-applicable` result.

| Criterion | Default classification | Evidence |
| --- | --- | --- |
| Requirements traceability | required | User request mapped to files, screens, APIs, tests, or review questions. |
| Project configuration | conditionally-required | Manifests, build files, schemes, package files, flavors, variants, targets. |
| Compilation/build validation | conditionally-required | Actual command output or unavailable-infrastructure report. |
| Unit tests | conditionally-required | Actual command output or missing-test explanation. |
| Integration/UI/snapshot/end-to-end tests | conditionally-required | Applicable for UI, workflow, platform, or regression changes. |
| Static analysis, lint, type checking, formatting | conditionally-required | Project-defined commands only. |
| Dependency resolution and lockfiles | conditionally-required | Required when dependencies or package files change. |
| Security and secret detection | required | Manual review at minimum; tool evidence when available. |
| Accessibility, localization, adaptive layout | conditionally-required | Required for user-facing UI changes. |
| Performance, memory, battery, startup, rendering | conditionally-required | Required for performance-sensitive changes; claims require measurements. |
| Network, storage, offline, loading, empty, error, retry, cancellation, recovery states | conditionally-required | Required when affected by behavior. |
| Documentation | conditionally-required | Required by project convention or public behavior change. |
| Independent final review | required | `mobile-code-reviewer` or explicit human review; no self-review. |

Unavailable infrastructure is reported as unavailable, never passed.

## Technology Evidence

- Android: discover Gradle tasks before recommending them; consider Android lint, manifests/permissions, unit tests, and instrumented/UI tests.
- iOS: discover workspace/project and schemes; use non-publishing build/build-for-testing paths; consider unit/UI tests, warnings, entitlements, privacy declarations, and absence of real signing credentials.
- KMP: validate target compilation, source-set dependencies, shared/platform tests, `expect`/`actual`, interoperability, and Compose Multiplatform only when present.
- Flutter: consider `flutter analyze`, unit/widget/integration tests, non-publishing build validation, flavors, packages, and permissions.
- React Native: consider type checking, lint, unit/component/end-to-end tests, Metro/package manager, native host builds when available, and bridge review.

## Workflow Field Template

Every workflow uses these fields: objective, trigger, inputs, supported technologies, preconditions, primary owner, reviewers, ordered steps, conditional steps, validation gates, failures, stop conditions, evidence, outputs, acceptance criteria, human approvals, and prohibited actions.

## Workflows

### `create-mobile-project`

- Objective: plan or review creation of a new mobile project without inventing identifiers or credentials.
- Trigger: user asks to create or scaffold a mobile app.
- Inputs: platform choice, app name, package/bundle identifier, targets, UI scope, API needs, testing expectations.
- Supported technologies: Android, iOS, KMP, Flutter, React Native.
- Preconditions: explicit platform and identifiers; no real signing credentials; selected toolchain evidence if implementation is expected.
- Primary owner: platform owner; `mobile-architect` for multi-platform or module decisions.
- Reviewers: `mobile-security-reviewer`, `mobile-test-engineer`, `mobile-release-engineer`, `mobile-code-reviewer`.
- Ordered steps: confirm requirements; detect or request toolchain; define architecture; define package structure; define validation commands; identify approvals; produce setup plan.
- Conditional steps: add KMP boundaries, Flutter flavors, React Native native host review, or iOS/Android permission review only when applicable.
- Validation gates: project opens, dependencies resolve, non-publishing build path, baseline tests, lint/static analysis.
- Failures: missing identifiers, unsupported toolchain, unavailable SDK, dependency install needs approval.
- Stop conditions: signing, publication, external service setup, paid service, destructive command, or unknown identifiers.
- Evidence: supplied requirements, manifests after creation if available, command output if tools run.
- Outputs: project creation plan or reviewed scaffold.
- Acceptance criteria: project structure matches chosen platform and validation plan is complete.
- Human approvals: identifiers, dependencies, signing setup, external integrations.
- Prohibited actions: signing, publishing, uploading, deploying, real credentials, fabricated scaffolds.

### `implement-mobile-feature`

- Objective: implement or plan a feature with platform-appropriate ownership and tests.
- Trigger: user requests new mobile behavior.
- Inputs: requirements, affected files, designs, API contracts, state/navigation expectations.
- Supported technologies: Android, iOS, KMP, Flutter, React Native.
- Preconditions: acceptance criteria, platform evidence, current conventions.
- Primary owner: platform owner; `kmp-engineer` for shared KMP logic.
- Reviewers: `mobile-test-engineer`, `mobile-security-reviewer` if data/permissions/auth are touched, `mobile-ui-accessibility-reviewer` for UI, `mobile-performance-reviewer` if performance-sensitive, `mobile-code-reviewer`.
- Ordered steps: map requirements; inspect current patterns; select owner; plan changes; define tests; implement or advise; validate; review.
- Conditional steps: native bridge review, offline/error states, localization, permissions, telemetry approval.
- Validation gates: targeted tests, build/type/lint checks, UI state coverage, security review when applicable.
- Failures: ambiguous behavior, missing files, failing validation, out-of-scope dependency/API changes.
- Stop conditions: required approval missing, production write, credential need, unsupported tool.
- Evidence: files, diffs, logs, test output, screenshots if supplied.
- Outputs: implementation guidance or validated change summary.
- Acceptance criteria: requirements met with evidence and no unresolved required gate.
- Human approvals: security/privacy, dependency, lockfile, connector, telemetry, permissions.
- Prohibited actions: broad rewrites, self-review, hidden defaults, invented contracts.

### `fix-mobile-bug`

- Objective: diagnose and fix or plan a targeted fix for a mobile defect.
- Trigger: bug report, crash, failing test, regression, log, or screenshot.
- Inputs: reproduction steps, expected/actual behavior, logs, stack traces, affected files, environment.
- Supported technologies: Android, iOS, KMP, Flutter, React Native.
- Preconditions: reproducible evidence or enough context to form bounded hypotheses.
- Primary owner: platform owner matching failure surface.
- Reviewers: `mobile-test-engineer`, `mobile-code-reviewer`; security/performance/UI reviewers as applicable.
- Ordered steps: classify failure; inspect evidence; isolate likely cause; propose minimal fix; add regression test; validate.
- Conditional steps: crash symbolication, device/OS matrix, race/flakiness analysis, rollback path.
- Validation gates: reproduction addressed, regression test, affected suite, static checks.
- Failures: non-reproducible issue, missing logs, unrelated pre-existing failures.
- Stop conditions: production data needed, destructive device operation, credential need, unrelated broad fix.
- Evidence: logs, failing/passing tests, affected code, screenshots.
- Outputs: diagnosis, minimal fix guidance, validation record.
- Acceptance criteria: defect cause addressed and regression evidence captured.
- Human approvals: destructive reproduction, production access, dependency change.
- Prohibited actions: masking errors, disabling tests, broad catches, silent fallbacks.

### `review-mobile-architecture`

- Objective: evaluate architecture, module boundaries, dependency direction, navigation, state, and migrations.
- Trigger: architecture review request or consequential design change.
- Inputs: diagrams, module tree, manifests, build files, data flow, requirements.
- Supported technologies: Android, iOS, KMP, Flutter, React Native.
- Preconditions: sufficient structural evidence.
- Primary owner: `mobile-architect`.
- Reviewers: `mobile-security-reviewer`, `mobile-performance-reviewer`, `mobile-code-reviewer`.
- Ordered steps: map modules; identify boundaries; check dependency direction; review state/navigation; evaluate migrations; document risks.
- Conditional steps: KMP shared/platform split, native bridge boundary, release migration plan.
- Validation gates: consistency with project conventions, testability, migration safety.
- Failures: missing structure, contradictory requirements, unknown runtime boundaries.
- Stop conditions: request turns into full implementation without owner split.
- Evidence: supplied architecture files, source layout, dependency graphs if supplied.
- Outputs: findings, decisions, alternatives, migration plan.
- Acceptance criteria: ownership and boundaries are unambiguous.
- Human approvals: public API, persistence, dependency, migration, security-affecting changes.
- Prohibited actions: release approval, complete feature implementation, unsupported shared runtime.

### `add-mobile-screen`

- Objective: add or plan a user-facing screen with accessibility, localization, states, and tests.
- Trigger: user requests a new screen or UI flow.
- Inputs: design, copy, navigation contract, state sources, API needs, platform files.
- Supported technologies: Android, iOS, Flutter, React Native; KMP only for shared state/business logic.
- Preconditions: UI requirements and navigation destination known.
- Primary owner: UI platform owner.
- Reviewers: `mobile-ui-accessibility-reviewer`, `mobile-test-engineer`, `mobile-code-reviewer`, security/performance if applicable.
- Ordered steps: inspect UI patterns; define states; implement screen or plan; add navigation; add tests; validate accessibility.
- Conditional steps: dynamic text, orientation, localization, empty/error/retry/loading states, screenshot tests.
- Validation gates: UI tests or snapshots where available, accessibility review, lint/type/build checks.
- Failures: missing designs, unknown navigation, inaccessible controls, text overlap, missing states.
- Stop conditions: unclear data contract, auth/privacy changes without approval.
- Evidence: UI files, screenshots, designs, test output.
- Outputs: screen plan or implementation summary.
- Acceptance criteria: screen meets functional and accessibility states.
- Human approvals: copy/product decisions, permissions, telemetry, analytics.
- Prohibited actions: hardcoded secrets, inaccessible UI, unverified visual claims.

### `integrate-mobile-api`

- Objective: integrate or review a mobile API safely with validation, error handling, and privacy controls.
- Trigger: user requests network or backend integration.
- Inputs: API contract, auth model, endpoint environment, data schema, caching/offline requirements.
- Supported technologies: Android, iOS, KMP, Flutter, React Native.
- Preconditions: non-secret API contract and approved auth/privacy model.
- Primary owner: platform owner or `kmp-engineer` for shared networking in KMP.
- Reviewers: `mobile-security-reviewer`, `mobile-test-engineer`, `mobile-code-reviewer`, performance reviewer if high-volume.
- Ordered steps: inspect networking pattern; validate contract; design models; implement errors/retry/cancellation; add tests; review security.
- Conditional steps: certificate pinning review, secure storage, token refresh, offline cache, privacy disclosure.
- Validation gates: unit/integration tests, serialization tests, network failure states, secret scan.
- Failures: missing contract, real secrets, private endpoint, auth uncertainty.
- Stop conditions: credential import, production writes, privacy change without approval.
- Evidence: API docs, models, tests, logs, mock responses supplied by user.
- Outputs: integration plan or reviewed implementation.
- Acceptance criteria: contract handled with secure failure paths and tests.
- Human approvals: auth, privacy, endpoints, analytics, external writes.
- Prohibited actions: embedding secrets, real production calls, fabricated responses as proof.

### `add-mobile-tests`

- Objective: add targeted, deterministic tests without changing production behavior just to pass.
- Trigger: user requests tests or validation gaps are found.
- Inputs: requirements, code under test, test framework, fixtures, failure cases.
- Supported technologies: Android, iOS, KMP, Flutter, React Native.
- Preconditions: test framework and behavior expectations known.
- Primary owner: `mobile-test-engineer`.
- Reviewers: platform owner and `mobile-code-reviewer`.
- Ordered steps: inspect test patterns; choose test level; design fixtures; add tests or plan; run targeted suite; report gaps.
- Conditional steps: UI synchronization, snapshot baselines, emulator/simulator availability, flakiness controls.
- Validation gates: targeted tests pass, affected suite reasonable, no production weakening.
- Failures: unavailable test runner, non-determinism, missing fixtures.
- Stop conditions: need to disable tests, alter behavior solely for tests, destructive devices.
- Evidence: test files, command output, fixture rationale.
- Outputs: test plan or test implementation summary.
- Acceptance criteria: meaningful regression coverage with deterministic evidence.
- Human approvals: golden updates, external services, large fixture data.
- Prohibited actions: arbitrary sleeps, broad mocks hiding behavior, disabled checks.

### `optimize-mobile-performance`

- Objective: improve or evaluate performance using measurements.
- Trigger: performance issue, startup/rendering/memory/battery/network/storage concern.
- Inputs: metrics, traces, profiles, code paths, device/OS/build variant.
- Supported technologies: Android, iOS, KMP, Flutter, React Native.
- Preconditions: measurable target and baseline evidence.
- Primary owner: platform owner for implementation; `mobile-performance-reviewer` for review.
- Reviewers: `mobile-test-engineer`, `mobile-code-reviewer`.
- Ordered steps: define metric; inspect hot path; form hypothesis; propose minimal change; measure before/after; check regressions.
- Conditional steps: startup profiling, rendering traces, memory leak analysis, binary size review, battery/background work review.
- Validation gates: measured baseline and result, correctness tests, no unmeasured claims.
- Failures: no baseline, noisy metric, unavailable profiler.
- Stop conditions: production data needed, unapproved telemetry, risky architecture change.
- Evidence: profiler output, benchmark result, trace, logs.
- Outputs: measurement plan, findings, or optimized change summary.
- Acceptance criteria: improvement or trade-off is measured and reproducible.
- Human approvals: telemetry, background behavior, dependency or architecture changes.
- Prohibited actions: claiming improvement without measurement, sacrificing correctness silently.

### `audit-mobile-security`

- Objective: audit security and privacy posture for a mobile change or project.
- Trigger: security review request or sensitive change.
- Inputs: manifests, entitlements, auth flow, storage, networking, WebViews, dependencies, logs.
- Supported technologies: Android, iOS, KMP, Flutter, React Native.
- Preconditions: enough files to inspect sensitive surfaces.
- Primary owner: `mobile-security-reviewer`.
- Reviewers: `mobile-code-reviewer`; platform owner answers implementation questions.
- Ordered steps: identify assets/data; review auth/storage/network/permissions; review logs/telemetry; inspect dependency risk; list findings.
- Conditional steps: deep links, WebViews, cryptography, privacy manifests, exported components, secure storage.
- Validation gates: no secrets, least privilege, approval gates, documented residual risk.
- Failures: missing sensitive files, secrets discovered, ambiguous auth model.
- Stop conditions: credential exposure, production data, request to weaken controls.
- Evidence: files, settings, dependency manifests, supplied policies.
- Outputs: read-only findings and required approvals.
- Acceptance criteria: risks are categorized with remediation options.
- Human approvals: all security/privacy changes and external integrations.
- Prohibited actions: implementing fixes during same review, exposing secrets, lowering protections.

### `prepare-mobile-release`

- Objective: prepare a manual release readiness plan without signing, uploading, submitting, publishing, deploying, distributing, spending money, or using real signing credentials.
- Trigger: explicit manual release-preparation request.
- Inputs: version, changelog, target platform, variants/flavors/schemes, validation evidence, signing prerequisites.
- Supported technologies: Android, iOS, KMP artifacts, Flutter, React Native.
- Preconditions: manual initiation and release scope.
- Primary owner: `mobile-release-engineer`.
- Reviewers: `mobile-security-reviewer`, `mobile-test-engineer`, `mobile-code-reviewer`, platform owners.
- Ordered steps: confirm release scope; inspect config; verify versioning; define unsigned build validation; collect test evidence; produce checklist; list blockers.
- Conditional steps: store metadata review, privacy labels, symbol/source map handling as manual blocked actions, rollback plan.
- Validation gates: non-publishing build path, tests/lint/static checks, security review, no real signing credentials.
- Failures: missing version, missing validation, signing credentials present, publication requested.
- Stop conditions: signing, uploading, submitting, publishing, deployment, distribution, paid action, credential handling.
- Evidence: config files, command output, review records.
- Outputs: manual release checklist and blocker report.
- Acceptance criteria: readiness is clear without performing prohibited release actions.
- Human approvals: any release-affecting action, signing prerequisite, external upload.
- Prohibited actions: sign, publish, upload, submit, deploy, distribute, spend money, use real credentials.

## Triple Validation

After substantial configuration, planning, implementation, or review, perform these passes:

1. Native conformance: paths, formats, fields, permissions, version/surface compatibility, native/unsupported classification, no simulations, no unnecessary files, no out-of-scope changes.
2. Responsibility/workflow precision: twelve responsibilities, ten workflows, unique ownership, deterministic delegation, no cycles, no conflicts, no self-review, exact gates.
3. Security/quality: no secrets, least privilege, human control, inactive integrations, no automatic publication/signing/upload/deployment/spending/destruction, measurable evidence, no fabricated results.

If any issue is found, correct it, discard the previous pass conclusions, and repeat all three passes.
