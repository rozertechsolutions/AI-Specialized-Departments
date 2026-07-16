---
name: audit-mobile-security
description: Perform read-only mobile security and privacy audit with risk classification and human-review gates.
---

# Audit Mobile Security

## Inputs

- Audit scope, supplied files, manifests, entitlements, dependency files, network config, auth/storage code, and privacy constraints.

## Preconditions

- Treat the workflow as read-only.
- Do not request or expose credentials, tokens, private keys, certificates, provisioning profiles, keystores, production data, or session material.
- ChatGPT cannot run repository builds, tests, devices, simulators, signing, or release actions unless a separately enabled native tool supplies verifiable evidence.

## Owner And Reviewers

- Owner: `mobile-security-reviewer`.
- Reviewer: `mobile-code-reviewer`.

## Steps

1. Inspect supplied evidence for secrets, auth, secure storage, transport security, permissions, WebViews, deep links, logging, telemetry, dependency risk, and privacy declarations.
2. Distinguish public client config from confidential credentials.
3. Classify findings by risk and cite files.
4. Define required human approvals and manual validation.
5. Return fixes to platform owners; the reviewer does not implement by default.

## Validation Gates

- Evidence: file references, risk levels, exploitability/impact, false positives, and stop conditions.
- Completion: no sensitive data is exposed and every finding has an owner.

## Prohibited Actions

- Do not edit files by default, reveal secrets, approve sensitive changes alone, activate services, sign, publish, upload, deploy, or access production systems.
