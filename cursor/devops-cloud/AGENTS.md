# DevOps and Cloud Cursor Instructions

## Scope

This package configures the DevOps and Cloud specialization for Cursor using stable project instructions, Cursor Project Rules, Agent Skills, and static workflow references. It is static and safe by default.

Do not run terminals, scripts, builds, tests, scanners, package managers, hooks, MCP servers, cloud agents, external integrations, Docker, Kubernetes, Terraform, OpenTofu, Pulumi, CloudFormation, Bicep, Ansible, cloud CLIs, pipelines, deployments, restores, failovers, signing, publishing, billing changes, or production actions from this package.

## Native Asset Discovery

- `AGENTS.md`: concise persistent routing and safety.
- `.cursor/rules/*.mdc`: Cursor Project Rules with explicit activation frontmatter.
- `.cursor/skills/*/SKILL.md`: on-demand section Skills.
- `docs/*-workflows.md`: static workflow references used by section Skills.

## Sections

Route each request to one primary section: Leadership and Architecture; Cloud Foundation and Infrastructure; CI/CD and Release Engineering; Containers and Platform Engineering; SRE, Observability, and Operations; Resilience and Disaster Recovery; Performance, Capacity, and Efficiency; DevSecOps; FinOps and Sustainability; Assurance and Independent Review.

Use the section Skill for detailed workflow steps. Use Project Rules for durable boundaries and activation. Do not treat repository files as automatic permission grants.

## Role and Review Boundaries

Preserve the twenty-role responsibility model through section rules and Skills. Assign exactly one primary owner per responsibility. Use Assurance only after primary work exists; Assurance may block completion but must not create the implementation under review, self-review, silently rewrite specialist output, or close findings without evidence or human waiver.

DevSecOps covers secure delivery controls, cloud IAM/secrets patterns, policy-as-code placement, SBOM, provenance, signing strategy, and supply-chain controls inside DevOps workflows. Hand off pentesting, SOC/SIEM, threat intelligence, forensics, enterprise GRC, and general security incident response to Cybersecurity.

## Safety

Keep outputs static and evidence-based. Do not request, expose, or commit secrets, tokens, credentials, private keys, real account identifiers, private URLs, or environment-specific values. Require human review for privileged, destructive, costly, externally visible, compliance-sensitive, production-impacting, irreversible, signing, spending, or publication decisions. State when validation is static and no runtime checks were executed.
