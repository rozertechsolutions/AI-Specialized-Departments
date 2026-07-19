# DevOps and Cloud for Mistral Vibe

This package provides a static, project-scoped Mistral Vibe setup for the DevOps and Cloud specialization. It uses current Vibe custom agents, prompt references, Skills, and local documentation only. It does not execute tools, connect to services, run infrastructure workflows, deploy, scan, publish, sign, or validate live runtime state.

## Package Contents
- `.vibe/config.toml`: selects `devops-cloud-orchestrator` as the default user-facing agent.
- `.vibe/agents/*.toml`: one selectable orchestrator plus nineteen delegation-only specialist agents. Each profile enables only read-oriented tools and explicitly disables shell and mutation tools.
- `.vibe/prompts/*.md`: detailed role instructions for the complete twenty-role DevOps and Cloud model.
- `.vibe/skills/*/SKILL.md`: reusable procedures for the ten department sections.
- `docs/*.md`: static workflow references for architecture, cloud foundation, delivery, platform engineering, reliability, resilience, performance, DevSecOps, FinOps, sustainability, and assurance.
- `AGENTS.md`: concise project routing, safety, and completion instructions.

## Department Coverage
1. Leadership and Architecture: intake, routing, architecture decisions, standards, target-state design, and Well-Architected review.
2. Cloud Foundation and Infrastructure: AWS, Azure, Google Cloud, hybrid and multicloud foundations, IaC, networking, managed services, lifecycle, drift, and decommissioning.
3. CI/CD and Release Engineering: Jenkins, GitHub Actions, GitLab CI/CD, Azure Pipelines, CircleCI, Tekton, promotion, release evidence, rollback, and deployment strategy design.
4. Containers and Platform Engineering: Docker, OCI, Docker Compose, Kubernetes, Helm, Kustomize, registries, internal developer platforms, catalogs, portals, and golden paths.
5. SRE, Observability, and Operations: OpenTelemetry, Prometheus, Grafana, Loki, Tempo, Jaeger, Elastic, OpenSearch, SLIs, SLOs, error budgets, alerts, incidents, postmortems, and toil reduction.
6. Resilience and Disaster Recovery: backup, restore, RTO, RPO, high availability, failover, failback, disaster recovery, and controlled chaos-experiment design.
7. Performance, Capacity, and Efficiency: load, stress, endurance, capacity, autoscaling, performance diagnosis, and technical resource efficiency.
8. DevSecOps: secure delivery, IAM and secrets controls, SAST, DAST, SCA, IaC/container/Kubernetes scanning design, policy as code, SBOM, signing, provenance, and supply-chain controls.
9. FinOps and Sustainability: allocation, budgets, forecasts, anomalies, unit economics, rightsizing, commitments, utilization, and measurable sustainability.
10. Assurance and Independent Review: independent review, evidence checks, cross-section consistency, waiver scrutiny, and completion gating.

## Safety Model
The Vibe `safety` labels are descriptive. Read-only behavior is enforced through the agent tool lists and per-tool permission denials. Shell execution, write tools, search/replace mutation, MCP, connectors, hooks, plugins, external integrations, schedules, deployments, and production actions are absent or disabled by default.

Human review is required before privileged, destructive, costly, externally visible, compliance-sensitive, irreversible, production-affecting, or security-sensitive action. Static guidance must not be presented as proof that a live platform, pipeline, cluster, cloud account, backup, failover, scanner, or deployment succeeded.

## Use
Select the default `devops-cloud-orchestrator` for intake and routing. Delegate to specialist agents only for their owned sections and use the matching Skills or workflow docs for detailed procedures. Use `devops-and-cloud-assurance-reviewer` only for independent review after implementation or planning work is complete.
