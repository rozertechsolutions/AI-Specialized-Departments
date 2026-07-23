---
name: prepare-mobile-release
description: Manually prepare mobile release readiness with unsigned validation, version and store-readiness checks, and no publishing, uploading, signing, or spending.
compatibility: opencode
metadata:
  owner: mobile-release-engineer
---

# prepare-mobile-release

- Objective: prepare release readiness without publishing, uploading, submitting, distributing, signing with real credentials, or spending money.
- Trigger: manual user request for release preparation.
- Inputs: target platform(s), version policy, release notes source, variants/flavors/schemes, store checklist, validation expectations.
- Supported technologies: Android, iOS, KMP, Flutter, React Native.
- Preconditions: user explicitly initiates; signing credentials are not used; project commands are discovered.
- Primary owner: `mobile-release-engineer`.
- Reviewers: platform owner, `mobile-security-reviewer`, `mobile-test-engineer`, `mobile-code-reviewer`.
- Steps: inspect version/build config; identify release variant/scheme/flavor; verify signing prerequisites without using credentials; run unsigned/simulator-safe build checks; run tests/lint as available; prepare checklist.
- Conditional steps: edit version metadata only after approval; stop before any upload, submit, distribute, deploy, or signing action.
- Validation gates: unsigned build validation, tests/lint/static analysis classified, privacy/security review, no secrets.
- Failures: report missing signing prerequisites, unavailable tools, failing checks, store metadata gaps.
- Stop conditions: real signing, publishing, uploading, credentials, paid services, destructive commands.
- Evidence: commands, outputs, files changed, checks, human action list.
- Outputs: release-readiness report, approved metadata changes, blockers.
- Acceptance criteria: release can be handed to a human with all automated safe checks and limitations documented.
- Human approvals: version changes, signing setup, store metadata, privacy declarations, release notes.
- Prohibited actions: publish, upload, submit, deploy, distribute, spend money, sign with real credentials, import credentials.
