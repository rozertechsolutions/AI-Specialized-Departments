---
name: integrate-mobile-api
description: Plan or implement mobile API integration with typed contracts, error handling, privacy review, and offline behavior.
---

# Integrate Mobile API

## Inputs

- API contract, authentication model, data models, target platform, privacy constraints, caching/offline expectations, and acceptance criteria.

## Preconditions

- Use supplied API contracts only; do not invent endpoints, tokens, schemas, or credentials.
- Separate public mobile client configuration from confidential administrative credentials.
- ChatGPT cannot run repository builds, tests, devices, simulators, signing, or release actions unless a separately enabled native tool supplies verifiable evidence.

## Owner And Reviewers

- Owner: relevant platform engineer; `kmp-engineer` owns shared KMP networking logic.
- Reviewers: `mobile-security-reviewer`, `mobile-test-engineer`, and `mobile-code-reviewer`.

## Steps

1. Validate request/response shape, auth requirements, privacy impact, and error taxonomy.
2. Follow existing networking, serialization, retry, cancellation, and caching patterns.
3. Define loading, empty, error, offline, retry, and recovery behavior.
4. Add tests with deterministic fixtures and no real credentials.
5. Require security and final code review.

## Validation Gates

- Evidence: contract source, secret handling, failure modes, test fixture policy, and manual validation still required.
- Completion: API integration has bounded behavior for success and failure.

## Prohibited Actions

- Do not call real services with credentials, embed secrets, activate connectors, upload data, deploy, publish, or claim network validation without evidence.
