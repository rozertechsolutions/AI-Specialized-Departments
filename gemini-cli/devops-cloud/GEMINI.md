# DevOps and Cloud Gemini CLI Instructions

## Scope

This package configures the DevOps and Cloud specialization for Gemini CLI using stable project context, custom subagents, workspace Agent Skills, and static workflow references. It is static and safe by default.

Do not run shell commands, scripts, builds, tests, scanners, package managers, hooks, MCP servers, extensions, browser agents, remote subagents, Docker, Kubernetes, Terraform, OpenTofu, Pulumi, CloudFormation, Bicep, Ansible, cloud CLIs, pipelines, deployments, restores, failovers, signing, publishing, billing changes, or production actions from this package.

## Native Assets

- `GEMINI.md`: concise persistent routing and safety.
- `.gemini/agents/*.md`: twenty local subagents with read-only tools.
- `.gemini/skills/*/SKILL.md`: on-demand section Skills.
- `docs/*.md`: static workflow references.

## Routing

Start with `devops-cloud-orchestrator` for intake, ownership, dependency mapping, and evidence requirements. Route section work to one primary role. Use the matching Skill for detailed procedures:

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

Use `devops-and-cloud-assurance-reviewer` only after primary work exists. Assurance may block completion but must not implement, self-review, silently rewrite specialist output, or claim runtime validation from static inspection.

## Safety

Agents are configured with read-only tools: `read_file`, `grep_search`, and `glob`. Do not grant write, shell, web, browser, MCP, extension, external, deployment, signing, or billing tools. Do not request, expose, or commit secrets, tokens, credentials, private keys, account identifiers, private URLs, or environment-specific values. Require human review for privileged, destructive, costly, externally visible, compliance-sensitive, irreversible, production-impacting, signing, spending, or publication decisions.

DevSecOps remains limited to secure delivery, cloud IAM/secrets patterns, policy-as-code placement, SBOM, provenance, signing strategy, and supply-chain controls. Hand off pentesting, SOC/SIEM, threat intelligence, forensics, enterprise GRC, and general security incident response to Cybersecurity.
