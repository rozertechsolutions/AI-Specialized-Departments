---
name: implement-mobile-feature
description: Implements a scoped mobile feature across applicable data, domain, UI, navigation, errors, offline behavior, tests, and independent reviews. Use when the user requests new behavior in an existing Android, iOS, KMP, Flutter, or React Native project.
---

# Implement Mobile Feature

## Objective and trigger

Deliver the smallest complete feature in an existing mobile project, with
traceable behavior, appropriate tests, specialist review, and no unintended
architecture or platform changes. Activate for a feature request, not a defect,
architecture-only review, single-screen-only request, or release preparation.

Use only project-allowed tools and approved local commands. Skill activation
does not broaden permissions or authorize dependency/external-service changes.

## Inputs

- User-visible behavior, acceptance criteria, non-goals, and compatibility.
- Affected platforms, modules, targets, screens, APIs, and data classifications.
- Required loading/empty/error/retry/cancellation/offline/recovery states.
- Existing architecture, design, tests, rollout/migration, and review constraints.

## Preconditions and ownership

Inspect actual instructions, status/diff, architecture, entry points, data flow,
navigation, dependencies, and tests before editing. Resolve ambiguous behavior.

Choose exactly one primary implementation owner: `android-engineer` for
Android-only code, `ios-engineer` for iOS-only code, `kmp-engineer` for established
shared KMP logic, `flutter-engineer` for Flutter, or `react-native-engineer` for
React Native. Additional platform agents own only explicit native-host files. `mobile-architect` is
required for boundary/state/navigation/public-contract changes.
`mobile-test-engineer`, security/UI/performance reviewers as applicable, and
`mobile-code-reviewer` provide independent stages.

## Workflow and gates

1. **Requirement gate:** turn each acceptance criterion into observable behavior
   and list non-goals, edge cases, data sensitivity, and affected platforms.
2. **Inspection gate:** map current architecture, state/navigation ownership,
   API/storage boundaries, feature flags, UI conventions, and test seams using
   exact file evidence. Inspect all files that will be edited.
3. **Ownership gate:** select one primary owner and assign disjoint files. Obtain
   architecture review before any boundary, public API, schema, persistence,
   dependency-direction, or navigation ownership change.
4. **Design gate:** define data/domain/UI contracts and complete state matrix.
   Specify validation, authorization, cancellation, retries, offline/conflict
   behavior, accessibility, localization, telemetry redaction, and migration.
5. **Implementation:** primary owner makes the smallest cohesive change following
   existing patterns. Native-host work is handed to Android/iOS owners with exact
   contracts. No speculative abstraction or unapproved framework/dependency.
6. **Test gate:** `mobile-test-engineer` maps risks to deterministic unit and
   applicable integration/UI/widget/component/E2E coverage. Run targeted checks.
7. **Specialist gates:** require security for sensitive data/auth/network/storage/
   permissions; UI/accessibility for user interface; performance for meaningful
   startup/render/network/storage/background risk. Resolve blocking findings.
8. **Validation gate:** run discovered platform compile, lint/static/format,
   tests, and broader reasonable checks. Record warnings and unavailable checks.
9. **Independent review gate:** `mobile-code-reviewer` traces requirements to
   code/tests/evidence. Correct findings, rerun affected checks, and repeat review.

## Completion classification

Classify before work and at exit: requirements/scope; configuration; compilation;
unit/integration/UI/snapshot/E2E tests; lint/static/formatting; dependencies;
security/secrets; accessibility/localization/adaptive UI; performance/memory/
battery/network/storage/offline; complete UI and recovery states; documentation;
warnings; regressions; independent review; and platform-native checks. Use only
`required`, `conditionally-required`, or `not-applicable`, each with a concrete
reason. Only executed successful checks may be `passed` in evidence.

## Errors and stop conditions

Stop for unresolved requirements, overlapping ownership, architecture/public API/
persistent format changes without approval, dependency changes, credentials,
external writes, production services, signing/release actions, destructive
commands, conflicting user changes, security uncertainty, or unfixable failures.

## Outputs, evidence, and acceptance

Return scope/owner matrix, requirements traceability, exact files and behavior,
state/error/offline design, tests, commands/results, specialist findings,
completion ledger, warnings, unavailable checks, risks, and human actions.

Acceptance requires all requested behavior and applicable states, scoped changes,
successful available validation, no unresolved blocking specialist finding, and
an independent reviewer pass. Unavailable infrastructure remains explicit.

## Human review and prohibited actions

Humans approve material architecture, dependencies, persistent/public contracts,
credentials, external effects, and release actions. Never install/update packages,
invent contracts, use secrets, contact production, enable MCP, sign, publish,
upload, deploy, submit, destroy data, or perform Git writes without authorization.
