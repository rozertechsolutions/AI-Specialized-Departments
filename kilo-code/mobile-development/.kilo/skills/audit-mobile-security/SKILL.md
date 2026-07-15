---
name: audit-mobile-security
description: Use when auditing mobile security, privacy, auth, secure storage, network security, permissions, cryptography, WebViews, deep links, logs, telemetry, or dependency risk.
---

# audit-mobile-security

- Objective: Perform a read-only security and privacy audit with actionable, evidence-backed findings.
- Trigger: User asks for security review, privacy audit, permission review, dependency risk review, auth review, WebView/deep-link review, or release security check.
- Inputs: Target scope, changed files or repository area, manifests, entitlements, privacy declarations, networking code, storage code, logs, dependency files, and validation evidence.
- Supported technologies: Android, iOS, KMP, Flutter, React Native.
- Preconditions: Avoid reading genuine secrets unless explicitly authorized. Confirm scope and available files before assessing.
- Primary owner: `mobile-security-reviewer`.
- Reviewers: `mobile-code-reviewer`; platform owners implement fixes.
- Steps: Inspect relevant files; identify data flows and trust boundaries; review permissions, storage, networking, logging, telemetry, WebViews, deep links, and dependencies; classify findings; record human approval requirements; avoid edits.
- Validation gates: Findings have severity, evidence, affected files, remediation, and clear separation from implementation.
- Failures: Stop on required secret access, unavailable context, active external authentication, or implementation request.
- Stop conditions: User asks reviewer to edit, import credentials, activate integrations, publish, sign, deploy, or run destructive commands.
- Evidence: Files/lines reviewed, command summaries, dependency risk notes, unavailable context, and not-applicable reasons.
- Outputs: Security findings, open questions, remediation guidance, and residual risk.
- Acceptance criteria: Audit is read-only, scoped, evidence-backed, and does not claim success without verification.
- Human approvals: Required for all auth, privacy, dependency, credential, signing, release, telemetry, and external integration decisions.
- Prohibited actions: Editing, secret exfiltration, credential use, external service activation, publishing, signing, deployment, destructive commands, and fabricated clearance.

