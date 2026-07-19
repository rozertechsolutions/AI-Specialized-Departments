# DevOps and Cloud for Claude

This is a manual/import package for Claude Projects, project instructions, project knowledge, and Claude Skills where available. It is intentionally separate from Claude Code and contains no `.claude/` subagents, hooks, MCP configuration, shell permissions, or repository runtime automation.

## Native Surfaces

- `project/project-instructions.md`: concise Project-level routing, safety, and completion guidance.
- `project/knowledge/*.md`: detailed knowledge for all ten DevOps and Cloud sections.
- `skills/*/SKILL.md`: on-demand Skill procedures for workspaces that support Claude Skills.

Connectors and remote MCP are intentionally absent. Current Claude custom connectors are configured in the Claude UI and require explicit user or organization setup; this package does not enable them.

## Sections Covered

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

## Setup

Create or open a Claude Project in the Claude UI, add `project/project-instructions.md` as Project instructions, and upload the relevant knowledge and Skill files according to the active plan and workspace capabilities. Claude Projects provide project instructions and project knowledge; enhanced knowledge capacity and collaboration depend on plan and workspace settings.

Do not copy this package into Claude Code. Claude Code has a separate package under `claude-code/devops-cloud/`.

## Safety

All outputs are static design, review, planning, or advisory artifacts. Do not use this package to execute builds, tests, scans, deployments, failovers, restores, infrastructure plans, signing, publishing, billing changes, cloud actions, or production operations. Human review is required for privileged, destructive, costly, externally visible, compliance-sensitive, or irreversible decisions.
