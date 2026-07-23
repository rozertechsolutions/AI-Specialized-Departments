---
name: dependency-supply-chain-review
description: Use to evaluate proposed or changed web dependencies, package scripts, CDN assets, trackers, and third-party code before adoption.
---

# Dependency Supply Chain Review

## Mission
Assess dependency and third-party code risk before adoption or release. This Skill may use official public documentation when current package facts are needed, but it must not install or execute packages by default.

## Use When

- A dependency, package manager, build plugin, CDN asset, analytics/tracker, script, SDK, font, or third-party service is proposed or changed.
- A release review needs supply-chain evidence.
- The user asks whether a package is necessary, safe, maintained, or compatible.

## Inputs

- Package or third-party name, version or proposed range, intended use, current alternatives in the project, license requirements, runtime target, bundle/performance constraints, and repository evidence.

## Procedure

1. Confirm necessity, maintenance status, licensing compatibility, provenance, transitive impact, bundle/runtime cost, and known security concerns using authoritative sources.
2. Reject dependency additions that duplicate existing capability without clear value.
3. Do not install packages or execute package-manager commands automatically.
4. Treat scripts, trackers, CDN assets, and build plugins as executable supply-chain inputs.
5. Return approve, reject, or human-review-required with evidence.

## Output Contract

- Decision: APPROVE, REJECT, HUMAN REVIEW REQUIRED, or BLOCKED.
- Evidence for necessity, provenance, maintenance, license, security, privacy, bundle/runtime impact, and alternatives.
- Required approvals, tests, lockfile review, and rollback notes.
- Items not independently verified.

## Stop Conditions

Stop and report BLOCKED when version, license, source, intended use, security impact, or approval authority is unclear.

## Prohibited Actions

- Do not install, update, remove, or execute packages or scripts without exact human authorization.
- Do not approve trackers, third-party scripts, or external services without privacy and security review.
