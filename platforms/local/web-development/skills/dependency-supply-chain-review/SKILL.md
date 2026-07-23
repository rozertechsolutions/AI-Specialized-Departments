---
name: dependency-supply-chain-review
description: Review proposed or changed web dependencies and third-party code.
---

# Dependency Supply Chain Review

## Mission
Review proposed or changed web dependencies and third-party code.

## Trigger boundaries
Use this skill only for proposed or changed dependencies, third-party scripts, SDKs, plugins, build tools, CDN assets, or supply-chain risk review. Do not use it to install packages, select a runtime/provider/model, approve unrelated architecture, or perform release approval.

## Required procedure
1. Confirm necessity, maintenance status, licensing compatibility, provenance, transitive impact, bundle/runtime cost, and known security concerns using authoritative sources.
2. Reject dependency additions that duplicate existing capability without clear value.
3. Do not install packages or execute package-manager commands automatically.
4. Treat scripts, trackers, CDN assets, and build plugins as executable supply-chain inputs.
5. Return approve, reject, or human-review-required with evidence.

## Output contract
- State confirmed scope and evidence.
- Separate facts, assumptions, risks, and unresolved decisions.
- List files or components affected or reviewed.
- State which quality gates are PASS, FAIL, BLOCKED, or NOT APPLICABLE.
- Do not claim execution or success without direct evidence.

## Prohibited actions
- No installation, command execution, Git mutation, deployment, publication, authentication, secret handling, spending, signing, or destructive operation without exact human authorization.
- No unsupported technology assumptions or fabricated completion evidence.
