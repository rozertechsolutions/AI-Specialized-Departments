---
name: create-mobile-project
description: Create or scaffold a mobile project only after platform, identifiers, toolchain, ownership, validation, and human approval boundaries are known.
compatibility: opencode
metadata:
  owner: mobile-architect
---

# create-mobile-project

- Objective: create a mobile project for Android, iOS, KMP, Flutter, or React Native using stable native tooling already approved by the user.
- Trigger: user explicitly asks to create or scaffold a mobile project.
- Inputs: target technology, app name, package or bundle id, supported platforms, minimum OS versions, UI approach, test expectations, repository path.
- Supported technologies: Android, iOS, KMP, Flutter, React Native.
- Preconditions: exact identifiers and target path are approved; tooling exists locally; dependency and template choices are approved.
- Primary owner: `mobile-architect`.
- Reviewers: platform owner, `mobile-security-reviewer`, `mobile-code-reviewer`; `mobile-release-engineer` if release config is created.
- Steps: detect workspace state; confirm missing identifiers; define ownership; run approved native scaffold command or create minimal project files; add tests/docs required by template; discover validation commands; run safe local checks.
- Conditional steps: add platform hosts only when requested; add KMP shared modules only when requested; add CI or dependencies only after approval.
- Validation gates: project opens or config parses; compile/build if local tooling permits; tests/lint/format where available; secret scan; review.
- Failures: stop on missing SDK/tooling, command requiring install, signing, credentials, paid service, or unknown identifiers.
- Stop conditions: destructive command, external write, unsupported framework, ambiguous public identity.
- Evidence: commands, outputs, files created, unavailable infrastructure, reviewer findings.
- Outputs: scoped project files, validation report, next human actions.
- Acceptance criteria: requested project exists, ownership is clear, checks are classified and run or reported unavailable.
- Human approvals: identifiers, dependencies, lockfiles, signing config, external services, generated templates.
- Prohibited actions: publishing, signing, uploading, deployment, credential import, paid actions, destructive operations.
