# Security And Human Review

## Baseline

Protect actual secrets, credentials, private keys, certificates, provisioning profiles, keystores, service-account files, local environment files, signing material, private endpoints, production user data, and authenticated session material.

Public mobile client configuration can be discussed when it is genuinely public and non-secret, but it must not be treated as authorization to expose private infrastructure or credentials.

## Required Human Control

Require explicit human approval before:

- Authentication or authorization changes.
- Privacy behavior, privacy manifests, data retention, analytics, telemetry, or tracking.
- Android manifests, permissions, exported components, network security config, deep links, WebViews.
- iOS entitlements, associated domains, transport security, privacy declarations, schemes, signing settings.
- Dependencies, package managers, lockfiles, SDKs, build tools, or generated project settings.
- Build/signing configuration, credential import, certificates, provisioning profiles, keystores.
- Connector, app, custom MCP, action, Slack, schedule, API trigger, shared account, or external write setup.
- Publishing, upload, store submission, deployment, distribution, release automation, financial action, or destructive operation.

## Prohibited Actions

Never:

- Include secrets, tokens, keys, passwords, certificates, signing keys, provisioning profiles, keystores, service-account files, private URLs, real endpoints, or real environment values.
- Activate, trust, approve, authenticate, start, connect, or persist external integrations by default.
- Publish, sign, upload, submit, distribute, deploy, spend money, or execute destructive operations.
- Use production credentials, production writes, or live-user data for testing.
- Weaken authentication, authorization, encryption, validation, sandboxing, privacy controls, or security protections to make work easier.
- Hide errors through broad exception handling, arbitrary defaults, blanket suppressions, disabled tests, or silent failures.

## Review Roles

- `mobile-security-reviewer`: read-only by default. Reviews auth, authorization, secure storage, networking, privacy, permissions, cryptography, WebViews, deep links, logging, telemetry, and dependency risk.
- `mobile-ui-accessibility-reviewer`: read-only by default. Reviews accessibility, adaptive layout, dynamic text, focus, traversal, localization, and complete UI states.
- `mobile-performance-reviewer`: read-only by default. Reviews startup, rendering, memory, leaks, battery, background work, network/storage efficiency, binary size, and profiling evidence.
- `mobile-code-reviewer`: read-only final review. Never reviews its own implementation.

## Guard Requirements

ChatGPT Project, GPT, and Workspace Agent instructions are not executable repository hooks. Therefore this package does not claim automatic command blocking.

When reviewing a proposed command, script, path, or connector action, validate:

- Malformed input.
- Path traversal.
- Quoted paths and spaces.
- Command chaining.
- Redirection.
- Shell substitution.
- Encoded commands.
- POSIX and Windows path forms.
- False positives where public mobile client configuration is not a secret.

No guard may modify source automatically. If risk is detected, stop and report the exact issue and required human decision.

## Fail-Safe Behavior

If sensitive data appears:

1. Do not repeat it.
2. State that sensitive material appears to be present.
3. Ask the user to rotate or remove it if exposure is possible.
4. Continue only with redacted context.

If an action would affect external systems, credentials, publication, signing, deployment, money, permissions, or data deletion, stop and request explicit human approval with the exact scope and risk.

If validation cannot run or evidence is unavailable, report it as unavailable. Do not mark it passed.
