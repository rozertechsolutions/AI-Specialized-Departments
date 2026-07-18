---
name: dependency-supply-chain-review
description: Review proposed or changed dependencies, package scripts, CDN assets, trackers, SDKs, fonts, and third-party web code before adoption.
---

# Dependency Supply Chain Review

## Mission
Review proposed or changed web dependencies and third-party code.

## Use when
- A dependency, package manager, build plugin, CDN asset, tracker, SDK, font, or third-party service is proposed or changed.

## Do not use when
- No dependency, script, external asset, or third-party code is involved.

## Inputs
Package or provider name, version/range, intended use, current alternatives, license needs, runtime target, bundle constraints, and repository evidence.

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

## Stop and failure behavior
Return BLOCKED when version, source, license, intended use, security impact, or approval authority is unclear.

## Review requirements
Return APPROVE, REJECT, HUMAN REVIEW REQUIRED, or BLOCKED with evidence for necessity, provenance, maintenance, license, security, privacy, runtime impact, alternatives, and rollback.

## Prohibited actions
- No installation, command execution, Git mutation, deployment, publication, authentication, secret handling, spending, signing, or destructive operation without exact human authorization.
- No unsupported technology assumptions or fabricated completion evidence.
