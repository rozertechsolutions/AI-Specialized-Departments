# DevOps and Cloud Rules for Warp

## Scope
This directory is a static Warp project package for the DevOps and Cloud specialization. Use Warp project Rules from this `AGENTS.md` file for durable routing and safety, and use project Skills in `.agents/skills/` for detailed section procedures.

Do not treat this repository as a deployment, scanning, cloud-agent, schedule, trigger, integration, MCP, or runtime-automation package. Warp profile permissions are user or account scoped and are not configured by repository files here.

## Routing
Route work to one primary owner and load the matching Skill when detail is needed:

1. Leadership and Architecture: `.agents/skills/leadership-architecture/SKILL.md`
2. Cloud Foundation and Infrastructure: `.agents/skills/cloud-foundation-infrastructure/SKILL.md`
3. CI/CD and Release Engineering: `.agents/skills/ci-cd-release-engineering/SKILL.md`
4. Containers and Platform Engineering: `.agents/skills/containers-platform-engineering/SKILL.md`
5. SRE, Observability, and Operations: `.agents/skills/sre-observability-operations/SKILL.md`
6. Resilience and Disaster Recovery: `.agents/skills/resilience-disaster-recovery/SKILL.md`
7. Performance, Capacity, and Efficiency: `.agents/skills/performance-capacity-efficiency/SKILL.md`
8. DevSecOps: `.agents/skills/devsecops/SKILL.md`
9. FinOps and Sustainability: `.agents/skills/finops-sustainability/SKILL.md`
10. Assurance and Independent Review: `.agents/skills/assurance-review/SKILL.md`

Supporting static workflow references live in `docs/` and are referenced by the corresponding Skill names.

## Professional Boundaries
- Preserve the twenty-role responsibility model through the ten Skills and workflow references; do not create repository-native Warp agent profiles or permission files for those roles.
- Keep one primary owner per responsibility and avoid circular handoffs.
- Keep DevSecOps limited to delivery, cloud, platform, IaC, container, Kubernetes, policy-as-code, SBOM, provenance, signing design, and software supply-chain controls. Do not absorb pentesting, SOC/SIEM operations, threat intelligence, forensics, enterprise GRC, or general security incident response.
- Keep Assurance independent. The Assurance reviewer must not implement the subject under review, self-review, or silently approve unresolved findings.

## Safety
- Work from repository-local files and user-provided context only unless the user explicitly authorizes current official documentation lookup.
- Do not run Docker, Kubernetes, Helm, Kustomize, Jenkins, GitHub Actions, GitLab CI/CD, Azure Pipelines, CircleCI, Tekton, Argo CD, Flux, Terraform, OpenTofu, Pulumi, CloudFormation, Bicep, Ansible, cloud CLIs, scanners, load tools, backup tools, observability systems, hooks, MCP servers, builds, tests, deployments, infrastructure plans, failovers, restores, or generated configurations from this package.
- Do not add secrets, credentials, tokens, private endpoints, real account identifiers, private URLs, or environment-specific values.
- Do not enable Warp cloud agents, Oz execution, schedules, environments, triggers, integrations, MCP, connectors, plugins, or external execution by default.
- Require human review before privileged, destructive, costly, externally visible, compliance-sensitive, irreversible, signing, publication, spending, infrastructure mutation, or production-impacting actions.

## Completion
Return static evidence only: files inspected, assumptions, decisions, risks, owners, handoffs, approvals needed, and checks not run. Never claim runtime validation, deployment success, scanner results, cloud state, reliability state, cost savings, or sustainability outcomes from static inspection.
