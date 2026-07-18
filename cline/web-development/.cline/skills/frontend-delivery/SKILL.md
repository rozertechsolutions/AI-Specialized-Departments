---
name: frontend-delivery
description: Plan, implement, or review frontend UI, routes, components, forms, state, data fetching, responsive behavior, and browser behavior.
---

# Frontend Delivery

## Mission
Plan or implement frontend work within the repository’s native stack.

## Use when
- A task changes UI, routes, components, styling, forms, client state, browser behavior, responsive layout, or frontend data fetching.

## Do not use when
- The change is backend-only and has no browser-facing contract or UI impact.

## Inputs
Relevant components, routes, styles, state model, API contracts, design requirements, accessibility criteria, browser targets, and acceptance criteria.

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

## Stop and failure behavior
Return BLOCKED when design requirements, API contracts, browser targets, content, assets, approvals, or source files are missing.

## Review requirements
Cover semantics, state, loading, empty, error, responsive behavior, keyboard/focus behavior, browser compatibility, API contracts, and reviewer handoffs.

## Prohibited actions
- No installation, command execution, Git mutation, deployment, publication, authentication, secret handling, spending, signing, or destructive operation without exact human authorization.
- No unsupported technology assumptions or fabricated completion evidence.
