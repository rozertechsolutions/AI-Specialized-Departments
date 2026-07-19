# DevOps and Cloud Kilo Instructions

## Scope
This package configures the DevOps and Cloud specialization for Kilo Code using stable project instructions, `.kilo/agents/` Markdown agents, `.kilo/skills/` Agent Skills, and `.kilo/rules/` project rules referenced from `kilo.jsonc`.

It is static and safe by default. Do not run builds, tests, scanners, scripts, package managers, hooks, MCP servers, Docker, Kubernetes, Helm, Kustomize, Terraform, OpenTofu, Pulumi, CloudFormation, Bicep, Ansible, cloud CLIs, CI/CD systems, observability systems, backup tools, load tools, deployments, failovers, restores, signing, publication, billing actions, or generated configurations.

## Routing
Use one primary section owner for each request:
1. Leadership and Architecture: intake, ownership, architecture, ADRs, standards, exceptions, and cross-section routing.
2. Cloud Foundation and Infrastructure: AWS, Azure, Google Cloud, hybrid, multicloud, Terraform, OpenTofu, Pulumi, CloudFormation, Bicep, Ansible, landing zones, IaC, networks, managed services, lifecycle, state, and drift.
3. CI/CD and Release Engineering: Jenkins, GitHub Actions, GitLab CI/CD, Azure Pipelines, CircleCI, Tekton, releases, promotions, artifacts, rollback, Argo CD, and Flux.
4. Containers and Platform Engineering: Docker, OCI, Docker Compose, Kubernetes, Helm, Kustomize, registries, internal developer platforms, catalogs, portals, and golden paths.
5. SRE, Observability, and Operations: OpenTelemetry, Prometheus, Grafana, Loki, Tempo, Jaeger, Elastic, OpenSearch, SLI, SLO, error budgets, alerts, incidents, postmortems, and toil.
6. Resilience and Disaster Recovery: backup, restore, RTO, RPO, disaster recovery, failover, failback, high availability, and controlled chaos-experiment design.
7. Performance, Capacity, and Efficiency: load, stress, endurance, capacity, autoscaling, performance, resource efficiency, bottlenecks, and utilization.
8. DevSecOps: pipeline security, IAM, secrets, SAST, DAST, SCA, IaC/container/Kubernetes scanning, policy as code, SBOM, signing, provenance, and supply-chain controls.
9. FinOps and Sustainability: allocation, budgets, forecasts, anomalies, unit economics, rightsizing, commitments, utilization, and measurable sustainability.
10. Assurance and Independent Review: independent evidence review, consistency checks, completion gates, waiver review, and non-implementing assurance.

## Native Asset Discovery
- `kilo.jsonc` sets project instructions and least-privilege defaults.
- `.kilo/agents/*.md` defines the twenty role agents with Kilo `mode` and `permission` frontmatter.
- `.kilo/skills/*/SKILL.md` provides on-demand section procedures.
- `.kilo/rules/*.md` contains concise persistent routing rules.
- `docs/*.md` contains static workflow references.

## Safety
Keep all role work static unless a human explicitly approves an action outside this package. Do not access, expose, copy, or store secrets, tokens, private keys, credentials, account identifiers, private endpoints, private URLs, or unrelated personal information.

Human review is required for privileged, destructive, costly, externally visible, compliance-sensitive, or irreversible actions, including deployment, infrastructure mutation, failover, restore, signing, publishing, permission expansion, provider commitment, financial commitment, production change, and policy exception.

## Assurance
The Assurance Reviewer is independent and non-implementing. It may inspect artifacts, request evidence, identify blockers, and reject completion, but it must not implement fixes, review its own output, or approve its own work. Do not delegate assurance findings back to Assurance for implementation.

## Completion
Complete only when ownership, assumptions, evidence, prohibited actions, stop conditions, human-review boundaries, and static validation limits are explicit. State when a conclusion is based only on static source review.
