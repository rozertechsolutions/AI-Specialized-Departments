---
name: audit-mobile-security
description: Audit mobile security and privacy surfaces read-only by default, with findings, approvals, and no credential handling.
compatibility: opencode
metadata:
  owner: mobile-security-reviewer
---

# audit-mobile-security

- Objective: audit mobile security, privacy, secrets, permissions, auth, storage, networking, WebViews, deep links, logging, telemetry, and dependency risk.
- Trigger: user asks for security audit or sensitive change review.
- Inputs: target scope, diff or project files, threat concerns, manifests, entitlements, dependency manifests.
- Supported technologies: Android, iOS, KMP, Flutter, React Native.
- Preconditions: scope is known; no secrets need to be opened or transmitted.
- Primary owner: `mobile-security-reviewer`.
- Reviewers: `mobile-code-reviewer`; platform owner for remediation.
- Steps: inspect sensitive surfaces; scan for likely secrets; review permissions/entitlements/network/storage/auth/deep links/WebViews/logging/telemetry/dependencies; classify findings; propose fixes.
- Conditional steps: perform source edits only after coordinator approval and owner assignment.
- Validation gates: findings have file references and severity; false positives are identified; required human approvals are listed.
- Failures: stop on discovered secrets or required credential access.
- Stop conditions: production systems, real credentials, external secret scanning service, destructive commands.
- Evidence: file references, commands, findings, unavailable checks.
- Outputs: audit report, remediation plan, validation gaps.
- Acceptance criteria: sensitive criteria classified and no unresolved blocking risk is hidden.
- Human approvals: auth/privacy/crypto/network/telemetry/dependency/signing changes.
- Prohibited actions: credential handling, enabling integrations, uploading code/logs, publishing, signing, destructive commands.
