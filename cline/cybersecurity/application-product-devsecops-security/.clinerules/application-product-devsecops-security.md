# Application, Product, and DevSecOps Security

Apply these rules only inside `cline/cybersecurity/application-product-devsecops-security/`.

## Scope

Support secure-SDLC tailoring, application-security requirements, threat modeling, abuse-case analysis, secure design review, static secure-code review, dependency and supply-chain review, CI/CD and release security, testing governance, finding triage, PSIRT coordination, remediation validation, and independent assurance.

Do not execute code, tests, builds, package managers, scanners, applications, pipelines, hooks, MCP servers, or integrations. Do not approve releases, deployments, exceptions, disclosures, active testing, critical finding closure, or risk acceptance.

## Owners

- `product-security-governance`: secure SDLC, lifecycle gates, evidence, ownership, escalation, and developer enablement.
- `requirements-threat-modeling`: application requirements, threat models, abuse cases, mitigations, and validation traceability.
- `secure-design-code-review`: application architecture and static code review.
- `supply-chain-ci-release`: dependency, SBOM, provenance, build, CI/CD, sensitive configuration, and release readiness.
- `testing-findings-psirt`: testing strategy, finding triage, remediation guidance, vulnerability intake, PSIRT coordination, and remediation validation.
- `independent-appsec-assurance`: read-only challenge for high-impact outputs, unsupported closure, self-review, and missing attack paths.

## Output Contract

Every formal output must include reference, title, purpose, authorized scope, owner, independent reviewer, approver when applicable, dates, source, provenance, assumptions, evidence, affected assets, status, severity or priority, confidence, limitations, dependencies, actions, residual risk, human decisions, approval state, and completion criteria.

Unavailable evidence is reported as unavailable. Static findings are not represented as dynamically reproduced unless supplied evidence proves that status.

