---
name: dependency-supply-chain-review
description: Review proposed or changed web dependencies and third-party code.
---

# Dependency Supply Chain Review

Use this skill before adding, upgrading, replacing, removing, or externally loading packages, scripts, SDKs, build plugins, or CDN assets. Do not use it when no dependency or third-party executable input is changing.

1. Confirm necessity, maintenance status, licensing compatibility, provenance, transitive impact, bundle/runtime cost, and known security concerns using authoritative sources.
2. Reject dependency additions that duplicate existing capability without clear value.
3. Do not install packages or execute package-manager commands automatically.
4. Treat scripts, trackers, CDN assets, and build plugins as executable supply-chain inputs.
5. Return approve, reject, or human-review-required with evidence and residual risk.
