# Mobile Validation

Classify validation criteria as `required`, `conditionally-required`, or `not-applicable`. Give a concrete reason for every `not-applicable` item.

Check the applicable areas:

- Requirements traceability, project configuration, compilation, tests, static analysis, lint, formatting, dependency resolution, warnings, regression risk, documentation, and independent review.
- Android: Gradle task discovery, non-publishing build tasks, Android lint, manifests and permissions, local unit tests, and instrumented or UI tests when infrastructure exists.
- iOS: project or workspace and scheme discovery, non-publishing build or build-for-testing, unit and UI tests, compiler warnings, configured lint, entitlements, privacy declarations, and absence of real signing credential use.
- KMP: target compilation, source-set dependency placement, shared and platform tests, `expect`/`actual` review, interoperability, and Compose Multiplatform only when present.
- Flutter: `flutter analyze`, unit/widget/integration tests, non-publishing build validation, flavors, packages, and platform permissions when present.
- React Native: type checking, lint, unit/component/end-to-end tests, Metro/package manager checks, native host builds when available, and bridge review.
- Security, accessibility, localization, adaptive layouts, offline behavior, loading/empty/error/retry/cancellation/recovery states, startup, rendering, memory, battery, network, storage, and binary size when relevant.

Unavailable infrastructure must be reported as unavailable, never successful.

