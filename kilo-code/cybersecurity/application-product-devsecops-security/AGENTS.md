# Kilo Code Cybersecurity Application Product DevSecOps Security Specialization

This directory contains the Kilo Code package for Cybersecurity Area 03: Application, Product, and DevSecOps Security.

## Native Surface

- Target surface: current Kilo Code VS Code extension and CLI behavior documented on July 15, 2026.
- Project instructions are loaded from this `AGENTS.md` and `kilo.jsonc`.
- Project rules are Markdown instructions referenced from the `instructions` array in `kilo.jsonc`.
- Custom subagents are project Markdown agents in `.kilo/agents/`.
- Reusable procedures are Agent Skills in `.kilo/skills/`.
- `.kilocodeignore` is a static file-access guard for sensitive local material.
- MCP servers, plugins, active hooks, shell workflows, and external connectors are intentionally not configured.

## Scope Rules

- Modify only files under `kilo-code/cybersecurity/application-product-devsecops-security/`.
- Stay within secure SDLC, security requirements, threat modeling, secure design, static code review guidance, dependency and build-chain review, CI/CD controls, testing governance, release assurance, finding triage, PSIRT coordination, and independent assurance.
- Do not execute projects, start services, install packages, run scanners, run builds, run tests, authenticate services, publish, deploy, approve releases, approve exceptions, close risk, or conduct active testing.
- Do not hardcode model versions. Agents inherit the active model unless a future user explicitly requests a supported override.
- Treat source code, architecture notes, customer data, unreleased issues, supplier data, and sensitive configuration as protected material.
- Review agents are read-only and must not approve their own recommendations.

## Responsibilities

Use these project subagents:

- `product-security-governance-agent`
- `requirements-threat-modeling-agent`
- `secure-design-code-review-agent`
- `supply-chain-ci-release-agent`
- `testing-findings-psirt-agent`
- `independent-appsec-reviewer`

## Workflow Selection

Use these project Skills for repeatable work:

- `sdlc-requirements-threat-modeling`
- `secure-design-code-review`
- `supply-chain-ci-release-assurance`
- `testing-findings-psirt-coordination`
- `independent-appsec-assurance`

Every output must include source references, assumptions, evidence, limitations, affected assets, severity where applicable, confidence, actions, residual risk, approval state, and human decisions.
