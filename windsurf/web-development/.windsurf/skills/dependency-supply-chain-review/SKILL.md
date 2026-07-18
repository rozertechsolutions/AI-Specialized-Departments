---
name: dependency-supply-chain-review
description: Review proposed or changed web dependencies and third-party code.
---

# Dependency Supply Chain Review

## Mission
Review proposed or changed web dependencies and third-party code.

## Invocation and surface
- Cascade: Invoke with `@dependency-supply-chain-review` or allow Cascade to select it when dependencies, lockfiles, third-party scripts, SDKs, build plugins, or CDN assets are proposed or changed.
- Devin Local: Compatible as a project skill; invoke with `/dependency-supply-chain-review` when using Devin Local.
- Not a package manager, installer, vulnerability scanner, MCP server, or external registry integration.

## Inputs and preconditions
Package names, version changes, lockfile or manifest changes, external scripts, SDKs, plugins, CDN assets, intended use, and approval boundaries.

## Expected output and evidence
Approve, reject, or human-review-required with evidence, affected files, runtime or bundle impact, unresolved risk, and NOT EXECUTED checks.

## Stop conditions
Stop with BLOCKED when provenance, license, security, maintenance, compatibility, or human-review evidence is unavailable for a required dependency decision.

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
- Do not run commands, install packages, mutate Git state, deploy, publish, authenticate, handle secrets, spend money, sign artifacts, or perform destructive operations without exact human authorization.
- No unsupported technology assumptions or fabricated completion evidence.
