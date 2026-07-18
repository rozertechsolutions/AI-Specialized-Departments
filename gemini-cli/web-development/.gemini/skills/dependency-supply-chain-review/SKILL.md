---
name: dependency-supply-chain-review
description: Review proposed or changed web dependencies and third-party code.
---

# Dependency Supply Chain Review

## Mission
Review proposed or changed web dependencies and third-party code.

## Trigger boundary
Use before adding, upgrading, replacing, removing, or externally loading packages, scripts, SDKs, build plugins, or CDN assets. Do not use when no dependency or third-party executable input is changing.

## Procedure
1. Confirm necessity, maintenance status, licensing compatibility, provenance, transitive impact, bundle/runtime cost, and known security concerns using authoritative sources.
2. Reject dependency additions that duplicate existing capability without clear value.
3. Do not install packages or execute package-manager commands automatically.
4. Treat scripts, trackers, CDN assets, and build plugins as executable supply-chain inputs.
5. Return approve, reject, or human-review-required with evidence.

## Output
State decision, evidence, affected files, runtime or bundle impact, unresolved risks, and PASS, FAIL, BLOCKED, or NOT APPLICABLE gates.
