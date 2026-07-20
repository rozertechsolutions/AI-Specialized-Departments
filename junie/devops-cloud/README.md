# DevOps and Cloud for Junie

This package is a repository-native DevOps and Cloud department for JetBrains Junie. It uses Junie guidelines and Agent Skills to cover DevOps, Cloud, Platform Engineering, SRE, resilience, performance, DevSecOps, FinOps, sustainability, and independent assurance as static guidance.

The package is static and safe by default. The Junie implementation is a repository-native Junie package; it provides platform-appropriate instructions, roles, Skills, rules, workflows, or source files without activating infrastructure, CI/CD systems, cloud access, scanners, billing actions, deployments, or runtime checks.

## Possible Uses

- Designing a cloud target architecture.
- Reviewing landing zones and environment separation.
- Designing or auditing IaC.
- Designing Jenkins, GitHub Actions, GitLab CI/CD, Azure Pipelines, CircleCI, Tekton, Argo CD, or Flux workflows.
- Designing Docker, OCI, Kubernetes, Helm, and Kustomize configurations.
- Creating SLI, SLO, error-budget, alerting, and observability plans.
- Preparing incident, rollback, backup, restore, RTO, RPO, and disaster-recovery plans.
- Reviewing performance, capacity, scaling, and resource efficiency.
- Performing static DevSecOps and software supply-chain reviews.
- Performing FinOps, cost allocation, forecasting, rightsizing, and sustainability analysis.
- Performing independent operational-readiness and assurance reviews.

## Department Coverage

1. Leadership and Architecture.
2. Cloud Foundation and Infrastructure.
3. CI/CD and Release Engineering.
4. Containers and Platform Engineering.
5. SRE, Observability, and Operations.
6. Resilience and Disaster Recovery.
7. Performance, Capacity, and Efficiency.
8. DevSecOps.
9. FinOps and Sustainability.
10. Assurance and Independent Review.

## Native Assets

- `.junie/AGENTS.md`: Junie project guidelines and routing.
- `.junie/skills/*/SKILL.md`: ten Agent Skills.
- `docs/*-workflows.md`: static workflow references used by Skills.
- No custom agent profiles, MCP, hooks, external integrations, or EAP-only configuration is included.

## Installation and Setup

Place `junie/devops-cloud/` contents at the repository root opened in a JetBrains IDE with Junie enabled. Junie can use `.junie/AGENTS.md` or configured project guidelines and can load Agent Skills where the installed Junie version supports them.

This package installs no IDE plugin, model, dependency, provider, or credential.

## Usage

Ask Junie for the relevant section, such as "use Cloud Foundation and Infrastructure to review landing-zone separation." Guidelines route the request; Skills provide detailed procedures; `docs/` files are supporting references.

Request Assurance only after primary work exists. Do not treat Junie's static answer as runtime evidence.

## Safety and Limitations

The default behavior is static-only design, planning, review, and documentation. The package contains no secrets, credentials, account identifiers, private endpoints, production bindings, active integrations, or automatic production changes.

Human approval is required before privileged, destructive, costly, externally visible, compliance-sensitive, production-impacting, signing, spending, publishing, failover, restore, deployment, scanner, or irreversible actions. Static validation means reviewing files and reasoning about artifacts; runtime validation requires separately authorized execution and evidence. This package must not be used as proof of runtime success.

DevSecOps is limited to secure delivery, cloud/platform control design, policy-as-code placement, SBOM, provenance, signing strategy, and software supply-chain controls. Pentesting, SOC/SIEM operations, threat intelligence, forensics, enterprise GRC, general cybersecurity incident response, and offensive security belong to the separate Cybersecurity specialization.

## Removal or Deactivation

Remove `.junie/AGENTS.md`, `.junie/skills/`, and this package's `docs/` files from the target repository, or point Junie project settings to different guidelines.
