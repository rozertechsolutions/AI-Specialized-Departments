# DevOps and Cloud for OpenAI Agents SDK

This package is a static source package for the OpenAI Agents SDK. It defines the complete DevOps and Cloud specialization as SDK `Agent` objects, typed role metadata, deterministic guardrails, reusable knowledge constants, and source-level tests. It is not installed, served, deployed, or executed by this repository work.

## Package Contents
- `src/devops_cloud_department/models.py`: authoritative typed role registry for all twenty roles, including section ownership, exclusive mission, review status, and delegation boundaries.
- `src/devops_cloud_department/agents.py`: exactly twenty SDK `Agent` objects, the entry agent, non-circular handoff graph, and deterministic input/output guardrails.
- `src/devops_cloud_department/*_*.py`: role instructions, Skills, workflows, and quality gates for each department section.
- `tests/test_static_contracts.py`: source-level contracts for role completeness, construction, reachability, no cycles, no self-review, Assurance independence, and guardrail attachment.
- `pyproject.toml`: package metadata for the static SDK package.

## Department Coverage
1. Leadership and Architecture: orchestration, routing, architecture decisions, standards, target-state design, and Well-Architected review.
2. Cloud Foundation and Infrastructure: AWS, Azure, Google Cloud, hybrid, multicloud, Terraform, OpenTofu, Pulumi, CloudFormation, Bicep, Ansible, landing zones, networking, managed services, lifecycle, and drift.
3. CI/CD and Release Engineering: Jenkins, GitHub Actions, GitLab CI/CD, Azure Pipelines, CircleCI, Tekton, release strategy, promotion, rollback, and evidence.
4. Containers and Platform Engineering: Docker, OCI, Docker Compose, Kubernetes, Helm, Kustomize, registries, internal developer platforms, catalogs, portals, and golden paths.
5. SRE, Observability, and Operations: OpenTelemetry, Prometheus, Grafana, Loki, Tempo, Jaeger, Elastic, OpenSearch, SLIs, SLOs, error budgets, alerts, incidents, postmortems, and toil.
6. Resilience and Disaster Recovery: backup, restore, RTO, RPO, disaster recovery, failover, failback, high availability, and controlled chaos-experiment design.
7. Performance, Capacity, and Efficiency: load, stress, endurance, capacity, autoscaling, performance analysis, and resource efficiency.
8. DevSecOps: pipeline security, IAM, secrets, SAST, DAST, SCA, IaC/container/Kubernetes scanning design, policy as code, SBOM, signing, provenance, and supply-chain controls.
9. FinOps and Sustainability: allocation, budgets, forecasts, anomalies, unit economics, rightsizing, commitments, utilization, and measurable sustainability.
10. Assurance and Independent Review: independent evidence review, findings, waivers, cross-section consistency, and completion gates.

## Safety Model
Agents are constructed with no shell, computer, code-interpreter, hosted MCP, file-mutation, deployment, external, or custom function tools. The package attaches deterministic SDK input and output guardrails that trip on secret material, real deployment or infrastructure mutation requests, destructive or privileged action patterns, spending, signing, publication, and unsupported runtime-success claims.

The DevOps and Cloud Assurance Reviewer is a non-implementing independent reviewer. It can be reached from the entry agent for review but has no outgoing handoffs and must not create or approve the primary implementation under review.

## Static Verification
The tests are authored as source contracts and are not executed as part of this package remediation. Static source inspection is the only validation claimed here.
