---
name: frontend-delivery
description: Use for frontend planning, implementation guidance, or review in the project's native web stack, including semantics, state, forms, and responsive behavior.
---

# Frontend Delivery

## Mission
Plan, implement, or review frontend work while preserving the project's existing stack, design system, state model, and browser-support expectations.

## Use When

- The task changes UI, routes, components, styling, forms, client state, browser behavior, responsive layout, or frontend data fetching.
- The user asks for frontend implementation guidance or review.
- A backend/API change needs frontend contract handling.

## Inputs

- Relevant component, route, style, state, API, design, accessibility, browser-support, and acceptance-criteria evidence.

## Procedure

1. Preserve semantic HTML, keyboard access, focus behavior, responsive layout, localization readiness, and browser compatibility.
2. Keep state ownership explicit and avoid duplicating server authority on the client.
3. Handle loading, empty, error, offline or degraded states when relevant.
4. Avoid unreviewed third-party scripts, trackers, and dependencies.
5. Return changed scope, behavior, evidence, limitations, and reviewer handoff.

## Output Contract

- Confirmed frontend scope, affected routes/components, and expected behavior.
- Implementation or review notes covering semantics, state, errors, loading, responsive behavior, accessibility, browser compatibility, and API contracts.
- Tests or manual checks required, with NOT EXECUTED for any check lacking direct evidence.
- Handoff items for security, backend, accessibility, performance, SEO, or release review.

## Stop Conditions

Stop and report BLOCKED when design requirements, API contracts, browser targets, content, assets, approvals, or source files are missing.

## Prohibited Actions

- Do not add dependencies, trackers, third-party scripts, external fonts, or analytics without human review.
- Do not claim rendered, browser, accessibility, or performance validation without direct evidence.
