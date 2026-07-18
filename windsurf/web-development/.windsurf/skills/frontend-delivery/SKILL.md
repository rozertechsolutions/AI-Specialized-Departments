---
name: frontend-delivery
description: Plan or implement frontend work within the repository’s native stack.
---

# Frontend Delivery

## Mission
Plan or implement frontend work within the repository’s native stack.

## Invocation and surface
- Cascade: Invoke with `@frontend-delivery` or allow Cascade to select it for scoped frontend planning or implementation after stack, acceptance criteria, and approval boundaries are clear.
- Devin Local: Compatible as a project skill; invoke with `/frontend-delivery` when using Devin Local.
- Not a browser automation, app preview, hook, workflow, external design tool, or custom agent.

## Inputs and preconditions
UI scope, affected components or routes, API assumptions, target browsers or viewports, design constraints, prohibited changes, and verification expectations.

## Expected output and evidence
Changed or proposed files, behavior, state and error handling, responsive and keyboard/focus notes, API assumptions, reviewer handoffs, evidence, risks, and NOT EXECUTED checks.

## Stop conditions
Stop with BLOCKED for unclear UI requirements, unresolved API assumptions, missing approval, inaccessible user-facing states, or missing review evidence.

## Required procedure
1. Preserve semantic HTML, keyboard access, focus behavior, responsive layout, localization readiness, and browser compatibility.
2. Keep state ownership explicit and avoid duplicating server authority on the client.
3. Handle loading, empty, error, offline or degraded states when relevant.
4. Avoid unreviewed third-party scripts, trackers, and dependencies.
5. Return changed scope, behavior, evidence, limitations, and reviewer handoff.

## Output contract
- State confirmed scope and evidence.
- Separate facts, assumptions, risks, and unresolved decisions.
- List files or components affected or reviewed.
- State which quality gates are PASS, FAIL, BLOCKED, or NOT APPLICABLE.
- Do not claim execution or success without direct evidence.

## Prohibited actions
- Do not run commands, install packages, mutate Git state, deploy, publish, authenticate, handle secrets, spend money, sign artifacts, or perform destructive operations without exact human authorization.
- No unsupported technology assumptions or fabricated completion evidence.
