# DevOps and Cloud for Qwen Code

This package provides a static Qwen Code setup for the DevOps and Cloud specialization. It uses current project subagents, Agent Skills, Markdown command workflows, and persistent `QWEN.md` instructions only. It does not execute commands, mutate files, connect to services, deploy, scan, publish, sign, spend money, or validate runtime state.

## Package Contents
- `.qwen/agents/*.md`: twenty subagent profiles with YAML-list tool allowlists, `approvalMode: plan`, and explicit mutation/shell disallow rules.
- `.qwen/skills/*/SKILL.md`: ten stable Agent Skills for on-demand department procedures.
- `.qwen/commands/*.md`: Markdown command workflows for static procedures.
- `QWEN.md`: concise routing, safety, native asset discovery, parent-mode warning, and completion guidance.

## Department Coverage
1. Leadership and Architecture: intake, routing, architecture decisions, standards, target-state design, and Well-Architected review.
2. Cloud Foundation and Infrastructure: AWS, Azure, Google Cloud, hybrid and multicloud, Terraform, OpenTofu, Pulumi, CloudFormation, Bicep, Ansible, landing zones, networking, managed services, lifecycle, and drift.
3. CI/CD and Release Engineering: Jenkins, GitHub Actions, GitLab CI/CD, Azure Pipelines, CircleCI, Tekton, Argo CD, Flux, release strategy, rollback, and evidence.
4. Containers and Platform Engineering: Docker, OCI, Docker Compose, Kubernetes, Helm, Kustomize, registries, internal developer platforms, catalogs, portals, and golden paths.
5. SRE, Observability, and Operations: OpenTelemetry, Prometheus, Grafana, Loki, Tempo, Jaeger, Elastic, OpenSearch, SLIs, SLOs, error budgets, alerts, incidents, postmortems, and toil.
6. Resilience and Disaster Recovery: backup, restore, RTO, RPO, disaster recovery, high availability, failover, failback, and controlled chaos-experiment design.
7. Performance, Capacity, and Efficiency: load, stress, endurance, capacity, autoscaling, performance analysis, and resource efficiency.
8. DevSecOps: pipeline security, IAM, secrets, SAST, DAST, SCA, IaC/container/Kubernetes scanning design, policy as code, SBOM, signing, provenance, and supply-chain controls.
9. FinOps and Sustainability: allocation, budgets, forecasts, anomalies, unit economics, rightsizing, commitments, utilization, and measurable sustainability.
10. Assurance and Independent Review: independent evidence review, findings, waivers, cross-section consistency, and completion gates.

## Safety Model
Each subagent is configured for plan/read-only work with `read_file`, `grep_search`, and `glob` only. `write_file`, `edit`, and `run_shell_command` are explicitly disallowed. Because permissive parent approval modes can override subagent mode, this package must be used only under a plan/read-only parent policy.

MCP, hooks, extensions, scheduled tasks, channels, external integrations, shell execution, file mutation, deployments, signing, publishing, and spending are absent. Static review must not be described as runtime validation.
