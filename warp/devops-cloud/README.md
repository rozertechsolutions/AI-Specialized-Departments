# DevOps and Cloud for Warp

This package provides a static, repository-scoped DevOps and Cloud specialization for Warp. It uses the current stable Warp project Rules surface (`AGENTS.md`) and project Agent Skills in `.agents/skills/`.

It does not configure Warp agent profiles, file permissions, MCP servers, integrations, cloud agents, Oz runs, schedules, triggers, environments, or external execution. Those controls remain user/account scoped or intentionally absent.

## Native Assets
- `AGENTS.md`: concise project Rules for routing, safety, human review, and Skill discovery.
- `.agents/skills/*/SKILL.md`: ten focused project Skills with YAML frontmatter (`name` and `description`) and static professional procedures.
- `docs/*-workflows.md`: supporting workflow references for the matching Skills.

## Department Coverage
1. Leadership and Architecture: request triage, architecture decisions, standards, technology tradeoffs, dependency routing, and Well-Architected review.
2. Cloud Foundation and Infrastructure: AWS, Azure, Google Cloud, hybrid and multicloud foundations; Terraform, OpenTofu, Pulumi, CloudFormation, Bicep, Ansible; networks, managed services, state, drift, and lifecycle design.
3. CI/CD and Release Engineering: Jenkins, GitHub Actions, GitLab CI/CD, Azure Pipelines, CircleCI, Tekton, Argo CD, Flux, artifact promotion, release strategy, rollback, and DORA metrics.
4. Containers and Platform Engineering: Docker, OCI, Docker Compose, Kubernetes, Helm, Kustomize, registries, internal developer platforms, catalogs, portals, and golden paths.
5. SRE, Observability, and Operations: OpenTelemetry, Prometheus, Grafana, Loki, Tempo, Jaeger, Elastic, OpenSearch, SLIs, SLOs, error budgets, alerts, incidents, postmortems, and toil.
6. Resilience and Disaster Recovery: RTO, RPO, backup, restore, disaster recovery, failover, failback, high availability, and controlled chaos-experiment design.
7. Performance, Capacity, and Efficiency: load, stress, endurance, capacity, autoscaling, bottleneck analysis, performance, and resource efficiency.
8. DevSecOps: pipeline security, IAM, secrets, SAST, DAST, SCA, IaC/container/Kubernetes scanning design, policy as code, SBOM, signing, provenance, and software supply-chain controls.
9. FinOps and Sustainability: allocation, budgets, forecasts, anomalies, unit economics, rightsizing, commitments, utilization, and measurable sustainability.
10. Assurance and Independent Review: independent evidence review, cross-section consistency, findings, waivers, and completion gates.

## Operating Model
Warp automatically applies `AGENTS.md` project Rules when working in this directory. Skills are discovered from `.agents/skills/` and can be invoked by natural language or slash command. Long procedures live in Skills and workflow references so persistent Rules stay concise.

Every task must have one primary owner, explicit assumptions, clear handoffs, stop conditions, and human-review boundaries. Assurance remains independent and must not review its own implementation.

## Safety Model
All outputs are static guidance, design, or review artifacts. Do not run platform CLIs, builds, tests, scanners, IaC plans, deployments, failovers, restores, hooks, MCP servers, cloud agents, schedules, triggers, or integrations from this package.

No secrets, credentials, real endpoints, account identifiers, private URLs, or environment-specific values belong in this package. Human review is required for privileged, destructive, costly, externally visible, compliance-sensitive, irreversible, signing, publication, spending, infrastructure mutation, or production-impacting actions.
