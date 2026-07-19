# DevOps and Cloud for Windsurf

This package provides a static, repository-scoped DevOps and Cloud specialization for Windsurf Cascade. It uses current stable workspace Rules, workspace Skills, workflows, and AGENTS.md instructions.

It does not enable hooks, MCP, worktree setup hooks, cloud execution, external integrations, deployments, scanner runs, command execution, or production operations.

## Native Assets
- `AGENTS.md`: always-on project guidance for identity, routing, safety, and completion.
- `.windsurf/rules/*.md`: workspace Rules with `trigger` frontmatter. Only `00-devops-cloud-routing-safety` is always on; section rules use `model_decision` or `manual`.
- `.windsurf/skills/*/SKILL.md`: workspace Agent Skills with `name` and `description` frontmatter for detailed section procedures.
- `.windsurf/workflows/*.md`: manual-only slash workflow prompts. They are static procedures and are not automatically invoked.

## Department Coverage
1. Leadership and Architecture: request triage, architecture decisions, technology tradeoffs, standards, dependency routing, and Well-Architected review.
2. Cloud Foundation and Infrastructure: AWS, Azure, Google Cloud, hybrid and multicloud foundations; Terraform, OpenTofu, Pulumi, CloudFormation, Bicep, Ansible; networks, managed services, state, drift, and lifecycle design.
3. CI/CD and Release Engineering: Jenkins, GitHub Actions, GitLab CI/CD, Azure Pipelines, CircleCI, Tekton, Argo CD, Flux, artifact promotion, release strategy, rollback, and DORA metrics.
4. Containers and Platform Engineering: Docker, OCI, Docker Compose, Kubernetes, Helm, Kustomize, registries, internal developer platforms, catalogs, portals, and golden paths.
5. SRE, Observability, and Operations: OpenTelemetry, Prometheus, Grafana, Loki, Tempo, Jaeger, Elastic, OpenSearch, SLIs, SLOs, error budgets, alerts, incidents, postmortems, and toil.
6. Resilience and Disaster Recovery: RTO, RPO, backup, restore, disaster recovery, failover, failback, high availability, and controlled chaos-experiment design.
7. Performance, Capacity, and Efficiency: load, stress, endurance, capacity, autoscaling, bottleneck analysis, performance, and resource efficiency.
8. DevSecOps: pipeline security, IAM, secrets, SAST, DAST, SCA, IaC/container/Kubernetes scanning design, policy as code, SBOM, signing, provenance, and software supply-chain controls.
9. FinOps and Sustainability: allocation, budgets, forecasts, anomalies, unit economics, rightsizing, commitments, utilization, and measurable sustainability.
10. Assurance and Independent Review: independent evidence review, cross-section consistency, findings, waivers, and completion gates.

## Safety Model
All outputs are static design, review, or workflow guidance. Human review is required for privileged, destructive, costly, externally visible, compliance-sensitive, irreversible, signing, publication, spending, infrastructure mutation, or production-impacting actions.

No file in this package should contain secrets, credentials, tokens, real endpoints, account identifiers, private URLs, or environment-specific values.
