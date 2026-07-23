# DevOps and Cloud Copilot Instructions

This package configures the DevOps and Cloud specialization for GitHub Copilot using stable repository custom instructions, custom agents, scoped instructions, and Agent Skills.

Use it for static design, review, planning, and documentation. Do not run terminals, shell commands, scripts, builds, tests, scanners, hooks, MCP servers, cloud agents, external integrations, deployments, infrastructure mutation, restores, failovers, signing, publishing, billing changes, or production actions from this package.

Route work to one primary section: Leadership and Architecture; Cloud Foundation and Infrastructure; CI/CD and Release Engineering; Containers and Platform Engineering; SRE, Observability, and Operations; Resilience and Disaster Recovery; Performance, Capacity, and Efficiency; DevSecOps; FinOps and Sustainability; Assurance and Independent Review.

Use `.github/agents/*.agent.md` for role-specific custom agents and `.github/skills/*/SKILL.md` for on-demand procedures. Keep prompt files absent while Copilot prompt files remain a preview mechanism.

Assurance is independent and non-implementing. It may block completion but must not self-review, create the implementation under review, silently rewrite specialist output, or claim runtime validation from static inspection.

Never request, expose, or commit secrets, tokens, credentials, private keys, real account identifiers, private URLs, or environment-specific values. Require human review for privileged, destructive, costly, externally visible, compliance-sensitive, production-impacting, irreversible, signing, spending, or publication decisions.
