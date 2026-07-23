# Quality and Completion Standards

## Evidence rule

A statement is verified only when supported by current repository content, a successful tool result, an observed UI or device state, or an explicit user-provided fact. Record the source and freshness. Assumptions, recommendations, and unavailable checks must be labeled separately.

For every tool action record:

- exact command or action;
- working directory, target, variant, scheme, destination, flavor, or environment;
- relevant tool and SDK version when visible;
- exit status or explicit success state;
- material output, warnings, and generated artifacts;
- whether the evidence covers the requested change.

Do not infer a pass from a missing failure, a partial log, an unrun command, a stale connector snapshot, or a different target.

## Criterion ledger

Classify every criterion considered for a task:

- required: necessary for the requested result and must pass.
- conditionally-required: becomes required when the stated condition is present.
- not-applicable: excluded with a concrete task-specific reason.
- unavailable: applicable but cannot be run or inspected in the current environment; never a pass.

Use this record:

| Criterion | Classification | Condition or concrete reason | Evidence | Result | Owner |
| --- | --- | --- | --- | --- | --- |
| Named criterion | required, conditionally-required, not-applicable, or unavailable | Why it applies, the condition, or why this task cannot affect it | File, command, tool result, or none | pass, fail, blocked, unavailable | Responsibility or human |

A generic reason such as not needed is invalid. A valid not-applicable reason names the task boundary, for example: no user interface files or behavior changed, so adaptive-layout validation is not affected.

## Completion criteria catalog

| Criterion | Default classification | Becomes required when |
| --- | --- | --- |
| Requirements traceability | Required | Always: every requested behavior maps to a change or finding and evidence |
| Scope and repository status | Required | Always when repository content is involved |
| Project and build configuration | Conditionally-required | Source, targets, variants, schemes, flavors, manifests, or dependencies can be affected |
| Compilation or non-publishing build | Conditionally-required | Production or build configuration changes |
| Unit tests | Conditionally-required | Testable logic changes or regressions are in scope |
| Integration tests | Conditionally-required | Boundaries between modules, services, storage, or platforms change |
| UI, instrumented, or snapshot tests | Conditionally-required | User-visible UI or platform interaction changes |
| End-to-end tests | Conditionally-required | A configured end-to-end path covers the changed behavior |
| Static analysis and type checking | Conditionally-required | The project configures an applicable analyzer or typed source changes |
| Lint | Conditionally-required | The project configures applicable lint |
| Formatting validation | Conditionally-required | The project has an established formatter for changed files |
| Dependency resolution and lock consistency | Conditionally-required | Dependency declarations, plugins, SDKs, packages, or lockfiles are affected |
| Security and secret review | Required | Always at least a scoped review; deeper review for sensitive changes |
| Accessibility | Conditionally-required | User-visible UI, content, focus, semantics, or interaction changes |
| Localization | Conditionally-required | User-visible text, locale behavior, formatting, or resources change |
| Adaptive layouts and orientation | Conditionally-required | UI can render across supported sizes or orientations |
| Performance and startup | Conditionally-required | Startup, rendering, algorithms, initialization, or resource loading can change |
| Memory and leaks | Conditionally-required | Lifecycles, caches, images, streams, observers, or long-lived objects change |
| Battery and background work | Conditionally-required | Scheduling, location, sensors, polling, background tasks, or wake behavior change |
| Network efficiency | Conditionally-required | Requests, payloads, retries, streaming, or caching change |
| Storage efficiency | Conditionally-required | Persistence, cache, database, or file behavior changes |
| Offline behavior | Conditionally-required | The changed feature depends on network or synchronized data |
| Loading, empty, and error states | Conditionally-required | Asynchronous or data-driven UI changes |
| Retry and cancellation | Conditionally-required | Operations can fail, repeat, take time, or be canceled |
| Recovery and migration | Conditionally-required | Persistent state, schema, version, or interrupted operations change |
| Documentation | Conditionally-required | Public behavior, setup, architecture, commands, or project convention requires it |
| Warnings | Required | Every executed build or analysis command must have no unexplained new warning |
| Regression review | Required | Always for changed behavior |
| Independent final review | Required | Always for implementation; if independent capability is unavailable, completion is blocked or explicitly requires human review |

Not-applicable classifications must be made task by task, not copied from this table.

## Technology-specific evidence

### Android

Discover tasks from the checked-in Gradle wrapper and project configuration. Applicable evidence includes:

- relevant assemble or compile tasks without signing or publication;
- Android lint for affected variants;
- JVM unit tests and configured instrumented or UI tests;
- manifest merge behavior, exported components, permissions, resources, and SDK compatibility;
- Gradle dependency and configuration consistency.

