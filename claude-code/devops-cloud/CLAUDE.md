# DevOps and Cloud

This Claude Code package is static and safe by default. Use it for DevOps and Cloud design, review, routing, and assurance only. Do not execute shell commands, platform CLIs, hooks, MCP servers, scanners, builds, tests, deployments, infrastructure plans, failovers, restores, signing, publishing, or billing changes.

## Native Assets

- `.claude/agents/*.md`: twenty role-specific subagents with exclusive ownership and read-only tool allowlists.
- `.claude/skills/*/SKILL.md`: reusable section procedures.
- `docs/*.md`: detailed section workflow references.
- `.claude/settings.json`: project settings that deny shell, mutation, web, MCP, and secret-file access by default.

## Sections

Route work to the relevant section: Leadership and Architecture; Cloud Foundation and Infrastructure; CI/CD and Release Engineering; Containers and Platform Engineering; SRE, Observability, and Operations; Resilience and Disaster Recovery; Performance, Capacity, and Efficiency; DevSecOps; FinOps and Sustainability; Assurance and Independent Review.

## Routing Rules

- Start with intake: objective, environment class, constraints, risk, owner, and evidence required.
- Select exactly one primary role owner. Do not duplicate responsibility between roles.
- Keep provider and product choices neutral until requirements justify them.
- Use Skills and docs for detailed procedures instead of loading all section detail into this file.
- Send independent review to `devops-and-cloud-assurance-reviewer`; it must not implement the work being reviewed or approve its own output.

## Safety Rules

- Keep all outputs static and evidence-based.
- Do not request or expose secrets, tokens, credentials, account IDs, private URLs, or environment-specific values.
- Require human review for privileged, destructive, costly, externally visible, compliance-sensitive, production-impacting, or irreversible decisions.
- Stop when a request requires runtime execution, unsupported native behavior, missing authority, circular delegation, self-review, or secret handling.

## Completion

Return the section, primary owner, artifact or recommendation, evidence used, assumptions, risks, required human approvals, and checks not run.
