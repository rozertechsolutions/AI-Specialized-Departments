# DevOps and Cloud for Junie

This package provides a static, stable Junie configuration for the complete DevOps and Cloud specialization. It uses project guidelines plus Agent Skills to keep persistent context small while preserving the ten department sections and twenty-role responsibility model.

## Native Assets
- `.junie/AGENTS.md`: persistent project guidance for routing, safety, native asset discovery, assurance independence, and completion.
- `.junie/skills/*/SKILL.md`: on-demand Skill instructions for each department section.
- `docs/*-workflows.md`: static workflow references linked from the Skills.

## Department Coverage
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

## Operating Model
Junie receives concise persistent guidance from `.junie/AGENTS.md`. Detailed professional procedures live in the matching Skill and workflow files. Each request should be routed to one primary section owner, with dependencies recorded explicitly when another section must contribute evidence.

The package represents the full role model through stable Junie guidelines, Skills, and workflow references. It intentionally does not create custom subagent files, extensions, MCP configuration, hooks, or external integrations because those mechanisms are not required for this stable repository package.

## Safety Model
All outputs are static recommendations, designs, reviews, or checklists. The package does not run platform tooling, authenticate to services, deploy infrastructure, mutate cloud state, scan systems, sign artifacts, publish releases, spend money, or validate runtime state.

Human review is required before privileged, destructive, costly, externally visible, compliance-sensitive, or irreversible actions. Secrets, credentials, tokens, private keys, account identifiers, private endpoints, and private URLs must not be stored in this package.

## Assurance
The Assurance and Independent Review Skill is non-implementing. It reviews evidence, checks cross-section consistency, identifies blockers, and enforces completion gates without approving its own work or replacing specialist owners.
