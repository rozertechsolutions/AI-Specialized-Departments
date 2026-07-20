# DevOps and Cloud for Local Provider-Neutral Specification

This package is a provider-neutral DevOps and Cloud department specification for users who want to implement their own runtime outside the repository. It covers DevOps, Cloud, Platform Engineering, SRE, resilience, performance, DevSecOps, FinOps, sustainability, and independent assurance while remaining model-neutral, endpoint-neutral, tool-neutral, and disabled by default.

The package is static and safe by default. The Local Provider-Neutral Specification implementation is a provider-neutral local specification; it provides platform-appropriate instructions, roles, Skills, rules, workflows, or source files without activating infrastructure, CI/CD systems, cloud access, scanners, billing actions, deployments, or runtime checks.

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

- `spec/department.yaml`: department metadata, sections, routing, and global boundaries.
- `spec/roles/*.yaml`: twenty role definitions.
- `spec/skills/*.yaml`: ten section procedures.
- `spec/workflows/*.yaml`: static workflow definitions.
- `spec/policies/*.yaml`: safety and quality-gate policies.
- No provider binding, endpoint, model, tool adapter, MCP server, credential, or executable runtime is included.

## Installation and Setup

Copy or reference `local/devops-cloud/spec/` from your own implementation outside this repository. Select your provider, model, runtime, tools, storage, permissions, and authentication separately, and keep them disabled until explicitly configured and reviewed.

Do not add real endpoints, account identifiers, credentials, cloud projects, subscriptions, or provider-specific defaults to this package.

## Usage

Use `spec/department.yaml` for routing, select one role from `spec/roles/`, and apply the relevant section procedure from `spec/skills/` or `spec/workflows/`. Ask for one section by name, such as "Cloud Foundation and Infrastructure," and map that request to your own runtime outside this repository.

Run Assurance only after primary output exists. The YAML specification is advisory and does not execute or validate anything by itself.

## Safety and Limitations

The default behavior is static-only design, planning, review, and documentation. The package contains no secrets, credentials, account identifiers, private endpoints, production bindings, active integrations, or automatic production changes.

Human approval is required before privileged, destructive, costly, externally visible, compliance-sensitive, production-impacting, signing, spending, publishing, failover, restore, deployment, scanner, or irreversible actions. Static validation means reviewing files and reasoning about artifacts; runtime validation requires separately authorized execution and evidence. This package must not be used as proof of runtime success.

DevSecOps is limited to secure delivery, cloud/platform control design, policy-as-code placement, SBOM, provenance, signing strategy, and software supply-chain controls. Pentesting, SOC/SIEM operations, threat intelligence, forensics, enterprise GRC, general cybersecurity incident response, and offensive security belong to the separate Cybersecurity specialization.

## Removal or Deactivation

Remove `local/devops-cloud/spec/` from the consuming project or stop referencing it in your external runtime. No repository-local provider state is created by this package.
