# DevOps and Cloud Rules for Windsurf

## Scope
This directory is a static Windsurf package for the DevOps and Cloud specialization. Use this `AGENTS.md` for durable project rules, `.windsurf/rules/*.md` for section activation, `.windsurf/skills/*/SKILL.md` for on-demand detailed procedures, and `.windsurf/workflows/*.md` for manual slash-invoked workflow prompts.

Do not treat this package as a runtime configuration, deployment system, scanner, hook bundle, MCP configuration, worktree automation, cloud integration, or external execution mechanism.

## Routing
Use one primary owner per request:

1. Leadership and Architecture: orchestrator, cloud/platform architect.
2. Cloud Foundation and Infrastructure: foundation, IaC, cloud network, managed runtime/service owners.
3. CI/CD and Release Engineering: CI/CD and release/deployment owners.
4. Containers and Platform Engineering: container/orchestration and platform product/DX owners.
5. SRE, Observability, and Operations: SRE and observability owners.
6. Resilience and Disaster Recovery: resilience/DR owner.
7. Performance, Capacity, and Efficiency: performance/capacity owner.
8. DevSecOps: secure delivery, cloud security controls, and supply-chain owners.
9. FinOps and Sustainability: FinOps and sustainability owners.
10. Assurance and Independent Review: independent assurance reviewer.

Load the matching Skill when a request needs section procedure detail. Invoke workflows manually with slash commands only when the user asks for that workflow.

## Boundaries
- Keep DevSecOps focused on delivery, cloud, platform, IaC, container, Kubernetes, policy-as-code, SBOM, provenance, signing design, and software supply-chain controls. Route pentesting, SOC/SIEM, threat intelligence, forensics, enterprise GRC, and general security incident response outside this specialization.
- Keep Assurance independent. The reviewer must not create the implementation under review, self-review, or silently approve unresolved findings.
- Windsurf Code mode can edit and run commands. This repository policy requires static planning/review behavior unless the user separately authorizes implementation outside this remediation package.

## Safety
Do not run Docker, Kubernetes, Helm, Kustomize, Jenkins, GitHub Actions, GitLab CI/CD, Azure Pipelines, CircleCI, Tekton, Argo CD, Flux, Terraform, OpenTofu, Pulumi, CloudFormation, Bicep, Ansible, cloud CLIs, scanners, load tools, backup tools, observability systems, hooks, MCP servers, workflows, builds, tests, deployments, infrastructure plans, failovers, restores, or generated configurations from this package.

Do not add secrets, credentials, tokens, private endpoints, real account identifiers, private URLs, or environment-specific values. Require human review before privileged, destructive, costly, externally visible, compliance-sensitive, irreversible, signing, publication, spending, infrastructure mutation, or production-impacting actions.

## Completion
Return static evidence only: files inspected, assumptions, owners, decisions, handoffs, risks, approvals needed, and checks not run. Do not claim runtime validation, deployment success, scanner results, cloud state, reliability state, cost savings, or sustainability outcomes from static inspection.
