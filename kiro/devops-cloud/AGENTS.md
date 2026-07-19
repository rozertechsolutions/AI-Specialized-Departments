# DevOps and Cloud Kiro Workspace Instructions

## Scope
This package targets Kiro IDE only. Use root `AGENTS.md`, `.kiro/steering/`, `.kiro/agents/`, and `.kiro/skills/` as stable workspace assets.

Do not use Kiro CLI JSON-agent schemas, hooks, powers, MCP servers, shell access, web access, external integrations, specs that execute work, deployment automation, signing, publication, spending, failover, restore, scanners, cloud CLIs, Docker, Kubernetes, Terraform, OpenTofu, Pulumi, CloudFormation, Bicep, Ansible, CI/CD systems, or runtime validation from this package.

## Routing
Start with the `devops-cloud-orchestrator` agent for intake and routing. Use one primary section owner:
1. Leadership and Architecture
2. Cloud Foundation and Infrastructure
3. CI/CD and Release Engineering
4. Containers and Platform Engineering
5. SRE, Observability, and Operations
6. Resilience and Disaster Recovery
7. Performance, Capacity, and Efficiency
8. DevSecOps
9. FinOps and Sustainability
10. Assurance and Independent Review

Use `.kiro/skills/*/SKILL.md` for detailed procedures. Use `.kiro/agents/*.md` for role-specific review and recommendations. Steering files are concise routing hints, not complete procedure copies.

## Safety
Agents are read-only by default and include `includeMcpJson: false`. Do not access secrets, tokens, private keys, credentials, account identifiers, private endpoints, private URLs, or unrelated personal information.

Human review is required for privileged, destructive, costly, externally visible, compliance-sensitive, or irreversible actions.

## Assurance
The Assurance Reviewer is independent and non-implementing. It may review evidence and block completion, but it must not create the reviewed implementation, self-review, approve its own output, or close findings without evidence or a human waiver.
