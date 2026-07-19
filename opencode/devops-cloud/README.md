# DevOps and Cloud for OpenCode

This package provides a static OpenCode setup for the DevOps and Cloud specialization. It uses current project `AGENTS.md` rules, `opencode.jsonc` configuration, custom primary/subagent definitions, custom commands, and Agent Skills. It does not run commands, mutate repositories through OpenCode, connect to services, deploy, scan, publish, sign, or validate runtime state.

## Package Contents
- `opencode.jsonc`: schema-backed OpenCode configuration with `devops-cloud-orchestrator` as the default primary agent, nineteen specialist subagents, and least-privilege permissions.
- `.opencode/agents/*.md`: twenty role prompts for the professional DevOps and Cloud model.
- `.opencode/skills/*/SKILL.md`: ten on-demand Agent Skills, one per department section.
- `.opencode/commands/*.md`: static workflow commands with native command frontmatter.
- `AGENTS.md`: concise routing, safety, and completion guidance.

## Department Coverage
1. Leadership and Architecture: intake, routing, architecture decisions, standards, target-state design, and Well-Architected review.
2. Cloud Foundation and Infrastructure: AWS, Azure, Google Cloud, hybrid and multicloud, Terraform, OpenTofu, Pulumi, CloudFormation, Bicep, Ansible, landing zones, networking, managed services, lifecycle, and drift.
3. CI/CD and Release Engineering: Jenkins, GitHub Actions, GitLab CI/CD, Azure Pipelines, CircleCI, Tekton, Argo CD, Flux, release strategies, rollback, and delivery evidence.
4. Containers and Platform Engineering: Docker, OCI, Docker Compose, Kubernetes, Helm, Kustomize, registries, internal developer platforms, catalogs, portals, and golden paths.
5. SRE, Observability, and Operations: OpenTelemetry, Prometheus, Grafana, Loki, Tempo, Jaeger, Elastic, OpenSearch, SLIs, SLOs, error budgets, alerts, incidents, postmortems, and toil.
6. Resilience and Disaster Recovery: backup, restore, RTO, RPO, high availability, failover, failback, disaster recovery, and controlled chaos-experiment design.
7. Performance, Capacity, and Efficiency: load, stress, endurance, capacity, autoscaling, bottleneck analysis, and technical resource efficiency.
8. DevSecOps: pipeline security, IAM, secrets, SAST, DAST, SCA, IaC/container/Kubernetes scanning design, policy as code, SBOM, signing, provenance, and supply-chain controls.
9. FinOps and Sustainability: allocation, budgets, forecasts, anomalies, unit economics, rightsizing, commitments, utilization, and measurable sustainability.
10. Assurance and Independent Review: independent evidence review, findings, waivers, cross-section consistency, and completion gates.

## Safety Model
The configuration denies `edit`, `bash`, `webfetch`, `websearch`, and external-directory access by default. It allows read/search/list operations, Skill loading, and orchestrator task delegation so the primary agent can reach specialist subagents without granting mutation or shell access. Assurance is read-only and cannot delegate further.

Plugins, MCP servers, hooks, custom tools, external integrations, scheduled work, deployments, signing, publishing, and spending are absent. Static review must not be described as runtime validation.