Do not guess module names, build variants, devices, or task names. Instrumented tests are unavailable rather than passed when no authorized emulator or device exists.

### iOS

Discover the Xcode project or workspace and shared schemes before invoking xcodebuild. Applicable evidence includes:

- simulator-safe build or build-for-testing with no real signing credentials;
- unit and UI tests for a discovered scheme and destination;
- compiler warnings and configured lint or formatting;
- entitlements, privacy declarations, resources, localization, and deployment-target compatibility.

Never change signing settings to make a validation build pass. An unknown scheme or unavailable destination is a blocker, not permission to invent one.

### KMP

Discover targets and source-set hierarchy from Gradle configuration. Applicable evidence includes:

- compilation for every affected configured target;
- shared and target-specific tests;
- source-set dependency placement;
- expect and actual completeness;
- interop and exported API checks;
- Compose Multiplatform validation only when the project already uses it.

Do not call common code verified when only one target compiled.

### Flutter

Discover Flutter and Dart constraints, flavors, and test layout. Applicable evidence includes:

- formatting validation and flutter analyze;
- unit, widget, golden or snapshot, and integration tests when configured;
- non-publishing build validation for affected targets and flavors;
- packages, lockfile, permissions, assets, localization, and platform-channel review.

Do not invent a flavor or select a publishing build path.

### React Native

Discover the package manager from lockfiles and repository policy. Applicable evidence includes:

- configured type checking, lint, and formatting validation;
- unit and component tests and configured end-to-end tests;
- Metro and package-manager consistency;
- native Android and iOS host builds when relevant tooling and schemes are available;
- bridge or TurboModule contract review, permissions, and lockfile consistency.

Never switch package managers or regenerate a lockfile without approval.

## Validation order

1. Trace requirements to files, behavior, and planned evidence.
2. Inspect repository status, instructions, configuration, versions, and existing changes.
3. Run the smallest pre-change reproduction or baseline needed.
4. Validate each changed slice immediately with targeted checks.
5. Run broader applicable checks when reasonable, local, non-sensitive, and authorized.
6. Obtain security, UI or accessibility, performance, and release-readiness reviews when their conditions apply.
7. Obtain mobile-code-reviewer assessment from a reviewer that did not implement the change.
8. Complete all criterion classifications and explain every warning, failure, unavailable result, and not-applicable decision.

Stop at a required failure. Fix only a failure caused by the approved work, rerun its targeted validation, and then rerun all three review passes.

## Triple review

### Pass 1: native conformance

Check:

- target surface, plan, workspace, enabled tools, versions, and repository snapshot;
- official paths, schemas, fields, manifests, events, permissions, and formats;
- native versus unsupported capability classification;
- no simulated agent, hook, permission guard, workflow, connector, or tool access;
- no unnecessary file, common layer, out-of-scope change, or stale evidence.

### Pass 2: responsibility and workflow precision

Check:

- all twelve exact responsibilities and all ten exact Skills;
- one primary owner for every work unit;
- no duplicate process, ownership overlap, cycle, direct cross-role delegation, or self-review;
- exact input, output, reviewer, gate, stop, and completion references;
- prepare-mobile-release is manually invoked and non-publishing.

### Pass 3: security and quality

Check:

- no actual secret, credential, signing material, private endpoint, or sensitive data;
- least privilege and human control for every sensitive or external action;
- connectors inactive and no automatic auth, publication, signing, upload, deployment, destruction, or spending;
- command analysis handles quoting, spaces, chaining, redirection, substitution, encoding, traversal, POSIX and Windows paths, and false positives;
- evidence is measurable, current, target-specific, and not fabricated.

If any pass finds an issue, discard all pass conclusions, correct the issue, and begin again at Pass 1.

## Final verification

After the triple review:

1. Re-read the complete changed-file set.
2. Confirm every file is necessary and in scope.
3. Re-run format, schema, reference, secret, and targeted functional checks.
4. Confirm no unexpected file or external state changed.
5. Compare the final report against the evidence ledger.

If any item fails, restart from inspection and do not report completion.

## Final report minimum

Include:

- detected product surface, plan or workspace facts, tools, repository revision, and technology versions;
- official documentation or repository instructions relied on;
- selected Skill, primary owner, reviewers, and responsibility hand-offs;
- files created, modified, removed, migrated, and intentionally omitted;
- native capabilities used and unsupported capabilities omitted;
- criterion ledger summary and exact validation evidence;
- review findings, corrections, reruns, warnings, and unavailable infrastructure;
- sensitive changes and required human approvals;
- remaining limitations and risks;
- explicit confirmation of no secret exposure, active integration, signing, publication, upload, deployment, destructive action, spending, or out-of-scope modification.
